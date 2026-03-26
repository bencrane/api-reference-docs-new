# Change Origin Max HTTP Version Setting

`PATCH /zones/{zone_id}/settings/origin_max_http_version`

Origin Max HTTP Setting Version sets the highest HTTP version Cloudflare will attempt to use with your origin. This setting allows Cloudflare to make HTTP/2 requests to your origin. (Refer to [Enable HTTP/2 to Origin](https://developers.cloudflare.com/cache/how-to/enable-http2-to-origin/), for more information.). The default value is "2" for all plan types except Enterprise where it is "1".

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Value of the Origin Max HTTP Version Setting. Values: `2`, `1`

## Response

### 200

Change Origin Max HTTP Version setting response.

_Empty object_

### 4XX

Change Origin Max HTTP Version response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
