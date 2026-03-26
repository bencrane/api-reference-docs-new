# Audit Logs API

Access Audit Logs programmatically using the Audit Logs API.

Available Plans

  * enterprise


* * *

  *  __3 minute read

  * 


This guide provides a detailed reference for the RudderStack Audit Logs API.

## Overview

The Audit Logs API lets you programmatically access Audit Logs for running your security audits. You can use the API to:

  * Access all existing Audit Logs
  * Access the Audit Logs generated after the last access
  * Filter Audit Logs based on workspaces, date, etc.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** You can also view [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) in the RudderStack dashboard.

## Prerequisites

  * Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can access the Audit Logs API
  * Generate an [organization-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#organization-sat>) in the RudderStack dashboard to authenticate the API


#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), see [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for generating the organization-level Service Access Token.

## Authentication

The Audit Logs API uses [Bearer authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the following format:
    
    
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Access Audit Logs

You can access Audit Logs using the below endpoint:

GET

/v2/audit-logs

**Query parameters** :

per_page

optional, default is `100`

integer

Indicates the number of items per page. You can set its value anywhere between the range of 1 to 100.

workspace_id

optional

string

Fetches the Audit Logs corresponding to the workspace ID. If not provided, all the Audit Logs corresponding to the organization are fetched.

created_after

optional

string

Date and time in the ISO date-time format after which you want to fetch the Audit Logs.

* * *

  * **Example request** :


    
    
    GET /v2/audit-logs
    Host: api.rudderstack.com
    Authorization: Bearer 2QHVKQJeojt6Ae9e4iiOhycHrdG
    
    
    
    curl --location 'https://api.rudderstack.com/v2/audit-logs?after_cursor=213&per_page=2&workspace_id=1wJCPWvDLHgsi5inTHAChsrFn7O' \
    --header 'Authorization: Bearer 2QHVKQJeojt6Ae9e4iiOhycHrdG'
    

  * **Example response** :


    
    
    {
      "data": [{
          "id": "2CHj1PJ61lv1NPyQtCiFi2KVX2y",
          "actorId": "1vtoxffVBhY2c2iIS6o3GeM0O5B",
          "actorType": "user",
          "targetId": "2CHj1QBfmNWmpHOMAAkfDZ66fCr",
          "targetType": "destination",
          "action": "created",
          "ip": "::ffff:10.1.3.23",
          "createdAt": "2022-07-22T05:03:08.928Z",
          "workspaceId": "1vtp6E0bfo3FoGChWFW2f81fogc",
          "organizationId": "1vtp6F2GdSqeAHciTsEpNaW9mKy"
        },
        {
          "id": "2CHj6cFHxk11t2QekhPzKhuu7BK",
          "actorId": "1vtoxffVBhY2c2iIS6o3GeM0O5B",
          "actorType": "user",
          "targetId": "2CHj1QBfmNWmpHOMAAkfDZ66fCr",
          "targetType": "destination",
          "action": "updated",
          "ip": "::ffff:10.1.3.23",
          "createdAt": "2022-07-22T05:03:49.495Z",
          "workspaceId": "1vtp6E0bfo3FoGChWFW2f81fogc",
          "organizationId": "1vtp6F2GdSqeAHciTsEpNaW9mKy"
        }
      ],
      "paging": {
        "next": "/v2/audit-logs?after_cursor=2CHj6cFHxk11t2QekhPzKhuu7BK&per_page=2&workspace_id=1vtp6E0bfo3FoGChWFW2f81fogc",
        "total": 200
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> RudderStack supports specific values for the `targetType` and `action` parameters. See Supported target types and actions for more information.

**Response object parameters** :

data

optional

object

Contains the Audit Logs array.

id

optional

string

Unique identifier for the audit log entry.

actorId

optional

string

Unique identifier for the user who performed the action.

actorType

optional

string

Describes who performed the action. RudderStack currently supports only `user` actor type.

targetId

optional

string

Unique identifier for the target of the action.

targetType

optional

string

Describes the target on which the action is performed.

action

optional

string

Action performed by the user.

ip

optional

string

IP address of the user who performed the action.

createdAt

optional

string

Timestamp when the audit log was created

workspaceId

optional

string

Unique identifier for the workspace where the action was performed.

organizationId

optional

string

Unique identifier for the organization where the action was performed.

paging

optional

object

Contains the pagination information.

next

optional

string

Endpoint to fetch the next page.

total

required

integer

Total number of Audit Logs resulting from the query.

* * *

### Supported target types and actions

RudderStack currently supports following values for the `targetType` and `action` parameters pair:

`targetType` parameter| `action` parameter  
---|---  
`destination`| `connected_source`  
`destination`| `connected_transformation`  
`destination`| `created`  
`destination`| `deleted`  
`destination`| `disconnected_source`  
`destination`| `disconnected_transformation`  
`destination`| `updated`  
`destination`| `updated_transformation`  
`notification`| `updated`  
`permission`| `deleted_user_permissions`  
`permission`| `resource_access_updated`  
`permission`| `resource_locked`  
`profiles`| `created`  
`profiles`| `deleted`  
`profiles`| `updated`  
`source`| `connected_sql_model`  
`source`| `connected_tracking_plan`  
`source`| `created`  
`source`| `deleted`  
`source`| `disconnected_sql_model`  
`source`| `disconnected_tracking_plan`  
`source`| `updated`  
`source`| `updated_tracking_plan_config`  
`source`| `updated_bot_event_management`  
`source`| `deleted_bot_event_management`  
`sql_model`| `created`  
`sql_model`| `deleted`  
`sql_model`| `updated`  
`transformation`| `created`  
`transformation`| `deleted`  
`transformation`| `updated`  
`transformation_library`| `created`  
`transformation_library`| `deleted`  
`transformation_library`| `updated`  
`user`| `added_to_organization`  
`user`| `changed_permission`  
`user`| `disabled_mfa`  
`user`| `enabled_mfa`  
`user`| `removed_from_organization`  
`user`| `updated_phone_number`  
`user_invitation`| `created`  
`user_invitation`| `deleted`  
`user_invitation`| `updated`  
`workspace`| `deleted`  
`workspace`| `updated_data_retention`  
`workspace`| `updated_bot_event_management`  
`workspace`| `updated_bot_detection`