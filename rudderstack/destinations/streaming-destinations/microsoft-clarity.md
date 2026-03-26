# Microsoft Clarity

Send your event data from RudderStack to Microsoft Clarity.

* * *

  * __3 minute read

  * 


[Microsoft Clarity](<https://clarity.microsoft.com/>) is a heatmap and session recording tool that helps you better understand how users are interacting with your website.

RudderStack supports Microsoft Clarity as a web device mode destination to which you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Microsoft Clarity** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Microsoft Clarity** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Project ID| Enter your Microsoft Clarity project ID.  
Microsoft Clarity Cookie Consent| Turn on this toggle to allow RudderStack to call the Microsoft Clarity API to track the users using a cookie.  
  


> ![info](/docs/images/info.svg)If the **Cookies** setting is enabled in the Clarity project settings, then you need not enable the **Microsoft Clarity Cookie Consent** dashboard setting.  
  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Microsoft Clarity.  
  
See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information on this setting.  
Use device mode to send events| This setting is toggled on by default as this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) events to create a new user in Microsoft Clarity.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com"
    });
    

By default, Clarity uses cookies to track your users and gather the session data. You can configure your Clarity project to require [cookie consent](<https://learn.microsoft.com/en-us/clarity/cookie-consent>), that is, Clarity **will not** place a cookie until a user provides consent.

[![Microsoft Clarity cookie consent enabled](/docs/images/event-stream-destinations/clarity-cookie-consent.webp)](</docs/images/event-stream-destinations/clarity-cookie-consent.webp>)

In this case, to track the user sessions via the cookie, make sure to enable the **Microsoft Clarity Cookie Consent** setting in the RudderStack dashboard. This setting indicates that RudderStack can call the Clarity API to track the users via a cookie once a user provides consent.

### Supported mappings

RudderStack maps the following `identify` attributes to the corresponding Microsoft Clarity properties:

RudderStack property| Microsoft Clarity property  
---|---  
`userId`  
Required| `customuserid`  
`context.sessionId`| `customsessionid`  
`context.traits.customPageId`| `custompageid`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events to send custom events to Microsoft Clarity. RudderStack maps these events to Clarity’s [custom events](<https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#add-custom-events>) to help you track specific user actions on your website.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added", {
      productId: "123",
      category: "Shoes"
    });
    

RudderStack maps the `track` event to Microsoft Clarity’s API by sending the event name to Clarity. The implementation uses the following mapping:
    
    
    window.clarity("event", "Product Added");
    

> ![warning](/docs/images/warning.svg)
> 
> Microsoft Clarity’s custom events accept only the event name. Event properties are not supported and will be ignored.

### Automatic mappings

Microsoft Clarity automatically classifies your `track` events to the following [Smart Events](<https://clarity.microsoft.com/blog/an-overview-of-smart-events/>), based on your [pre-configured mappings specified in the Microsoft Clarity dashboard](<https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events>):

  * `Purchase`
  * `Add to Cart`
  * `Begin Checkout`
  * `Contact Us`
  * `Submit Form`
  * `Request Quote`
  * `Sign Up`
  * `Login`
  * `Download`


## FAQ

#### Where can I find the Microsoft Clarity project ID?

To get your Microsoft Clarity project ID, follow these steps:

  1. Log into your [Microsoft Clarity dashboard](<https://clarity.microsoft.com/projects>).
  2. Select your Microsoft Clarity project and go to **Settings** > **Overview** to get your project ID:

[![Microsoft Clarity project ID](/docs/images/event-stream-destinations/clarity-project-id.webp)](</docs/images/event-stream-destinations/clarity-project-id.webp>)