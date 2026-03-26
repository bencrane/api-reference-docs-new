# Update IP profile

`PATCH /accounts/{account_id}/devices/ip-profiles/{profile_id}`

Updates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An optional description of the Device IP profile.
- **enabled** (boolean, optional): Whether the Device IP profile is enabled.
- **match** (string, optional): The wirefilter expression to match registrations. Available values: "identity.name", "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.saml_attributes".
- **name** (string, optional): A user-friendly name for the Device IP profile.
- **precedence** (integer, optional): The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.
- **subnet_id** (string, optional): The ID of the Subnet.

## Response

### 200

Update Device IP profile response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
