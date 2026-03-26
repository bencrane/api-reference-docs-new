# HubSpot Cloud Mode Integration (New API v3)

Send events to HubSpot via cloud mode using the new API.

* * *

  * __4 minute read

  * 


RudderStack supports the following API calls while sending data to Hubspot via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using the [new API v3](<https://developers.hubspot.com/docs/api/overview>).

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support the [new datetime data type](<https://www.youtube.com/watch?v=2YjCUQUt8iY&ab_channel=HubSpot>) introduced by HubSpot.

## Identify

RudderStack sends the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to check if a contact exists, if it does, RudderStack updates the contact with new information. Otherwise, it creates a new contact.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify({
      firstName: "Alex",
      city: "New Orleans",
      country: "USA",
      phone: "+1-202-555-0146",
      email: "alex@example.com",
      custom_flavor: "chocolate",
      custom_date: 1574769933368,
      custom_date1: new Date("2019-10-14T11:15:53.296Z"),
    })
    

Make sure to specify the HubSpot property you set in **HubSpot property to be used for upsert** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/setup-guide/#new-api-settings>) in the `traits` object of the `identify` call — RudderStack sends this property to HubSpot for matching contacts.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** For best performance, choose a HubSpot contact property that is unique in your account. Unique properties let RudderStack call HubSpot’s [batch upsert contacts API](<https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/batch/post-crm-v3-objects-contacts-batch-upsert>) for `identify` events, which significantly increases throughput.
> 
> Non-unique properties will still work, but RudderStack uses a slower search-based flow.

A sample snippet is shown below:
    
    
    rudderanalytics.identify({
      name: "Alex Keener",
      phone: "+1-202-555-0146",
      traits: {
        "uniqueId": "user-12345",
      },
    })
    

> ![info](/docs/images/info.svg)
> 
> If you configure **HubSpot property to be used for upsert** in the dashboard but omit that property from the `identify` call’s `traits`, RudderStack uses `email` as the default field for matching.

### Trait mappings

The following table lists the mappings between the RudderStack properties and the HubSpot properties:

RudderStack property| HubSpot property  
---|---  
`traits.email`  
`context.traits.email`  
`properties.email`| `email`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`  
`properties.firstname`| `firstname`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`  
`properties.lastname`| `lastname`  
`phone`| `phone`  
`traits.address.street`  
`context.traits.address.street`  
`properties.address.street`| `address`  
`traits.address.city`  
`context.traits.address.city`  
`properties.address.city`| `city`  
`traits.address.country`  
`context.traits.address.country`  
`properties.address.country`| `country`  
`traits.address.state`  
`context.traits.address.state`  
`properties.address.state`| `state`  
`traits.address.postalcode`  
`context.traits.address.postalcode`  
`properties.address.postalcode`| `zip`  
`traits.company.name`  
`context.traits.company.name`  
`properties.company.name`| `company`  
  
## Track

A [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record various user actions and any properties associated with them.

To associate a `track` call with a user, you need to specify the user’s `email` under `context.traits`.

> ![info](/docs/images/info.svg)
> 
> RudderStack associates the `track` events with the same user only after you make a successful `identify` call. However, if you send a `track` call without making any `identify` call first and there is no contact present in HubSpot, RudderStack will not associate the events as there is no identifier.

A sample `track` event is as shown:
    
    
    rudderanalytics.track(
      "Order Completed", {
        value: 30,
      }, {
        context: {
          traits: {
            firstname: "Alex",
            city: "New Orleans",
            country: "USA",
            phone: "+1-202-555-0146",
            email: "alex@example.com",
          },
        },
      }
    )
    

### Property mappings

The following table lists the properties and their mappings between RudderStack and HubSpot for the `track` call:

RudderStack property| HubSpot property  
---|---  
`traits.utk`  
`context.traits.utk`  
`properties.utk`| `utk`  
`traits.email`  
`context.traits.email`| `email`  
`traits.objectId`  
`context.traits.objectId`  
`properties.objectId`| `objectId`  
`properties.occurred_at`  
`timestamp`  
`originalTimestamp`| `occurredAt`  
  
> ![warning](/docs/images/warning.svg)
> 
> You must send either of the `utk`, `email`, or `objectId` (can be `contact_id` or `visitor_ id`) properties to make a `track` call successfully.

### Custom behavioral events

> ![warning](/docs/images/warning.svg)
> 
> The custom behavorial events can be used for both the authentication types. However, they must have the `analytics.behavioral_events.send` permission to be used for private apps.

[Custom behavioral events](<https://developers.hubspot.com/docs/api/analytics/events>) are account-defined events in HubSpot that store event details in the event properties. You can create custom behavioral events and their associated properties in the RudderStack dashboard as explained in the [New API](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/setup-guide/#new-api>) section.

The following parameters are sent in the custom behavorial events:

  * **Identifier** : Either the contact ID, email, or [utk](<https://developers.hubspot.com/docs/api/events/tracking-code>) (user token) of the contact associated with the event. The utk is the user token stored in the visitor’s `hubspotutk` browser cookie.
  * **Event name:** The internal name of the event which can be found in HubSpot.
  * **Properties object** : When you create a custom behavioral event in HubSpot, some default properties are provided with those events, explained in the below section.


#### Behavioral events property mappings

The following table lists the **optional** and default property mappings between RudderStack and HubSpot for custom behavioral events:

RudderStack property| HubSpot property  
---|---  
`properties.assetDescription`  
`properties.hsAssetDescription`| `hs_asset_description`  
`properties.assetType`  
`properties.hsAssetType`| `hs_asset_type`  
`properties.campaignId`| `hs_campaign_id`  
`traits.address.city`  
`context.traits.address.city`  
`properties.address.city`| `hs_city`  
`traits.address.country`  
`context.traits.address.country`  
`properties.address.country`| `hs_country`  
`context.device.name`| `hs_device_name`  
`properties.elementClass`  
`properties.hsElementClass`| `hs_element_class`  
`properties.elementId`  
`properties.hsElementId`| `hs_element_id`