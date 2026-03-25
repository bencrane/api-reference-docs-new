# Server Authentication Documentation

## Overview

Vapi implements a credential-based authentication system that replaces inline authentication. Users create Custom Credentials through the dashboard and reference them using `credentialId` in server configurations. This approach enables "better security, reusability, and centralized management of your authentication credentials."

## Quick Start Process

The setup involves three steps:
1. Creating a Custom Credential in the dashboard (selecting authentication type and entering credentials)
2. Referencing the credential ID in assistant server configuration
3. Testing the webhook to verify authentication works

## Authentication Types Available

**Bearer Token Authentication**
The most common method, supporting standard Authorization headers or legacy X-Vapi-Secret headers. Configuration includes credential name, token value, header name, and optional Bearer prefix.

**OAuth 2.0 Authentication**
Supports client credentials flow with automatic token refresh. Requires Token URL, Client ID, Client Secret, and optional scopes. Vapi automatically handles token requests and includes access tokens in Authorization headers.

**HMAC Authentication**
Provides signature-based authentication for verifying request integrity. Configuration includes secret key, hash algorithm, signature header name, optional timestamp header, and payload format.

## Usage Locations

Credentials can be referenced in:
- Assistant server configurations
- Phone number configurations for incoming call authentication
- Tool function endpoints for securing specific operations

## Best Practices

The documentation recommends:
- Using descriptive credential names like "Production API Key"
- Regular credential rotation for enhanced security
- Secure storage of credential secrets (encrypted in dashboard, not viewable after creation)

## Migration Guidance

For users transitioning from inline authentication, the guide provides mapping:
- Inline `secret` field → Bearer Token credential with X-Vapi-Secret header
- Inline `headers` field → Bearer Token credential with appropriate header
- OAuth configurations → OAuth 2.0 credential

## Common Implementation Patterns

The documentation illustrates reusing credentials across multiple resources, environment-specific credential management, and service-specific credentials for different API endpoints.
