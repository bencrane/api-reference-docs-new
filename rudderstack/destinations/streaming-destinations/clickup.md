# ClickUp Destination

Send your event data from RudderStack to ClickUp.

* * *

  * __6 minute read

  * 


[ClickUp](<https://clickup.com/>) is a productivity tool that lets you set up project workflows and tasks, and enable smooth cross-team collaboration.

RudderStack supports ClickUp as a destination where you can seamlessly send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/clickup>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **ClickUp** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to ClickUp, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **ClickUp**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure ClickUp as a destination, you will need to configure the following settings:

[![ClickUp connection settings](/docs/images/event-stream-destinations/clickup-connection-settings-1.webp)](</docs/images/event-stream-destinations/clickup-connection-settings-1.webp>)

  * **API Token** : Enter your ClickUp API token.
  * **List ID** : Enter your ClickUp list ID.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your ClickUp API token and list ID, refer to the FAQ section below.

  * **Mapping to add custom fields while creating a task** : Use this setting to map a specific RudderStack event property to a ClickUp Custom Field.


> ![info](/docs/images/info.svg)
> 
> For more information on using this setting, refer to the Adding custom fields section below.

> ![info](/docs/images/info.svg)
> 
> You can provide multiple ClickUp custom fields associated with different lists. However, note that the custom field name **must be unique** within a list to successfully create a task.

  * **Client-side Events Filtering** : This setting lets you specify which events should be allowed to flow through to ClickUp.

[![ClickUp connection settings](/docs/images/event-stream-destinations/clickup-connection-settings-2.webp)](</docs/images/event-stream-destinations/clickup-connection-settings-2.webp>)

> ![warning](/docs/images/warning.svg)
> 
> RudderStack will discard the events **not included** in the allowlist.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) calls to create a task in ClickUp.

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Product Viewed", {
        "taskName": "Whole Foods Market",
        "tags": ["plan", "proposal", "marketing"],
        "timeEstimate": 10800000,
        "status": "Proposal",
        "dueDate": "2023-02-25T13:39:21.032Z",
        "startDate": "2022-01-20T13:39:21.032Z",
        "industryKey": "Retail",
        "paymentStatus": "Reject",
        "label": ["Transformer", "QA", "Testing"],
        "location": {
          "lat": -28.016667,
          "lng": 124,
          "formattedAddress": "New Orleans, Louisiana",
        },
        "phone": "+12025550146",
      }, {
        "externalId": [{
            "type": "clickUpListId",
            "id": "199314977",
          },
          {
            "type": "clickUpAssigneeId",
            "id": 61205104,
          },
          {
            "type": "clickUpAssigneeId",
            "id": 61229682,
          },
        ],
      }
    );
    

