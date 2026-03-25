# Create Eval - API Reference

## Endpoint Details

**Method:** POST
**URL:** `https://api.vapi.ai/eval`
**Content-Type:** `application/json`

## Description

Creates a new evaluation for testing assistant responses through mock conversations. This endpoint allows you to define test scenarios with message exchanges and establish checkpoints where the assistant's output is evaluated against expected criteria.

## Authentication

**Header:** `Authorization`
**Type:** Bearer Token
**Description:** "Retrieve your API Key from Dashboard"
**Required:** Yes

## Request Body

### Schema: CreateEvalDTO

```yaml
Type: object
Required Fields:
  - messages (array)
  - type (string)

Optional Fields:
  - name (string)
  - description (string)
```

### Messages Array

The `messages` array can contain the following message types:

- **ChatEvalAssistantMessageMock** - Simulated assistant responses
- **ChatEvalUserMessageMock** - Simulated user inputs
- **ChatEvalSystemMessageMock** - System instructions mid-conversation
- **ChatEvalToolResponseMessageMock** - Tool execution responses
- **ChatEvalAssistantMessageEvaluation** - Checkpoints evaluating assistant output
- **ChatEvalToolResponseMessageEvaluation** - Checkpoints evaluating tool responses

### Type Field

```yaml
Enum Values:
  - chat.mockConversation
Description: "Currently fixed to chat.mockConversation"
```

## Response Schema

### Success Response (201 Created)

```yaml
Type: object
Properties:
  id: string
  orgId: string
  createdAt: string (date-time)
  updatedAt: string (date-time)
  name: string (optional)
  description: string (optional)
  type: string
  messages: array
```

## Message Type Specifications

### ChatEvalAssistantMessageMock

```yaml
Properties:
  role: "assistant" (default)
  content: string (optional)
  toolCalls: array (optional)
    - name: string (required)
    - arguments: object
```

### ChatEvalUserMessageMock

```yaml
Properties:
  role: "user" (default)
  content: string (required)
```

### ChatEvalSystemMessageMock

```yaml
Properties:
  role: "system" (default)
  content: string (required)
  Description: "System message injected mid-conversation"
```

### ChatEvalAssistantMessageEvaluation

```yaml
Properties:
  role: "assistant" (default)
  judgePlan: object (required)
    Type Options:
      - exact
      - regex
      - ai
  continuePlan: object (optional)
    - exitOnFailureEnabled: boolean
    - contentOverride: string
    - toolCallsOverride: array
```

### Judge Plan: Exact Match

```yaml
Type: AssistantMessageJudgePlanExact
Properties:
  type: "exact"
  content: string (required)
  toolCalls: array (optional)
Description: "Case-insensitive exact match evaluation"
```

### Judge Plan: Regex Match

```yaml
Type: AssistantMessageJudgePlanRegex
Properties:
  type: "regex"
  content: string (required)
  toolCalls: array (optional)
Description: "Pattern matching evaluation without LLM"
```

### Judge Plan: AI Evaluation

```yaml
Type: AssistantMessageJudgePlanAI
Properties:
  type: "ai"
  model: object (optional)
    Providers: openai | anthropic | google | custom-llm
  autoIncludeMessageHistory: boolean (default: true)
Description: "LLM-as-judge evaluation with custom criteria"
```

## AI Judge Model Configuration

### OpenAI Model

```yaml
Provider: openai
Available Models:
  - gpt-5.2
  - gpt-4o
  - gpt-4-turbo
  - gpt-3.5-turbo
  - Regional variants (Azure endpoints)
```

### Anthropic Model

```yaml
Provider: anthropic
Available Models:
  - claude-3-opus-20240229
  - claude-3-5-sonnet-20241022
  - claude-3-5-haiku-20241022
Optional Features:
  - thinking: budgetTokens (1024-100000)
```

### Google Model

```yaml
Provider: google
Available Models:
  - gemini-2.5-pro
  - gemini-2.5-flash
  - gemini-1.5-pro
```

### Custom LLM Provider

```yaml
Provider: custom-llm
Required:
  - url: string (baseURL)
  - model: string
Optional:
  - headers: object
  - timeoutSeconds: number (default: 20)
```

### Common Model Properties

```yaml
temperature: number (recommended 0-0.3 for judging)
maxTokens: number
messages: array (required)
  Description: "Instruction messages for evaluation criteria"
  Variables:
    - {{messages}} - full conversation
    - {{messages[-1]}} - last message only
```

## Example Request

```python
from vapi import Vapi, ChatEvalUserMessageMock, ChatEvalAssistantMessageEvaluation
from vapi.types import AssistantMessageJudgePlanExact

client = Vapi(token="YOUR_TOKEN_HERE")

response = client.eval.eval_controller_create(
    name="Greeting Test",
    description="Validates proper greeting responses",
    type="chat.mockConversation",
    messages=[
        ChatEvalUserMessageMock(
            role="user",
            content="Hello, how are you?"
        ),
        ChatEvalAssistantMessageEvaluation(
            role="assistant",
            judgePlan=AssistantMessageJudgePlanExact(
                type="exact",
                content="I'm doing well, thank you for asking!"
            )
        )
    ]
)
```

## Example Response

```json
{
  "id": "eval_abc123xyz",
  "orgId": "org_def456uvw",
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z",
  "name": "Greeting Test",
  "description": "Validates proper greeting responses",
  "type": "chat.mockConversation",
  "messages": [
    {
      "role": "user",
      "content": "Hello, how are you?"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "exact",
        "content": "I'm doing well, thank you for asking!"
      }
    }
  ]
}
```

## Notes

- The evaluation flow simulates a complete conversation with mock messages interspersed with evaluation checkpoints
- Tool calls must reference valid tools configured in the assistant
- For LLM-as-judge evaluations, responses must be "pass" or "fail"
- The `continuePlan` allows conditional flow based on evaluation results
- Content overrides enable testing alternate conversation branches
