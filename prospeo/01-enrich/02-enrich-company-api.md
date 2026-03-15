# Enrich Company API

## Enrich a company

This endpoint allows you to enrich a company with its complete accurate B2B data.

**Important note:** When possible, it is recommended to use our Bulk Enrich Company endpoint instead for faster response time. It allows you to enrich up to 50 companies at once, instead of performing 50 individual requests.

## How are credits spent?

Enriching a company record cost 1 credit per match.

You won't be charged if no results are found.

You won't be charged if you enrich the same record twice in the lifetime of your account.

## Endpoint

* **URL:** `https://api.prospeo.io/enrich-company`
* **Method:** `POST`
* **Headers:**
  * `X-KEY: your_api_key`
  * `Content-Type: application/json`

## Parameters

| Parameter | Example value | Description |
|-----------|--------------|-------------|
| `data` (required) | See below | The company to enrich. See below for complete details. |

## Data parameter

The `data` parameter contains the datapoints you have for us to identify the company. We offer the following matching datapoints:

| Datapoint | Example value | Description |
|-----------|--------------|-------------|
| `company_website` (optional) | deloitte.com | The company website. |
| `company_linkedin_url` (optional) | https://linkedin.com/company/deloitte | The company's LinkedIn URL. |
| `company_name` (optional) | Deloitte | The company name. We discourage using solely the company name for enrichment, as many company have the same name. Prioritize the `company_website` or `company_linkedin_url`. |
| `company_id` (optional) | cccc7c7da6116a8830a07100 | The `company_id` from a previously enriched company object. You can use this to directly enrich a company by its ID. |

## Minimum requirements for matching

We require at least one of the above datapoints to accurately match a company.

**Important note #1:** We advise strongly against using only the `company_name` for matching. Many company have the same name, and this can result in mismatch/inaccurate results. Whenever possible, try to use at least the `company_website`.

**Important note #2:** the more datapoints you submit, the better, so whenever possible, submit everything you have for greater accuracy. For example, it is better to submit `company_website` and `company_linkedin_url` together rather than just one of them.

## Example request

Simple request that always returns a result if a company is matched.

In this example, we used the `company_website`. This request will perform better than a request with only the `company_name`.

```
POST "https://api.prospeo.io/enrich-company"
X-KEY: "your_api_key"
Content-Type: "application/json"

{
   "data": {
       "company_website": "intercom.com"
   }
}
```

## Response

This response contains all the possible fields and their example value. When a field is unavailable, it will be `null`.

