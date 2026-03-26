# List videos

`GET /accounts/{account_id}/stream`

Lists up to 1000 videos from a single request. For a specific range, refer to the optional parameters.

## Parameters

- **account_id** (string, required) [path]: 
- **status** (string, optional) [query]: 
- **creator** (string, optional) [query]: 
- **type** (string, optional) [query]: 
- **asc** (string, optional) [query]: 
- **video_name** (string, optional) [query]: 
- **search** (string, optional) [query]: 
- **start** (string, optional) [query]: 
- **end** (string, optional) [query]: 
- **include_counts** (string, optional) [query]: 

## Response

### 200

List videos response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 
- **range** (integer, optional): The total number of remaining videos based on cursor position.
- **total** (integer, optional): The total number of videos that match the provided filters.

### 4XX

List videos response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
