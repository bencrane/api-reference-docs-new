# Send Events to OneSignal (Device Model)

Send events to OneSignal via the Device Model API.

* * *

  * __3 minute read

  * 


After you have successfully instrumented OneSignal as a destination in RudderStack, follow this guide to correctly send your events to OneSignal via their Device Model.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/one_signal>).

> ![danger](/docs/images/danger.svg)
> 
> OneSignal device model is deprecated. RudderStack recommends sending events to OneSignal via their [User Model API](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/user-model/>).
> 
> See the [OneSignal documentation](<https://documentation.onesignal.com/docs/user-model-migration-guide>) for more information.

## Identify

You can make an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [add a new device](<https://documentation.onesignal.com/reference/add-a-device>) to your OneSignal App. If a device is already registered with the specified identifier, then RudderStack updates the device records.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify('1hKOmRA4eGRlm', {
      firstName: 'Alex',
      lastName: 'Keener',
      email: "alex@example.com"
    }, {
      externalId: [{
        type: "playerId",
        id: "Df344sdFgdDsS4"
      }],
      integrations: {
        oneSignal: {
          deviceType: "6",
          identifier: "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
        }
      }
    });
    

In the above snippet, the `playerId` is the unique ID for a device. If `playerId` is provided in `externalId`, RudderStack updates the device having `playerId`. Note that for correct mapping, you must include `externalId` in your event in the exact format as shown above.

> ![info](/docs/images/info.svg)
> 
> RudderStack adds the `anonymousId` as a tag with the key as `anonymousId` along with the corresponding value.

RudderStack maps the following browser and mobile device types by default:
    
    
    deviceTypeMapping = {
        android: 1,
        ios: 0,
        chrome: 5,
        safari: 7,
        firefox: 8
    }
    

You can override the above device type mappings or set any other device type by providing the `deviceType` and `identifier` in the `integrations` object:
    
    
    "integrations": {
      "one_signal": {
        "deviceType": "Sample device",
        "identifier": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"
      }
    }
    

For email and SMS, you can enable the **Toggle on to add a device using email** and **Toggle on to add a device using phone number** dashboard settings and send the relevant data (`email` or `phone`) in your events.

### Property mapping

RudderStack maps the following **optional** properties to the corresponding OneSignal fields:

RudderStack property| OneSignal property  
---|---  
`context.device.model`| `device_model`  
`context.os.version`| `device_os`  
`context.timezone`| `timezone`  
`userId`| `external_user_id`  
`context.locale`| `language`  
`traits.createdAt`  
`context.traits.createdAt`  
`timestamp`  
`originalTimestamp`| `created_at`  
`last_active`  
`traits.country`  
`context.traits.country`  
`traits.address.country`  
`context.traits.address.country`| `country`  
`integrations.one_signal.deviceType`| `device_type`  
`integrations.one_signal.identifier`| `identifier`  
  
Note the following:

  * RudderStack maps all the `string` key-value pairs from `traits` in the `tags` object as is.

  * For browsers:

    * RudderStack checks the browser name in `deviceTypeMapping` and maps it to OneSignal’s `device_type` property.
    * It also sets the `anonymousId` as the `identifier` depending on the browser name.
  * For iOS and Android:

    * RudderStack collects the `context.device.type` field and maps it to OneSignal’s `device_type` property.
    * It also sets the `context.device.token`/`context.device.id` as the `identifier`.


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends sending the `device.token` property for push notifications.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to update an existing device’s tags in your OneSignal apps using the `external_user_id` parameter. All devices containing the particular `external_user_id` are updated simultaneously.

> ![info](/docs/images/info.svg)
> 
> To update the device tags using `external_user_id`, you must first identify the device using the `identify` call.

While updating a device tag, you can delete any key inside a tag by providing the key value as an empty string.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Add to cart', {
        purchased_item: "Shirt",
        brand: "Adidas"
    });
    

### Property mapping

RudderStack maps the following properties to the corresponding OneSignal properties:

RudderStack property| OneSignal property  
---|---  
`userId`  
Required| `external_user_id`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack maps all properties added in the **Allowed Property List** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/setup-guide/#connection-settings>) to the `tags` object if they are present in the payload. However, note that the key-value pair should be of the String data type only.

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to group the devices with the device tags having the same `groupId`.

A sample `group` call is as shown:
    
    
    rudderanalytics.group('1hKOmRA4GRlm', {
      name: "Apple Inc.",
      location: "USA",
    });
    

### Property mapping

The following table details the mappings between RudderStack and OneSignal properties:

RudderStack property| OneSignal property| Presence  
---|---|---  
`groupId`| `groupId`| Required  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack maps all properties added in the **Allowed Property List** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/setup-guide/#connection-settings>) to the `tags` object if they are present in the payload. However, note that the key-value pair should be of the String data type only.