# Delete (reset) DLP account-level settings to initial values.

`DELETE /accounts/{account_id}/dlp/settings`



## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

DLP settings reset.

- **result** (object, optional): DLP account-level settings response.

### 4XX

Failed to delete DLP settings.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
