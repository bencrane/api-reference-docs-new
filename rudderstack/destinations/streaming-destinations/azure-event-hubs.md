# Azure Event Hubs

Send your event data from RudderStack to Azure Event Hubs.

* * *

  * __3 minute read

  * 


[Azure Event Hubs](<https://docs.microsoft.com/en-us/azure/event-hubs/>) is a data streaming platform and an event ingestion service. It provides a Kafka endpoint which can be used by your existing Kafka-based applications as an alternative to running your own Kafka clusters.

RudderStack supports Azure Event Hubs as a destination to which you can seamlessly send your event data.

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not support the Basic tier of Azure Event Hubs**. For this integration to work, you need to have a standard tier (or higher) of Event Hubs which includes an Apache Kafka endpoint.
> 
> For more information, refer to the Event Hubs’ [pricing page](<https://azure.microsoft.com/en-us/pricing/details/event-hubs/#pricing>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/azure_event_hub>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Azure Event Hubs** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that the platform supports sending events to Azure Event Hubs, perform the steps as mentioned below:

  * Choose a source to which you would like to add Azure Event Hubs as a destination.
  * Select the destination as **Azure Event Hubs**. Give your destination a name, and then click **Next**.
  * In the **Connection Settings** , fill the required fields with the relevant information and click **Next**.


[![Azure Event Hubs Connection Settings](/docs/images/image%20%28100%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29.webp)](</docs/images/image%20%28100%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29.webp>)Azure Event Hubs Connection Settings

### Connection Settings

This section lists the required connection settings to configure Event Hubs as a destination in RudderStack.

  * **Bootstrap server** : The bootstrap server information goes here. This is in the format`hostname of your event hub namespace`:`port`
  * **Topic Name** : The topic name, or the name of the Event Hub that you have created in your [Azure portal](<https://portal.azure.com>).
  * **Event Hubs Connection String** : Your Event Hubs’ primary connection string. For more information, refer to Microsoft’s [How to get Event hubs connection string](<https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string>) guide.


## Partition Key

RudderStack uses `userId` as the partition key of a given message.

> ![info](/docs/images/info.svg)
> 
> If the `userId` is not present in the payload, then `anonymousId` is used.

If you have a multi-partitioned topic, then the records of the same `userId` (or `anonymousId` in absence of `userId`) will always go to the same partition.

## FAQ

#### What is my Bootstrap server address?

The Bootstrap server address is in the following format:

`hostname of Event Hub namespace`: `port`

For example: `NAMESPACENAME.servicebus.windows.net:9093`

Here `NAMESPACENAME` is your event hubs namespace, while `9093` is the port number.

#### Where can I get the Topic name?

The Topic name is the name of the **Event Hub** that you have created in your [Azure portal](<https://portal.azure.com>).

#### Where can I get the Event Hubs connection string?

Event Hubs connection string is the primary connection string of your shared access policy. For more information, refer to Microsoft’s [How to get Event hubs connection string](<https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string>) guide.

#### Why am I getting the “The client is not authorized to access this topic” error?

Check whether you are using the proper Event Hubs connection string for the policy that you have created.

You need to create a policy to write to the Event Hub with a `Send` permission, and put the corresponding primary connection string in the destination settings, as described in the Getting Started section of this guide.