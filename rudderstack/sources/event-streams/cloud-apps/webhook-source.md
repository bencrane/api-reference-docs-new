# Webhook Source

Ingest events from a custom webhook source into RudderStack.

* * *

  * __6 minute read

  * 


Apart from the [Event Stream cloud sources](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/>), RudderStack also supports any other source that provides a webhook and lets you use it to send events to your preferred destinations.

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * RudderStack recommends using the webhook source only if your input data is not in the standard RudderStack event format. In such cases, you can write a [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to convert the data into the standard event format.
>   * To ingest events that follow the standard RudderStack event format, use an [HTTP source](<https://www.rudderstack.com/docs/api/http-api/>) instead.
> 


## How the integration works

  1. Set up a webhook source in the RudderStack dashboard.
  2. Once the source is created, note the **Webhook URL** and use it to configure a webhook in the platform from where you want to ingest events.


> ![warning](/docs/images/warning.svg)
> 
> Not all platforms support configuring webhook sources.

  3. When the users perform any action configured in the source, the source platform automatically sends the generated events to the webhook URL.
  4. RudderStack takes the data, creates the event payload, and sends it to the connected destinations after transforming them in the required format.


## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Webhook**.
  2. Assign a name to your source and click **Continue**.
  3. Toggle on the **Put source request details in event context** setting to include all the request details like headers, query parameters, method, URLs, etc. in the event payload. See Send source request details in event’s context section for more information.
  4. Your webhook source is now created. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Webhook endpoint](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  5. [Add a destination in RudderStack](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#adding-a-destination>) and connect it to this webhook source.


> ![warning](/docs/images/warning.svg)
> 
> You must also connect an appropriate [Transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform the ingested event payload into the destination-specific format.
> 
> See the Use case section below for an end-to-end example.

After the setup is complete, configure the webhook in your source platform and specify the webhook URL obtained above. You can test and confirm if your webhook is working as expected by ingesting some events and using the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#source-live-events>) functionality to view the events in real time.

## Send source request details in event’s context

While setting up the webhook source, you can toggle on the **Put source request details in event context** setting to include all the request details like headers, query parameters, method, URLs, etc. in the event payload.

[![Webhook connection settings](/docs/images/event-stream-sources/webhook/webhook-source-details-event-context.webp)](</docs/images/event-stream-sources/webhook/webhook-source-details-event-context.webp>)

For existing webhook sources, go to the **Configuration** tab of the source, click the **Update** button and toggle on this setting.

[![Update webhook connection settings](/docs/images/event-stream-sources/webhook/update-webhook-configuration.webp)](</docs/images/event-stream-sources/webhook/update-webhook-configuration.webp>)

See the following sections to understand how this setting impacts the payload creation and transformation:

  * How RudderStack creates the event payload
  * Event transformation


## Use case

This section covers an end-to-end use case that ingests events from [Mailchimp](<https://mailchimp.com>) into RudderStack by configuring a webhook and sends it to the [Google Analytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>) destination.

  1. Obtain the webhook URL by following the steps in the Get started section.
  2. Configure a webhook and specify the webhook URL in Mailchimp. The following image shows the webhook URL added in Mailchimp:

[![Adding the webhook to an event source](/docs/images/event-stream-sources/webhook-5.webp)](</docs/images/event-stream-sources/webhook-5.webp>)

As seen in the above image, Mailchimp sends the updates under **Trigger on Events** as user events to the specified webhook URL with the content type `application/x-www-form-urlencoded`.

> ![info](/docs/images/info.svg)
> 
> The content type can vary in case of the other webhook sources.

## How RudderStack creates the event payload

This section continues with the above use case containing the Mailchimp example and details how RudderStack receives the data from the webhook source and creates the resulting event payload.

  1. Suppose a customer subscribes to Mailchimp. Mailchimp then sends the following data to RudderStack:


    
    
    type=subscribe&fired_at=2021-07-28+08%3A06%3A59&data%5Bid%5D=e2ff089583&data%5Bemail%5D=ruchira%40rudderlabs.com&data%5Bemail_type%5D=html&data%5Bip_opt%5D=1.2.3.4&data%5Bweb_id%5D=161912900&data%5Bmerges%5D%5BEMAIL%5D=name%40rudderlabs.com&data%5Bmerges%5D%5BFNAME%5D=Name&data%5Bmerges%5D%5BLNAME%5D=Surname&data%5Bmerges%5D%5BADDRESS%5D=&data%5Bmerges%5D%5BPHONE%5D=&data%5Bmerges%5D%5BBIRTHDAY%5D=&data%5Blist_id%5D=ec4689c266
    

  2. RudderStack receives this data and creates the following payload:


    
    
      {
      type: "track",
      event: "webhook_source_event",
      rudderId: "044448e2-a674-426c-ba61-8341262babcc",
      messageId: "4379907d-689a-4e3a-a2f7-477e29a02299",
      properties: {
        type: ["subscribe"],
        "data[id]": ["e2ff089583"],
        fired_at: ["2021-07-28 08:06:59"],
        "data[email]": ["[name@rudderlabs.com](mailto:name@rudderlabs.com)"],
        "data[ip_opt]": ["1.2.3.4"],
        "data[web_id]": ["161912900"],
        "data[list_id]": ["ec4689c266"],
        "data[email_type]": ["html"],
        "data[merges][EMAIL]": [
          "[name@rudderlabs.com](mailto:name@rudderlabs.com)",
        ],
        "data[merges][FNAME]": ["Name"],
        "data[merges][LNAME]": ["Surname"],
        "data[merges][PHONE]": [""],
        "data[merges][ADDRESS]": [""],
        "data[merges][BIRTHDAY]": [""],
      },
      anonymousId: "d6597ba2-54db-4bd7-8769-86ac067b4178",
    }
    

  3. If you toggle on the **Put source request details in event context** dashboard setting, then RudderStack creates the following event payload instead:


    
    
    {
      "type": "track",
      "event": "webhook_source_event",
      "rudderId": "044448e2-a674-426c-ba61-8341262babcc",
      "messageId": "4379907d-689a-4e3a-a2f7-477e29a02299",
      "properties": {
        "type": ["subscribe"],
        "data[id]": ["e2ff089583"],
        "fired_at": ["2021-07-28 08:06:59"],
        "data[email]": ["[name@rudderlabs.com](mailto:name@rudderlabs.com)"],
        "data[ip_opt]": ["1.2.3.4"],
        "data[web_id]": ["161912900"],
        "data[list_id]": ["ec4689c266"],
        "data[email_type]": ["html"],
        "data[merges][EMAIL]": [
          "[name@rudderlabs.com](mailto:name@rudderlabs.com)",
        ],
        "data[merges][FNAME]": ["Name"],
        "data[merges][LNAME]": ["Surname"],
        "data[merges][PHONE]": [""],
        "data[merges][ADDRESS]": [""],
        "data[merges][BIRTHDAY]": [""],
      },
      "anonymousId": "d6597ba2-54db-4bd7-8769-86ac067b4178",
      "context": {
        "headers": {
          "Accept": "*/*",
          "Accept-Encoding": "gzip, deflate, br",
          "Content-Length": "439",
          "Content-Type": "application/json",
          "Postman-Token": "<token>",
          "User-Agent": "PostmanRuntime/7.43.0",
          "X-Forwarded-For": "<ip>",
          "X-Forwarded-Host": "dataplane.rudderstack.com",
          "X-Forwarded-Port": "443",
          "X-Forwarded-Proto": "https",
          "X-Forwarded-Server": "traefik-ingress-controller-v3-us-east-1b-858dfc6bfc-9224q",
          "X-Real-Ip": "<ip>"
        },
        "method": "POST",
        "proto": "HTTP/1.1",
        "query_parameters": {
          "key": "value",
          "writeKey": "<write_key>"
        },
        "url": "/v1/webhook?writeKey=<write_key>&key=value"
      },
    }
    

## Event transformation

This section highlights how to transform the created event payload in a destination-specific format by leveraging RudderStack’s [Transformation](<https://www.rudderstack.com/docs/transformations/overview/>) feature.

> ![warning](/docs/images/warning.svg)
> 
> Make sure this transformation is connected to the destination where you want to send the data.

#### Case 1: No request details in event context

If **Put source request details in event context** setting is toggled off, then use the following sample transformation to transform the event payload:
    
    
    export function transformEvent(event) {
      const updatedEvent = event
      const { properties } = event
    
      if (properties) {
        updatedEvent.event = properties.type
        updatedEvent.userId = properties["data[email]"]
        updatedEvent.properties.name = `${properties["data[merges][FNAME]"]} ${properties["data[merges][LNAME]"]}`
        updatedEvent.properties.phone = properties["data[merges][PHONE]"]
    
        delete updatedEvent.properties["data[merges][PHONE]"]
        delete updatedEvent.properties["data[merges][FNAME]"]
        delete updatedEvent.properties["data[merges][LNAME]"]
      }
    
      return updatedEvent
    }
    
    
    
    {
      type: 'track',
      event: [
        'subscribe'
      ],
      rudderId: '044448e2-a674-426c-ba61-8341262babcc',
      messageId: '4379907d-689a-4e3a-a2f7-477e29a02299',
      properties: {
        type: [
          'subscribe'
        ],
        'data[id]': [
          'e2ff089583'
        ],
        fired_at: [
          '2021-07-28 08:06:59'
        ],
        'data[email]': [
          'name@rudderlabs.com'
        ],
        'data[ip_opt]': [
          '1.2.3.4'
        ],
        'data[web_id]': [
          '161912900'
        ],
        'data[list_id]': [
          'ec4689c266'
        ],
        'data[email_type]': [
          'html'
        ],
        'data[merges][EMAIL]': [
          'name@rudderlabs.com'
        ],
        'data[merges][ADDRESS]': [
          ''
        ],
        'data[merges][BIRTHDAY]': [
          ''
        ],
        name: 'Name Surname',
        phone: [
          ''
        ]
      },
      anonymousId: 'd6597ba2-54db-4bd7-8769-86ac067b4178',
      userId: [
        'name@rudderlabs.com'
      ]
    }
    

#### Case 2: Request details present in event context

If you have toggled on the **Put source request details in event context** setting, then you can modify the above transformation as follows:

> ![info](/docs/images/info.svg)
> 
> You can write this transformation to use the values from the event’s context as per your requirement.
    
    
    export function transformEvent(event) {
      const updatedEvent = event
      
      // Notice we destructured context out of the event
      const { properties, context } = event
    
      if (properties) {
        updatedEvent.event = properties.type
        updatedEvent.userId = properties["data[email]"]
        updatedEvent.properties.name = `${properties["data[merges][FNAME]"]} ${properties["data[merges][LNAME]"]}`
        updatedEvent.properties.phone = properties["data[merges][PHONE]"]
    
        // Notice we populated these from context
        // Make sure to enable "put request details" as indicated above to find these in context
        updatedEvent.properties.customParam = context.query_parameters.query_param_test
        updatedEvent.properties.userAgent = context.headers["User-Agent"]
    
        delete updatedEvent.properties["data[merges][PHONE]"]
        delete updatedEvent.properties["data[merges][FNAME]"]
        delete updatedEvent.properties["data[merges][LNAME]"]
      }
    
      return updatedEvent
    }
    
    
    
    {
      type: 'track',
      event: [
        'subscribe'
      ],
      rudderId: '044448e2-a674-426c-ba61-8341262babcc',
      messageId: '4379907d-689a-4e3a-a2f7-477e29a02299',
      properties: {
        type: [
          'subscribe'
        ],
        'data[id]': [
          'e2ff089583'
        ],
        fired_at: [
          '2021-07-28 08:06:59'
        ],
        'data[email]': [
          'name@rudderlabs.com'
        ],
        'data[ip_opt]': [
          '1.2.3.4'
        ],
        'data[web_id]': [
          '161912900'
        ],
        'data[list_id]': [
          'ec4689c266'
        ],
        'data[email_type]': [
          'html'
        ],
        'data[merges][EMAIL]': [
          'name@rudderlabs.com'
        ],
        'data[merges][ADDRESS]': [
          ''
        ],
        'data[merges][BIRTHDAY]': [
          ''
        ],
        name: 'Name Surname',
        phone: [
          ''
        ]
        customParam: 'query_param_test_value',
        userAgent: 'PostmanRuntime/7.43.0'
      },
      anonymousId: 'd6597ba2-54db-4bd7-8769-86ac067b4178',
      userId: [
        'name@rudderlabs.com'
      ]
    }
    

RudderStack then sends this payload to the destinations connected to the webhook source set up in the dashboard - Google Analytics, in this case.