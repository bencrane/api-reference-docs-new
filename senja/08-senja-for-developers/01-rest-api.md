---
title: "REST API"
url: "https://support.senja.io/rest-api-wbnz4"
path: "/rest-api-wbnz4"
---

# REST API

The Senja REST API is available on the Starter and Pro plan. You can see the available plans on our pricing page.

With Senja's API, you can easily build custom workflows for testimonial collection and sharing, or integrate Senja with tools that we currently do not have 1st party integrations for.

## Getting started

Senja's API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

### Endpoint

```
https://api.senja.io/v1
```

### Authentication

You can find your API in the Automate section on your Senja dashboard.

To authenticate your requests, you need to pass the newly created key as an Authorization header:

```bash
curl "https://api.senja.io/v1/testimonials" \
  -H "Content-Type: application/json" \
  -H "Authorization: <Replace this with your API Key>"
```

### Endpoints

- `GET /testimonials`: Retrieves all the testimonials in your Senja project.
- `POST /testimonials`: Creates a new testimonial.
- `GET /testimonials/[id]`: Retrieves a specific testimonial from your Senja project.

## List all testimonials in your Senja project

**Endpoint:** `GET /testimonials`

This endpoint returns a list of all the testimonials in your Senja project. You can also filter the testimonials by tags, type, rating and integration.

By default, it returns the most recent testimonials first (date), but you can sort by rating (rating). You can also change the direction of the sort (asc/desc).

### Query Parameters

| Parameter | Possible options | Default | Description |
|-----------|-----------------|---------|-------------|
| sort | date, rating | date | Sort by date or rating. |
| order | asc, desc | desc | Order in ascending or descending order. |
| approved | true, false | NULL | List approved or unapproved testimonials. If left empty, both are retrieved. |
| rating | int | NULL | List testimonials matching a rating. |
| type | text, video | NULL | List text or video testimonials. |
| integration | Integration | NULL | List testimonials matching a specific integration. |
| tags | string[] | [] | List testimonials matching specific tags. Use the names of the tags, not their ids. |
| lang | ISO 639 language code | NULL | Find testimonials written in or translated to a specific language. |
| limit | int between 1 and 1000 | 100 | Limit testimonials returned by the API. |
| page | int | NULL | Use this to paginate between responses. |

> Working with dates? Due to limitations with our data providers, exact review dates may not always be available. We recommend using relative dates (e.g., "3 months ago") for a better user experience. Learn more about handling review dates.

### Example: Find 1 and 2-star reviews

```bash
curl "https://api.senja.io/v1/testimonials?rating=2" \
  -H "Authorization: Bearer API_KEY"
```

## Add a testimonial to your Senja Project

**Endpoint:** `POST /testimonials`

This endpoint allows you to add a new testimonial to your Senja project. You must provide the required information in the form of a JSON payload in the request body.

### Example Request

```bash
curl -X POST "https://api.senja.io/v1/testimonials" \
  -H "Authorization: Bearer API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "text",
    "title": "Amazing product!",
    "text": "This product has changed my life!",
    "rating": 5,
    "endorser": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }'
```

### JSON Body Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | string | Yes | The type of testimonial. Possible values: "text" or "video". |
| title | string | No | The title of the testimonial. |
| text | string | No | The text content of the testimonial. |
| rating | number | No | The rating of the testimonial (e.g., 1-5). |
| url | string | No | The URL of the testimonial. |
| date | string | No | The date of the testimonial (ISO 8601 format). |
| approved | boolean | No | The approval status of the testimonial. |
| thumbnail_url | string | No | The URL of the testimonial's thumbnail image. |
| form_id | string | No | The ID of the form associated with the testimonial. |
| customer_name | string | Yes | The name of the customer. |
| customer_email | string | No | The email address of the customer. |
| customer_avatar | string | No | The URL of the customer's avatar. |
| customer_company_logo | string | No | The URL of the customer's company logo. |
| customer_company | string | No | The customer's company. |
| customer_tagline | string | No | The customer's tagline. |
| customer_username | string | No | The customer's username. |
| customer_url | string | No | The URL of the customer's website or social media profile. |
| integration | Integration | No | The integration associated with the testimonial. |
| tags | string[] | No | An array of strings representing tags associated with the testimonial. |
| video_url | string | No | The URL of the video testimonial. Required if type is "video". |
| media[] | object[] | No | A list of images associated with the testimonial. |
| media[].alt | string | No | The alternative text for the media. |
| media[].url | string | No | The URL of the media. |
| media[].type | string | No | The type of media (image, video). |

## Shareable Testimonial URL

You can construct a shareable URL to link directly to a specific testimonial:

```
https://senja.io/p/[permalink]/t/[testimonial_id]
```

Replace `[permalink]` with your project's permalink and `[testimonial_id]` with the ID of the testimonial you want to share.

## Supported integrations

```
twitter, linkedin, google, facebook, airbnb, amazon, app_store, apple_podcasts,
appsumo, capterra, chrome-web-store, embedsocial, fiverr, g2, homestars,
instagram, play-store, product-hunt, realtor, reddit, skillshare, sourceforge,
testimonial-to, tiktok, trustpilot, udemy, upwork, whop, wordpress, yelp,
youtube, zillow
```
