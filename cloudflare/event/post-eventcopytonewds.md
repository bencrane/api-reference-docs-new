# Copies specified events from one dataset to another dataset

`POST /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/copy`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.
- **keepRawData** (boolean, optional) [query]: If true, copies raw data to the destination dataset. Default is false (raw data is stripped/not copied).

## Request Body

- **destDatasetId** (string, required): 
- **eventIds** (array, required): 

## Response

### 200

Returns the number of copied events

- **copied** (number): Number of events successfully copied
- **indicatorsCopied** (number): Number of indicators successfully copied
- **insertFailures** (array): Array of events that failed to insert into destination
- **relationshipsCopied** (number): Number of relationships successfully copied

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
