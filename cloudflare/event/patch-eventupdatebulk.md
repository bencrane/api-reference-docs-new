# Bulk update events

`PATCH /accounts/{account_id}/cloudforce-one/events/update/bulk`

Updates multiple events with the same field values. Maximum 100 events per request.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **datasetId** (string, required): Dataset ID containing the events to update. Required to prevent cross-account modifications.
- **eventIds** (array, required): List of event UUIDs to update (1-100)
- **updates** (object, required): Fields to update on all specified events. All fields including 'insight' are supported, except 'date' which requires shard migration.

## Response

### 200

Returns the count of updated events and any failures.

- **failedCount** (number): 
- **failures** (array): List of events that failed to update with error messages
- **updatedCount** (number): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
