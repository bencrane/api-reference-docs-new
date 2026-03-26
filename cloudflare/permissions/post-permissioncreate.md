# Create a permission for dataset

`POST /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/permissions`

Create a permission

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Request Body

- **role** (string, required):  Values: `read`, `write`
- **subjectId** (string, required): 
- **subjectType** (string, required):  Values: `account`, `group`

## Response

### 200

Returns the created permission.

- **createdAt** (string): 
- **resourceId** (string): The resource ID this permission applies to account_id or group_id
- **resourceType** (string): 
- **role** (string): 
- **subjectId** (string): 
- **subjectType** (string): 
- **updatedAt** (string): 
- **uuid** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
