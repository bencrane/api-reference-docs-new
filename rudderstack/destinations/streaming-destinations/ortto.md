# Ortto (formerly Autopilot) Beta

Send your event data from RudderStack to Ortto.

* * *

  * __4 minute read

  * 


[Ortto](<https://www.autopilothq.com/>) (formerly Autopilot) is a popular marketing automation platform that allows you to track and capture new leads, create detailed customer journeys, and boost customer retention.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/ortto>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Ortto**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Ortto as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Private API Key** : Enter your private API key from the Ortto data source. For more information on generating this key, see [Ortto’s documentation](<https://help.ortto.com/user/latest/data-sources/configuring-a-new-data-source/other-integrations/custom-api.html#create-your-custom-api-key>).
  * **Instance Region** : Specify your Ortto account’s instance region from **Australia** , **Europe** , or **Other**.


### Connection mode

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Ortto** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Ortto:

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Event and property mapping

Click the **Set up mapping** button to map your RudderStack events and properties to specific Ortto custom events/properties. You can also use the JSON mapper to set these mappings.

RudderStack provides the following options:

  * **Event and property mappings** : Map a RudderStack event or property to an Ortto event/property. In the property mappings, you can also specify the **Ortto Property Type**.

[![Ortto event mapping](/docs/images/event-stream-destinations/ortto-event-mapping.webp)](</docs/images/event-stream-destinations/ortto-event-mapping.webp>)

  * **Custom user traits mappings** : Use this setting to map the user traits in your `identify` events to your [Ortto Person](<https://help.ortto.com/developer/latest/api-reference/person/index.html>) attributes.

[![Ortto traits mapping](/docs/images/event-stream-destinations/ortto-trait-mapping.webp)](</docs/images/event-stream-destinations/ortto-trait-mapping.webp>)

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update an user in Ortto. RudderStack sends this data to Ortto by leveraging their [`merge`](<https://help.ortto.com/developer/latest/api-reference/person/merge.html>) endpoint.

A sample `identify` event is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      "firstName": "Alex",
      "lastName": "Keener",
      "email": "alex@example.com",
      "phone": "+1-202-555-0146",
      "emailConsent": true,
      "smsConsent": false,
      "gdpr": false,
      "address": {
        "city": "New Orleans",
        "country": "USA",
        "zipcode": 900001
      }
    });
    

Note that:

  * `userId` or `anonymousId` are required fields in your `identify` calls for RudderStack to send data to Ortto successfully.
  * RudderStack uses `userId`/`anonymousId` to look up the user and update their profile in Ortto. If these fields are absent, it uses `email` instead.
  * Use the `emailConsent`, `smsConsent`, and `gdpr` fields to set consent for email subscription, SMS subscription, and GDPR, respectively.


## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) to record user activities in Ortto. RudderStack sends this data to Ortto by leveraging their [`activities`](<https://help.ortto.com/a-270-activities>) API. The event mapping is shown below:

RudderStack event| Ortto event  
---|---  
`event`  
Required| `activities[i].activity_id`  
  
A sample `track` payload is as shown in the snippet below:
    
    
    rudderanalytics.track("Product Clicked", {
      description: "Adidas Sneakers",
      brand: "Adidas",
      colors: "red",
      productName: "Shoes"
    }, {
      context: {
        traits: {
          emailConsent: false,
          smsConsent: true,
          gdpr: true
        }
      }
    });
    

As seen in the above snippet, you can use the `emailConsent`, `smsConsent`, and `gdpr` fields within the `context.traits` object to set consent for email subscription, SMS subscription, and GDPR, respectively.

> ![warning](/docs/images/warning.svg)
> 
> Make sure the events you want to send to Ortto are specified and mapped to the Ortto events in the Event and property mappings dashboard setting. Otherwise, RudderStack will drop them.

## Supported mappings

RudderStack maps the following `identify`/`track` event properties to the corresponding Ortto properties:

RudderStack property| Ortto property  
---|---  
`userId`  
`anonymousId`  
Required| `str::ei`  
`context.traits.firstName`| `people[i].fields.str::first`  
`context.traits.lastName`| `people[i].fields.str::last`  
`context.traits.email`| `people[i].fields.str::email`  
`context.traits.address.city`| `people[i].fields.geo::city.name`  
`context.traits.address.country`| `people[i].fields.geo::country.name`  
`context.traits.address.region`| `people[i].fields.geo::region.name`  
`context.traits.address.zipcode`| `people[i].fields.str::postal`  
`context.traits.birthday`  
  


> ![warning](/docs/images/warning.svg)This field should be a string in `YYYY-MM-DD` format.  
>   
> You can use a [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to convert the field values if they are not present in the above format.

| `people[i].fields.dtz::b`  
`context.traits.language`  
`context.locale`| `str::language`  
`context.traits.phone`| `phn::phone.n`  
`userId`  
`anonymousId`| `str::ei`  
  
> ![info](/docs/images/info.svg)
> 
> You can send up to 100 fields in a single request.