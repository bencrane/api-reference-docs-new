# Migrating from Trieve - Complete Documentation

## Overview Section

Trieve's cloud service is "shutting down on November 1st, 2025," requiring users to migrate their knowledge bases beforehand. The guide presents two primary migration pathways designed to maintain assistant functionality.

## Key Migration Options

**Custom Knowledge Base** suits users seeking automatic retrieval on every message, offering complete infrastructure control but requiring server development expertise.

**Google Knowledge Base** provides a simpler alternative, functioning as a tool the assistant calls selectively, though it depends on Google's Gemini models for processing.

## Important Behavioral Distinction

A critical note emphasizes that "Google knowledge bases work as tools that the assistant calls when needed based on your prompt instructions. Custom knowledge bases are queried on every user request automatically."

The documentation recommends Custom Knowledge Base migration to preserve existing Trieve behavior patterns, ensuring consistent automatic knowledge retrieval.

## Comparison Matrix

| Factor | Custom KB | Google KB |
|--------|-----------|-----------|
| Retrieval | Every message | Tool-based |
| Latency | Lower | Higher |
| Complexity | High | Low |
| Maintenance | Server required | None |
| Cost | Hosting fees | Included |

## Migration Steps Overview

**Custom Knowledge Base** involves: exporting data from Trieve, setting up a custom server with vector database infrastructure, creating the knowledge base via API, and updating assistant configuration.

**Google Knowledge Base** requires: file preparation from Trieve exports, uploading files to Vapi, creating query tools, and updating assistant settings with explicit tool references.

## Critical Post-Migration Actions

Users must test assistants thoroughly, monitor response quality, remove legacy Trieve configurations, and delete old credentials from their dashboard to complete the transition successfully.
