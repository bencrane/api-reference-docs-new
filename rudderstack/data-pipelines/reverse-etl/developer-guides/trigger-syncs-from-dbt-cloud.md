# How to Trigger Reverse ETL Syncs from dbt Cloud

Trigger Reverse ETL syncs when dbt Cloud jobs complete by implementing webhooks with the RudderStack RETL Connections API.

* * *

  * __9 minute read

  * 


This guide shows you how to automatically trigger RudderStack Reverse ETL syncs when your dbt Cloud jobs complete.

## Overview

You can automatically trigger RudderStack Reverse ETL syncs whenever your dbt Cloud jobs complete, ensuring your downstream destinations always get fresh, transformed data without manual intervention or arbitrary CRON schedules.

> ![info](/docs/images/info.svg)
> 
> This integration uses dbt Cloud webhooks to notify a middleware endpoint when jobs complete. Your middleware then calls the [RudderStack RETL Connections API](<https://www.rudderstack.com/docs/api/retl-connections-api/>) to start a sync.

### Integration architecture

[![Integration architecture overview](/docs/images/data-pipelines/retl-trigger-sync/integration-architecture-overview.webp)](</docs/images/data-pipelines/retl-trigger-sync/integration-architecture-overview.webp>)

The following steps summarize the integration flow:

  1. dbt Cloud job completes successfully.
  2. dbt Cloud sends a `POST` request (without authentication) with a fixed payload to your middleware endpoint.
  3. Your middleware receives the webhook and checks for `runStatus === "Success"`.
  4. Middleware calls the [RudderStack Reverse ETL Connections API](<https://www.rudderstack.com/docs/api/retl-connections-api/>) with the `Authorization: Bearer <TOKEN>` header.
  5. RudderStack sync runs with fresh data from your warehouse.


## Prerequisites

Before you begin, make sure you have the following:

  * dbt Cloud account with Team or Enterprise plan
  * Account Admin, Admin, or Developer permissions in dbt Cloud
  * RudderStack workspace with a [Reverse ETL connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) configured
  * Ability to deploy a webhook handler (AWS Lambda, GCP Cloud Function, Cloudflare Worker, or similar)


## 1\. Get your RudderStack credentials

This section lists the steps to get the RudderStack credentials required for the integration.

### Generate a Service Access Token

Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>):

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
  
#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Editor** or **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Editor permission](/docs/images/access-management/permissions/legacy/editor.webp)](</docs/images/access-management/permissions/legacy/editor.webp>)

### Get your Reverse ETL connection ID

  1. Go to **RudderStack Dashboard** > **Collect** > **Sources**.
  2. Select your Reverse ETL source.
  3. Click on the connection (source-destination pair) you want to trigger.
  4. Go to the **Settings** tab and copy the **Connection ID** from the URL or connection details.

[![Reverse ETL connection ID](/docs/images/data-pipelines/retl-trigger-sync/retl-connection-id.webp)](</docs/images/data-pipelines/retl-trigger-sync/retl-connection-id.webp>)

## 2\. dbt Cloud webhook payload

When a job completes, dbt Cloud sends a `POST` request with a payload **similar** to the one shown below:
    
    
    {
      "accountId": 12345,
      "eventId": "wev_2KkC78P4Qux7RSn8XeZ2o2pdvcU",
      "timestamp": "2026-01-28T15:59:37.985673361Z",
      "eventType": "job.run.completed",
      "webhookId": "wsu_2OOKhFqtZGSLkMezu3SUujcF0Zj",
      "webhookName": "RudderStack rETL Sync",
      "data": {
        "jobId": "123",
        "jobName": "Daily Transform Job",
        "runId": "456",
        "environmentId": "789",
        "environmentName": "Production",
        "dbtVersion": "1.7.0",
        "projectName": "Analytics Project",
        "projectId": "101112",
        "runStatus": "Success",
        "runStatusCode": 10,
        "runStatusMessage": "",
        "runReason": "Scheduled",
        "runStartedAt": "2026-01-28T14:59:37.985673814Z",
        "runFinishedAt": "2026-01-28T15:59:37.985673955Z"
      }
    }
    

#### Key fields to reference

Field| Notes  
---|---  
`data.runStatus`| Check for `"Success"` before triggering the sync  
`data.runStatusCode`| `10` indicates Success, `20` indicates Error  
`data.jobId`| Use this to map specific dbt jobs to specific Reverse ETL connections  
  
> ![warning](/docs/images/warning.svg)
> 
> **Important consideration**
> 
> dbt Cloud sends a simple `POST` request with a fixed JSON payload. You cannot add custom headers, authentication, or modify the payload structure. This is why you need middleware — your middleware receives this `POST` request, then makes an authenticated call to RudderStack’s [Reverse ETL Connections API](<https://www.rudderstack.com/docs/api/retl-connections-api/>) with the required `Authorization: Bearer <TOKEN>` header.

## 3\. Create the webhook handler

Choose a platform that best fits your infrastructure. The following examples show implementations for common serverless platforms.

### AWS Lambda (Node.js)
    
    
    // index.js
    const https = require('https');
    
    // Configuration - use environment variables
    const RUDDERSTACK_API_TOKEN = process.env.RUDDERSTACK_API_TOKEN;
    const RETL_CONNECTION_ID = process.env.RETL_CONNECTION_ID;
    
    // RudderStack API base URL (use api.eu.rudderstack.com for EU)
    const RS_API_BASE = 'api.rudderstack.com';
    
    exports.handler = async (event) => {
      try {
        // Parse the dbt Cloud webhook payload
        const body = JSON.parse(event.body);
    
        console.log('Received dbt Cloud webhook:', JSON.stringify(body, null, 2));
    
        // Check if the job completed successfully
        const runStatus = body.data?.runStatus;
    
        if (runStatus !== 'Success') {
          console.log(`Job did not succeed (status: ${runStatus}). Skipping sync.`);
          return {
            statusCode: 200,
            body: JSON.stringify({
              message: 'Skipped - job not successful',
              status: runStatus
            })
          };
        }
    
        // Trigger RudderStack RETL sync
        const syncResult = await triggerRETLSync();
    
        return {
          statusCode: 200,
          body: JSON.stringify({
            message: 'RETL sync triggered successfully',
            syncId: syncResult.syncId
          })
        };
    
      } catch (error) {
        console.error('Error processing webhook:', error);
        return {
          statusCode: 500,
          body: JSON.stringify({
            error: error.message
          })
        };
      }
    };
    
    function triggerRETLSync() {
      return new Promise((resolve, reject) => {
        const postData = JSON.stringify({
          syncType: 'incremental' // or 'full' for full sync
        });
    
        const options = {
          hostname: RS_API_BASE,
          port: 443,
          path: `/v2/retl-connections/${RETL_CONNECTION_ID}/start`,
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${RUDDERSTACK_API_TOKEN}`,
            'Content-Length': Buffer.byteLength(postData)
          }
        };
    
        const req = https.request(options, (res) => {
          let data = '';
          res.on('data', chunk => data += chunk);
          res.on('end', () => {
            if (res.statusCode === 200) {
              resolve(JSON.parse(data));
            } else {
              reject(new Error(`API returned ${res.statusCode}: ${data}`));
            }
          });
        });
    
        req.on('error', reject);
        req.write(postData);
        req.end();
      });
    }
    

Set the following environment variables — replace the placeholders with the actual values obtained in Step 1:
    
    
    RUDDERSTACK_API_TOKEN=<SERVICE_ACCESS_TOKEN>
    RETL_CONNECTION_ID=<REVERSE_ETL_CONNECTION_ID>
    

### GCP Cloud Function (Python)
    
    
    # main.py
    import os
    import json
    import requests
    import functions_framework
    
    RUDDERSTACK_API_TOKEN = os.environ.get('RUDDERSTACK_API_TOKEN')
    RETL_CONNECTION_ID = os.environ.get('RETL_CONNECTION_ID')
    
    # Use api.eu.rudderstack.com for EU region
    RS_API_BASE = 'https://api.rudderstack.com/v2'
    
    @functions_framework.http
    def handle_dbt_webhook(request):
      """Handle incoming dbt Cloud webhook and trigger RETL sync."""
    
      # Parse webhook payload
      try:
        payload = request.get_json()
        print(f"Received dbt webhook: {json.dumps(payload, indent=2)}")
      except Exception as e:
        return (f'Invalid JSON: {e}', 400)
    
      # Check job status
      run_status = payload.get('data', {}).get('runStatus')
    
      if run_status != 'Success':
        print(f"Job status is '{run_status}', skipping sync")
        return (json.dumps({
          'message': 'Skipped - job not successful',
          'status': run_status
        }), 200)
    
      # Trigger RETL sync with Bearer authentication
      try:
        response = requests.post(
          f'{RS_API_BASE}/retl-connections/{RETL_CONNECTION_ID}/start',
          headers={
            'Authorization': f'Bearer {RUDDERSTACK_API_TOKEN}',
            'Content-Type': 'application/json'
          },
          json={
            'syncType': 'incremental' # or 'full'
          }
        )
        response.raise_for_status()
        result = response.json()
    
        print(f"RETL sync triggered: {result}")
        return (json.dumps({
          'message': 'RETL sync triggered successfully',
          'syncId': result.get('syncId')
        }), 200)
    
      except requests.exceptions.RequestException as e:
        print(f"Error triggering sync: {e}")
        return (json.dumps({
          'error': str(e)
        }), 500)
    

Set the following environment variables — replace the placeholders with the actual values obtained in Step 1:
    
    
    RUDDERSTACK_API_TOKEN=<SERVICE_ACCESS_TOKEN>
    RETL_CONNECTION_ID=<REVERSE_ETL_CONNECTION_ID>
    

Then, update `requirements.txt` with the following dependencies:
    
    
    functions-framework==3.*
    requests==2.*
    

### Cloudflare Worker (JavaScript)
    
    
    // worker.js
    const RS_API_BASE = 'https://api.rudderstack.com/v2';
    
    export default {
      async fetch(request, env) {
        // Only accept POST requests
        if (request.method !== 'POST') {
          return new Response('Method not allowed', {
            status: 405
          });
        }
    
        try {
          const payload = await request.json();
          console.log('Received dbt webhook:', JSON.stringify(payload));
    
          // Check job status
          const runStatus = payload.data?.runStatus;
    
          if (runStatus !== 'Success') {
            return Response.json({
              message: 'Skipped - job not successful',
              status: runStatus
            });
          }
    
          // Trigger RudderStack RETL sync
          const syncResponse = await fetch(
            `${RS_API_BASE}/retl-connections/${env.RETL_CONNECTION_ID}/start`, {
              method: 'POST',
              headers: {
                'Authorization': `Bearer ${env.RUDDERSTACK_API_TOKEN}`,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                syncType: 'incremental'
              })
            }
          );
    
          if (!syncResponse.ok) {
            throw new Error(`API returned ${syncResponse.status}`);
          }
    
          const result = await syncResponse.json();
    
          return Response.json({
            message: 'RETL sync triggered successfully',
            syncId: result.syncId
          });
    
        } catch (error) {
          console.error('Error:', error);
          return Response.json({
            error: error.message
          }, {
            status: 500
          });
        }
      }
    };
    

Set the environment variables in `wrangler.toml` — replace the placeholders with the actual values obtained in Step 1:
    
    
    [vars]
    RETL_CONNECTION_ID = "<REVERSE_ETL_CONNECTION_ID>"
    
    # Use secrets for the Service Access Token:
    # wrangler secret put RUDDERSTACK_API_TOKEN
    

## 4\. Deploy your webhook handler

This section lists the steps to deploy the webhook handler depending on your chosen platform.

### AWS Lambda

  1. Create a new Lambda function with Node.js 18.x or later.
  2. Paste the code and set the environment variables.
  3. Create an API Gateway trigger (HTTP API).
  4. Note the endpoint URL for the next step.


### GCP Cloud Function
    
    
    gcloud functions deploy dbt-rudderstack-webhook \
      --runtime python311 \
      --trigger-http \
      --allow-unauthenticated \
      --set-env-vars RUDDERSTACK_API_TOKEN=xxx,RETL_CONNECTION_ID=xxx
    

### Cloudflare Worker
    
    
    wrangler deploy
    

## 5\. Configure the dbt Cloud webhook

  1. In dbt Cloud, go to **Account** > **Account Settings** in the left sidebar.
  2. Select **Webhooks** under the **Settings** menu.
  3. Click **Create Webhook**.
  4. Configure the webhook with the following details:

Setting| Notes  
---|---  
Webhook name| Name it as `RudderStack rETL Sync`  
Description| Enter a brief description of the webhook, for example, `Triggers RudderStack Reverse ETL sync on job completion`  
Events| Select `Run completed` (optionally, `Run started` or `Run errored`)  
Jobs| Select the specific jobs, for example, `Salesforce Utilisation Model`  
Endpoint| Enter your deployed middleware URL, for example, `https://your-function.cloud.provider.com`  
  
  5. Click **Save**.
  6. Use the **Test Endpoint** button to verify your middleware is reachable.
  7. Finally, click **Save**.


## 6\. Test the integration

This section lists the various options to test your integration.

### Test the webhook handler directly
    
    
    curl -X POST https://your-webhook-url.com \
      -H "Content-Type: application/json" \
      -d '{
        "eventType": "job.run.completed",
        "data": {
          "jobId": "12345",
          "jobName": "Test Job",
          "runStatus": "Success"
        }
      }'
    

**Expected response** :
    
    
    {
      "message": "RETL sync triggered successfully",
      "syncId": "abc123..."
    }
    

### Test from dbt Cloud

  1. Go to your dbt Cloud job.

  2. Click **Run Now**.

  3. Wait for the job to complete.

  4. Check the following:

     * Your webhook handler logs
     * In your RudderStack dashboard, go to your Reverse ETL connection and click the **Syncs** tab


You should see a new sync entry with the timestamp matching your dbt Cloud job completion time.

## 7\. (Optional) Test the integration locally with ngrok

Before deploying to production, test the entire flow locally using ngrok to expose your local server to dbt Cloud.

#### 1\. Install ngrok
    
    
    # macOS
    brew install ngrok
    
    # Or download from https://ngrok.com/download
    

#### 2\. Create a local server

Create a file named `webhook_server.py`:
    
    
    from flask import Flask, request, jsonify
    import requests
    import os
    
    app = Flask(__name__)
    
    RUDDERSTACK_API_TOKEN = os.environ.get('RUDDERSTACK_API_TOKEN')
    RETL_CONNECTION_ID = os.environ.get('RETL_CONNECTION_ID')
    RS_API_BASE = 'https://api.rudderstack.com/v2'
    
    @app.route('/webhook', methods=['POST'])
    def handle_webhook():
      payload = request.get_json()
      print(f"Received dbt Cloud webhook: {payload}")
    
      run_status = payload.get('data', {}).get('runStatus')
    
      if run_status != 'Success':
        print(f"Job status is '{run_status}', skipping sync")
        return jsonify({
          'message': 'Skipped',
          'status': run_status
        }), 200
    
      # Trigger RETL sync
      response = requests.post(
        f'{RS_API_BASE}/retl-connections/{RETL_CONNECTION_ID}/start',
        headers={
          'Authorization': f'Bearer {RUDDERSTACK_API_TOKEN}',
          'Content-Type': 'application/json'
        },
        json={
          'syncType': 'incremental'
        }
      )
    
      print(f"RudderStack API response: {response.status_code} - {response.text}")
    
      if response.ok:
        return jsonify({
          'message': 'Sync triggered',
          'result': response.json()
        }), 200
      else:
        return jsonify({
          'error': response.text
        }), 500
    
    if __name__ == '__main__':
      app.run(port=5000, debug=True)
    

#### 3\. Run the local server
    
    
    # Install dependencies
    pip install flask requests
    
    # Set environment variables
    export RUDDERSTACK_API_TOKEN="SERVICE_ACCESS_TOKEN"
    export RETL_CONNECTION_ID="REVERSE_ETL_CONNECTION_ID"
    
    # Start the server
    python webhook_server.py
    

#### 4\. Expose with ngrok

In a new terminal:
    
    
    ngrok http 5000
    

ngrok outputs something like:
    
    
    Forwarding    https://ed94845ef6e0.ngrok-free.app -> http://localhost:5000
    

#### 5\. Configure dbt Cloud

  1. Copy the ngrok HTTPS URL, for example, `https://ed94845ef6e0.ngrok-free.app`.
  2. In dbt Cloud, go to **Settings** > **Webhooks**.
  3. Set the **Endpoint** to `https://ed94845ef6e0.ngrok-free.app/webhook`.
  4. Click **Test Endpoint** to verify connectivity.
  5. Run a dbt job and watch your local terminal for the webhook payload.


#### 6\. Verify the flow

In your local terminal, you should see the incoming dbt Cloud webhook payload and the RudderStack API response confirming the sync was triggered successfully.

Check the RudderStack dashboard to confirm the sync started.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** ngrok free tier URLs change each time you restart. For persistent URLs, use ngrok’s paid plan or deploy to a cloud function for final testing.

## Troubleshooting

Problem| Solution  
---|---  
Webhook not firing| Check the dbt Cloud webhook configuration and ensure the correct job is selected  
401 Unauthorized from RudderStack| Verify the Service Access Token has the correct permissions and is not expired  
404 Not Found| Check the Connection ID is correct and the connection exists in your workspace  
409 Conflict| A sync is already running — wait for it to complete before triggering another sync  
Sync triggers but no data flows| Check your Reverse ETL source query and field mappings in the connection configuration  
  
#### API endpoints for debugging

  1. Check sync status


    
    
    curl -X GET "https://api.rudderstack.com/v2/retl-connections/{connectionId}/syncs" \
      -H "Authorization: Bearer {TOKEN}"
    

  2. Stop a running sync


    
    
    curl -X POST "https://api.rudderstack.com/v2/retl-connections/{connectionId}/stop" \
      -H "Authorization: Bearer {TOKEN}"
    

## See more

  * [RudderStack RETL Connections API](<https://www.rudderstack.com/docs/api/retl-connections-api/>)
  * [Set Up a Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>)


## Help and support

For any questions or support, contact [RudderStack support](<mailto:support@rudderstack.com>).