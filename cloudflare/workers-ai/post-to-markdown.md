# Convert Files into Markdown

`POST /accounts/{account_id}/ai/tomarkdown`

Converts uploaded files into Markdown format using Workers AI.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Model Schema

- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
