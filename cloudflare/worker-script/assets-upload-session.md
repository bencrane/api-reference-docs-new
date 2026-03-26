# Create Assets Upload Session

`POST /accounts/{account_id}/workers/scripts/{script_name}/assets-upload-session`

Start uploading a collection of assets for use in a Worker version. To learn more about the direct uploads of assets, see https://developers.cloudflare.com/workers/static-assets/direct-upload/.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

- **manifest** (object, required): A manifest ([path]: {hash, size}) map of files to upload. As an example, `/blog/hello-world.html` would be a valid path key.

## Response

### 200

Create Assets Upload Session response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create Assets Upload Session response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
