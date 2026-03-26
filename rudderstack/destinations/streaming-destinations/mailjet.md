# Mailjet Destination

Send your event data from RudderStack to Mailjet.

* * *

  * __3 minute read

  * 


[Mailjet](<https://www.mailjet.com/>) is a popular email marketing and delivery platform. It lets you create and send impactful email marketing campaigns, newsletters, and automated emails to grow your business.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/mailjet>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Mailjet** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Mailjet, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Mailjet**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully set up Mailjet as a destination, you need to configure the following settings:

  * **Mailjet API Key** : Enter your Mailjet API key.
  * **Mailjet API Secret** : Enter your Mailjet secret key.
  * **Mailjet Contact List ID** : Enter your Mailjet contact list ID. RudderStack will use this ID if the list ID is not provided via the `externalId` field in the event’s payload.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section for more information on obtaining the Mailjet API Key, secret key, and contact list ID.

  * **Map RudderStack user attributes to Mailjet contact properties** : Use this setting to map your RudderStack event properties to specific custom properties created in the Mailjet dashboard. For more information on creating and managing contact properties, refer to the [Mailjet documentation](<https://documentation.mailjet.com/hc/en-us/articles/360043176353-How-to-create-manage-contact-properties->).


> ![warning](/docs/images/warning.svg)
> 
> Mailjet will not create a contact for the event properties configured in the RudderStack dashboard but not created in Mailjet.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to add or remove a contact in Mailjet. If a contact already exists, RudderStack updates the contact details.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4el9Z', {
          firstName: 'Alex',
          lastName: 'Keener',
          email: "alex@example.com"
        },
          externalId: [{
            type: "listId",
            id: "13314el9Z"
          }],
          integrations: {
            Mailjet: {
              Action: "remove"
            }
          }
        );
    

When sending events to Mailjet, note the following:

  * The `email` field is mandatory. Otherwise, Mailjet rejects the events.
  * You can specify the Mailjet list ID either in the **Mailjet Contact List ID** setting of the RudderStack dashboard or in the `externalId` field.
  * You can specify the Mailjet action (adding/removing user) in the `Action` field of the `integrations` object. If no action is specified, RudderStack sets this field to `addnoforce`, by default.


> ![info](/docs/images/info.svg)
> 
> For more information on the `addnoforce` parameter, refer to the [Mailjet Subscriptions API reference](<https://dev.mailjet.com/email/reference/contacts/subscriptions/>).

### Supported mappings

The following table lists the mappings between the RudderStack attributes and the Mailjet properties:

RudderStack property| Mailjet property  
---|---  
`traits.email`  
Required| `Email`  
`traits.name`| `Name`  
`context.traits.IsExcludedFromCampaigns`  
`traits.IsExcludedFromCampaigns`| `IsExcludedFromCampaigns`  
  
## FAQ

#### Where can I find the Mailjet API key and secret key?

To obtain your Mailjet API key and secret, follow these steps:

  1. Log into your [Mailjet dashboard](<https://app.mailjet.com/account>).
  2. From the top right section of the dashboard, click your name and go to **Account settings** > **REST API** > **API Key Management (Primary and Sub-account)**. Your primary API key and secret will listed here:

[![Mailjet API key and secret key](/docs/images/event-stream-destinations/mailjet-apikey-secret.webp)](</docs/images/event-stream-destinations/mailjet-apikey-secret.webp>)

#### Where can I find contact list ID in Mailjet?

To get your Mailjet contact list ID, log into your [Mailjet dashboard](<https://app.mailjet.com/account>) and go to **Contacts** > **Contact Lists**. You can find your contact lists and the associated IDs listed here:

[![Mailjet contact list ID](/docs/images/event-stream-destinations/mailjet-contactlistid.webp)](</docs/images/event-stream-destinations/mailjet-contactlistid.webp>)