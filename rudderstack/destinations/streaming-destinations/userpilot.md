# Userpilot Beta

Send your event data from RudderStack to Userpilot.

* * *

  * __4 minute read

  * 


[Userpilot](<https://userpilot.com/>) is a no-code product experience platform that helps you enhance the user onboarding experience. It allows you to drive user activation, boost feature adoption, and improve user retention through personalized in-app experiences.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/develop/src/cdk/v2/destinations/userpilot>).

> ![info](/docs/images/info.svg)
> 
> This integration is built by the Userpilot team. Contact their [Support team](<mailto:support@userpilot.com>) for any assistance.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web, Cloud
  * Refer to it as **Userpilot** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, the Userpilot native SDK is loaded from the `https://js.userpilot.io/` domain.
> 
> Based on your website’s content security policy, you might need to allowlist this domain to load the Userpilot SDK successfully.

## Get started

Once you have confirmed that the platform supports sending events to Userpilot, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Userpilot**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
App Token| Enter your Userpilot app token. This token is required to send events to Userpilot in device mode.  
  
You can obtain the app token by going to **Configure** > [Environment](<https://run.userpilot.io/environment>) in your Userpilot dashboard.  
JS SDK Endpoint| Specify the custom endpoint URL for hosting the Userpilot JavaScript SDK.  
  
Note that:  
  


  * This setting is applicable for the web device mode integration only.
  * The URL must start with `wss://` or `ws://`.

  
API Key| Enter your Userpilot API key. This token is required to send events to Userpilot in cloud mode.  
  
You can obtain the app token by going to **Configure** > [Environment](<https://run.userpilot.io/environment>) in your Userpilot dashboard.  
HTTP API Endpoint| Specify the endpoint for the HTTP API. By default, it is set to `https://analytex.userpilot.io`.  
  
Note that:  
  


  * The endpoint URL may differ based on different Userpilot plans based on your hosting region, as mentioned in the [Userpilot documentation](<https://docs.userpilot.com/article/195-identify-users-and-track-api#:~:text=2020%2D09%2D22%27-,HTTP%20Endpoints,-For%20most%20users>). See the Environment Page in the application to retrieve your dedicated endpoint URL.
  * This setting is applicable for the cloud mode integration only.

  
  
### Configuration settings

Setting| Description  
---|---  
Consent settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event lets you identify a user in Userpilot and associate them with their traits.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlmr123", {
      name: "Alex Keener",
      email: "alex@example.com",
      company: {
        id: "company123", // Mandatory if the `company` object is passed
    
        ... // Other company properties.
    
      },
      plan: "Enterprise",
      role: "Admin",
      createdAt: "2020-01-01T00:00:00.000Z"
    });
    

> ![warning](/docs/images/warning.svg)
> 
> The `id` property is mandatory if you pass the `company` object in your `identify` call.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event lets you track user events and send them to Userpilot.

When you make a `track` call, RudderStack sends the event to Userpilot as a custom event with the event properties included in the call.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Feature Used", {
      featureName: "Dashboard Export",
      exportFormat: "CSV",
      itemsExported: 42
    });
    

## Page

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports the `page` event only in the web device mode integration.

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event lets you record page views in your web app. RudderStack then sends a page view event to Userpilot.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home", {
      path: "/home",
      url: "https://example.com/home",
      title: "Home Page",
      referrer: "https://google.com"
    });
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) event lets you associate users with a specific group, like a company or organization.

When you make a `group` call, RudderStack sends the group information to Userpilot, which you can use for segmentation and creating targeted experiences.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group123", {
      name: "Example Corp",
      industry: "Technology",
      plan: "Enterprise",
      employees: 500,
      website: "https://example.com"
    });
    

## FAQ

#### Where can I find my Userpilot App Token and API Key?

You can find both Userpilot App Token and API Key by going to **Configure** > [Environment](<https://run.userpilot.io/environment>) in your Userpilot dashboard.