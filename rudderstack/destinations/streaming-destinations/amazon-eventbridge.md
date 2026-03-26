# Amazon EventBridge

Send your event data from RudderStack to Amazon EventBridge.

* * *

  * __3 minute read

  * 


[Amazon EventBridge](<https://aws.amazon.com/eventbridge/>) is a serverless event bus that allows you to connect applications using data from your own apps, integrated SaaS applications, or AWS services.

RudderStack supports Amazon EventBridge as a destination where you can seamlessly send your event data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/eventbridge>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **AWS EventBridge** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to EventBridge, follow these steps:

  1. From your RudderStack dashboard, add the source. Then, from the list of destinations, select **AWS EventBridge**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully set up EventBridge as a destination, you need to configure the following settings:

  * **AWS Region** : Enter the AWS region in which you have created the EventBridge bus. This is a required field.
  * **Role-based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

  * If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack in order to write to the configured event bus.


> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your event bus. Refer to the Policy permissions section below for more information.

  * **Event Bus Name** : Specify the name of the event bus where you want to send the events. RudderStack sends the event to the default bus if no event bus name is specified.
  * **Detail Type** : Specify the event’s detail type to send to EventBridge. This is a **required** field.
  * **Amazon Resource Name:** This field contains an ARN (Amazon Resource Name) that identifies a resource involved in your EventBridge setup. To add multiple ARNs (for multiple targets involved in your setup), click **\+ ADD MORE**.


## Policy permissions

To authorize RudderStack, you need to create an IAM policy that provides the required permission to write to your event bus. Refer to the [Using Identity-Based Policies (IAM Policies) for EventBridge](<https://docs.aws.amazon.com/eventbridge/latest/userguide/iam-identity-based-access-control-eventbridge.html>) guide to know the applicable policies.

A sample permissions policy that allows a user to put event data into EventBridge is shown below:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "CloudWatchEventsInvocationAccess",
          "Effect": "Allow",
          "Action": ["events:PutEvents"],
          "Resource": "*"
        }
      ]
    }
    

## Sending events to EventBridge

You can map a RudderStack event to an EventBridge event in the following manner:

RudderStack| EventBridge  
---|---  
Event payload| `Detail`  
Amazon Resource Name| `Resources`  
Detail Type| `DetailType`  
Event Bus Name| `EventBusName`  
`"rudderstack"`| `Source`  
  
  * **Event Payload** : This is the generated event payload
  * **Amazon Resource Name, Detail Type, Event Bus Name** : These are the values you configured while setting up the destination with RudderStack.