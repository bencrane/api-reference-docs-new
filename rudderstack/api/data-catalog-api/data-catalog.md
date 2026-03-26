# Catalog API Endpoints for Data Catalog

Use the Data Catalog API to create and manage events, properties, categories, and custom data types in your data catalog.

Available Plans

  * growth
  * enterprise


* * *

  *  __25 minute read

  * 


This guide covers the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>) endpoints for:

  * Managing data catalog events
  * Managing data catalog properties
  * Managing data catalog categories
  * Managing custom data types


## Prerequisites

  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Data Catalog and Tracking Plans:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit**  
Data Catalog| **Edit**  
  
  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## Authentication

The Data Catalog API uses [Bearer authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the following format:
    
    
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com/v2
    
    
    
    https://api.eu.rudderstack.com/v2
    

## Manage data catalog events

This section covers the API endpoints for creating and managing events in your [data catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>).

### Create new event

POST

/catalog/events

**Request body**

name

Required for `track` events only

String

Name of the event.  
  
Note the following:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.
  * Do not include this parameter for non-`track` events like `identify`, `page,` or `group`, as it will result in an error.


description

Optional

String

Event description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

eventType

Optional

String

Type of event to be created in the data catalog.  
  
Note that:

  * Once set, the event type **cannot** be updated later.
  * Allowed event types are `track`, `identify`, `group`, `page`, and `screen`.


categoryId

Optional

String

Category ID of the event. It should be a valid, non-empty string.

**Example request**
    
    
     POST /v2/catalog/events HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 145
    
    {
      "name": "Product Viewed",
      "description": "User viewed a product",
      "eventType": "track",
      "categoryId": null
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/events' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: ••••••' \
    --data '{
      "name": "Product Viewed",
      "description": "User viewed a product",
      "eventType": "track",
      "categoryId": null
    }'
    

**Example response**
    
    
    {
      "name": "Product Viewed",
      "description": "User viewed a product.",
      "eventType": "track",
      "categoryId": null,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "id": "ev_2gqmsfib1Zl6n6QL0mjCi9PJbDS",
      "createdAt": "2024-05-23T03:08:09.972Z",
      "updatedAt": "2024-05-23T03:08:09.972Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is created successfully.  
400| Invalid request.  
  
### List all events

GET

/catalog/events

**Query parameters**

orderBy

Optional

String

Order the events list by a specific field.  


Allowed fields are `name`, `createdAt`, `updatedAt`. For example, `name:asc`.

page

Optional

Number

In a paginated view, all the response entries are divided into pages. Use this field to specify which page of results to return. Default value is **1**.  
  
**Note** :  
  


  * This parameter must be a positive integer.
  * The API returns a maximum of 50 pages.


**Example request**
    
    
     GET /v2/catalog/events?page=1&orderBy=name:desc HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/events?page=1&orderBy=name%3Adesc' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "data": [{
          "id": "ev_2g60ZQeit5D54rBHUUh0oK3IxzH",
          "name": "Order Placed",
          "description": "User placed an order.",
          "eventType": "track",
          "categoryId": null,
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "updatedBy": null,
          "createdAt": "2024-05-06T13:39:34.294Z",
          "updatedAt": "2024-05-06T13:39:34.294Z"
        },
        ....
    
        {
          "id": "ev_2dJfRK8t0hOmmAaCTc0VvMB36e1",
          "name": "Product Added to Cart",
          "description": "User added product to cart.",
          "eventType": "track",
          "categoryId": null,
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "updatedBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "createdAt": "2024-03-06T13:18:12.044Z",
          "updatedAt": "2024-05-13T11:39:40.115Z"
        },
      ],
      "total": 3563,
      "currentPage": 1,
      "pageSize": 50
    }
    

**Response codes**

Code| Description  
---|---  
200| All events in the data catalog are retrieved successfully.  
  
The response body contains the below fields:

Field| Type| Description  
---|---|---  
`data`| Array| Contains all the events in the data catalog.  
`total`| Number| Total number of entries in the response.  
`currentPage`| Number| Current page number being viewed (starts from 1).  
`pageSize`| Number| Maximum number of items displayed per page.  
  
### Get event by ID

GET

/catalog/events/{eventId}

**Path parameters**

eventId

Required

String

The event ID.

**Example request**
    
    
     GET /v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "id": "ev_2dJfRQIZLrBhqdLoLoxywHpicLp",
      "name": "Product Viewed",
      "description": "User viewed a product.",
      "eventType": "track",
      "categoryId": null,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
      "updatedBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "createdAt": "2024-03-06T13:18:12.044Z",
      "updatedAt": "2024-05-22T14:57:50.265Z",
      "category": null
    }
    

**Response codes**

Code| Description  
---|---  
200| All events in the data catalog are retrieved successfully.  
404| Event not found for the specified event ID.  
  
### Update event

PUT

/catalog/events/{eventId}

> ![info](/docs/images/info.svg)
> 
> Changes to events are applied immediately. However, it may take a couple of minutes for all dependent tracking plans to reflect these updates.

**Path parameters**

eventId

Required

String

The event ID.

**Request body**

