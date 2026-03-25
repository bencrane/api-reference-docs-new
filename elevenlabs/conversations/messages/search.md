# Smart Search

**GET** `https://api.elevenlabs.io/v1/convai/conversations/messages/smart-search`

This endpoint performs semantic searches across conversation transcripts, finding relevant messages based on meaning rather than keyword matching.

## Parameters

| Name | Location | Required | Type | Description |
|------|----------|----------|------|-------------|
| `text_query` | query | Yes | string | Search query text for semantic similarity matching |
| `agent_id` | query | No | string | The id of the agent you're taking the action on |
| `page_size` | query | No | integer | Results per page (max 50, default 20) |
| `cursor` | query | No | string | Pagination cursor from previous response |
| `xi-api-key` | header | No | string | API authentication key |

## Response Schema

The successful response (200) returns a `MessagesSearchResponse` containing:

- **meta**: Pagination metadata (total, page, page_size)
- **results**: Array of `MessagesSearchResult` objects with:
  - `conversation_id`: Conversation identifier
  - `agent_id`: Agent identifier
  - `agent_name`: Agent display name
  - `transcript_index`: Message position in transcript
  - `chunk_text`: Transcript content
  - `score`: Semantic similarity score
  - `conversation_start_time_unix_secs`: Conversation timestamp
- **next_cursor**: Pagination cursor for next page
- **has_more**: Boolean indicating additional results exist

Error responses (422) return validation errors.

## SDK Examples

Available implementations in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift demonstrating authentication and parameter usage.
