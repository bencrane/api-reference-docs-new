# PostHog Cloud Mode Integration

Send events to PostHog using RudderStack cloud mode.

* * *

  * __4 minute read

  * 


RudderStack lets you send your event data to PostHog via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/posthog>).

## Identify

You can use RudderStack’s [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in PostHog.

A sample `identify` call is as shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      first_name: "Alex",
      last_name: "Keener",
      email: "alex@example.com",
      createdAt: "2019-07-23T23:45:56.000Z",
    })
    

RudderStack passes the user traits within the `identify` call to PostHog under the `$set` key according to the [PostHog Identify API](<https://posthog.com/docs/api/post-only-endpoints#identify>).

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
    

PostHog supports the RudderStack `track` call as type `capture.` and sends the user action as an event to PostHog according to the [PostHog Capture API](<https://posthog.com/docs/api/post-only-endpoints#capture>).

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
    

In the above example, RudderStack captures information related to the viewed page such as its path, URL, referrer, etc.

For the `page` call, RudderStack sends `$pageview` as an event to PostHog according to the [PostHog Page API](<https://posthog.com/docs/api/post-only-endpoints#page>).

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen with any additional relevant information about the screen.

A sample `screen` call using RudderStack’s iOS (Obj-C) SDK is shown below:
    
    
    [[RudderClient sharedInstance] screen:@"Home Screen"
                properties:@{@"category" : @"launcher"}];
    

In the above snippet, RudderStack captures information related to the viewed screen such as its name and category.

For the `screen` call, RudderStack sends `$screen` as an event to PostHog according to the [PostHog Screen API](<https://posthog.com/docs/api/post-only-endpoints#screen>).

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to associate an identified user with a group, such as a company, organization, or an account.

> ![info](/docs/images/info.svg)
> 
> It is highly recommended to include `groupId` and `groupType` in your `group` calls to create or update the group details.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      groupType: "Lead",
      name: "Sample Group",
      total: 100
    });
    

> ![info](/docs/images/info.svg)
> 
> If you pass the `name` in the group `traits`, then the group is created in PostHog with that `name`. Otherwise, it is created by the `groupId` (if present).

For the `group` call, RudderStack sends `$groupidentify` as an event to PostHog according to the [PostHog Group API](<https://posthog.com/docs/api/post-only-endpoints#group>).

### Updated group mapping

RudderStack lets you use the updated mapping feature for the `group` calls where it maps the group traits as event properties before sending them to PostHog. To use this feature, enable the **Use Updated Mapping for Group calls** setting in the RudderStack dashboard:

[![PostHog group mapping setting](/docs/images/event-stream-destinations/posthog-updated-group-mapping.webp)](</docs/images/event-stream-destinations/posthog-updated-group-mapping.webp>)

By default, the **Use Updated Mapping for Group calls** setting is disabled in the dashboard. In this case, RudderStack sends the group traits to PostHog as received without any modification, as shown in the following snippet:
    
    
    {
      "version": "1",
      "type": "REST",
      "method": "POST",
      "endpoint": "https://app.posthog.com/batch",
      "headers": {
        "Content-Type": "application/json"
      },
      "params": {},
      "body": {
        "JSON": {
          "groupId": "groupId27",
          "distinct_id": "sampleusrRudder7",
          "traits": {
            "groupType": "company",
            "KEY_3": {
              "CHILD_KEY_92": "value_95",
              "CHILD_KEY_102": "value_103"
            },
            "name_trait": "Company",
            "value_trait": "Company-ABC"
          },
          "messageId": "e5034df0-a404-47b4-a463-76df99934fea",
          "event": "$group",
          "api_key": "<API_KEY>",
          "type": "group"
        },
      },
    }
    

When **Use Updated Mapping for Group calls** is enabled in the dashboard, RudderStack sends the group traits as event properties to PostHog:
    
    
    {
      "version": "1",
      "type": "REST",
      "method": "POST",
      "endpoint": "https://app.posthog.com/batch",
      "headers": {
        "Content-Type": "application/json"
      },
      "params": {},
      "body": {
        "JSON": {
          "distinct_id": "sampleusrRudder7",
          "messageId": "e5034df0-a404-47b4-a463-76df99934fea",
          "properties": {
            "$group_key": "groupId27",
            "$group_type": "company",
            "$group_set": {
              "KEY_3": {
                "CHILD_KEY_92": "value_95",
                "CHILD_KEY_102": "value_103"
              },
              "name_trait": "Company",
              "value_trait": "Comapny-ABC"
            },
          },
          "event": "$group",
          "api_key": "<API_KEY>",
          "type": "group"
        },
      },
    }
    

The mapping is summarized in the following table:

RudderStack group trait| Updated group mapping disabled| Updated group mapping enabled  
---|---|---  
`groupId`| `groupId`| `$group_key`  
`groupType`| `groupType`| `$group_type`  
`traits`| `traits`| `$group_set`  
  
## Alias

Calling [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) passes `userId` and `previousId` to the PostHog queue.

A sample `alias` call in RudderStack is as shown:
    
    
    rudderanalytics.alias("user01", "previous01")
    

In the above example, `previous01` gets mapped to `distinct id` in PostHog, while `user01` gets mapped to `alias` in PostHog.

For the `alias` call, RudderStack sends `$create_alias` as an event to PostHog according to [PostHog Alias API](<https://posthog.com/docs/api/post-only-endpoints#alias>).

## Property mappings

RudderStack also maps the following properties to the PostHog standard contextual properties:

RudderStack field| PostHog field  
---|---  
`context.os.name`| `$os`  
`context.page.url`| `$current_url`  
`url`| `$host`  
`context.page.path`| `$pathname`  
`context.screen.height`| `$screen_height`  
`context.screen.width`| `$screen_width`  
`context.library.name`| `$lib`  
`context.library.version`| `$lib_version`  
`timestamp`  
`originalTimestamp`| `$time`  
`context.device.id`| `$device_id`  
`request_ip`  
`context.ip`| `$ip`  
`timestamp`  
`originalTimestamp`| `$timestamp`  
`anonymousId`| `$anon_distinct_id`  
`userId`  
`anonymousId`| `distinct_id`  
`context.screen.density`| `$screen_density`  
`context.device.manufacturer`| `$device_manufacturer`  
`context.os.version`| `$os_version`  
`context.timezone`| `$timezone`  
`context.locale`| `$locale`  
`context.userAgent`| `$useragent`  
`context.app.version`| `$app_version`  
`context.device.name`| `$device_name`  
`context.network.carrier`| `$network_carrier`  
`context.app.name`| `$app_name`  
`context.device.model`| `$device_model`  
`context.app.namespace`| `$app_namespace`  
`context.app.build`| `$app_build`  
`properties.viewport_height`| `$viewport_height`  
`properties.viewport_width`| `$viewport_width`  
`context.page.loaded`| `$performance_page_loaded`  
`context.campaign.source`| `utm_source`  
`context.campaign.medium`| `utm_medium`  
`context.campaign.name`| `utm_campaign`  
`context.campaign.content`| `utm_content`  
`context.campaign.term`| `utm_term`