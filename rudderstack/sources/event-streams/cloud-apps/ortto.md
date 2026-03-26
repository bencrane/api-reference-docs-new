# Ortto Source (formerly Autopilot)

Ingest your event data from Ortto into RudderStack.

* * *

  * __2 minute read

  * 


[Ortto](<https://www.autopilothq.com/>) (formerly Autopilot) is a popular marketing automation platform that allows you to track and capture new leads, create detailed customer journeys, and boost customer retention.

This guide will help you set up Ortto as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Ortto**.
  2. Assign a name to your source and click **Continue**.
  3. Your Ortto source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Ortto webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [Ortto dashboard](<https://ortto.app/>). From the left sidebar, go to **More** > **Data sources** > **New data source** :

[![Add webhook source in Ortto](/docs/images/event-stream-sources/ortto-webhook-source-1.webp)](</docs/images/event-stream-sources/ortto-webhook-source-1.webp>)

  5. Search for **Webhook** and select **Webhook (advanced)**.

[![Add webhook source in Ortto](/docs/images/event-stream-sources/ortto-webhook-source-2.webp)](</docs/images/event-stream-sources/ortto-webhook-source-2.webp>)

  6. Enter the **Webhook name**. Specify the URL obtained in Step 3 in the **Webhook URL** field.

[![Add webhook name and URL](/docs/images/event-stream-sources/ortto-webhook-source-3.webp)](</docs/images/event-stream-sources/ortto-webhook-source-3.webp>)

  7. Complete the rest of the configuration as per your requirements and click **Create**.


> ![info](/docs/images/info.svg)
> 
> It is recommended to test your webhook using the **Test** button before clicking **Create** to complete the setup.

## Event transformation

RudderStack ingests the events from Ortto as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events, after converting them into the appropriate event format.

RudderStack supports ingesting events related to the following [Ortto standard activities](<https://help.ortto.com/a-251-configuring-a-webhook#webhook-payload-data>):

  * **Email activities**
  * **SMS activities**
  * **Push activities**
  * **Web and user session activities**
  * **Audience and tag activities**
  * **Playbook activities**
  * **Journey activities**
  * **Capture widget activities**
  * **Talk conversation activities**


### Property mappings

RudderStack maps the following Ortto properties from the event payload to the RudderStack fields:

Ortto Property| RudderStack Property  
---|---  
`activity.field_id`| event  
`time`| `originalTimestamp`  
`id`| `messageId`  
`contact.first_name`| `contact.first_name`  
`contact.last_name`| `context.traits.lastName`  
`contact.email`| `context.traits.email`  
`contact.external_id`| `userId` / `anonymousId`  
`contact.country.name`| `context.traits.address.country`  
`contact.city.name`| `context.traits.address.city`  
`contact.postal`| `context.traits.address.postal`  
`contact.phone_number`| `context.traits.phone`  
`contact.birthday`| `context.traits.birthday`  
  
A sample input payload ingested by RudderStack:
    
    
    {
      "activity": {
        "id": "00651b946bfef7e80478efee",
        "field_id": "act::s-all",
        "created": "2023-10-03T04:11:23Z",
        "attr": {
          "str::is": "API",
          "str::s-ctx": "Subscribed via API"
        }
      },
      "contact": {
        "contact_id": "00651b946baa9be6b2edad00",
        "email": "alex@example.com"
      },
      "id": "00651b946cef87c7af64f4f3",
      "time": "2023-10-03T04:11:24.25726779Z",
      "webhook_id": "651b8aec8002153e16319fd3"
    }
    

The RudderStack-transformed event payload is shown below:
    
    
    {
      "anonymousId": "3ce8d38c-ecad-4941-8226-c802a08a7889",
      "context": {
        "externalId": [{
          "id": "00651b946baa9be6b2edad00",
          "type": "orttoPersonId"
        }],
        "integration": {
          "name": "ortto"
        },
        "ip": "3.139.195.252",
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "traits": {
          "email": "alex@example.com"
        }
      },
      "event": "Resubscribe globally",
      "integrations": {
        "ortto": false
      },
      "messageId": "00651b946cef87c7af64f4f3",
      "originalTimestamp": "2023-10-03T04:11:24.000Z",
      "properties": {
        "activity.attr.str::is": "API",
        "activity.attr.str::s-ctx": "Subscribed via API",
        "activity.created": "2023-10-03T04:11:23Z",
        "activity.id": "00651b946bfef7e80478efee",
        "webhook_id": "651b8aec8002153e16319fd3"
      },
      "receivedAt": "2023-10-03T13:38:06.762Z",
      "request_ip": "3.139.195.252",
      "rudderId": "2e69b7d1-1511-4f10-bec9-43652ab8efe0",
      "sentAt": "2023-10-17T13:38:10.993Z",
      "timestamp": "2023-10-17T13:38:01.768Z",
      "type": "track"
    }
    

## FAQ

#### Why am I getting a 500 error while testing my webhook data source in Ortto?

If you’re getting a `Unexpected status code 500 received` while setting up your webhook data source in Ortto, verify if your webhook URL is correctly configured to receive events.

[![Ortto webhook source error](/docs/images/event-stream-sources/ortto-source-error.webp)](</docs/images/event-stream-sources/ortto-source-error.webp>)