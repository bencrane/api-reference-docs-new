# Queries

## List Saved Queries

Returns saved queries that have associated domains. Use this to find queries for inclusion/exclusion in discovery.

```
GET /queries/saved
```

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| max_records | integer | 100 | Maximum records to return (1-1000) |
| offset | integer | 0 | Records to skip for pagination |

### Response

```json
{
  "results": [
    {
      "query_id": "uuid",
      "query_name": "My Discovery Query",
      "action": "discover",
      "user_name": "John Doe",
      "mtime": "2026-01-29T12:00:00",
      "domains": ["company1.com", "company2.com"],
      "domain_count": 2,
      "query_params": { ... }
    }
  ],
  "count": 50
}
```

### Plan Requirements

Requires STARTER plan or higher.

## Create Exclusion List

Create a new exclusion list from a list of domains or persona IDs. The list can be used for inclusion/exclusion filtering in discovery and contacts queries.

```
POST /queries/exclusion-list
```

### Request Body

Domain list example:

```json
{
  "query_name": "My Exclusion List",
  "domains": ["competitor1.com", "competitor2.com", "competitor3.com"]
}
```

Persona ID list example (from contacts search results):

```shell
curl -X POST "https://api.discolike.com/v1/queries/exclusion-list" \
  -H "x-discolike-key: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_name": "Contacted VPs", "persona_ids": [12345678, 87654321]}'
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| query_name | string | Yes | Name for the exclusion list (1-255 characters) |
| domains | array[string] | No | List of domains to save. Provide domains, persona_ids, or both. |
| persona_ids | array[integer] | No | Array of persona IDs to save (from contacts search results). Provide domains, persona_ids, or both. |

### Response

```json
{
  "query_id": "uuid",
  "query_name": "My Exclusion List",
  "domain_count": 3
}
```

### Plan Requirements

Requires STARTER plan or higher.

### Notes

- Maximum of 240,000 domains or 240,000 persona IDs per exclusion list (lists exceeding this limit are automatically truncated)
- Duplicate domains and persona IDs are automatically removed
- At least one of domains or persona_ids must be provided
- Lists created from contacts search results store persona IDs. Lists created from discover or other endpoints store domains. Both types appear in the same saved queries listing and can be used with `exclusion_query_id` or `inclusion_query_id` parameters.
- The created query has `action: "exclusion_list"`
- Use the returned `query_id` in the `inclusion_query_id` or `exclusion_query_id` parameters of the discover or contacts endpoints

## Update Query

Update the name and/or tags of a saved query. You can update just the name, just the tags, or both in a single request.

```
PATCH /queries/{query_id}
```

### Request Body

```json
{
  "query_name": "New Query Name",
  "tags": ["campaign-q1", "enterprise"]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| query_name | string | No | New name for the query |
| tags | array[string] | No | New list of tags (replaces existing) |

At least one field must be provided.

### Response

```json
{
  "query_id": "uuid",
  "query_name": "New Query Name",
  "tags": ["campaign-q1", "enterprise"]
}
```

### Plan Requirements

Requires STARTER plan or higher.
