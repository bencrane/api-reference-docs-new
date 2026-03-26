# List Zaraz historical configuration records

`GET /zones/{zone_id}/settings/zaraz/history`

Lists a history of published Zaraz configuration records for a zone.

## Parameters

- **zone_id** (string, required) [path]: 
- **offset** (integer, optional) [query]: Ordinal number to start listing the results with. Default value is 0.
- **limit** (integer, optional) [query]: Maximum amount of results to list. Default value is 10.
- **sortField** (string, optional) [query]: The field to sort by. Default is updated_at.
- **sortOrder** (string, optional) [query]: Sorting order. Default is DESC.

## Response

### 200

List Zaraz historical configuration records response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (array, optional): 

### 4XX

List Zaraz historical configuration records failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
