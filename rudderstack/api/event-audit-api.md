# Event Audit API v2

Get event metadata to ensure compliance with your data governance policies.

Available Plans

  * enterprise


* * *

  *  __8 minute read

  * 


RudderStack’s Event Audit API gives you full access to your event metadata, including event schemas and their versions.

> ![success](/docs/images/tick.svg)
> 
> The Event Audit API is a part of RudderStack’s [Data Governance toolkit](<https://www.rudderstack.com/docs/data-governance/overview/>) that ensures the quality and integrity of your data in a secure and compliant manner.

## Prerequisites

  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in your RudderStack workspace.


> ![info](/docs/images/info.svg)
> 
> The workspace-level Service Access Token has **Read** permissions by default. You do not need to assign any [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) while generating the token.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Viewer** permission.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Viewer permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

## Authentication

The Event Audit API uses [Bearer authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the following format:
    
    
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Enable Event Audit API

To enable the Event Audit API in the RudderStack dashboard:

  1. Go to **Settings** > **Workspace** and click the **Data Management** tab.
  2. Scroll down to the **Data governance** section and toggle on the **Event audit API** setting.


> ![warning](/docs/images/warning.svg)
> 
> Only users with the [Org Admin](<https://www.rudderstack.com/docs/dashboard-guides/user-management/#organization-roles>) role have the access to this setting.

[![Event Audit API setting in RudderStack dashboard](/docs/images/api/event-audit-api-dashboard.webp)](</docs/images/api/event-audit-api-dashboard.webp>)

When this setting is turned on, you can leverage the Event Audit API to create and manage your [tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>). Use these plans to monitor and act on any non-compliant data coming into your RudderStack sources based on predefined rules.

Also, note that the Event Audit API collects sample events (used for fetching event schema version by ID) only if the [Sample event data](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#sample-event-data>) toggle is turned on.

[![Opt in to sample event data storage](/docs/images/dashboard-guides/sample-event-data.webp)](</docs/images/dashboard-guides/sample-event-data.webp>)

## Get all event schemas

GET

/v2/schemas

**Example Request** :
    
    
    "GET /v2/schemas HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "results": [{
          "uid": "2Vi1RvrDVL1cQwij9UHNWr0za2U",
          "writeKey": "2VFrTRhKIgDFLYImdhWTvQUiqhE",
          "eventType": "track",
          "eventIdentifier": "Test event 3",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "event": "string",
            "messageId": "string",
            "properties.full-time": "bool",
            "properties.name": "string",
            "properties.price": "float64",
            "properties.product": "string",
            "properties.product_id": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:47:53.612087Z",
          "lastSeen": "2023-09-21T13:55:06.852916Z",
          "count": 2
        },
        {
          "uid": "2Vi2jEzAD5fY3STlEXQSwjEhEQh",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "identify",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.traits.city": "string",
            "context.traits.country": "string",
            "context.traits.email": "string",
            "context.traits.name": "string",
            "context.traits.testMap.notNested.a": "float64",
            "messageId": "string",
            "rudderId": "string",
            "timestamp": "string",
            "traits.age": "float64",
            "traits.anonymousId": "string",
            "traits.firstName": "string",
            "traits.lastName": "string",
            "traits.phone": "string",
            "traits.userId": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:58:27.993077Z",
          "lastSeen": "2023-09-21T13:58:27.993077Z",
          "count": 1
        },
        {
          "uid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        }
      ],
      "currentPage": 1
    }
    

### Filter by source

To filter event schemas by source, specify the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) as a query parameter.

GET

/v2/schemas?writeKey={writeKey}

**Path parameters**

writeKey

required

String

Write key of the source for which you want to fetch the event schemas.

* * *

**Example Request** :
    
    
    "GET /v2/schemas?writeKey=2PyHFFtH978n7xob6RCJ3BQ9nKu HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas?writeKey=2PyHFFtH978n7xob6RCJ3BQ9nKu' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "results": [{
          "uid": "2Vi2jEzAD5fY3STlEXQSwjEhEQh",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "identify",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.traits.city": "string",
            "context.traits.country": "string",
            "context.traits.email": "string",
            "context.traits.name": "string",
            "context.traits.testMap.notNested.a": "float64",
            "messageId": "string",
            "rudderId": "string",
            "timestamp": "string",
            "traits.age": "float64",
            "traits.anonymousId": "string",
            "traits.firstName": "string",
            "traits.lastName": "string",
            "traits.phone": "string",
            "traits.userId": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:58:27.993077Z",
          "lastSeen": "2023-09-21T13:58:27.993077Z",
          "count": 1
        },
        {
          "uid": "2Vi2LAqj4XrEc6N23ztNdpgikYl",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 112",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:55:19.860445Z",
          "lastSeen": "2023-09-21T13:55:21.866016Z",
          "count": 3
        },
        {
          "uid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        }
      ],
      "currentPage": 1
    }
    

