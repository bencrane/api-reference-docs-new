# List users

GET https://api.elevenlabs.io/v1/convai/users

"Get distinct users from conversations with pagination."

## Overview

This endpoint retrieves a paginated list of unique users who have engaged in conversations, with support for filtering and sorting options.

## Key Parameters

**Filtering Options:**
- `agent_id` - Identifies which agent's conversations to query
- `branch_id` - Narrows results by branch
- `call_start_before_unix` and `call_start_after_unix` - Unix timestamp filters for conversation dates
- `search` - Locates users by exact user ID match

**Pagination & Sorting:**
- `page_size` - Maximum results per request (defaults to 30)
- `sort_by` - Orders by either "last_contact_unix_secs" or "conversation_count"
- `cursor` - Enables fetching subsequent pages

## Response Structure

The successful response contains:
- `users` array with user records including ID, contact timestamps, conversation count, and last contact details
- `next_cursor` for pagination continuation
- `has_more` boolean indicating additional results

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Examples

Code implementations provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift languages.
