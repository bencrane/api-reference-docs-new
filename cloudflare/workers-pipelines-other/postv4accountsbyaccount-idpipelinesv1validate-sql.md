# Validate SQL

`POST /accounts/{account_id}/pipelines/v1/validate_sql`

Validate Arroyo SQL.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **sql** (string, required): Specifies SQL to validate.

## Response

### 200

Indicates SQL validation success.

- **result** (object): 
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates SQL validation failed.
