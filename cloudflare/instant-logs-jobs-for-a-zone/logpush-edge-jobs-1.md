# Create Instant Logs job

`POST /zones/{zone_id}/logpush/edge/jobs`

Creates a new Instant Logs job for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **fields** (string, optional): Comma-separated list of fields.
- **filter** (string, optional): Filters to drill down into specific events.
- **sample** (integer, optional): The sample parameter is the sample rate of the records set by the client: "sample": 1 is 100% of records "sample": 10 is 10% and so on.

## Response

### 200

Create Instant Logs job response.

- **result** (object, optional): 

### 4XX

Create Instant Logs job response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
