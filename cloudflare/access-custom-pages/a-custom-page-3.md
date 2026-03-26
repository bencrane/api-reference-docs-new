# Update a custom page

`PUT /accounts/{account_id}/access/custom_pages/{custom_page_id}`

Update a custom page

## Parameters

- **custom_page_id** (string, required) [path]: 
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

### 200

Update a custom page response

_Empty object_

### 4XX

Update a custom page response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
