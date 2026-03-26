# Patch Script Settings

`PATCH /accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/settings`

Patch script metadata, such as bindings.

## Parameters

- **account_id** (string, required) [path]: 
- **service_name** (string, required) [path]: 
- **environment_name** (string, required) [path]: 

## Request Body

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

## Response

### 200

Patch script settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch script settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
