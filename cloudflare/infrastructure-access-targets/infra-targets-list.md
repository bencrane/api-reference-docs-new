# List all targets

`GET /accounts/{account_id}/infrastructure/targets`

Lists and sorts an account’s targets. Filters are optional and are ANDed
together.

## Parameters

- **account_id** (string, required) [path]: 
- **hostname** (string, optional) [query]: Hostname of a target
- **hostname_contains** (string, optional) [query]: Partial match to the hostname of a target
- **virtual_network_id** (string, optional) [query]: Private virtual network identifier of the target
- **ip_v4** (string, optional) [query]: IPv4 address of the target
- **ip_v6** (string, optional) [query]: IPv6 address of the target
- **created_before** (string, optional) [query]: Date and time at which the target was created before (inclusive)
- **created_after** (string, optional) [query]: Date and time at which the target was created after (inclusive)
- **modified_before** (string, optional) [query]: Date and time at which the target was modified before (inclusive)
- **modified_after** (string, optional) [query]: Date and time at which the target was modified after (inclusive)
- **ips** (array, optional) [query]: Filters for targets that have any of the following IP addresses. Specify
`ips` multiple times in query parameter to build list of candidates.
- **target_ids** (array, optional) [query]: Filters for targets that have any of the following UUIDs. Specify
`target_ids` multiple times in query parameter to build list of
candidates.
- **ip_like** (string, optional) [query]: Filters for targets whose IP addresses look like the specified string.
Supports `*` as a wildcard character
- **ipv4_start** (string, optional) [query]: Defines an IPv4 filter range's starting value (inclusive). Requires
`ipv4_end` to be specified as well.
- **ipv4_end** (string, optional) [query]: Defines an IPv4 filter range's ending value (inclusive). Requires
`ipv4_start` to be specified as well.
- **ipv6_start** (string, optional) [query]: Defines an IPv6 filter range's starting value (inclusive). Requires
`ipv6_end` to be specified as well.
- **ipv6_end** (string, optional) [query]: Defines an IPv6 filter range's ending value (inclusive). Requires
`ipv6_start` to be specified as well.
- **page** (integer, optional) [query]: Current page in the response
- **per_page** (integer, optional) [query]: Max amount of entries returned per page
- **order** (string, optional) [query]: The field to sort by.
- **direction** (string, optional) [query]: The sorting direction.

## Response

### 200

Successfully retrieved all targets in the account

- **result** (array, optional): 

### 4XX

Failed to retrieve all targets in the account

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
