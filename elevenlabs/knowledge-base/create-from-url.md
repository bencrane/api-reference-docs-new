# Create Knowledge Base Document from URL

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/knowledge-base/url` that generates knowledge base documents by scraping webpage content.

## Request Parameters

The endpoint accepts the following JSON properties:

- **url** (required, string): The webpage URL to scrape for documentation
- **name** (optional, string): Custom human-readable identifier for the document
- **parent_folder_id** (optional, string): Folder location for the created document
- **enable_auto_sync** (optional, boolean): Activates automatic updates; defaults to false
- **auto_remove** (optional, boolean): Removes document if URL becomes unavailable when auto-sync is enabled; defaults to false

## Response Schema

A successful 200 response returns an object containing:

- **id** (string): Unique document identifier
- **name** (string): Document name
- **folder_path** (array): Hierarchical folder segments from root to parent

## Code Examples

### TypeScript
```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

async function main() {
    const client = new ElevenLabsClient();
    await client.conversationalAi.knowledgeBase.documents.createFromUrl({
        url: "url",
    });
}
main();
```

### Python
```python
from elevenlabs import ElevenLabs

client = ElevenLabs()
client.conversational_ai.knowledge_base.documents.create_from_url(url="url")
```

### cURL/Go/Ruby/Java/PHP/C#/Swift examples also provided in source documentation

## Error Handling

The endpoint returns a 422 status for validation errors, with details about the specific validation failures encountered.