### Filter by page

To filter event schemas by page, specify the page number as a query parameter.

GET

/v2/schemas?page={number}

> ![info](/docs/images/info.svg)
> 
> Default page size is 50 - one page contains 50 event schemas.

**Example Request** :
    
    
    "GET /v2/schemas?page=1 HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas?page=1' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "results": [{
          "uid": "2Vi2jEzAD5fY3STlEXQSwjEhEQh",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "identify",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.traits.city": "string",
            "context.traits.country": "string",
            "context.traits.email": "string",
            "context.traits.name": "string",
            "context.traits.testMap.notNested.a": "float64",
            "messageId": "string",
            "rudderId": "string",
            "timestamp": "string",
            "traits.age": "float64",
            "traits.anonymousId": "string",
            "traits.firstName": "string",
            "traits.lastName": "string",
            "traits.phone": "string",
            "traits.userId": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:58:27.993077Z",
          "lastSeen": "2023-09-21T13:58:27.993077Z",
          "count": 1
        },
        {
          "uid": "2Vi2LAqj4XrEc6N23ztNdpgikYl",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 112",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:55:19.860445Z",
          "lastSeen": "2023-09-21T13:55:21.866016Z",
          "count": 3
        },
        {
          "uid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "createdAt": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        }
      ],
      "currentPage": 1
    }
    

> ![info](/docs/images/info.svg)
> 
> You can also pass the write key and page number together in the following format:
> 
> GET
> 
> /v2/schemas?writeKey={writeKey}&page={number}

## Get schema by ID

Gets event schema details based on the specified schema ID.

GET

/v2/schemas/{schemaID}

**Path parameters**

schemaID

required

String

ID of the event schema you want to fetch.

* * *

**Example Request** :
    
    
    "GET /v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "uid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
      "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
      "eventType": "track",
      "eventIdentifier": "Order Viewed 113",
      "schema": {
        "anonymousId": "string",
        "context.ip": "string",
        "context.library.name": "string",
        "context.userAgent": "string",
        "event": "string",
        "messageId": "string",
        "properties.amount": "float64",
        "properties.city": "string",
        "properties.park": "string",
        "properties.price": "float64",
        "properties.product": "string",
        "rudderId": "string",
        "timestamp": "string",
        "type": "string",
        "userId": "string"
      },
      "createdAt": "2023-09-21T13:56:19.910831Z",
      "lastSeen": "2023-09-21T14:09:31.415404Z",
      "count": 5,
      "latestVersions": [{
          "uid": "2Vi45IOhtqw4a8yJCh4JJnyTNKs",
          "firstSeen": "2023-09-21T14:09:31.415404Z",
          "lastSeen": "2023-09-21T14:09:31.415404Z",
          "count": 1
        },
        {
          "uid": "2Vi42oQQPGWwaBUHOmc6tnZtASa",
          "firstSeen": "2023-09-21T14:09:18.399919Z",
          "lastSeen": "2023-09-21T14:09:18.399919Z",
          "count": 1
        },
        {
          "uid": "2Vi2Sq70lF8DhnNEg5PijmU48kR",
          "firstSeen": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        }
      ]
    }
    

## Get all versions of event schema

GET

/v2/schemas/{schemaID}/versions

**Path parameters**

schemaID

required

String

ID of the event schema you want to fetch.

* * *

**Example Request** :
    
    
    "GET /v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "results": [{
          "uid": "2Vi2Sq70lF8DhnNEg5PijmU48kR",
          "schemaUid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "firstSeen": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        },
        {
          "uid": "2Vi45IOhtqw4a8yJCh4JJnyTNKs",
          "schemaUid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.city": "string",
            "properties.park": "string",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "firstSeen": "2023-09-21T14:09:31.415404Z",
          "lastSeen": "2023-09-21T14:09:31.415404Z",
          "count": 1
        }
      ],
      "currentPage": 1
    }
    

### Filter by page

To filter event schema versions by page, specify the page number as a query parameter.

GET

/v2/schemas?page={number}

> ![info](/docs/images/info.svg)
> 
> Default page size is 10 - one page contains 10 event schema versions.

