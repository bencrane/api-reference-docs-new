# PostHog Web Device Mode Integration

Send events to PostHog using RudderStack web device mode.

* * *

  * __5 minute read

  * 


RudderStack lets you send your event data to PostHog via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

## Prerequisites

  * [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) integrated with your website.
  * An active PostHog account and project.


## Identify

To identify a user in PostHog, use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      first_name: "Alex",
      last_name: "Keener",
      email: "alex@example.com",
      createdAt: "2019-07-23T23:45:56.000Z",
    })
    

When you send an `identify` event, RudderStack checks if `userId` is present. If present, it then calls PostHog’s [Identify API](<https://posthog.com/docs/libraries/js/usage#identifying-users>) and maps `userId` to `distinct_id` in PostHog.

RudderStack also passes the user traits within the `identify` call to PostHog under the `$set` key.

> ![info](/docs/images/info.svg)
> 
> If `userId` is absent, RudderStack does not call PostHog’s Identify API. However, it still processes the super properties from the `integrations` object, if present in the event.

## Track

RudderStack’s [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture the user events along with their associated properties and send this data to PostHog.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "C324532",
      order_id: "T1230",
      revenue: 16.98,
      shipping: 3.0,
      coupon: "FY21",
      currency: "INR",
      products: [
        {
          product_id: "product-mixedfruit-jam",
          sku: "sku-1",
          category: "Food",
          currency: "INR",
          value: 6.0,
          typeOfProduct: "Food",
          url: "https://www.example.com/product/bacon-jam",
          image_url: "https://www.example.com/product/bacon-jam.jpg",
        },
      ],
    })
    

RudderStack sends the `track` events to PostHog via their [Capture endpoint](<https://posthog.com/docs/libraries/js/usage#capturing-events>).

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your app’s page views with any additional relevant information about the viewed page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page({
      path: "/best-seller/1",
      url: "https://www.estore.com/best-seller/1",
      title: "EStore Bestsellers",
      search: "estore bestseller",
      referrer: "https://www.google.com/search?q=estore+bestseller",
    })
    

RudderStack calls `posthog.capture('$pageview')` to send the `page` event to PostHog. It does not pass any page properties (`path`, `url`, `title`, `referrer`, etc.) — PostHog infers the page context from the browser directly, if available.

## Group

Use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to associate an identified user with a group, such as a company, organization, or an account.

> ![warning](/docs/images/warning.svg)
> 
> You must include `groupId` and `groupType` in your `group` calls to create or update the group details in PostHog.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      groupType: "Lead",
      name: "Sample Group",
      total: 100
    });
    

Note that:

  * Pass `name` in the group traits to create a group in PostHog with that name. Otherwise, the group is created by the `groupId`.
  * RudderStack removes the `groupType` field from the traits and passes them to PostHog as the group properties.


In device mode, RudderStack calls the [group analytics](<https://posthog.com/docs/integrate/client/js#group-analytics>) function to create a group in PostHog. It also uses the [PostHog Super Properties](<https://posthog.com/docs/integrate/client/js#super-properties>) to assign the group to an identified user.

The traits mapping is summarized in the following table:

RudderStack group trait| Updated group mapping disabled| Updated group mapping enabled  
---|---|---  
`groupId`  
Required| `groupId`| `$group_key`  
`groupType`  
Required| `groupType`| `$group_type`  
  
## Property mappings

In device mode, RudderStack forwards events as-is to the PostHog SDK. PostHog adds the relevant contextual properties (`$os`, `$current_url`, etc.) via its own SDK.

## Send super properties

For `identify`, `track`, `page`, and `group` events, you can set PostHog [super properties](<https://posthog.com/docs/libraries/js/usage#super-properties>) via the `integrations` object in the event.

> ![info](/docs/images/info.svg)
> 
> Super properties are automatically attached to every subsequent event (for example, `$pageview`, `autocapture`, `capture`, etc.) in that session and persist until removed or the session ends.

To pass the super properties to PostHog, include them in the `integrations.PostHog` object in the event, as shown:
    
    
    rudderanalytics.track('Order Completed', { revenue: 30 }, {
      integrations: {
        PostHog: {
          superProperties: { plan: 'premium' },
          setOnceProperties: { campaign_source: 'twitter' },
          unsetProperties: ['old_prop']
        }
      }
    });
    

The following table lists the available `integrations` options and the corresponding PostHog API endpoints used to set the super properties:

Integration option| PostHog API endpoint| Description  
---|---|---  
`superProperties`| `posthog.register()`| Properties sent with every subsequent event — you can overwrite them in future events  
`setOnceProperties`| `posthog.register_once()`| Properties set only once — they cannot be overwritten if already set  
`unsetProperties`| `posthog.unregister()`| Removes previously-set super properties  
  
#### Why use super properties

Super properties let you attach consistent metadata (for example, plan tier, campaign source, A/B variant) to all events in a session without repeating it in every event.

Some common use cases for super properties are as follows:

Use case| Description  
---|---  
Plan or tier tracking| Set `plan: 'premium'` in the `identify` so all events are tagged with the user’s plan  
Campaign attribution| Set `campaign_source: 'twitter'` once (via `setOnceProperties`) so the first-touch source is stored and not overwritten  
Feature context| Set `feature_flag_variant: 'experiment'` to filter events by feature exposure  
Section or funnel context| Set `section: 'pricing'` when the user enters a pricing flow so all related events are tagged  
Cleanup| Use `unsetProperties` to remove super properties when they are no longer needed (for example, after checkout)  
  
A sample flow is shown below:
    
    
    // User lands from campaign - set once, won't be overwritten
    rudderanalytics.identify('1hKOmRA4GRlm', { email: 'alex@example.com' }, {
      integrations: {
        PostHog: {
          setOnceProperties: { utm_source: 'newsletter', utm_campaign: 'new_year_sale' }
        }
      }
    });
    
    // User upgrades - add plan to all future events
    rudderanalytics.track('Upgrade Completed', { plan: 'pro' }, {
      integrations: {
        PostHog: {
          superProperties: { plan: 'pro' }
        }
      }
    });
    

## FAQ

#### How can I prevent RudderStack from loading the PostHog SDK on my website?

To prevent RudderStack from loading the PostHog SDK on your website, you can [load the JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) as shown:
    
    
    rudderanalytics.load("WRITE_KEY", "DATA_PLANE_URL", {
      integrations: {
        All: true,
        PostHog: {
          loadIntegration: false,
        },
      },
    });
    

#### How do I set the RudderStack event’s `anonymousId` as the PostHog `anonymous_id`?

To set `anonymousId` in your RudderStack event as the PostHog `anonymous_id`, call PostHog’s [`identify` function](<https://posthog.com/docs/data/identify>) using the RudderStack `anonymousId`.