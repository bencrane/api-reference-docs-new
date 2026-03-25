# Server Events Documentation Summary

This documentation outlines how Vapi sends events to your Server URL via POST requests containing message objects with specific types and payloads.

## Key Event Categories

**Events Requiring Responses:**
- "assistant-request" (must respond within 7.5 seconds)
- "tool-calls"
- "transfer-destination-request"
- "knowledge-base-request"

**Informational Events:** Most others don't require responses but include metadata like phone numbers, timestamps, and call artifacts.

## Major Event Types

**Function Calling:** When assistants trigger tools, your server receives tool specifications and must return results with the corresponding tool call IDs.

**Assistant Retrieval:** For inbound calls without assigned assistants, the system requests one from your server. The response can include an existing assistant ID, a new inline assistant configuration, or a transfer destination.

**Status Updates:** Track call lifecycle events (scheduled, queued, ringing, in-progress, forwarding, ended).

**Call Reports:** End-of-call messages contain recordings, transcripts, and message history.

**Conversation Data:** Updates include current conversation messages and OpenAI-formatted versions.

**Transcripts & Speech:** Partial/final transcripts and speech status indicators.

**Transfers:** Both immediate transfers and requests for dynamic destination determination.

**Advanced Features:** Custom knowledge bases, voice input/output, smart endpointing, and phone call control delegation.

## Critical Timing Note

The "assistant-request" webhook has a fixed 7.5-second end-to-end limit enforced by telephony providers. Optimization strategies include returning quickly with existing IDs and enriching context asynchronously after call start.
