# Update a Request

`PUT /accounts/{account_id}/cloudforce-one/requests/{request_id}`

Updating a request alters the request in the Cloudforce One queue. This API may be used to update any attributes of the request after the initial submission. Only fields that you choose to update need to be add to the request body.

## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Request Body

- **content** (string, optional): Request content.
- **priority** (string, optional): Priority for analyzing the request.
- **request_type** (string, optional): Requested information from request.
- **summary** (string, optional): Brief description of the request.
- **tlp** (string, optional): The CISA defined Traffic Light Protocol (TLP). Values: `clear`, `amber`, `amber-strict`, `green`, `red`

## Response

### 200

Update request response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update request response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
