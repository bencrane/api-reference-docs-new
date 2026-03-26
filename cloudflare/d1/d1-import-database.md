# Import SQL into your D1 Database

`POST /accounts/{account_id}/d1/database/{database_id}/import`

Generates a temporary URL for uploading an SQL file to, then instructing the D1 to import it
and polling it for status updates. Imports block the D1 for their duration.


## Parameters

- **account_id** (string, required) [path]: 
- **database_id** (string, required) [path]: 

## Request Body

One of: init, ingest, poll

## Response

### 200

Successful action. Import is either ready to start, under way, or finished (succeeded or failed).

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
