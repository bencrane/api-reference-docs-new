# Get BGP route leak events

`GET /radar/bgp/leaks/events`

Retrieves the BGP route leak events.

## Parameters

- **page** (integer, optional) [query]: Current page number, starting from 1.
- **per_page** (integer, optional) [query]: Number of entries per page.
- **eventId** (integer, optional) [query]: The unique identifier of a event.
- **leakAsn** (integer, optional) [query]: The leaking AS of a route leak event.
- **involvedAsn** (integer, optional) [query]: ASN that is causing or affected by a route leak event.
- **involvedCountry** (string, optional) [query]: Country code of a involved ASN in a route leak event.
- **dateRange** (string, optional) [query]: Filters results by date range.
- **dateStart** (string, optional) [query]: Start of the date range (inclusive).
- **dateEnd** (string, optional) [query]: End of the date range (inclusive).
- **sortBy** (string, optional) [query]: Sorts results by the specified field.
- **sortOrder** (string, optional) [query]: Sort order.
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
