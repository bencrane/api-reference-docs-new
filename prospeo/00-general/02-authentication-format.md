# Authentication Format

# Authentication Format

## Authentication

To authenticate with the Prospeo API, add the header `X-KEY` to your request.

You can find your API key on your dashboard. You have the ability to create multiple API keys.

## Request

The host is `api.prospeo.io`

All requests should be made with HTTPS

All of our endpoints accept the POST method only

You are required to add the header `Content-Type: application/json`

Below are minimal example of our Enrich Person API.

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "X-KEY: your_api_key" \
  -d '{
        "only_verified_email": true,
        "enrich_mobile": false,
        "data": {
            "first_name": "John",
            "last_name": "Doe",
            "company_website": "intercom.com"
        }
    }' \
  "https://api.prospeo.io/enrich-person"
```

## Response

Read the error handling section of the endpoint page you need to handle errors.

All the response will be in JSON.

Each response will always contain an `error` property: `false` if the request was successful, `true` otherwise

Response codes:

* `200` : Valid request
* `400` : An error occurred
* `401` : Invalid API key
* `429` : Rate limit exceeded

### Example of a successful response (Enrich Person API)

This response contains a revealed mobile (`enrich_mobile:true`).

```json
{
    "error": false,
    "free_enrichment": false,
    "person": {
        "person_id": "aaaacd817619fba3d254cd64",
        "first_name": "Eoghan",
        "last_name": "Mccabe",
        "full_name": "Eoghan Mccabe",
        "linkedin_url": "https://www.linkedin.com/in/eoghanmccabe",
        "current_job_title": "CEO, chairman, and co-founder",
        "current_job_key": null,
        "headline": "CEO and founder at Intercom, building Fin.ai",
        "linkedin_member_id": null,
        "last_job_change_detected_at": null,
        "job_history": [
            {
                "title": "CEO, chairman, and co-founder",
                "company_name": "Intercom",
                "logo_url": "9ded0364-c88a-4789-9d39-2a15ed239edb.jpg",
                "current": true,
                "start_year": 2022,
                "start_month": 10,
                "end_year": null,
                "end_month": null,
                "duration_in_months": 39,
                "departments": [
                    "Founder",
                    "Chief Executive"
                ],
                "seniority": "C-Suite",
                "company_id": "cccc7c7da6116a8830a07100",
                "job_key": "82981650"
            },
            {
                "title": "Chairman and co-founder",
                "company_name": "Intercom",
                "logo_url": "9ded0364-c88a-4789-9d39-2a15ed239edb.jpg",
                "current": false,
                "start_year": 2020,
                "start_month": 7,
                "end_year": 2022,
                "end_month": 10,
                "duration_in_months": 27,
                "departments": [
                    "Founder"
                ],
                "seniority": "Founder/Owner",
                "company_id": "cccc7c7da6116a8830a07100",
                "job_key": "23054356"
            },
            {
                "title": "CEO and co-founder",
                "company_name": "Intercom",
                "logo_url": "9ded0364-c88a-4789-9d39-2a15ed239edb.jpg",
                "current": false,
                "start_year": 2011,
                "start_month": 8,
                "end_year": 2020,
                "end_month": 7,
                "duration_in_months": 107,
                "departments": [
                    "Founder",
                    "Chief Executive"
                ],
                "seniority": "C-Suite",
                "company_id": "cccc7c7da6116a8830a07100",
                "job_key": "68686694"
            },
            {
                "title": "CEO",
                "company_name": "Exceptional",
                "logo_url": "2588d75e-d2e7-4fb1-bf31-35cafd119ec0.jpg",
                "current": false,
                "start_year": 2008,
                "start_month": 10,
                "end_year": 2011,
                "end_month": 7,
                "duration_in_months": 33,
                "departments": [
                    "Chief Executive"
                ],
                "seniority": "C-Suite",
                "company_id": "ccccd431f3dfa7e88993bb18",
                "job_key": "80900834"
            },
            {
                "title": "CEO",
                "company_name": "Contrast",
                "logo_url": "d4bbee3f-7128-436d-a474-fcac68b989e4.jpg",
                "current": false,
                "start_year": 2007,
                "start_month": 12,
                "end_year": 2011,
                "end_month": 7,
                "duration_in_months": 43,
                "departments": [
                    "Chief Executive"
                ],
                "seniority": "C-Suite",
                "company_id": "ccccf3e7f023592ee266a9d8",
                "job_key": "72014547"
            }
        ],
        "mobile": {
            "status": "VERIFIED",
            "revealed": false,
            "mobile": "+1 415-3**-****",
            "mobile_national": "(415) 3**-****",
            "mobile_international": "+1 415-3**-****",
            "mobile_country": "United States",
            "mobile_country_code": "US"
        },
        "email": {
            "status": "VERIFIED",
            "revealed": true,
            "email": "eoghan.*****@intercom.com",
            "verification_method": "BOUNCEBAN",
            "email_mx_provider": "Google"
        },
        "location": {
            "country": "United States",
            "country_code": "US",
            "state": "California",
            "city": "San Francisco",
            "time_zone": "America/Los_Angeles",
            "time_zone_offset": -7.0
        },
        "skills": []
    },
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

### Example of an error response

```json
{
    "error": true,
    "error_code": "NO_MATCH"
}
```