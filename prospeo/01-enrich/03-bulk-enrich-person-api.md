# Bulk Enrich Person API

## Enrich up to 50 person records at once

This endpoint allows you to enrich multiple person's in one request while staying blazing-fast.

## How are credits spent?

Credit spending using this endpoints depends on the enrichment parameters you submit and the matches that are returned.

The credit system works in the same way as the unique Enrich Person endpoint, and it can be controlled in the same way (using `only_verified_email`, `enrich_mobile`, `only_verified_mobile`).

Please refer to the Enrich Person endpoint to understand how credits are spent.

## Endpoint

* **URL:** `https://api.prospeo.io/bulk-enrich-person`
* **Method:** `POST`
* **Headers:**
  * `X-KEY: your_api_key`
  * `Content-Type: application/json`

## Parameters

The parameters are the same as the unique Enrich Person endpoint, except for the `data` parameter.

| Parameter | Example value | Description |
|-----------|--------------|-------------|
| `only_verified_email` (optional) | `true` | Chose if you only want records with a verified email to be returned. Default is `false`. |
| `enrich_mobile` (optional) | `true` | Chose if you want to enrich the mobile (if it exists). |
| `only_verified_mobile` (optional) | `true` | Chose if you only want records with a mobile to be returned. Default is `false`. If `true`, `enrich_mobile` will automatically be `true`. |
| `data` (required) | See below | The records to enrich (up to 50 at once). See below for complete details. |

## Data parameter

The `data` parameter for the `/bulk-enrich-person` endpoint is a list of all the persons you wish to enrich.

The `data` parameter contains the datapoints you have for us to identify the record. We offer the following matching datapoints:

| Datapoint | Example value | Description |
|-----------|--------------|-------------|
| `identifier` (required) | 1234abcd | A random alpha-numeric string generated on your side to identify the specific matching object. This will be used when you parse the response, to attributes which data object represents which match in the response. |
| `first_name` (optional) | Roger | The first name of the person |
| `last_name` (optional) | Sterling | The last name of the person |
| `full_name` (optional) | Roger Sterling | The full name of the person |
| `linkedin_url` (optional) | https://www.linkedin.com/in/roger-sterling | The person's public LinkedIn URL |
| `email` (optional) | roger.sterling@deloitte.com | The work email of the person |
| `company_name` (optional) | Deloitte | The company name |
| `company_website` (optional) | deloitte.com | The company website |
| `company_linkedin_url` (optional) | https://linkedin.com/company/deloitte | The company's public LinkedIn URL |
| `person_id` (optional) | 6f745841665155f554e5f | If enriching from search: the ID of the person from the `/search-person` endpoint |

## Minimum requirements for matching

We require at a minimum the below datapoints together in one data object (allowing us to accurately identify the person):

* `first_name` + `last_name` + any of (`company_name`/`company_website`/`company_linkedin_url`)
* `full_name` + any of (`company_name`/`company_website`/`company_linkedin_url`)
* `linkedin_url`
* `email`
* `person_id` (enrich from `/search-person`)

**Important note #1:** We advise strongly against using only the `company_name` for matching. Many company have the same name, and this can result in mismatch/inaccurate results. Whenever possible, try to use at least the `company_website`.

**Important note #2:** the more datapoints you submit, the better, so whenever possible, submit everything you have for greater accuracy. For example, it is better to submit `company_website` and `company_linkedin_url` together rather than just one of them.

## Enrich records from our search API

Another way to enrich records is to use the `person_id` you get from the search results (`/search-person`) to this endpoint. This will identify the person and enrich as per your option (`only_verified_email`, `only_verified_mobile`, `enrich_mobile`).

## Example request

Whenever a parameter such as `only_verified_email`, it will apply to all of the object in the request.

We generated our own identifier (1,2,3,4,5,6,7) so that in case of a match, we can reconcile it with the response.

In the below request, the identifier 4 does not match the minimum matching requirements of a data object. Hence, this record will be ignored and provided in the `invalid_datapoints` list of the response.

We also enriched the identifier 7 by using its `person_id` we got from the `/search-person` endpoint.

```
POST "https://api.prospeo.io/bulk-enrich-person"
X-KEY: "your_api_key"
Content-Type: "application/json"

{
   "only_verified_email": true,
   "enrich_mobile": true,
   "data": [
       {
           "identifier": "1",
           "full_name": "Eva Kiegler",
           "company_website": "intercom.com"
       },
       {
           "identifier": "2",
           "first_name": "Jonah",
           "last_name": "Stones",
           "linkedin_url": "https://www.linkedin.com/in/jonah-stones",
           "company_name": "Deloitte",
           "company_website": "deloitte.com",
           "company_linkedin_url": "https://www.linkedin.com/company/deloitte"
       },
       {
           "identifier": "3",
           "linkedin_url": "https://www.linkedin.com/in/micah-sanders"
       },
       {
           "identifier": "4",
           "full_name": "Brandon Stering"
       },
       {
           "identifier": "5",
           "email": "nicolas.b@kpmg.com"
       },
       {
           "identifier": "6",
           "full_name": "Nicole Wonda",
           "company_linkedin_url": "https://www.linkedin.com/company/young"
       },
       {
           "identifier": "7",
           "person_id": "6f564548455488874f48e"
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
    "not_matched": ["2", "3"],
    "invalid_datapoints": ["4"],
    "matched": [
        {
            "identifier": "1",
            "person": {
                ...
            },
            "company": {
                ...
            }
        },
        {
            "identifier": "5",
            "person": {
                ...
            },
            "company": {
                ...
            }
        },
        {
            "identifier": "6",
            "person": {
                ...
            },
            "company": {
                ...
            }
        },
        {
            "identifier": "7",
            "person": {
                ...
            },
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
| `total_cost` | integer | Indicates the total cost of the request. It varies depending on the matches and the `enrich_mobile` option. |
| `matched` | list | This list contains all the matched records as per your requirements (`only_verified_email`, `only_verified_mobile`). |
| `matched.identifier` | string | This is the identifier you generated corresponding to the matched record. Use it to know which match is which. |
| `matched.person` | object | The matched person. |
| `matched.company` | object | The current company of the matched person. |
| `not_matched` | list | This list contains all the identifiers that we couldn't match given your requirements (`only_verified_email`, `only_verified_mobile`). |
| `invalid_datapoints` | list | This list contains all the identifiers that were not meeting our minimum requirements for matching, so matching wasn't attempted. |

## Error codes

| HTTP code | `error_code` property | Meaning |
|-----------|----------------------|---------|
| 400 | `INSUFFICIENT_CREDITS` | You do not have enough credit to perform the request. |
| 401 | `INVALID_API_KEY` | Invalid API key, check your `X-KEY` header. |
| 429 | `RATE_LIMITED` | You hit the rate limit for your current plan. |
| 400 | `INVALID_REQUEST` | The request your submitted is invalid. |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |