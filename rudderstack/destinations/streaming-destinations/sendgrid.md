# SendGrid Destination

Send your event data from RudderStack to SendGrid.

* * *

  * __10 minute read

  * 


[SendGrid](<https://sendgrid.com/>) is a cloud-based email marketing platform built for marketers and developers. It helps businesses deliver billions of transactional and marketing emails every month.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/sendgrid>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Sendgrid** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to SendGrid, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **SendGrid**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure SendGrid as a destination, you will need to configure the following settings:

  * **API Key** : Enter your SendGrid API Key. Refer to the [SendGrid documentation](<https://docs.sendgrid.com/ui/account-and-settings/api-keys>) for more information on obtaining the API Key.
  * **Email Subject** : Enter the subject of the email. You can also send it via the `subject` field in the `track` call’s properties. For more information, refer to the Track section below.
  * **Template ID** : Enter the **Template ID** present in your [SendGrid dashboard](<https://app.sendgrid.com/>) > **Email API** > **Dynamic Templates**. You can also set the Template ID via the `templateId` field in the `track` call’s properties.


> ![info](/docs/images/info.svg)
> 
> `templateId` in the `track` call gets higher priority over the **Template ID** specified in the RudderStack dashboard.

  * **Get email ID from traits** : Enable this setting to let RudderStack search for the user’s `email` inside the user’s `traits`. If found, you can send an event to SendGrid without any `track` call properties.


> ![warning](/docs/images/warning.svg)
> 
> This option is only useful when there are no properties in the `track` call. SendGrid requires either the `templateId` or `content` for a successful event delivery.

  * **Reply-To Email** : Enter the email address where the email reply or bounce should be returned.
  * **Reply-To Name** : Enter the user’s name associated with the above email address.


> ![info](/docs/images/info.svg)
> 
> You can also send the email ID and name in the `replyTo` field in the `track` call’s properties. Note that these fields will override the **Reply-To Email** and **Reply-To Name** fields set in the RudderStack dashboard.

> ![info](/docs/images/info.svg)
> 
> For more information on how to send these details via the `replyTo` object, refer to the replyTo section below.

  * **IP Pool Name** : Enter your SendGrid IP Pool name. For detailed steps on creating an IP pool, refer to the [SendGrid documentation](<https://docs.sendgrid.com/ui/account-and-settings/ip-pools#create-an-ip-pool>).


> ![info](/docs/images/info.svg)
> 
> The length of the IP Pool name must be between 2 and 64 characters.

  * **SendGrid Contact List Id** : Enter the SendGrid’s contact list ID where you want to create a contact. Refer to the [SendGrid documentation](<https://docs.sendgrid.com/api-reference/lists/get-all-lists>) to use their API endpoint to retrieve all your contact lists with their IDs.
  * **Map your traits to SendGrid custom fields** : Use this setting to map the RudderStack properties with SendGrid’s custom fields.


#### From

  * **Email ID** : Enter the user’s email address through which the email will be sent. For more information on creating a verified sender identity, refer to this [SendGrid documentation](<https://docs.sendgrid.com/ui/sending-email/sender-verification>).

  * **Name** : Enter the name associated with above email ID.


> ![info](/docs/images/info.svg)
> 
> You can also include `email` and `name` inside the `from` object in the `track` call (shown below). Note that this will override the **Email** and **Name** fields specified in the RudderStack dashboard.
    
    
    from:{
        "email": "test@email.com",
        "name": "test"
    }
    

#### Event names

  * **Event** : Create the list of events for which RudderStack makes the `track` calls.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack **discards** any `track` call made with an event name that is not specified in this list.

#### Content

  * **Type** : Enter the type of value for the content of your email.
  * **value** : Enter the actual value to be included in the email.


> ![info](/docs/images/info.svg)
> 
> You can also send the `content` array via the `track` properties (shown below) which will override the dashboard settings.
    
    
    content: [
        {
            "type": "text/plain",
            "value": "sample text"
        }
    ]
    

#### Attachments

Use the **Attachments** settings to specify any attachments you want to include in your email. The individual settings are as follows:

  * **Content** : This should be a Base64-encoded string.
  * **Type** : The attachment **type** contains the type of content you are attaching, for example, `"text/plain"`, `"text/html"`, etc.
  * **Filename** : Use this setting to specify the attachment’s file name.
  * **Disposition** : This option specifies how you would like the attachment to be displayed.
  * **Content ID** : Use this option when **disposition** is set to `inline` and the attachment is an image.


> ![info](/docs/images/info.svg)
> 
> SendGrid requires that each attachment element must contain **content** and **filename**. The attachments can also be sent via the `track` call (shown below), which will override the dashboard settings.
    
    
    attachments:[
        {
            "content": "base64encodedString",
            "filename": "index.html",
            "type": "text/html",
            "disposition": "attachment"
        }
    ]
    

#### ASM

The **ASM** settings allow you to handle the user’s unsubscribing activity. The configurable options are:

  * **Group ID** : This option specifies the unsubscribe group to associate with this email.
  * **Groups** : This option contains the array of unsubscribing groups that would be displayed in the unsusbcribing preferences page.


> ![info](/docs/images/info.svg)
> 
> SendGrid requires that the **Group ID** should always be present if the `asm` object is to be sent.

#### Email settings

  * To include a default footer in every mail, enable the **Footer** option. When enabled, the **text** option contains the plain content of footer. The **HTML** contains the HTML content of footer.


> ![info](/docs/images/info.svg)
> 
> The footer can also be sent via `track` properties (shown below), which will override the dashboard settings.
    
    
    mailSettings:{
        "footer": true,
        "footerText": "plain text",
        "footerHtml": "html content"
    }
    

  * To send a test mail and ensure everything is correct, you can enable the **Sandbox Mode** setting.


> ![info](/docs/images/info.svg)
> 
> The sandbox mode can also be enabled or disabled via the `track` properties (shown below), which will override the dashboard setting.
    
    
    mailSettings:{
        "sandboxMode": true
    }
    

#### Tracking settings

The following table describes the various tracking settings to be configured in the RudderStack dashboard:

**Setting**| **Description**  
---|---  
**Click Tracking**|  Allows you to track if a recipient clicked a link in your email.  
**Click Tracking enable text**|  Indicates if this setting should be included in the text/plain portion of your email.  
**Open Tracking**|  Allows you to track if the email was opened by including a single pixel image in the body of the content.  
**Substitution Tag**|  When **Open Tracking** is enabled, this setting allows you to specify a substitution tag that you can insert in the email body at a specific location.  
**Subscription Tracking**|  Allows you to insert a subscription management link at the bottom of your email’s text and HTML bodies.  
**Text**|  When **Subscription Tracking** is enabled, this setting refers to the string to be appended to the email with the subscription tracking link.  
**HTML**|  When **Subscription Tracking** is enabled, this is appended to the email with the subscription tracking link.  
**Substitution Tag**|  Refers to the tag that will be replaced with the unsubscribe URL.  
**GAnalytics**|  Allows you to enable Google Analytics tracking.  
**utm source**|  Refers to the name of the referrer source, e.g. Google.  
**utm medium**|  Refers to the name of the marketing medium, e.g. Email.  
**utm term**|  This setting is used to identify any paid keywords.  
**utm content**|  Allows you to differentiate your campaign from advertisements.  
**utm campaign**|  Corresponds to the name of the campaign.  
  
> ![info](/docs/images/info.svg)
> 
> The **utm source** , **utm medium** , **utm term** , **utm content** , **utm campaign** options are associated with the **GAnalytics** setting on the dashboard.

Finally, click **Next** to complete the setup. SendGrid will now be enabled as a destination in RudderStack.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a new contact in SendGrid based on their email ID. If the email ID already exists, RudderStack updates the contact details.

RudderStack sends the `identify` events to SendGrid in a batch where the batch limit is 30000.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      name: "Alex Keener",
      email: "alex@example.com"
    }, {
      "externalId": [{
        "type": "listIds",
        "id": ["037ae8d4-25b4-496e-adff-2fded15fd0c5", "137ae8d4-25b4-496e-adff-2fded15fd0c3"]
      }],
    });
    

You can pass the SendGrid `listId` in any of the following ways:

  * In the `externalId` object as shown in the above code snippet (takes the highest precedence)
  * In the **SendGrid Contact List Id** RudderStack dashboard setting.


### Supported mappings

The following table lists the property mappings betweeen RudderStack and SendGrid:

RudderStack property| SendGrid property  
---|---  
`email`  
Required| `email`  
`city`| `city`  
`country`| `country`  
`first_name`| `first_name`  
`last_name`| `last_name`  
`postal_code`| `postal_code`  
`state_province_region`| `state`  
`address_line_1`| `address`  
`phone_number`| `phone_number`  
  
> ![info](/docs/images/info.svg)
> 
> If you send any custom field in the event payload, make sure it is present in SendGrid and mapped in the **Map your traits to SendGrid custom fields** RudderStack dashboard setting.

### Deleting a user

You can delete a contact in SendGrid using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![info](/docs/images/info.svg)
> 
> To delete a user, you must specify their `userId` in the event. Additionally, you can specify a custom identifier (optional) in the event.

A sample regulation request body for deleting a user in SendGrid is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
          "userId": "eab57ccf-6322-498e-9338-7761c6dc0656"
        },
        {
          "userId": "47983ca9-7cc6-4942-8ff0-ac443g95658d"
        }
      ],
    }
    

## Track

The `track` call lets you send an event to SendGrid along with its properties. **Note that the properties specified in the`track` call will override the settings specified in the RudderStack dashboard.**

> ![warning](/docs/images/warning.svg)
> 
> Note that SendGrid requires either the `templateId` or `content` to be present in the body. Otherwise, the event will be **discarded**.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('testing',
          {
              "personalizations": [
              {
                "to": [
                  {
                    "email": "recipient@email.com",
                    "name": "Name"
                  }
                ],
                "cc": [
                    {
                        "email": "ccUser@gmail.com",
                        "name": "CCUser"
                    },
                    {
                        "email": "ccUser2@gmail.com",
                        "name": "CCUser2"
                    }
                ],
                "subject": "subject"
              }
            ],
            "from": {
                "email": "test@email.com",
                "name": "Name here"
            },
            "attachments":[
                {
                    "content": "base64encodedString",
                    "filename": "index.html",
                    "type": "text/html",
                    "disposition": "attachment"
                }
            ],
            "content":[
                {
                    "type": "text/html",
                    "value": "<p>Hello</p>"
                }
            ],
            "templateId": "value",
            "headers":{
                "key": "value"
            },
            "customArgs":{
                "key": "value"
            },
            "categories": ["sample","values","here"],
            "sendAt": 1617260400,
            "batchId": "some valid batch ID",
            "subject": "Subject Value",
            "mailSettings":{
              "bypassBounceManagement": true,
              "bypassSpamManagement": true,
              "bypassUnsubscribeManagement": true,
              "footer": true,
              "footerText": "text",
              "footerHtml": "html",
              "sandboxMode": true
            },
            "replyTo":{
              "email": "testingreplyto@email.com",
              "name": "Name"
            },
            "replyToList":[
                {
                    "email": "test@gmail.com",
                    "name": "Test"
                }
            ],
            "field1": "value"
      });
    

The following sections highlight some important things to keep in mind while using the `track` call to send customer data to SendGrid.

### `categories`

SendGrid allows the `categories` array to have a maximum of 10 values.

### `customArgs`

If `customArgs` is not provided in the `track` call, the non-default fields are taken as custom fields. In the sample `track` call above, `field1` will be mapped inside `customArgs`.

### Email settings

To send the event to SendGrid successfully, the following points must be kept in mind:

  * In the `mailSettings`, you cannot combine `bypassListManagement` with `bypassBounceManagement`, `bypassSpamManagement`, and `bypassUnsubscribeManagement`.

  * If `bypassListManagement` is present, then neither `bypassSpamManagement`, `bypassBounceManagement`, or `bypassUnsubscribeManagement` can be present.


### `personalizations`

SendGrid requires that the `personalizations` array should be present in every event and each object must contain the field `to`.

  * If the **Get email ID from traits** option is enabled in the RudderStack dashboard and the properties are not sent in track call, RudderStack will look for `email` in the event traits. If found, RudderStack will create a `personalizations` object and assign `email` to the `to` field.

  * In case both **Template ID** and **content** are not assigned in the dashboard settings, the event will **not** be sent as either of `templateId` or `content` is required.


### `replyTo`

Note that SendGrid does not allow only `name` to be sent in the `replyTo` object. `email` must be present too, otherwise the `replyTo` object will be ignored.

A sample `replyTo` object is as shown:
    
    
    replyTo:{
        "email": "test@email.com",
        "name": "test"
    }
    

### `asm`

It is mandatory to have the `groupId` field inside the `asm` object.

### Event name

As mentioned in the Connection settings section above, the event names for which a `track` call is made must be specified in the RudderStack dashboard. In the sample `track` call above, `testing` is the event name that should be configured in the RudderStack dashboard. Otherwise, this event will be discarded.

### `content`

Each object inside `content` array must contain the `type` and `value` fields. If these fields are absent, then the object will be dropped. However, note that the event will **not** be discarded.

### `attachments`

Each object inside attachments array must at least contain the `content` and `filename` fields. If these fields are absent, then the object will be dropped. However the event will **not** be discarded.