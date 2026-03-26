# Google Ads (gtag.js) Web Device Mode Integration

Send events to Google Ads using RudderStack web device mode.

* * *

  * __3 minute read

  * 


This guide will help you send conversion events to Google Ads in the [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

> ![info](/docs/images/info.svg)
> 
> This integration leverages the [`gtag.js`](<https://developers.google.com/tag-platform/gtagjs>) global site tag - a JavaScript tagging framework that lets you send your event data to Google Ads.

## Identify

> ![warning](/docs/images/warning.svg)
> 
> Before sending the `identify` events to Google Ads, make sure to:
> 
>   * Set up and enable [enhanced conversions for web](<https://support.google.com/google-ads/answer/13258081#zippy=%2Cvalidate-your-implementation-using-chrome-developer-tools%2Cfind-enhanced-conversions-fields-on-your-conversion-page>).
>   * Turn on the **Allow identify calls for the Google Ads destination** [connection setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/setup-guide/#connection-settings>) in the RudderStack dashboard.
> 


Use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send `user_data` to Google Ads for [enhanced conversions](<https://support.google.com/google-ads/answer/9888656>).

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      firstName: "Alex",
      lastName: "Keener",
      email: "alex@example.com",
      phone: "(800) 555‑0175",
    })
    

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can send a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call with the conversion name and specify it in the **Click Event Conversion** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/setup-guide/#click-event-conversion-settings>). RudderStack, in turn, sends this data to Google Ads.

RudderStack maps `properties.currency`, `properties.order_id`, and `properties.revenue` in the event to Google Ads’ `currency`, `transaction_id`, and `value` fields respectively. Note that this is applicable only when the **Track Dynamic Remarketing** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/setup-guide/#track-event-settings>) is turned off.

A sample `track` call is as shown:
    
    
    rudderanalytics.track('track conversion', {
      revenue: 125,
      currency: 'INR',
      order_id: 'order_1'
    });
    

A sample `track` call after turning on the **Track Dynamic Remarketing** setting in the dashboard is shown below:
    
    
    rudderanalytics.track('view_item', {
      'value': 998.55,
      'items': [{
          'id': 1234,
          'google_business_vertical': 'retail'
        },
        {
          'id': 45678,
          'google_business_vertical': 'retail'
        }
      ]
    });
    

> ![info](/docs/images/info.svg)
> 
> The format for passing the parameters is quite flexible. You can use the standard Google format for tracking specific categories or use your own format for tracking custom categories.

A sample `track` call for a custom event is shown below:
    
    
    rudderanalytics.track("custom_event", {
      custom_parameter1: "1",
      custom_parameter2: 2,
    });
    

### Set up new customer acquisition reporting

RudderStack supports sending a `newCustomer` property in your `track` events to determine whether a converting user is a new customer in your Google Ads campaign. This is helpful in [setting up new customer acquisition reporting](<https://support.google.com/google-ads/answer/12077475?hl=en#zippy=%2Cinstall-with-the-global-site-tag%2Cinstall-with-google-tag-manager>) in Google Ads.

> ![warning](/docs/images/warning.svg)
> 
> Do not pass the `newCustomer` property if you are unsure about the converting the user status (applicable for new and existing customers).

A sample `track` call highlighting this feature is shown:
    
    
    rudderanalytics.track('Order Completed', {
      'newCustomer': false,
      'currency': 'USD',
      'price': 43.99,
      'transaction_id': 'A122311',
      "checkout_id": "CHK1044",
      "revenue": 47.99,
      "products": [{
        "product_id": "A1223",
        "name": "car"
      }]
    });
    

## Page

You can make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call with the conversion name to RudderStack for a page load conversion. RudderStack, in turn, sends this data to Google Ads.

A sample `page` call is as shown below:
    
    
    rudderanalytics.page('page view');
    

You can turn on **Track Dynamic Remarketing** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/setup-guide/#track-event-settings>) to send custom parameters in the `page` call:
    
    
    rudderanalytics.page("custom_event", {
      custom_parameter1: "Sample",
      custom_parameter2: 2,
    });