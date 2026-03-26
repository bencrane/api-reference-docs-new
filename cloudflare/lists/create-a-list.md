# Create a list

`POST /accounts/{account_id}/rules/lists`

Creates a new list of the specified kind.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): An informative summary of the list.
- **kind** (enum, required): The type of the list. Each type supports specific list items (IP addresses, ASNs, hostnames or redirects). Values: `ip`, `redirect`, `hostname`, `asn`
- **name** (string, required): An informative name for the list. Use this name in filter and rule expressions.

## Response

### 200

Create a list response.

_Empty object_

### 4XX

Create a list response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
