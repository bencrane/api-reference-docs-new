# Enigma Gov Archive Documentation

> https://documentation.enigma.com/guides/gov-archive

## Overview

The Gov Archive feature enables searching government records about businesses across 7,000+ federal, state, and municipal datasets. Users can query permits, violations, filings, licenses, and regulatory records through AI assistants, custom agents, or direct API access.

## Prerequisites

- An Enigma account (available at console.enigma.com/register)
- Active subscription to Max plan or Enterprise plan
- API key required for custom agents and direct API access (available in Console settings)

## Using Gov Archive with AI Assistants

Gov Archive integrates with Claude, ChatGPT, Gemini CLI, and other platforms through the `search_gov_archive` tool. Setup for Claude involves:

1. Opening Settings > Connectors > Add custom connector
2. Entering "Enigma" as name and `https://mcp.enigma.com/http` as Remote MCP Server URL
3. Clicking Connect and logging in with Enigma credentials

Example queries include searching for specific business permits, violations, and regulatory filings.

## Custom Agent Integration

Integration with agent frameworks (OpenAI Agents SDK, LangChain, CrewAI, AutoGen) requires an API key and connection to the MCP server at `https://mcp.enigma.com/http-key`.

## Direct API Access

Direct API calls use JSON-RPC requests to the MCP HTTP endpoint with the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | string | — | Search string for business name and address |
| original_prompt | string | — | Full original user prompt for context |
| page | integer | 1 | Page number for pagination |
| limit | integer | — | Maximum results per page |
| historical_data | boolean | false | Include archived records |
| category | string | — | Filter by record category |
| resource_ids | array | — | Filter to specific dataset IDs |
| include_row_details | boolean | — | Include full row_details object |

## Response Structure

Responses contain `dataset_info` (source metadata) and `matched_row_info` (matched records). The `row_details` field contains complete original government records with dataset-specific fields.

## Available Record Categories

- Business registrations (Secretary of State filings, DBA registrations)
- Permits and licenses (liquor, cannabis, professional licenses)
- Health and safety (food inspections, code violations)
- Court filings and liens (UCC liens, bankruptcy filings)
- Environmental compliance (EPA records, remediation data)
- Workplace safety (OSHA violations, citations)
- Government contracts (USA Spending data)
- Financial incentives (economic programs, tax credits)

## Rate Limits

| Plan | Daily Limit | Monthly Limit |
|------|------------|--------------|
| Pro | 500 | 6,000 |
| Max | 500 | 6,000 |
| Enterprise | Configurable | Configurable |

## Related Pages

- [AI MCP Setup Guides](/guides/ai-mcp)
- [KYB Verification](/kyb/verify-identity)
- [Rate Limits](/resources/rate-limits)
- [Console Overview](/console/)
