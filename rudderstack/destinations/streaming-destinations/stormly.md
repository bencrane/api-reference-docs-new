# Stormly Beta

Send your event data from RudderStack to Stormly.

* * *

  * __3 minute read

  * 


[Stormly](<https://www.stormly.com/>) is a product analytics tool powered by AI. It gives you insights into your users’ behavior and tailored tips on improving their product experience.

Find the open source transformation code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/blob/main/src/v0/destinations/stormly/transform.js>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Stormly** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the platform supports sending events to Stormly, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Stormly**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

  * **API Key** : Enter your Stormly API key. For steps on obtaining the key, see FAQ.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

Use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a user in Stormly.

A sample `identify` call sent to Stormly:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm",{
            city: "New York",
            name: "Alex Keener",
            email: "alex@example.com",
            country: "US",
            trait1:123
        });
    

#### Supported mappings

The following table details the mappings between RudderStack traits and Stormly properties:

RudderStack trait| Stormly property| Data type  
---|---|---  
`userId`  
Required| `userId`| String  
`traits`  
`context.traits`| `traits`| Object  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events and add them to the Stormly database.

The following snippet highlights a sample `track` call:
    
    
    rudderanalytics.track('Product Reviewed', {
      review_id: 'REV1344112',
      product_id: 'XUV112',
      rating: 3.0,
      review_body: 'Good product.',
      groupId: '91Yb32830',
    });
    

#### Supported mappings

The following table details the mappings between RudderStack and Stormly properties:

RudderStack property| Stormly property| Data type  
---|---|---  
`userId`  
Required| `userId`| String  
`event`  
Required| `event`| String  
`properties`| `properties`| Object  
  
## Group

Use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create a group in Stormly and add a user to it.

A sample `group` call sent to Stormly:
    
    
    rudderanalytics.group("91Yb32830", {
      name: "User Group 1",
      employees: 1000,
      industry: "Software",
    });
    

#### Supported mappings

The following table details the mappings between RudderStack and Stormly properties:

RudderStack property| Stormly property| Data type  
---|---|---  
`userId`  
Required| `userId`| String  
`groupId`  
Required| `groupId`| String  
`traits`| `traits`| Object  
  
## FAQ

#### Where can I find the Stormly API key?

  1. Log in to your [Stormly dashboard](<https://www.stormly.com/login>).
  2. From the left sidebar, click the dropdown and select **Manage Projects**.
  3. Select your project.
  4. Click **Set-Up Data**.

[![Stormly Setup Data option](/docs/images/event-stream-destinations/stormly-setup-data.webp)](</docs/images/event-stream-destinations/stormly-setup-data.webp>)

  5. Copy the API key from the resulting URL.

[![Stormly API key](/docs/images/event-stream-destinations/stormly-api-key.webp)](</docs/images/event-stream-destinations/stormly-api-key.webp>)