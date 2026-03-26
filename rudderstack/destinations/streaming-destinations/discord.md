# Discord

Send your event data from RudderStack to Discord.

* * *

  * __4 minute read

  * 


[Discord](<https://discord.com/>) is a popular communications app used by gamers to communicate online. It lets you share voice, video, and text chat with friends, game communities, and developers.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/discord>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Discord** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Discord, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Discord**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure Discord as a destination, you need to configure the following settings:

  * **Identify Template** : Enter a template for building a text message while sending an `identify` call to Discord. If not provided, RudderStack uses `User {{name}} with {{traits}} is identified` as the default template.
  * **Event Name** : Enter the event name for which RudderStack should trigger the `track` call’s event template.
  * **Event Template** : Enter a template for building a text message while sending a `track` call to Discord. If not provided, RudderStack uses `User {{name}} did {{event}} with {{properties}}` as the default template.
  * **Regex Matching** : Enable this setting if you want to match multiple event names in the `track` call using a regex. It helps in setting the same event template for the event names matching the regex.
  * **Embed Flag** : Enable this setting to set an embed message for Discord. If enabled, also specify the following:
    * **Title Template** : Enter the template for building the title of the embed message. If not provided, RudderStack uses `Identify/Track call made` as the default title.
    * **Description Template** : Enter the template for building the description of the embed message. If not provided, RudderStack uses `Message from RudderStack` as the default description.
  * **Webhook Url** : Enter the webhook URL of the Discord channel where you want to send the data. You can create it by logging in to [Discord](<https://discord.com/login>), selecting the channel, and going to the **Channel settings** > **Integrations** > **Create Webhook**.
  * **Trait** : Enter all traits you want to send to Discord in the text message.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in Discord.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA"
    });
    

> ![info](/docs/images/info.svg)
> 
> Either one of the `userId` or `anonymousId` is required to make an `identify` call successfully.

RudderStack sends the above `identify` call to Discord in the following text message format (using the default `identify` template):

  * `User Alex Keener with email: alex@example.com, country: USA is identified`
  * When the **Embed Flag** setting is enabled and the default values for **Title Template** and **Description Template** are used:


    
    
    "content": "User Alex Keener with email: alex@example.com, country: USA is identified",
    "embeds": [{
      "description": "Identify call made",
      "title": "Message from Rudderstack "
    }]
    

RudderStack sends the text message in the `content` property after converting it into the `identify` template specified in the dashboard. Also, if the **Embed Flag** setting is enabled, it sends the embed message details in the `embeds` property. Refer to the [Discord documentation](<https://discord.com/developers/docs/resources/webhook>) for more information.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      category: "category",
      label: "label",
      value: 120
    });
    

> ![info](/docs/images/info.svg)
> 
> `event name` is a required property to make a `track` call successfully.

RudderStack sends the above `track` call to Discord in the following text message format (using the default `track` template):

  * `Anonymous user anon_id did Order Completed with category: category, label: label, value: 120`
  * When the **Embed Flag** setting is enabled and the default values for **Title Template** and **Description Template** are used:


    
    
    "content": "Anonymous user anon_id did Order Completed with category: category, label: label, value: 120",
    "embeds": [{
      "description": "Track call made",
      "title": "Message from Rudderstack "
    }]
    

RudderStack sends the text message in `content` property after converting it into the `track` template specified in the **Event Template** dashboard setting. Also, if the **Embed Flag** setting is enabled, it sends the embed message details in the `embeds` property. Refer to the [Discord documentation](<https://discord.com/developers/docs/resources/webhook>) for more information.