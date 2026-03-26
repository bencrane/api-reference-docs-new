# Create a preset

`POST /accounts/{account_id}/realtime/kit/{app_id}/presets`

Creates a preset belonging to the current App

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 

## Request Body

- **config** (object, required): 
- **name** (string, required): Name of the preset
- **permissions** (object, optional): 
- **ui** (object, required): 

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation
