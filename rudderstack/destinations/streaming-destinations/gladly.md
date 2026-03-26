# Gladly Beta

Send your event data from RudderStack to Gladly.

* * *

  * __2 minute read

  * 


[Gladly](<https://www.gladly.com/>) is a customer service platform that leverages AI to deliver personalized agent-assisted customer service and enhance customer relationships.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/gladly/>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse
  * Refer to it as **Gladly** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Gladly**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Gladly as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **API Token** : Enter your Gladly API token by going to **Settings** > **API Tokens** in your Gladly dashboard.
  * **Domain** : Enter your Gladly domain.
  * **User Name** : Enter your Gladly agent email. You can find it in your Gladly dashboard under **Settings** > **Users** > **Email**.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send user details like profile and contact information, notes, and transactions to Gladly.

RudderStack sends this information to Gladly using their [`Customers`](<https://developer.gladly.com/rest/#tag/Customers>) REST API endpoint.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      createdAt: "Mon May 19 2019 18:34:24 GMT+0000 (UTC)",
    })
    

### Traits mapping

RudderStack maps the following `identify` traits to the [Gladly attributes](<https://developer.gladly.com/rest/#operation/createCustomer>):

RudderStack property| Gladly property| Data type  
---|---|---  
`userId`  
Required| `id`| String  
`traits.name`  
`context.traits.name`| `name`| String  
`traits.email`  
`context.traits.email`| `emails[0].original`| String  
`traits.phone`  
`context.traits.phone`| `phones[0].original`| String  
`traits.image_url`  
`context.traits.image_url`| `image`| String  
`traits.address`  
`context.traits.address`| `address`| String  
`externalId`| `externalCustomerId`| String  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack sends any other user information apart from the above-mentioned traits as `customAttributes`.

Note that RudderStack currently does not support additional email properties. However, you can send this information to Gladly by sending an `emailProperties` object in your event as follows:
    
    
    {
      "emailProperties": [{
          "<traits.email1>": {
            "normalised": "",
            "primary": true,
            "newKey": ""
          }
        },
        {
          "<traits.email2>": {
            "normalised": "",
            "primary": false,
            "newKey": ""
          }
        }
      ]
    }
    

## FAQ

#### **Where can I find the Gladly API token?**

  1. Log in to your Gladly dashboard.


> ![warning](/docs/images/warning.svg)
> 
> Each organization has its own unique Gladly login URL. Make sure to log in using the correct URL. Contact your Gladly customer success team for more information.

  2. Go to **Settings**. Under **APP DEVELOPER TOOLS** , click **API Tokens**.

[![Gladly API token](/docs/images/event-stream-destinations/gladly-api-token.webp)](</docs/images/event-stream-destinations/gladly-api-token.webp>)