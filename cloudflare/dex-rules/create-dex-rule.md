# Create a DEX Rule

`POST /accounts/{account_id}/dex/rules`

Create a DEX Rule

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path

## Request Body

- **description** (string, optional): 
- **match** (string, required): The wirefilter expression to match.
- **name** (string, required): The name of the Rule.

## Response

### 200

success response

- **result** (object, optional): 

### 4XX

Create DEX Rule failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
