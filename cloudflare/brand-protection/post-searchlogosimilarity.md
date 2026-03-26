# Search scanned images

`POST /accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/search`

Submit an image and find the n closest matches from the scanned images index without creating any match records. Returns similarity scores and metadata for each match.

## Parameters

- **account_id** (string, required) [path]: 
- **showHistoric** (string, optional) [query]: Include scanned images without domain metadata (historic data). Default: false (only show images with domain)
- **download** (string, optional) [query]: If true, include base64-encoded image data in the response

## Request Body

- **image_data** (string, required): Base64 encoded image data. Can include data URI prefix (e.g., 'data:image/png;base64,...') or just the base64 string.
- **score_threshold** (number, optional): Minimum similarity score threshold for matches (0-1, default: 0)
- **top_k** (integer, optional): Number of closest matches to return (1-100, default: 10)

## Response

### 200

Scanned images search completed successfully

- **matches** (array):
