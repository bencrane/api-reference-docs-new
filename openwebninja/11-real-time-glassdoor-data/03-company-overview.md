# Company Overview

`GET /company-overview`

Get company (employer) overview/details from Glassdoor (e.g. `https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm`).

## Query Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `company_id` | string | Yes | — | Glassdoor company ID. |
| `domain` | string (enum) | No | `www.glassdoor.com` | The Glassdoor domain to use. |

### `domain` enum values

```
www.glassdoor.com
www.glassdoor.co.uk
www.glassdoor.com.ar
www.glassdoor.com.au
www.glassdoor.be
... (show all values)
```

## Responses

**`200` — Successful Response** (`application/json`)

## Request Example

```shell
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-overview?company_id=1138' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "5899f694-de49-4cd3-947b-996675eddad8",
      "parameters": {
        "company_id": "1138",
        "domain": "www.glassdoor.com"
      },
      "data": {
        "company_id": 1138,
        "name": "Apple",
        "company_link": "https://www.glassdoor.com/Overview/Working-at-Apple-EI_IE1138.11,16.htm",
        "rating": 4.1,
        "review_count": 47998,
        "salary_count": 168369,
        "job_count": 5937,
        "headquarters_location": "Cupertino, US",
        "logo": "https://media.glassdoor.com/sql/1138/apple-squarelogo-1595530154096.png",
        "company_size": "10000+ Employees",
        "company_size_category": "GIANT",
        "company_description": "We’re a diverse collective of thinkers and doers, continually reimagining what’s possible to help us all do what we love in new ways. And the same innovation that goes into our products also applies to our practices — strengthening our commitment to leave the world better than we found it. This is where your work can make a difference in people’s lives. Including your own.  \n\nApple is an equal opportunity employer that is committed to inclusion and diversity. Visit apple.com/careers to learn more.",
        "industry": "Computer Hardware Development",
        "website": "https://www.apple.com",
        "company_type": "Company - Public",
        "revenue": "$10+ billion (USD)",
        "business_outlook_rating": 0.73,
        "career_opportunities_rating": 3.7,
        "ceo": "Tim Cook",
        "ceo_rating": 0.88,
        "compensation_and_benefits_rating": 4.2,
        "culture_and_values_rating": 4,
        "diversity_and_inclusion_rating": 4.2,
        "recommend_to_friend_rating": 0.8,
        "senior_management_rating": 3.6,
        "work_life_balance_rating": 3.6,
        "stock": "AAPL",
        "year_founded": 1976,
        "reviews_link": "https://www.glassdoor.com/Reviews/Apple-Reviews-E1138.htm",
        "jobs_link": "https://www.glassdoor.com/Jobs/Apple-Jobs-E1138.htm",
        "faq_link": "https://www.glassdoor.com/FAQ/Apple-Questions-E1138.htm",
        "competitors": [
          {
            "id": 9079,
            "name": "Google"
          },
          {
            "id": 1651,
            "name": "Microsoft"
          },
          {
            "id": 3363,
            "name": "Samsung Electronics"
          }
        ],
        "office_locations": [
          {
            "city": "Austin, TX",
            "country": "United States"
          },
          {
            "city": "San Marcos, TX",
            "country": "United States"
          },
          {
            "city": "Cerritos, CA",
            "country": "United States"
          },
          {
            "city": "Costa Mesa, CA",
            "country": "United States"
          },
          {
            "city": "Irvine, CA",
            "country": "United States"
          },
          {
            "city": "Los Angeles, CA",
            "country": "United States"
          },
          {
            "city": "Pasadena, CA",
            "country": "United States"
          },
          {
            "city": "Santa Monica, CA",
            "country": "United States"
          },
          {
            "city": "Campbell, CA",
            "country": "United States"
          },
          {
            "city": "Cupertino, CA",
            "country": "United States"
          },
          {
            "city": "Los Gatos, CA",
            "country": "United States"
          },
          {
            "city": "Milpitas, CA",
            "country": "United States"
          },
          {
            "city": "Mountain View, CA",
            "country": "United States"
          },
          {
            "city": "Palo Alto, CA",
            "country": "United States"
          },
          {
            "city": "San Jose, CA",
            "country": "United States"
          },
          {
            "city": "Santa Clara, CA",
            "country": "United States"
          },
          {
            "city": "Stanford, CA",
            "country": "United States"
          },
          {
            "city": "Sunnyvale, CA",
            "country": "United States"
          },
          {
            "city": "Manhattan Beach, CA",
            "country": "United States"
          },
          {
            "city": "East Palo Alto, CA",
            "country": "United States"
          },
          {
            "city": "London, England",
            "country": "United Kingdom"
          },
          {
            "city": "Bukit Merah Estate, ",
            "country": "Singapore"
          },
          {
            "city": "Ang Mo Kio New Town, ",
            "country": "Singapore"
          },
          {
            "city": "Singapore",
            "country": "Singapore"
          },
          {
            "city": "Munich, Bavaria",
            "country": "Germany"
          }
        ],
        "best_places_to_work_awards": [
          {
            "time_period": "2018",
            "rank": 84
          },
          {
            "time_period": "2019",
            "rank": 71
          },
          {
            "time_period": "2020",
            "rank": 84
          },
          {
            "time_period": "2021",
            "rank": 31
          },
          {
            "time_period": "2022",
            "rank": 56
          },
          {
            "time_period": "2024",
            "rank": 39
          },
          {
            "time_period": "2025",
            "rank": 56
          },
          {
            "time_period": "2009",
            "rank": 19
          },
          {
            "time_period": "2010",
            "rank": 22
          },
          {
            "time_period": "2011",
            "rank": 20
          },
          {
            "time_period": "2012",
            "rank": 10
          },
          {
            "time_period": "2013",
            "rank": 34
          },
          {
            "time_period": "2014",
            "rank": 35
          },
          {
            "time_period": "2015",
            "rank": 22
          },
          {
            "time_period": "2016",
            "rank": 25
          },
          {
            "time_period": "2017",
            "rank": 36
          }
        ]
      }
    }
  }
}
```
