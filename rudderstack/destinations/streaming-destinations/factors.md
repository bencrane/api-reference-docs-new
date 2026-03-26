# FactorsAI Beta

Step-by-step guide on sending your event data from RudderStack to FactorsAI.

* * *

  * __2 minute read

  * 


[FactorsAI](<https://www.factors.ai/>) is a marketing analytics and attribution platform. It collects and processes all data across your customer journeys to help you make smart business decisions.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/factorsai>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Factors AI** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to FactorsAI, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Factors AI**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure FactorsAI as a destination, you will need to configure the following settings:

  * **API Key** : Enter the FactorsAI API Key. For more information on obtaining your FactorsAI API key, refer to the FAQ section below.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in FactorsAI. RudderStack uses the `userId` field to perform these actions.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4e', {
      email: 'alex@example.com'
    });
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events and their associated properties, and send this information to FactorsAI.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 4.0,
      review_body: "Good product."
    })
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event lets you record your website’s page views with any additional relevant information about the viewed page.

A sample `page` call sent using RudderStack’s JavaScript SDK:
    
    
    rudderanalytics.page("Home")
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user to a group like a company, organization, or an account.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("sample-group-id", {
      name: "Example Company",
      employees: 1000,
      industry: "Software"
    });
    

## FAQ

#### Where can I get the FactorsAI API key?

To get your FactorsAI API key:

  1. Log in to your [FactorsAI dashboard](<https://app.factors.ai/>).
  2. Click the menu button in the left corner and go to **Settings** > **Integrations**.
  3. From the integrations list, select **RudderStack** to generate the API key:

[![FactorsAI API key](/docs/images/event-stream-destinations/factorsai-api-key.webp)](</docs/images/event-stream-destinations/factorsai-api-key.webp>)