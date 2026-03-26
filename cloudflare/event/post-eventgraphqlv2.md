# GraphQL endpoint for event aggregation

`POST /accounts/{account_id}/cloudforce-one/v2/events/graphql`

Execute GraphQL aggregations over threat events. Supports multi-dimensional group-bys, optional date range filtering, and multi-dataset aggregation.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

GraphQL response payload (data and errors).

- **data** (object): 
- **errors** (array): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