To update an event in the data catalog, **at least one** of the following parameters is required:

name

String

Name of the event.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.
  * Do not include this parameter for non-`track` events like `identify`, `page,` or `group`, as it will result in an error.


description

String

Event description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

categoryId

String

Category ID of the event. It should be a valid, non-empty string.

**Example request**
    
    
     PUT /v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 98
    
    {
      "name": "Product Viewed Again",
      "description": "User viewed a product again.",
      "categoryId": null
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
      "name": "Product Viewed Again",
      "description": "User viewed a product again.",
      "categoryId": null
    }'
    

**Example response**
    
    
    {
      "name": "Product Viewed Again",
      "description": "User revisited a product on the website.",
      "categoryId": null
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is updated successfully.  
404| Event not found for the specified event ID.  
  
### Delete event

> ![warning](/docs/images/warning.svg)
> 
> You cannot delete an event that is connected to a tracking plan. Use the Delete event from tracking plan API to disconnect the event and then try deleting it.

DELETE

/catalog/events/{eventId}

**Path parameters**

eventId

Required

String

Event ID.

**Example request**
    
    
     DELETE /v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/events/ev_2dJfRQIZLrBhqdLoLoxywHpicLp' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "name": "Product Purchased",
      "description": "User purchased a product on the website.",
      "eventType": "track",
      "categoryId": null,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": null,
      "createdAt": "2024-05-22T14:59:14.287Z",
      "updatedAt": "2024-05-22T14:59:14.287Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is deleted from the catalog successfully.  
404| Event not found for the specified event ID.  
  
## Manage data catalog properties

This section covers the API endpoints for creating and managing properties in your [data catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>).

### Create new property

POST

/catalog/properties

**Request body**

name

Required

String

Property name.  
  
Note that the name must be between 1 and 65 characters.

description

Optional

String

Property description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

type

Required

String

Data type of the property.  
  
Note that:

  * The data type must be either string, integer, number, object, array, boolean, null, or multi data type.
  * If not explicitly set, RudderStack allows all the above data types for the property, by default.


propConfig

Optional

Object

Advanced rules for the property. See [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/>) for the complete list of supported keywords.

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports multi data type for the `type` parameter. An example is shown:
>     
>     
>     {
>       "type": ["string", "integer", "boolean", "null"]
>     }
>     

#### Keyword validations

The API validates the data types for the various keywords defined in the `propConfig` parameter and gives an error if you pass an invalid value for any field.

See this FAQ for more information on the type-specific keywords supported by RudderStack.

For example, if you pass the `propConfig` object as follows:
    
    
    {
      "type": "string",
      ...
    
      "propConfig": {
        "maxLength": "4",   // String instead of a number.
        "title": 45   // Number instead of a string
      }
    }
    

Then, you will get the below error:
    
    
    {
      "error": "max length must be an integer, title must be a string"
    }
    

**Example request**
    
    
     POST /v2/catalog/properties HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 117
    
    {
      "name": "amount",
      "description": "Amount for the product",
      "type": "number",
      "propConfig": {
          "multipleOf": 2
      },
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/properties' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
      "name": "amount",
      "description": "Amount for the product",
      "type": "number",
      "propConfig": {
          "multipleOf": 2
      },
    }'
    

**Example response**
    
    
    {
      "name": "amount",
      "description": "Amount for the product",
      "type": "number",
      "propConfig": {
          "multipleOf": 2
      },
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "id": "prop_2gqpkKg1GtHWKR8JtNChoKsqhIK",
      "createdAt": "2024-05-23T03:31:43.297Z",
      "updatedAt": "2024-05-23T03:31:43.297Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Property is created successfully.  
400| Invalid request.  
  
### List all properties

GET

/catalog/properties

**Path parameters**

orderBy

Optional

String

Order the properties list by a specific field.  


Allowed fields are `name`, `createdAt`, `updatedAt`. For example, `name:asc`.

page

Optional

Number

In a paginated view, all the response entries are divided into pages. Use this field to specify which page of results to return. Default value is **1**.  
  
**Note** :  
  


  * This parameter must be a positive integer.
  * The API returns a maximum of 50 pages.


**Example request**
    
    
     GET /v2/catalog/properties?page=1&orderBy=name:asc HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/properties?page=1&orderBy=name%3Aasc' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "data": [{
          "id": "prop_2dJfRQ233WrPRpWBPqbF4PuiMc0",
          "name": "affiliation",
          "description": "Product affiliation",
          "type": "string",
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "updatedBy": null,
          "createdAt": "2024-03-06T13:18:12.044Z",
          "updatedAt": "2024-03-06T13:18:12.044Z"
        },
    
        ...
    
        {
          "id": "prop_2bfXbQuinn4298XzqlyxmktRAX9d",
          "name": "Email",
          "description": "User's email",
          "type": "string",
          "propConfig": {},
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "updatedBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "createdAt": "2024-01-30T09:32:57.983Z",
          "updatedAt": "2024-01-30T09:33:18.885Z"
        }
      ],
      "total": 450,
      "currentPage": 1,
      "pageSize": 50
    }
    

**Response codes**

