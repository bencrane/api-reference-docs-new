# Create authenticated direct upload URL V2

`POST /accounts/{account_id}/images/v2/direct_upload`

Direct uploads allow users to upload images without API keys. A common use case are web apps, client-side applications, or mobile devices where users upload content directly to Cloudflare Images. This method creates a draft record for a future image. It returns an upload URL and an image identifier. To verify if the image itself has been uploaded, send an image details request (accounts/:account_identifier/images/v1/:identifier), and check that the `draft: true` property is not present.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Create authenticated direct upload URL V2 response

- **result** (object, optional): 

### 4XX

Create authenticated direct upload URL V2 response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
