# Request Trace

`POST /accounts/{account_id}/request-tracer/trace`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **body** (object, optional): 
- **context** (object, optional): Additional request parameters
- **cookies** (object, optional): Cookies added to tracing request
- **headers** (object, optional): Headers added to tracing request
- **method** (string, required): HTTP Method of tracing request
- **protocol** (string, optional): HTTP Protocol of tracing request
- **skip_response** (boolean, optional): Skip sending the request to the Origin server after all rules evaluation
- **url** (string, required): URL to which perform tracing request

## Response

### 200

Request Trace response

_Empty object_

### 4XX

Request Trace response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