RudderStack uses the ClickUp [`task`](<https://clickup.com/api/clickupreference/operation/CreateTask/>) endpoint to create a task within a list.

To successfully create a task, you need to specify the List ID in the dashboard settings. You can also pass the list ID through `externalId`, as seen in the above sample snippet.

> ![info](/docs/images/info.svg)
> 
> RudderStack gives preference to the list ID passed via `externalId` over the list ID specified in the dashboard.

### Adding assignees to a task

While creating a task, you can assign it to a Team(Workspace) member by specifying a `userId`. You can also pass multiple `userId` in an `externalId` array:
    
    
    {
      "context": {
        "externalId": [{
            "type": "clickUpAssigneeId",
            "id": 1232
          },
          {
            "type": "clickUpAssigneeId",
            "id": 88765
          }
        ]
      }
    }
    

### Adding custom fields

You can pass the custom fields to ClickUp by specifying the mapping in the **Mapping to add custom fields while creating a task** dashboard setting:

[![ClickUp custom field dashboard setting](/docs/images/event-stream-destinations/clickup-custom-field.webp)](</docs/images/event-stream-destinations/clickup-custom-field.webp>)

You can specify the **ClickUp Custom Field Name** corresponding to the custom field you created in the ClickUp dashboard and the **RudderStack Payload Property** corresponding to the event property present in the payload.

RudderStack uses the custom field name to retrieve the `id` using the [`field`](<https://clickup.com/api/clickupreference/operation/GetAccessibleCustomFields/>) endpoint.

### Supported custom fields

RudderStack supports specifying the following ClickUp custom fields in the dashboard settings:

Custom Field| Notes  
---|---  
URL| Must be in a valid URL format.  
Email| Must be in a valid email format.  
Phone| Must be a valid phone number with a country code, for example, `+1 123 456 7890`.  
Date| Must be a valid date in a datetime format, for example, `2022-02-25T13:39:21.032Z`.  
Text| Must be a string.  
Checkbox| Must be in a Boolean format.  
Number| -  
Currency| Must be a number.  
Emoji (integer)| Used for rating. The value must be in a range defined in the ClickUp dashboard.  
Location| Latitude/longitude and the formatted address must be passed as the [Google Geocoding API](<https://developers.google.com/maps/documentation/geocoding/overview?hl=en>).  
Dropdown| RudderStack uses the dropdown option name to find the UUID using the `field` endpoint.  
Label| RudderStack will use the label name to find the UUID using the `field` endpoint.  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the above-mentioned fields, refer to the the [ClickUp Custom Fields API reference](<https://clickup.com/api/clickupreference/operation/GetAccessibleCustomFields/>).

RudderStack currently **does not support** specifying the following custom fields:

  * Tasks
  * Users
  * Automatic Progress
  * Manual Progress


Note that when sending the custom fields to ClickUp:

  * You can provide multiple custom fields of different ClickUp lists in the dashboard.
  * To successfully create a task, you need to provide a **unique** custom field name within a list in the custom field mapping.


### Supported mapping

The following table lists the mappings between the **optional** RudderStack properties and the ClickUp properties:

RudderStack property| ClickUp property| Data type  
---|---|---  
`context.externalId.id`  
when `context.externalId.type` = `clickUpListId`| `list_id`| String  
`properties.taskName` / `message.event`| `name`| String  
`properties.description`| `description`| String  
`context.externalId.id`  
when `context.externalId.type` = `clickUpAssigneeId`| `assignees`| Array  
`properties.tags`| `tags`| Array  
`properties.priority`| `priority`| Integer  
`properties.timeEstimate`| `time_estimate`| Integer (in ms)  
`properties.status`| `status`| String  
`properties.dueDate`| `due_date`| Datetime  
`properties.includeDueDateTime`| `due_date_time`| Boolean  
`properties.startDate`| `start_date`| Datetime  
`properties.includeStartDateTime`| `start_date_time`| Boolean  
`properties.notifyAll`| `notify_all`| Boolean  
`properties`  
(Only fields mentioned in the dashboard mapping)| `custom_fields`| Array  
  
## Rate limits

Note that the ClickUp enforces rate limits per OAuth and personal token. This rate limit depends on your ClickUp plan and is summarized in the following table:

ClickUp plan| Requests allowed per minute  
---|---  
Free Forever, Unlimited, Business| 100  
Business Plus| 1000  
Enterprise| 10000  
  
> ![info](/docs/images/info.svg)
> 
> For more information, refer to the [ClickUp Pricing](<https://clickup.com/pricing>) page.

## FAQ

#### Where can I find the ClickUp API Token?

To obtain your ClickUp API token, follow these steps:

  1. Log into your [ClickUp dashboard](<https://app.clickup.com/>).
  2. From the left sidebar, click the **Settings** button at the bottom and go to **MY APPS** > **Apps**.
  3. You can find the API token listed here:

[![ClickUp API token](/docs/images/event-stream-destinations/clickup-api-token.webp)](</docs/images/event-stream-destinations/clickup-api-token.webp>)

#### Where can I find the ClickUp List ID?

To get your ClickUp list ID, follow these steps:

  1. In your [ClickUp dashboard](<https://app.clickup.com/>), click the ellipsis button next to your list and select **Copy Link**.

[![ClickUp List ID](/docs/images/event-stream-destinations/clickup-listid-1.webp)](</docs/images/event-stream-destinations/clickup-listid-1.webp>)

  2. Paste the URL in your browser’s URL bar. You can find the list ID in the URL as highlighted in the below image:

[![ClickUp List ID](/docs/images/event-stream-destinations/clickup-listid-2.webp)](</docs/images/event-stream-destinations/clickup-listid-2.webp>)

#### How can I create custom fields in ClickUp?

To create custom fields in your ClickUp list, follow these steps:

  1. In your [ClickUp dashboard](<https://app.clickup.com/>), click the ellipsis button next to your list and go to **List settings** > **Custom Fields**.

[![ClickUp List ID](/docs/images/event-stream-destinations/clickup-custom-fields-1.webp)](</docs/images/event-stream-destinations/clickup-custom-fields-1.webp>)

  2. Choose the type of custom field you want to create and configure the **Field Name** and **Field Type** accordingly.

[![ClickUp List ID](/docs/images/event-stream-destinations/clickup-custom-fields-2.webp)](</docs/images/event-stream-destinations/clickup-custom-fields-2.webp>)

  3. Finally, click **Create**.