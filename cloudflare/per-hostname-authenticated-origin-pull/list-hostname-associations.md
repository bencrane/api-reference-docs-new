# List Hostname Associations

`GET /zones/{zone_id}/origin_tls_client_auth/hostnames`

List certificate ID - hostname associations for the given zone. Shows which hostnames are associated to which certificates for authenticated origin pulls.

## Parameters

- **zone_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

List Hostname Associations response

- **result** (array, optional): 
- **result_info** (object, optional): 

### 4XX

List Hostname Associations response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
