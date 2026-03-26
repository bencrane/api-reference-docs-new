# Candu

Send your event data from RudderStack to Candu.

* * *

  * __2 minute read

  * 


[Candu](<https://www.candu.ai/>) is a product experience platform that provides no-code web tools for SaaS applications. It lets software teams to design, refine, and personalize their application’s user interface to create intuitive product experiences.

RudderStack supports Candu as a destination platform where you can send your event data seamlessly.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/candu>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Candu** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Candu, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Candu**.

[![Candu connection settings](/docs/images/event-stream-destinations/candu-connection-settings.webp)](</docs/images/event-stream-destinations/candu-connection-settings.webp>)

## Connection settings

To successfully configure Candu as a destination, you will need to configure the following settings:

  * **API Key** : Your API Key is the unique key generated against your Candu account. You can find it under the **Settings** > **Workspaces** > **Access Keys** section of your Candu account. Refer to the FAQ section for more details.


## Identify

The `identify` call lets you capture the details of a visiting user along with any associated traits such as their name, email address, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("webUser01", {
      email: "abc@mail.com",
      firstName: "Name",
      lastName: "LastName",
      phoneNumber: "22222222",
      dateOfBirth: "xxxx-xx-xx",
      custom_fields: {
        key1: "value1",
        key2: "value2",
      },
    });
    }
    

## Track

The `track` call lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Promotion Clicked', {
      promotion_id: 'promo1',
      creative: 'banner1',
      name: 'sale',
      position: 'home_top'
    });
    

> ![warning](/docs/images/warning.svg)
> 
> When sending events to Candu, make an `identify` call before the `track` call. This ensures that no duplicate user identities are created in the Candu platform.

## FAQ

#### Where can I get the API key in Candu?

  1. Login to your Candu account.
  2. Go to the **Settings** option.
  3. Look for the API key under **Access Keys** section in the **Workspaces** tab.[![API Key Candu Account](/docs/images/event-stream-destinations/candu-api-key.webp)](</docs/images/event-stream-destinations/candu-api-key.webp>)