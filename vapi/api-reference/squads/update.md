# Update Squad API Reference

## Endpoint

**PATCH** `https://api.vapi.ai/squad/{id}`

Updates an existing squad configuration with new parameters.

## Parameters

### Path Parameters
- **id** (string, required): The unique identifier of the squad to update

### Header Parameters
- **Authorization** (string, required): API key for authentication. "Retrieve your API Key from Dashboard"

### Request Body
The request body accepts an `UpdateSquadDTO` schema containing the squad configuration to be updated.

## Response

**Status: 200 OK**

Returns the updated Squad object with all current configuration details.

## Key Schema Components

The UpdateSquadDTO supports configuration for:

### Transfer Destinations
- **TransferDestinationAssistant**: Routes calls to other assistants with customizable transfer messages
- **TransferMode**: Options include `rolling-history`, `swap-system-message-in-history`, `delete-history`, and `swap-system-message-in-history-and-remove-transfer-tool-messages`

### Transcription Providers
Supported transcribers include:
- AssemblyAI
- Azure Speech
- Deepgram
- ElevenLabs
- Gladia
- Google
- Talkscriber
- Speechmatics
- OpenAI
- Cartesia
- Soniox
- Custom transcribers via webhook

Each supports language selection, confidence thresholds, and fallback plans.

### Context Engineering
Handoff configuration includes options for message context manipulation before transferring to destination assistants.

## Reference

Full documentation: https://docs.vapi.ai/api-reference/squads/update
