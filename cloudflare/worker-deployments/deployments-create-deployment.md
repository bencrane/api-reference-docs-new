# Create Deployment

`POST /accounts/{account_id}/workers/scripts/{script_name}/deployments`

Deployments configure how [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions) are deployed to traffic. A deployment can consist of one or two versions of a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 
- **force** (boolean, optional) [query]: If set to true, the deployment will be created even if normally blocked by something such rolling back to an older version when a secret has changed.

## Request Body

- **annotations** (object, optional): 
- **author_email** (string, optional): 
- **created_on** (string, required): 
- **id** (string, required): 
- **source** (string, required): 
- **strategy** (string, required):  Values: `percentage`
- **versions** (array, required): 

## Response

### 200

Create Deployment response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create Deployment response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
