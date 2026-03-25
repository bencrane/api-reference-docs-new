# Custom Knowledge Base Documentation

## Overview

Custom Knowledge Bases enable developers to operate their own document retrieval infrastructure rather than depending on Vapi's prebuilt options. This approach grants complete autonomy over search mechanisms, vector databases, and retrieval methodologies.

**Key Capabilities:**
- Deploy proprietary vector databases or search systems
- Develop bespoke retrieval algorithms with custom scoring
- Connect to established document management platforms
- Enforce specialized business rules for document filtering
- Retain complete authority over data protection and confidentiality

## Operational Mechanism

The integration follows a webhook pattern: Vapi transmits search requests to your endpoint and anticipates structured replies containing pertinent documents.

**Three-step workflow:**
1. User poses inquiry to the assistant during conversation
2. Vapi forwards search request to your custom endpoint
3. Your server furnishes relevant documents or comprehensive response

## Configuration Process

### Creating the Knowledge Base

Submit an API request to establish your knowledge base setup:

**cURL Example:**
```bash
curl --location 'https://api.vapi.ai/knowledge-base' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_VAPI_API_KEY' \
--data '{
    "provider": "custom-knowledge-base",
    "server": {
        "url": "https://your-domain.com/kb/search",
        "secret": "your-webhook-secret"
    }
}'
```

SDKs are available for TypeScript and Python as well.

### Linking to Your Assistant

**Important limitation:** Custom knowledge bases attach exclusively through API calls, not the dashboard interface.

When updating the assistant's model, include the entire configuration object—the API doesn't accommodate partial modifications for nested structures.

## Endpoint Implementation

Your server must process POST requests and provide structured output.

### Incoming Request Format

```json
{
  "message": {
    "type": "knowledge-base-request",
    "messages": [
      {
        "role": "user",
        "content": "What is your return policy?"
      }
    ]
  }
}
```

### Response Approaches

**Option 1 - Document Return:** Provide documents for the AI to synthesize responses

```json
{
  "documents": [
    {
      "content": "Return items within 30 days for full refund...",
      "similarity": 0.92,
      "uuid": "doc-return-policy-1"
    }
  ]
}
```

**Option 2 - Direct Response:** Supply a complete answer the assistant articulates verbatim

## Production Considerations

### Performance Requirements

"Your endpoint should respond in **milliseconds** (ideally under ~50ms) for optimal user experience." The system permits 10-second timeouts, but sluggish responses compromise conversational quality.

### Optimization Tactics

Implement document caching, establish request timeouts, and leverage pre-computed embeddings. Consider vector database solutions like Pinecone or Weaviate for scalable implementations.

### Error Management

Return empty document arrays during failures rather than throwing errors, maintaining assistant functionality under adverse circumstances.

## Additional Resources

- Query Tool Configuration documentation
- Vector Database integration guides
- Assistant optimization materials

**Deployment note:** Your webhook endpoint requires public accessibility with concurrent request handling and comprehensive monitoring for production environments.
