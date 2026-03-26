# Get Fraud Detection Settings

`GET /zones/{zone_id}/fraud_detection/settings`

Retrieve Fraud Detection settings for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Fraud Detection settings response

- **result** (object, optional): 

### 4XX

Fraud Detection settings response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
