# PublicLink Dataset

The PublicLink dataset identifies relationships between business domains by matching shared public contact information — phone numbers, email addresses, and social media URLs — extracted from their websites. When two domains publish the same phone number, email, or social profile, they are linked as related entities.

## Use Cases

* **Corporate group mapping**: Identify brands, subsidiaries, and regional sites owned by the same organization (e.g., `acmehotels.com` and `acmeresorts.com` sharing `privacy@acmehotels.com`)
* **M&A and portfolio analysis**: Detect domains that began sharing contact info after an acquisition
* **Lead deduplication**: Avoid reaching out to the same organization through multiple domains
* **Fraud and spam detection**: Flag networks of domains sharing identical contact details, which can indicate lead-gen farms or templated sites

## Link Sources

| Source | How it works |
|--------|-------------|
| `email` | Identical email addresses extracted from both websites (e.g., `info@company.com` found on two different domains) |
| `social` | Identical social media profile URLs extracted from both websites (e.g., the same LinkedIn company page linked from two domains) |
| `phone` | Identical phone numbers extracted from both websites |

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| domain | String | Normalized domain name (excluding any subdomain). |
| linked_domain | String | Normalized linked domain name (excluding any subdomain). |
| record_date | Date (YYYY-MM-DD) | Date the record was compiled. |
| source | String | Link method: `email`, `social`, or `phone`. |
| link_values | Array[String] | The shared values establishing the link (email addresses, phone numbers, or social media URLs). |

## Example Record

```json
{
  "domain": "acmehotels.com",
  "linked_domain": "acmeresorts.com",
  "source": "email",
  "link_values": ["privacy@acmehotels.com", "dpo@acmehotels.com"],
  "record_date": "2024-07-17"
}
```

## API Access

Query PublicLink relationships via the [PublicLink API](/v1/docs/api/endpoints/publiclink/) (Enterprise plan) or the `public-company-links` MCP tool. Filter by domain and link source.

## Delivery

Available as JSON or delimited flat files. Updated periodically as new website crawl data is processed.
