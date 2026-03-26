# AWS Lambda

Send your event data from RudderStack to AWS Lambda.

* * *

  * __4 minute read

  * 


[AWS Lambda](<https://aws.amazon.com/lambda/>) is a serverless compute service that lets you seamlessly run any application code or service without managing or provisioning servers.

RudderStack supports AWS Lambda as a destination where you can send your event data seamlessly.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **AWS Lambda** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to AWS Lambda, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **AWS Lambda**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure AWS Lambda as a destination, you need to configure the following settings:

[![AWS Lambda connection settings](/docs/images/event-stream-destinations/aws-lambda-connection-settings-1.webp)](</docs/images/event-stream-destinations/aws-lambda-connection-settings-1.webp>)

  * **Region** : Enter the region associated with your AWS Lambda service.


> ![info](/docs/images/info.svg)
> 
> For more information on the AWS regions, refer to the [AWS Regions and Availability Zones](<https://aws.amazon.com/about-aws/global-infrastructure/regions_az/>) guide.

  * **Role-based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

  * If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack.


> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to send data to your Lambda function. Refer to the Policy permissions section below for more information.

  * **Lambda** : Enter the name of the Lambda function to be invoked. RudderStack supports the following formats:

Name format| Example  
---|---  
Function name| 

  * `lambda-function` (Name only)
  * `lambda-function:v1` (Name with alias)

  
Function ARN| `arn:aws:lambda:us-west-2:123456789012:function:my-function`  
Partial ARN| `123456789012:function:lambda-function`  
  
> ![success](/docs/images/tick.svg)
> 
> You can also append a version number or alias to any of the above formats.

  * **Enable Batch Input** : Enable this setting if your lambda function expects a batch input (array of events) in the event object.
    * **Max Batch Size** : If **Enable Batch Input** setting is enabled, use this field to set the maximum size of the event batch.
  * **Client Context** : Use this field to pass up to **3583 bytes** of Base64-encoded data about the invoking client to the function in the context object.


## Policy permissions

To use the Lambda destination with RudderStack correctly, you must have a Lambda function set up in AWS. Refer to the [AWS documentation](<https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html>) for more information on setting up your Lambda function.

You also need to create an IAM role and grant the necessary permissions for RudderStack to send data to your lambda function. For more information, refer to this [AWS documentation](<https://docs.aws.amazon.com/lambda/latest/dg/access-control-identity-based.html>).

The following permission need to be attached to the role while setting up the policy:
    
    
    "Action": ["lambda:InvokeFunction"]
    

A sample permissions policy that allows a user to send event data into AWS Lambda is shown below:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "CloudWatchEventsInvocationAccess",
          "Effect": "Allow",
          "Action": ["lambda:InvokeFunction"],
          "Resource": "*"
        }
      ]
    }
    

## Supported events

> ![info](/docs/images/info.svg)
> 
> This destination accepts raw event data similar to a webhook. RudderStack sends the entire event payload to AWS Lambda as is, without any transformation or modification.

You can send your [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>), and [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) events to your lambda function via RudderStack.

RudderStack leverages the [AWS SDK for Go](<https://docs.aws.amazon.com/sdk-for-go/api/service/lambda/>) to send the events to the lambda function. It uses the SDK’s [`Invoke`](<https://docs.aws.amazon.com/sdk-for-go/api/service/lambda/#Lambda.Invoke>) method to **asynchronously** invoke the lambda function.

> ![warning](/docs/images/warning.svg)
> 
> As RudderStack supports only asynchronous invocation, it only guarantees the order in which the events are triggered. Also, the execution time is completely dependent on the complexity of your lambda function.

> ![info](/docs/images/info.svg)
> 
> It is highly recommended to configure a [dead-letter queue](<https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq>) to save the discarded events for further processing.

## Viewing error logs

RudderStack does not get any information related to the runtime errors for your lambda function. As a result, you will not be able to view these errors in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab of your dashboard.

To view these errors, you can configure the [AWS CloudWatch logs](<https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html>) for your lambda function.

## FAQ

#### Why am I getting a `UnrecognizedClientException`/`InvalidSignatureException` error?

If you’re getting a `UnrecognizedClientException` error with a 403 status code, verify if your AWS credentials (both **AWS Access Key ID** and **Secret Access Key**) are valid.

For the `InvalidSignatureException` error, verify if the provided secret access key is valid.