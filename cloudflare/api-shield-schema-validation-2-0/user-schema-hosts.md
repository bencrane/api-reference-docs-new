# Retrieve schema hosts in a zone

`GET /zones/{zone_id}/api_gateway/user_schemas/hosts`

> **Deprecated**

Lists all unique hosts found in uploaded OpenAPI schemas for the zone. Useful for understanding which domains have schema coverage.

## Response

### 200

Retrieve schema hosts in a zone response

- **result** (array, optional): 

### 4XX

Retrieve schema hosts in a zone response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
