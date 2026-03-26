# Create predefined entry

`POST /accounts/{account_id}/dlp/entries/predefined`

Predefined entries can't be created, this will update an existing predefined entry.
This is needed for our generated terraform API.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): 
- **entry_id** (string, required): 
- **profile_id** (string, optional): This field is not used as the owning profile.
For predefined entries it is already set to a predefined profile.

## Response

### 200

Create predefined entry response.

- **result** (object, optional): 

### 4XX

Create entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
