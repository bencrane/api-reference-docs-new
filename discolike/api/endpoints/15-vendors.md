# Vendors API [Team]

Find vendor relationships for a domain. Uses data from our Vendor Integration Dataset.

## Endpoint

```
GET https://api.discolike.com/v1/vendors
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Query domain |
| match | Match as `client` or `vendor` |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| client_domain | String | Normalized client domain |
| client_fqdn | String | Client's full URL |
| vendor_domain | String | Normalized vendor domain |
| vendor_fqdn | String | Vendor's full URL (white-label) |
| record_date | Date | Date the record was compiled |

## Example Request

```
curl "https://api.discolike.com/v1/vendors?domain=acmemanufacturing.com&match=client" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
[
  {
    "client_domain": "acmemanufacturing.com",
    "vendor_domain": "cloudprovider.com",
    "client_fqdn": "analytics.acmemanufacturing.com",
    "vendor_fqdn": "analytics-12345.us-east-1.cloudprovider.com",
    "record_date": "2024-06-07"
  },
  {
    "client_domain": "acmemanufacturing.com",
    "vendor_domain": "cdnservice.net",
    "client_fqdn": "assets.acmemanufacturing.com",
    "vendor_fqdn": "acme-cdn-prod.cdnservice.net",
    "record_date": "2024-03-01"
  }
]
```
