# PostHog Source

Ingest your event data from PostHog into RudderStack.

* * *

  * __3 minute read

  * 


[PostHog](<https://posthog.com/>) is a complete product analytics stack that you can seamlessly deploy on your infrastructure. It simplifies scalable product analytics while giving you full control over all your user data.

You can send your PostHog events to RudderStack by configuring it as a destination in your PostHog dashboard.

## ‌Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **PostHog**.
  2. Assign a name to your source and click **Continue**.
  3. Your PostHog source is now configured. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for the source.

[![PostHog source write key](/docs/images/event-stream-sources/posthog/posthog-write-key.webp)](</docs/images/event-stream-sources/posthog/posthog-write-key.webp>)

  4. Note the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) for your workspace.


## RudderStack destination setup

  1. Go to your [PostHog dashboard](<https://posthog.com/>).
  2. In the left navigation bar, click **Data management** > **Destinations**.

[![PostHog data management destinations](/docs/images/event-stream-sources/posthog/data-management-destinations.webp)](</docs/images/event-stream-sources/posthog/data-management-destinations.webp>)

  3. Under **Create a a new destination** , search for **RudderStack**. Then, click **Create**.

[![Create RudderStack destination](/docs/images/event-stream-sources/posthog/posthog-destination-rudderstack.webp)](</docs/images/event-stream-sources/posthog/posthog-destination-rudderstack.webp>)

  4. Configure the following destination settings:

Setting| Instruction  
---|---  
RudderStack host| Replace the placeholder data plane URL with your workspace data plane URL.  
Write API key| Enter your PostHog source write key.  
[![RudderStack destination settings in PostHog](/docs/images/event-stream-sources/posthog/rudderstack-destination-setup.webp)](</docs/images/event-stream-sources/posthog/rudderstack-destination-setup.webp>)

  5. Configure the rest of the settings as required.
  6. Click the **Create & enable** button to complete the setup.


## Sample payload and transformation

This section details how RudderStack receives the data from PostHog and creates the resulting payload.

A sample payload sent by PostHog is shown:
    
    
    {
      "event": {
        "uuid": "dc4685b0-2f39-4ddf-b99e-ec50fd928469",
        "distinct_id": "219ce97b-c06e-4e7d-821c-d15081c293a6",
        "timestamp": "2025-12-19T04:14:59.004Z",
        "elements_chain": "",
        "url": "https://us.posthog.com/project/<ID>/events/",
        "event": "$pageview",
        "properties": {
          "$current_url": "https://us.posthog.com/project/<ID>/functions/new/template-rudderstack",
          "$browser": "Chrome",
          "$ip": "<IP>",
          "this_is_an_example_event": true
        }
      },
      "person": {
        "id": "e6aed9ee-2e84-49bc-93d5-e80302d110b5",
        "properties": {
          "email": "example@posthog.com"
        },
        "name": "Example person",
        "url": "https://us.posthog.com/person/e6aed9ee-2e84-49bc-93d5-e80302d110b5"
      },
      "groups": {},
      "project": {
        "id": <ID>,
        "name": "Default Project",
        "url": "https://us.posthog.com/project/<ID>"
      },
      "source": {
        "name": "RudderStack",
        "url": "https://us.posthog.com/project/<ID>/functions/new/template-rudderstack"
      }
    }
    

RudderStack transforms the above payload into the following `page` payload:
    
    
    {
        "anonymousId": "219ce97b-c06e-4e7d-821c-d15081c293a6",
        "channel": "s2s",
        "context": {
            "app": {
                "name": "PostHogPlugin"
            },
            "browser": "Chrome",
            "library": {},
            "os": {},
            "page": {
                "url": "https://us.posthog.com/project/<ID>/functions/new/template-rudderstack"
            },
            "screen": {}
        },
        "messageId": "dc4685b0-2f39-4ddf-b99e-ec50fd928469",
        "originalTimestamp": "2025-12-19T04:14:59.004Z",
        "properties": {
            "this_is_an_example_event": true,
            "url": "https://us.posthog.com/project/<ID>/functions/new/template-rudderstack"
        },
        "receivedAt": "2025-12-19T04:25:31.101676164Z",
        "request_ip": "<REQUEST_IP>",
        "rudderId": "f7388609-f1fb-43c7-b85d-ceb7be4986f2",
        "type": "page",
        "userId": "e6aed9ee-2e84-49bc-93d5-e80302d110b5"
    }
    

## Troubleshooting

Issue| Solution  
---|---  
Getting a `Error('Failed to post message to Rudderstack: 401: invalid write key` error even though the PostHog source write key is correct| Make sure to replace the placeholder data plane URL with your workspace data plane URL.  
  
## FAQ

#### Is the plugin-based PostHog source setup deprecated?

Yes, the [plugin-based PostHog source setup](<https://github.com/rudderlabs/rudderstack-posthog-plugin>) is deprecated.

You can now directly configure RudderStack as a destination in your PostHog dashboard and start sending your PostHog events.