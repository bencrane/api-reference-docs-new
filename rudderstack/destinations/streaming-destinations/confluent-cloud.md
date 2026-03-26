# Confluent Cloud

Send your event data from RudderStack to Confluent Cloud.

* * *

  * __2 minute read

  * 


[Confluent Cloud](<https://www.confluent.io/confluent-cloud/>) is a cloud-native, fully-managed event streaming platform. Powered by Apache Kafka, it is simple, secure, and simplifies data ingestion and processing on all major clouds. With Confluent Cloud, you can easily handle large-scale data workloads without compromising on performance.

RudderStack allows you to seamlessly configure Confluent Cloud as a destination to send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/confluent_cloud>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Confluent Cloud** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the platform supports sending events to Confluent Cloud, perform the steps mentioned below:

  * Choose a source to which you would like to add Confluent Cloud as a destination.
  * Select the destination as **Confluent Cloud**. Give your destination a name, and then click **Next**.
  * In the **Connection Settings** , **fill the required fields with the relevant information and click Next.**


[![](/docs/images/screenshot-2020-11-27-at-1.28.49-pm.webp)](</docs/images/screenshot-2020-11-27-at-1.28.49-pm.webp>) Confluent Cloud connection settings

The required fields are as follows:

  * **Bootstrap server** : Enter your bootstrap server information here. This is in the format `hostname:`:`port` . You will get this information in your cluster settings.
  * **Topic Name** : Enter the name of the Kafka topic in this field.
  * **API Key** : This is the key you need to generate in the Confluent Cloud UI to give RudderStack the required API access. Enter the key in this field.
  * **API Secret** : Enter the API Secret in this field - you can generate this in the Confluent Cloud UI.


## Partition Key

RudderStack uses `userId` as the partition key of a given message.

> ![info](/docs/images/info.svg)
> 
> If `userId` is not present in the payload, then `anonymousId` is used.

If you have a multi-partitioned topic, then the records of the same `userId` (or `anonymousId` in the absence of `userId`) will always go to the same partition.