Code| Description  
---|---  
200| All properties in the data catalog are retrieved successfully.  
  
The response body contains the below fields:

Field| Type| Description  
---|---|---  
`data`| Array| Contains all the properties in the data catalog.  
`total`| Number| Total number of entries in the response.  
`currentPage`| Number| Current page number being viewed (starts from 1).  
`pageSize`| Number| Maximum number of items displayed per page.  
  
### Get property by ID

GET

/catalog/properties/{propertyId}

**Path parameters**

propertyId

Required

String

Property ID.

**Example request**
    
    
     GET /v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "id": "prop_2bfXbQuinn4298XzqlyxmktRAX9d",
      "name": "Email",
      "description": "User's email",
      "type": "string",
      "propConfig": {},
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
      "updatedBy": "1zirfVbEQN0zIImR235a1JivVYU",
      "createdAt": "2024-01-30T09:32:57.983Z",
      "updatedAt": "2024-01-30T09:33:18.885Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Property for the specified ID is retrieved successfully.  
404| Property not found for the specified event ID.  
  
### Update property

PUT

/catalog/properties/{propertyId}

> ![info](/docs/images/info.svg)
> 
> Changes to properties are applied immediately. However, it may take a couple of minutes for all dependent tracking plans to reflect these updates.

**Path parameters**

propertyId

Required

String

Property ID.

**Request body**

To update the event property in the data catalog, **at least one** of the following parameters is required:

name

String

Property name.  
  
Note that the name must be between 1 and 65 characters.

description

String

Property description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

type

String

Data type of the property.  
  
Note that:

  * The data type must be either string, integer, number, object, array, boolean, null, or multi data type.
  * If not explicitly set, RudderStack allows all the above data types for the property, by default.


propConfig

Optional

Object

Advanced rules for the property. See [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/>) for the complete list of supported keywords.

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports multi data type for the `type` parameter. An example is shown:
>     
>     
>     {
>       "type": ["string", "integer", "boolean", "null"]
>     }
>     

#### Keyword validations

The API validates the data types for the various keywords defined in the `propConfig` parameter and gives an error if you pass an invalid value for any field.

See this FAQ for more information on the type-specific keywords supported by RudderStack.

For example, if you pass the `propConfig` object as follows:
    
    
    {
      "type": "string",
      ...
    
      "propConfig": {
        "maxLength": "4",   // String instead of a number.
        "title": 45   // Number instead of a string
      }
    }
    

Then, you will get the below error:
    
    
    {
      "error": "max length must be an integer, title must be a string"
    }
    

**Example request**
    
    
     PUT /v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 45
    
    {
      "description": "User's email address",
      "propConfig": {
          "format": "email"
      }
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
      "description": "User's email address",
      "propConfig": {
          "format": "email"
      }
    }'
    

**Example response**
    
    
    {
      "id": "prop_2bfXbQuinn4298XzqlyxmktRAX9d",
      "name": "Email",
      "description": "User's email address",
      "propConfig": {
          "format": "email"
      },
      "type": "number",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
      "updatedBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "createdAt": "2024-01-30T09:32:57.983Z",
      "updatedAt": "2024-05-23T03:41:10.715Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Property is updated successfully.  
400| Property not found for the specified event ID.  
  
### Delete property

DELETE

/catalog/properties/{propertyId}

**Path parameters**

propertyId

Required

String

Property ID.

**Example request**
    
    
     DELETE /v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/properties/prop_2bfXbQuinn4298XzqlyxmktRAX9d' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "name": "Email",
      "description": "User's email address",
      "type": "number",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
      "updatedBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "createdAt": "2024-01-30T09:32:57.983Z",
      "updatedAt": "2024-05-23T03:41:10.715Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Property is deleted from the catalog successfully.  
400| Property not found for the specified event ID.  
  
## Manage data catalog categories

This section covers the API endpoints for creating and managing categories in your [data catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>). Go to **Govern** > **Data Catalog** > **Events** tab in your RudderStack dashboard to view the categories and associate them to your events.

[![Data catalog categories](/docs/images/data-governance/categories.webp)](</docs/images/data-governance/categories.webp>)

### Create new category

POST

/catalog/categories

**Request body**

name

Required

String

Category name.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.


description

Optional

String

Category description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

**Example request**
    
    
     POST /v2/catalog/categories HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 70
    
    {
      "name": "Onboarding",
      "description": "Customer onboarding"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/categories' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
      "name": "Onboarding",
      "description": "Customer onboarding"
    }'
    

**Example response**
    
    
    {
      "name": "Onboarding",
      "description": "Customer onboarding",
      "icon": "star",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "id": "cat_2gqs1Yzy1Vpeeewm69meqc6d8zH",
      "createdAt": "2024-05-23T03:50:27.416Z",
      "updatedAt": "2024-05-23T03:50:27.416Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Category is created successfully.  
400| Invalid Request.  
  
### List all categories

GET

/catalog/categories

**Path parameters**

orderBy

Optional

String

Order the categories list by a specific field.  


Allowed fields are `name`, `createdAt`, `updatedAt`. For example, `name:asc`.

page

Optional

Number

In a paginated view, all the response entries are divided into pages. Use this field to specify which page of results to return. Default value is **1**.  
  
**Note** :  
  


  * This parameter must be a positive integer.
  * The API returns a maximum of 50 pages.


**Example request**
    
    
     GET /v2/catalog/categories HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/categories' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "data": [{
          "id": "cat_2gqs1Yzy1Vpeeewm69meqc6d8zH",
          "name": "Onboarding",
          "description": "Customer onboarding",
          "icon": "star",
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
          "updatedBy": null,
          "createdAt": "2024-05-23T03:50:27.416Z",
          "updatedAt": "2024-05-23T03:50:27.416Z"
        },
    
        ...
    
        {
          "id": "cat_4gs21Yzy1Vpw1m69meqc6d8zH",
          "name": "Product Experience",
          "description": "Enhance overall product and customer experience",
          "icon": "star",
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
          "createdBy": "1zirfVbEQN0zIImR235a1JivVYU",
          "updatedBy": null,
          "createdAt": "2024-04-30T14:30:30.254Z",
          "updatedAt": "2024-04-30T14:30:30.254Z"
        }
      ],
      "total": 10,
      "currentPage": 1,
      "pageSize": 1000
    }
    

