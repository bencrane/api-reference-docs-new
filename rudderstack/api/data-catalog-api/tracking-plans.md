# Catalog API Endpoints for Tracking Plans

Use the Data Catalog API to create and manage your Tracking Plans programmatically.

Available Plans

  * growth
  * enterprise


* * *

  *  __24 minute read

  * 


This guide provides a reference for the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>) endpoints to:

  * Manage Tracking Plans
  * Manage Tracking Plan events
  * Manage Tracking Plan-source connections


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
    

## Manage Tracking Plans

This section covers the API endpoints for creating and managing your [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>).

### Create Tracking Plan

POST

/catalog/tracking-plans

**Request body**

name

Required

String

Tracking Plan name.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.


description

Optional

String

Tracking Plan description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

**Example request**
    
    
     POST /v2/catalog/tracking-plans HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 83
    
    {
        "name": "Product Ordered Plan",
        "description": "Tracking Plan for users placing an order for the product."
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "name": "Product Ordered Plan",
        "description": "Tracking Plan for users placing an order for the product."
    }'
    

**Example response**
    
    
    {
      "id": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
      "name": "Product Ordered Plan",
      "description": "Tracking Plan for users placing an order for the product.",
      "version": 1,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "creationType": "Data catalog API",
      "createdAt": "2024-05-22T10:34:03.016Z",
      "updatedAt": "2024-05-22T10:34:03.016Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Tracking Plan is successfully created. RudderStack also returns an ID for the newly created Tracking Plan.  
400| Bad or invalid request.  
  
### List all Tracking Plans

GET

/catalog/tracking-plans

**Example request**
    
    
     GET /v2/catalog/tracking-plans HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "trackingPlans": [{
          "id": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
          "name": "Product Ordered Plan",
          "description": "Tracking Plan for users placing an order for the product.",
          "version": 1,
          "createdAt": "2024-05-22T13:07:18.617Z",
          "updatedAt": "2024-05-22T13:07:18.617Z",
          "creationType": "Data catalog API",
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e"
        },
        {
          "id": "tp_2rKxjFu6R1qot19aWhTW7W7Ojew",
          "name": "Order Completed Plan",
          "description": "Tracking Plan for users completing an order for the product.",
          "version": 4,
          "createdAt": "2024-01-30T15:41:14.446Z",
          "updatedAt": "2024-02-01T08:59:15.095Z",
          "creationType": "Event Audit API",
          "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e"
        }
      ]
    }
    

**Response codes**

Code| Description  
---|---  
200| List of all Tracking Plans in the associated workspace.  
  
### Get Tracking Plan by ID

GET

