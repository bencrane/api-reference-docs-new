# Waterfall Logic

## Overview
The Waterfall ICP engine uses "smart routing" to identify the best decision-maker at target companies. Rather than returning unfiltered contact lists, it executes sequential search logic through a hierarchical preference cascade.

## Core Concept
The system attempts to find your ideal contact first. Only if unsuccessful does it proceed to alternative tiers.

**Example Flow:**
1. Seek a CMO
2. If unavailable, search for Marketing Manager
3. If still unsuccessful, escalate to CEO level

## Key Endpoint

| Property | Value |
|----------|-------|
| **Path** | `/v2/search/waterfall-icp-keyword` |
| **Latency** | Less than 600ms |
| **Plan** | Included in Unlimited Leads+ plans |
| **Max Results** | 25 contacts per query |

## Request Structure

### Top-Level Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `company_linkedin_url` | Yes | Full LinkedIn company URL |
| `cascade` | Yes | Ordered array of up to 8 search tiers |
| `max_results` | No | Default 1, maximum 25 |

### Per-Tier Cascade Parameters

| Parameter | Description |
|-----------|-------------|
| `include_title` | Job titles to match (supports partial matching) |
| `exclude_title` | Titles to filter out (interns, assistants, etc.) |
| `location` | LinkedIn country codes or "WORLD" for global scope |
| `include_headline_search` | Boolean to search LinkedIn bios when titles don't match exactly |

## Response Structure

Returns matched contacts ordered by cascade priority and relevance:

| Field | Description |
|-------|-------------|
| `icp` | Which tier matched (1 = highest priority) |
| `ranking` | Overall company relevance position |
| `what_matched` | Filter criteria that triggered the match |
| `person` | Full profile data including LinkedIn URL, experience, education, and skills |

## Example: Marketing First Strategy

This example targets Welcome to the Jungle with five cascading tiers, progressively expanding search criteria and geographic scope while maintaining quality filtering through exclusions.

```json
{
  "company_linkedin_url": "https://www.linkedin.com/company/wttj",
  "cascade": [
    {
      "include_title": ["CMO", "Chief Marketing Officer"],
      "exclude_title": ["assistant", "intern"],
      "location": ["WORLD"],
      "include_headline_search": false
    },
    {
      "include_title": ["VP Marketing", "Head of Marketing"],
      "exclude_title": ["assistant"],
      "location": ["US", "FR", "GB"],
      "include_headline_search": true
    },
    {
      "include_title": ["Marketing Director", "Director of Marketing"],
      "exclude_title": ["assistant", "coordinator"],
      "location": ["WORLD"],
      "include_headline_search": true
    },
    {
      "include_title": ["Marketing Manager"],
      "exclude_title": ["assistant", "junior"],
      "location": ["FR"],
      "include_headline_search": false
    },
    {
      "include_title": ["CEO", "Founder", "Co-Founder"],
      "exclude_title": [],
      "location": ["WORLD"],
      "include_headline_search": false
    }
  ],
  "max_results": 3
}
```
