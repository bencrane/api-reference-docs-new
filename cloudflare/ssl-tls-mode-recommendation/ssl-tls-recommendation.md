# SSL/TLS Recommendation

`GET /zones/{zone_id}/ssl/recommendation`

> **Deprecated**

Retrieve the SSL/TLS Recommender's recommendation for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

SSL/TLS Recommendation response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.

### 4XX

SSL/TLS Recommendation response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Indicates the API call's success or failure.
