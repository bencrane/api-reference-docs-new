# Create Chapter

## API Endpoint

**POST** `https://api.elevenlabs.io/v1/studio/projects/{project_id}/chapters`

This endpoint allows you to create a new chapter within a Studio project, either as a blank chapter or initialized from a URL source.

## Request Parameters

**Path Parameter:**
- `project_id` (string, required): The identifier for the Studio project

**Header:**
- `xi-api-key` (string, optional): Authentication key

**Request Body (JSON):**
- `name` (string, required): Chapter identification label
- `from_url` (string, optional): "An optional URL from which we will extract content to initialize the Studio project."

## Response

**Success (200):** Returns an `AddChapterResponseModel` containing:
- `chapter_id`: Unique chapter identifier
- `name`: Chapter name provided
- `state`: Current chapter state (default or converting)
- `content`: Chapter content blocks with nodes
- `statistics`: Character and paragraph conversion metrics
- `can_be_downloaded`: Boolean indicating download availability
- `voice_ids`: Array of voices used in chapter
- `conversion_progress`: Percentage completion

**Error (422):** Validation error response with detailed error information

## SDK Examples

The documentation provides implementation examples in:
- TypeScript/JavaScript
- Python
- Go
- Ruby
- Java
- PHP
- C#
- Swift

Each example demonstrates creating a chapter named "Chapter 1" in project `21m00Tcm4TlvDq8ikWAM`.
