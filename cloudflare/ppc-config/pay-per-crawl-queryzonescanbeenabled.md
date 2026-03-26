# Gets the can_be_enabled zone setting

`POST /accounts/{account_id}/pay-per-crawl/zones_can_be_enabled/query`

Provided a list of pay-per-crawl configured zones this method will return whether they can enable PPC or not.

## Parameters

- **account_id** (string, required) [path]: account id

## Request Body

- **zones** (array, optional): 

## Response

### 200

OK

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
