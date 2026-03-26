# CommandBar Beta

Send your event data from RudderStack to CommandBar.

* * *

  * __3 minute read

  * 


[CommandBar](<https://www.commandbar.com/>) is an AI-powered user assistance platform. It allows product, marketing, and customer success teams achieve their user engagement, activation, conversion, and retention goals.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/CommandBar>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **CommandBar**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up CommandBar as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Organization ID** : Enter your CommandBar organization ID. You can find it in the left navigation bar of your CommandBar dashboard by clicking your organization name.


### Connection mode

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web
  * Refer to it as **CommandBar** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the CommandBar snippet from the `https://*.commandbar.com` domain. Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) for the integration to work correctly.
> 
> For more information, see [setting up content security policies for CommandBar](<https://www.commandbar.com/docs/guides/developer-docs/dealing-with-content-security-policies/#setting-up-content-security-policies-for-commandbar>).

### Configuration settings

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to CommandBar. For more information on this setting, see [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify users in CommandBar. RudderStack maps this event to CommandBar SDK’s [`boot`](<https://www.commandbar.com/docs/sdk/lifecycle/boot/>) method.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      address: "1800 Blue Gum Street",
      hmac: "hmacUserId",
      createdAt: "Mon May 19 2019 18:34:24 GMT+0000 (UTC)",
    })
    

### Traits mapping

RudderStack maps the following `identify` traits to the CommandBar attributes:

RudderStack property| CommandBar property| Data type  
---|---|---  
`userId`  
Required| `userId`| String  
`context.traits` \+ `traits`  
Default: `{}`| `traits`| Object  
`context.traits.hmacId`  
`traits.hmacId`| `Commandbar.hmac`| String  
  
`hmacId` is used to identify users with an HMAC of their user ID, helping secure user-related features like customizable shortcuts. See [CommandBar identity verification](<https://app.commandbar.com/identity-verification>) for more information.

## Track

You can use the event names in your [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) calls to trigger surveys in CommandBar. RudderStack maps this event to CommandBar SDK’s [`trackEvent`](<https://www.commandbar.com/docs/sdk/events/trackevent/>) method.

A sample `track` call is shown:
    
    
    rudderanalytics.track("User Signed Up", {});
    

## FAQ

#### **Where can I find the CommandBar organization ID?**

  1. Log in to your [CommandBar dashboard](<https://app.commandbar.com/login>).
  2. In the left navigation bar, click your organization name at the bottom and copy the **Org ID**.

[![CommandBar organization ID](/docs/images/event-stream-destinations/commandbar-org-id.webp)](</docs/images/event-stream-destinations/commandbar-org-id.webp>)