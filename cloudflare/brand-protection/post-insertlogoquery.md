# Insert logo query

`POST /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries`

Create a new saved brand protection logo query for visual similarity matching

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **image_data** (string, required): Base64 encoded image data. Can include data URI prefix (e.g., 'data:image/png;base64,...') or just the base64 string.
- **search_lookback** (boolean, optional): If true, search historic scanned images for matches above the similarity threshold
- **similarity_threshold** (number, required): Minimum similarity score (0-1) required for visual matches
- **tag** (string, required): Unique identifier for the logo query

## Response

### 200

Logo query inserted successfully

- **message** (string): 
- **query_id** (integer): 
- **success** (boolean):
