# Job Salary Data API Documentation

**Version:** v1.0.0  
**OpenAPI:** 3.0.0

Complete reference documentation for the OpenWeb Ninja Job Salary Data API. Includes code examples, data samples, and usage guides for retrieving salary insights and pay estimates by job title, location, and experience level from Glassdoor.

## Server

**Base URL:** `https://api.openwebninja.com/job-salary-data`

## Authentication

**Type:** X-API-Key (Required)

All requests require the `x-api-key` header with your API key.

### Example Header
```
x-api-key: YOUR_SECRET_TOKEN
```

## Client Libraries

Shell/Curl examples are provided for all endpoints.

## Operations

The API provides two main endpoints:

- **GET `/job-salary`** - Get estimated job salaries/pay by job title and location
- **GET `/company-job-salary`** - Get estimated job salaries/pay in a specific company by job title

## Common Parameters

### Experience Level (`years_of_experience`)

Get job estimation for a specific experience level range (years).

- `ALL` (default)
- `LESS_THAN_ONE`
- `ONE_TO_THREE`
- `FOUR_TO_SIX`
- `SEVEN_TO_NINE`
- `TEN_TO_FOURTEEN`
- `ABOVE_FIFTEEN`

### Location Type (`location_type`)

Specify the type of the location for additional accuracy.

- `ANY` (default)
- `CITY`
- `STATE`
- `COUNTRY`
