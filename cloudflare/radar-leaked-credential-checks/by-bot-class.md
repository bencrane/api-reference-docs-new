# Get HTTP authentication requests by bot class summary

`GET /radar/leaked_credential_checks/summary/bot_class`

> **Deprecated**

Retrieves the distribution of HTTP authentication requests by bot class.

## Parameters

- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **dateRange** (array, optional) [query]: Filters results by date range. For example, use `7d` and `7dcontrol` to compare this week with the previous week. Use this parameter or set specific start and end dates (`dateStart` and `dateEnd` parameters).
- **dateStart** (array, optional) [query]: Start of the date range.
- **dateEnd** (array, optional) [query]: End of the date range (inclusive).
- **compromised** (array, optional) [query]: Filters results by compromised credential status (clean vs. compromised).
- **format** (string, optional) [query]: Format in which results will be returned.

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
