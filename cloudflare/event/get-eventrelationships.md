# Filter and list events related to specific event

`GET /accounts/{account_id}/cloudforce-one/events/{event_id}/relationships`

The `event_id` must be defined (to list existing events (and their IDs), use the [`Filter and List Events`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/) endpoint). Also, must provide query parameters.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **event_id** (string, required) [path]: Event UUID.
- **direction** (string, optional) [query]: The direction to traverse the graph. Defaults to 'both' to search all.
- **maxDepth** (number, optional) [query]: The maximum depth to traverse. Defaults to 5.
- **relationshipTypes** (string, optional) [query]: An optional array of relationship types to filter by.
- **indicatorTypeIds** (array, optional) [query]: An optional array of indicator type IDs to filter the results by.
- **datasetId** (string, required) [query]: The dataset ID to search within.
- **includeParent** (boolean, optional) [query]: Whether to include the starting event in the results. Defaults to true.
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 

## Response

### 200

Returns a list of events related to the specified starting event.

Type: array

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
