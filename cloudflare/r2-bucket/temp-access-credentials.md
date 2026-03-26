# Create Temporary Access Credentials

`POST /accounts/{account_id}/r2/temp-access-credentials`

Creates temporary access credentials on a bucket that can be optionally scoped to prefixes or objects.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **bucket** (string, required): Name of the R2 bucket.
- **objects** (array, optional): Optional object paths to scope the credentials to.
- **parentAccessKeyId** (string, required): The parent access key id to use for signing.
- **permission** (string, required): Permissions allowed on the credentials. Values: `admin-read-write`, `admin-read-only`, `object-read-write`, `object-read-only`
- **prefixes** (array, optional): Optional prefix paths to scope the credentials to.
- **ttlSeconds** (number, required): How long the credentials will live for in seconds.

## Response

### 200

Create temporary access credentials response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Create temporary access credentials response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
