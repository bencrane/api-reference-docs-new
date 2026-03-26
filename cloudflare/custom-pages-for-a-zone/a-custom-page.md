# Get a custom page

`GET /zones/{zone_identifier}/custom_pages/{identifier}`

Fetches the details of a custom page.

## Parameters

- **identifier** (string, required) [path]: 
- **zone_identifier** (string, required) [path]: 

## Response

### 200

Get a custom page response

- **created_on** (string): 
- **description** (string): 
- **id** (string): 
- **modified_on** (string): 
- **preview_target** (string): 
- **required_tokens** (array): 
- **state** (string): The custom page state.
- **url** (string): The URL associated with the custom page.

### 4XX

Get a custom page response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
