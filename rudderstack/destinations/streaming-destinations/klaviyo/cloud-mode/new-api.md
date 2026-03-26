# Klaviyo Cloud Mode Integration (New API)

Send events to Klaviyo via RudderStack cloud mode using the API v2024-10-15.

* * *

  * __7 minute read

  * 


After you have successfully instrumented Klaviyo as a destination in RudderStack, follow this guide to correctly send your events to Klaviyo in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using the [API v2024-10-15](<https://developers.klaviyo.com/en/v2024-10-15/reference/api_overview>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [create](<https://developers.klaviyo.com/en/v2024-10-15/reference/create_profile>) or [update](<https://developers.klaviyo.com/en/v2024-10-15/reference/update_profile>) a profile in Klaviyo.

A sample `identify` event payload sent to Klaviyo is shown:
    
    
    {
      "type": "identify",
      "sentAt": "2021-01-03T17:02:53.195Z",
      "userId": "1hKOmRA4el9Z",
      "rudderId": "w226lhkncvr182fc1ywq4xdo457min899rva",
      "messageId": "t7z7ods5xkzgqg5m3a9r3104jyele9aogx9f",
      "context": {
        "externalId": [
          {
            "type": "klaviyo-profileId",
            "id": "klaviyoID"
          }
        ],
        "traits": {
          "firstName": "Alex",
          "lastName": "Keener",
          "email": "alex@example.com",
          "phone": "+12 345 578 900",
          "title": "Developer",
          "organization": "Example Co.",
          "city": "New Orleans",
          "region": "Louisiana",
          "country": "US",
          "zip": "100-0001",
          "Flagged": false,
          "Residence": "31, North Avenue",
          "street": "Blue Gum Street",
          "properties": {
            "listId": "XUepkK",
            "subscribe": true,
            "consent": [
              "email",
              "sms"
            ]
          }
        }
      },
      "anonymousId": "97c46c81-3140-456d-b2a9-690d70aaca35",
      "originalTimestamp": "2021-01-03T17:02:53.193Z"
    }
    

Note that specifying `consent` in the event’s `properties` object (seen above) overrides the [consent settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/setup-guide/#configuration-settings>) configured in the RudderStack dashboard.

### Subscribe or unsubscribe users

  * Set `traits.properties.subscribe` to `true` for subscribing users to the `listId` passed in the event (in `traits.properties.listId`) or in the [RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/setup-guide/#configuration-settings>). RudderStack uses the [Subscribe Profiles API](<https://developers.klaviyo.com/en/v2024-10-15/reference/bulk_subscribe_profiles>) to subscribe the profile the list.
  * Set `traits.properties.subscribe` flag to `false` for unsubscribing the user from the list by leveraging the [Unsubscribe Profiles API](<https://developers.klaviyo.com/en/v2024-10-15/reference/bulk_unsubscribe_profiles>). RudderStack requires either of the `email` or `phone_number` fields (depending on the user’s subscription) in the event for unsubscribing.


> ![info](/docs/images/info.svg)
> 
> Klaviyo doesn’t support specifying the Klaviyo profile ID to unsubscribe a user. Also, it removes all the relative consents.

### Supported mappings

This section lists the mappings between RudderStack and Klaviyo fields for the `identify` event.

#### Top level mappings

RudderStack property| Klaviyo property| Note  
---|---|---  
`id` in the `externalId` array, where `type` is set to `klaviyo-profileId`. For example:  
  

    
    
    “context”: {  
      “externalId”: [  
        {  
          “type”: “klaviyo-profileId”,  
          “id”: “some_id”  
        }  
      ]  
    }

| `data.id`| Alphanumeric string.  
  
This field uniquely identifies the Klaviyo profile to update. If not explicitly provided, RudderStack creates/updates the Klaviyo profile based on the `userId`/`email`/`phone` match.  
  
See User attributes mapping section below for more information on how RudderStack maps these fields.  
-| `data.type`| Automatically set to `profile`.  
  
#### Traits mappings

**User attributes mapping**  


RudderStack maps the following fields within the [`data.attributes`](<https://developers.klaviyo.com/en/reference/create_or_update_profile#:~:text=Generated%20by%20Klaviyo.-,attributes,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
`context.traits.email`  
`traits.email`| `email`| Email format  
`context.traits.phone`  
`traits.phone`| `phone_number`| Must be a valid [E.164 format phone number](<https://developers.klaviyo.com/en/v2024-10-15/reference/events_api_overview#receiving-a-400>). Otherwise, the event will fail.  
`userId`  
`context.traits.userId`  
`traits.userId`| `external_id`| String data type  
`anonymousId`| `anonymous_id`| String data type  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `first_name`| String data type  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `last_name`| String data type  
`context.traits.title`  
`traits.title`| `title`| Individual’s job title  
  
String data type  
`context.traits.organization`  
`traits.organization`| `organization`| String data type  
`context.traits.image`  
`traits.image`| `image`| URL format  
`context.traits._kx`  
`traits._kx`| `_kx`| Also known as the `exchange_id`, this is an encrypted identifier used for identifying a profile by Klaviyo’s web tracking.  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack maps the custom properties for the user profile (of string data type) to Klaviyo’s [`data.attributes.properties`](<https://developers.klaviyo.com/en/reference/create_or_update_profile#:~:text=LOCATION%20OBJECT-,properties,-object>) object in a key-value format.

**Location attributes mapping**  


RudderStack maps the following fields within the [`data.attributes.location`](<https://developers.klaviyo.com/en/reference/create_or_update_profile#:~:text=photo%2D3760854.jpeg-,location,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
`traits.street`  
`traits.address.street`  
`context.traits.street`  
`context.traits.address.street`  
`properties.street`| `address1`| String data type  
`context.traits.address.city`  
`traits.address.city`| `city`| String data type  
`context.traits.address.country`  
`traits.address.country`| `country`| String data type  
`context.traits.address.region`  
`traits.address.region`| `region`| String data type  
`traits.zip`  
`traits.postalcode`  
`traits.postalCode`  
`traits.address.zip`  
`traits.address.postalcode`  
`traits.address.postalCode`  
`context.traits.zip`  
`context.traits.postalcode`  
`context.traits.postalCode`  
`context.traits.address.zip`  
`context.traits.address.postalcode`  
`context.traits.address.postalCode`  
`properties.zip`  
`properties.postalcode`  
`properties.postalCode`| `zip`| String data type  
`context.traits.address.timezone`  
`traits.address.timezone`| `timezone`| String data type  
  
RudderStack recommends using time zones from the [IANA time zone database](<https://www.iana.org/time-zones>).  
`context.ip`| `ip`| String data type  
`context.address.longitude`  
`context.location.longitude`| `longitude`| String data type  
`context.address.latitude`  
`context.location.latitude`| `latitude`| String data type  
  
## Track

> ![warning](/docs/images/warning.svg)
> 
> Klaviyo **does not** support ecommerce events. Hence, RudderStack does not adhere to the [Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) while sending `track` events to Klaviyo.

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [track a profile’s activity](<https://developers.klaviyo.com/en/reference/create_event>) in Klaviyo.

A sample `track` event payload sent to Klaviyo is shown:
    
    
    {
      "type": "track",
      "sentAt": "2021-01-25T16:12:02.048Z",
      "userId": "1hKOmRA4el9Z",
      "event": "Sample Event",
      "context": {
        "traits": {
          "firstName": "Alex",
          "lastName": "Keener",
          "email": "alex@example.com",
          "title": "Developer",
          "organization": "Example Co.",
          "city": "New Orleans",
          "region": "Louisiana",
          "country": "US",
          "zip": "100-0001",
          "Flagged": false,
          "Residence": "31, North Avenue",
          "street": "Blue Gum Street",
        }
      },
      "properties": {
        "PreviouslVicePresident": true,
        "YearElected": 1801,
        "VicePresidents": [
          "AaronBurr",
          "GeorgeClinton"
        ],
        "revenue": 3000,
        "currency": "USD"
      },
      "rudderId": "re515f91ynjf62i3h98g52ao6w8qm7vmg94s",
      "messageId": "5vs9plymaxu4zfh40cmqca7r220y3wzb2giu",
      "anonymousId": "9c6bd77ea9da3e68",
      "originalTimestamp": "2021-01-25T15:32:56.409Z"
    }
    

### Supported mappings

This section lists the mappings between RudderStack and Klaviyo fields for the `track` event.

#### Top level mappings

RudderStack property| Klaviyo property| Note  
---|---|---  
-| `data.type`| Automatically set to `event`.  
  
#### Traits mappings

**User attributes mapping**  


RudderStack maps the following fields within the [`data.profile.data.attributes`](<https://developers.klaviyo.com/en/reference/create_event#:~:text=Generated%20by%20Klaviyo.-,attributes,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
`context.traits.email`  
`traits.email`| `email`| Email format  
`context.traits.phone`  
`traits.phone`| `phone_number`| Must be a valid [E.164 format phone number](<https://developers.klaviyo.com/en/v2024-10-15/reference/events_api_overview#receiving-a-400>). Otherwise, the event will fail.  
`userId`  
`context.traits.userId`  
`traits.userId`| `external_id`| String data type  
`anonymousId`| `anonymous_id`| String data type  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `first_name`| String data type  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `last_name`| String data type  
`context.traits.title`  
`traits.title`| `title`| Individual’s job title  
  
String data type  
`context.traits.organization`  
`traits.organization`| `organization`| String data type  
`context.traits.image`  
`traits.image`| `image`| URL format  
`context.traits._kx`  
`traits._kx`| `_kx`| Also known as the `exchange_id`, this is an encrypted identifier used for identifying a profile by Klaviyo’s web tracking.  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack maps the custom properties for the user profile (of string data type) to Klaviyo’s [`data.profile.data.attributes`](<https://developers.klaviyo.com/en/reference/create_event#:~:text=127.0.0.1-,properties,-object>) object in a key-value format.

**Location attributes mapping**  


RudderStack maps the following fields to the [`data.profile.data.attributes.location`](<https://developers.klaviyo.com/en/reference/create_event#:~:text=photo%2D3760854.jpeg-,location,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
`traits.street`  
`traits.address.street`  
`context.traits.street`  
`context.traits.address.street`  
`properties.street`| `address1`| String data type  
`context.traits.address.city`  
`traits.address.city`| `city`| String data type  
`context.traits.address.country`  
`traits.address.country`| `country`| String data type  
`context.traits.address.region`  
`traits.address.region`| `region`| String data type  
`traits.zip`  
`traits.postalcode`  
`traits.postalCode`  
`traits.address.zip`  
`traits.address.postalcode`  
`traits.address.postalCode`  
`context.traits.zip`  
`context.traits.postalcode`  
`context.traits.postalCode`  
`context.traits.address.zip`  
`context.traits.address.postalcode`  
`context.traits.address.postalCode`  
`properties.zip`  
`properties.postalcode`  
`properties.postalCode`| `zip`| String data type  
`context.traits.address.timezone`  
`traits.address.timezone`| `timezone`| String data type  
  
RudderStack recommends using time zones from the [IANA time zone database](<https://www.iana.org/time-zones>).  
`context.ip`| `ip`| String data type  
`context.address.longitude`  
`context.location.longitude`| `longitude`| String data type  
`context.address.latitude`  
`context.location.latitude`| `latitude`| String data type  
  
#### Other mappings

RudderStack property| Klaviyo property| Note  
---|---|---  
-| `data.metric.data.type`| Automatically set to `metric`.  
`event`  
Required| `data.attributes.metric.data.attributes.name`| Event name as a string.  
`properties`| `data.attributes.properties`| Event properties excluding the following fields:  
  
`email`, `phone`, `revenue`, `total`, `value`, `value_currency`, and `currency`  
`timestamp`  
`originalTimestamp`| `data.attributes.time`| Time when the event occurred.  
`properties.revenue`  
`properties.total`  
`properties.value`| `data.attributes.value`| String data type / Integer  
`properties.currency`| `data.attributes.value_currency`| ISO 4217 currency code with string data type.  
  
> ![warning](/docs/images/warning.svg)
> 
> A user profile and metric objects should include at least one profile identifier (for example, `id`, `email`, or `phone_number`) and the metric `name`.

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to subscribe one or more profiles to email marketing, SMS marketing, or both. RudderStack uses Klaviyo’s [Bulk Subscribe Profiles](<https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles>) API to send this data.

> ![info](/docs/images/info.svg)
> 
> You must include either `email`, `userId` or `phone` fields to send a `group` event to Klaviyo successfully.

A sample `group` event payload sent to Klaviyo is shown:
    
    
    {
      "channel": "web",
      "userId": "1hKOmRA4el9Z",
      "type": "group",
      "groupId": "group123",
      "traits": {
        "subscribe": true
      },
      "context": {
        "externalId": [
          {
            "type": "klaviyo-profileId",
            "id": "klaviyoID"
          }
        ],
        "traits": {
          "email": "alex@example.com",
          "consent": [
            "email"
          ]
        }
      },
      "timestamp": "2020-01-21T00:21:34.208Z",
      "anonymousId": "jzfsz147d02cil0gqz6rkg7mtou10dovcwia",
      "originalTimestamp": "2019-10-14T09:03:17.562Z"
    }
    

In the above snippet, the user with the associated traits is added and subscribed to the group as `subscribe` set to `true`.

Note that specifying `consent` in the event’s `context` object (seen above) overrides the [consent settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/setup-guide/#configuration-settings>) configured in the RudderStack dashboard.

### Top level mappings

The following table lists the mappings between RudderStack and Klaviyo properties:

RudderStack property| Klaviyo property| Note  
---|---|---  
-| `data.type`| Automatically set to `profile-subscription-bulk-create-job`.  
  
### Other mappings

**Attributes mapping**  


RudderStack maps the following fields within the [`data.attributes`](<https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles#:~:text=ATTRIBUTES%20OBJECT-,custom_source,-string>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
`traits.custom_source`| `custom_source`| String data type  
  
##### **Profile data mappings**

RudderStack maps the following fields within the [`data.attributes.profiles`](<https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles#:~:text=Marketing%20Event-,profiles,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
-| `data.type`| Automatically set to `profile`.  
`id` in the `externalId` array, where `type` is set to `klaviyo-profileId`. For example:  
  

    
    
    “context”: {  
      “externalId”: [  
        {  
          “type”: “klaviyo-profileId”,  
          “id”: “some_id”  
        }  
      ]  
    }

| `data.id`| ID of the profile to subscribe. If provided, Klaviyo uses it to perform the lookup.  
  
If not explicitly provided, RudderStack updates the Klaviyo profile based on the `userId`/`email`/`phone` match.  
`email`| `data.attributes.email`| Email format  
`phone number`| `data.attributes.phone_number`| Must be a valid [E.164 format phone number](<https://developers.klaviyo.com/en/v2024-10-15/reference/events_api_overview#receiving-a-400>). Otherwise, the event will fail.  
`context.traits.consent` array including `email` or `sms` values| `marketing.consent` within `data.attributes.subscriptions` (either `email` or `sms`)| Values required for the marketing consent.  
**Relationships mapping**  


RudderStack maps the following fields in the [`data.relationships`](<https://developers.klaviyo.com/en/reference/bulk_subscribe_profiles#:~:text=LIST%20OBJECT-,data,-object>) object:

RudderStack property| Klaviyo property| Note  
---|---|---  
-| `list.data.type`| Automatically set to `list`.  
`groupId`  
Required| `list.data.id`| List/group to add the newly subscribed profiles to.