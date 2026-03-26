# Get BGP hijack events

`GET /radar/bgp/hijacks/events`

Retrieves the BGP hijack events.

## Parameters

- **page** (integer, optional) [query]: Current page number, starting from 1.
- **per_page** (integer, optional) [query]: Number of entries per page.
- **eventId** (integer, optional) [query]: The unique identifier of a event.
- **hijackerAsn** (integer, optional) [query]: The potential hijacker AS of a BGP hijack event.
- **victimAsn** (integer, optional) [query]: The potential victim AS of a BGP hijack event.
- **involvedAsn** (integer, optional) [query]: The potential hijacker or victim AS of a BGP hijack event.
- **involvedCountry** (string, optional) [query]: The country code of the potential hijacker or victim AS of a BGP hijack event.
- **prefix** (string, optional) [query]: 
- **minConfidence** (integer, optional) [query]: Filters events by minimum confidence score (1-4 low, 5-7 mid, 8+ high).
- **maxConfidence** (integer, optional) [query]: Filters events by maximum confidence score (1-4 low, 5-7 mid, 8+ high).
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
