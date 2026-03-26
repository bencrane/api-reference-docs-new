# Update details about a dataset

`PUT /accounts/{account_id}/dlp/datasets/{dataset_id}`

Updates the configuration of an existing DLP dataset, such as its name, description, or detection settings.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 

## Request Body

- **case_sensitive** (boolean, optional): Determines if the words should be matched in a case-sensitive manner.

Only required for custom word lists.
- **description** (string, optional): The description of the dataset.
- **name** (string, optional): The name of the dataset, must be unique.

## Response

### 200

Dataset updated successfully.

- **result** (object, optional): 

### 4XX

Dataset update failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
