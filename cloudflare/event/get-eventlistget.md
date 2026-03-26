# Filter and list events

`GET /accounts/{account_id}/cloudforce-one/events`

When `datasetId` is unspecified, events will be listed from the `Cloudforce One Threat Events` dataset. To list existing datasets (and their IDs), use the [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/) endpoint). Also, must provide query parameters.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **cursor** (string, optional) [query]: 
- **search** (array, optional) [query]: 
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 
- **orderBy** (string, optional) [query]: 
- **order** (string, optional) [query]: 
- **datasetId** (array, optional) [query]: 
- **forceRefresh** (boolean, optional) [query]: 
- **format** (string, optional) [query]: 

## Response

### 200

Returns a list of events.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