**Response codes**

Code| Description  
---|---  
200| All the categories are fetched successfully.  
  
The response body contains the below fields:

Field| Type| Description  
---|---|---  
`data`| Array| Contains all the categories in the data catalog.  
`total`| Number| Total number of entries in the response.  
`currentPage`| Number| Current page number being viewed (starts from 1).  
`pageSize`| Number| Maximum number of items displayed per page.  
  
### Get category by ID

GET

/catalog/categories/{categoryId}

**Path parameters**

categoryId

Required

String

Category ID.

**Example request**
    
    
     GET /v2/catalog/categories/cat_2gqs1Yzy1Vpeeewm69meqc6d8zH HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/categories/cat_2gqs1Yzy1Vpeeewm69meqc6d8zH' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "id": "cat_2gqs1Yzy1Vpeeewm69meqc6d8zH",
      "name": "Onboarding",
      "description": "Customer onboarding",
      "icon": "star",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": null,
      "createdAt": "2024-05-23T03:50:27.416Z",
      "updatedAt": "2024-05-23T03:50:27.416Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Category for the specified ID is retrieved successfully.  
404| Category not found for the specified ID.  
  
### Delete category

DELETE

/catalog/categories/{categoryId}

**Path parameters**

categoryId

Required

String

Category ID.

**Example request**
    
    
     DELETE /v2/catalog/categories/cat_2gqs1Yzy1Vpeeewm69meqc6d8zH HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/categories/cat_2gqs1Yzy1Vpeeewm69meqc6d8zH' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "name": "Onboarding",
      "description": "Customer onboarding",
      "icon": "star",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": null,
      "createdAt": "2024-05-23T03:50:27.416Z",
      "updatedAt": "2024-05-23T03:50:27.416Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Category is deleted from the catalog successfully.  
400| Category not found for the specified event ID.  
  
## Manage custom data types

> ![announcement](/docs/images/announcement.svg)
> 
> The endpoints covered in this section are in **Closed Beta** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/>), where we work with early users and customers to test new features and get feedback.
> 
> Note that these features are functional but can change as we improve them. [Contact](<mailto:product@rudderstack.com>) the RudderStack team to get access.

This section covers the API endpoints for creating and managing [custom data types](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#custom-data-types>) in your data catalog.

### Create custom type

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)

POST

/catalog/custom-types

**Request body**

> ![warning](/docs/images/warning.svg)
> 
> The request body must not be empty. Otherwise, you will encounter an error.

name

Required

String

Custom type name.  
  
Note that:

  * The custom type name must be between 2 and 65 characters long.
  * It must start with a capital letter and contain only letters, numbers, underscores and dashes. Spaces are **not** allowed.
  * You cannot change the custom type name later.


description

Optional

String

Custom type description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

type

Required

String

Valid data type. Acceptable values are `string`, `number`, `integer`, `boolean`, `null`, `array`, and `object`.

config

Required

Object

Custom type configuration. See Config object for more details.

properties

Required for object type

Array

Array of properties. See Properties structure for more information on passing this array in the request body.  
  
**This parameter is ignored for non-object data types.**

#### Config object

You must include the `config` object to create a new custom type successfully. You can also pass an empty object to accept any values.

The `config` object can take the below parameters depending on `type` (data type of the custom type) specified in the request body:

Custom data type| Acceptable fields  
---|---  
String| | Field| Description  
---|---  
`enum`| Array of acceptable values for the custom type.  
`minLength`| Number defining the minimum string length for the custom type.  
`maxLength`| Number defining the maximum string length for the custom type.  
`pattern`| Regular expression defining the constraints for the property.  
  
You can also define a custom pattern.  
`format`| Defines the accepted format.  
  
