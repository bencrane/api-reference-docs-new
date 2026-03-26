# Set up HubSpot Destination in RudderStack

Set up HubSpot as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up HubSpot as a destination in RudderStack.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **HubSpot** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the HubSpot native SDK from the `https://js.hs-scripts.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the HubSpot SDK successfully.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **HubSpot** from the list of destinations. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in your RudderStack dashboard.  
API Version| Select the HubSpot API version from the dropdown. RudderStack supports both the **New API (v3)** and **Legacy API (v1)** (deprecated).  
  
> ![danger](/docs/images/danger.svg)
> 
> HubSpot has deprecated the legacy API (v1). RudderStack recommends using the New API (v3) instead.

### Legacy API settings

Setting| Description  
---|---  
Authorization Type| Select the authorization mechanism from **API Key** (deprecated) or **Private Apps**.  
API Key| If you selected **API Key** , specify your HubSpot API key. You can find this by going to **Settings** > **Integrations** > **API Key** in your HubSpot account.  
  


> ![warning](/docs/images/warning.svg)HubSpot has [deprecated](<https://developers.hubspot.com/docs/guides/apps/authentication/intro-to-auth>) the API key authentication mechanism.  
  
Access Token| If you selected **Private Apps** , specify the HubSpot access token.  
  
### New API settings

These settings are only applicable if you selected **New API (v3)** as the API version:

Setting| Description  
---|---  
Authorization Type| Select the authorization mechanism from **API Key** (deprecated) or **Private Apps**.  
  


  * If you select **API Key** , then specify your HubSpot API key by going to **Settings** > **Integrations** > **API Key**. Note that HubSpot has [deprecated](<https://developers.hubspot.com/docs/guides/apps/authentication/intro-to-auth>) the API key authentication mechanism.
  * If you select **Private Apps** , then specify the HubSpot access token.

  
HubSpot property to be used for upsert| Enter the contact property that RudderStack uses as a lookup field to [match contacts in HubSpot](<https://developers.hubspot.com/docs/api/crm/contacts>), for example, `uniqueId`. Make sure to then pass the same property in the `identify` event’s `traits` object with the value to upsert.  
  
For best performance, use a property that is unique in HubSpot — unique properties enable batch upsert and higher throughput, whereas non-unique properties use a slower search-based flow.  
  
For more information, see HubSpot’s [Create or update a batch of contacts](<https://developers.hubspot.com/docs/api-reference/crm-contacts-v3/batch/post-crm-v3-objects-contacts-batch-upsert>) API reference.  
  


> ![info](/docs/images/info.svg)**This setting is available only when using the new HubSpot API**.  
>   
> In the legacy API, RudderStack supports updating a contact only via email.

  
See the [`identify`](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/cloud-mode/new-api/#identify>) section for more information.  
Create association between object records| Toggle on this setting to create associations between the object records while using a Reverse ETL source.  
  
See [Creating associations between object records](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/connect-retl-source/#create-association-between-object-records>) section for more information.  
  
### Configuration settings

Setting| Description  
---|---  
Hub ID| Specify your HubSpot Hub ID.  
  
See the [HubSpot documentation](<https://knowledge.hubspot.com/account/manage-multiple-hubspot-accounts#identify-the-current-account-s-hub-id>) for more information on obtaining this ID.  
  
### Consent settings

Setting| Description  
---|---  
Consent settings| Configure the consent management settings for the specified sources by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
### Web device mode settings

The below setting is applicable **only if** you want to send events to HubSpot in the [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>):

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to HubSpot.  
  
See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information on this feature.  
  
### Event mapping settings

> ![warning](/docs/images/warning.svg)
> 
> These settings are applicable only for the New HubSpot API.

Click **Set up mapping** and map RudderStack events to your HubSpot [custom behavioral events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/cloud-mode/new-api/#custom-behavioral-events>).

Although HubSpot provides some [default properties](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/cloud-mode/new-api/#behavioral-events-property-mappings>) with custom behavioral events, you can create additional custom properties and map them to specific RudderStack properties using these settings.

You can also specify multiple properties for a single event.

## FAQ

#### Where can I find the HubSpot access token?

  1. Log in to your [HubSpot account](<https://app.hubspot.com/login/>).
  2. Go to **Integrations** > **Private Apps** from the left sidebar.
  3. Click your app to get the access token:

[![](/docs/images/event-stream-destinations/Hubspot-access-token.webp)](</docs/images/event-stream-destinations/Hubspot-access-token.webp>)

> ![warning](/docs/images/warning.svg)
> 
> If you’re connecting a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) source to HubSpot that uses [private app access token](<https://developers.hubspot.com/docs/api/intro-to-auth#private-app-access-tokens>) for authentication, make sure your access token has the [required scopes](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/connect-retl-source/#required-scopes>).
> 
> See the [HubSpot documentation](<https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app#create-a-new-private-app>) for more information on adding the above scopes.