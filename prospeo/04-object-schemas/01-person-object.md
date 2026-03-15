# Person Object

The person object is present in most responses (`/enrich`, `/search`) and represents a person (lead) and contains it's potential email address, mobile number, and many more datapoints.

Any property can be `null` if no data is available. High-level properties (such as `location`) can also be `null`, hence accessing nested keys needs to be done carefully (null-check).

The person object will be returned along with its company. You can find the details of every company fields in the Company Object documentation.

When performing a Search Person API request, the `mobile` and `email` wont be present in the response. Use our Enrich person endpoint to reveal/access those.

## Properties

| Property | Type | Description |
|----------|------|-------------|
| `person_id` | string | Unique identifier for the person in Prospeo's system. |
| `first_name` | string | Person's given name. |
| `last_name` | string | Person's family name. |
| `full_name` | string | Person's full name. |
| `linkedin_url` | string | Link to the person's public LinkedIn profile. |
| `headline` | string | Person's headline summarizing current role and expertise. |
| `current_job_title` | string | Title of the person's current position. |
| `current_job_key` | string | Internal key representing the current job in Prospeo's system. As a person can have multiple current jobs, this key represents the main job. |
| `skills` | array of strings | List of the person's self-assigned skills (can be any string). |
| `last_job_change_detected_at` | datetime | When was the last job change of that person detected by Prospeo. |

### Job Details (within `job_history` array)

| Property | Type | Description |
|----------|------|-------------|
| `title` | string | Job title for this role. |
| `company_name` | string | Name of the company. |
| `current` | boolean | `true` if this role is current (no end date); otherwise `false`. Multiple job can be current at once. |
| `start_year` | integer | Four-digit year when this role began. |
| `start_month` | integer | Month (1–12) when this role began. This can be `null` if unspecified. |
| `end_year` | integer | Four-digit year when this role ended, or `null` if ongoing. |
| `end_month` | integer | Month (1–12) when this role ended, or `null` if ongoing. |
| `duration_in_months` | integer | Total duration of the role in months. |
| `departments` | array of strings | Departments assigned to this job. |
| `seniority` | string | Seniority assigned to this job. |
| `company_id` | string | Prospeo's internal identifier for the company. This can be `null` if the job is not internally linked to a company. |
| `job_key` | string | Prospeo's internal key for the specific job entry. Useful when multiple current jobs exists to find the correct one with `current_job_key`. |

### Mobile Details (within `mobile`)

| Property | Type | Description |
|----------|------|-------------|
| `status` | string | Verification status (`VERIFIED` or `UNAVAILABLE`). |
| `revealed` | boolean | `true` if you revealed and paid for this mobile; `false` otherwise. |
| `mobile` | string | E.164 formatted phone number (e.g., "+12345678900"). Only available if the mobile is revealed. |
| `mobile_national` | string | National format of the number (e.g., "234 567 8900"). Only available if the mobile is revealed. |
| `mobile_international` | string | International formatting of the number (e.g., "+1 234 567 8900"). Only available if the mobile is revealed. |
| `mobile_country_code` | string | ISO 3166-1 alpha-2 country code for the number. Only available if the mobile is revealed. |
| `mobile_country` | string | Full country name corresponding to `mobile_country`. Only available if the mobile is revealed. |

### Email Details (within `email`)

| Property | Type | Description |
|----------|------|-------------|
| `status` | string | Verification status (`VERIFIED` or `UNAVAILABLE`). |
| `revealed` | boolean | `true` if the email is revealed; `false` otherwise. |
| `email` | string | The person's email address. Only available if the email is revealed. |
| `verification_method` | string | Verification method used to validate the email (`SMTP` or `BOUNCEBAN`). |
| `email_mx_provider` | string | MX record provider for the domain (e.g., "GOOGLE"). Only available if the email is revealed. |

### Location Details (within `location`)

| Property | Type | Description |
|----------|------|-------------|
| `country` | string | Full country name (e.g., "United States"). |
| `country_code` | string | ISO 3166-1 alpha-2 country code (e.g., "US"). |
| `state` | string | State or region name. |
| `city` | string | City name. |
| `time_zone` | string | IANA timezone identifier (e.g., "America/Los_Angeles"). |
| `time_zone_offset` | integer | UTC offset in hours (e.g., -8). |

## JSON example

```json
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
}
```