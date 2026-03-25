# Authentication Management for Vapi CLI

## Overview
The Vapi CLI enables sophisticated authentication workflows, supporting multiple accounts, organizations, and environments. This capability suits developers managing various teams, client projects, or production/staging deployments.

## Core Authentication Methods

**OAuth Login (Recommended)**
The default approach prioritizes security: `vapi login` initiates browser-based authentication with automatic token refresh and secure local storage.

**API Key Authentication**
For automation scenarios, developers can pass keys via environment variables (`VAPI_API_KEY`) or command flags, or store them in `~/.vapi-cli.yaml`.

## Multi-Account Workflows

Users can maintain multiple authenticated accounts simultaneously. The command `vapi auth status` displays the active account plus additional registered accounts. Switching between accounts uses `vapi auth switch [alias|email]`.

Key account information includes user identity, organization membership, API access permissions, and environment designation (production/staging/custom).

## Security Considerations

**Credential Storage:** The CLI leverages platform-native secure storage—Keychain on macOS, Secret Service on Linux, and Credential Manager on Windows.

**Environment Separation:** Maintaining distinct accounts prevents accidental operations across development and production systems.

**CI/CD Integration:** Automated workflows should use environment variables like `VAPI_API_KEY` rather than hardcoded credentials.

**Access Revocation:** The command `vapi auth logout [account]` removes accounts; `--all` flag logs out everywhere.

## Advanced Configuration

For enterprise deployments, custom API endpoints are configurable via `--base-url` flags. Service accounts and proxy settings support corporate infrastructure requirements.

## Best Practices Summary

- Use descriptive account aliases (e.g., "prod-acme" instead of "test1")
- Conduct regular authentication audits via `vapi auth status`
- Maintain team documentation mapping aliases to organizations
- Reserve OAuth for interactive use; restrict API keys to automation
