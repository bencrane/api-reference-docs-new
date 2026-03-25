# Get Project Muted Tracks

GET https://api.elevenlabs.io/v1/studio/projects/{project_id}/muted-tracks

The endpoint "returns a list of chapter IDs that have muted tracks in a project."

## Request Parameters

- **project_id** (path, required): The Studio project identifier
- **xi-api-key** (header, optional): API authentication key

## Response

Success (200) returns a `ProjectMutedTracksResponseModel` containing:
- **chapter_ids**: Array of strings representing chapters with muted audio tracks

Error responses (422) include validation error details.

## SDK Examples

Multiple language implementations are provided:
- **TypeScript**: Uses `client.studio.projects.getMutedTracks(projectId)`
- **Python**: Calls `client.studio.projects.get_muted_tracks(project_id=...)`
- **Go, Ruby, Java, PHP, C#, Swift**: Direct HTTP GET requests to the endpoint

All examples use the sample project ID "21m00Tcm4TlvDq8ikWAM" for demonstration.

## API Servers

Four regional endpoints are available:
- https://api.elevenlabs.io (primary)
- https://api.us.elevenlabs.io
- https://api.eu.residency.elevenlabs.io
- https://api.in.residency.elevenlabs.io
