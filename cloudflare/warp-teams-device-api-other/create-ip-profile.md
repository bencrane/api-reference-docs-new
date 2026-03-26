# Create IP profile

`POST /accounts/{account_id}/devices/ip-profiles`

Creates a WARP Device IP profile. Currently, only IPv4 Device subnets can be associated.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An optional description of the Device IP profile.
- **enabled** (boolean, optional): Whether the Device IP profile will be applied to matching devices.
- **match** (string, required): The wirefilter expression to match registrations. Available values: "identity.name", "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.saml_attributes".
- **name** (string, required): A user-friendly name for the Device IP profile.
- **precedence** (integer, required): The precedence of the Device IP profile. Lower values indicate higher precedence. Device IP profile will be evaluated in ascending order of this field.
- **subnet_id** (string, required): The ID of the Subnet.

## Response

### 200

Create Device IP profile response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
