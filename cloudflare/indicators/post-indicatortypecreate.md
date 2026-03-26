# Create a new indicator type

`POST /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicatorTypes/create`

Creates a new indicator type and initializes its dedicated Durable Object

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset ID.

## Request Body

- **description** (string, optional): Optional description for the indicator type
- **indicatorType** (string, required): The indicator type to create (e.g., 'DOMAIN', 'IP', 'URL', 'HASH', 'EMAIL')

## Response

### 200

Indicator type created successfully

- **durableObjectId** (string): 
- **indicatorType** (string): 
- **message** (string): 

### 400

Bad Request

- **content** (object): 
- **description** (string): 

### 500

Internal Server Error

- **content** (object): 
- **description** (string):
