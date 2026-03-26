# Update a preset

`PATCH /accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}`

Update a preset by the provided preset ID

## Parameters

- **account_id** (string, required) [path]: 
- **app_id** (string, required) [path]: 
- **preset_id** (string, required) [path]: ID of the preset to fetch

## Request Body

- **config** (object, optional): 
- **name** (string, optional): Name of the preset
- **permissions** (object, optional): 
- **ui** (object, optional): 

## Response

### 200

Success response

- **data** (object, optional): 
- **success** (boolean, optional): Success status of the operation
