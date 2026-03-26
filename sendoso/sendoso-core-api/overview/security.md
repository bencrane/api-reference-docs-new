# Security

Sendoso implements multiple protective mechanisms for API interactions, including OAuth authentication, authorization frameworks, encrypted data transmission, request rate limiting, and comprehensive logging practices.

## Authentication

The system employs OAuth standards to authenticate your API requests, requiring access tokens in request headers.

## Authorization

Access control relies on permissions associated with the OAuth application and the scopes available and requested to govern resource access and permitted actions.

## Data Protection

Transmissions use dual encryption:

- **AES-256** standards for stored data (at rest)
- **HTTPS TLS 1.2 with RSA 256-bit** for transit security

## Rate Limiting

The API enforces usage limits that temporarily block IP addresses exceeding thresholds, preventing resource abuse.

## Monitoring

All requests to the Sendoso API are logged, including the IP address of the request, the request method, the resource requested, and the response status.

## Recommendations

Users should revoke API keys when no longer needed. Security inquiries can be directed to developers@sendoso.com.
