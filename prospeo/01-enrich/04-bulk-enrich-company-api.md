# Bulk Enrich Company API

## Enrich up to 50 company records at once

This endpoint allows you to enrich multiple company's in one request while staying blazing-fast.

## How are credits spent?

One credit is spent per matched company.

You won't be charged if no results are found.

You won't be charged if you enrich the same record twice in the lifetime of your account.

## Endpoint

* **URL:** `https://api.prospeo.io/bulk-enrich-company`
* **Method:** `POST`
* **Headers:**
  * `X-KEY: your_api_key`
  * `Content-Type: application/json`

## Parameters

| Parameter | Example value | Description |
|-----------|--------------|-------------|
| `data` (required) | See below | The records to enrich (up to 50 at once). See below for complete details. |

## Data parameter

The `data` parameter for the `/bulk-enrich-company` endpoint is a list of all the companies you wish to enrich.

The `data` parameter contains the datapoints you have for us to identify the record. We offer the following matching datapoints:

| Datapoint | Example value | Description |
|-----------|--------------|-------------|
| `identifier` (required) | 1234abcd | A random alpha-numeric string generated on your side to identify the specific matching object. This will be used when you parse the response, to attributes which data object represents which match in the response. |
| `company_name` (optional) | Deloitte | The company name |
| `company_website` (optional) | deloitte.com | The company website |
| `company_linkedin_url` (optional) | https://linkedin.com/company/deloitte | The company's public LinkedIn URL |
| `company_id` (optional) | cccc7c7da6116a8830a07100 | The `company_id` from a previously enriched company object. You can use this to directly enrich a company by its ID. |

## Minimum requirements for matching

We require at least one of the above datapoints to accurately match a company.

**Important note #1:** We advise strongly against using only the `company_name` for matching. Many company have the same name, and this can result in mismatch/inaccurate results. Whenever possible, try to use at least the `company_website`.

**Important note #2:** the more datapoints you submit, the better, so whenever possible, submit everything you have for greater accuracy. For example, it is better to submit `company_website` and `company_linkedin_url` together rather than just one of them.

## Example request

We generated our own identifier (1,2,3,4,5) so that in case of a match, we can reconcile it with the response.

In the below request, the identifier 4 contains an property (`full_name`). Hence, this record will be ignored and provided in the `invalid_datapoints` list of the response.

```
POST "https://api.prospeo.io/bulk-enrich-company"
X-KEY: "your_api_key"
Content-Type: "application/json"

{
   "data": [
       {
           "identifier": "1",
           "company_website": "intercom.com"
       },
       {
           "identifier": "2",
           "company_linkedin_url": "https://www.linkedin.com/company/deloitte"
       },
       {
           "identifier": "3",
           "company_name": "Milka"
       },
       {
           "identifier": "4",
           "full_name": "Pinterest"
       },
       ... up to 50 objects
   ]
}
```

## Response

The response structure is as follow:

```json
{
    "error": false,
    "total_cost": 10,
    "not_matched": ["3"],
    "invalid_datapoints": ["4"],
    "matched": [
        {
            "identifier": "1",
            "company": {
                ...
            }
        },
        {
            "identifier": "2",
            "company": {
                ...
            }
        }
    ]
}
```

## Response details

| Property | Type | Description |
|----------|------|-------------|
| `error` | boolean | Indicates if an error has occurred. If `false`, the request was successful. If `true`, an error has occurred and a `error_code` property will be present. See below. |
| `total_cost` | integer | Indicates the total cost of the request. It varies depending on the matches. |
| `matched` | list | This list contains all the matched records. |
| `matched.identifier` | string | This is the identifier you generated corresponding to the matched record. Use it to know which match is which. |
| `matched.company` | object | The matched company. |
| `not_matched` | list | This list contains all the identifiers that we couldn't match. |
| `invalid_datapoints` | list | This list contains all the identifiers that were not meeting our minimum requirements for matching. |

## Error codes

| HTTP code | `error_code` property | Meaning |
|-----------|----------------------|---------|
| 400 | `INSUFFICIENT_CREDITS` | You do not have enough credit to perform the request. |
| 401 | `INVALID_API_KEY` | Invalid API key, check your `X-KEY` header. |
| 429 | `RATE_LIMITED` | You hit the rate limit for your current plan. |
| 400 | `INVALID_REQUEST` | The request your submitted is invalid. |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |