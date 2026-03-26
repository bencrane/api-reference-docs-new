# AMP Analytics

Send event data from your AMP page to RudderStack.

* * *

  * __6 minute read

  * 


The RudderStack AMP component makes it easy to send the event data from your AMP page to your specified destinations via RudderStack. Now you don’t need to implement or test multiple components for different destinations for your event data. This component collects the default properties and sends a `page` event to RudderStack.

> ![info](/docs/images/info.svg)
> 
> Since the AMP source sends the data directly to the RudderStack backend, it supports only cloud mode destinations. For more information on cloud mode, see [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

## Setup requirements

  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up an AMP source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> In the dashboard, the **Setup** tab for the source has an SDK installation snippet containing both the write key and the data plane URL. You can use it to integrate the AMP component into your project.

## Getting started

> ![info](/docs/images/info.svg)
> 
> Learn more about the AMP project from their [official website](<https://amp.dev/>). To get started and set up your AMP project, check out their [Quick Start Guide](<https://amp.dev/documentation/guides-and-tutorials/start/create/>).

After completing the initial setup of your AMP project, follow these steps to start sending your event data to RudderStack:

  * Add an AMP source in your RudderStack [dashboard](<https://app.rudderstack.com>).
  * Note the **Write Key**. This will be required later when using the AMP Analytics component.

[![](/docs/images/event-stream-sources/amp-analytics-1.webp)](</docs/images/event-stream-sources/amp-analytics-1.webp>)

  * Include the RudderStack AMP component before the closing `</head>` tag:


    
    
    <script async custom-element="amp-analytics"
    src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script>
    

  * Start sending the event data to RudderStack by adding the following script inside of your `<body>` tag.
  * You can fetch the AMP config JSON from our [CDN](<https://cdn.rudderlabs.com/amp/rudderstack.json>). The following snippet shows you how to do this:


    
    
    <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
      <script type="application/json">
        {
          "vars": {
            "writeKey": WRITE_KEY,
            "dataPlaneUrl": DATA_PLANE_URL,
            "pageName": "Your Page Name"
          }
        }
      </script>
    </amp-analytics>
    

## Page

You can record the page views on your website using the `page` request. To add custom properties to your page request, you can use the `extraUrlParams` object.

Refer to the custom properties section for details.

RudderStack’s AMP analytics component includes an automatic page view. You can set the name of the automatic page view through `pageName`, as shown in the following snippet:
    
    
    <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
    <script type="application/json">
      {
        "vars": {
          "writeKey": WRITE_KEY,
          "dataPlaneUrl": DATA_PLANE_URL,
          "pageName": "Your Page Name"
        }
      }
    </script>
    </amp-analytics>
    

> ![warning](/docs/images/warning.svg)
> 
> If you fail to provide the value for the `pageName` variable, RudderStack automatically sets the page name to `Unknown Page`.

## Track

You can record any user event on your website using the `track` request, or create a [trigger](<https://amp.dev/documentation/components/amp-analytics/#triggers>) to do so. You need to set the event’s name in the trigger’s variables, as shown in the code snippet below:
    
    
    <body>
    <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
      <script type="application/json">
      {
        "vars": {
          "writeKey": WRITE_KEY,
          "dataPlaneUrl": DATA_PLANE_URL,
          "pageName": "My AMP Page"
        },
        "triggers": {
          "clickEvent": {
            "on": "click",
            "selector":"#clickTrigger",
            "request": "track",
            "vars": {
              "eventName": "new click event"
            },
            "extraUrlParams": {
              "properties.clickType": "href"
            }
          }
        }
      }
      </script>
    </amp-analytics>
    Track - Click <a href="#" id="clickTrigger">here</a> to send
    </body>
    

## Properties

You can send extra properties for your `page` or `track` events to add more information along with the event request. Once you mention the properties as `extraUrlParams` in the `amp-analytics` tag of your implementation, they will be passed to RudderStack for further processing.

> ![warning](/docs/images/warning.svg)
> 
> Prepend `properties.` to the property name within the `extraUrlParams` object so that it can be parsed as the property value in RudderStack. For more information, refer to the Custom properties section below.

### Default properties

RudderStack collects the following properties with each `track` and `page` view:
    
    
    {
      "anonymousId": "amp-<unique-id>",
      "context.locale": "en-US",
      "context.page.path": "/article",
      "context.page.url": "http://example.com/article",
      "context.page.referrer": "referrer",
      "context.page.title": "My Article",
      "context.screen.width": 600,
      "context.screen.height": 800
    }
    

### Custom properties

You can choose to send custom properties by adding the `extraUrlParams` object. Every property name should be prefixed with `properties.`.

A sample call with the custom properties is shown below:
    
    
    <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
    <script type="application/json">
      {
        "vars": {
          "writeKey": WRITE_KEY,
          "dataPlaneUrl": DATA_PLANE_URL,
          "pageName": "Your Page Name"
        },
        "extraUrlParams": {
          "properties.type": "article",
          "properties.published_at": "2016-06-28",
          "properties.author": "John Doe",
          "properties.button_type": "read-more",
          "properties.article_id": "my-article-id"
        }
      }
    </script>
    </amp-analytics>
    

Any property set at the top-level `extraUrlParams` object will be sent with each request. For example, the property `article_id` will be sent for all requests triggered by this snippet.

If you want to add custom properties to a specific event or a `page` call, you need to add an `extraUrlParams` object within your trigger configuration. The following code snippet shows how to do so:
    
    
    <body>
      <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
        <script type="application/json">
        {
          "vars": {
            "writeKey": WRITE_KEY,
            "dataPlaneUrl": DATA_PLANE_URL,
            "pageName": "My AMP Page"
          },
          "triggers": {
            "clickEvent": {
              "on": "click",
              "selector":"#clickTrigger",
              "request": "track",
              "vars": {
                "eventName": "new click event"
              },
              "extraUrlParams": {
                "properties.clickType":"href"
              }
            }
          },
          "extraUrlParams": {
            "properties.type": "article",
            "properties.published_at": "2016-06-28",
            "properties.author": "John Doe",
            "properties.button_type": "read-more",
            "properties.article_id": "my-article-id"
          }
        }
        </script>
      </amp-analytics>
      Track - Click <a href="#" id="clickTrigger">here</a> to send
    </body>
    

The property `clickType` will be sent only for the `track` request, whereas the property `article_id` will be sent for both the requests (the automatic `page` and `track` call).

### UTM parameters

RudderStack does not collect the UTM information from the SDK. Instead, we encourage you to send the properties as `extraUrlParams`.

An example of using `extraUrlParams` is as shown:
    
    
    <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
      <script type="application/json">
        {
        "vars": {
          "writeKey": WRITE_KEY,
          "dataPlaneUrl": DATA_PLANE_URL,
          "pageName": "Your Page Name"
        },
        "extraUrlParams": {
          "properties.utm_source": "google",
          "properties.utm_campaign": "2016-06-28",
          "properties.utm_medium": "email"
        }
      }
      </script>
    </amp-analytics>
    

## AMP Linker

You can use the [AMP Linker](<https://amp.dev/documentation/examples/advertising-analytics/joining_analytics_sessions/>) feature to ensure a merged session for users navigating from cached AMP pages (on an AMP cache) to AMP pages on your domain. When a user navigates from a cached AMP page to an AMP page on your domain, the linker sends the current `AMP ClientID` by adding a URL parameter to the outgoing link. The AMP page on your domain receives this parameter and uses it to set a first-party cookie.

Once this cookie is set, both AMP and Non-AMP pages on your domain use this cookie to identify the user uniquely. This way, the same AMP Client ID (set by the cached AMP page) can be used to identify the user in all contexts.

The following code snippet demonstrates how to enable this feature:
    
    
    <body>
      <amp-analytics config="https://cdn.rudderlabs.com/amp/rudderstack.json">
        <script type="application/json">
          {
            "vars": {
              "writeKey": WRITE_KEY,
              "dataPlaneUrl": DATA_PLANE_URL,
              "pageName": "Your Page Name"
            },
            "linkers": {
              "enabled": true
            }
          }
        </script>
      </amp-analytics>
    </body>
    

You can also use the query parameter from the decorated outgoing link from an AMP cache page to a non-AMP page on your domain by using the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#overriding-anonymous-id>).