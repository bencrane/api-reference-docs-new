# Profiles API

Run your Profiles project programmatically and check its run status.

Available Plans

  * enterprise


* * *

  *  __2 minute read

  * 


You can use the Profiles API to programmatically run your Profiles project and check its run status.

## Prerequisites

  * Set up a Profiles project in the [RudderStack dashboard](<https://app.rudderstack.com/>). Then, note down the Profiles project ID from the URL:

[![Profiles project ID from the URL](/docs/images/api/source-id.webp)](</docs/images/api/source-id.webp>)

  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to authenticate the API:

Resource| Permissions  
---|---  
Profiles| **Edit**  
  
#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Editor** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Editor permission](/docs/images/access-management/permissions/legacy/editor.webp)](</docs/images/access-management/permissions/legacy/editor.webp>)

## Authentication

The Profiles API uses [Bearer authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) in the following format:
    
    
    Authorization: Bearer <SERVICE_ACCESS_TOKEN>
    

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com/v2
    
    
    
    https://api.eu.rudderstack.com/v2
    

## Run project

You can trigger the run of a Profiles project using the below endpoint:

POST

/sources/<profilesID>/start

> ![info](/docs/images/info.svg)
> 
> To obtain the

**Path parameters**

profilesID

Required

String

ID of the Profiles project for which you want to trigger a run.

* * *

**Request body**

parameters

Optional

Array

Specify the parameters and their associated values to be passed for running the project. Multiple parameters can be passed. Each parameter and its associated value is a single string. Allowed parameters:  
  


  * `--model_refs`
  * `--begin_time`
  * `--end_time`
  * `--rebase_incremental`


**Example request**
    
    
     POST /v2/sources/<profilesID>/start HTTP/1.1
    Host: api.rudderstack.com
    Content-Type: application/json
    Accept: application/json
    Authorization: Bearer <token>
    
    {
      "parameters": ["--model_refs models/id_graph_users"]
    }
    
    
    
    curl --location 'https://api.rudderstack.com/v2/sources/<profilesID>/start' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <token>' \
    --data '{
      "parameters": ["--model_refs models/id_graph_users"]
    }'
    

**Example response**
    
    
    {
      "runId": "<run_id>"
    }
    

**Response codes**

Code| Description  
---|---  
200| Run started for the Profiles project. RudderStack also returns a run ID for the project.  
409| Profiles project is already running for the specified source ID.  
  
## Get run status

You can get the run status of your Profiles project using the below endpoint:

GET

/sources/{profilesID}/runs/{runId}/status

**Path parameters**

profilesID

Required

String

ID of the Profiles project for which you want to trigger a run.

runId

Required

String

ID of the Profiles project’s run.

> ![info](/docs/images/info.svg)
> 
> You can obtain the `runId` as the response of the above API endpoint (`/sources/<profilesID>/start`).

**Example request**
    
    
     GET /v2/sources/<profilesID>/runs/{run_id}/status HTTP/1.1
    Host: api.rudderstack.com
    Accept: application/json
    Authorization: Bearer <token>
    
    
    
    curl --location 'https://api.rudderstack.com/v2/sources/<profilesID>/runs/<run_id>/status' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <token>'
    

**Example response**
    
    
    {
      "jobId": "string",
      "jobRunId": "string",
      "status": "string",
      "startedAt": "2024-05-31T06:48:08.228Z",
      "finishedAt": "2024-05-31T06:48:08.228Z",
      "tasks": [{
        "taskId": "string",
        "taskRunId": "string",
        "startedAt": "2024-05-31T06:48:08.228Z",
        "finishedAt": "2024-05-31T06:48:08.228Z"
      }]
    }
    

**Response codes**

Code| Description  
---|---  
200| Successfully retrieved the run status of the project.