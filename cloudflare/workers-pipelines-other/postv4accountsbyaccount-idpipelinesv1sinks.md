# Create Sink

`POST /accounts/{account_id}/pipelines/v1/sinks`

Create a new Sink.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, optional): Defines the configuration of the R2 Sink.
- **format** (object, optional): 
- **name** (string, required): Defines the name of the Sink.
- **schema** (object, optional): 
- **type** (string, required): Specifies the type of sink. Values: `r2`, `r2_data_catalog`

## Response

### 200

Indicates a successfully created Sink.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in creating a Sink.
