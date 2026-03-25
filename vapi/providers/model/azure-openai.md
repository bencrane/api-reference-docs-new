# Azure OpenAI Integration with Vapi

## Overview

Vapi enables integration with custom Azure OpenAI instances, allowing organizations to leverage their own rate limits, regional deployments, and specific configurations while maintaining control over billing and data residency.

## Key Requirements

Before setup, you'll need:
- An active Azure subscription
- Deployed Azure OpenAI Service resource
- Configured model deployments
- API keys and endpoint information

## Critical Configuration Details

**Deployment Naming**: Your Azure deployment names must "exactly match" one of Vapi's supported models. Custom naming conventions aren't supported—for instance, use `gpt-4o-2024-11-20` rather than custom identifiers.

**Endpoint Format**: Use only the base endpoint URL (e.g., `https://your-resource.openai.azure.com`), not the full completions path.

## Supported Models

Vapi supports:
- GPT-4.1 series (2025-04-14 variants)
- GPT-4o models (2024-11-20, 2024-08-06, and others)
- GPT-4 Turbo and standard versions
- GPT-3.5 Turbo models

## Regional Availability

Deployments can be configured across 18 Azure regions, including US, Europe, Asia-Pacific, and Middle East locations. The documentation recommends selecting regions closest to your users for optimal performance.

## Setup Process

Configuration involves gathering Azure details, verifying deployment names match supported models, entering credentials in the Vapi dashboard, and testing the connection with a sample assistant.

## Troubleshooting

Common issues include endpoint URL formatting errors, mismatched deployment names, and invalid API credentials—each with specific verification steps outlined in the documentation.
