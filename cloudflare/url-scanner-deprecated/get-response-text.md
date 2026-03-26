# Get raw response

`GET /accounts/{account_id}/urlscanner/response/{response_id}`

> **Deprecated**

Returns the plain response of the network request.

## Parameters

- **response_id** (string, required) [path]: Response hash.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

When `har.log.entries[].response._cf.contentAvailable` is `true`, use `response._cf.hash` value to fetch the raw response.

### 400

Invalid params.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not

### 404

Scan not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not
