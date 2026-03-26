# Aggregate events by single or multiple columns with optional date filtering

`GET /accounts/{account_id}/cloudforce-one/events/aggregate`

Aggregate threat events by one or more columns (e.g., attacker, targetIndustry) with optional date filtering and daily grouping. Supports multi-dimensional aggregation for cross-analysis.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **aggregateBy** (string, required) [query]: Column(s) to aggregate by - single column or comma-separated list (e.g., 'attacker', 'targetIndustry', 'attacker,targetIndustry')
- **datasetId** (array, optional) [query]: Dataset ID(s) to filter by. Can be a single dataset ID, comma-separated list, or array. If not provided, uses default dataset
- **startDate** (string, optional) [query]: Start date for filtering (ISO 8601 format, e.g., '2024-01-01')
- **endDate** (string, optional) [query]: End date for filtering (ISO 8601 format, e.g., '2024-12-31')
- **groupByDate** (boolean, optional) [query]: Whether to group results by date (daily aggregation)
- **limit** (number, optional) [query]: Maximum number of results to return

## Response

### 200

Returns aggregated event data.

- **aggregateBy** (string): Column(s) that were aggregated by
- **aggregations** (array): Array of aggregation results with dynamic fields based on aggregateBy columns
- **dateRange** (object): Date range used for filtering
- **total** (number): Total number of events in the aggregation

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
