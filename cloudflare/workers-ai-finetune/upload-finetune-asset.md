# Upload a Finetune Asset

`POST /accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets`

Uploads training data assets for a Workers AI fine-tuning job.

## Parameters

- **account_id** (string, required) [path]: 
- **finetune_id** (string, required) [path]: 


## Response

### 200

Returns successfully if finetunes were uploaded

- **success** (boolean): 

### 400

Finetune creation failed

- **errors** (array): 
- **success** (boolean):
