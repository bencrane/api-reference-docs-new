# RudderStack Pixel API

Complete Pixel API reference for tracking events via GET requests when POST is not feasible.

* * *

  * __4 minute read

  * 


This guide provides a complete reference for the RudderStack Pixel API.

## Overview

The RudderStack Pixel API lets you track events and route them to your destinations using `GET` requests. Use this API when `POST` requests are not feasible — for example, when tracking email opens or page views in environments like [AMP](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-amp-analytics/>) where `POST` requests do not add any value.

## Prerequisites

  * The [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) for your workspace must be accessible from your client
  * [Set up a source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) and connect it to a [destination](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#add-a-destination>) in your RudderStack dashboard
  * Note your [source write key](<https://www.rudderstack.com/docs/dashboard-guides/sources/#overview>) to authenticate API requests

[![Source information](/docs/images/dashboard-guides/sources/source-information.webp)](</docs/images/dashboard-guides/sources/source-information.webp>)

## Base URL

Use your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) as the base URL for the Pixel API requests.

## Send a `page` call

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call records page views with optional context and properties.

For the `page` endpoint, RudderStack expects the basic page view properties (`path`, `url`, `referrer`, `title`) to be passed with `context.page.{property}` or with `properties.{property}`.

GET

/pixel/v1/page

**Query parameters**

writeKey

Required

String

Your source write key for authentication

anonymousId

Required

String

Anonymous identifier for the user. Either `userId` or `anonymousId` is required

userId

Optional

String

Unique identifier for the user in your database

name

Optional

String

Name of the page being viewed

context.library.name

Optional

String

Name of the library or SDK (for example, `Rudderstack AMP SDK`)

context.library.version

Optional

String

Version of the library or SDK

context.platform

Optional

String

Platform context (for example, `AMP`)

context.locale

Optional

String

User locale (for example, browser language)

context.userAgent

Optional

String

User agent string

context.screen.width

Optional

String

Screen width in pixels

context.screen.height

Optional

String

Screen height in pixels

context.page.path

Optional

String

Canonical page path

context.page.url

Optional

String

Full page URL

context.page.referrer

Optional

String

Referrer URL

context.page.title

Optional

String

Page title

properties.{key}=${value}

Optional

String

Custom page properties. Pass page view properties like `path`, `url`, `referrer`, and `title` either with `context.page.{property}` or with `properties.{property}`

> ![info](/docs/images/info.svg)
> 
> Parameters that use dot notation (for example, `context.page.path`, `context.screen.width`) represent nested fields in the event payload. RudderStack maps these query parameters to the standard [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event structure before sending to your destinations.

**Example call**
    
    
     https://{DATA_PLANE_URL}/pixel/v1/page?writeKey={WRITE_KEY}&anonymousId=anon-123
    &context.locale=en-US
    &context.userAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)
    &context.page.path=%2Fhome&context.page.url=https%3A%2F%2Fexample.com%2Fhome
    &context.page.referrer=https%3A%2F%2Fexample.com%2F&context.page.title=Home
    &context.screen.width=1920&context.screen.height=1080
    &properties.path=%2Fhome&properties.url=https%3A%2F%2Fexample.com%2Fhome
    &properties.referrer=https%3A%2F%2Fexample.com%2F&properties.title=Home&name=Home%20Page
    

**Resulting event object**

The above call maps to the following event payload (excluding fields RudderStack adds automatically, like `messageId`, `originalTimestamp`, `sentAt`, and `receivedAt`):
    
    
    {
      "type": "page",
      "anonymousId": "anon-123",
      "name": "Home Page",
      "properties": {
        "path": "/home",
        "url": "https://example.com/home",
        "referrer": "https://example.com/",
        "title": "Home"
      },
      "context": {
        "locale": "en-US",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "page": {
          "path": "/home",
          "url": "https://example.com/home",
          "referrer": "https://example.com/",
          "title": "Home"
        },
        "screen": {
          "width": 1920,
          "height": 1080
        }
      }
    }
    

**Response codes**

Code| Description  
---|---  
`200 OK`| Request processed successfully  
`400 Bad Request`| Invalid request or missing required parameters  
  
## Send a `track` call

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call records user actions with event-specific properties.

For the `track` endpoint:

  * Pass basic page view properties (`path`, `url`, `referrer`, `title`) with `context.page.{property}`.
  * Pass event-related properties with `properties.{key}=value`.


GET

/pixel/v1/track

**Query parameters**

writeKey

Required

String

Your source write key for authentication.

anonymousId

Required

String

Anonymous identifier for the user. Either `userId` or `anonymousId` is required.

event

Required

String

Name of the event being tracked.

userId

Optional

String

Unique identifier for the user in your database.

name

Optional

String

Page name for context.

context.library.name

Optional

String

Name of the library or SDK (for example, `Rudderstack AMP SDK`).

context.library.version

Optional

String

Version of the library or SDK.

context.platform

Optional

String

Platform context (for example, `AMP`).

context.locale

Optional

String

User locale (for example, browser language).

context.userAgent

Optional

String

User agent string.

context.screen.width

Optional

String

Screen width in pixels.

context.screen.height

Optional

String

Screen height in pixels.

context.page.path

Optional

String

Canonical page path.

context.page.url

Optional

String

Full page URL.

context.page.referrer

Optional

String

Referrer URL.

context.page.title

Optional

String

Page title.

properties.{key}

Optional

String

Custom event properties. Use `context.page.{property}` for page view properties; use `properties.{key}=value` for event-specific properties.

> ![info](/docs/images/info.svg)
> 
> Parameters that use dot notation (for example, `context.page.path`, `properties.productId`) represent nested fields in the event payload. RudderStack maps these query parameters to the standard [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event structure before sending to your destinations.

**Example call**
    
    
     https://{DATA_PLANE_URL}/pixel/v1/track?writeKey={WRITE_KEY}&anonymousId=anon-123
    &context.locale=en-US
    &context.userAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)
    &context.page.path=%2Fproduct%2Fsku-123&context.page.url=https%3A%2F%2Fexample.com%2Fproduct%2Fsku-123
    &context.page.referrer=https%3A%2F%2Fexample.com%2F&context.page.title=Product%20Page
    &context.screen.width=1920&context.screen.height=1080&name=Product%20Page
    &event=Product%20Viewed&properties.productId=sku-123&properties.revenue=29.99
    

**Resulting event object**

The example call above maps to the following event payload (excluding fields RudderStack adds automatically, such as `messageId`, `originalTimestamp`, `sentAt`, and `receivedAt`):
    
    
    {
      "type": "track",
      "anonymousId": "anon-123",
      "event": "Product Viewed",
      "name": "Product Page",
      "properties": {
        "productId": "sku-123",
        "revenue": 29.99
      },
      "context": {
        "locale": "en-US",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "page": {
          "path": "/product/sku-123",
          "url": "https://example.com/product/sku-123",
          "referrer": "https://example.com/",
          "title": "Product Page"
        },
        "screen": {
          "width": 1920,
          "height": 1080
        }
      }
    }
    

**Response codes**

Code| Description  
---|---  
`200 OK`| Request processed successfully  
`400 Bad Request`| Invalid request or missing required parameters  
  
## Limitations

The Pixel API does not support overriding the `integration` key to send data to selective destinations. All configured destinations receive the events.