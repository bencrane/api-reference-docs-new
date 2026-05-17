# Company Job Salary Endpoint

## GET /company-job-salary

Get estimated job salaries/pay in a specific company by job title and optionally a location and experience level in years.

## Query Parameters

### company (Required)
**Type:** string

The company name for which to get salary information.

**Example:** `Amazon`

### job_title (Required)
**Type:** string

Job title for which to get salary estimation.

**Example:** `software developer`

### location (Optional)
**Type:** string

Free-text location/area in which to get salary estimation.

**Example:** `San Francisco`

### location_type (Optional)
**Type:** string (enum)  
**Default:** `ANY`

Specify the type of the location you are looking to get salary estimation for additional accuracy.

**Allowed Values:**
- `ANY`
- `CITY`
- `STATE`
- `COUNTRY`

### years_of_experience (Optional)
**Type:** string (enum)  
**Default:** `ALL`

Get job estimation for a specific experience level range (years).

**Allowed Values:**
- `ALL`
- `LESS_THAN_ONE`
- `ONE_TO_THREE`
- `FOUR_TO_SIX`
- `SEVEN_TO_NINE`
- `TEN_TO_FOURTEEN`
- `ABOVE_FIFTEEN`

## Response

**Status Code:** 200 (Successful Response)  
**Content Type:** application/json

### Response Schema

```json
{
  "status": "OK",
  "request_id": "2bd097a9-396e-4261-9337-39f3160a3d60",
  "data": [
    {
      "location": "string",
      "job_title": "string",
      "company": "string",
      "min_salary": number,
      "max_salary": number,
      "median_salary": number,
      "min_base_salary": number,
      "max_base_salary": number,
      "median_base_salary": number,
      "min_additional_pay": number,
      "max_additional_pay": number,
      "median_additional_pay": number,
      "salary_period": "string",
      "salary_currency": "string",
      "confidence": "string",
      "salary_count": number
    }
  ]
}
```

### Response Fields

- **status** - Request status (e.g., "OK")
- **request_id** - Unique identifier for the request
- **data** - Array of salary records
  - **location** - The location for the salary data
  - **job_title** - The job title
  - **company** - The company name
  - **min_salary** - Minimum total salary
  - **max_salary** - Maximum total salary
  - **median_salary** - Median/average total salary
  - **min_base_salary** - Minimum base salary
  - **max_base_salary** - Maximum base salary
  - **median_base_salary** - Median/average base salary
  - **min_additional_pay** - Minimum additional pay (bonus, stock, etc.)
  - **max_additional_pay** - Maximum additional pay
  - **median_additional_pay** - Median/average additional pay
  - **salary_period** - Period for the salary (e.g., "YEAR")
  - **salary_currency** - Currency code (e.g., "USD")
  - **confidence** - Confidence level of the data
  - **salary_count** - Number of salary records used for calculation

## Request Example

### cURL
```bash
curl 'https://api.openwebninja.com/job-salary-data/company-job-salary?company=Amazon&job_title=software%20developer' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example

```json
{
  "status": "OK",
  "request_id": "2bd097a9-396e-4261-9337-39f3160a3d60",
  "data": [
    {
      "location": "United States",
      "job_title": "Software Developer",
      "company": "Amazon",
      "min_salary": 140594.13,
      "max_salary": 209058.84,
      "median_salary": 170162.89,
      "min_base_salary": 111791.03,
      "max_base_salary": 155293.04,
      "median_base_salary": 131758.75,
      "min_additional_pay": 28803.1,
      "max_additional_pay": 53765.8,
      "median_additional_pay": 38404.14,
      "salary_period": "YEAR",
      "salary_currency": "USD",
      "confidence": "CONFIDENT",
      "salary_count": 988
    }
  ]
}
```
