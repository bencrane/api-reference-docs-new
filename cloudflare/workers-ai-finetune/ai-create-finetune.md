# Create a new Finetune

`POST /accounts/{account_id}/ai/finetunes`

Creates a new fine-tuning job for a Workers AI model using custom training data.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **model** (string, required): 
- **name** (string, required): 
- **public** (boolean, optional): 

## Response

### 200

Returns the created finetune

- **result** (object): 
- **success** (boolean): 

### 400

Finetune creation failed

- **errors** (array): 
- **success** (boolean):
