# Text Search API Documentation

## Overview

The Text Search endpoint enables searching through conversation transcripts using full-text and fuzzy matching capabilities. It's a GET request to `https://api.elevenlabs.io/v1/convai/conversations/messages/text-search`.

## Core Functionality

This API allows users to search conversation messages with a required text query parameter while supporting numerous optional filters for refining results.

## Required Parameters

- **text_query**: The search query string for matching against conversation content

## Optional Filtering Parameters

**Conversation Metadata:**
- `agent_id`: Filter by specific agent
- `user_id`: Filter by user who initiated conversations
- `branch_id`: Filter by branch identifier

**Call Performance:**
- `call_successful`: Results filter (success/failure/unknown)
- `call_start_before_unix`: Upper bound timestamp in seconds
- `call_start_after_unix`: Lower bound timestamp in seconds
- `call_duration_min_secs` / `call_duration_max_secs`: Duration range filters

**Quality Metrics:**
- `rating_min` / `rating_max`: Rating range (1-5 scale)
- `has_feedback_comment`: Boolean filter for feedback presence

**Tool & Language Filters:**
- `tool_names`: Tools used during calls
- `tool_names_successful`: Successfully executed tools
- `tool_names_errored`: Tools that encountered errors
- `main_languages`: Language codes (e.g., "en", "es")

**Evaluation & Data:**
- `evaluation_params`: Format as "criteria_id:result" (repeatable)
- `data_collection_params`: Format as "id:op:value" with operators (eq|neq|gt|gte|lt|lte|in|exists|missing)

**Pagination & Output:**
- `page_size`: Results per page, maximum 50 (default: 20)
- `cursor`: Pagination token for subsequent pages
- `summary_mode`: Include/exclude transcript summaries (default: exclude)
- `conversation_initiation_source`: Origin platform identifier

## Response Structure

The API returns a `MessagesSearchResponse` containing:

- **meta**: Pagination metadata (total, page, page_size)
- **results**: Array of `MessagesSearchResult` objects including:
  - conversation_id and agent_id
  - transcript_index: Message position in conversation
  - chunk_text: Actual transcript content
  - score: Relevance similarity metric
  - conversation_start_time_unix_secs
  - agent_name (optional)
- **next_cursor**: Token for fetching additional results
- **has_more**: Boolean indicating remaining results

## HTTP Details

**Method**: GET
**Authentication**: Via `xi-api-key` header
**Success Response**: HTTP 200 with JSON payload
**Error Response**: HTTP 422 with validation errors

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io

## SDK Support

Code examples are provided for TypeScript/JavaScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to construct requests with various parameter combinations.
