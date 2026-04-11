# DiscoLike API Documentation

## Introduction

The DiscoLike API provides programmatic access to a B2B company discovery and data enrichment platform covering 65M+ business domains across 180+ countries.

Users authenticate via API key using the `x-discolike-key` header. JSON responses follow REST conventions.

## Getting Started

1. Create an API key (requires DiscoLike account signup)
2. Authenticate using the header
3. Run discovery queries to find companies
4. Enrich results with firmographic data

## Core Workflows

| Workflow | Endpoints | Purpose |
|----------|-----------|---------|
| Find companies | Discover, Count, Segment | Search by lookalike domains, ICP text, or filters |
| Enrich domains | BizData, Score, Growth | Access firmographic profiles and growth metrics |
| Find contacts | Contacts, Contact Match, Contact Bulk Match | Search B2B contacts by persona or domain |
| Match & enrich lists | Match, Append | Resolve company names to domains |
| Map relationships | Vendors, Subsidiaries, PublicLink | Detect technology stacks, explore corporate hierarchies |

## AI Assistant Integration

Connect AI coding assistants directly to DiscoLike data via the MCP server. Supports Claude Code, Claude Desktop, Cursor, VS Code, and Windsurf.

## Datasets

Nine datasets available with monthly, weekly, or daily updates:

- BizData
- Domain Status
- Vendor Integration
- Subsidiaries
- Site Text
- DNS
- Certificate Stream
- Redirect Domains
- PublicLink

## Navigation

- [Datasets](/v1/docs/datasets/)
- [API Endpoints](/v1/docs/api/)
- [MCP Integration](/v1/docs/mcp/)
- [Guides](/v1/docs/guides/)
- [Supported Languages](/v1/docs/languages/)
