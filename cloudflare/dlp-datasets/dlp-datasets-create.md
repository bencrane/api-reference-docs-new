# Create a new dataset

`POST /accounts/{account_id}/dlp/datasets`

Creates a new DLP (Data Loss Prevention) dataset for storing custom detection patterns. Datasets can contain exact match data, word lists, or EDM (Exact Data Match) configurations.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **case_sensitive** (boolean, optional): Only applies to custom word lists.
Determines if the words should be matched in a case-sensitive manner
Cannot be set to false if `secret` is true or undefined
- **description** (string, optional): The description of the dataset.
- **encoding_version** (integer, optional): Dataset encoding version

Non-secret custom word lists with no header are always version 1.
Secret EDM lists with no header are version 1.
Multicolumn CSV with headers are version 2.
Omitting this field provides the default value 0, which is interpreted
the same as 1.
- **name** (string, required): 
- **secret** (boolean, optional): Generate a secret dataset.

If true, the response will include a secret to use with the EDM encoder.
If false, the response has no secret and the dataset is uploaded in plaintext.

## Response

### 200

Dataset created successfully.

- **result** (object, optional): 

### 4XX

Dataset creation failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
