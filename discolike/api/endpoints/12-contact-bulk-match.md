# Contact Bulk Match API [Starter]

Match a list of person names to contacts in bulk. Uses text search for fast matching, with optional full-data enrichment from the contacts database.

## Endpoint

```
POST https://api.discolike.com/v1/contacts/bulk-match
```

## Request Body (JSON)

| Parameter | Type | Description |
|-----------|------|-------------|
| queries | Array | List of match queries (required, 1-500 items). Each item has: `name` (required), `company_name` (optional), `domain` (optional), `person_country` (optional ISO-3166-1 alpha-2 code). |
| enrich | Boolean | Set to `true` to hydrate matches with full contact data from the contacts database. Counts toward usage. Defaults to `false`. |
| limit | Integer | Maximum matches per query, range 1-20 (optional, defaults to 10). |

## Example Request

```bash
curl -X POST "https://api.discolike.com/v1/contacts/bulk-match" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "queries": [
      {"name": "Jane Doe", "company_name": "Acme Corp"},
      {"name": "John Smith", "domain": "techstartup.io"}
    ],
    "enrich": false,
    "limit": 5
  }'
```

## Initial Response

```json
{ "task_id": "e362cb75-35e2-4006-a239-3d87a7472872" }
```

## Check Status

```bash
curl "https://api.discolike.com/v1/bulkcontactmatch/status/{task_id}" \
  -H "x-discolike-key: API_KEY"
```

```json
{ "status": "in_progress", "progress": 45 }
```

## Final Response

When `enrich` is `false`, matches contain lightweight results (persona_id, name, title, domain, company_name, match_score):

```json
{
  "status": "completed",
  "progress": 100,
  "results": [
    {
      "query": { "name": "Jane Doe", "company_name": "Acme Corp", "domain": null },
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
  ]
}
```

When `enrich` is `true`, matches contain full contact data (email, phone, social URLs, seniority, department, skills, etc.) -- same fields as Search Contacts results.

---

Previous: [Contact Match](/v1/docs/api/endpoints/contact-match/) | Next: [Count](/v1/docs/api/endpoints/count/)