Acceptable values are `date-time`, `date`, `time`, `email`, `uuid`, `hostname`, `ipv4`, and `ipv6`.  
Number / Integer| | Field| Description  
---|---  
`enum`| Array of acceptable values for the custom type.  
`minimum`| Minimum acceptable value for the custom type.  
`maximum`| Minimum acceptable value for the custom type.  
`exclusiveMinimum`| Minimum exclusive value for the custom type.  
`exclusiveMaximum`| Maximum exclusive value for the custom type.  
`multipleOf`| Number that is a multiple of a factor.  
Array| | Field| Description  
---|---  
`itemTypes`| List of valid data types (including custom type).  
  
If you specify a custom type, note that:

  * You can include **only one** custom type, for example, `itemTypes: ["CustomType1"]`.
  * You **cannot** include multiple custom types, for example, `itemTypes: ["CustomType1", "CustomType2"]`.

  
`minItems`| Minimum number of items for the array.  
`maxItems`| Maximum number of items for the array.  
`uniqueItems`| Boolean requiring uniqueness of items for the array.  
  
##### **Keyword validations**

The API validates the data types for the various keywords defined in the `config` parameter and gives an error if you pass an invalid value for any field.

See this FAQ for more information on the type-specific keywords supported by RudderStack.

For example, if you pass the `config` object as follows:
    
    
    {
      "type": "string",
      ...
    
      "config": {
        "maxLength": "4",   // String instead of a number.
        "title": 45   // Number instead of a string
      }
    }
    

Then, you will get the below error:
    
    
    {
      "error": "max length must be an integer, title must be a string"
    }
    

#### Properties structure

You must include the `properties` array if your custom type is of the object data type. Note that the `properties` array must contain a list of objects, with each object containing the following details:

Parameter| Description  
---|---  
`id`  
Required| Property ID.  
`required`| Boolean that determines if the property is required or optional.  
  
A sample `properties` array is shown below:
    
    
    "properties": [
      {
        "id": "prop_<id1>",      // Property ID
        "required": true/false      // Determines whether the property is required or optional
      },
      ....
      {
        "id": "prop_<id2>",
        "required": true/false
      }
    ]
    

**Example request**
    
    
     POST /v2/catalog/custom-types HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <token>
    Content-Length: 234
    
    {
        "name": "StringCustomType",
        "type": "string",
        "config": {
            "enum": [
                "ABC",
                "DEF",
                "XYZ"
            ],
            "maxLength": 10,
            "minLength": 4
        }
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/custom-types' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <token>' \
    --data '{
        "name": "StringCustomType",
        "type": "string",
        "config": {
            "enum": [
                "ABC",
                "DEF",
                "XYZ"
            ],
            "maxLength": 10,
            "minLength": 4
        },
    }'
    

**Example response**
    
    
    {
      "config": {
        "enum": [
          "ABC",
          "DEF",
          "XYZ"
        ]
      },
      "rules": {
        "enum": [
          "ABC",
          "DEF",
          "XYZ"
        ],
        "type": [
          "string"
        ]
      },
      "defs": [],
      "itemDefinitions": [],
      "name": "StringCustomType",
      "type": "string",
      "dataType": "string",
      "version": 1,
      "description": "",
      "workspaceId": "2Csl0lSTbuM3daOQB2GcDH8o",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "id": "def_2rvoibDJPpoFKgGvNFAZHKSwWss",
      "createdAt": "2025-01-21T08:43:57.515Z",
      "updatedAt": "2025-01-21T08:43:57.515Z"
    }
    

> ![info](/docs/images/info.svg)
> 
> The `rules` object in the above response corresponds to the internal schema constructed based on the provided configuration and is used for validation.

**Response codes**

Code| Description  
---|---  
200| Custom type is successfully created. RudderStack returns an ID for the newly created custom type in the response.  
400| Bad or invalid request. Some reasons include:  
  


  * Missing `name`.
  * Missing/incorrect `config` object.
  * Missing/incorrect `type`.
  * Missing/incorrect `properties` array (for object type).

  
  
### Update custom type

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)

PUT

/catalog/custom-types/{customTypeId}

> ![info](/docs/images/info.svg)
> 
> Changes to custom types are applied immediately. However, it may take a couple of minutes for all dependent tracking plans to reflect these updates.

**Path parameters**

customTypeId

Required

String

Custom type ID.

**Request body**

> ![warning](/docs/images/warning.svg)
> 
> The request body must not be empty. Otherwise, you will encounter an error.

config

Required

Object

Updated configuration for the custom type. See Config object for more details.

type

Required

String

New data type for the custom type. Acceptable values are `string`, `number`, `integer`, `boolean`, `null`, `array`, and `object`.

properties

Required for object type

Array

Array of properties. See Properties structure for more information on passing this array in the request body.  
  
**Note: This parameter is ignored for non-object data types.**

#### Config object

You must include the `config` object to create a new custom type successfully. You can also pass an empty object to accept any values.

The `config` object can take the below parameters depending on `type` (data type of the custom type) specified in the request body:

Custom data type| Acceptable fields  
---|---  
String| | Field| Description  
---|---  
`enum`| Array of acceptable values for the custom type.  
`minLength`| Number defining the minimum string length for the custom type.  
`maxLength`| Number defining the maximum string length for the custom type.  
`pattern`| Regular expression defining the constraints for the property.  
  