/catalog/tracking-plans/{trackingPlanId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Query parameters**

version

Optional

String

Tracking Plan version. Note that it must be a number.

rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

**Example request**
    
    
     GET /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T?rebuildSchemas=false' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "id": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
      "name": "Product Ordered Plan",
      "description": "Tracking Plan for users placing an order for the product.",
      "version": 1,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "creationType": "Data catalog API",
      "createdAt": "2024-05-22T13:07:18.617Z",
      "updatedAt": "2024-05-22T13:07:18.617Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Tracking Plan retrieved successfully.  
404| Tracking Plan not found for the specified ID.  
  
### Update Tracking Plan

PUT

/catalog/tracking-plans/{trackingPlanId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Request body**

To update the Tracking Plan, **at least one** of the following parameters is required:

name

String

Tracking Plan name.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.


description

String

Tracking Plan description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

**Example request**
    
    
     PUT /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 87
    
    {
        "name": "New Product Ordered Plan",
        "description": "Updated Tracking Plan for users placing an order for the product."
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "name": "New Product Ordered Plan",
        "description": "Updated Tracking Plan for users placing an order for the product."
    }'
    

**Example response**
    
    
    {
      "id": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
      "name": "New Product Ordered Plan",
      "description": "Updated Tracking Plan for users placing an order for the product.",
      "version": 2,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "creationType": "Data catalog API",
      "createdAt": "2024-05-22T10:34:03.016Z",
      "updatedAt": "2024-05-22T10:36:49.252Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Tracking Plan is updated successfully.  
400| Bad or invalid request.  
  
### Delete Tracking Plan

> ![danger](/docs/images/danger.svg)
> 
> Deleted Tracking Plans cannot be recovered or restored.

DELETE

/catalog/tracking-plans/{trackingPlanId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Example request**
    
    
     DELETE /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "name": "New Product Ordered Plan",
      "version": 1,
      "description": "Updated Tracking Plan for users placing an order for the product.",
      "creationType": "Data catalog API",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": null,
      "createdAt": "2024-05-22T13:41:33.057Z",
      "updatedAt": "2024-05-22T13:41:33.057Z",
      "events": []
    }
    

**Response codes**

Code| Description  
---|---  
200| Tracking Plan is deleted successfully.  
400| Bad or invalid request.  
  
## Manage Tracking Plan events

This section covers the API endpoints for upserting and managing events in your Tracking Plans.

> ![info](/docs/images/info.svg)
> 
> The Data Catalog API creates the events and properties in the data catalog only if they do not exist already.

### Upsert event to Tracking Plan

> ![warning](/docs/images/warning.svg)
> 
> While upserting an event to a Tracking Plan, make sure the schema of the properties adheres to the [advanced rules](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#advanced-rules>) set for those properties in the data catalog. Otherwise, RudderStack will **drop** the schema and give the below error:
> 
> “Property with name [${prop.name}] and type [${prop.type}] already exists with different advanced keywords.”
> 
> If you get this error, you can update the existing catalog property by adding required advanced rules and try again.

#### Upsert event with rules

> ![danger](/docs/images/danger.svg)
> 
> This endpoint will be deprecated soon.

PATCH

/catalog/tracking-plans/{trackingPlanId}/events

> ![info](/docs/images/info.svg)
> 
> The changes are queued for processing and typically reflect within a few minutes.

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Query parameters**

rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

**Request body**

name

Required

String

Name of the event to be upserted.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.
  * For non-`track` events, the name should be an empty string.


description

Optional

String

Event description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

eventType

Required

String

Type of event to be upserted.  
  
Note that:

  * Once set, the event type **cannot** be updated later.
  * Allowed event types are `track`, `identify`, `group`, `page`, and `screen`.


categoryId

Optional

String

Category ID of the event. It should be a valid, non-empty string.

rules

Required

Object

[JSON schema](<https://rudderstack.com/docs/api/data-catalog-api/json-schema/>) against which RudderStack validates the event. The event rules **cannot** be empty.  
  
**Note** : The keywords defined for a property in the `rules` parameter are the same as the [advanced rules](<https://www.rudderstack.com/docs/data-governance/data-catalog/#advanced-rules>) defined for a property in the dashboard.

identitySection

Optional

String

Section from which RudderStack extracts the event properties. See [Event structure for Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#event-structure-for-tracking-plan-validation>) for more information.

**Example request**
    
    
     PATCH /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 955
    
    {
      "name": "Product Viewed",
      "eventType": "track",
      "description": "User viewed a product.",
      "categoryId": null,
      "rules": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
          "properties": {
            "type": "object",
            "required": [
              "amount"
            ],
            "additionalProperties": false,
            "properties": {
              "amount": {
                "type": [
                  "number"
                ]
              },
            }
          }
        }
      }
    }
    
    
    
    curl --location --request PATCH 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events?rebuildSchemas=false' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
      "name": "Product Viewed",
      "eventType": "track",
      "description": "User viewed a product.",
      "categoryId": null,
      "rules": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
          "properties": {
            "type": "object",
            "required": [
              "amount"
            ],
            "additionalProperties": false,
            "properties": {
              "amount": {
                "type": [
                  "number"
                ]
              },
            }
          }
        }
      }
    }'
    

**Example response**
    
    
    {
      "id": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
      "name": "Product Viewed Plan",
      "version": 3,
      "description": "User viewed a product.",
      "creationType": "Data catalog API",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdAt": "2024-05-22T10:34:03.016Z",
      "updatedAt": "2024-05-22T11:01:24.706Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is upserted to the Tracking Plan successfully. The API gives the updated Tracking Plan information as a response.  
400| Bad or invalid request.  
  
#### Upsert event with properties

This endpoint has the same functionality as Upsert event with rules except that this request operates on the event properties rather than rules.

POST

/catalog/tracking-plans/{trackingPlanId}/events

> ![info](/docs/images/info.svg)
> 
> The changes are queued for processing and typically reflect within a few minutes.

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Query parameters**

rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

**Request body**

name

Required

String

Name of the event to be upserted.  
  
Note that:

  * The name must be between 3 and 65 characters and should start with a letter.
  * It must contain only letters, numbers, underscores, commas, spaces, dashes, and dots.
  * For non-`track` events, the name should be an empty string.


description

Optional

String

Event description.  
  
Note that the description must be between 3 and 2000 characters and should start with a letter.

eventType

Required

String

Type of event to be upserted.  
  
Note that:

  * Once set, the event type **cannot** be updated later.
  * Allowed event types are `track`, `identify`, `group`, `page`, and `screen`.


categoryId

Optional

String

Category ID of the event. It should be a valid, non-empty string.

properties

Required

Array

The event properties against which RudderStack validates the event. It **cannot** be empty.  
  
See **Properties structure** section below for more information on this parameter.

identitySection

Optional

String

Section from which RudderStack extracts the event properties. See [Event structure for Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#event-structure-for-tracking-plan-validation>) for more information.

**Properties structure**

name

Required

String

Property name.  
  
Note that:

  * The name must be of at least one character and should start with a letter.
  * It must contain only letters, numbers, underscores, and spaces.


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

Required

Object

Advanced rules for the property. See [JSON Schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/>) for the complete list of supported keywords.

required

Optional

Boolean

Determines whether the property must be present in the event.

additionalProperties

Optional

Boolean

This parameter is only applicable for arrays and objects if nested properties are present. It determines if additional properties (apart from the provided nested properties) should be allowed.

metadata

Optional

Object

Additional [metadata](<https://rudderstack.com/docs/api/data-catalog-api/json-schema/#metadata>) for the property containing generic keywords.

properties

Required only for nested properties

Array

Details of the nested properties.

**Example request**
    
    
     POST /v2/catalog/tracking-plans/tp_2u9kdo9I3y0ou8O722ZTc8SOgMk/events?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 955
    {
        "description": "Triggered when user views a product.",
        "eventType": "track",
        "name": "Product Viewed",
        "properties": [
            {
                "name": "product_details",
                "description": "Product details",
                "type": "object",
                "propConfig": {},
                "required": false,
                "additionalProperties": true,
                "metadata": {},
                "properties": [
                    {
                        "name": "id",
                        "description": "Product ID",
                        "type": "string",
                        "propConfig": {
                            "minLength": 1
                        },
                        "required": true,
                        "additionalProperties": true,
                        "metadata": {}
                    }
                ]
            },
            {
                "name": "amount",
                "description": "Product amount",
                "type": "number, string",
                "propConfig": {},
                "required": true,
                "additionalProperties": true,
                "metadata": {},
                "properties": []
            }
        ]
    }
    
    
    
    curl --location --request POST 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_2u9kdo9I3y0ou8O722ZTc8SOgMk/events?rebuildSchemas=false' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "description": "Triggered when user views a product.",
        "eventType": "track",
        "name": "Product Viewed",
        "properties": [
            {
                "name": "product_details",
                "description": "Product details",
                "type": "object",
                "propConfig": {},
                "required": false,
                "additionalProperties": true,
                "metadata": {},
                "properties": [
                    {
                        "name": "id",
                        "description": "Product ID",
                        "type": "string",
                        "propConfig": {
                            "minLength": 1
                        },
                        "required": true,
                        "additionalProperties": true,
                        "metadata": {}
                    }
                ]
            },
            {
                "name": "amount",
                "description": "Product amount",
                "type": "number, string",
                "propConfig": {},
                "required": true,
                "additionalProperties": true,
                "metadata": {},
                "properties": []
            }
        ]
    }'
    

**Example response**
    
    
    {
      "id": "tp_2u9kdo9I3y0ou8O722ZTc8SOgMk",
      "name": "Product Viewed Plan",
      "version": 3,
      "description": "User viewed a product.",
      "creationType": "Data catalog API",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdAt": "2024-05-22T10:34:03.016Z",
      "updatedAt": "2024-05-22T11:01:24.706Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is upserted to the Tracking Plan successfully. The API gives the updated Tracking Plan information as a response.  
400| Bad or invalid request.  
  
#### Upsert event with identifiers

This endpoint has the same functionality as Upsert event with properties except that this request only requires the identifiers (Tracking Plan ID, event ID, and property IDs).

PUT

/catalog/tracking-plans/{trackingPlanId}/events

> ![info](/docs/images/info.svg)
> 
> The changes are queued for processing and typically reflect within a few minutes.

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Query parameters**

rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

**Request body**

id

Required

String

Event ID.  
  
RudderStack automatically fetches the event name, description, type, and other event details from this ID.

properties

Required

Array

The event properties against which RudderStack validates the event. It **cannot** be empty.  
  
See **Properties structure** section below for more information on this parameter.

**Properties structure**

id

Required

String

Property ID.  
  
RudderStack automatically fetches the property name, description, type, and other details from this ID.

required

Optional

Boolean

Determines whether the property must be present in the event.

additionalProperties

Optional

Boolean

This parameter is only applicable for arrays and objects if nested properties are present. It determines if additional properties (apart from the provided nested properties) should be allowed.

metadata

Optional

Object

Additional [metadata](<https://rudderstack.com/docs/api/data-catalog-api/json-schema/#metadata>) for the property containing generic keywords.

properties

Required only for nested properties

Array

Details of the nested properties.

**Example request**
    
    
     PUT /v2/catalog/tracking-plans/tp_2u9kdo9I3y0ou8O722ZTc8SOgMk/events?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 955
    
    {
        "id": "ev_2govsgWGzvmkZqiHESDpdHqkbsI", 
        "properties": [
            {
                "id": "prop_2bc0rhFC4oOKa8VCfAhMCkN31rf",
                "required": true,
                "additionalProperties": true,
                "metadata": {},
                "properties": [
                    {
                        "id": "prop_2rQucgLjgHWYQQIst2iu5yIjWKh",
                        "required": true,
                        "additionalProperties": true,
                        "metadata": {}
                    }
                ]
            },
            {
                "id": "prop_2bdWBUck8T5kqMoWnwTyn4h5reo",
                "required": false,
                "additionalProperties": false,
                "metadata": {},
                "properties": []
            }
        ]
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_2u9kdo9I3y0ou8O722ZTc8SOgMk/events?rebuildSchemas=false' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "id": "ev_2govsgWGzvmkZqiHESDpdHqkbsI", 
        "properties": [
            {
                "id": "prop_2bc0rhFC4oOKa8VCfAhMCkN31rf",
                "required": true,
                "additionalProperties": true,
                "metadata": {},
                "properties": [
                    {
                        "id": "prop_2rQucgLjgHWYQQIst2iu5yIjWKh",
                        "required": true,
                        "additionalProperties": true,
                        "metadata": {}
                    }
                ]
            },
            {
                "id": "prop_2bdWBUck8T5kqMoWnwTyn4h5reo",
                "required": false,
                "additionalProperties": false,
                "metadata": {},
                "properties": []
            }
        ]
    }'
    

**Example response**
    
    
    {
      "id": "tp_2u9kdo9I3y0ou8O722ZTc8SOgMk",
      "name": "Product Viewed Plan",
      "version": 3,
      "description": "User viewed a product.",
      "creationType": "Data catalog API",
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdAt": "2024-05-22T10:34:03.016Z",
      "updatedAt": "2024-05-22T11:01:24.706Z"
    }
    

**Response codes**

Code| Description  
---|---  
200| Event is upserted to the Tracking Plan successfully. The API gives the updated Tracking Plan information as a response.  
400| Bad or invalid request.  
  
#### Property keyword validations

While upserting event with properties to a Tracking Plan, the API validates the data types for the various keywords defined in the `propConfig` and [`metadata`](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/#metadata>) parameters, and gives an error if you pass an invalid value.

See this FAQ for more information on the type-specific keywords supported by RudderStack.

For example, if you pass the `propConfig` and `metadata` objects as follows:
    
    
    {
      "type": "string",
      ...
    
      "metadata": {
        "title": 45   // Number instead of a string
      },
    
      "propConfig": {
        "maxLength": "4",   // String instead of a number.
      }
    }
    

Then, you will get the below errors:
    
    
    {
      "error": "max length must be an integer, title must be a string"
    }
    
    {
      "error": "schema is invalid: data/properties/properties/properties/<property_name>/title must be string"
    }
    

### List all events in Tracking Plan

GET

/catalog/tracking-plans/{trackingPlanId}/events

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Query parameters**

rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

page

Optional

Number

In a paginated view, all the response entries are divided into pages. Use this field to specify which page of results to return. Default value is **1**.  
  
**Note** :  
  


  * This parameter must be a positive integer.
  * The API returns a maximum of 50 pages.


**Example request**
    
    
     GET /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events?rebuildSchemas=false' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "data": [{
        "id": "ev_2gotMKGuOtdDY4XbSdKjkwk4qc2",
        "name": "Product Viewed",
        "description": "User viewed a product.",
        "eventType": "track",
        "categoryId": null,
        "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
        "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
        "updatedBy": null,
        "createdAt": "2024-05-22T11:01:24.706Z",
        "updatedAt": "2024-05-22T11:01:24.706Z",
        "identitySection": "properties",
        "additionalProperties": true,
      }],
      "total": 1,
      "currentPage": 1,
      "pageSize": 50
    }
    

**Response codes**

Code| Description  
---|---  
200| All the events in the Tracking Plan are fetched successfully.  
  
The response body contains the below fields:

Field| Type| Description  
---|---|---  
`data`| Array| Contains all the events in the Tracking Plan.  
`total`| Number| Total number of entries in the response.  
`currentPage`| Number| Current page number being viewed (starts from 1).  
`pageSize`| Number| Maximum number of items displayed per page.  
  
### Get Tracking Plan event by ID

GET

/catalog/tracking-plans/{trackingPlanId}/events/{eventId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

eventId

Required

String

Event ID.

**Query parameters**

format

Optional

String

Fetches the response in the specified format. Acceptable values are:  
  


  * `schema`: Response is shown with the `rules` object. This is the default `format` value.
  * `properties`: Response is shown with the `properties` object.


rebuildSchemas

Optional

Boolean

When set to `true`, RudderStack returns the latest Tracking Plan data by rebuilding all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan will be rejected.  
  
When set to `false`, RudderStack returns cached data immediately, which may be slightly out of date. The data will eventually be refreshed in the background. This option provides faster response times and is recommended for read-heavy operations.  
  
**Default value** : `true`.

**Example request**
    
    
     GET /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events/ev_2gotMKGuOtdDY4XbSdKjkwk4qc2?rebuildSchemas=false HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events/ev_2gotMKGuOtdDY4XbSdKjkwk4qc2?rebuildSchemas=false' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**

The response when you add `format=schema` as the query parameter is shown:
    
    
    {
      "id": "ev_2gotMKGuOtdDY4XbSdKjkwk4qc2",
      "name": "Product Viewed",
      "description": "User viewed a product.",
      "eventType": "track",
      "categoryId": null,
      "workspaceId": "1hitizAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": null,
      "createdAt": "2024-05-22T11:01:24.706Z",
      "updatedAt": "2024-05-22T11:01:24.706Z",
      "identitySection": "properties",
      "rules": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
          "properties": {
            "type": "object",
            "required": [
              "amount"
            ],
            "additionalProperties": false,
            "properties": {
              "amount": {
                "type": [
                  "number"
                ]
              },
            }
          }
        }
      }
    }
    

The response when you add `format=properties` as the query parameter is shown:
    
    
    {
      "id": "ev_2gotMKGuOtdDY4XbSdKjkwk4qc2",
      "name": "Product Viewed",
      "description": "User viewed a product.",
      "eventType": "track",
      "categoryId": null,
      "workspaceId": "1zitShAoFT91DD6rfFhBjiTex3e",
      "createdBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "updatedBy": "2KDKycoVHAOLttVvzBiqw12O3Hr",
      "createdAt": "2024-05-22T11:22:32.710Z",
      "updatedAt": "2025-03-11T04:44:43.633Z",
      "identitySection": "properties",
      "additionalProperties": false,
      "properties": [{
        "id": "prop_2bc0rhFC4oOKa8VCfAhMCkN31rf",
        "name": "amount",
        "description": "Product amount",
        "type": "number, string",
        "propConfig": {},
        "required": true,
        "additionalProperties": false,
        "metadata": {},
        "properties": []
      }]
    }
    

**Response codes**

Code| Description  
---|---  
200| Event specified by the ID is fetched successfully.  
404| Tracking Plan event not found for the specified ID.  
  
### Delete event from Tracking Plan

DELETE

/catalog/tracking-plans/{trackingPlanId}/events/{eventId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

eventId

Required

String

Event ID.

**Example request**
    
    
     DELETE /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events/ev_2gotMKGuOtdDY4XbSdKjkwk4qc2 HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/events/ev_2gotMKGuOtdDY4XbSdKjkwk4qc2' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Response codes**

Code| Description  
---|---  
204| Event is deleted from Tracking Plan successfully.  
400| Bad or invalid request.  
  
## Manage Tracking Plan connections

This section covers the API endpoints for managing the connections between your Tracking Plans and sources.

### Add new connection

POST

/catalog/tracking-plans/{trackingPlanId}/sources/{sourceId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

sourceId

Required

String

Source ID.

**Request body**

> ![warning](/docs/images/warning.svg)
> 
> The request body must not be empty. Otherwise, you will encounter an error.

config

Required

Object

Tracking Plan configuration for the source. See **Config object structure** below for more information.

**Config object structure**

The `config` object provided in the request body contains the source-specific Tracking Plan settings for validating the individual events. A sample object is shown below:
    
    
    {
      "config": {
        "page": {
          "unplannedProperties": "forward",  // or "drop"
          "anyOtherViolation": "forward",  // or "drop"
          "propagateValidationErrors": "true",  // or "false"
        },
        "group": {
          "unplannedProperties": "forward",
          "anyOtherViolation": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "allowUnplannedEvents": "true",
          "unplannedProperties": "forward",
          "anyOtherViolation": "forward",
          "propagateValidationErrors": "true",  // or "false"
        },
        "global": {
          "allowUnplannedEvents": "true",
          "unplannedProperties": "forward",
          "anyOtherViolation": "forward",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "unplannedProperties": "forward",
          "anyOtherViolation": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "unplannedProperties": "forward",
          "anyOtherViolation": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    

The event-level settings that you can define within the `config` object are described below. See [Source-specific Tracking Plan settings](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#source-specific-settings>) for more information:

Field| Description  
---|---  
`allowUnplannedEvents`| **Applicable for`track` object only.**  
  
Boolean that determines if RudderStack should drop all events that do not match the predefined event names in the Tracking Plan.  
`unplannedProperties`| Acceptable values are `forward` and `drop`.  
  
Determines if RudderStack should forward or drop events that contain properties not matching the list of predefined properties for the specific event.  
`anyOtherViolation`| Acceptable values are `forward` and `drop`.  
  
Determines if RudderStack should forward or drop events with any other violations that include **Type Mismatch** , **Required Fields Missing** , and others outlined in the [Violation types](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) section.  
`propagateValidationErrors`| Boolean that determines if RudderStack should capture the validation errors in the event’s `context` object and send them downstream (user transformations and destinations).  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You need not provide the Tracking Plan settings for all events. For example, you can include only the `track` and `global` objects within `config`. However, note that you **must not** provide a blank event object. If included, you must define at least one setting for that event.
>   * RudderStack uses the default settings for the events that you do not specify explicitly and validates them accordingly.
> 


**Example request**
    
    
     POST /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iNTR HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 1125
    
    {
      "config": {
        "page": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "group": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "true",
          "propagateValidationErrors": "true"
        },
        "global": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "false",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iNTR' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "config": {
            "page": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "group": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "track": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "allowUnplannedEvents": "true",
                "propagateValidationErrors": "true"
            },
            "global": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "allowUnplannedEvents": "false",
                "propagateValidationErrors": "true"
            },
            "screen": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "identify": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            }
        }
    }'
    

**Example response**
    
    
    {
      "sourceId": "2nk0qVvmxE79uIwsKebgVH4iNTR",
      "trackingPlanId": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
      "config": {
        "page": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "group": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "true",
          "propagateValidationErrors": "true"
        },
        "global": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "false",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    

**Response codes**

Code| Description  
---|---  
200| Connection created successfully.  
400| 

  * Invalid Request
  * Empty or incorrect `config` object.
  * Source already connected to Tracking Plan.

  
  
### Update Tracking Plan configuration

PUT

/catalog/tracking-plans/{trackingPlanId}/sources/{sourceId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

sourceId

Required

String

Source ID.

**Request body**

> ![warning](/docs/images/warning.svg)
> 
> The request body must not be empty. Otherwise, you will encounter an error.

config

Required

Object

Tracking Plan configuration for the source. See **Config object structure** below for more information.

**Config object structure**

The `config` object provided in the request body contains the source-specific Tracking Plan settings for validating the individual events. A sample object is shown below:
    
    
    {
      "config": {
        "page": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "group": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "true",
          "propagateValidationErrors": "true"
        },
        "global": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "false",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    

The event-level settings that you can define within the `config` object are described below. See [Source-specific Tracking Plan settings](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#source-specific-settings>) for more information:

Field| Description  
---|---  
`allowUnplannedEvents`| **Applicable for`track` object only.**  
  
Boolean that determines if RudderStack should drop all events that do not match the predefined event names in the Tracking Plan.  
`unplannedProperties`| Acceptable values are `forward` and `drop`.  
  
Determines if RudderStack should forward or drop events that contain properties not matching the list of predefined properties for the specific event.  
`anyOtherViolation`| Acceptable values are `forward` and `drop`.  
  
Determines if RudderStack should forward or drop events with any other violations that include **Type Mismatch** , **Required Fields Missing** , and others outlined in the [Violation types](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>) section.  
`propagateValidationErrors`| Boolean that determines if RudderStack should capture the validation errors in the event’s `context` object and send them downstream (user transformations and destinations).  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You need not provide the Tracking Plan settings for all events. For example, you can include only the `track` and `global` objects within `config`. However, note that you **must not** provide a blank event object. If included, you must define at least one setting for that event.
>   * RudderStack uses the default settings for the events that you do not specify explicitly and validates them accordingly.
> 


**Example request**
    
    
     PUT /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iNTR HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    Content-Length: 1125
    
    {
      "config": {
        "page": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "group": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "true",
          "propagateValidationErrors": "true"
        },
        "global": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "false",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    
    
    
    curl --location --request PUT 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iNTR' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>' \
    --data '{
        "config": {
            "page": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "group": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "track": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "allowUnplannedEvents": "true",
                "propagateValidationErrors": "true"
            },
            "global": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "allowUnplannedEvents": "false",
                "propagateValidationErrors": "true"
            },
            "screen": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            },
            "identify": {
                "anyOtherViolation": "forward",
                "unplannedProperties": "forward",
                "propagateValidationErrors": "true"
            }
        }
    }'
    

**Example response**
    
    
    {
      "config": {
        "page": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "group": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "track": {
          "anyOtherViolation": "drop",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "true",
          "propagateValidationErrors": "true"
        },
        "global": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "allowUnplannedEvents": "false",
          "propagateValidationErrors": "true"
        },
        "screen": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        },
        "identify": {
          "anyOtherViolation": "forward",
          "unplannedProperties": "forward",
          "propagateValidationErrors": "true"
        }
      }
    }
    

**Response codes**

Code| Description  
---|---  
200| Configuration updated successfully.  
400| 

  * Invalid Request
  * Empty or incorrect `config` object.
  * Source is not connected to Tracking Plan.

  
  
### List all sources connected to Tracking Plan

GET

/catalog/tracking-plans/{trackingPlanId}/sources

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

**Example request**
    
    
     GET /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Example response**
    
    
    {
      "connections": [{
          "sourceId": "2nk0qVvmxE79uIwsKebgVH4iNTR",
          "trackingPlanId": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
          "config": {
            "track": {
              "anyOtherViolation": "forward",
              "unplannedProperties": "forward",
              "allowUnplannedEvents": "true",
              "propagateValidationErrors": "true"
            },
            "global": {
              "anyOtherViolation": "forward",
              "unplannedProperties": "forward",
              "allowUnplannedEvents": "false",
              "propagateValidationErrors": "true"
            },
            "identify": {
              "anyOtherViolation": "forward",
              "unplannedProperties": "forward",
              "propagateValidationErrors": "true"
            }
          }
        },
        {
          "sourceId": "2rL1XeHCG8P8OrMHnHx4WjMjuTo",
          "trackingPlanId": "tp_5gopz6tfKxAjpS4TjuqVIeTdm7T",
          "config": {
            "track": {
              "anyOtherViolation": "drop",
              "unplannedProperties": "forward",
              "allowUnplannedEvents": "true",
              "propagateValidationErrors": "true"
            },
            "global": {
              "anyOtherViolation": "forward",
              "unplannedProperties": "forward",
              "allowUnplannedEvents": "false",
              "propagateValidationErrors": "true"
            }
          }
        }
      ]
    }
    

**Response codes**

Code| Description  
---|---  
200| All the sources connected to a Tracking Plan fetched successfully.  
  
### Delete source connection

DELETE

/catalog/tracking-plans/{trackingPlanId}/sources/{sourceId}

**Path parameters**

trackingPlanId

Required

String

Tracking Plan ID.

sourceId

Required

String

Source ID.

**Example request**
    
    
     DELETE /v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iNTR HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/v2/catalog/tracking-plans/tp_5gopz6tfKxAjpS4TjuqVIeTdm7T/sources/2nk0qVvmxE79uIwsKebgVH4iJNR' \
    --header 'Authorization: Bearer <SERVICE_ACCESS_TOKEN>'
    

**Response codes**

Code| Description  
---|---  
204| Source disconnected from Tracking Plan successfully.  
400| 

  * Source already disconnected from Tracking Plan.
  * Invalid source ID.

  
  
## Supported type-specific keywords

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

## FAQ

#### How do I handle concurrent update failures when working with the Tracking Plan endpoints?

When you use endpoints that support the `rebuildSchemas` query parameter with its default value (`true`), RudderStack rebuilds all schema rules before responding. During this operation, any concurrent updates to the Tracking Plan are rejected, which can cause your requests to fail.

If you encounter concurrent update failures, set the `rebuildSchemas` query parameter to `false`. This option:

  * Returns cached data immediately, which may be slightly out of date
  * Allows concurrent updates to proceed without rejection
  * Provides faster response times


`rebuildSchemas=false` is recommended for read-heavy operations — the data will eventually be refreshed in the background, so you still get updated information eventually.