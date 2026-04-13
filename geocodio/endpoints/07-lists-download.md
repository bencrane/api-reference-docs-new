# Download a Geocoded List | Geocodio API

## Overview

Download a fully processed geocoding list as a UTF-8 encoded, comma-separated CSV file. The response may include an HTTP redirect, so configure your HTTP client to follow redirects.

## Endpoint

```
GET https://api.geocod.io/v1.12/lists/{id}/download
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The list ID (path parameter) |
| `api_key` | string | Yes | Your Geocodio API key |

## Example Request

```bash
curl -L "https://api.geocod.io/v1.12/lists/42/download?api_key=YOUR_API_KEY"
```

Note the `-L` flag to follow redirects.

## Example Response (CSV)

The response is a CSV file with the original columns plus appended geocoding data:

```
address,city,state,zip,Latitude,Longitude,"Accuracy Score","Accuracy Type",Number,Street,"Unit Type","Unit Number",City,State,County,Zip,Country,Source
"660 Pennsylvania Ave SE",Washington,DC,20003,38.885172,-76.996565,1,rooftop,660,"Pennsylvania Ave SE",,,Washington,DC,"District of Columbia",20003,US,Statewide
"1718 14th St NW",Washington,DC,20009,38.913274,-77.032266,1,rooftop,1718,"14th St NW",,,Washington,DC,"District of Columbia",20009,US,Statewide
"1309 5th St NE",,,20002,38.908724,-76.997653,0.9,rooftop,1309,"5th St NE",,,Washington,DC,"District of Columbia",20002,US,Statewide
```

## Error Response (Still Processing)

If the list has not finished processing, the endpoint returns:

```json
{
  "message": "List is still processing",
  "success": false
}
```

## Notes

- The response may be a redirect HTTP header. Always configure your HTTP client to follow redirects.
- Results are only available when the list status is `COMPLETED`.
- Data is automatically deleted 72 hours after processing completes.
