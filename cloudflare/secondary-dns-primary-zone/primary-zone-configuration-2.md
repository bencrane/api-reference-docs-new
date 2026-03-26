# Update Primary Zone Configuration

`PUT /zones/{zone_id}/secondary_dns/outgoing`

Update primary zone configuration for outgoing zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **id** (string, required): 
- **name** (string, required): Zone name.
- **peers** (array, required): A list of peer tags.

## Response

### 200

Update Primary Zone Configuration response.

_Empty object_

### 4XX

Update Primary Zone Configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