**Example Request** :
    
    
    "GET /v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions?page=1 HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions?page=1' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "results": [{
          "uid": "2Vi2Sq70lF8DhnNEg5PijmU48kR",
          "schemaUid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "firstSeen": "2023-09-21T13:56:19.910831Z",
          "lastSeen": "2023-09-21T13:56:19.910831Z",
          "count": 3
        },
        {
          "uid": "2Vi45IOhtqw4a8yJCh4JJnyTNKs",
          "schemaUid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
          "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
          "eventType": "track",
          "eventIdentifier": "Order Viewed 113",
          "schema": {
            "anonymousId": "string",
            "context.ip": "string",
            "context.library.name": "string",
            "context.userAgent": "string",
            "event": "string",
            "messageId": "string",
            "properties.amount": "float64",
            "properties.city": "string",
            "properties.park": "string",
            "properties.price": "float64",
            "properties.product": "string",
            "rudderId": "string",
            "timestamp": "string",
            "type": "string",
            "userId": "string"
          },
          "firstSeen": "2023-09-21T14:09:31.415404Z",
          "lastSeen": "2023-09-21T14:09:31.415404Z",
          "count": 1
        }
      ],
      "currentPage": 1
    }
    

## Get schema version by ID

GET

/v2/schemas/{schemaID}/versions/{versionID}

**Path parameters**

schemaID

required

String

ID of the event schema you want to fetch.

versionID

required

String

ID of the specific schema version you want to fetch.

* * *

**Example Request** :
    
    
    "GET /v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions/2Vi45IOhtqw4a8yJCh4JJnyTNKs HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq"
    
    
    
    "curl --location 'https://api.rudderstack.com/v2/schemas/2Vi2Su09PnHfaBPie2lKEMEkJjB/versions/2Vi45IOhtqw4a8yJCh4JJnyTNKs' \
    --header 'Authorization: Bearer 2VhyC7yQumW09M6GF5Yqcp6HIiq'"
    

**Example Response** :
    
    
    {
      "uid": "2Vi45IOhtqw4a8yJCh4JJnyTNKs",
      "schemaUid": "2Vi2Su09PnHfaBPie2lKEMEkJjB",
      "writeKey": "2PyHFFtH978n7xob6RCJ3BQ9nKu",
      "eventType": "track",
      "eventIdentifier": "Order Viewed 113",
      "schema": {
        "anonymousId": "string",
        "context.ip": "string",
        "context.library.name": "string",
        "context.userAgent": "string",
        "event": "string",
        "messageId": "string",
        "properties.amount": "float64",
        "properties.city": "string",
        "properties.park": "string",
        "properties.price": "float64",
        "properties.product": "string",
        "rudderId": "string",
        "timestamp": "string",
        "type": "string",
        "userId": "string"
      },
      "firstSeen": "2023-09-21T14:09:31.415404Z",
      "lastSeen": "2023-09-21T14:09:31.415404Z",
      "count": 1,
      "sample": "eyJ0eXBlIjogInRyYWNrIiwgImV2ZW50IjogIk9yZGVyIFZpZXdlZCAwOTg3Iiw
      gInVzZXJJZCI6ICJpZGVudGlmaWVkIHVzZXIgaWQ2OCIsICJjb250ZXh0IjogImFiYyIsICJy
      dWRkZXJJZCI6ICI3OTNjN2QxNi05YWE0LTRiYTUtODJhMi0xMWUzZGE1YjFkMDAiLCAib
      WVzc2FnZUlkIjogIjQxNWU4ZDdkLWFlNzgtNDE4Mi1hMWIxLTM2M2Y0Y2JjYjhlOSIsICJ0a
      W1lc3RhbXAiOiAiMjAyMC0wMi0wMlQwMDoyMzowOS41NDRaIiwgInByb3BlcnRpZXMiOiB
      7InByaWNlIjogIm5pbmV0eSBvbmUiLCAiYW1vdW50IjogMTAxLCAib3B0aW9ucyI6IHsib3B0
      aW9uMSI6ICJoeWRlcmFiYWQiLCAib3B0aW9uMiI6ICJiYW5nYWxvcmUiLCAib3B0aW9uMyI
      6ICJjaGVubmFpIiwgIm9wdGlvbjQiOiAia29jaGkiLCAib3B0aW9uNSI6ICJiYXBhdGxhIiwgIm9w
      dGlvbjYiOiAibXVtYmFpIiwgIm9wdGlvbjciOiAicG9uZHkifSwgInByb2R1Y3QiOiAic2hvZXMifSw
      gImFub255bW91c0lkIjogImFub24taWQtbmV3NjgifQ=="
    }
    

> ![info](/docs/images/info.svg)
> 
> In the above response, the `sample` parameter is the sample event encoded in Base64 format.
> 
> As mentioned above, the Event Audit API collects sample events only if the [Sample event data](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#sample-event-data>) toggle is turned on in the [Data management](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#sample-event-data>) settings.

## API responses

The API responds with a `200` HTTP status code for all successful requests. If the authentication fails, you will get a `400` status with the appropriate error message.