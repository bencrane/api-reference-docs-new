# Vendor Integration Dataset

The Vendor Integration Dataset captures information about vendors who have implemented their services under a client's primary domain, utilizing white labeling.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| client_domain | String | Normalized domain name (excluding any subdomain). |
| client_fqdn | String | The client FQDN (Fully Qualified Domain Name) used for the implementation of the vendor solution. |
| vendor_domain | String | Normalized vendor domain name (excluding any subdomain). |
| vendor_fqdn | String | The vendor FQDN (Fully Qualified Domain Name) used in the client's white label implementation. |
| record_date | Date (YYYY-MM-DD) | Date in which we compiled the record. |
