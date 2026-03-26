# Create a New Priority Intelligence Requirement

`POST /accounts/{account_id}/cloudforce-one/requests/priority/new`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **labels** (array, required): List of labels.
- **priority** (integer, required): Priority.
- **requirement** (string, required): Requirement.
- **tlp** (string, required): The CISA defined Traffic Light Protocol (TLP). Values: `clear`, `amber`, `amber-strict`, `green`, `red`

## Response

### 200

Create priority response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create priority response  failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
