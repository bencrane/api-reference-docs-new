# Cloudflare/JD Cloud IP Details

`GET /ips`

Get IPs used on the Cloudflare/JD Cloud network, see https://www.cloudflare.com/ips for Cloudflare IPs or https://developers.cloudflare.com/china-network/reference/infrastructure/ for JD Cloud IPs.

## Parameters

- **networks** (string, optional) [query]: Specified as `jdcloud` to list IPs used by JD Cloud data centers.

## Response

### 200

Cloudflare IP Details response

- **result** (object, optional): 

### 4XX

Cloudflare IP Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
