# History API [Starter]

Returns historical and current SSL certificates for a domain (up to 10,000 records). Subdomains are normalized to root domain.

## Endpoint

```
GET https://api.discolike.com/v1/history
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to look up |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| domain | String | Normalized domain |
| certificates | Array | List of certificate records |

### Certificate Object

| Field | Type | Description |
|-------|------|-------------|
| sha1_fingerprint | String | SHA-1 fingerprint of the certificate |
| fqdn | String | Fully Qualified Domain Name |
| alternative_fqdn | Array | Subject Alternative Names |
| organization | String | Organization from certificate |
| city | String | City from certificate |
| state | String | State from certificate |
| country | String | Country code |
| date_from | DateTime | Certificate validity start |
| date_to | DateTime | Certificate validity end |

## Example Request

```shell
curl "https://api.discolike.com/v1/history?domain=acmecorp.com" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "domain": "acmecorp.com",
  "certificates": [
    {
      "sha1_fingerprint": "34ab1d0be3af8ad1c60b44e1805fb55ebb71e6e6",
      "fqdn": "api.acmecorp.com",
      "organization": "Acme Corporation",
      "city": "San Francisco",
      "state": "California",
      "country": "US",
      "date_from": "2024-04-27 18:57:41",
      "date_to": "2024-07-26 18:57:40",
      "alternative_fqdn": ["api.acmecorp.com"]
    }
  ]
}
```
