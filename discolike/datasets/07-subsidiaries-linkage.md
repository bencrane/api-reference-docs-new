# Subsidiaries Linkage Dataset

This dataset maps the connections between business domains by leveraging alternative domain names listed in SSL certificates, facilitating the identification of related entities.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| source_domain | String | Normalized domain name (excluding any subdomain). |
| source_fqdn | String | The source FQDN used to establish domain linkages within this dataset. |
| source_score | Unsigned Int32 | Domain score computed from certificates history, numeric number, values (1 - 800). |
| linked_domain | String | Normalized linked domain name (excluding any subdomain). |
| linked_fqdn | String | The linked FQDN used to establish domain linkages within this dataset. |
| linked_score | Unsigned Int32 | Domain score computed from certificates history, numeric number, values (1 - 800). |
| record_date | Date (YYYY-MM-DD) | Date in which we compiled the record. |
| parent_domain | String | Domain with the highest score among all source-linked pairs. |
| child_domain | String | Remaining domains with scores lower than the parent domain's score. |