```json
{
    "error": false,
    "free_enrichment": false,
    "company": {
        "company_id": "cccc7c7da6116a8830a07100",
        "name": "Intercom",
        "website": "https://intercom.com",
        "domain": "intercom.io",
        "other_websites": [],
        "description": "Intercom is the only complete AI-first customer service platform, enhancing the customer experience, improving operational efficiency, and scaling with your business every step of the way.",
        "description_seo": "Intercom is the complete AI-first customer service solution, giving exceptional experiences for support teams with AI agent, AI copilot, tickets, phone & more",
        "description_ai": "Intercom is an AI-first customer service solution that provides exceptional experiences for support teams with AI agent, AI copilot, tickets, phone, and more.",
        "type": "Private",
        "industry": "Software Development",
        "employee_count": 1822,
        "employee_count_on_prospeo": 437,
        "employee_range": "1001-2000",
        "location": {
            "country": "United States",
            "country_code": "US",
            "state": "California",
            "city": "San Francisco",
            "raw_address": "55 2nd Street, 4th Floor, San Francisco, California 94105, US"
        },
        "sic_codes": ["737"],
        "naics_codes": [],
        "email_tech": {
            "domain": "intercom.io",
            "mx_provider": "Google"
        },
        "linkedin_url": "https://www.linkedin.com/company/intercom",
        "twitter_url": "https://x.com/intercom",
        "facebook_url": "https://www.facebook.com/intercominc",
        "crunchbase_url": "https://www.crunchbase.com/organization/intercom",
        "instagram_url": "https://www.instagram.com/intercom",
        "youtube_url": "https://www.youtube.com/c/@intercominc",
        "phone_hq": {
            "phone_hq": "+14156733820",
            "phone_hq_national": "(415) 673-3820",
            "phone_hq_international": "+14156733820",
            "phone_hq_country": "United States",
            "phone_hq_country_code": "US"
        },
        "linkedin_id": null,
        "founded": 2011,
        "revenue_range": {
            "min": 100000000,
            "max": 250000000
        },
        "revenue_range_printed": "100M",
        "keywords": [
            "Customer Support",
            "Live Chat",
            "Marketing Automation",
            "Customer Relationship Management",
            "Customer Experience",
            "Customer Engagement",
            "Customer Service",
            "Mobile",
            "Customer Feedback",
            "AI",
            "Helpdesk",
            "CX",
            "Chat Bots",
            "Customer Communication",
            "Support Automation",
            "Shared Inbox"
        ],
        "logo_url": "https://prospeo-static-assets.s3.us-east-1.amazonaws.com/company_logo/9ded0364-c88a-4789-9d39-2a15ed239edb.jpg",
        "attributes": {
            "is_b2b": true,
            "has_demo": false,
            "has_free_trial": true,
            "has_downloadable": false,
            "has_mobile_apps": false,
            "has_online_reviews": true,
            "has_pricing": true
        },
        "funding": {
            "count": 2,
            "total_funding": 125000000,
            "total_funding_printed": "$125.0M",
            "latest_funding_date": "2021-01-01T00:00:00",
            "latest_funding_stage": "Series unknown",
            "funding_events": [
                {
                    "amount": null,
                    "amount_printed": null,
                    "raised_at": "2021-01-01T00:00:00",
                    "stage": "Series unknown",
                    "link": "https://www.crunchbase.com/funding_round/intercom-series-unknown--6ce20dfb"
                },
                {
                    "amount": 125000000,
                    "amount_printed": "$125,000,000",
                    "raised_at": "2018-04-27T00:00:00",
                    "stage": "Series D",
                    "link": "https://www.crunchbase.com/funding_round/intercom-series-d--15490ce6"
                }
            ]
        },
        "technology": {
            "count": 43,
            "technology_names": [
                "6sense",
                "theTradeDesk",
                "Amazon SES",
                "Contentful",
                "Node.js",
                "Tailwind CSS"
            ],
            "technology_list": [
                {
                    "name": "6sense",
                    "category": "Marketing automation"
                },
                {
                    "name": "theTradeDesk",
                    "category": "Advertising"
                },
                {
                    "name": "Amazon SES",
                    "category": "Email"
                },
                {
                    "name": "Contentful",
                    "category": "CMS"
                }
            ]
        },
        "job_postings": {
            "active_count": 3,
            "active_titles": [
                "account executive, senior midmarket",
                "senior product engineer",
                "senior recruiting coordinator"
            ]
        }
    }
}
```

## Response details

| Property | Type | Description |
|----------|------|-------------|
| `error` | boolean | Indicates if an error has occurred. If `false`, the request was successful. If `true`, an error has occurred and a `error_code` property will be present. See below. |
| `free_enrichment` | boolean | Indicates whether you were charged. This will be `true` if you enriched the record in the past. |
| `company` | object | The matched company. |

## Error codes

| HTTP code | `error_code` property | Meaning |
|-----------|----------------------|---------|
| 400 | `NO_MATCH` | We couldn't match the data you provided with a company record. |
| 400 | `INSUFFICIENT_CREDITS` | You do not have enough credit to perform the request. |
| 401 | `INVALID_API_KEY` | Invalid API key, check your `X-KEY` header. |
| 429 | `RATE_LIMITED` | You hit the rate limit for your current plan. |
| 400 | `INVALID_REQUEST` | The request your submitted is invalid. |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |