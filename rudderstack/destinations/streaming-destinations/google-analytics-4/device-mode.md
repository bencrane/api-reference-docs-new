# Google Analytics 4 Web Device Mode Integration

Send events to Google Analytics 4 using RudderStack web device mode.

* * *

  * __5 minute read

  * 


RudderStack lets you send your event data to Google Analytics 4 destination via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK, using the `gtag` tagging method.

> ![info](/docs/images/info.svg)
> 
> You need to select `gtag.js` as the **Client Type** and enable **Use device-mode to send events** in the RudderStack dashboard to send events via device mode. For more information on device mode settings in the RudderStack dashboard, see [Setting up Google Analytics 4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/setup-guide/>) guide.

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/GA4>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

User-ID is an advanced feature that lets GA4 present a cross-device, cross-platform view of your customers’ behavior. Google Analytics 4 uses `userId` and `deviceId` (GA’s `cid` value from Universal Analytics terminology) to identify users.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

In the above snippet, the `userId` is set to `1hKOmRA4el9Zt1WSfVJIVo4GRlm` and the `name` and `email` is set as `user_properties`.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

Google Analytics 4 `gtag` sends a `page_view` event to Google Analytics by default every-time it is loaded. You can also send `page_view` event to Google Analytics whenever you make an explicit `page()` call to RudderStack SDK.

RudderStack sends the following properties by default:

  * `url` mapped to `page_location`
  * `title` mapped to `page_title`
  * `referrer` mapped to `page_referrer`


You can also make `page()` call with any custom and standard properties as shown below:
    
    
    rudderanalytics.page({
      path: "/test_browser.html",
      url: "http://example.com/test_browser.html?param1=true",
      title: "Page Load",
      search: "?param1=true",
      referrer: "referrer",
    })
    

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Track me")
    

RudderStack SDK sends the track event name and any properties as custom properties to Google Analytics 4.

> ![info](/docs/images/info.svg)
> 
> RudderStack SDK flattens the properties that are nested and not standard Google Analytics 4 properties before sending them to Google Analytics.

> ![info](/docs/images/info.svg)
> 
> There are limits on the number of custom properties per event that can be sent to Google Analytics 4. The RudderStack SDK **does not drop** the payload based on these limits. If the events are don’t show up in the debug view or in the Google Analytics dashboard reports, refer to the [Google support page](<https://support.google.com/analytics/answer/9267744?hl=en>) to learn more about the collection limits.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group such as a company, organization, or an account, and record any traits associated with that group, for example, company name, number of employees, etc.

RudderStack maps the `group` call to the `join_group` event by default.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("1hKOmRA4", {
        "custom1": 1234,
        "custom2": "custom2"
    });
    

## Ecommerce events tracking

RudderStack supports ecommerce tracking for Google Analytics 4. Use the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for sending events while instrumenting your site with the RudderStack SDK.

Below are some examples of the track event names that are passed to Google Analytics 4-specific ecommerce event name:

RudderStack event name| Google Analytics 4 event name  
---|---  
Products Searched| `search`  
Product List Viewed| `view_item_list`  
Promotion Viewed| `view_promotion`  
Product Clicked| `select_item`  
Product Added To Wishlist| `add_to_wishlist`  
Product Added| `add_to_cart`  
Cart Shared| `share`  
Checkout Started| `begin_checkout`  
Order Completed| `purchase`  
  
> ![info](/docs/images/info.svg)
> 
> For each product in the order, there must be an `id` and `name` associated with it. Refer to the [GA4 documentation](<https://developers.google.com/gtagjs/reference/ga4-events#view_item_list>) for more information on ecommerce events and corresponding properties.

## Debug mode

RudderStack sends all the device mode events with a `debug_mode` parameter so that you can view them in the [DebugView](<https://support.google.com/analytics/answer/7201382>).

## FAQ

#### How can I disable sending `userId` to GA4?

You can disable sending `userId` to GA4 by [passing an `integrations` object](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>) in your JavaScript SDK load options and setting `sendUserId` to `false`.
    
    
    rudderanalytics.load(
      "WRITE_KEY",
      "DATA_PLANE_URL", {
        integrations: {
          All: true,
          "Google Analytics 4": {
            sendUserId: false
          },
        }
      }
    )
    

> ![warning](/docs/images/warning.svg)
> 
> If you set `sendUserId` to `false`, RudderStack will not send `userId` to GA4 in any of the events.

#### How can I enable Google Signals in GA4?

[Google Signals](<https://support.google.com/analytics/answer/9445345?hl=en#zippy=%2Cin-this-article>) helps you understand the interaction of users with your website across multiple devices and sessions. To enable Google Signals and capture user data, the following conditions must be met:

  * A user must be signed in to their Google Account on the website or app.
  * Ad Personalization must be enabled for their account.


> ![info](/docs/images/info.svg)
> 
> The Google Signals feature is available in the web [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) only.

To enable Google Signals in GA4 and reflect the collected user data in your reports, follow the steps below:

  1. Log into your [Google Analytics dashboard](<https://analytics.google.com/>).

  2. Open the Admin panel by clicking on the gear icon at the bottom left.[![Google Signals](/docs/images/event-stream-destinations/Google-signals-1.webp)](</docs/images/event-stream-destinations/Google-signals-1.webp>)

  3. Select the property for which you want to enable Google Signals. Then, go to **Data Settings** > **Data Collection**.

  4. Click **Get Started** in the **Google signals data collection** section:[![Google Signals](/docs/images/event-stream-destinations/Google-signals-2.webp)](</docs/images/event-stream-destinations/Google-signals-2.webp>)

  5. Click **Continue**.[![Google Signals](/docs/images/event-stream-destinations/Google-signals-3.webp)](</docs/images/event-stream-destinations/Google-signals-3.webp>)

  6. Read the additional information and click **Activate**.[![Google Signals](/docs/images/event-stream-destinations/Google-signals-4.webp)](</docs/images/event-stream-destinations/Google-signals-4.webp>)


Google Signals is now enabled. You will be able to see the **Age** , **Gender** , and other relevant data in the GA4 Demographics reports after 24 hours.