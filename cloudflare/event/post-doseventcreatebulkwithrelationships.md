# Creates bulk DOS event with relationships and indicators

`POST /accounts/{account_id}/cloudforce-one/events/create/bulk/relationships`

> **Deprecated**

This method is deprecated. Please use `event_create_bulk` instead

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **data** (array, required): 
- **datasetId** (string, required): 

## Response

### 200

Returns the number of created bulk events with relationships.

- **createdEventsCount** (number): Number of events created
- **createdIndicatorsCount** (number): Number of indicators created
- **createdRelationshipsCount** (number): Number of relationships created
- **errorCount** (number): Number of errors encountered
- **errors** (array): Array of error details

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
