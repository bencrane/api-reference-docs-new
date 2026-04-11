# Contact Match API [Starter]

Match a person name to contact profiles. Returns ranked candidates with match scores.

## Endpoint

```
GET https://api.discolike.com/v1/contacts/match
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| name | Person name to search for (required, minimum 2 characters). |
| company_name | Company name to narrow search (optional). |
| domain | Domain to filter by (optional). |
| person_country | Person's country code to filter by (optional). |
| limit | Maximum results to return, range 1-20 (optional, defaults to 10). |

## Example Request

```bash
curl "https://api.discolike.com/v1/contacts/match?name=John%20Smith&company_name=Acme%20Corp&limit=5" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "query": {
    "name": "Jane Doe",
    "company_name": "Acme Corp",
    "domain": null
  },
  "matches": [
    {
      "persona_id": 12345678,
      "name": "Jane Doe",
      "title": "VP of Sales",
      "domain": "acmecorp.com",
      "company_name": "Acme Corporation",
      "match_score": 95.2
    }
  ]
}
```

---

Previous: [Contacts](/v1/docs/api/endpoints/contacts/) | Next: [Contact Bulk Match](/v1/docs/api/endpoints/contact-bulk-match/)
