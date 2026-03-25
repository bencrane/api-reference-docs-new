# Render Project API Endpoint

## Overview

The Render Project endpoint allows you to regenerate output media for a specific language in a dubbing project using the latest Studio state.

## Endpoint Details

**Method:** POST
**URL:** `https://api.elevenlabs.io/v1/dubbing/resource/{dubbing_id}/render/{language}`
**Content-Type:** application/json

## Key Information

The endpoint description states: "Regenerate the output media for a language using the latest Studio state. Please ensure all segments have been dubbed before rendering, otherwise they will be omitted. Renders are generated asynchronously."

To check rendering status, use the 'Get Dubbing Resource' endpoint.

## Required Parameters

- **dubbing_id** (path): ID of the dubbing project
- **language** (path): Target language code (e.g., 'es') or 'original' for source track
- **render_type** (body): Type of render - mp4, aac, mp3, wav, aaf, tracks_zip, or clips_zip

## Optional Parameters

- **normalize_volume** (body): Boolean flag to normalize rendered audio volume
- **xi-api-key** (header): API authentication key

## Response

Success returns a 200 status with:
- **version**: Integer version number
- **render_id**: String identifier for the render

## Available Servers

- https://api.elevenlabs.io
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
