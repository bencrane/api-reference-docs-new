# Adjust Cloud Mode Integration

Send events to Adjust in RudderStack cloud mode.

* * *

  * __4 minute read

  * 


After you have [successfully instrumented](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/>) Adjust as a destination in RudderStack, follow this guide to correctly send your events to Adjust in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/adj>).

## Supported events

In cloud mode, RudderStack supports sending the following events to Adjust:

  * [Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>)


> ![info](/docs/images/info.svg)
> 
> RudderStack does not support [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) events in the cloud mode integration — these events are only available in device mode.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record user actions along with any properties associated with them.

When you make a `track` call, RudderStack maps the event name with the corresponding Adjust custom event using Adjust’s server-to-server event endpoint.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to define the event mapping in the [**Map events to Adjust Event Tokens**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) dashboard setting. Adjust will reject any events apart from these mappings.
> 
> You must [create the event token in the Adjust dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#how-can-i-create-a-new-event-token-in-adjust>) before specifying the mappings.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Purchased", {
      revenue: 20.99,
      currency: "USD",
      quantity: 10
    });
    

### Callback parameters

RudderStack sends all custom properties in your `track` calls as [callback parameters](<https://dev.adjust.com/en/sdk/ios/v4/features/session-parameters/>) to Adjust. However, `revenue` and `currency` are excluded from callback parameters as they’re handled separately.

### Partner parameters

You can also send custom properties in your `track` calls as [partner parameters](<https://dev.adjust.com/en/sdk/adobe-extension/ios/global-parameters/>) to Adjust. Adjust then sends those parameters to the external partners you have set up in your Adjust dashboard. See the [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/#how-can-i-set-up-new-partners-in-adjust>) for more information on adding a partner in Adjust.

RudderStack uses the property mappings specified in the [**RudderStack Parameters to Partner Parameters**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) dashboard setting to check if a key is present in the `track` event properties and maps it to the corresponding Adjust partner parameter object.

> ![warning](/docs/images/warning.svg)
> 
>   * Adjust will reject any properties apart from mappings specified in the **RudderStack Parameters to Partner Parameters** dashboard setting.
>   * The partner parameters only accept the String data type. RudderStack automatically converts numeric values into strings before sending the data to Adjust.
> 


Suppose you set the following mappings in the RudderStack dashboard:

RudderStack property| Adjust partner parameter  
---|---  
`revenue`| `price`  
`quantity`| `quantity`  
  
A sample `track` call with the above properties is shown below:
    
    
    rudderanalytics.track("purchase", {
      revenue: 20.99,
      currency: "USD",
      quantity: 10
    });
    

The corresponding Adjust payload highlighting the parameters is shown below:
    
    
    {
      "params": {
        "android_id": "3f034872-5e28-45a1-9eda-ce22a3e36d1a",
        "gps_adid": "3f034872-5e28-45a1-9eda-ce22a3e36d1a",
        "att_status": 3,
        "tracking_enabled": true,
        "currency": "USD",
        "ip_address": "[::1]",
        "s2s": 1,
        "app_token": "t1yurrb968zk",
        "event_token": "tf4gm5",
        "environment": "production",
        "partner_params": {
          "price": "20.99",
          "quantity": "10"
        }
      }
    }
    

### Revenue tracking

To send [revenue tracking](<https://help.adjust.com/en/article/record-events-ios-sdk#record-event-revenue>) events to Adjust, add `revenue` and `currency` to your event properties:
    
    
    rudderanalytics.track("purchase", {
      revenue: 2.99,
      currency: "USD"
    });
    

If you don’t specify the `currency` property, RudderStack defaults to `USD`.

## Device requirements

For cloud mode to work correctly, your events must include the following device information:

  * **Device type** : Must be either `android` or an Apple family device (iOS, iPadOS, etc.)
  * **Device ID** : Required for identifying the device
  * **Advertising ID** : Optional but recommended for better attribution


## Property mapping

The following table highlights the mapping between RudderStack fields and Adjust parameters:

RudderStack property| Adjust parameter| Description  
---|---|---  
`context.device.type`  
Required| Platform detection| Must be `android` or Apple family device (for example, `iOS`)  
`context.device.id`  
Required| `android_id` (Android)  
`idfv` (Apple)| Device identifier for attribution  
`context.device.advertisingId`| `gps_adid` (Android)  
`idfa` (Apple)| Advertising ID for better attribution  
`context.device.attTrackingStatus`| `att_status`| App Tracking Transparency status  
`context.device.adTrackingEnabled`| `tracking_enabled`| Ad tracking enabled status  
`context.ip` or `request_ip`| `ip_address`| IP address for geo-targeting  
`properties.revenue`| `revenue`| Revenue amount for purchase events  
`properties.currency`| `currency`| Currency code (defaults to `USD`)  
`properties.*`| `callback_params`| All other properties as callback parameters  
`properties.*` (mapped)| `partner_params`| Mapped properties as partner parameters  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `revenue` and `currency` are excluded from `callback_params` as they’re handled separately.
>   * Partner parameters only accept String data type — RudderStack automatically converts numeric values to strings before sending them to Adjust.
> 


## Troubleshooting

Issue| Resolution  
---|---  
Events failing with “Device type/id not present” error| Verify that you’re providing the `type` and `id` in the `context.device` field.  
Events not appearing in Adjust dashboard| 

  * Verify that your event is mapped to an Adjust event token in the [dashboard settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).
  * Check that the event token exists in your Adjust dashboard.
  * Ensure your **App Token** is correctly configured.