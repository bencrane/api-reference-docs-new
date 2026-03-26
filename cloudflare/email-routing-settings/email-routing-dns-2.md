# Enable Email Routing

`POST /zones/{zone_id}/email/routing/dns`

Enable you Email Routing zone. Add and lock the necessary MX and SPF records.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): Domain of your zone.

## Response

### 200

Enable Email Routing response

- **result** (object, optional):
