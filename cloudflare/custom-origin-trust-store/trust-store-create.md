# Upload Custom Origin Trust Store

`POST /zones/{zone_id}/acm/custom_trust_store`

Add Custom Origin Trust Store for a Zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **certificate** (string, required): The zone's SSL certificate or certificate and the intermediate(s).

## Response

### 200

Upload Custom Origin Trust Store response

- **result** (object, optional): 

### 4XX

Upload Custom Origin Trust Store response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
