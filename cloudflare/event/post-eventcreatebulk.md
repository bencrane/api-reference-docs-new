# Creates bulk events

`POST /accounts/{account_id}/cloudforce-one/events/create/bulk`

The `datasetId` parameter must be defined. To list existing datasets (and their IDs) in your account, use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **data** (array, required): 
- **datasetId** (string, required): 
- **includeCreatedEvents** (boolean, optional): When true, response includes array of created event UUIDs and shard IDs. Useful for tracking which events were created and where.

## Response

### 202

Accepted. Events created; indicators queued for async processing.

- **createBulkEventsRequestId** (string): Correlation ID for async indicator processing
- **createdEvents** (array): Array of created events with UUIDs and shard locations. Only present when includeCreatedEvents=true
- **createdEventsCount** (number): Number of events created
- **createdTagsCount** (number): Number of new tags created in SoT
- **errorCount** (number): Number of errors encountered
- **errors** (array): Array of error details
- **queuedIndicatorsCount** (number): Number of indicators queued for async processing

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
