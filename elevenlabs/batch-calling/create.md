# Submit Batch Calling Job

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/batch-calling/submit` for scheduling outbound calls to multiple recipients simultaneously.

## Core Functionality

This endpoint enables users to "submit a batch call request to schedule calls for multiple recipients." The service processes these requests and returns a response containing batch details and status information.

## Required Parameters

The request body must include three mandatory fields:

- **call_name** (string): A descriptive identifier for the batch operation
- **agent_id** (string): The conversational AI agent that will conduct the calls
- **recipients** (array): A collection of `OutboundCallRecipient` objects containing contact details

## Optional Configuration

Additional parameters allow customization:

- **scheduled_time_unix**: Unix timestamp for delayed execution
- **timezone**: Geographic timezone for scheduling
- **target_concurrency_limit**: "Maximum number of simultaneous calls for this batch"
- **telephony_call_config**: Ringing timeout and provider settings
- **whatsapp_params**: WhatsApp-specific configuration for message-based calls
- **agent_phone_number_id**: Specific phone number identifier for calls

## Response Schema

Successful requests (HTTP 200) return a `BatchCallResponse` containing:

- Batch ID and status tracking
- Call counters (dispatched, scheduled, finished)
- Timestamps and timezone information
- Agent and phone provider details
- Current batch status (pending, in_progress, completed, failed, or cancelled)

## Available SDKs

The documentation provides code examples in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, demonstrating how to integrate batch calling functionality across various platforms.
