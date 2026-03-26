# User Suppression API

Suppress and delete user data in accordance with your user suppression policies.

Available Plans

  * enterprise


* * *

  *  __8 minute read

  * 


This guide explains how to use the User Suppression API to suppress and delete user data in accordance with the compliance and user suppression policies of your organization.

## Overview

With RudderStack’s User Suppression API, you can create regulations to suspend data collection and delete data for specific users. You can apply these regulations across multiple destination integrations simultaneously, simplifying the process of implementing compliance requests.

With these APIs, you can:

  * Add a suppression regulation to drop user events at the source. These events **will not be available** for debugging, replay, or forwarded to destinations.
  * Add a suppression with delete regulation to delete any user data sent to a destination.
  * List all regulations created with the User Suppression API.
  * Delete a specific regulation created previously.


> ![success](/docs/images/tick.svg)
> 
> The User Suppression API is a part of RudderStack’s [Data Governance toolkit](<https://www.rudderstack.com/docs/data-governance/overview/>) that ensures the quality and integrity of your data in a secure and compliant manner.

## How is the User Suppression API helpful?

You can use the User Suppression API to comply with data regulation statutes and users’ privacy choices by:

  * Suppressing incoming source data for a user or list of users.
  * Deleting the collected user data in a given downstream destination or across multiple destinations.


For example, if a user updates their preferences to opt-out of being tracked, you can implement a regulation in the User Suppression API that stops RudderStack from collecting their data at the source, and ensuring no data is sent to downstream destinations. Also, if the user requests to be forgotten, you can delete their data from multiple downstream destinations like Amplitude and Braze with one API call.

## Prerequisites

  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in your RudderStack workspace.


> ![info](/docs/images/info.svg)
> 
> The workspace-level Service Access Token has **Read** permissions by default. You do not need to assign any [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) while generating the token.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Viewer** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Viewer permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

## Authorization

The User Suppression API uses [Bearer Authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the format `Authorization: Bearer <SERVICE_ACCESS_TOKEN>`.

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Specify source and destination IDs in your regulation

To name specific sources for your Suppress regulation, or specific destinations for your Suppress with Delete regulation, you will first need to obtain the respective source and destination IDs.

### Retrieve source ID

You can review the source ID of a particular source from your RudderStack dashboard, as shown:

[![Source ID in RudderStack dashboard](/docs/images/api/suppression-api/source-id.webp)](</docs/images/api/suppression-api/source-id.webp>)

Alternatively, you can retrieve the source ID by using the `/v2/sources` endpoint of the API:

GET

/v2/sources
    
    
    GET /v2/sources HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    

### Retrieve destination ID

You can review the destination ID of a particular destination from your RudderStack dashboard, as shown:

[![Destination ID in RudderStack dashboard](/docs/images/api/suppression-api/destination-id.webp)](</docs/images/api/suppression-api/destination-id.webp>)

Alternatively, you can retrieve the destination ID by using the `/v2/destinations` endpoint of the API:

GET

/v2/destinations
    
    
    GET /v2/destinations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    

## Add a suppression regulation

Add a new user suppression regulation to suppress a given user’s data at the source.

> ![info](/docs/images/info.svg)
> 
> RudderStack processes most suppression requests within 24 hours. However, in some cases, it may take up to 30 days depending on the number of requests in the queue for your workspace.

POST

/v2/regulations

**Request body** :

See Request body for details on the request parameters.

**Example request** :
    
    
    POST /v2/regulations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    Content-Type: application/json
    Content-Length: 182
    
    {
      "regulationType": "suppress",
      "sourceIds": [
        "27OeyCriZ4vGFiOFPihSMgr0Nt1"
      ],
      "users": [
        {
          "userId": "54321",
          "phone": "+12125551212",
          "email": "user@email.com"
        },
        {
          "userId": "54322",
          "randomKey-1": "randomVal-1",
          "randomKey-2": "randomVal-2"
        }
      ]
    }
    
    
    
    curl --location --request POST 'https://api.rudderstack.com/v2/regulations' \
    --header 'Authorization: Bearer 2345678Dv9J5NZsEqVJWLQutE4E' \
    --header 'Content-Type: application/json' \
    --data-raw '{
      "regulationType": "suppress",
      "sourceIds": [
        "27OeyCriZ4vGFiOFPihSMgr0Nt1"
      ],
      "users": [
        {
          "userId": "54321",
          "phone": "+12125551212",
          "email": "user@email.com"
        },
        {
          "userId": "54322",
          "randomKey-1": "randomVal-1",
          "randomKey-2": "randomVal-2"
        }
      ]
    }'
    

**Example response** :
    
    
    [
        {
            "id": "b287a287-6b83-4402-902e-d2793b3e4ba4",
            "workspaceId": "2H2WbKP1613awrY1YgA9Q58wBOc",
            "canceled": false,
            "regulationType": "suppress",
            "attributes": {
                "email": "user@email.com",
                "phone": "+12125551212",
                "userId": "54321"
            }
        },
        {
            "id": "f57475da-5f00-4f77-a22a-26be261ad3b6",
            "workspaceId": "2H2WbKP1613awrY1YgA9Q58wBOc",
            "canceled": false,
            "regulationType": "suppress",
            "attributes": {
                "randomKey-1": "randomVal-1",
                "randomKey-2": "randomVal-2",
                "userId": "54322"
            }
        }
    ]
    

**Status codes** :

A successful request returns a `201` response status.

### Suppression across multiple sources

You can leverage the User Suppression API to suppress all incoming data for a given user. RudderStack drops the events for that user at the source of collection. Suppression applies across all sources, however you can also specify the sources you want to suppress by specifying the source IDs in the request body.

> ![warning](/docs/images/warning.svg)
> 
> Note that after suppression, the events:
> 
>   * Will not be shown in any debuggers.
>   * Will not be forwarded to any destinations.
>   * Will not be available for [event replay](<https://www.rudderstack.com/docs/user-guides/administrators-guide/event-replay/>).
> 


## Add a suppression with delete regulation

Add a new regulation to suppress and delete a given user’s data. See Limitations before using this regulation.

POST

/v2/regulations

**Request body** :

See Request body for details on the request parameters.

**Example request** :
    
    
    POST /v2/regulations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    Content-Type: application/json
    Content-Length: 182
    
    {
        "regulationType": "suppress_with_delete",
        "destinationIds": [
            "27OeyCriZ4vGFiOFPihSMgr0Nt1"
        ],
        "users": [
            {
                "userId": "54321",
                "phone": "+12125551212",
                "email": "user@email.com"
            },
            {
                "userId": "54322",
                "randomKey-1": "randomVal-1",
                "randomKey-2": "randomVal-2"
            }
        ]
    }
    
    
    
    curl --location --request POST 'https://api.rudderstack.com/v2/regulations' \
    --header 'Authorization: Bearer 2345678Dv9J5NZsEqVJWLQutE4E' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "regulationType": "suppress_with_delete",
        "destinationIds": [
            "27OeyCriZ4vGFiOFPihSMgr0Nt1"
        ],
        "users": [
            {
                "userId": "54321",
                "phone": "+12125551212",
                "email": "user@email.com"
            },
            {
                "userId": "54322",
                "randomKey-1": "randomVal-1",
                "randomKey-2": "randomVal-2"
            }
        ]
    }'
    

**Example response** :
    
    
    [
        {
            "id": "5d2417f6-655f-494b-aab7-b0dac55a9b52",
            "workspaceId": "2H2WbKP1613awrY1YgA9Q58wBOc",
            "canceled": false,
            "regulationType": "suppress_with_delete",
            "attributes": {
                "email": "user@email.com",
                "phone": "+12125551212",
                "userId": "54321"
            }
        },
        {
            "id": "f2414ddd-e664-4a22-bd7a-b165138ccd8f",
            "workspaceId": "2H2WbKP1613awrY1YgA9Q58wBOc",
            "canceled": false,
            "regulationType": "suppress_with_delete",
            "attributes": {
                "randomKey-1": "randomVal-1",
                "randomKey-2": "randomVal-2",
                "userId": "54322"
            }
        }
    ]
    

**Status codes** :

A successful request returns a `201` response status.

### Supported destinations

RudderStack supports the `suppress_with_delete` request for the following destinations:

[![Amplitude logo](/docs/images/logos/destinations/amplitude.svg)Amplitude](</docs/destinations/streaming-destinations/amplitude/>)[![AppsFlyer logo](/docs/images/logos/destinations/appsflyer.svg)AppsFlyer](</docs/destinations/streaming-destinations/appsflyer/>)[![Braze logo](/docs/images/logos/destinations/braze.svg)Braze](</docs/destinations/streaming-destinations/braze/>)[![CleverTap logo](/docs/images/logos/destinations/clevertap.webp)CleverTap](</docs/destinations/streaming-destinations/clevertap/>)[![Intercom logo](/docs/images/logos/destinations/intercom.svg)Intercom](</docs/destinations/streaming-destinations/intercom/>)[![Iterable logo](/docs/images/logos/destinations/iterable.svg)Iterable](</docs/destinations/streaming-destinations/iterable/>)[![Mixpanel logo](/docs/images/logos/destinations/mixpanel.svg)Mixpanel](</docs/destinations/streaming-destinations/mixpanel/>)[![Redis logo](/docs/images/logos/destinations/redis.svg)Redis](</docs/destinations/streaming-destinations/redis/>)

  


> ![announcement](/docs/images/announcement.svg)
> 
> Contact [RudderStack Support](<mailto:support@rudderstack.com>) if you need support for a destination that is not listed above.

Note that:

  * You can delete a user for these destinations by specifying the `userId` in the event.
  * Except for **Redis** , you can also specify a custom identifier (optional) in the event along with the `userId`.


### Deletion across multiple destinations

When a user requests that their data be deleted, you can leverage the User Suppression API to delete user data across multiple downstream destinations.

> ![info](/docs/images/info.svg)
> 
> The User Suppression API can delete data only for destinations connected to RudderStack in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

### Limitations

Before using the Suppression with Delete regulation, note that:

  * While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with the respective destination provider if the request is fulfilled.
  * The requests made to the User Suppression API are rate-limited. See Rate limits for more details.


## Request body

regulationType

required

string

Defines the user suppression type. Can be one of `suppress`, which suppresses incoming user data or `suppress_with_delete` which suppresses and deletes events from your specified destinations.

Possible Values: suppress, suppress_with_delete

sourceIds

optional

array

Specify only `sourceIds` with the `suppress` regulation. If no `sourceIds` are specified, RudderStack will suppress data from all sources in the workspace associated with your access token.

destinationIds

optional

array

Specify only `destinationIds` with the `suppress_with_delete` regulation. Otherwise, RudderStack throws an error.

users

required

array

An array of user objects identifying users to be suppressed. The `userId` field is mandatory for all users. You can pass additional custom identifiers such as `email` in the `users` object.

* * *

> ![warning](/docs/images/warning.svg)
> 
> Specify either `sourceIds` or `destinationIds` in your request body — **do not specify both**.

## List user suppressions

List your existing user suppression regulations.

GET

/v2/regulations

**Example request** :
    
    
    GET /v2/regulations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    
    
    
    curl --location --request GET 'https://api.rudderstack.com/v2/regulations' \
    --header 'Authorization: Bearer 23456pCURNbcG0fGRfkgAdcWQsW'
    

**Example response** :
    
    
    {
      "data": [
        {
          "id": "c8fae8a7-1555-4807-89d8-972837671071",
          "workspaceId": "216AlUz1kdkhkh7RFFvJVA9THlq",
          "canceled": false,
          "regulationType": "suppress",
          "attributes": {
            "userId": "12",
            "phone": "1234567890",
            "email": "abc@xyz.com"
          }
        },
        {
          "id": "1ac629bf-d795-45df-8bfb-be06d22a636b",
          "workspaceId": "216AlUz1kdkhkh7RFFvJVA9THlq",
          "canceled": false,
          "regulationType": "suppress_with_delete",
          "attributes": {
            "userId": "rudder-1"
          }
        },
        {
          "id": "7bdf698f-80bd-4278-bb85-414ad8d27888",
          "workspaceId": "216AlUz1kdkhkh7RFFvJVA9THlq",
          "canceled": true,
          "regulationType": "suppress",
          "attributes": {
            "userId": "123",
            "phone": "9876543210",
            "email": "name@email.com"
          }
        }
      ],
      "paging": {
        "next": "/v2/regulations?after_cursor=a450395bb52f4acb99e492c358e104eb"
      },
    }
    

**Response object parameters** :

paging

object

Provides a `next` URL for fetching paginated results. The `next` URL contains an `after_cursor` query parameter.

* * *

## Cancel a user suppression

Cancel an existing user suppression regulation.

DELETE

/v2/regulations{regulation_id}

**Query parameters** :

regulation_id

required

string

The ID of the regulation to be canceled. The `regulation_id` is the `id` that is returned for a regulation in `GET /v2/regulations`.

* * *

**Example request** :
    
    
    DELETE /v2/regulations/f0222ce9-bbaf-4585-9c17-18cde664c0af HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer 2Le5TOgDjwR0djObWRW6Le5kq3E
    
    
    
    curl --location --request DELETE 'http://api.rudderstack.com/v2/regulations/e44c5f3b-b4ca-4b17-8147-7bc1c9620fe3' \
    --header 'Authorization: Bearer 12345nuDv9J5NZsEqVJWLQutE4E'
    

> ![success](/docs/images/tick.svg)
> 
> A successful response returns a `204 No Content` status.

## Rate limits

Requests to the User Suppression API are rate-limited:

Type| Limit (tokens per hour)  
---|---  
Suppression| 4,000  
Deletion| 200,000  
  
Note that:

  * In case of user suppression, 1 user is equivalent to 1 token.
  * For deletion, RudderStack calculates the number of tokens by multiplying the number of users with the number of destinations. For example, if there are `m` users with `n` destinations, the total number of tokens would be `m * n`.