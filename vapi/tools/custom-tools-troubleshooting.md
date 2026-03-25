# Custom Tools Troubleshooting - Complete Documentation

## Overview

This guide helps developers resolve common issues with custom tool integrations in Vapi assistants, covering diagnosis of triggering failures, response format errors, parameter issues, and multi-tool scenarios.

## Quick Diagnosis

Four main problem categories:

1. **Tool won't trigger** - Assistant fails to call the tool despite appropriate conditions
2. **No result returned** - Logs display "no result returned" messages
3. **Response ignored** - Tool data exists but assistant doesn't incorporate it
4. **Parameters cut off** - Tool inputs or outputs experience truncation

## Tool Won't Trigger

### Prompting Requirements

The documentation emphasizes using "exact tool name in your assistant instructions." For example, if a tool is named `get_weather`, reference that precise name rather than generic alternatives like `weather_tool`.

### Schema Validation

Proper tool schemas must include:
- Clear parameter definitions with type specifications
- Required parameters array listing mandatory fields
- Strict validation enabled via `"strict": true`

## No Result Returned Error

### Correct Response Format

All webhooks must return this structure:

```json
{
  "results": [
    {
      "toolCallId": "call_123",
      "result": "Single-line string response"
    }
  ]
}
```

### Critical Rules

- **HTTP status**: "Always return HTTP 200, even for errors"
- **String format**: No line breaks (`\n`) within response strings
- **ID matching**: The `toolCallId` must "exactly match the ID from the request"
- **Data types**: Both `result` and `error` fields must be strings, never objects

## Response Ignored

Common causes include formatting issues, incorrect HTTP status codes, and mismatched tool call IDs in parallel execution scenarios.

## Token Truncation

Default token limit is 100. Adjust via `"maxTokens": 500` for complex operations. Monitor logs for "Token truncation warnings."

## Multiple Tools

Return results in the same order as triggered calls, with proper `toolCallId` correspondence for each.

## Async vs Sync Behavior

- **Sync (default)**: Webhook response determines resolution
- **Async**: Tool marked resolved immediately for long-running operations

## Debugging Reference

Common error messages and solutions:

| Error | Solution |
|-------|----------|
| "ok, no result returned" | Verify JSON structure |
| "Tool call ID mismatches" | Ensure exact ID correspondence |
| "HTTP errors" | Return status 200 consistently |
| "Schema validation errors" | Check required parameters array |
| "Token truncation warnings" | Increase maxTokens setting |
