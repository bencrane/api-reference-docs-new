# Update a Priority Intelligence Requirement

`PUT /accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **priority_id** (string, required) [path]: 

## Request Body

- **labels** (array, required): List of labels.
- **priority** (integer, required): Priority.
- **requirement** (string, required): Requirement.
- **tlp** (string, required): The CISA defined Traffic Light Protocol (TLP). Values: `clear`, `amber`, `amber-strict`, `green`, `red`

## Response

### 200

Update priority response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update priority response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
