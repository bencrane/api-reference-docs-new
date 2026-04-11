# DiscoLike MCP Tools Reference

## Discovery & Company Data

| Tool | Description |
|------|-------------|
| `account-status` | Check subscription plan and limits |
| `usage-statistics` | View API usage for billing period |
| `discover-similar-companies` | Find companies matching examples, description, or natural language ICP prompt |
| `count-matching-domains` | Count matches before full search |
| `business-profile` | Get firmographic data |
| `digital-footprint-score` | Get score with breakdown |
| `growth-metrics` | View quarterly trends |
| `segment-domains` Pro | Group companies into clusters |
| `match-company-to-domain` Team | Find domain for company name |
| `extract-website-text` | Get cached text content from pre-crawled websites |
| `domain-redirects` Team | Get redirect mappings for a domain |
| `append-data` | Bulk-enrich domains with firmographics, growth, redirects, or domain status |
| `vendor-and-technology-data` Team | See technologies a company uses |
| `subsidiaries-and-parent-companies` Enterprise | Explore corporate hierarchies |
| `public-company-links` Enterprise | Find related domains sharing contact info |

## Contacts

| Tool | Description |
|------|-------------|
| `search-contacts` | Search for business contacts using similarity matching, domain filtering, or persona filters |
| `count-contacts` | Count contacts matching filters before running a full search |
| `contact-lookup` | Look up a specific contact by persona ID or LinkedIn profile |
| `match-contacts` | Match contacts by name/company via text search (lightweight, no usage cost) |
| `bulk-match-contacts` | Batch match a list of names to contacts with optional full-data enrichment |

## Saved Queries & Lists

| Tool | Description |
|------|-------------|
| `list-saved-queries` | List saved queries with their domains for use in inclusion/exclusion |
| `save-mcp-query` | Save MCP results as a reusable query |
| `save-exclusion-list` | Create an exclusion list from domains and/or persona IDs |
| `list-tags` | List all unique tags in your organization |
| `add-tags-to-query` | Add tags to a saved query for organization |
| `remove-tags-from-query` | Remove tags from a saved query |
| `get-domains-by-tags` | Get all domains from queries matching specified tags |

## Enrichment & Research

| Tool | Description |
|------|-------------|
| `run-discogen` | Run an LLM prompt against domains — offload enrichment to DiscoGen instead of analyzing each company yourself |
| `run-discogen-personas` | Run an LLM prompt against contacts — same as above but for people |
| `get-discogen-status` | Poll async DiscoGen task status and results |
| `cancel-discogen` | Cancel a running DiscoGen task |
| `list-discogen-integrations` | Check configured LLM and search providers before running DiscoGen |

## Example Conversation

1. "Find US-based SaaS companies with 50-200 employees that recently raised Series A"
2. AI calls `discover-similar-companies` with `icp_prompt` — automatically extracts filters (country: US, employee_range, category: SAAS), generates ICP text, suggests domains, and returns results in one call
3. "Segment these into market categories"
