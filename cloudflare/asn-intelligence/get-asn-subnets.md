# Get ASN Subnets

`GET /accounts/{account_id}/intel/asn/{asn}/subnets`

Get ASN Subnets.

## Parameters

- **asn** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get ASN Subnets response.

- **asn** (integer): 
- **count** (number): Total results returned based on your search parameters.
- **ip_count_total** (integer): 
- **page** (number): Current page within paginated list of results.
- **per_page** (number): Number of results per page of results.
- **subnets** (array): 

### 4XX

Get ASN Subnets response failure.

- **asn** (integer, optional): 
- **count** (number, optional): Total results returned based on your search parameters.
- **ip_count_total** (integer, optional): 
- **page** (number, optional): Current page within paginated list of results.
- **per_page** (number, optional): Number of results per page of results.
- **subnets** (array, optional): 
- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
