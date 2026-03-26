# Create Stream

`POST /accounts/{account_id}/pipelines/v1/streams`

Create a new Stream.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **format** (object, optional): 
- **http** (object, optional): 
- **name** (string, required): Specifies the name of the Stream.
- **schema** (object, optional): 
- **worker_binding** (object, optional): 

## Response

### 200

Indicates a successfully created Stream.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in creating a Stream.
