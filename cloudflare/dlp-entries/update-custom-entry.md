# Update custom entry

`PUT /accounts/{account_id}/dlp/entries/custom/{entry_id}`

Updates a DLP custom entry.

## Parameters

- **account_id** (string, required) [path]: 
- **entry_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **name** (string, optional): 
- **pattern** (object, optional): 
- **enabled** (boolean, optional): 

## Response

### 200

Update entry response.

- **result** (object, optional): 

### 4XX

Update entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
