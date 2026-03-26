# Create Secondary Zone Configuration

`POST /zones/{zone_id}/secondary_dns/incoming`

Create secondary zone configuration for incoming zone transfers.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **auto_refresh_seconds** (number, required): How often should a secondary zone auto refresh regardless of DNS NOTIFY.
Not applicable for primary zones.
- **id** (string, required): 
- **name** (string, required): Zone name.
- **peers** (array, required): A list of peer tags.

## Response

### 200

Create Secondary Zone Configuration response.

_Empty object_

### 4XX

Create Secondary Zone Configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
