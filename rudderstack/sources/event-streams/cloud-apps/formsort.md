# Formsort

Ingest your event data from Formsort into RudderStack.

* * *

  * __2 minute read

  * 


[Formsort](<https://formsort.com/>) platform provides tools for businesses and organizations to create user-friendly forms and surveys. You can use these forms for lead generation, customer feedback, event registration, job applications, etc.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Formsort**.
  2. Assign a name to your source and click **Continue**.
  3. Your Formsort source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Formsort source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [Formsort account](<https://studio.formsort.com/auth/login>).
  5. [Set up your webhook integration](<https://docs.formsort.com/handling-data/integration-reference/webhooks#setting-up-the-webhook-integration>), add the **Webhook URL** obtained in step 3, and save the configuration:

[![Formsort source webhook URL](/docs/images/event-stream-sources/formsort-webhook.webp)](</docs/images/event-stream-sources/formsort-webhook.webp>)

## Event transformation

Based on the [webhook posting frequency](<https://docs.formsort.com/handling-data/integration-reference/webhooks#posting-frequency>) you choose while setting up the webhook integration in Formsort, RudderStack sets the event name as `FlowFinalized` when the flow is finalized. Otherwise, it sets the event name as `FlowLoaded`.

RudderStack ingests the Formsort events after converting them into the RudderStack event format. It also maps the following properties from the Formsort event payload to the RudderStack properties:

Formsort property| RudderStack property  
---|---  
`created_at`| `originalTimestamp`  
`responder_uuid`| `userId`  
`answers`| `properties`  
`flow_label`| `context.page.title`  
`variant_label`| `context.variantLabel`  
`variant_uuid`| `context.variantUuid`  
  
## How RudderStack creates the event payload

This section details how RudderStack receives the data from Formsort source and creates the resulting payload.

### FlowFinalized event

A sample payload sent by Formsort when `finalized` is `true` is shown below:
    
    
    {
      "answers": {
        "yes": true,
        "enter_email": "testUser@rudderstack.com",
        "enter_name": "2000-11-25",
        "yes_or_no": false
      },
      "responder_uuid": "be2f3a8d-8aa4-4a01-8855-8e464a752b52",
      "flow_label": "new-flow-2022-11-25",
      "variant_label": "main",
      "variant_uuid": "0828efa7-7215-4e7d-a7ab-6c1079010cea",
      "finalized": true,
      "created_at": "2022-11-25T14:36:58+00:00"
    }
    

RudderStack transforms the above payload into the following [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) payload with event name as `FlowFinalized`:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "integration": {
          "name": "Formsort"
        },
        "page": {
          "title": "new-flow-2022-11-25"
        },
        "variantLabel": "main",
        "variantUuid": "0828efa7-7215-4e7d-a7ab-6c1079010cea"
      },
      "integrations": {
        "Formsort": false
      },
      "type": "track",
      "anonymousId": "7bd86cd0-df65-4e3e-bddd-3ba4da17fbb3",
      "userId": "be2f3a8d-8aa4-4a01-8855-8e464a752b52",
      "originalTimestamp": "2022-11-25T14:36:58+00:00",
      "properties": {
        "yes": true,
        "enter_email": "testUser@rudderstack.com",
        "enter_name": "2000-11-25",
        "yes_or_no": false
      },
      "event": "FlowFinalized"
    }
    

### FlowLoaded event

A sample payload sent by Formsort when `finalized` is `false` is shown below:
    
    
    {
      "answers": {
        "yes": true,
        "enter_email": "test@user.com",
        "enter_name": "2022-11-17",
        "yes_or_no": false
      },
      "responder_uuid": "66a8e5bb-67e1-47ec-b55f-a26fd4be2dc7",
      "flow_label": "new-flow-2022-11-25",
      "variant_label": "main",
      "variant_uuid": "0828efa7-7215-4e7d-a7ab-6c1079010cea",
      "finalized": false,
      "created_at": "2022-11-25T14:41:22+00:00"
    }
    

RudderStack transforms the above payload into the following [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) payload with event name as `FlowLoaded`:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "integration": {
          "name": "Formsort"
        },
        "page": {
          "title": "new-flow-2022-11-25"
        },
        "variantLabel": "main",
        "variantUuid": "0828efa7-7215-4e7d-a7ab-6c1079010cea"
      },
      "integrations": {
        "Formsort": false
      },
      "type": "track",
      "anonymousId": "448a42fd-18e5-4cdf-859b-5b99aceaf474",
      "userId": "be2f3a8d-8aa4-4a01-8855-8e464a752b52",
      "originalTimestamp": "2022-11-25T14:36:58+00:00",
      "properties": {
        "yes": true,
        "enter_email": "testUser@rudderstack.com",
        "enter_name": "2000-11-25",
        "yes_or_no": false
      },
      "event": "FlowLoaded"
    }