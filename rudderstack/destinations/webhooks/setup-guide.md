# Setup Guide

Set up and configure a webhook destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up a webhook destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to your webhook destination.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Webhook** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Webhook**.

Assign a name to uniquely identify your destination in the RudderStack dashboard and click **Continue**.

### Connection settings

Setting| Description  
---|---  
Webhook URL| Specify the endpoint where RudderStack sends the events. RudderStack supports both `HTTP` and `HTTPS` URLs.  
  
**Note** : For successful event delivery in case of an `HTTPS` URL, you must have a **valid TLS certificate**.  
URL Method| Select the HTTP method of the request sent to the configured endpoint from the dropdown. By default, RudderStack uses the `POST` method to send the events.  
Headers| Add custom headers for your events. RudderStack stringifies (for non-string data types) and adds these headers to the request made to your webhook.  
  
**Note** : RudderStack adds the below headers for the `POST` and `PUT` requests by default:  
  
| Key| Value  
---|---  
`user-agent`| `RudderLabs`  
`content-type`| `application/json`  
See the below sections for more information:  
  


  * Set non-string data types as headers
  * Add a dynamic header to your events
  * Add a dynamic path to your base URL

  
  
### Configuration settings

Configure the below settings to receive your data correctly in your webhook destination.

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Set non-string data types as headers

RudderStack supports defining non-string data types (like Boolean, object, array, etc.) as headers while setting up your webhook destination. RudderStack automatically stringifies these data types before setting the header.

For example, if you set the headers as shown:

[![Webhook configuration](/docs/images/releases/webhook-headers.webp)](</docs/images/releases/webhook-headers.webp>)

In this case, RudderStack automatically stringifies and sets the below headers in the transformed payload before sending it to the specified webhook URL:
    
    
    "headers": {
        "key1": "null",
        "key2": "{\"key1\":\"\"}",
        "key3": "true",
    }
    

## Add dynamic header to events

RudderStack provides a [transformation template](<https://www.rudderstack.com/docs/transformations/templates/#dynamic-headers>) for cases where you need to dynamically change or add a header to the webhook, as shown:
    
    
    export function transformEvent(event, metadata) {
      event.header = {
        Authorization: "Basic <credentials>",  // Change headers and values
        header_2: "<value>"
      };
      return event;
    }
    

The following snippet highlights a sample event payload with a dynamic header:
    
    
    {
      event: "Product Viewed",
      type: "track",
      properties: {
        color: "blue",
        number: 3,
        newMember: true
      },
      header: {
        "Authorization": "Bearer 3841718412jhcdskc"
      }
    }
    

## Add dynamic path to base URL

> ![success](/docs/images/tick.svg)
> 
> This feature is helpful in cases where you need to change the webhook endpoint depending on a certain condition.

RudderStack provides a [transformation template](<https://www.rudderstack.com/docs/transformations/templates/#dynamic-path>) for cases where you need to add a dynamic path to your base webhook URL.

For example, if the webhook URL configured in the RudderStack dashboard is `https://www.example.com/`, you can append a string `/search?email=${email}` to it depending on the `email` property present in your event:
    
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email; // Change property
      if (email) event.appendPath = `/search?email=${email}`; // Change property and appendPath
      return event;
    }
    

In this case, the final webhook URL endpoint where RudderStack sends the event becomes `https://www.example.com/search?email=${email}`.

## FAQ

#### How do I check for delivery failures while sending events to the webhook destination?

Log in to your [RudderStack dashboard](<https://app.rudderstack.com>) and go to the **Live Events** tab of your destination to check for any delivery failures. In case there are any, you can check the **Error Response** by clicking the event to get more details.

## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/webhooks/cloud-mode/>)