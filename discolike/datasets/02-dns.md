# DNS Dataset

A continuously updated dataset covering all domains that we see through our certificates firehose, including domains referenced in the subject alternative name data field.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| fqdn | String | Fully qualified domain name for which the DNS record was queried. |
| domain | String | Domain portion of the FQDN. |
| record_type | String | Type of DNS record, currently supported record types: A/MX/TXT/SOA/NS/CNAME/DNAME. |
| record_data | Array(String) | DNS data for the specified record type. |
| record_date | Date (YYYY-MM-DD) | Date in which the DNS record was queried. |
