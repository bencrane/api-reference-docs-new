# Vitally

Send data from RudderStack to Vitally.

* * *

  * __3 minute read

  * 


[Vitally](<https://vitally.io/?utm_source=rudderstack&utm_medium=docs&utm_campaign=partners>) is a customer success platform for B2B SaaS companies that wraps your unified customer data with powerful analytics, alerts, and workflows to help you build successful customers.

> ![info](/docs/images/info.svg)
> 
> This destination is maintained by Vitally. For any issues, [contact the Vitally Support team](<mailto:support@vitally.io>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Vitally** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Vitally, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Vitally**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Vitally as a destination, you will need to configure the following settings:

  * **API Key** : Enter your Vitally API key. For more information on obtaining the API key, refer to the FAQ section below.


> ![info](/docs/images/info.svg)
> 
> Once Vitally receives at least one event from RudderStack, you will be able to proceed with the setup process and [create accounts from RudderStack](<https://docs.vitally.io/managing-the-customer-lifecycle/account-hierarchy-using-vitallys-organization-object/supported-integrations-and-how-to-create-the-hierarchy#rudderstack>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

A sample `identify` event is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      name: 'Alex Keener',
      email: 'alex@example.com',
      avatar: 'https://example.com/avatars/alexkeener.webp',
      role: 'CEO'
    });
    

Vitally uses the information from the `identify` calls to consolidate the user profile. Also, you can use the traits for sorting and filtering users within an account.

You can view the following `identify` traits in the Vitally dashboard:

Trait| Description  
---|---  
`name`| Sets the username in Vitally.  
`email`| Sets the user’s email.  
`avatar`| Displays the user’s avatar in the Vitally dashboard.  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Enabled Slack Integration', {
      channel: '#support'
    })
    

Vitally uses the `track` calls to track and analyze the account’s (user’s) engagement with your product. It provides out-of-the-box analysis for your events and the ability to define your own custom metrics on top of them, for example, [Success Metrics](<https://docs.vitally.io/account-health-scores-and-metrics/success-metrics>) and [Elements](<https://docs.vitally.io/account-health-scores-and-metrics/elements>).

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group like a company, organization, or an account.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      name: "Initech",
      industry: "Technology",
      plan: "enterprise",
      mrr: 2000
    });
    

Vitally uses the `group` events to maintain a picture of the account. It adds any group traits to the account which you can use to analyze your customer base as a whole. You can view a customer’s traits on their dashboard, use these traits for sorting and filtering, configure rules to automate your customer success process, and much more.

> ![info](/docs/images/info.svg)
> 
> RudderStack sets the group trait `name` as the account name in the Vitally dashboard.

## FAQ

#### Where can I find the Vitally API key?

  1. From your [Vitally dashboard](<https://login.vitally.io/>), go to **Account Settings** > **Product Data** integrations list.
  2. Select and enable the RudderStack integration. You will find the **API key** listed here.