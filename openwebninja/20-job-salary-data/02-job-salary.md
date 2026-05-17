# Job Salary Endpoint

## GET /job-salary

Get estimated job salaries/pay by job title and location.

## Query Parameters

### job_title (Required)
**Type:** string

Job title for which to get salary estimation.

**Example:** `nodejs developer`

### location (Required)
**Type:** string

Free-text location/area in which to get salary estimation.

**Example:** `New York`

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
  "request_id": "987d4b94-f10c-4e32-881d-184005fce21b",
  "data": [
    {
      "location": "string",
      "job_title": "string",
      "min_salary": number,
      "max_salary": number,
      "median_salary": number,
      "salary_period": "string",
      "salary_currency": "string",
      "publisher_name": "string",
      "publisher_link": "string",
      "confidence": "string"
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
  - **min_salary** - Minimum salary
  - **max_salary** - Maximum salary
  - **median_salary** - Median/average salary
  - **salary_period** - Period for the salary (e.g., "YEAR")
  - **salary_currency** - Currency code (e.g., "USD")
  - **publisher_name** - Source of the data (e.g., "Glassdoor")
  - **publisher_link** - Link to the source
  - **confidence** - Confidence level of the data

## Request Example

### cURL
```bash
curl 'https://api.openwebninja.com/job-salary-data/job-salary?job_title=nodejs%20developer&location=New%20York' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example

```json
{
  "status": "OK",
  "request_id": "987d4b94-f10c-4e32-881d-184005fce21b",
  "data": [
    {
      "location": "New York City, NY",
      "job_title": "Nodejs Developer",
      "min_salary": 111485.45,
      "max_salary": 185122.49,
      "median_salary": 142576.14,
      "salary_period": "YEAR",
      "salary_currency": "USD",
      "publisher_name": "Glassdoor",
      "publisher_link": "https://www.glassdoor.com/Salaries/company-salaries.htm?suggestCount=0&suggestChosen=false&sc.keyword=Nodejs%20Developer&locT=C&locId=1132348",
      "confidence": "CONFIDENT"
    }
  ]
}
```
