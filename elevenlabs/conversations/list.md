# List Conversations API Documentation

## Overview

This endpoint retrieves all conversations from agents owned by the user, with optional filtering for specific agents.

**Endpoint:** `GET https://api.elevenlabs.io/v1/convai/conversations`

## Key Parameters

The API accepts numerous optional query parameters for filtering:

- **Pagination:** `cursor` for fetching subsequent pages, `page_size` (max 100, default 30)
- **Agent Filtering:** `agent_id`, `branch_id`
- **Call Metrics:** `call_duration_min_secs`, `call_duration_max_secs`, `call_successful`
- **Timing:** `call_start_before_unix`, `call_start_after_unix` (Unix timestamps in seconds)
- **Ratings:** `rating_min`, `rating_max` (1-5 scale)
- **User Data:** `user_id`, `has_feedback_comment`
- **Language & Tools:** `main_languages`, `tool_names`, `tool_names_successful`, `tool_names_errored`
- **Search & Summary:** `search` (full-text/fuzzy), `summary_mode` (exclude/include)
- **Advanced Filters:** `evaluation_params`, `data_collection_params`, `conversation_initiation_source`

## Response Structure

Successful responses (HTTP 200) return a `GetConversationsPageResponseModel` containing:

- `conversations`: Array of conversation objects with agent/call details
- `next_cursor`: Token for pagination
- `has_more`: Boolean indicating additional results available

Each conversation includes: agent ID, conversation ID, start time, duration, message count, status, success evaluation, transcript summary, language, tools used, and optional ratings.

## SDK Support

Code examples are provided for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift implementations.
