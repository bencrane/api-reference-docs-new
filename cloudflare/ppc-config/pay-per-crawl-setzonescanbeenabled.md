# Set can_be_enabled setting on zones

`PATCH /accounts/{account_id}/pay-per-crawl/zones_can_be_enabled`

Allows an account admin to set the can_be_enabled setting on a list of zones.

## Parameters

- **account_id** (string, required) [path]: account id

## Request Body

- **zones** (array, optional): 

## Response

### 200

OK

- **errors** (array): 
- **messages** (array): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
