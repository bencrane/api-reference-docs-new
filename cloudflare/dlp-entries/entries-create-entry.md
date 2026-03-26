# Create custom entry

`POST /accounts/{account_id}/dlp/entries`

Creates a DLP custom entry.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **enabled** (boolean, required): 
- **name** (string, required): 
- **pattern** (object, required): 
- **profile_id** (string, optional): 

## Response

### 200

Create new custom entry response.

- **result** (object, optional): 

### 4XX

Create new custom entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
