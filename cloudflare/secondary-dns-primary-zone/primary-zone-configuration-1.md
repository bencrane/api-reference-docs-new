# Create Primary Zone Configuration

`POST /zones/{zone_id}/secondary_dns/outgoing`

Create primary zone configuration for outgoing zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **id** (string, required): 
- **name** (string, required): Zone name.
- **peers** (array, required): A list of peer tags.

## Response

### 200

Create Primary Zone Configuration response.

_Empty object_

### 4XX

Create Primary Zone Configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
