# Create a custom page

`POST /accounts/{account_id}/access/custom_pages`

Create a custom page

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **app_count** (integer, optional): Number of apps the custom page is assigned to.
- **created_at** (object, optional): 
- **custom_html** (string, required): Custom page HTML.
- **name** (string, required): Custom page name.
- **type** (string, required): Custom page type. Values: `identity_denied`, `forbidden`
- **uid** (string, optional): UUID.
- **updated_at** (object, optional): 

## Response

### 201

Create a custom page response

_Empty object_

### 4XX

Create a custom page response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
