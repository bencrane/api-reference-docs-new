# Extract API [Starter]

Extract text content and links from any web page URL.

## Endpoint

```
GET https://api.discolike.com/v1/extract
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| url | URL of the web page to extract |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| language | String | Detected language (ISO-639-2 code) |
| text | String | Extracted text content |
| links | Object | Map of URLs to link text |

## Example Request

```bash
curl "https://api.discolike.com/v1/extract?url=https://acmecorp.com/" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "language": "en",
  "text": "Acme Corp - Enterprise Solutions. We provide cutting-edge software solutions for businesses of all sizes...",
  "links": {
    "https://acmecorp.com/products": "Products",
    "https://acmecorp.com/services": "Services",
    "https://acmecorp.com/about": "About Us",
    "https://acmecorp.com/contact": "Contact"
  }
}
```
