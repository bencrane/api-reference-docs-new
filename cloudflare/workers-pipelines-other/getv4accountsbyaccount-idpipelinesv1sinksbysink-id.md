# Get Sink Details

`GET /accounts/{account_id}/pipelines/v1/sinks/{sink_id}`

Get Sink Details.

## Parameters

- **account_id** (string, required) [path]: 
- **sink_id** (string, required) [path]: 

## Response

### 200

Indicates that Sink was retrieved.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in listing Sinks.
