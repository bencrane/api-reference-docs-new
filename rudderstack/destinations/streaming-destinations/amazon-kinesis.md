# Amazon Kinesis

Send your event data from RudderStack to Amazon Kinesis.

* * *

  * __3 minute read

  * 


[Amazon Kinesis](<https://aws.amazon.com/kinesis/>) enables you to ingest, buffer and process streaming data in real-time. It can handle any amount of streaming data and process data from hundreds of thousands of sources with very low latencies along with the flexibility to choose the tools that best suit the requirements of your application.

RudderStack supports Amazon Kinesis as a destination where you can seamlessly send your event data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/kinesis>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Amazon Kinesis** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Kinesis, follow these steps:

  1. From your RudderStack dashboard, add the source. Then, from the list of destinations, select **AWS Kinesis**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully set up Kinesis as a destination, you need to configure the following settings:

  * **Region** : Enter the AWS Region in which you have created the Kinesis stream.
  * **Stream name** : Specify the name of your Kinesis stream.
  * **Role-based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

  * If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack to write to your Kinesis stream.


> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your Kinesis stream. Refer to the Policy permissions section below for more information.

  * **Use MessageId as Partition Key** : By default, RudderStack uses `userId` ( or `anonymousId`, if `userId` is not present in the payload) as the partition key. You can enable this setting to set your event’s `messageId` as the partition key for your Kinesis stream. This enables your data to be more evenly distributed across the shards in the stream.


## Policy permissions

To authorize RudderStack to write to your stream, you must create an IAM policy that provides the necessary permissions to write to your data stream. Refer to [Controlling Access to Amazon Kinesis Data Streams Resources Using IAM](<https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html>) for the applicable policies.

A sample permissions policy is shown below:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": ["kinesis:PutRecord"],
          "Resource": ["arn:aws:kinesis:{region}:{account-id}:stream/{stream-name}"]
        }
      ]
    }
    

## FAQ

#### How do I verify if the events are published to my Kinesis stream?

To verify that RudderStack has successfully sent the events to your configured Kinesis stream, you can check the **Live Events** tab of your source.

To verify if the events are successfully delivered or check for any delivery failures, go to the **Live Events** tab of your configured destination.