# Pendo

Send your event data from RudderStack to Pendo.

* * *

  * __3 minute read

  * 


[Pendo](<https://www.pendo.io/>) is a popular product analytics platform that allows you to better understand your customers, and deliver personalized, guided product journeys for them.

RudderStack allows you to configure Pendo as a destination to which you can send your event data seamlessly, for delivering personalized user experiences.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Pendo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Pendo native SDK from the`https://cdn.pendo.io/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Pendo SDK successfully.

## Get started

Once you have ascertained that the platform is supported by Pendo, please follow these steps:

  * Choose a source to which you would like to add Pendo as a destination.
  * Select the destination as **Pendo** to your source. Give your destination a name and then click **Next**.
  * On the **Connection Settings** page, fill all fields with the relevant information and click **Next**.

[![](/docs/images/screenshot-2020-11-27-at-2.29.18-pm.webp)](</docs/images/screenshot-2020-11-27-at-2.29.18-pm.webp>)

> ![info](/docs/images/info.svg)
> 
> To get the Pendo **API Key** , follow these steps:
> 
>   1. Login to Pendo dashboard.
>   2. Go to the **Settings** on the left sidebar and click **Subscription Settings**.
>   3. You will see an option called **Apps** and under that hover on the square box and click **view app details**.
>   4. Here you will find your **API Key** in **App Details** section.
> 


## Identify

To identify a user to Pendo, you need to call the `identify` API. When you send an `identify` call, RudderStack will pass that user’s information to Pendo with `userId` as Pendo’s visitor ID. The user traits that you pass are mapped to visitor metadata in Pendo.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("name123", {
      name: "Name Surname",
      first_name: "Name",
      last_name: "Surname",
      email: "name@surname.com",
      createdAt: "Thu Mar 24 2020 17:46:45 GMT+0000 (UTC)",
    })
    

## Group

You can use the `group` call to create or update an account in Pendo. When you send a Group call, RudderStack sends the `groupId` to Pendo as account ID. The group traits are mapped to account metadata in Pendo.

> ![info](/docs/images/info.svg)
> 
> If you are using your Pendo account data, the group calls (with fields `groupId` & `traits`) are required.

Here is a sample `group` call:
    
    
    rudderanalytics.group("groupId", {
        "name": "Company",
        "industry": "Industry",
        "employees": 123,
        "email": abc@xyz.com
      }
    );
    

## Track

The `track` call allows you to capture any action that the user might perform, along with the properties that are associated with that action. Each action is considered to be an event.

Here is a sample `track` call:
    
    
    rudderanalytics.track("test track event", {
      revenue: 30,
      currency: "USD",
      userId: "12345",
    })
    

## FAQ

#### Where do I find the Pendo API Key?

  * Login to Pendo dashboard.
  * Go to the **Settings** on the left sidebar and click **Subscription Settings.**
  * You will see an option called **Apps** and under that hover on the square box and click **view app details**.
  * Here you will find your **API Key** in **App Details** section.