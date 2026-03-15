# Search Company API

## Search for companies

This endpoint allows you to perform a precise search against our extensive up-to-date database of companies and build account lists.

We offer more than 20 filters that can be used to craft your perfect company list.

In order to keep Prospeo's infrastructure efficient, the maximum amount of results you can pull using this API is 25,000 (1000 pages of 25 results).

## How are credits spent?

1 credit is spent per search request that returns at least one company.

There are 25 results per page, hence 1 credit is spent for a maximum of 25 results.

## Endpoint

* **URL:** `https://api.prospeo.io/search-company`
* **Method:** `POST`
* **Headers:**
  * `X-KEY: your_api_key`
  * `Content-Type: application/json`

## Parameters

| Parameter | Example value | Description |
|-----------|--------------|-------------|
| `filters` (required) | `true` | The complete filter configuration you want to use. See the Filters Documentation or the filter section below for all details. |
| `page` (optional) | `true` | The page you want to query for your search. Always defaults to 1 if no page is used. |

## How to perform a search?

There are two ways to build your search filters:

* **Dashboard UI helper** - Use our dashboard to visually build your search and export the JSON payload (described below)
* **Filters Documentation** - Refer to our complete Filters Documentation for all available filters and their values

### Using the dashboard helper

**Step 1**

Head to our dashboard and build a company search with various filters (ensure to be on the company search page).

**Step 2**

Click on the `...` in the top-right corner of the search results, and click on `API JSON`.

**Step 3**

A modal will open with the current search payload you built. By using this tool, you can understand what filters does what, and how it is represented through the API.

**Step 4**

You can copy the payload and directly re-use it in your request. Here is the example of a request for quick understanding:

```bash
curl --location 'https://api.prospeo.io/search-company' \
--header 'X-KEY: api-key' \
--header 'Content-Type: application/json' \
--data '{
    "page": 1,
    "filters": {
        "company_industry": {
            "exclude": [
                "Semiconductors",
                "Pet Services"
            ]
        },
        "company_funding": {
            "stage": [
                "Series B",
                "Series C"
            ],
            "funding_date": 365,
            "last_funding": {
                "min": "1M",
                "max": "10M"
            },
            "total_funding": {
                "min": "10M",
                "max": "100M"
            }
        }
    }
}'
```

## Response

The response will contain the results.

Each result will contain a `company` object (see the Company object page for the complete schema).

```json
{
    "error": false,
    "results": [
        {
            "company": ...
        },
        {
            "company": ...
        },
        {
            "company": ...
        },
        ... up to 25 per page
    ],
    "pagination": {
        "current_page": 1,
        "per_page": 25,
        "total_page": 11,
        "total_count": 271
    }
}
```

Example of a failed request:

```json
{
    "error": true,
    "error_code": "INVALID_FILTERS",
    "filter_error": "The value `Accountingg` is not supported for the filter `company_industry`."
}
```

**Final note:**

There are additional search filters available through our API that are not available on the dashboard. Those are: `company.names` and `company.websites`. They allow you to pre-filter on a list of companies.

Due to technical limitation, there are a few filters on the dashboard search that are unavailable through our public API. Those filters are: `company_intent`, `company.company_oids`, `company.company_list_oids`, `company.temp_matching_oids`

## Paginate the results

You can use the `page` parameter to go paginate the complete result set. The maximum pages is always 1000 when using our API. Use the `pagination` in response to see how many pages exists.

## Response details

| Property | Type | Description |
|----------|------|-------------|
| `error` | boolean | Indicates if an error has occurred. If `false`, the request was successful. If `true`, an error has occurred and a `error_code` property will be present. See below. |
| `results` | list | Contains the current page of results. Up to 25 records per page. |
| `pagination` | object | Contains the information about the pagination. Use it to know if you can turn to the next page. |

## Error codes

| HTTP code | `error_code` property | Meaning |
|-----------|----------------------|---------|
| 400 | `INVALID_FILTERS` | The filter configuration you used is not supported. See the `filter_error` property for more details. |
| 400 | `NO_RESULTS` | There was no results matching your filters. |
| 400 | `INSUFFICIENT_CREDITS` | You do not have enough credit to perform the request. |
| 401 | `INVALID_API_KEY` | Invalid API key, check your `X-KEY` header. |
| 429 | `RATE_LIMITED` | You hit the rate limit for your current plan. |
| 400 | `INVALID_REQUEST` | The request your submitted is invalid. |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |

## Filters

To understand how to use our filters, you have two options:

* **Filters Documentation** - Refer to our complete Filters Documentation for all available filters, their types, and accepted values.
* **Dashboard UI** - Use our dashboard UI as described above to visually build your search and see the generated payload.

Keep in mind that it is not allowed to perform a search solely with exclude filters for performance reasons.

### Search from a list of company websites or names

There is no option in the UI builder to search using a list of company websites or names. This API still allows you to perform searches using those elements.

The maximum size is 500 websites or names at once.

```json
{
    "page": 1,
    "filters": {
        "company": {
            "websites": {
                "include": [
                    "deloitte.com",
                    "https://facebook.com/"
                ]
            },
            "names": {
                "include": [
                    "Walmart",
                    "Microsoft"
                ]
            }
        }
    }
}
```

### ENUM filter values

Many filters are linked to an ENUM, which means that we accept a set list of values.

Below is the list of all the values allowed per filter:

* `company_industries`: Industries
* `company_headcount_range`: Employee ranges
* `company_funding`: Funding stages
* `company_technology`: Technologies
* `company_email_provider`: MX providers
* `company_naics`: NAICS codes
* `company_sics`: SIC codes

### Location filter values

As it can be seen on the dashboard, the `company_location` filter takes strings as values.

In order to ensure accuracy, the location strings you submit must match exactly the one you can pull from the dashboard.

We do not accept arbitrary location string such as "nyc".

**Programmatic access:** Use our Search Suggestions API to programmatically retrieve valid location values. This endpoint allows you to search for locations and get properly formatted strings that can be used directly in your filters.

Alternatively, build a list of location by inserting them on the filter on the dashboard, look at the generated payload, and re-use those values.