# Update a Web Analytics site

`PUT /accounts/{account_id}/rum/site_info/{site_id}`

Updates an existing Web Analytics site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Request Body

- **auto_install** (boolean, optional): If enabled, the JavaScript snippet is automatically injected for orange-clouded sites.
- **enabled** (boolean, optional): Enables or disables RUM. This option can be used only when auto_install is set to true.
- **host** (string, optional): The hostname to use for gray-clouded sites.
- **lite** (boolean, optional): If enabled, the JavaScript snippet will not be injected for visitors from the EU.
- **zone_tag** (string, optional): The zone identifier.

## Response

### 200

Updated Web Analytics site.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
