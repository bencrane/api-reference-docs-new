# Delighted

Send your event data from RudderStack to Delighted.

* * *

  * __5 minute read

  * 


[Delighted](<https://delighted.com/>) is a popular customer feedback platform. It allows your teams to gather instant, invaluable, and actionable customer feedback to improve your processes and product.

RudderStack supports Delighted as a destination to which you can seamlessly send your customer data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/delighted>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Delighted** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source supports sending events to Delighted, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **Delighted**.
  * Give a name to the destination and click **Next**. You should then see the following screen:


[![](/docs/images/Delighted.webp)](</docs/images/Delighted.webp>)Delighted Connection Settings

  * Enter your Delighted **API Key**.


> ![info](/docs/images/info.svg)
> 
> For more information on how to get your Delighted API key, refer to the Delighted [docs](<https://app.delighted.com/docs/api>).

  * By default, the channel is set to **Email**. You can also select **SMS** from the dropdown.
  * Set the **Delay** value (in seconds) here. By default it is set to **0**.
  * To make a `track` call, enter the **Event Names** for which `track` call will be triggered.


> ![warning](/docs/images/warning.svg)
> 
> If the RudderStack dashboard does not contain the **Event** for which the `track` call is triggered, RudderStack will throw an error.

  * Finally, click **Next**. Delighted will now be enabled as a destination in RudderStack.


## Identify

The `identify` call lets you to add a user to your **People** [List](<https://app.delighted.com/people>). If the user already exists, RudderStack will update the user with the latest information. This includes `userId` as well as other additional properties related to user like name,phone number/email, channel, and the ‘Last sent at’ timestamp.

  * The `userId` provided during the call must match the **Channel** type. The channel type can be either set from RudderStack dashboard or you can send it via the `identify` call with the parameter `DelightedChannelType`.


> ![info](/docs/images/info.svg)
> 
> The channel type set via the `identify` call will get a higher precedence.

  * You can provide the user email or phone number. Both are not required at the same time, since one of the values will be set from the `userId`.
  * You can also send the `last_sent_at` value with the call. Refer to the example below for more details.


> ![info](/docs/images/info.svg)
> 
> `Last sent at` (in UNIX timestamp) is used to manually set the time a person was most recently sent a survey. This value will be used in the Delighted **Survey throttling** system, which ensures that same person won’t be surveyed more than once per month.
> 
> To change its value manually, go the Delighted [dashboard](<https://app.delighted.com/dashboard>), select your **Project** from top left corner and click the settings icon beside **Project Name**.

A sample `identify` call is as shown below:
    
    
    rudderanalytics.identify("name@surname.com", {
      name: "User",
      last_sent_at: "1624293839",
      phone_number: "+1234567890"},
      { externalId: [
        {
            type: "delightedChannelType",
            id: "sms"
        }
      ]}
    });
    

In this example, since the `userId` is already an email, you can provide the user’s `phone_number` as well. Also, the `delightedChannelType` will override the **Channel Type** set in the RudderStack dashboard.

> ![info](/docs/images/info.svg)
> 
> Except `userId`, all other fields in the call are optional.

## Track

The `track` call lets you send the survey to the user added to the **People** [List](<https://app.delighted.com/people>) in your account. In addition to name, phone number/email,channel, and the ‘Last sent at’ timestamp, you can also add as many custom properties as you need.

> ![warning](/docs/images/warning.svg)
> 
> If the user does not exist, you cannot make a `track` call. You need to first add the user in the People list via the `identify` call.

> ![info](/docs/images/info.svg)
> 
> The **Delay** value from the dashboard will override the value sent via the `track` call.

A sample `track` call is as shown below:
    
    
    rudderanalytics.track("Test", {
      delighted_email_subject: "Custom Email Subject.",
      customProperty: "Custom Value",
      customProperty2: "Custom Value2"},
      { externalId: [
        {
            type: "delightedChannelType",
            id: "sms"
        }
      ]}
    });
    

In the above example, `Test` is the event name. Except the event name, all other fields are optional.

> ![warning](/docs/images/warning.svg)
> 
> If you do not enter the **Event** name in the dashboard for which the `track` call is triggered, RudderStack will throw an error.

Delighted also provides some custom properties by itself. In the above example, `delighted_email_subject` sets the email subject of the survey to `Custom Email Subject`. Note that this change can be done from the [Delighted website](<https://app.delighted.com/platforms>) too.

Some other default properties provided by Delighted are mentioned in the table below:

**Delighted Property**| **Description**  
---|---  
`question_product_name`| Delighted shows this question in the survey.  
`delighted_intro_message`| Delighted displays this message in the email subject.  
`locale`| This property determines the localization (including language) of the survey experience.  
  
For more default properties, check out this Delighted [support page](<https://help.delighted.com/article/577-special-properties>).

In the example shown above, `customProperty` is the custom property field that you can set. Note that you must provide values for these custom fields, or else they will be dropped by Delighted.

## Alias

The `alias` call allows you to update the user’s email or phone number. You need to set `previousId` as the current value and `userId` as the updated value.

> ![info](/docs/images/info.svg)
> 
> The `previousId` and `userId` must be of the same type, i.e., either email or phone number.

A sample `alias` call is as shown below:
    
    
    rudderanalytics.alias("new@email.com", "old@email.com")
    

> ![info](/docs/images/info.svg)
> 
> Both `previousId` and `userId` are required.