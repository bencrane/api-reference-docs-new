# RudderStack Reverse ETL Connections API

Programmatically run syncs for a Reverse ETL connection.

* * *

  * __5 minute read

  * 


The Reverse ETL Connections API lets you programmatically run syncs for your Reverse ETL connections.

You can use this API to:

  * Trigger a new sync for a particular connection
  * Get details of all syncs for a connection
  * Stop a running sync for a connection


## Prerequisites

  * Get the connection ID for which you want to start/stop syncs from the RudderStack dashboard.
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to use the various API endpoints:

Resource| Permission  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
PII permissions  
Enterprise plan only| **Reverse ETL Sync Failure Samples** configured for the required source  
  
#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

The token leverages the following permissions for various endpoints:

Endpoint| Permissions  
---|---  
`/start`| Editor, Admin  
`/syncs`| Viewer, Editor, Admin  
`/syncs/{syncId}`| Viewer, Editor, Admin  
`/stop`| Editor, Admin  
  
## Authentication

The Reverse ETL Connections API uses [Bearer authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the following format:
    
    
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com/v2
    
    
    
    https://api.eu.rudderstack.com/v2
    

## Start sync

You can start a new sync for a Reverse ETL connection using the below endpoint:

POST

/retl-connections/{connectionId}/start

**Path parameters**

connectionId

Required

String

Connection ID for which RudderStack starts a new sync

* * *

**Request body**

syncType

Required

String

Specify the scope of sync. It can be one of the following:  
  


  * `incremental`: RudderStack syncs only the newly added data in the warehouse since the last sync.
  * `full`: RudderStack syncs all the data irrespective of whether it was synced to the destination previously.


**Example request**
    
    
     POST /v2/retl-connections/<connection_id>/start HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Accept: application/json
    Authorization: Bearer <token>
    
    {
      "syncType": "incremental"  // Other acceptable values: full
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/retl-connections/<connection_id>/start' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <token>' \
    --data '{
      "syncType": "incremental"  // Other acceptable values: full
    }'
    

**Example response**
    
    
    {
       “syncId”: “<sync_id>"
    }
    

**Response codes**

Code| Description  
---|---  
200| Sync started for Reverse ETL connection.  
  
RudderStack also returns a unique ID for the newly created sync.  
404| Reverse ETL connection was not found for the specified connection ID.  
409| A Reverse ETL sync is already running for the specified connection ID.  
  
## Get sync details

Use the following endpoints to get details of all syncs or an individual sync for a particular Reverse ETL connection. You can also filter the results by sync status, start time, and limit the number of results per page.

### All syncs

GET

/retl-connections/{connectionId}/syncs

**Path parameters**

connectionId

Required

String

Connection ID for which RudderStack fetches the syncs details.

**Query parameters**

status

Optional

String

Filter syncs by status. It accepts one of the following values - `running`, `succeeded`, and `failed`.

started_after

Optional

String (datetime)

Filter syncs started after the specified time (in UTC).

started_before

Optional

String (datetime)

Filter syncs started before the specified time (in UTC).

per_page

Optional

Integer

Limit the number of results shown in the page.

page

Optional

Integer

Show a particular page in the results.

* * *

**Example request**
    
    
     GET /v2/retl-connections/<connection_id>/syncs?status=<status>>&started_after=<started_after_date>&started_before=<started_before_date>&per_page=<results_per_page>>&page=<page_number> HTTP/1.1
    Host: api.rudderstack.com
    Accept: application/json
    Authorization: Bearer <token>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/retl-connections/<connection_id>/syncs?status=<status>&started_after=<started_after_time>&started_before=<started_before_time>&per_page=<results_per_page>>&page=<page_number>' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <token>'
    

**Example response**
    
    
    {
      "syncs": [{
        "id": "<sync_id>",
        "status": "running",
        "startedAt": "2024-04-20T05:41:18.871Z",
        "finishedAt": "2024-04-20T05:41:18.871Z",
        "error": "<string>",
        "metrics": {
          "succeeded": {
            "total": 0
          },
          "failed": {
            "total": 0
          },
          "changed": {
            "total": 0
          },
          "total": 0
        }
      }],
      "paging": {
        "total": 200,
        "next": "/<collection path>?page=2"
      }
    }
    

**Response codes**

Code| Description  
---|---  
200| List of all Reverse ETL syncs for the specified connection ID.  
404| Reverse ETL connection was not found for the specified connection ID.  
  
### Individual sync

GET

/retl-connections/{connectionId}/syncs/{syncId}

**Path parameters**

connectionId

Required

String

Connection ID for which RudderStack fetches the syncs details.

syncId

Required

String

ID for a particular Reverse ETL sync.

> ![info](/docs/images/info.svg)
> 
> You can find the sync ID from the `/start` endpoint response.

**Example request**
    
    
     GET /v2/retl-connections/<connection_id>/syncs/<sync_id> HTTP/1.1
    Host: api.rudderstack.com
    Accept: application/json
    Authorization: Bearer <token>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/retl-connections/<connection_id>/syncs/<sync_id>' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <token>'
    

**Example response**
    
    
    {
      "id": "<sync_id>",
      "status": "running",
      "startedAt": "2024-04-20T05:58:14.778Z",
      "finishedAt": "2024-04-20T05:58:14.778Z",
      "error": "<string>",
      "metrics": {
        "succeeded": {
          "total": 0
        },
        "failed": {
          "total": 0
        },
        "changed": {
          "total": 0
        },
        "total": 0
      }
    }
    

**Response codes**

Code| Description  
---|---  
200| Sync details for the specified connection ID and sync ID.  
404| Reverse ETL connection was not found for the specified connection ID.  
  
## Cancel sync

You can cancel a sync for a Reverse ETL connection using the below endpoint:

POST

/retl-connections/{connectionId}/stop

**Path parameters**

connectionId

Required

String

Connection ID for which RudderStack starts a new sync

* * *

**Example request**
    
    
     POST /v2/retl-connections/<connection_id>/stop HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Bearer <token>
    
    
    
    curl --location --request POST 'https://api.rudderstack.com/v2/retl-connections/<connection_id>/stop' \
    --header 'Authorization: Bearer <token>'
    

**Example response**

Code| Response| Description  
---|---|---  
204| Stop was requested.| RudderStack has successfully sent a cancellation request to stop the Reverse ETL connection sync.  
404| -| Reverse ETL connection was not found for the specified connection ID.  
  
## See also

  * [Trigger Syncs from dbt Cloud](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/trigger-syncs-from-dbt-cloud/>) using the Reverse ETL Connections API


## FAQ

#### Where can I find the connection ID for a Reverse ETL connection?

Go to the **Settings** tab of the connection to get the Connection ID for a particular Reverse ETL connection:

[![connection ID for Reverse ETL](/docs/images/retl-sources/connection-id.webp)](</docs/images/retl-sources/connection-id.webp>)