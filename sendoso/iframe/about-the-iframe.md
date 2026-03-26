# About the iFrame

With the Sendoso iFrame we handle the sending & user experience; you display it. The Sendoso iFrame allows applications to embed gift-sending functionality without leaving their platform.

## Use Cases

- Embedding in internal CRMs or channel partner applications
- Support for messaging applications and custom integrations

## Setup Requirements

1. Email developers@sendoso.com with your use case and application URL for authorization
2. Enable Sendoso icon and create iFrame link
3. Provide sender/recipient information and delivery location details

## Technical Specifications

| Property | Value |
|----------|-------|
| URL | `https://app.sendoso.com/v2/plugin/sends` |
| Width | 435px |
| Height | 500px |

## URL Parameters for Prepopulation

The iFrame supports URL parameters to prepopulate recipient data:

| Parameter | Description |
|-----------|-------------|
| `name` | Recipient's name |
| `email` | Recipient's email |
| `address1` | Street address line 1 |
| `address2` | Street address line 2 |
| `state` | State/province |
| `zip` | Postal code |
| `country` | Country |

All special characters must be HTML encoded.
