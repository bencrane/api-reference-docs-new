# Disable Email Routing

`DELETE /zones/{zone_id}/email/routing/dns`

Disable your Email Routing zone. Also removes additional MX records previously required for Email Routing to work.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): Domain of your zone.

## Response

### 200

Disable Email Routing response

Type: object
