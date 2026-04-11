# Domain Status Dataset

Output of our processing pipeline, from resolving DNS to obtaining site page text including detection of parked domains.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| domain | String | Company domain and unique record identifier. |
| record_date | Date (YYYY-MM-DD) | Date in which we compiled the record. |
| status_code | UInt8 | Best status code for the record's compiled date. |
| status_reason | Nullable(String) | Additional verbose information for status_code. |

## Status Codes

| Code | Description |
|------|-------------|
| 0 | Non-Business or personal domain (portfolio page, personal page, school project, blog, etc.) |
| 1 | Business Domain |
| 2 | Parked Domain (registrar parked pages, e-commerce parked, hosted parked, etc.) |
| 3 | Re-scrape required; Additional re-scraping is necessary to generate a more meaningful status (usually caused by WAF protection or scraping limitations) |
| 4 | Re-scrape not required; Identified as a server default page, login page, page with no helpful info, etc. |
| 80 | Language not supported; Website is not in a language we currently process. The detected language is in the reason column. |
| 81 | Body too short; Content retrieved needs to be longer to be an actual website, despite receiving HTTP status 200 (in some cases, this is triggered by WAF). |
| 82 | Scraping unsuccessful; we could not to get website content in this pass. The HTTP error code is in the reason column. |
| 90 | NXDOMAIN (domain not exists) or SERVFAIL (DNS server cannot return a result) response returned from the DNS server. Some SERVFAILs are recoverable in future retries. |
