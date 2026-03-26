# Traceroute

`POST /accounts/{account_id}/diagnostics/traceroute`

Run traceroutes from Cloudflare colos.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **colos** (array, optional): If no source colo names specified, all colos will be used. China colos are unavailable for traceroutes.
- **options** (object, optional): 
- **targets** (array, required): 

## Response

### 200

Traceroute response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Traceroute response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
