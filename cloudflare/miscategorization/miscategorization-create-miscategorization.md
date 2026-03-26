# Create Miscategorization

`POST /accounts/{account_id}/intel/miscategorization`

Allows you to submit requests to change a domain’s category.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **content_adds** (array, optional): Content category IDs to add.
- **content_removes** (array, optional): Content category IDs to remove.
- **indicator_type** (string, optional):  Values: `domain`, `ipv4`, `ipv6`, `url`
- **ip** (string, optional): Provide only if indicator_type is `ipv4` or `ipv6`.
- **security_adds** (array, optional): Security category IDs to add.
- **security_removes** (array, optional): Security category IDs to remove.
- **url** (string, optional): Provide only if indicator_type is `domain` or `url`. Example if indicator_type is `domain`: `example.com`. Example if indicator_type is `url`: `https://example.com/news/`.

## Response

### 200

Create Miscategorization response.

_Empty object_

### 4XX

Create Miscategorization response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
