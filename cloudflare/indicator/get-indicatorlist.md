# Lists indicators across multiple datasets

`GET /accounts/{account_id}/cloudforce-one/events/indicators`

Retrieves a paginated list of indicators across specified datasets. Use datasetIds=all or datasetIds=* to query all datasets for the account. If no datasetIds provided, uses the default dataset.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **datasetIds** (array, optional) [query]: Dataset IDs to query indicators from (array of UUIDs), or special value 'all' or '*' to query all datasets. If not provided, uses the default dataset.
- **page** (number, optional) [query]: 
- **pageSize** (number, optional) [query]: 
- **search** (array, optional) [query]: Structured search as a JSON array of {field, op, value} objects. Searchable fields: value, indicatorType. Supports operators: equals, not, contains, startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use the 'in' operator with an array value to bulk-check up to 100 indicators in a single request, e.g. search=[{"field":"value","op":"in","value":["evil.com","bad.org"]}]. Multiple conditions are AND'd together. Max 10 conditions per request.
- **name** (string, optional) [query]: Filter indicators by value using substring match (LIKE). Legacy alternative to structured search.
- **indicatorType** (string, optional) [query]: 
- **relatedEvents** (array, optional) [query]: Filter by related event IDs
- **tags** (array, optional) [query]: Filter by tag values or UUIDs. Indicators must have at least one of the specified tags (OR logic). Supports both tag UUID and tag value.
- **createdAfter** (string, optional) [query]: Filter indicators created on or after this date. Must use ISO 8601 format (e.g., '2024-01-15T00:00:00Z').
- **createdBefore** (string, optional) [query]: Filter indicators created on or before this date. Must use ISO 8601 format (e.g., '2024-12-31T23:59:59Z').
- **relatedEventsLimit** (number, optional) [query]: Limit the number of related events returned per indicator. Default: 2. Set to 0 for none, -1 for all events.
- **includeTags** (boolean, optional) [query]: Whether to include full tag details for each indicator. Defaults to true.
- **includeTotalCount** (boolean, optional) [query]: Whether to compute accurate total count via COUNT(*). Defaults to false for performance. When false, total_count is an approximation.
- **format** (string, optional) [query]: Output format for indicator data. 'json' returns the default format, 'stix2' returns STIX 2.1 Indicator SDOs.

## Response

### 200

Returns a paginated list of indicators.

- **properties** (object): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
