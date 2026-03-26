# Pipedream Source

Ingest your event data from Pipedream into RudderStack.

* * *

  * __2 minute read

  * 


[Pipedream](<https://pipedream.com/>) lets you build and automate processes that connect APIs. It supports open source triggers and actions for hundreds of integrations.

This guide will help you set up Pipedream as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Pipedream**.
  2. Assign a name to your source and click **Continue**.
  3. Your Pipedream source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Pipedream source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [Pipedream dashboard](<https://pipedream.com/workflows/>) and set up your workflow.
  5. After [adding a trigger](<https://pipedream.com/new?tutorial=1>), click the **+** icon to add a step.
  6. Select the **HTTP/Webhook** option and choose **Send any HTTP Request** :

[![Pipedream add a step](/docs/images/event-stream-sources/pipedream-http-webhook.webp)](</docs/images/event-stream-sources/pipedream-http-webhook.webp>)

  7. In the **HTTP Request Configuration** section, choose **POST** as the request type and enter the RudderStack webhook URL obtained in Step 3 above.


> ![info](/docs/images/info.svg)
> 
> RudderStack only accepts the incoming HTTP requests of type **POST**.

[![Pipedream custom HTTP request](/docs/images/event-stream-sources/pipedream-custom-http-request.webp)](</docs/images/event-stream-sources/pipedream-custom-http-request.webp>)

  8. Configure the other request configuration settings as required.
  9. Click **Deploy** to finish setting up the workflow.


## Event transformation

RudderStack ingests the Pipedream events and checks for the `userId`/`anonymousId` field and the event type (`identify`, `track`, etc.). If both are present, it considers the event to be in a RudderStack payload format. Otherwise, it converts it into a RudderStack payload according to the below property-value mapping:

RudderStack property| Value  
---|---  
`message.event`| `pipedream_source_event`  
`message.type`| `track`  
`message.properties`| Pipedream input payload  
  
## How RudderStack creates the event payload

RudderStack supports all [standard events](<https://www.rudderstack.com/docs/event-spec/standard-events/>) in the specified format. For the other events, it transforms the incoming data to a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) payload.

A sample incoming payload is as shown:
    
    
    {
        "artist": "Artist One",
        "genre": "Jazz",
        "song": "Take Five"
      }
    

RudderStack transforms the above payload into the following `track` payload:
    
    
    {
      "event": "pipedream_soure_event",
      "anonymousId": "63767499ca6fb1b7c988d5bb",
      "integration": {
        "name": "PIPEDREAM"
      },
      "integrations": {
        "PIPEDREAM": false
      },
      "type": "track",
      "properties": {
        "artist": "Artist One",
        "genre": "Jazz",
        "song": "Take Five"
      }
    }