# Statsig

Send your event data from RudderStack to Statsig.

* * *

  * __4 minute read

  * 


[Statsig](<https://statsig.com/>) helps companies safely A/B test features in production before rolling out new features, thereby avoiding costly mistakes.

RudderStack supports Statsig as a destination to which you can send real-time events for efficient A/B testing.

For more information on the Statsig-supported data connectors, see their [documentation](<https://docs.statsig.com/>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Statsig** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Statsig**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in the RudderStack dashboard.  
Secret Key| Enter the server secret key associated with your Statsig project.  
  
### Configuration settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
> ![warning](/docs/images/warning.svg)
> 
> Make sure to enable the RudderStack integration on the [Statsig integration page](<https://console.statsig.com/login?redirect=%2Fintegrations>) before sending any events.
> 
> See [Configuring incoming events in Statsig](<https://docs.statsig.com/integrations/data-connectors/rudderstack/#configuring-incoming-events>) for more information.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

### Retrieve `userId`

To get the `userId` associated with an identified user, you can use the `getUserId()` method as shown:
    
    
    rudderanalytics.getUserId();
    

### Retrieve `anonymousId`

An anonymous ID (`anonymousId`) is an autogenerated UUID (Universally Unique Identifier) that is assigned to each unique, unidentified visitor coming to your website.

You can retrieve the `anonymousId` of any visitor by running the `getAnonymousId()` method:
    
    
    rudderanalytics.getAnonymousId();
    

> ![info](/docs/images/info.svg)
> 
> If the value of `anonymousId` is `null` in the SDK, calling `getAnonymousId()` automatically sets a new `anonymousId` in RudderStack.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record user activities along with their associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 4.0,
      review_body: "Good product."
    })
    

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record your website’s page views with any additional relevant information about the viewed page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever a user views their mobile screen, with any additional relevant information about the viewed screen.

A sample `screen` call sent via the [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                    properties:@{@"prop_key" : @"prop_value"}];
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, like a company, organization, or an account. You can also record any custom traits associated with that group, for example, the company name, number of employees, etc.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("12345", {
      name: "MyGroup",
      industry: "IT",
      employees: 450,
      plan: "basic"
    })
    

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) event lets you merge different identities of a known user.

> ![info](/docs/images/info.svg)
> 
> `alias` is an advanced method that lets you change the tracked user’s ID explicitly. This method is useful when managing identities for some of the downstream destinations.

A sample `alias` call is as shown:
    
    
    rudderanalytics.alias("12345")
    

## FAQ

#### Where can I find the Statsig server secret key?

  1. Log into your [Statsig console](<https://console.statsig.com>).
  2. Go to your project and click the **Settings** icon on the top right:

[![Statsig settings](/docs/images/event-stream-destinations/statsig-settings.webp)](</docs/images/event-stream-destinations/statsig-settings.webp>)

  3. Click **API Keys**. You should find the **Server Secret Key** listed here:

[![Statsig API key](/docs/images/event-stream-destinations/statsig-api-keys.webp)](</docs/images/event-stream-destinations/statsig-api-keys.webp>)

#### Why am I not seeing any events in Statsig even though I am getting a 200 response?

Make sure to enable the RudderStack integration on the [Statsig integration page](<https://console.statsig.com/login?redirect=%2Fintegrations>) before sending any events.