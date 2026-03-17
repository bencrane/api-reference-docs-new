# BlitzAPI Documentation

## Overview
BlitzAPI provides a programmable interface to access verified B2B data from a proprietary LinkedIn-based dataset covering 380M+ contacts worldwide. The platform targets Growth Engineers and RevOps teams building automated lead pipelines.

## Core Feature: Waterfall ICP Search
The platform's signature capability uses hierarchical filtering to identify decision-makers. Users define a priority hierarchy (e.g., CEO → VP Sales → Sales Director), and the API executes a cascading search until it matches your criteria.

The three-step process involves:
1. **Define priorities** through JSON rules
2. **Intelligent routing** that queries data in order and stops at first match
3. **Structured output** returning the most relevant contact

## Pricing Structure
BlitzAPI operates on flat-rate monthly subscriptions:

| Plan | Price | Features |
|------|-------|----------|
| **Unlimited Leads** | $399/mo | Waterfall ICP, Company Search, Employee Finder, Domain→LinkedIn tools |
| **Unlimited Email** | $499/mo | Adds email enrichment (62M+ emails, 97% accuracy) |
| **Unlimited Phone Numbers** | $599/mo | Adds US phone enrichment (40M+ mobile numbers) |

No per-request fees or overage charges apply.

## Key Integrations
Compatible platforms include n8n, Make, Zapier, Clay, Airtable, HubSpot, Salesforce, and Smartlead. As long as your tool can make an HTTP POST request, it works with BlitzAPI.

## Getting Started Resources
- [Quick Start](guide/getting-started/quickstart.md) - API key setup
- [Authentication](guide/getting-started/authentication.md) - How to authenticate
- [Code Examples](guide/getting-started/code-examples.md) - Full workflow documentation
- [API Reference](api-reference/) - OpenAPI specs and endpoint details
- [Pricing & Plans](guide/concepts/pricing-unlimited.md) - Technical limits details
