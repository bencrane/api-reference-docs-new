# Migrate Segments API Documentation

## Endpoint Overview

The Migrate Segments endpoint allows you to reassign audio segments to different speakers within a dubbing project.

**Endpoint:** `POST https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/migrate-segments`

## Purpose

This API operation enables you to "Change the attribution of one or more segments to a different speaker" within an existing dubbing project.

## Request Parameters

**Path Parameter:**
- `dubbing_id` (string, required): The identifier for the dubbing project

**Header:**
- `xi-api-key` (string, optional): Authentication key

**Request Body:**
- `segment_ids` (array of strings, required): List of segment identifiers to reassign
- `speaker_id` (string, required): The target speaker to assign these segments to

## Response

**Success (200):** Returns a `SegmentMigrationResponse` object containing:
- `version` (integer): The updated version number

**Validation Error (422):** Returns detailed validation error information including location, message, and error type.

## Implementation Examples

Code examples are provided in TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the same operation with language-specific syntax.
