# Patch Zero Trust account configuration

`PATCH /accounts/{account_id}/gateway/configuration`

Update (PATCH) a single subcollection of settings such as `antivirus`, `tls_decrypt`, `activity_log`, `block_page`, `browser_isolation`, `fips`, `body_scanning`, or `certificate` without updating the entire configuration object. This endpoint returns an error if any settings collection lacks proper configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **settings** (object, optional): Specify account settings.

## Response

### 200

Zero Trust account configuration response.

_Empty object_

### 4XX

Zero Trust account configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
