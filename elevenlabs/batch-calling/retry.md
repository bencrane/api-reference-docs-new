# Retry Batch Calling Job

## Overview

The retry batch calling endpoint allows you to resend calls to recipients who failed to connect or didn't respond during the initial batch call attempt.

**Endpoint:** `POST https://api.elevenlabs.io/v1/convai/batch-calling/{batch_id}/retry`

## Request Parameters

- **batch_id** (path, required): The identifier for the batch call to retry
- **xi-api-key** (header, optional): Authentication API key

## Response

A successful retry returns a `BatchCallResponse` object containing:

- Batch identification and metadata
- Call statistics (dispatched, scheduled, finished)
- Current status and retry count
- Telephony configuration settings
- Associated agent information

## Status Codes

- **200**: Operation completed successfully
- **422**: Validation error in request parameters

## Available SDKs

Code examples are provided for:
- TypeScript/JavaScript
- Python
- Go
- Ruby
- Java
- PHP
- C#
- Swift

Each SDK example demonstrates calling the retry function with the batch_id parameter, with implementation details varying by language and SDK approach.
