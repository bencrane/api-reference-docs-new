# AWS Personalize

Send your event data from RudderStack to AWS Personalize.

* * *

  * __5 minute read

  * 


[Amazon Personalize](<https://aws.amazon.com/personalize/>) is a machine learning service by AWS. It enables you to create high-quality content recommendations, personalized product and marketing promotions, and much more.

RudderStack supports AWS Personalize as a destination where you can send your event data seamlessly.

> ![info](/docs/images/info.svg)
> 
> To use [`PutUsers`](<https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutUsers.html>) and [`PutItems`](<https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutItems.html>) permissions for this destination, use the latest images for [`rudder-server`](<https://github.com/rudderlabs/rudder-server>) and [`rudder-transformer`](<https://github.com/rudderlabs/rudder-transformer>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/personalize>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **AWS Personalize** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Prerequisites

  * You must have a Personalize service set up in AWS. See the [AWS documentation](<https://docs.aws.amazon.com/personalize/latest/dg/setup.html>) for more information on setting up your Personalize account.
  * Follow these [instructions](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/personalize/scripts>) to generate a Tracking ID required for creating the AWS Personalize destination in RudderStack.


## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **AWS Personalize** from the list of destinations. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
Role-based Authentication| Turn on this toggle to use the [RudderStack IAM role](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>) for authentication.  
IAM Role ARN| You will see this field only if **Role-based Authentication** is enabled.  
  
Enter the ARN of the IAM role in this field.  
Access Key ID| You will see this field only if **Role-based Authentication** is disabled.  
  
Enter your AWS Access Key ID in this field.  
Secret Access Key| Enter the corresponding secret access key in this field.  
Region| Enter the region associated with your AWS account in this field.  
  
> ![info](/docs/images/info.svg)
> 
> In both role-based and access key-based authentication methods, you will need to set a policy specifying the required permissions for RudderStack to send data to Personalize.
> 
> See the Policy permissions section below for more information.

### Dataset group settings

Setting| Description  
---|---  
Tracking ID| Enter the Tracking ID generated in the Prerequisites section above.  
Dataset ARN| Enter the dataset ARN of the dataset from the chosen dataset group.  
  
### Operational choice settings

Setting| Description  
---|---  
Personalize Events| Select the type of Personalize event you want to avail from the dropdown. RudderStack supports the following Personalize events:  
  


  * **PutEvents**
  * **PutItems**
  * **PutUsers**

  
  
### Mapping settings

Setting| Description  
---|---  
Map all fields| Enter the **Schema Field** used to create the schema in AWS Personalize (for example, `USER_ID`, `TIMESTAMP`, `ITEM_ID`, etc.).  
  
Then, enter the corresponding **Mapped Field** — RudderStack takes the value from this field present in the event payload and maps it to the value specified in the **Schema Field**.  
  
See the [Personalize documentation](<https://docs.aws.amazon.com/personalize/latest/dg/data-prep-creating-datasets.html>) for more information on creating a schema in Personalize.  
  


> ![info](/docs/images/info.svg)When using the `PutItems` operation, you need to provide the path to the **Mapped Field** corresponding to the `ITEM_ID` present in your Personalize database schema.  
  
Disable stringifying additional properties| Turn on this toggle to disable the conversion of additional properties to string data type in Personalize.  
  


> ![info](/docs/images/info.svg)This is an exclusive setting only applicable for the `putEvents` operation.  
>   
> If it is disabled, RudderStack converts any mapped fields other than `ITEM_ID`, `EVENT_VALUE`, `IMPRESSION`, `RECOMMENDATION_ID`, `TIMESTAMP`, `EVENT_TYPE`, and `USER_ID` to a string before forwarding to Personalize.  
  
## Policy permissions

To send data to Personalize correctly, you need to create an IAM role and grant the necessary permissions for RudderStack.

The following actions need to be attached to the role while setting up the AWS policy:
    
    
    "Action": [
        "personalize:PutEvents",
        "personalize:PutUsers",
        "personalize:PutItems"
    ]
    

You can use these actions based on the type of Personalize events you want to send. For example, to send only `putEvents` type of events, you can attach only `personalize:PutEvents`.

A sample permissions policy that allows a user to send event data into Personalize is shown below:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "CloudWatchEventsInvocationAccess",
          "Effect": "Allow",
          "Action": [
            "personalize:PutEvents",
            "personalize:PutUsers",
            "personalize:PutItems"
            ],
          "Resource": "*"
        }
      ]
    }
    

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send data to Personalize using the `PutUsers` operation.

Note that:

  * For the `PutUsers` operation, RudderStack sends the value of the `userId` or `anonymousId` field in the event payload as `userId`.
  * You must specify the **Dataset ARN** field in the RudderStack dashboard settings.


The following snippet highlights a sample `identify` event with the **Mapped Field** settings specified in the RudderStack dashboard:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex",
      email: "alex@example.com"
      });
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send data to Personalize using the [`PutEvents`](<https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutEvents.html>) and [`PutItems`](<https://docs.aws.amazon.com/personalize/latest/dg/API_UBS_PutItems.html>) operations.

Note that:

  * For `PutEvents`, RudderStack sends the value of the `event` field in the payload as `EVENT_TYPE`. Also, the value of the `timestamp` or `originalTimestamp` fields in the payload is sent as `sentAt`.
  * For the `PutItems` and `PutEvents` operations, you must specify the **Dataset ARN** and **Tracking ID** settings in the RudderStack dashboard settings.


The following snippet shows a sample `track` event with the mapped fields specified in the RudderStack dashboard settings:
    
    
    rudderanalytics.track("Product Added", {
      typeOfSdk: "JavaScript",
      numberOfRatings: "12",
      X: "item 1",
    });
    

### Using the `PutItems` operation

When using the `PutItems` operation, you must map the **Schema Field** `ITEM_ID` to a specific key in the event payload. You also need to mention the path to the chosen key as the corresponding **Mapped Field**.

In the above example, if you map `ITEM_ID` to the field `X`, the corresponding **Mapped Field** will be `properties.X`.

> ![info](/docs/images/info.svg)
> 
> For any other **Schema Field** in your `ITEMS` dataset, RudderStack does **not** recommend specifying the path — only the field name is sufficient.

The following image shows an example of the dashboard configuration for `PutItems`:

[![](/docs/images/event-stream-destinations/personalize/personalize-putitems.webp)](</docs/images/event-stream-destinations/personalize/personalize-putitems.webp>)

### Using the `PutEvents` operation

When using the `PutEvents` operation, the **Mapped Field** for `ITEM_ID` should **not** contain the path to the field — only the name of the field is sufficient. The same rule is applicable for any other **Schema Field** mapping.

The following image shows an example of the dashboard configuration for `PutEvents`:

[![](/docs/images/event-stream-destinations/personalize/personalize-putevents.webp)](</docs/images/event-stream-destinations/personalize/personalize-putevents.webp>)