# Set Account Custom Nameserver Related Zone Metadata

`PUT /zones/{zone_id}/custom_ns`

> **Deprecated**

Set metadata for account-level custom nameservers on a zone.

If you would like new zones in the account to use account custom nameservers by default, use PUT /accounts/:identifier to set the account setting use_account_custom_ns_by_default to true.

Deprecated in favor of [Update DNS Settings](https://developers.cloudflare.com/api/operations/dns-settings-for-a-zone-update-dns-settings).


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): Whether zone uses account-level custom nameservers.
- **ns_set** (number, optional): The number of the name server set to assign to the zone.

## Response

### 200

Set Account Custom Nameserver Related Zone Metadata response

_Empty object_

### 4XX

Set Account Custom Nameserver Related Zone Metadata response failure

_Empty object_
