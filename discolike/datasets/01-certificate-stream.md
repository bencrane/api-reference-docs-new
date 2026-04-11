# Certificate Stream Dataset

Certificate information as we collect it from Certificate Authorities (CA), full worldwide coverage.

## Flat-File Layout

| Name | Format | Description |
|------|--------|-------------|
| domain | String | Normalized domain name (excluding any subdomain). |
| record_date | Date (YYYY-MM-DD) | Date in which we compiled the record. |
| fqdn | String | Fully Qualified Domain Name for the certificate, as appears in the certificate's subject. |
| secondary_domains | Array[String] | List of secondary domains and certificates, as appears in the certificate's secondary alternate domains. |
| date_from | DateTime (YYYY-MM-DD HH:MM:SS) | Start of certificate validity period. |
| date_to | DateTime (YYYY-MM-DD HH:MM:SS) | End of certificate validity period. |
| organization | String | Organization information for the certificate, as appears in the certificate's subject. |
| city | String | City information for the certificate, as appears in the certificate's subject. |
| state | String | State information for the certificate, as appears in the certificate's subject. |
| country | String | Country information for the certificate, as appears in the certificate's subject. |
| email | String | E-mail information for the certificate, as appears in the certificate's subject. |
| sha1 | String | The SHA-1 fingerprint of a certificate (SHA-1 digest value of the certificate's DER representation). |
| issuer_country | String | Country information for the issuer of the certificate, as appears in the issuer. |
| issuer_organization | String | Organization information for the certificate issuer, as appears in the certificate's issuer. |
