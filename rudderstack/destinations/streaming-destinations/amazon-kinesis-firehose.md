# Amazon Kinesis Firehose

Send your event data from RudderStack to Kinesis Firehose.

* * *

  * __4 minute read

  * 


[Amazon Kinesis Firehose](<https://aws.amazon.com/kinesis/data-firehose/>) gives you an easy and reliable way to load your streaming data into data lakes, data stores, and a host of other analytics tools. It is a fully-managed service that can be scaled automatically to match the load and throughput of your data, without requiring any additional administration.

RudderStack supports Amazon Kinesis Firehose as a destination where you can seamlessly send your event data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/firehose>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Amazon Kinesis Firehose** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Kinesis Firehose, follow these steps:

  1. From your RudderStack dashboard, add the source. Then, from the list of destinations, select **Amazon Kinesis Firehose**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully set up Kinesis Firehose as a destination, you need to configure the following settings:

  * **AWS Region** : Enter the AWS region in which you have created the Kinesis Firehose stream. This is a required field.
  * **Role-based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

  * If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack in order to write to the configured stream.


> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your Kinesis Firehose stream. Refer to the Policy permissions section below for more information.

  * **Mapping event to delivery streams** : Use this setting to map the RudderStack **Event Name** to a Kinesis Firehose **Delivery Stream**.


## Sending events to Kinesis Firehose

RudderStack supports sending the `identify`, `page`, and `track` events to specific Kinesis Firehose streams by configuring them in the dashboard.

You can also send an event `type` as `page`, `identify`, or `track`. For the `track` events, you can specify the event name based on the event name in the payload. For example:

  * If the event name is `page`, RudderStack sends all events with the `type` set to `page`.
  * If event name is `Product Added` , RudderStack sends all track events with the `event` as `Product Added`.


> ![info](/docs/images/info.svg)
> 
> To send all events to a particular stream irrespective of the type or name, you can use `*` as the event name in the dashboard settings.

> ![warning](/docs/images/warning.svg)
> 
> Note that the field **Delivery Stream Name** is case sensitive and has to be specified exactly as named in AWS. On the other hand, the **Event Name** field is not case sensitive, and thus RudderStack does not differentiate between `Page` or `page` before sending it to the Firehose stream.

## Policy permissions

To use the Firehose destination with RudderStack correctly, you must have a Firehose stream created in AWS. For more information on creating a Kinesis Firehose data delivery stream, refer to this [AWS documentation](<http://docs.aws.amazon.com/firehose/latest/dev/basic-create.html>).

You also need to create an IAM role and attach the policy containing the necessary permissions (`PutRecord`) for RudderStack to write to the stream.

  * To create an IAM role, follow the instructions on [Creating an IAM role](<http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html#roles-creatingrole-user-console>).
  * For more information on creating an IAM policy, refer to this [AWS documentation](<http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>).


A sample permissions policy that allows a user to send event data into Kinesis Firehose is shown below:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "firehose:PutRecord"
          ],
          "Resource": [
            "arn:aws:firehose:{region}:{account-id}:stream/{stream-name}"
          ]
        }
      ]
    }
    

## FAQ

#### How does event mapping work with the delivery stream?

  * If there is no delivery stream set for an event in the dashboard settings, RudderStack will not send the event to the Firehose stream.
  * If an event is set with a delivery stream, RudderStack sends the payload to the configured delivery stream.
  * If you have set the event `type`, **Event Name** , and `*` for mapping purposes, RudderStack gives the topmost priority to the event name, followed by `type`, and then `*`. For example, if the type of event is `track` and **Event Name** is `Product Added`, RudderStack does the mapping as shown:

[![](/docs/images/screenshot-2020-07-14-at-10.37.02-pm.webp)](</docs/images/screenshot-2020-07-14-at-10.37.02-pm.webp>)

Then all events go to the stream mapped with `Product Added`.