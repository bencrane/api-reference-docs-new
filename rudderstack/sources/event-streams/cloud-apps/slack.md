# Slack Source Beta

Ingest your event data from Slack into RudderStack.

* * *

  * __4 minute read

  * 


[Slack](<https://slack.com/intl/en-in/>) is a popular business communication platform that lets you organize all your business-related chats by specific topics, groups, or direct messaging.

This guide will help you set up Slack as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Slack**.
  2. Assign a name to your source and click **Continue**.
  3. Your Slack source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Slack webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. In your Slack app, click your workspace and select **Tools and Settings** > **Manage Apps** to open the Slack app directory.


> ![info](/docs/images/info.svg)
> 
> You must have an admin role in your Slack workspace to see these options.

[![Add webhook source in Slack](/docs/images/event-stream-sources/slack-tools.webp)](</docs/images/event-stream-sources/slack-tools.webp>)

  5. Click **Build** from the top right navigation bar.
  6. Select an existing app or [create a new one](<https://api.slack.com/quickstart#creating>) by clicking **Create New App**.

[![Add webhook name and URL](/docs/images/event-stream-sources/slack-src-1.webp)](</docs/images/event-stream-sources/slack-src-1.webp>)

  7. Click **Event Subscriptions** from the left navigation bar.
  8. Turn on the **Enable events** setting and enter the webhook URL in the **Request URL** field obtained in Step 3.

[![Add webhook name and URL](/docs/images/event-stream-sources/slack-src-2.webp)](</docs/images/event-stream-sources/slack-src-2.webp>)

  9. In **Subscribe to bot events** section, [add the events you want to track](<https://api.slack.com/quickstart#listening>) and click **Save Changes**.

[![Add webhook name and URL](/docs/images/event-stream-sources/slack-src-3.webp)](</docs/images/event-stream-sources/slack-src-3.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on steps 4-9, see [Subscribing to event types](<https://api.slack.com/apis/events-api#subscribing>).

## Event transformation

RudderStack supports ingesting all the [Slack events](<https://api.slack.com/events>) related to user’s activities. It converts:

  * Slack’s `team_join` and `user_change` events as [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) events, and
  * Rest of the Slack events as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events.


> ![info](/docs/images/info.svg)
> 
> The [`url_verification`](<https://api.slack.com/events/url_verification>) event verifies the webhook URL. It has a different object structure than the rest of the events and is triggered only once during the first time webhook setup.

RudderStack maps the following Slack properties from the event payload to the RudderStack fields:

Slack Property| RudderStack Property  
---|---  
`event.type`| `event`  
`event.ts`| `originalTimestamp`  
`event.user`  
`event.user.id`| `context.externalId`  
`event.profile.first_name`| `context.traits.firstName`  
`event.profile.last_name`| `context.traits.lastName`  
`event.user.profile.real_name`| `context.traits.name`  
`event.user.profile.email`| `context.traits.email`  
`event.user.tz`| `timezone`  
`event.user.profile.image_original`| `context.traits.avatar`  
`event.user.profile.title`| `context.traits.title`  
  
## How RudderStack creates the event payload

This section details how RudderStack receives the data from Slack source and creates the resulting payload.

### Identify event

A sample input payload received from Slack webhook (`team_join` event):
    
    
    {
      "event": {
        "type": "team_join",
        "user": {
          "id": "W012CDE"',
          "name": "johnd",
          "real_name": "John Doe",
        },
      "type": "event_callback",
      "event_id": "<event_id>",
      "event_time": "1709441309",
      "token": "<token>",
      "team_id": "T0GFJL5J7",
      "context_team_id": "T0GFJL5J7",
      "context_enterprise_id": "null",
      "api_app_id": "<api_app_id>",
      "authorizations": [{
        "enterprise_id": "null",
        "team_id": "T0GFJL5J7",
        "user_id": "U04G7H550",
        "is_bot": true,
        "is_enterprise_install": false,
      }, ],
      "is_ext_shared_channel": false,
      "event_context": "eJldCI65436EUEpMSFhgfhg76joiQzAxRTRQTEIxMzUifQ"
    }
    

The corresponding RudderStack-transformed (`identify`) event payload is shown below:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown",
        },
        "integration": {
          "name": "SLACK",
        },
        "externalId": [{
          "type": "slackUserId",
          "id": "W012CDE",
        }, ],
      },
      "integrations": {
        "SLACK": false,
      },
      "type": "identify",
      "event": "Team Join",
      "anonymousId": "2bc5ae2825a712d3d154cbdacb86ac16c278",
      "originalTimestamp": "2024-03-03T04:48:29.000Z",
      "sentAt": "2024-03-03T04:48:29.000Z",
      "properties": {
        "type": "team_join",
        "user": {
          "id": "W012CDE",
          "name": "johnd",
          "real_name": "John Doe",
        },
      },
    }
    

### Track event

A sample input payload received from Slack webhook (`message` event):
    
    
    {
      "event": {
        "user": "U04G7H550",
        "type": "message",
        "ts": "1709441309.308399",
        "client_msg_id": "834r664e-ec75-445d-t5c6-b873a07y9c81",
        "text": "What is the pricing of product X",
        "team": "T0GFJL5J7",
        "thread_ts": "1709407304.839329",
        "parent_user_id": "U06P6LQTPV",
        "blocks": [{
          "type": "rich_text",
          "block_id": "xGKJl",
          "elements": [{
            "type": "rich_text_section",
            "elements": {
                "type": "text",
                "text": "What is the pricing of product X",
              },
              {
                "type": "channel",
                "channel_id": "C03CDQTPI65",
              },
              {
                "type": "text",
                "text": "to do this",
              },
            ],
          }, ],
        }, ],
        "channel": "C03CDQTPI65",
        "event_ts": "1709441309.308399",
        "channel_type": "channel",
      }, {
      "type": "event_callback",
      "event_id": "<event_id>",
      "event_time": "1709441309",
      "token": "<token>",
      "team_id": "T0GFJL5J7",
      "context_team_id": "T01gqtPIL5J7",
      "context_enterprise_id": "null",
      "api_app_id": "<api_app_id>",
      "authorizations": [{
        "enterprise_id": "null",
        "team_id": "T0GFJL5J7",
        "user_id": "W012CDE",
        "is_bot": true,
        "is_enterprise_install": false,
      }, ],
      "is_ext_shared_channel": false,
      "event_context": "4-wd6joiQfdgTRQTpIzdfifQ"
    },
    

The corresponding RudderStack-transformed (`track`) event payload is shown below:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown",
        },
        "integration": {
          "name": "SLACK",
        },
        "externalId": [{
          "type": "slackUserId",
          "id": "U04G7H550",
        }, ],
      },
      "integrations": {
        "SLACK": false,
      },
      "type": "track",
      "event": "Message",
      "anonymousId": "7509c04f547b05afb6838aa742f4910263d6",
      "originalTimestamp": "2024-03-03T04:48:29.308Z",
      "sentAt": "2024-03-03T04:48:29.000Z",
      "properties": {
        "user": "U04G7H550",
        "type": "message",
        "ts": "1709441309.308399",
        "client_msg_id": "834r664e-ec75-445d-t5c6-b873a07y9c81",
        "text": "What is the pricing of product X",
        "team": "T0GFJL5J7",
        "thread_ts": "1709407304.839329",
        "parent_user_id": "U06P6LQTPV",
        "blocks": [{
          "type": "rich_text",
          "block_id": "xGKJl",
          "elements": [{
            "type": "rich_text_section",
            "elements": [{
                "type": "text",
                "text": "What is the pricing of product X",
              },
              {
                "type": "channel",
                "channel_id": "C03CDQTPI65",
              },
              {
                "type": "text",
                "text": "to do this",
              },
            ],
          }, ],
        }, ],
        "channel": "C03CDQTPI65",
        "event_ts": "1709441309.308399",
        "channel_type": "channel",
      },
    }