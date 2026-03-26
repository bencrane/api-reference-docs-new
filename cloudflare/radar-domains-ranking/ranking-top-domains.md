# Get top or trending domains

`GET /radar/ranking/top`

Retrieves the top or trending domains based on their rank. Popular domains are domains of broad appeal based on how people use the Internet. Trending domains are domains that are generating a surge in interest. For more information on top domains, see https://blog.cloudflare.com/radar-domain-rankings/.

## Parameters

- **limit** (integer, optional) [query]: Limits the number of objects returned in the response.
- **name** (array, optional) [query]: Array of names used to label the series in the response.
- **location** (array, optional) [query]: Filters results by location. Specify a comma-separated list of alpha-2 location codes.
- **domainCategory** (array, optional) [query]: Filters results by domain category.
- **date** (array, optional) [query]: Filters results by the specified array of dates.
- **rankingType** (string, optional) [query]: The ranking type.
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
