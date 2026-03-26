# Mailmodo Destination

Send your event data from RudderStack to Mailmodo.

* * *

  * __3 minute read

  * 


[Mailmodo](<https://www.mailmodo.com/>) is an interactive email marketing tool. It provides several useful features like sending transactional campaigns, email automation, and drip emails with customer journeys, WYSIWYG email editor, and many other tool integrations.

> ![success](/docs/images/tick.svg)
> 
> RudderStack also supports Mailmodo as a data source. For more information, refer to the [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Mailmodo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Mailmodo, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Mailmodo**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Mailmodo as a destination, you will need to configure the following settings:

[![Mailmodo connection settings](/docs/images/event-stream-destinations/mailmodo-connection-settings.webp)](</docs/images/event-stream-destinations/mailmodo-connection-settings.webp>)

  * **API Key** : Enter your Mailmodo API key.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your Mailmodo API key, refer to the FAQ section below.

  * **List Name** : This field is **only applicable** for the `identify` call. Enter the name of the Mailmodo list where the contacts should be added. If not provided, `RudderStack` is taken as the default list name.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [add contacts to your Mailmodo list](<https://www.mailmodo.com/developers/6661e4fb7833e-bulk-add-contact-to-a-list/>). If a contact already exists, RudderStack updates the contact details.

> ![warning](/docs/images/warning.svg)
> 
> You cannot add more than 100 contacts in a single `identify` call.

A sample `identify` call is shown below:
    
    
    {
      "userId": "1hKOmRA4el9Z",
      "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8",
      "context": {
        "traits": {
          "trait1": "new-val"
        },
        "ip": "14.5.67.21",
        "library": {
          "name": "http"
        }
      },
      "traits": {
        "email": "alex@example.com",
        "name": "Alex Keener",
        "firstName": "Alex",
        "lastName": "Keener",
        "age": 40,
        "phone": "+1-202-555-0146",
        "lastClick": "2020-02-02T00:23:09.544Z",
        "lastOpen": "2020-02-02T00:23:09.544Z"
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

### Supported mappings

The following table lists the mappings between the RudderStack and Mailmodo properties:

RudderStack property| Mailmodo property| Presence  
---|---|---  
`traits.email`/`context.traits.email`/`properties.email`| `values.email`| Required  
`traits.firstName`/`context.traits.firstName`| `values.data.first_name`| Optional  
`traits.lastName`/`context.traits.lastName`| `values.data.last_name`| Optional  
`traits.name`/`context.traits.name`| `values.data.name`| Optional  
`traits.gender`/`context.traits.gender`| `values.data.gender`| Optional  
`traits.age`/`context.traits.age`| `values.data.age`| Optional (Integer format)  
`traits.birthday`/`context.traits.birthday`| `values.data.birthday`| Optional (ISO format/UNIX timestamp)  
`traits.phone`/`context.traits.phone`| `values.data.phone`| Optional  
`traits.city`/`context.traits.city`/`traits.address.city`/`context.traits.address.city`| `values.data.city`| Optional  
`traits.address`/`context.traits.address`| `address1` \+ `address2`| Optional  
`traits.state`/`context.traits.state`/`traits.address.state`/`context.traits.address.state`| `values.data.state`| Optional  
`traits.country`/`context.traits.country`/`traits.address.country`/`context.traits.address.country`| `values.data.country`| Optional  
`traits.zipcode`/`context.traits.zipcode`/`traits.postalcode`/`context.traits.postalcode`/`traits.postal_code`/`context.traits.postal_code`| `values.data.postal_code`| Optional  
`traits.designation`/`context.traits.designation`| `values.data.designation`| Optional  
`traits.company`/`context.traits.company`| `values.data.company`| Optional  
`traits.industry`/`context.traits.industry`| `values.data.industry`| Optional  
`traits.description`/`context.traits.description`| `values.data.description`| Optional  
`traits.anniversaryDate`/`context.traits.anniversaryDate`/`traits.anniversary_date`/`context.traits.anniversary_date`| `values.data.anniversary_date`| Optional (ISO format/UNIX timestamp)  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack sends any property apart from the ones mentioned above as a custom property inside `traits/context.traits` and maps it to `values.data` before sending it to Mailmodo.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [add custom events for a contact](<https://www.mailmodo.com/developers/93cba3fa7f1ea-add-event/>).

A sample `track` call is shown below:
    
    
    {
      "userId": "1hKOmRA4el9Z",
      "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8",
      "event": "Product Purchased",
      "properties": {
        "name": "Shirt",
        "email": "alex@example.com",
        "revenue": 4.99
      },
      "context": {
        "ip": "14.5.67.21",
        "library": {
          "name": "http"
        }
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

### Supported mappings

The following table lists the mappings between the RudderStack and Mailmodo properties:

RudderStack property| Mailmodo property| Presence  
---|---|---  
`event`| `event_name`| Required  
`traits.email`/`context.traits.email`/`properties.email`| `email`| Required  
`timestamp`| `ts`| Optional (UNIX epoch in seconds)  
`properties`| `event_properties`| Optional  
  
## FAQ

#### Where can I find the Mailmodo API key?

To obtain your Mailmodo API key, follow these steps:

  1. Log into your [Mailmodo dashboard](<https://manage.mailmodo.com/auth/login>).
  2. Go to **Settings** > **API Keys** as shown:

[![Mailmodo API key](/docs/images/event-stream-destinations/mailmodo-api-key.webp)](</docs/images/event-stream-destinations/mailmodo-api-key.webp>)