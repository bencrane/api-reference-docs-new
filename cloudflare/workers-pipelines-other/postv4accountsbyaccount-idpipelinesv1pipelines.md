# Create Pipeline

`POST /accounts/{account_id}/pipelines/v1/pipelines`

Create a new Pipeline.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, required): Specifies the name of the Pipeline.
- **sql** (string, required): Specifies SQL for the Pipeline processing flow.

## Response

### 200

Indicates a successfully created Pipeline.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates an error in creating a Pipeline.
