# Lists indicators

`GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/indicators`

> **Deprecated**

This method is deprecated. Please use /events/indicators to retrieve a paginated list of indicators.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 
- **name** (string, optional) [query]: Filter by indicator value (substring match)
- **indicatorType** (string, optional) [query]: 
- **relatedEvent** (array, optional) [query]: Filter indicators by related event UUID(s). Multiple UUIDs can be provided by repeating the parameter.

## Response

### 200

Returns a list of indicators.

- **indicators** (array): 
- **pagination** (object):
