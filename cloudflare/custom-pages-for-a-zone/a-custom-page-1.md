# Update a custom page

`PUT /zones/{zone_identifier}/custom_pages/{identifier}`

Updates the configuration of an existing custom page.

## Parameters

- **identifier** (string, required) [path]: 
- **zone_identifier** (string, required) [path]: 

## Request Body

- **state** (string, required): The custom page state. Values: `default`, `customized`
- **url** (string, required): The URL associated with the custom page.

## Response

### 200

Update a custom page response

- **result** (object, optional): 

### 4XX

Update a custom page response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
