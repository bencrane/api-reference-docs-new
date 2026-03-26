# Update Stream

`PATCH /accounts/{account_id}/pipelines/v1/streams/{stream_id}`

Update a Stream.

## Parameters

- **account_id** (string, required) [path]: 
- **stream_id** (string, required) [path]: 

## Request Body

- **http** (object, optional): 
- **worker_binding** (object, optional): 

## Response

### 200

Indicates a successfully updated Stream.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in creating a Stream.
