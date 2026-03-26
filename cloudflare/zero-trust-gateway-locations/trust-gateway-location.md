# Create a Zero Trust Gateway location

`POST /accounts/{account_id}/gateway/locations`

Create a new Zero Trust Gateway location.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **client_default** (boolean, optional): Indicate whether this location is the default location.
- **dns_destination_ips_id** (string, optional): Specify the identifier of the pair of IPv4 addresses assigned to this location. When creating a location, if this field is absent or set to null, the pair of shared IPv4 addresses (0e4a32c6-6fb8-4858-9296-98f51631e8e6) is auto-assigned. When updating a location, if this field is absent or set to null, the pre-assigned pair remains unchanged.
- **ecs_support** (boolean, optional): Indicate whether the location must resolve EDNS queries.
- **endpoints** (object, optional): Configure the destination endpoints for this location.
- **name** (string, required): Specify the location name.
- **networks** (array, optional): Specify the list of network ranges from which requests at this location originate. The list takes effect only if it is non-empty and the IPv4 endpoint is enabled for this location.

## Response

### 200

Creates a Zero Trust Gateway location response.

_Empty object_

### 4XX

Creates a Zero Trust Gateway location response failure.

_Empty object_
