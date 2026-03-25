# Cloudflare R2 Documentation Summary

## Overview
The documentation explains how to configure assistants to record chat conversations and upload them to Cloudflare R2 buckets. Users must set up credentials and bucket settings through the Vapi dashboard's "Provider Credentials" section.

## Key Configuration Requirements

The page outlines eight credential settings needed for integration:

1. **Account Information**: Cloudflare Account ID and associated email address
2. **Authentication**: API Key/Token (Cloudflare uses these terms interchangeably)
3. **Bucket Details**: Bucket name and optional custom URL for CORS-enabled buckets
4. **Storage Organization**: Optional path prefix supporting date templating like `{{ "now" | date: "%Y/%m/%d" }}`
5. **Access Credentials**: 32-character Access Key ID and 64-character Secret Access Key

## Important Notes

- Users must generate R2 tokens and access keys through Cloudflare's developer documentation
- Custom bucket hostnames require CORS policy configuration
- The path prefix field accepts LiquidJS date formatting for automatic organization

An example configuration screenshot is included but not reproduced here.

**Resources**: The page links to Cloudflare's official guides for token generation and CORS setup.
