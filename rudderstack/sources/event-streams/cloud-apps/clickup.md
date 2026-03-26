# ClickUp Source

Ingest your event data from ClickUp into RudderStack.

* * *

  * __4 minute read

  * 


[ClickUp](<https://clickup.com/>) is a productivity tool that lets you set up project workflows and tasks, and enable smooth cross-team collaboration.

You can use RudderStack’s [Webhook](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/webhook-source/>) source to capture real-time updates from your ClickUp workspace and send that data to your preferred downstream destinations.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Webhook**.
  2. Assign a name to your source and click **Continue**.
  3. Your source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![ClickUp source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Go to your [ClickUp dashboard](<https://app.clickup.com/>) and open the ClickUp [space](<https://help.clickup.com/hc/en-us/articles/6309466958103-Spaces-overview>) of your choice.
  5. From the top-right side of the dashboard, click the **Automate** option and select **Add Automation**.

[![ClickUp add automation](/docs/images/event-stream-sources/clickup-add-automation.webp)](</docs/images/event-stream-sources/clickup-add-automation.webp>)

  6. Select the relevant ClickUp trigger from the dropdown under **When** for the automation to happen.
  7. In the **Then** section, select **Call webhook** from the dropdown.
  8. Enter the webhook URL copied in step 3, as shown below. You can also add specific fields in the event sent to the webhook.

[![ClickUp source webhook URL](/docs/images/event-stream-sources/clickup-configure-automation.webp)](</docs/images/event-stream-sources/clickup-configure-automation.webp>)

  9. Click **Create**.


## How RudderStack creates the event payload

This section details how RudderStack receives the data from ClickUp source and creates the resulting payload.

A sample payload ingested by RudderStack when you create a new task in ClickUp is shown below:
    
    
    {
      "event": "taskCreated",
      "history_items": [{
          "id": "2800763136717140857",
          "type": 1,
          "date": "1642734631523",
          "field": "status",
          "parent_id": "162641062",
          "data": {
            "status_type": "open"
          },
          "source": null,
          "user": {
            "id": 183,
            "username": "Alex",
            "email": "alex@example.com",
            "color": "#7b68ee",
            "initials": "A",
            "profilePicture": null
          },
          "before": {
            "status": null,
            "color": "#000000",
            "type": "removed",
            "orderindex": -1
          },
          "after": {
            "status": "to do",
            "color": "#f9d900",
            "orderindex": 0,
            "type": "open"
          }
        },
        {
          "id": "2800763136700363640",
          "type": 1,
          "date": "1642734631523",
          "field": "task_creation",
          "parent_id": "162641062",
          "data": {},
          "source": null,
          "user": {
            "id": 183,
            "username": "Alex",
            "email": "alex@example.com",
            "color": "#7b68ee",
            "initials": "A",
            "profilePicture": null
          },
          "before": null,
          "after": null
        }
      ],
      "task_id": "1vj37mc",
      "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204"
    }
    

RudderStack transforms the above payload into the following [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) payload:
    
    
    {
      "type": "track",
      "event": "webhook_source_event",
      "properties": {
        "event": "taskCreated",
        "history_items": [{
            "id": "2800763136717140857",
            "type": 1,
            "date": "1642734631523",
            "field": "status",
            "parent_id": "162641062",
            "data": {
              "status_type": "open"
            },
            "source": null,
            "user": {
              "id": 183,
              "username": "Alex",
              "email": "alex@example.com",
              "color": "#7b68ee",
              "initials": "A",
              "profilePicture": null
            },
            "before": {
              "status": null,
              "color": "#000000",
              "type": "removed",
              "orderindex": -1
            },
            "after": {
              "status": "to do",
              "color": "#f9d900",
              "orderindex": 0,
              "type": "open"
            }
          },
          {
            "id": "2800763136700363640",
            "type": 1,
            "date": "1642734631523",
            "field": "task_creation",
            "parent_id": "162641062",
            "data": {},
            "source": null,
            "user": {
              "id": 183,
              "username": "Alex",
              "email": "alex@example.com",
              "color": "#7b68ee",
              "initials": "A",
              "profilePicture": null
            },
            "before": null,
            "after": null
          }
        ],
        "task_id": "1vj37mc",
        "webhook_id": "7fa3ec74-69a8-4530-a251-8a13730bd204"
      },
      "anonymousId": "12e90bef-e7c6-44c7-a09a-b9b5478630f7"
    }
    

> ![info](/docs/images/info.svg)
> 
> To send this data to the downstream destinations, you need to transform it into a destination-specific format using RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature. Refer to the below use case for more information.

## Use case

Consider a scenario where a new contact is automatically created in HubSpot whenever a new assignee is added to a ClickUp task.

To do this, set up a ClickUp source by following the steps in the Getting started section above. Connect this source to the [HubSpot destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/>).

Once the connection is set up, RudderStack automatically receives a payload from ClickUp whenever a new assignee is added to a ClickUp task. It then transforms the payload in the following format:
    
    
    {
      "anonymousId": "38c5a078-c1ea-4024-9628-7f8971aeb915",
      "event": "webhook_source_event",
      "messageId": "cbd5e04a-8e0b-4bf9-959d-26c4d8e455b0",
      "properties": {
        "event": "taskAssigneeUpdated",
        "history_items": [{
          "after": {
            "color": "#02579b",
            "email": "alex@example.com",
            "id": 61217234,
            "initials": "A",
            "profilePicture": null,
            "username": "Alex"
          },
          "data": {},
          "date": "1663044688239",
          "field": "assignee_rem",
          "id": "3141509348132974740",
          "parent_id": "175476135",
          "source": null,
          "type": 1,
          "user": {
            "color": "#536cfe",
            "email": "jane@doe.com",
            "id": 55300044,
            "initials": "JD",
            "profilePicture": null,
            "username": "Jane Doe"
          }
        }],
        "task_id": "2rc0nvx",
        "webhook_id": "3425a884-4f24-4d81-a373-1991c2d20743"
      },
      "rudderId": "0240a617-9492-47f8-ac5c-c842ab2cd9f4",
      "type": "track"
    }
    

To automatically add a new contact in HubSpot for this event, you need to add the following user transformation and [connect it to your HubSpot destination](<https://www.rudderstack.com/docs/transformations/overview/#connecting-transformation-to-a-destination>):
    
    
    export function transformEvent(event, metadata) {
      let indetifyEvent;
    
      if (event.properties.event === "taskAssigneeUpdated") {
        indetifyEvent = {
          type: "identify",
          userId: event.properties?.history_items[0]?.after?.id,
          traits: {
            email: event.properties?.history_items[0]?.after?.email
          }
        }
      }
      return indetifyEvent;
    }
    

RudderStack sends the following transformed event payload to HubSpot:
    
    
    {
      "version": "1",
      "type": "REST",
      "method": "POST",
      "endpoint": "https://api.hubapi.com/contacts/v1/contact/batch/",
      "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer ******2b27"
      },
      "params": {},
      "body": {
        "JSON": {},
        "JSON_ARRAY": {
          "batch": "[{\"email\":\"alex@example.com\",\"properties\":[]}]"
        },
        "XML": {},
        "FORM": {}
      },
      "files": {}
    }
    

The above payload then creates the contact in HubSpot.