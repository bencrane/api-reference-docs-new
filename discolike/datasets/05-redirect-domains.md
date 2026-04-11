# Redirect Domains Dataset

The Redirect Domains Dataset identifies and maps domain linkages based on URL redirects, highlighting the connections between domains through their redirection patterns.

This dataset captures multiple redirect types, including HTTP 301 and 302, JavaScript redirects, meta tag redirects, and more.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| source_domain | String | Normalized domain name (excluding any subdomain). |
| source_fqdn | String | The source FQDN used to establish domain linkages within this dataset. |
| linked_domain | String | Normalized linked domain name (excluding any subdomain). |
| linked_fqdn | String | The linked FQDN used to establish domain linkages within this dataset. |
| record_date | Date (YYYY-MM-DD) | Date in which we compiled the record. |
