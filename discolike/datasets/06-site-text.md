# Site Text Dataset

Extracted text and site links. Available only in JSON format and as a daily feed.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| url | String | The page source for content extraction. |
| domain | String | Normalized domain name (excluding any subdomain). |
| extraction_date | Date (YYYY-MM-DD) | Date in which the content was extracted. |
| page | String | URL classification: home, about, careers, documentation, location, policy, products, or services. |
| extracted_text | String | Text as extracted from the URL, cleaned up from all HTML tags. |
| extracted_links | Array[LinkObject] | Compilation of URL links and their corresponding or alternative text from `<a>` tags. |

Note: LinkObject represents a key/value pairing of Link Text (String) to URL (String).
