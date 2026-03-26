# Get logs received

`GET /zones/{zone_id}/logs/received`

The `/received` api route allows customers to retrieve their edge HTTP logs. The basic access pattern is "give me all the logs for zone Z for minute M", where the minute M refers to the time records were received at Cloudflare's central data center. `start` is inclusive, and `end` is exclusive. Because of that, to get all data, at minutely cadence, starting at 10AM, the proper values are: `start=2018-05-20T10:00:00Z&end=2018-05-20T10:01:00Z`, then `start=2018-05-20T10:01:00Z&end=2018-05-20T10:02:00Z` and so on; the overlap will be handled properly.

## Parameters

- **zone_id** (string, required) [path]: 
- **start** (string, optional) [query]: 
- **end** (string, required) [query]: 
- **fields** (string, optional) [query]: 
- **sample** (string, optional) [query]: 
- **count** (string, optional) [query]: 
- **timestamps** (string, optional) [query]: 

## Response

### 200

Get logs received response

Type: object

### 4XX

Get logs received response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
