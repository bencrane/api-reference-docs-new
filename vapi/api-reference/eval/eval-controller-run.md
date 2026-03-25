# Create Eval Run API Reference

## Endpoint

**POST** `https://api.vapi.ai/eval/run`

## Description

Creates an evaluation run to test assistant responses against predefined criteria using mock conversations.

## Authentication

**Required Header:**
- `Authorization: [API Key]` - Retrieve from [Dashboard](dashboard.vapi.ai)

## Request Body

### Schema: CreateEvalDTO

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `messages` | Array | Yes | Mock conversation flow with evaluation checkpoints. Includes user messages, assistant responses, and system prompts. |
| `type` | String | Yes | Fixed value: `chat.mockConversation` |
| `name` | String | No | Identifier describing what the eval validates |
| `description` | String | No | Detailed explanation of eval purpose |

### Message Types

Messages array supports six types:

1. **ChatEvalUserMessageMock** - "This is the message that the user would have sent"
   - `role`: "user" (required)
   - `content`: string (required)

2. **ChatEvalSystemMessageMock** - System context added mid-conversation
   - `role`: "system" (required)
   - `content`: string (required)

3. **ChatEvalAssistantMessageMock** - Expected assistant output
   - `role`: "assistant"
   - `content`: string
   - `toolCalls`: array of tool invocations

4. **ChatEvalAssistantMessageEvaluation** - Checkpoint validating responses
   - `role`: "assistant"
   - `judgePlan`: evaluation strategy (exact/regex/AI)

5. **ChatEvalToolResponseMessageMock** - Tool result in conversation
   - `role`: "tool"
   - `content`: string (stringified JSON)

6. **ChatEvalToolResponseMessageEvaluation** - Validate tool responses
   - `role`: "tool"
   - `judgePlan`: evaluation criteria

### Judge Plan Options

**Exact Match:**
```yaml
type: "exact"
content: "Expected text"
toolCalls: [array of expected tool calls]
```

**Regex Pattern:**
```yaml
type: "regex"
content: "pattern.*match"
toolCalls: [array with regex arguments]
```

**LLM-as-Judge:**
```yaml
type: "ai"
model: [OpenAI/Anthropic/Google/Custom]
autoIncludeMessageHistory: true
```

### LLM Judge Model Configuration

Supports OpenAI, Anthropic, Google, or custom models:

**EvalOpenAIModel:**
- `provider`: "openai"
- `model`: gpt-4o, gpt-4-turbo, gpt-3.5-turbo, etc.
- `temperature`: 0-0.3 recommended for judging
- `maxTokens`: low values for binary pass/fail
- `messages`: judging instructions

**EvalAnthropicModel:**
- `provider`: "anthropic"
- `model`: claude-3.5-sonnet, claude-3-opus, etc.
- `thinking`: optional extended thinking config
- `temperature`: 0-0.3 recommended
- `maxTokens`: appropriate for response length
- `messages`: evaluation prompts

**EvalGoogleModel:**
- `provider`: "google"
- `model`: gemini-2.5-pro, gemini-2.0-flash, etc.
- `temperature`: recommended 0-0.3
- `maxTokens`: sizing for output
- `messages`: judgment instructions

**EvalCustomModel:**
- `provider`: "custom-llm"
- `url`: base URL for custom provider
- `headers`: authentication headers
- `model`: model identifier
- `messages`: eval instructions

## Liquid Template Variables

Within judge messages, reference conversation context:
- `{{messages}}` - entire mock conversation
- `{{messages[-1]}}` - last message (assistant response being evaluated)

## Response

**Status 200 - Success**

Returns evaluation run object with results indicating pass/fail status and details.

## Example Request

```json
{
  "type": "chat.mockConversation",
  "name": "greeting_eval",
  "description": "Validates assistant greeting behavior",
  "messages": [
    {
      "role": "user",
      "content": "Hello, who are you?"
    },
    {
      "role": "assistant",
      "content": "Hi! I'm an AI assistant here to help.",
      "toolCalls": []
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "exact",
        "content": "Hi! I'm an AI assistant here to help."
      }
    }
  ]
}
```

## Example with AI Judge

```json
{
  "type": "chat.mockConversation",
  "name": "response_quality_eval",
  "messages": [
    {
      "role": "user",
      "content": "What's the capital of France?"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "ai",
        "model": {
          "provider": "openai",
          "model": "gpt-4o",
          "temperature": 0.1,
          "maxTokens": 10,
          "messages": [
            {
              "role": "system",
              "content": "Evaluate if response correctly identifies Paris as French capital."
            },
            {
              "role": "user",
              "content": "Response: {{messages[-1].content}}"
            }
          ]
        }
      }
    }
  ]
}
```

## Notes

- Judge models must respond with "pass" or "fail" only
- Low temperature values (0-0.3) prevent hallucination in evaluations
- Transcriber fallback plans available for primary/secondary transcription services
- Tool calls validated by name and argument patterns