You can also define a custom pattern.  
`format`| Defines the accepted format.  
  
Acceptable values are `date-time`, `date`, `time`, `email`, `uuid`, `hostname`, `ipv4`, and `ipv6`.  
Number / Integer| | Field| Description  
---|---  
`enum`| Array of acceptable values for the custom type.  
`minimum`| Minimum acceptable value for the custom type.  
`maximum`| Minimum acceptable value for the custom type.  
`exclusiveMinimum`| Minimum exclusive value for the custom type.  
`exclusiveMaximum`| Maximum exclusive value for the custom type.  
`multipleOf`| Number that is a multiple of a factor.  
Array| | Field| Description  
---|---  
`itemTypes`| List of valid data types (including custom type).  
  
If you specify a custom type, note that:

  * You can include **only one** custom type, for example, `itemTypes: ["CustomType1"]`.
  * You **cannot** include multiple custom types, for example, `itemTypes: ["CustomType1", "CustomType2"]`.

  
`minItems`| Minimum number of items for the array.  
`maxItems`| Maximum number of items for the array.  
`uniqueItems`| Boolean requiring uniqueness of items for the array.  
  
##### **Keyword validations**

The API validates the data types for the various keywords defined in the `config` parameter and gives an error if you pass an invalid value for any field.

See this FAQ for more information on the type-specific keywords supported by RudderStack.

For example, if you pass the `config` object as follows:
    
    
    {
      "type": "string",
      ...
    
      "config": {
        "maxLength": "4",   // String instead of a number.
        "title": 45   // Number instead of a string
      }
    }
    

Then, you will get the below error:
    
    
    {
      "error": "max length must be an integer, title must be a string"
    }
    

#### Properties structure

You must include the `properties` array if your custom type is of the object data type. Note that the `properties` array must contain a list of objects, with each object containing the following details:

Parameter| Description  
---|---  
`id`  
Required| Property ID.  
`required`| Boolean that determines if the property is required or optional.  
  
A sample `properties` array is shown below:
    
    
    "properties": [
      {
        "id": "prop_<id1>",      // Property ID
        "required": true/false      // Determines whether the property is required or optional
      },
      ....
      {
        "id": "prop_<id2>",
        "required": true/false
      }
    ]
    

**Example request**
    
    
     PUT /v2/catalog/custom-types/def_2s1OUfwmHOEwMdoJFOKoaMr6VWS HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <token>
    Content-Length: 174
    
    {
        "config": {
            "enum": [
                "A",
                "B",
                "C"
            ],
            "maxLength": 15,
            "minLength": 5
        },
        "type": "string"
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/custom-types/def_2s1OUfwmHOEwMdoJFOKoaMr6VWS' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <token>' \
    --data '{
        "config": {
            "enum": [
                "A",
                "B",
                "C"
            ],
            "maxLength": 15,
            "minLength": 5
        },
        "type": "string"
    }'
    

**Example response**
    
    
    {
      "config": {
        "enum": ["A", "B", "C"],
        "maxLength": 15,
        "minLength": 5
      },
      "rules": {
        "enum": ["A", "B", "C"],
        "maxLength": 15,
        "minLength": 5,
        "type": ["string"]
      },
      "defs": [],
      "itemDefinitions": [],
      "id": "def_2s1OUfwmHOEwMdoJFOKoaMr6VWS",
      "name": "StringCustomType",
      "type": "string",
      "dataType": "string",
      "version": 2,
      "description": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "createdAt": "2025-01-23T08:07:11.872Z",
      "updatedBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "updatedAt": "2025-01-23T08:07:11.872Z"
    }
    

> ![info](/docs/images/info.svg)
> 
> The `rules` object in the above response corresponds to the internal schema constructed based on the provided configuration and is used for validation.

**Response codes**

Code| Description  
---|---  
200| Custom type is successfully updated.  
400| Bad or invalid request. Some reasons include:  
  


  * Missing/incorrect `config` object.
  * Missing/incorrect `type`.
  * Missing/incorrect `properties` array (for object type).

  
  
### List all custom types

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)

GET

/catalog/custom-types

**Example request**
    
    
     GET /v2/catalog/custom-types HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <token>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/custom-types' \
    --header 'Authorization: Bearer <token>'
    

**Example response**
    
    
    {
      "data": [{
        "config": {
          "itemTypes": ["integer", "number", "string", "object"]
        },
        "rules": {
          "type": ["array"],
          "items": {
            "type": ["integer", "number", "string", "object"]
          }
        },
        "defs": [],
        "itemDefinitions": [],
        "id": "def_2rvgmGLCrAYftKqBHLSxVU2hGYz",
        "name": "ArrayCustomType",
        "type": "array",
        "dataType": "array",
        "version": 1,
        "description": "",
        "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
        "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
        "createdAt": "2025-01-21T07:38:39.327Z",
        "updatedBy": null,
        "updatedAt": "2025-01-21T07:38:39.327Z",
        "properties": []
      }, 
      .....
      
      {
        "config": {
          "enum": ["ABC", "DEF", "XYZ"]
        },
        "rules": {
          "enum": ["ABC", "DEF", "XYZ"],
          "type": ["string"]
        },
        "defs": [],
        "itemDefinitions": [],
        "id": "def_2p4Sbks9YgDTNL7tQv78L15Vxgp",
        "name": "StringCustomType",
        "type": "string",
        "dataType": "string",
        "version": 2,
        "description": "",
        "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
        "createdBy": "2m9DOlUweDGtsguECIDn7xIz0xc",
        "createdAt": "2024-11-19T13:45:27.391Z",
        "updatedBy": "2m9DOlUweDGtsguECIDn7xIz0xc",
        "updatedAt": "2024-11-19T13:45:27.391Z",
        "properties": []
      }]
    } 
    

