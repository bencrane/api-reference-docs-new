# BizData Dataset

The BizData dataset is DiscoLike's core business intelligence feed. It provides comprehensive company profiles with firmographic data, contact details, and industry classifications.

## Dataset Contents

The BizData dataset encompasses:

- Company identification (name and domain)
- Physical location and communication details
- Social media presence
- Industry categorization
- Digital footprint score
- Business operational status and confidence metrics

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| domain | String | Primary domain. |
| name | String | Company name. |
| status | Object | Active/inactive status with confidence. |
| score | Integer | Digital footprint score (1-800). |
| address | Object | Street, city, state, zip, country. |
| phones | Array | Phone numbers. |
| public_emails | Array | Public email addresses. |
| social_urls | Array | Social media profile URLs. |
| description | String | Company description. |
| industry_groups | Object | Industry classifications with confidence. |
| employees | String | Employee count range (e.g., `51-200`, `1001-5000`). |

## Delivery Format

Available as JSON or delimited flat files with daily, weekly, or monthly update frequency.
