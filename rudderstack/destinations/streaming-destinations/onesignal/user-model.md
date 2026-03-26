# Send Events to OneSignal (User Model)

Send events to OneSignal via the User Model API.

* * *

  * __3 minute read

  * 


After you have successfully instrumented OneSignal as a destination in RudderStack, follow this guide to correctly send your events to OneSignal via their [User Model REST API](<https://documentation.onesignal.com/reference/rest-api-overview>).

Find the open source transformer code for this integration in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/blob/develop/src/v0/destinations/one_signal/transformV2.js>).

## Identify

You can make an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [add a new user](<https://documentation.onesignal.com/docs/users>) to your OneSignal App. If a user is already present with the specified identifier, then RudderStack updates the user properties instead.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
          firstName: 'Alex',
          lastName: 'Keener',
          email: "alex@example.com"
        }, {
          integrations: {
            one_signal: {
              aliases: {
                custom_alias: 'custom_identifier'
              },
    
            }
          }
        });
    

You can send subscription-level details to OneSignal by passing them in the `properties.subscriptions` object, as shown:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      firstName: 'Alex',
      lastName: 'Keener',
      email: "alex@example.com"
      subscriptions: {
        email: { // for email as device_type
          "enabled": true,
          "notification_types": 23,
          "session_time": 20,
          "session_count": 2,
          "app_version": "1.6.7",
          "test_type": 1
        },
        phone: { // for phone as device_type
          "enabled": true,
          "notification_types": 23,
          "session_time": 20,
          "session_count": 2,
          "app_version": "1.6.7",
          "test_type": 1
        },
        iOSPush: { // for device_type fetched from integrations object
          "enabled": true,
          "notification_types": 23,
          "session_time": 20,
          "session_count": 2,
          "app_version": "1.6.7",
          "test_type": 1
        }
      }
    });
    

For email and SMS, enable the **Toggle on to add a device using email** and **Toggle on to add a device using phone number** settings in the RudderStack dashboard and send the relevant data (`email` or `phone`) in the event payload.

### Property mapping

RudderStack maps the following **optional** properties to the corresponding OneSignal fields:

RudderStack property| OneSignal property  
---|---  
`context.os.version`| `subscriptions.$.device_os`  
`context. timezone`| `properties.timezone_id`  
`context.locale`| `properties.language`  
`traits.address.country`| `properties.country`  
`traits.createdAt`  
`context.traits.createdAt`  
`timestamp`  
`originalTimestamp`| `created_at`  
`traits.createdAt`  
`context.traits.createdAt`  
`timestamp`  
`originalTimestamp`| `properties.last_active`  
`traits.first_active`  
`context.traits.first_active`| `properties.first_active`  
`userId`| `identity.external_id`  
  
Note the following:

  * RudderStack maps all the `string` key-value pairs from `traits` inside the `tags` object as it is.

  * For mobile channels:

    * RudderStack maps `context.device.type` to `subscription.$.type`.
    * It also maps `context.device.token` or `context.device.id` to OneSignal’s `subscriptions.$.token` field.
  * For web channels:

    * RudderStack maps `<browser_name>_Push` (depending on the browser) to `subscription.$.type`.
    * Also, it maps the event’s `anonymousId` to OneSignal’s `subscription.$.token`. However, you can override this mapping by passing the `deviceType` field or in the `integrations` object. See the [OneSignal documentation](<https://documentation.onesignal.com/reference/create-subscription#:~:text=Application%20ID%20%28UUID%29-,type,-string>) for more information on the supported device types.


## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [update an existing user’s tags](<https://documentation.onesignal.com/reference/update-user>) in your OneSignal app using the external user ID.

> ![warning](/docs/images/warning.svg)
> 
> You must associate the external user ID with a single user only.

While updating a tag, you can delete any key inside a tag by providing the key value as an empty string.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Add to cart', {
      purchased_item: "Shirt",
      brand: "Zara"
    }, {
      integrations: {
        one_signal: {
          aliases: {
            custom_alias: 'custom_alias_identifier'
          },
        }
      }
    });
    

### Property mapping

RudderStack maps the following properties to the corresponding OneSignal properties:

RudderStack property| OneSignal property  
---|---  
`userId`  
`one_signal.aliases`  
Any one of the above is required| `external_id`  
  
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
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `groupId` is a required field to send `group` events to OneSignal.
>   * RudderStack maps all properties added in the **Allowed Property List** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal/setup-guide/#connection-settings>) to the `tags` object if they are present in the payload. However, note that the key-value pair should be of the String data type only.
>