**Response codes**

Code| Description  
---|---  
200| Custom types are fetched successfully.  
400| Bad or invalid request.  
  
### Get custom type by ID

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)

GET

/catalog/custom-types/{customTypeId}

**Path parameters**

customTypeId

Required

String

Custom type ID.

**Example request**
    
    
     GET /v2/catalog/custom-types/def_2rvnBxBZumX0CxZeDPqJhsj3suT HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <token>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/custom-types/def_2rvnBxBZumX0CxZeDPqJhsj3suT' \
    --header 'Authorization: Bearer <token>'
    

**Example response**
    
    
    {
      "config": {
        "enum": ["A", "B", "C"],
        "maxLength": 15,
        "minLength": 5
      },
      "rules": {
        "enum": ["A", "B", "C"],
        "maxLength": 15,
        "minLength": 5,
        "type": ["string"]
      },
      "defs": [],
      "itemDefinitions": [],
      "id": "def_2s1OUfwmHOEwMdoJFOKoaMr6VWS",
      "name": "StringCustomType",
      "type": "string",
      "dataType": "string",
      "version": 2,
      "description": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "createdAt": "2025-01-23T08:07:11.872Z",
      "updatedBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "updatedAt": "2025-01-23T08:07:11.872Z",
      "properties": []
    }
    

**Response codes**

Code| Description  
---|---  
200| Custom type fetched successfully.  
400| Bad or invalid request.  
404| Custom type with the specified ID was not found.  
  
### Delete custom type

