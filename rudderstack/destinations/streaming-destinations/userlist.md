# Userlist

Send your event data from RudderStack to Userlist.

* * *

  * __3 minute read

  * 


[Userlist](<https://userlist.com>) is a popular behavior-based messaging platform that lets you engage with your SaaS users effectively through targeted, behavior-based campaigns.

RudderStack supports sending your events to Userlist from the cloud mode S2S (Server to Server) by calling the relevant RudderStack APIs.

> ![success](/docs/images/tick.svg)
> 
> This destination is supported by the Userlist team. You can contact the Userlist team via [[support@userlist.com](<mailto:support@userlist.com>)](<mailto:support@userlist.com>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/userlist>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Userlist** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the platform supports sending events to Userlist, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source and Userlist as a destination.
  * Name your destination, and click **Next**. You should be able to see the following screen:


[![](/docs/images/userlist.webp)](</docs/images/userlist.webp>)Connection settings for Userlist destination

  * Enter the **Userlist Pus Key** which you can find from your [Userlist Push API settings](<https://app.userlist.com/settings/push>).
  * Once the destination is enabled, events from the RudderStack SDK will start to flow to Userlist.


> ![warning](/docs/images/warning.svg)
> 
> Userlist does not support tracking of anonymous users. So, make sure you call `identify` before calling `track`.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call sends the event data to Userlist along with the properties that you pass as the RudderStack traits.

If the `userId` is already known, Userlist will update the user record. Otherwise, it’ll create a new one.

> ![warning](/docs/images/warning.svg)
> 
> Userlist will only process messages with a `userId`. Messages with only an `anonymousId` will be ignored.

The following code snippet is an example of an `identify` call in RudderStack:
    
    
    rudderanalytics.identify("test-user-id", {
      name: "Tintin",
      city: "Brussels",
      country: "Belgium",
      email: "tintin@herge.com",
    })
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call is made to associate the user with a company in Userlist.

An example of a `group` call is as shown:
    
    
    rudderanalytics.group("test-group-id", {
      name: "Example, Inc.",
      industry: "Testing",
      employees: 42,
    })
    

> ![info](/docs/images/info.svg)
> 
> Userlist supports adding properties to the relationship between user and group. As this isn’t officially supported by RudderStack’s message format, you can specify the relationship properties by providing additional data for Userlist specifically.

The following example will associate the currently identified user with the given group (company) and set their `role` for that particular group (company) to `owner`.
    
    
    rudderanalytics.group("test-group-id", {
      name: "Example, Inc.",
      industry: "Testing",
      employees: 42,
      integrations: {
        Userlist: {
          extensions: {
            relationship: {
              properties: {
                role: "owner",
              },
            },
          },
        },
      },
    })
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call will pass the event properties to Userlist. You may call `rudderanalytics.track()` with or without event properties.

The following code snippet shows how a sample `track` call is made in RudderStack:
    
    
    rudderanalytics.track("Project created", {
      project_name: "Demo Project",
    })
    

> ![info](/docs/images/info.svg)
> 
> Note that every `track` call will be sent to Userlist as a new event. You may send additional properties to describe the event in more detail.
> 
> Both the event name and additional properties will be stored with the event and normalized to snake case (`project_created` and `project_name`) automatically within Userlist.

To track an event in the context of a group (company), you need to specify the `groupId` in the `context`:
    
    
    rudderanalytics.track("Project created", {
      project_name: "Demo Project",
      context: {
        groupId: "test-group-id",
      },
    })