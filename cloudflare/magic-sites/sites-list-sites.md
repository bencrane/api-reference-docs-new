# List Sites

`GET /accounts/{account_id}/magic/sites`

Lists Sites associated with an account. Use connectorid query param to return sites where connectorid matches either site.ConnectorID or site.SecondaryConnectorID.

## Parameters

- **account_id** (string, required) [path]: 
- **connectorid** (string, optional) [query]: 

## Response

### 200

List Sites response

- **result** (array, optional): 

### 4XX

List Sites response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
