# Create a rate limit

`POST /zones/{zone_id}/rate_limits`

> **Deprecated**

Creates a new rate limit for a zone. Refer to the object definition for a list of required attributes.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **action** (object, required): The action to perform when the threshold of matched traffic within the configured period is exceeded.
- **match** (object, required): Determines which traffic the rate limit counts towards the threshold.
- **period** (number, required): The time in seconds (an integer value) to count matching traffic. If the count exceeds the configured threshold within this period, Cloudflare will perform the configured action.
- **threshold** (number, required): The threshold that will trigger the configured mitigation action. Configure this value along with the `period` property to establish a threshold per period.

## Response

### 200

Create a rate limit response.

- **result** (object, optional): 

### 4XX

Create a rate limit response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
