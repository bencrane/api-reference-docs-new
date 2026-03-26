# Appcues

Send your event data from RudderStack to Appcues.

* * *

  * __4 minute read

  * 


[Appcues](<https://www.appcues.com/>) is a popular product marketing platform that helps you deliver scalable user experiences and accelerate business growth.

RudderStack supports Appcues as a destination to which you can send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/appcues>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Appcues** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Appcues native SDK from the `https://fast.appcues.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Appcues SDK successfully.

## Get started

Once you have confirmed that the platform supports sending events to Appcues, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Appcues**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up Appcues as a destination, you will need to configure the following settings:

  * **Account ID** : Enter your Appcues account ID. To get the ID, log in to your Appcues account and navigate to **Settings** > **Account**.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Appcues. See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Web SDK settings

  * **Appcues JavaScript Native SDK URL** : Enter the URL for hosting the native Appcues JavaScript SDK. If not specified, RudderStack sets it to `https://fast.appcues.com/${<your_account_id>}.js` by default.
  * **Use device mode to send events** : Turn on this setting to enable sending events to Appcues in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to uniquely identify a user in Appcues.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You must make an `identify` call before making any other call to Appcues.
>   * RudderStack flattens any objects/array properties in the `identify` call before sending it to Appcues by leveraging their `Appcues.identify(userId,[properties])` call.
> 


A sample `identify` call looks like the following snippet:
    
    
    rudderanalytics.identify("userId", {
      name: "John Doe",
      title: "CEO",
      email: "name.surname@domain.com",
      company: "Company123",
      country: "US",
      state: "TX",
    })
    

## Track

Use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track custom events as they occur in your application.

A sample `track` call looks like the following:
    
    
    rudderanalytics.track("Clicked button", {
      color: "red",
      buttonText: "Get started",
    })
    

RudderStack sends the `track` call information to Appcues using its `Appcues.track(eventName, [eventProperties])` call.

## Page

A [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call contains information such as the URL or the name of the web page visited by the user.

A sample `page` call looks like the following:
    
    
    rudderanalytics.page("homepage")
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * In device mode, RudderStack passes the `page` call information to Appcues using its `Appcues.page()` call along with any additional properties passed to it. Appcues checks to see if a user qualifies for an experience every time the page changes. When you first make the `page` call, Appcues checks if there are any current flows associated with the given user and loads them, if necessary.
>   * In cloud mode, RudderStack sends the above `page` call as a `track` event with the name as `Visited a Page` along with any associated properties. It also updates the properties associated with the user profile like user ID, user agent, current page URL, browser langugage, current page title, etc.
> 


## Screen

> ![info](/docs/images/info.svg)
> 
> The `screen` call is available only in the cloud mode.

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method allows you to record whenever a user sees the mobile screen along with any associated optional properties.

A sample `screen` call looks like the following code snippet:
    
    
    [[RSClient sharedInstance] screen:@"Main" properties:@{@"prop_key" : @"prop_value"}];
    

In the above snippet, RudderStack captures screen-related like the screen name and category.

RudderStack sends the above call is sent as a `track` event with the name `Viewed a Screen`, along with any additional properties passed to it.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group like a company, organization, or an account. You can also record any custom traits associated with that group like the company name, number of employees, etc.

A sample `group` call sent to Appcues is shown:
    
    
    rudderanalytics.group("5ea6247", {
      name: "Company Inc.",
      industry: "Technology",
      employees: 4500,
      plan: "basic"
    })
    

## FAQ

#### How do I get the Appcues Account ID?

You can find the Appcues Account ID in the [Appcues Settings Page](<https://login.appcues.com/>).