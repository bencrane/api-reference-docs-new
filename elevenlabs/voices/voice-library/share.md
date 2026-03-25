# Add Shared Voice API Endpoint

## Overview

The ElevenLabs API provides an endpoint to add a shared voice to your collection. This POST request allows users to incorporate voices from the voice library into their personal voice collection.

## Endpoint Details

**URL:** `POST https://api.elevenlabs.io/v1/voices/add/{public_user_id}/{voice_id}`

**Content-Type:** `application/json`

## Parameters

The endpoint requires two path parameters:

- **public_user_id**: A string identifier used to publicly identify ElevenLabs users
- **voice_id**: The identifier of the voice to add, obtainable through the Get voices endpoint

An optional header parameter `xi-api-key` is available for authentication.

## Request Body

The request accepts a JSON object with these properties:

- **new_name** (required, string): The display name for this voice in the website dropdown
- **bookmarked** (optional, boolean): Defaults to true

## Response

A successful 200 response returns a JSON object containing:

- **voice_id** (string): The identifier of the added voice

Error responses (422) include validation error details with location, message, and error type information.

## Available Servers

The API is accessible through multiple regional endpoints including the main US server and EU/India residency options.