![Github Badge](https://img.shields.io/badge/Stability-Beta-blue?style=flat)

DELETE

/catalog/custom-types/{customTypeId}

> ![warning](/docs/images/warning.svg)
> 
> You cannot delete a custom type that is referenced by another property.
> 
> For example, if you have a property `propertyname1` of data type `CustomType-1`, then you cannot use this endpoint to delete `CustomType-1`.

**Path parameters**

customTypeId

Required

String

Custom type ID.

**Example request**
    
    
     DELETE /v2/catalog/custom-types/def_2obn0uC4GTrlqoLbb03Bmt0nK9D HTTP/1.1
    Host: api.rudderstack.com
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/custom-types/def_2obn0uC4GTrlqoLbb03Bmt0nK9D'
    

**Example response**
    
    
    {
      "config": {
        "enum": ["ABC", "DEF", "XYZ"],
        "maxLength": 10,
        "minLength": 4
      },
      "rules": {
        "enum": ["ABC", "DEF", "XYZ"],
        "maxLength": 10,
        "minLength": 4,
        "type": ["string"]
      },
      "defs": [],
      "itemDefinitions": [],
      "name": "StringCustomType",
      "type": "string",
      "dataType": "string",
      "version": 1,
      "description": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "createdAt": "2025-01-23T08:18:50.790Z",
      "updatedBy": null,
      "updatedAt": "2025-01-23T08:18:50.790Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Custom type is successfully deleted.  
400| Bad or invalid request.  
404| Custom type with the specified ID was not found.  
  
## FAQ

#### How can I create a property with a schema that validates an array of enums?

The following example highlights how to create a property that is an array of enums:

**Step 1: Create a new custom type of string type containing the enums**

Create a new custom type of `type` **string**. Specify the `config` object containing enums, as shown below:
    
    
    "config": {
      "enum": [
        "iOS",
        "Android"
      ]
    }
    

The corresponding request and response looks as follows:
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/custom-types' \
    --data '{
        "name": "CustomTypeOS", // Replace with the desired name
        "type": "string",
        "config": {
            "enum": [
                "iOS",
                "Android"
            ]
        }
    }'
    
    
    
    {
      "config": {
        "enum": [
          "iOS",
          "Android"
        ]
      },
      "rules": {
        "enum": [
          "iOS",
          "Android"
        ],
        "type": [
          "string"
        ]
      },
      "defs": [],
      "itemDefinitions": [],
      "name": "CustomTypeOS",
      "type": "string",
      "dataType": "string",
      "version": 1,
      "description": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "id": "def_2s24AqVRImBgtDgrUxgZPdwULUc",
      "createdAt": "2025-01-23T13:49:54.884Z",
      "updatedAt": "2025-01-23T13:49:54.884Z"
    }
    

**Step 2: Create a new array custom type**

Create a new custom type of `type` **array**. Specify the `config` object with `itemTypes` set to an array of `CustomTypeOS` (created in Step 1), as shown below:
    
    
    "config": {
      "itemTypes": [
        "CustomTypeOS"
      ]
    }
    

The corresponding request and response looks as follows:
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/custom-types' \
    --data '{
        "name": "CustomTypeArray", // Replace with the desired name
        "type": "array",
        "config": {
            "itemTypes": [
                "CustomTypeOS"
            ]
        }
    }'
    
    
    
    {
      "config": {
        "itemTypes": [
          "CustomTypeOS"
        ]
      },
      "rules": {
        "type": [
          "array"
        ],
        "items": {
          "$ref": "#/$defs/CustomTypeOS"
        }
      },
      "defs": [],
      "itemDefinitions": [
        "CustomTypeOS"
      ],
      "name": "CustomTypeArray",
      "type": "array",
      "dataType": "array",
      "version": 1,
      "description": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "id": "def_2s24KxYCyq0zXOW5Ms3A8BdTejk",
      "createdAt": "2025-01-23T13:51:15.164Z",
      "updatedAt": "2025-01-23T13:51:15.164Z"
    }
    

**Step 3: Create a new property of custom array type**

Create a new property and set the data type to the custom array type created in the above step. The request body looks as follows:
    
    
    {
      "name": "NewPropertyOS", // Replace with the desired name
      "description": "Sample property of array custom type",
      "type": "CustomTypeArray",
      "propConfig": {}
    }
    

The corresponding request and response looks as follows:
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/properties' \
    --data '{
        "name": "NewPropertyOS",
        "description": "Sample property of array custom type",
        "type": "CustomTypeArray",
        "propConfig":{}
    }'
    
    
    
    {
      "propConfig": {
        "$ref": "#/$defs/CustomTypeArray"
      },
      "name": "NewPropertyOS",
      "description": "Sample property of array custom type",
      "type": "CustomTypeArray",
      "arrayItemTypes": "",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "definitionId": "def_2s24KxYCyq0zXOW5Ms3A8BdTejk",
      "itemDefinitionId": null,
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "id": "prop_2s24hYtHCj4Egn1PTFLDnN6cQ2C",
      "createdAt": "2025-01-23T13:54:15.913Z",
      "updatedAt": "2025-01-23T13:54:15.913Z"
    }
    

The above property `NewPropertyOS` is of type `CustomTypeArray`, where:

  * `CustomTypeArray` is an array of `CustomTypeOS` custom type.
  * `CustomTypeOS` is a string custom type containing enums (`iOS` and `Android`).


**Alternative Step 3: Create array property and specify string custom type in property configuration**

You can also create a property of array type and specify the string custom type (containing the enums) within the `propConfig` object, as shown:
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/properties' \
    --data '{
        "name": "NewPropertyOS",
        "description": "Sample property of array custom type",
        "type": "array",
        "propConfig":{
            "itemTypes": ["CustomTypeOS"]
        }
    }'
    
    
    
    {
      "propConfig": {
        "itemTypes": [
          "CustomTypeOS"
        ]
      },
      "name": "NewPropertyOS",
      "description": "Sample property of array custom type",
      "type": "array",
      "arrayItemTypes": "CustomTypeOS",
      "workspaceId": "29fJnntLeqmZEj0MBIFOCi6jRce",
      "definitionId": null,
      "itemDefinitionId": "def_2s24AqVRImBgtDgrUxgZPdwULUc",
      "createdBy": "1sW1rW9Q03EobQOuJekQKnrjRem",
      "id": "prop_2s2572eInNFWWW8S1G3hPurQhen",
      "createdAt": "2025-01-23T13:57:37.289Z",
      "updatedAt": "2025-01-23T13:57:37.289Z"
    }
    

#### While updating a property in the dashboard, I get errors like “invalid properties: minLength” but this rule is not visible in the `rules` section. How do I update such a property?

To fix issues related to updating properties where you get errors related to advanced rules but no such rules are present:

**Option 1: Update property in the RudderStack dashboard**

  1. Locate the property in the RudderStack dashboard.
  2. Clear the **Data type**.
  3. Add the required data type again.

[![Update property in RudderStack dashboard](/docs/images/api/update-property.webp)](</docs/images/api/update-property.webp>)

**Option 2: Use the Data Catalog API**

You can also leverage the [Update property](<https://www.rudderstack.com/docs/api/data-catalog-api/data-catalog/#update-property>) endpoint of the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>) to update the property with the required data type and property rules.

#### What are the different type-specific keywords supported by RudderStack?

RudderStack supports the following keywords for the string data type:

  * `minLength`
  * `maxLength`
  * `pattern`
  * `format`


See the [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/#strings>) guide for more information on these keywords.

RudderStack supports the following keywords for the integer and number data type:

  * `multipleOf`
  * `minimum`
  * `maximum`
  * `exclusiveMinimum`
  * `exclusiveMaximum`


See the [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/#integers-and-numbers>) guide for more information on these keywords.

RudderStack supports the following keywords for the array data type:

  * `minItems`
  * `maxItems`
  * `uniqueItems`


See the [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/#arrays>) guide for more information on these keywords.