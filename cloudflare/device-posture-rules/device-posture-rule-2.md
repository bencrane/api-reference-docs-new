# Update a device posture rule

`PUT /accounts/{account_id}/devices/posture/{rule_id}`

Updates a device posture rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): The description of the device posture rule.
- **expiration** (string, optional): Sets the expiration time for a posture check result. If empty, the result remains valid until it is overwritten by new data from the WARP client.
- **input** (object, optional): The value to be checked against.
- **match** (array, optional): The conditions that the client must match to run the rule.
- **name** (string, required): The name of the device posture rule.
- **schedule** (string, optional): Polling frequency for the WARP client posture check. Default: `5m` (poll every five minutes). Minimum: `1m`.
- **type** (string, required): The type of device posture rule. Values: `file`, `application`, `tanium`, `gateway`, `warp`, `disk_encryption`, `serial_number`, `sentinelone`, `carbonblack`, `firewall`, `os_version`, `domain_joined`, `client_certificate`, `client_certificate_v2`, `antivirus`, `unique_client_id`, `kolide`, `tanium_s2s`, `crowdstrike_s2s`, `intune`, `workspace_one`, `sentinelone_s2s`, `custom_s2s`

## Response

### 200

Update a device posture rule response.

- **result** (object, optional): 

### 4XX

Update a device posture rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
