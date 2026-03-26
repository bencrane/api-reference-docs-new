# Unlock Email Routing

`PATCH /zones/{zone_id}/email/routing/dns`

Unlock MX Records previously locked by Email Routing.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): Domain of your zone.

## Response

### 200

Unlock Email Routing MX records

- **result** (object, optional):
