# Setup Guide

Set up Sendinblue as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Sendinblue as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Sendinblue.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Sendinblue** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Sendinblue native SDK from the `https://sibautomation.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Sendinblue SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Sendinblue, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Sendinblue**.
  2. Assign a name and click **Continue**.


## Connection settings

To successfully configure Sendinblue as a destination, you will need to configure the following settings:

  * **API Key:** Enter your Sendinblue API key. Refer to the FAQ section for more information on obtaining the API key.
  * **Client Key:** Enter your Sendinblue client key. Refer to the FAQ section for more information on obtaining the client key.
  * **Create contact via Double-opt-in:** This setting is applicable **only** for the cloud mode. You can enable it to [create a contact using the DOI flow](<https://developers.sendinblue.com/reference/createdoicontact>). If enabled, enter the following settings:
    * **Template ID:** Enter the ID of the Double opt-in (DOI) template. Refer to the FAQ section for more information on obtaining the DOI template ID.
    * **Redirection URL:** Enter the URL of the web page where the user is redirected after clicking on the verification email.
  * **Send user traits in track call:** Enable this setting to send user traits to Sendinblue via the `track` call. RudderStack updates the contact’s attributes corresponding to their traits in the `track` call.
  * **Map your traits to Sendinblue contact attributes:** Enter the traits in RudderStack’s payload to be mapped to the [contact attributes in Sendinblue](<https://my.sendinblue.com/lists/add-attributes>).


> ![warning](/docs/images/warning.svg)
> 
> Enter only the key name present in the event’s `traits` object.
> 
> For example, to map `context.traits.email` to Sendinblue’s `EMAIL` attribute, specify `email` in the **Rudder payload trait key** field and `EMAIL` in the **Sendinblue contact attribute name** field.
> 
> ![Sendinblue trait mapping](/docs/images/event-stream-destinations/sendinblue-mapping.webp)

  * **Client-side Events Filtering** : This setting is applicable **only** for the device mode and lets you specify which events should be blocked or allowed to flow through to Sendinblue. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.


## FAQ

#### Where can I find the API key?

  1. Log in to the [Sendinblue account](<https://account-app.sendinblue.com/account/login>).
  2. Click on your profile and select **SMTP & API**. Here, you can find an existing API key or create a new one by clicking on **CREATE A NEW API KEY** :

[![Sendinblue API Key](/docs/images/event-stream-destinations/sendinblue-api-key.webp)](</docs/images/event-stream-destinations/sendinblue-api-key.webp>)

#### Where can I find the Client Key?

  1. Log in to the [Sendinblue account](<https://account-app.sendinblue.com/account/login>).
  2. Click **Automation** tab > **Script set up** under the **Help** section in the left navigation bar.
  3. Select **JS Tracker** in the **Choose an installation option** step to obtain the **client_key** from the script:

[![Sendinblue Client Key](/docs/images/event-stream-destinations/sendinblue-client-key.webp)](</docs/images/event-stream-destinations/sendinblue-client-key.webp>)

#### Where can I find the DOI templated ID?

  1. Log in to the [Sendinblue account](<https://account-app.sendinblue.com/account/login>).
  2. Click **Templates** in the left navigation bar to obtain your template’s ID:

[![Sendinblue DOI template ID](/docs/images/event-stream-destinations/sendinblue-doi-template-id.webp)](</docs/images/event-stream-destinations/sendinblue-doi-template-id.webp>)