# Generate fallthrough WAF expression template from a set of API hosts

`POST /zones/{zone_id}/api_gateway/expression-template/fallthrough`

Creates an expression template fallthrough rule for API Shield. Used for configuring default behavior when no other expression templates match.

## Request Body

- **hosts** (array, required): List of hosts to be targeted in the expression

## Response

### 200

Generate fallthrough WAF expression template response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Generate fallthrough WAF expression template failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
