# Company Object

The company object is present in most responses (`/enrich`, `/search`) and represents a company.

Any property can be `null` if no data is available. High-level properties (such as `location`) can also be `null`, hence accessing nested keys needs to be done carefully (null-check).

## Properties

| Property | Type / Structure | Description |
|----------|-----------------|-------------|
| `company_id` | string | Unique identifier for the company in Prospeo's system. |
| `name` | string | Company name. |
| `website` | string | URL of the main website of the company. |
| `domain` | string | Root domain extracted from website (e.g., prospeo.io). |
| `other_websites` | array of strings | Additional websites or domains linked to the company. |
| `description` | string | Social-network company description. |
| `description_seo` | string | SEO description of the company as found on Google. |
| `description_ai` | string | AI-generated summary of the company. |
| `type` | string | Legal type, values can be: Private, Public, Non profit, Other. |
| `industry` | string | Main industry of the company. |
| `employee_count` | integer | Estimated headcount of the company. |
| `employee_count_on_prospeo` | integer | Number of employees available for this company in Prospeo's database. |
| `employee_range` | string | Bucketed employee range (e.g., "1000-5000"). |
| `location` | object | Registered HQ or primary location of the company (see Location Details below). |
| `sic_codes` | array of strings | Standard Industrial Classification codes. |
| `naics_codes` | array of strings | North American Industry Classification System codes. |
| `email_tech` | object | Technical details about the company email infrastructure (see Email Tech Details below). |
| `linkedin_url` | string | Public LinkedIn page for the company. |
| `twitter_url` | string | Twitter page for the company. |
| `facebook_url` | string | Facebook page for the company. |
| `instagram_url` | string | Instagram page for the company. |
| `youtube_url` | string | Youtube page for the company. |
| `crunchbase_url` | string | Crunchbase page for the company. |
| `phone_hq` | object | Company headquarters phone data (see Phone HQ Details below). This is usually a landline number. |
| `founded` | integer | Year the company was founded. |
| `revenue_range` | object | Numeric min/max annual revenue in USD (see Revenue Range Details). |
| `revenue_range_printed` | string | Human-readable revenue range (e.g., "$5B-10B+"). |
| `keywords` | array of strings | Self-reported keywords describing the company. |
| `logo_url` | string | Prospeo-hosted URL to the company's logo image. Full URL format: `https://prospeo-static-assets.s3.us-east-1.amazonaws.com/company_logo/{id}.jpg` |
| `attributes` | object | Company attributes such as `has_pricing`, etc. (see Attribute Flags below). |
| `funding` | object | Funding information (see Funding Details below). |
| `technology` | object | Technology stack (see Technology Details below). |
| `job_postings` | object | Active job postings (see Job Postings Details below). |

### Location Details (`location`)

| Key | Type | Description |
|-----|------|-------------|
| `country` | string | Full country name. |
| `country_code` | string | Alpha-2 code. |
| `state` | string | State / province / region. |
| `city` | string | City name. |
| `raw_address` | string | Self-reported unstructured company address. |

### Email Tech Details (`email_tech`)

| Key | Type | Description |
|-----|------|-------------|
| `domain` | string | Main domain used for emails. |
| `mx_provider` | string | Mail-exchange provider for the company. |
| `catch_all_domain` | boolean | `true` if the domain accepts all email addresses (catch-all). |

### Phone HQ Details (`phone_hq`)

| Key | Type | Description |
|-----|------|-------------|
| `phone_hq` | string | E.164 formatted phone (e.g., "+12345678900"). |
| `phone_hq_national` | string | National format (e.g., "234 567 8900"). |
| `phone_hq_international` | string | International spacing (e.g., "+1 234 567 8900"). |
| `phone_hq_country_code` | string | Alpha-2 code of the phone number. |
| `phone_hq_country` | string | Full country name of the phone number. |

### Revenue Range Details (`revenue_range`)

| Key | Type | Description |
|-----|------|-------------|
| `min` | number | Lower-bound annual revenue in USD. |
| `max` | number | Upper-bound annual revenue in USD. |

### Attribute Flags (`attributes`)

| Key | Type | Description |
|-----|------|-------------|
| `has_demo` | boolean | `true` if the company offers demo, `false` if not, `null` if unknown. |
| `has_free_trial` | boolean | `true` if the company offers a free trial, `false` if not, `null` if unknown. |
| `has_downloadable` | boolean | `true` if the company offers a downloadable app/software, `false` if not, `null` if unknown. |
| `has_mobile_apps` | boolean | `true` if the company has a mobile app, `false` if not, `null` if unknown. |
| `has_online_reviews` | boolean | `true` if the company has online reviews, `false` if not, `null` if unknown. |
| `has_pricing` | boolean | `true` if the company has a public pricing page, `false` if not, `null` if unknown. |

### Funding Details (`funding`)

| Key | Type / Structure | Description |
|-----|-----------------|-------------|
| `count` | integer | Number of recorded funding rounds. |
| `total_funding` | integer | Aggregate capital raised (USD). |
| `total_funding_printed` | string | Human-readable total of fund raised (e.g., "$1M"). |
| `latest_funding_date` | datetime | Date of most recent funding round. |
| `latest_funding_stage` | string | Stage of most recent round (e.g., Series A). |
| `funding_events` | array of objects | List of all the individual rounds; see Funding Event. |

#### Funding Event (object inside `funding_events`)

| Key | Type / Structure | Description |
|-----|-----------------|-------------|
| `amount` | integer | Amount raised (USD). |
| `amount_printed` | string | Human-readable amount (e.g., "$1M"). |
| `raised_at` | datetime | Date at which this funding event occured. |
| `stage` | string | Stage of this event (e.g., Series A). |
| `link` | string | Link to the public Crunchbase page for this event. |

### Technology Details (`technology`)

| Key | Type / Structure | Description |
|-----|-----------------|-------------|
| `count` | integer | Total detected technologies. |
| `technology_names` | array of strings | Simple list of tech names. |
| `technology_list` | array of objects | Complete list of technologies with their `name` (string) & `category` (string). |

### Job Postings Details (`job_postings`)

| Key | Type | Description |
|-----|------|-------------|
| `active_count` | integer | Number of currently open roles. |
| `active_titles` | array of strings | Job titles of current openings. |

## JSON example

```json
{
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
```