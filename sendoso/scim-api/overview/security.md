# Security

Sendoso's SCIM API incorporates multiple protective measures for data safeguarding and access control.

## Authentication

The system employs OAuth standards to authenticate your API requests. Access tokens must be included in request headers for each call.

## Authorization

Access follows a permission-based model tied to OAuth application credentials and SCIM scope assignments. Accessing resources beyond SCIM requires separate Core API credentials with distinct permissions.

## Data Protection

Information undergoes encryption both at rest using AES-256 and in transit via HTTPS TLS 1.2 with RSA 256-bit encryption, providing secure internet transmission.

## Rate Limiting

The API enforces rate limits to prevent misuse and guarantee equitable resource distribution. Exceeding these thresholds results in temporary IP blocking.

## Request Logging

The system maintains comprehensive logs capturing IP addresses, request methods, accessed resources, and response statuses to enable monitoring for suspicious patterns and security incident detection.

## Key Revocation

Upon completing API usage, revoking your API key is advised as a best practice.

For security questions, contact developers@sendoso.com.
