# Export D1 Database as SQL

`POST /accounts/{account_id}/d1/database/{database_id}/export`

Returns a URL where the SQL contents of your D1 can be downloaded. Note: this process may take
some time for larger DBs, during which your D1 will be unavailable to serve queries. To avoid
blocking your DB unnecessarily, an in-progress export must be continually polled or will automatically cancel.


## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Request Body

- **current_bookmark** (string, optional): To poll an in-progress export, provide the current bookmark (returned by your first polling response)
- **dump_options** (object, optional): 
- **output_format** (string, required): Specifies that you will poll this endpoint until the export completes Values: `polling`

## Response

### 200

Polled successfully, task no longer running (errored or complete)

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 202

Polled successfully, task is currently running

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Poll failed (API error)

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
