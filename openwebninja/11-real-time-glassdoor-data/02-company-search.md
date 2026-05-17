# Company Search

`GET /company-search`

Search for companies (employers) on Glassdoor.

## Query Parameters

| Parameter | Type | Required | Constraints | Default | Description |
|-----------|------|----------|-------------|---------|-------------|
| `query` | string | Yes | — | — | Search query or Company ID. |
| `limit` | number | No | min: 1, max: 100 | 10 | Maximum number of results to return. |
| `domain` | string (enum) | No | — | `www.glassdoor.com` | The Glassdoor domain to use. |

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
curl 'https://api.openwebninja.com/realtime-glassdoor-data/company-search?query=goo' \
  --header 'x-api-key: YOUR_SECRET_TOKEN'
```

## Response Example (`200`)

```json
{
  "Example": {
    "value": {
      "status": "OK",
      "request_id": "cb4312c6-8060-4ee8-8538-018f9d92a573",
      "parameters": {
        "query": "goo",
        "domain": "www.glassdoor.com",
        "limit": 10
      },
      "data": [
        {
          "company_id": 1145391,
          "name": "Goo.Com",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Goo-Com-EI_IE1145391.11,18.htm",
          "rating": 4.3,
          "review_count": 2,
          "salary_count": 2,
          "job_count": 0,
          "headquarters_location": "Trezzano sul Naviglio, Italy",
          "logo": "https://media.glassdoor.com/sql/1145391/goo-com-squarelogo-1458658483643.png",
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": "Goo.com Srl is a dynamic Italian Company. We are IT Solution Provider, System Integrator and, above all, IDEAS DEVELOPER! We provide: - IT **TOP** Consultancy. - Software Engineering, Software Architecture and Hardware Engineering services. - Web and Mobile Responsive development. - Consolidate and Certified SysAdmin experience. - Software ad hoc. Our Customers and Partners: Have a look here: http://goodotcom.com/pages/chi_siamo Our Story: A long time ago in a galaxy far, far away, our first company SOPRIT was funded. Back in the 1999 we took the challenge to support our Customers in the process of integration and optimisation of their resources. We developed customised solutions for their security systems and automation. After years of experience we founded Goo.com to offer technologically advanced solutions with the highest standards of quality and reliability.",
          "industry": "Enterprise Software & Network Solutions",
          "website": "https://www.goodotcom.com",
          "company_type": "Company - Private",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 1,
          "career_opportunities_rating": 4,
          "ceo": "Marco Simone",
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 5,
          "culture_and_values_rating": 5,
          "diversity_and_inclusion_rating": 0,
          "recommend_to_friend_rating": 1,
          "senior_management_rating": 4.7,
          "work_life_balance_rating": 4,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Goo-Com-Reviews-E1145391.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Goo-Com-Jobs-E1145391.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Goo-Com-Questions-E1145391.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 8070755,
          "name": "Stichting GOO",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Stichting-GOO-EI_IE8070755.11,24.htm",
          "rating": 0,
          "review_count": 0,
          "salary_count": 0,
          "job_count": 0,
          "headquarters_location": "Gemert, Netherlands",
          "logo": null,
          "company_size": "Unknown",
          "company_size_category": "UNKNOWN",
          "company_description": null,
          "industry": null,
          "website": "https://www.stichtinggoo.nl",
          "company_type": "Company - Public",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0,
          "career_opportunities_rating": 0,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 0,
          "culture_and_values_rating": 0,
          "diversity_and_inclusion_rating": 0,
          "recommend_to_friend_rating": 0,
          "senior_management_rating": 0,
          "work_life_balance_rating": 0,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Stichting-GOO-Reviews-E8070755.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Stichting-GOO-Jobs-E8070755.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Stichting-GOO-Questions-E8070755.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 939648,
          "name": "Goo-Goo Express Wash",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Goo-Goo-Express-Wash-EI_IE939648.11,31.htm",
          "rating": 3,
          "review_count": 31,
          "salary_count": 57,
          "job_count": 0,
          "headquarters_location": "Chattanooga, GA",
          "logo": "https://media.glassdoor.com/sql/939648/goo-goo-express-wash-squarelogo-1562581717382.png",
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": "Vehicle Repair & Maintenance",
          "website": "https://www.googooexpresswash.com",
          "company_type": "Company - Private",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0.17,
          "career_opportunities_rating": 2.4,
          "ceo": "Roger Beck",
          "ceo_rating": 0.46,
          "compensation_and_benefits_rating": 2.7,
          "culture_and_values_rating": 2.8,
          "diversity_and_inclusion_rating": 3.1,
          "recommend_to_friend_rating": 0.37,
          "senior_management_rating": 2.5,
          "work_life_balance_rating": 2.7,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Goo-Goo-Express-Wash-Reviews-E939648.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Goo-Goo-Express-Wash-Jobs-E939648.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Goo-Goo-Express-Wash-Questions-E939648.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 3651112,
          "name": "Black Goo",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Black-Goo-EI_IE3651112.11,20.htm",
          "rating": 3.6,
          "review_count": 7,
          "salary_count": 19,
          "job_count": 0,
          "headquarters_location": "Tring, United Kingdom",
          "logo": "https://media.glassdoor.com/sql/3651112/black-goo-squarelogo-1663594570619.png",
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": null,
          "website": "https://www.blackgoocoffee.co.uk",
          "company_type": "Unknown",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0.53,
          "career_opportunities_rating": 3.5,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 3.8,
          "culture_and_values_rating": 3.8,
          "diversity_and_inclusion_rating": 3.8,
          "recommend_to_friend_rating": 0.62,
          "senior_management_rating": 3.3,
          "work_life_balance_rating": 4.4,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Black-Goo-Reviews-E3651112.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Black-Goo-Jobs-E3651112.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Black-Goo-Questions-E3651112.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 1895285,
          "name": "Let's Goo Social",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Let-s-Goo-Social-EI_IE1895285.11,27.htm",
          "rating": 2.9,
          "review_count": 6,
          "salary_count": 7,
          "job_count": 6,
          "headquarters_location": "Singapore, Singapore",
          "logo": "https://media.glassdoor.com/sql/1895285/let-s-goo-social-squarelogo-1515482818126.png",
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": "Advertising & Public Relations",
          "website": "https://www.letsgoosocial.com",
          "company_type": "Company - Private",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0.41,
          "career_opportunities_rating": 2.8,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 2.4,
          "culture_and_values_rating": 2.4,
          "diversity_and_inclusion_rating": 2.1,
          "recommend_to_friend_rating": 0.53,
          "senior_management_rating": 2.4,
          "work_life_balance_rating": 2.6,
          "stock": null,
          "year_founded": 2016,
          "reviews_link": "https://www.glassdoor.com/Reviews/Let-s-Goo-Social-Reviews-E1895285.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Let-s-Goo-Social-Jobs-E1895285.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Let-s-Goo-Social-Questions-E1895285.htm",
          "competitors": [],
          "office_locations": [
            {
              "city": "Chennai",
              "country": "India"
            }
          ],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 5953502,
          "name": "Goo Goo Gaa Gaa",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Goo-Goo-Gaa-Gaa-EI_IE5953502.11,26.htm",
          "rating": 4.2,
          "review_count": 2,
          "salary_count": 5,
          "job_count": 0,
          "headquarters_location": "Brookfield, WI",
          "logo": null,
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": null,
          "website": "https://googoogaagaa.com",
          "company_type": "Government",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0,
          "career_opportunities_rating": 3,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 3,
          "culture_and_values_rating": 3,
          "diversity_and_inclusion_rating": 3,
          "recommend_to_friend_rating": 0,
          "senior_management_rating": 3,
          "work_life_balance_rating": 3,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Goo-Goo-Gaa-Gaa-Reviews-E5953502.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Goo-Goo-Gaa-Gaa-Jobs-E5953502.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Goo-Goo-Gaa-Gaa-Questions-E5953502.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 107591,
          "name": "WATG",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-WATG-EI_IE107591.11,15.htm",
          "rating": 3.5,
          "review_count": 186,
          "salary_count": 351,
          "job_count": 0,
          "headquarters_location": "Irvine, CA",
          "logo": "https://media.glassdoor.com/sql/107591/watg-squarelogo-1543326423910.png",
          "company_size": "201 to 500 Employees",
          "company_size_category": "MEDIUM",
          "company_description": "From our dawning days in 1945 Honolulu, we have pioneered hospitality, tourism and destination design. Independent to this day, we are a global multi-disciplinary design firm specializing in Strategy, Master Planning, Architecture, Landscape and Wimberly Interiors. We are a team of 500 creative, world-traveling professionals designing landmark urban and leisure destinations with eight offices across three continents.",
          "industry": "Architectural & Engineering Services",
          "website": "https://www.watg.com",
          "company_type": "Company - Private",
          "revenue": "$25 to $100 million (USD)",
          "business_outlook_rating": 0.67,
          "career_opportunities_rating": 3.1,
          "ceo": "David D Moore ",
          "ceo_rating": 0.69,
          "compensation_and_benefits_rating": 3.6,
          "culture_and_values_rating": 3.4,
          "diversity_and_inclusion_rating": 3.6,
          "recommend_to_friend_rating": 0.66,
          "senior_management_rating": 3.1,
          "work_life_balance_rating": 3.5,
          "stock": null,
          "year_founded": 1945,
          "reviews_link": "https://www.glassdoor.com/Reviews/WATG-Reviews-E107591.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/WATG-Jobs-E107591.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/WATG-Questions-E107591.htm",
          "competitors": [
            {
              "id": 267586,
              "name": "HBA Architecture & Interior Design"
            },
            {
              "id": 376657,
              "name": "Rockwell Group"
            },
            {
              "id": 1381077,
              "name": "Populous"
            }
          ],
          "office_locations": [
            {
              "city": "New York, NY",
              "country": "United States"
            },
            {
              "city": "Honolulu, HI",
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
              "city": "Shanghai, Shanghai",
              "country": "China"
            },
            {
              "city": "London, England",
              "country": "United Kingdom"
            },
            {
              "city": "Singapore",
              "country": "Singapore"
            }
          ],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 923128,
          "name": "Goo Technologies",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Goo-Technologies-EI_IE923128.11,27.htm",
          "rating": 4.5,
          "review_count": 2,
          "salary_count": 5,
          "job_count": 0,
          "headquarters_location": "Stockholm, Sweden",
          "logo": null,
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": "Information Technology Support Services",
          "website": "https://www.goocreate.com",
          "company_type": "Company - Private",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0,
          "career_opportunities_rating": 4.1,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 4,
          "culture_and_values_rating": 4.5,
          "diversity_and_inclusion_rating": 4,
          "recommend_to_friend_rating": 1,
          "senior_management_rating": 3.6,
          "work_life_balance_rating": 4,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Goo-Technologies-Reviews-E923128.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Goo-Technologies-Jobs-E923128.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Goo-Technologies-Questions-E923128.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 812843,
          "name": "Pwi-Di-Goo-Zing Ne-Yaa-Zhing Advisory Services",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Pwi-Di-Goo-Zing-Ne-Yaa-Zhing-Advisory-Services-EI_IE812843.11,57.htm",
          "rating": 3.9,
          "review_count": 3,
          "salary_count": 3,
          "job_count": 1,
          "headquarters_location": "Fort Frances, Canada",
          "logo": null,
          "company_size": "201 to 500 Employees",
          "company_size_category": "MEDIUM",
          "company_description": null,
          "industry": "State & Regional Agencies",
          "website": "https://www.advisoryservices.ca",
          "company_type": "Government",
          "revenue": "$25 to $100 million (USD)",
          "business_outlook_rating": 0,
          "career_opportunities_rating": 2.3,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 3.7,
          "culture_and_values_rating": 3.3,
          "diversity_and_inclusion_rating": 0,
          "recommend_to_friend_rating": 0,
          "senior_management_rating": 3.7,
          "work_life_balance_rating": 4,
          "stock": null,
          "year_founded": null,
          "reviews_link": "https://www.glassdoor.com/Reviews/Pwi-Di-Goo-Zing-Ne-Yaa-Zhing-Advisory-Services-Reviews-E812843.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Pwi-Di-Goo-Zing-Ne-Yaa-Zhing-Advisory-Services-Jobs-E812843.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Pwi-Di-Goo-Zing-Ne-Yaa-Zhing-Advisory-Services-Questions-E812843.htm",
          "competitors": [],
          "office_locations": [],
          "best_places_to_work_awards": []
        },
        {
          "company_id": 2888762,
          "name": "Dembach Goo Informatik",
          "company_link": "https://www.glassdoor.com/Overview/Working-at-Dembach-Goo-Informatik-EI_IE2888762.11,33.htm",
          "rating": 4.4,
          "review_count": 2,
          "salary_count": 3,
          "job_count": 3,
          "headquarters_location": "Cologne, Germany",
          "logo": "https://media.glassdoor.com/sql/2888762/dembach-goo-informatik-squarelogo-1599212755043.png",
          "company_size": "1 to 50 Employees",
          "company_size_category": "SMALL",
          "company_description": null,
          "industry": "Information Technology Support Services",
          "website": "https://www.dg-i.net",
          "company_type": "Company - Private",
          "revenue": "Unknown / Non-Applicable",
          "business_outlook_rating": 0.36,
          "career_opportunities_rating": 4,
          "ceo": null,
          "ceo_rating": 0,
          "compensation_and_benefits_rating": 3.7,
          "culture_and_values_rating": 3.7,
          "diversity_and_inclusion_rating": 3,
          "recommend_to_friend_rating": 1,
          "senior_management_rating": 3.1,
          "work_life_balance_rating": 3.7,
          "stock": null,
          "year_founded": 2003,
          "reviews_link": "https://www.glassdoor.com/Reviews/Dembach-Goo-Informatik-Reviews-E2888762.htm",
          "jobs_link": "https://www.glassdoor.com/Jobs/Dembach-Goo-Informatik-Jobs-E2888762.htm",
          "faq_link": "https://www.glassdoor.com/FAQ/Dembach-Goo-Informatik-Questions-E2888762.htm",
          "competitors": [],
          "office_locations": [
            {
              "city": "Cologne",
              "country": "Germany"
            }
          ],
          "best_places_to_work_awards": []
        }
      ]
    }
  }
}
```
