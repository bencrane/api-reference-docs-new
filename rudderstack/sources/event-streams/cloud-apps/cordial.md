# Cordial Source

Ingest your event data from Cordial into RudderStack.

* * *

  * __3 minute read

  * 


[Cordial](<https://cordial.com/>) is a smart data platform for marketing teams. It lets you leverage AI to process real-time customer information and complex business data and deliver personalized content to users across various channels.

This guide will help you set up Cordial as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Cordial**.
  2. Assign a name to your source and click **Continue**.
  3. Your Cordial source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Cordial webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [Cordial dashboard](<https://admin.cordial.io/#/login>) and navigate to **Integrations** > **Webhooks** > **New** to [create a webhook](<https://support.cordial.com/hc/en-us/articles/13584534464141-Webhooks#createwebhook>).

  5. Click **Edit** in the **Webhook Settings** pane to [configure the webhook](<https://support.cordial.com/hc/en-us/articles/13584534464141-Webhooks#createwebhook>).

  6. In the **Webhook Payload** section, add the following schema:


    
    
    {$payload = ['contact' => $contact, 'event' => $event]} 
    {$utils->setPayload($payload)}
    

  6. In the **Request URL** field, enter the webhook URL obtained in Step 3.


Further, you can choose to configure [webhook triggers](<https://support.cordial.com/hc/en-us/articles/13584534464141-Webhooks#configurewebhooktriggers>).

## Event transformation

RudderStack ingests the events from Cordial as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events, after converting them into the appropriate event format. Cordial supports sending the single or batched request based on your webhook configuration.

### Event mappings

RudderStack maps the following Cordial event types as is:

  * **Email channel events**

    * `open`
    * `click`
    * `optout`
    * `bounce`
  * **SMS/MMS channel events**

    * `message_sent`
    * `click`
  * **REST channel events**

    * `message_sent`
  * **Custom events**

  * **Mobile channel events**

    * `crdl_notification_tap`
    * `crdl_deep_link_open`
    * `crdl_notification_delivered_in_foreground`


It also maps some additional **mobile channel events** as shown:

Cordial event| RudderStack event  
---|---  
`crdl_app_install`| [Application Installed](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>)  
`crdl_app_open`| [Application Opened](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>)  
  
### Property mappings

RudderStack maps the following Cordial properties from the event payload to the RudderStack fields:

Cordial property| RudderStack property  
---|---  
`event._id`| `properties.event_id`  
`contact._id`| `context.traits.userId/userId`  
`event.ts`  
`event.ats`| `timestamp` & `sentAt` & `originalTimestamp`  
`event.d`| `context.device`  
`contact.channels.email.address`| `context.traits.email`  
  
### How RudderStack creates the event payload

This section details how RudderStack receives the data from Cordial source and creates the resulting payload.

A sample payload sent by Cordial is shown below:
    
    
    {
      "contact": {
        "_id": "6690fe3655e334d6270287b5",
        "channels": {
          "email": {
            "address": "alex@example.com",
            "subscribeStatus": "subscribed",
            "subscribedAt": "2024-07-12T09:58:14+0000"
          }
        },
        "createdAt": "2024-07-12T09:58:14+0000",
        "address": {
          "city": "San Diego"
        },
        "first_name": "Alex",
        "last_name": "Keener",
        "lastUpdateSource": "api",
        "lastModified": "2024-07-12T13:00:49+0000",
        "cID": "6690fe3655e334d6270287b5"
      },
      "event": {
        "_id": "669141857b8cc361ba0da2ef",
        "cID": "6690fe3655e334d6270287b5",
        "ts": "2024-07-12T14:45:25+00:00",
        "ats": "2024-07-12T14:45:25+0000",
        "d": {
          "type": "computer",
          "device": false,
          "platform": false,
          "browser": false,
          "robot": true
        },
        "a": "browse",
        "tzo": -7,
        "rl": "a",
        "UID": "4934ee07118197f93f74d5215b7b0076",
        "time": "2024-07-12T14:45:25+0000",
        "action": "browse",
        "bmID": "",
        "first": 0,
        "properties": {
          "category": "Games",
          "url": "http://example.com/games",
          "description": "A really cool game.",
          "price": 9.99,
          "title": "Monopoly",
          "test_key": "value"
        }
      }
    }
    

RudderStack transforms the above payload into the following [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) payload:
    
    
    {
      "context": {
        "device": {
          "browser": false,
          "device": false,
          "platform": false,
          "robot": true,
          "type": "computer"
        },
        "externalId": [{
          "id": "6690fe3655e334d6270287b5",
          "type": "cordialContactId"
        }],
        "integration": {
          "name": "Cordial"
        },
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "traits": {
          "_id": "6690fe3655e334d6270287b5",
          "address": {
            "city": "San Diego"
          },
          "cID": "6690fe3655e334d6270287b5",
          "channels": {
            "email": {
              "address": "alex@example.com",
              "subscribeStatus": "subscribed",
              "subscribedAt": "2024-07-12T09:58:14+0000"
            }
          },
          "createdAt": "2024-07-12T09:58:14+0000",
          "email": "alex@example.com",
          "first_name": "Alex",
          "lastModified": "2024-07-12T13:00:49+0000",
          "lastUpdateSource": "api",
          "last_name": "Keener",
          "userId": "6690fe3655e334d6270287b5"
        }
      },
      "event": "browse",
      "integrations": {
        "Cordial": false
      },
      "messageId": "68d60184-93e4-4624-81e3-f6eda579088d",
      "originalTimestamp": "2024-07-12T14:45:25+00:00",
      "properties": {
        "UID": "4934ee07118197f93f74d5215b7b0076",
        "a": "browse",
        "action": "browse",
        "ats": "2024-07-12T14:45:25+0000",
        "bmID": "",
        "cID": "6690fe3655e334d6270287b5",
        "category": "Games",
        "description": "A really cool game.",
        "event_id": "669141857b8cc361ba0da2ef",
        "first": 0,
        "price": 9.99,
        "rl": "a",
        "test_key": "value",
        "time": "2024-07-12T14:45:25+0000",
        "title": "Monopoly",
        "ts": "2024-07-12T14:45:25+00:00",
        "tzo": -7,
        "url": "http://example.com/games"
      },
      "receivedAt": "2024-07-26T13:59:42.848+05:30",
      "request_ip": "[::1]",
      "rudderId": "93df6e69-2df5-4ed4-a59b-ff8a673ed663",
      "sentAt": "2024-07-12T14:45:25+00:00",
      "timestamp": "2024-07-12T14:45:25+00:00",
      "type": "track",
      "userId": "6690fe3655e334d6270287b5"
    }