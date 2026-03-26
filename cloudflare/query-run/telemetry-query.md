# Run a query

`POST /accounts/{account_id}/workers/observability/telemetry/query`

Run a temporary or saved query.

## Request Body

- **chart** (boolean, optional): Whether to include timeseties data in the response
- **compare** (boolean, optional): Whether to include comparison data with previous time periods
- **dry** (boolean, optional): Whether to perform a dry run without saving the results of the query. Useful for validation
- **granularity** (number, optional): This is only used when the view is calculations. Leaving it empty lets Workers Observability detect the correct granularity.
- **ignoreSeries** (boolean, optional): Whether to ignore time-series data in the results and return only aggregated values
- **limit** (number, optional): Use this limit to cap the number of events returned when the view is events.
- **offset** (string, optional): Cursor pagination for event/trace/invocation views. Pass the last item's $metadata.id as the next offset.
- **offsetBy** (number, optional): Numeric offset for pattern results (top-N list). Use with limit to page pattern groups; not used by cursor pagination.
- **offsetDirection** (string, optional): Direction for offset-based pagination (e.g., 'next', 'prev')
- **parameters** (object, optional): Optional parameters to pass to the query execution
- **queryId** (string, required): Unique identifier for the query to execute
- **timeframe** (object, required): Timeframe for your query using Unix timestamps in milliseconds. Provide from/to epoch ms; narrower timeframes provide faster responses and more specific results.
- **view** (string, optional): Examples by view type. Events: show errors for a worker in the last 30 minutes. Calculations: p99 of wall time or count by status code. Invocations: find a specific request that resulted in a 500. Values: `traces`, `events`, `calculations`, `invocations`, `requests`, `agents`

## Response

### 200

Successful request

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 401

Unauthorized

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): 

### 500

Internal error

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
