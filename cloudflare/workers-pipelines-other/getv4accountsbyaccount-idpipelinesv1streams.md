# List Streams

`GET /accounts/{account_id}/pipelines/v1/streams`

List/Filter Streams in Account.

## Parameters

- **account_id** (string, required) [path]: 
- **pipeline_id** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 

## Response

### 200

Indicates a successfully created Stream.

- **result** (array): 
- **result_info** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in listing Streams.
