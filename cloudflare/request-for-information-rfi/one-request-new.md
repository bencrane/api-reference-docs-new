# Create a New Request.

`POST /accounts/{account_id}/cloudforce-one/requests/new`

Creating a request adds the request into the Cloudforce One queue for analysis. In addition to the content, a short title, type, priority, and releasability should be provided. If one is not provided, a default will be assigned.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **content** (string, optional): Request content.
- **priority** (string, optional): Priority for analyzing the request.
- **request_type** (string, optional): Requested information from request.
- **summary** (string, optional): Brief description of the request.
- **tlp** (string, optional): The CISA defined Traffic Light Protocol (TLP). Values: `clear`, `amber`, `amber-strict`, `green`, `red`

## Response

### 200

Create request response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
