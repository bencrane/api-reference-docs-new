# Create Leaked Credential Checks Custom Detection

`POST /zones/{zone_id}/leaked-credential-checks/detections`

Create user-defined detection pattern for Leaked Credential Checks.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **id** (object, optional): Defines the unique ID for this custom detection.
- **password** (string, optional): Defines ehe ruleset expression to use in matching the password in a request.
- **username** (string, optional): Defines the ruleset expression to use in matching the username in a request.

## Response

### 200

Create Leaked Credential Checks custom detection response.

- **result** (object, optional): Defines a custom set of username/password expressions to match Leaked Credential Checks on.

### 4XX

Create Leaked Credential Checks custom detection failure response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
