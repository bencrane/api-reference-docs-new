# Get organization audit logs (Version 2, Beta release)

`GET /organizations/{organization_id}/logs/audit`

Gets a list of audit logs for an organization.

## Parameters

- **organization_id** (string, required) [path]: 
- **action_result** (array, optional) [query]: 
- **action_type** (array, optional) [query]: 
- **actor_context** (array, optional) [query]: 
- **actor_email** (array, optional) [query]: 
- **actor_id** (array, optional) [query]: 
- **actor_ip_address** (array, optional) [query]: 
- **actor_token_id** (array, optional) [query]: 
- **actor_token_name** (array, optional) [query]: 
- **actor_type** (array, optional) [query]: 
- **id** (array, optional) [query]: 
- **raw_cf_ray_id** (array, optional) [query]: 
- **raw_method** (array, optional) [query]: 
- **raw_status_code** (array, optional) [query]: 
- **raw_uri** (array, optional) [query]: 
- **resource_id** (array, optional) [query]: 
- **resource_product** (array, optional) [query]: 
- **resource_type** (array, optional) [query]: 
- **resource_scope** (array, optional) [query]: 
- **action_result.not** (array, optional) [query]: 
- **action_type.not** (array, optional) [query]: 
- **actor_context.not** (array, optional) [query]: 
- **actor_email.not** (array, optional) [query]: 
- **actor_id.not** (array, optional) [query]: 
- **actor_ip_address.not** (array, optional) [query]: 
- **actor_token_id.not** (array, optional) [query]: 
- **actor_token_name.not** (array, optional) [query]: 
- **actor_type.not** (array, optional) [query]: 
- **id.not** (array, optional) [query]: 
- **raw_cf_ray_id.not** (array, optional) [query]: 
- **raw_method.not** (array, optional) [query]: 
- **raw_status_code.not** (array, optional) [query]: 
- **raw_uri.not** (array, optional) [query]: 
- **resource_id.not** (array, optional) [query]: 
- **resource_product.not** (array, optional) [query]: 
- **resource_type.not** (array, optional) [query]: 
- **resource_scope.not** (array, optional) [query]: 
- **since** (string, required) [query]: Limits the returned results to logs newer than the specified date. This can be a date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that conforms to RFC3339.
- **before** (string, required) [query]: Limits the returned results to logs older than the specified date. This can be a date string 2019-04-30 (interpreted in UTC) or an absolute timestamp that conforms to RFC3339.
- **direction** (string, optional) [query]: 
- **limit** (number, optional) [query]: 
- **cursor** (string, optional) [query]: 

## Response

### 200

Get organization audit logs successful response

- **errors** (array, optional): 
- **result_info** (object, optional): Provides information about the result of the request, including count and cursor.
- **success** (boolean, optional): Indicates whether the API call was successful Values: `true`
- **result** (array, optional): 

### 4XX

Get organization audit logs failed response

- **errors** (array): A list of error messages.
- **messages** (array): 
- **success** (boolean): Indicates whether the API call was failed
