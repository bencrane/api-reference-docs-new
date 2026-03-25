# Evals Quickstart - Complete Documentation

## Overview

This guide helps you set up automated testing for AI assistants and squads in just minutes. You'll create mock conversations, define expected behaviors, and validate agents work correctly before production.

## What are Evals?

Evals is Vapi's AI agent testing framework for systematically testing assistants and squads using mock conversations with automated validation. You can:

1. Create mock conversations with user messages and expected responses
2. Validate behavior using exact match, regex patterns, or AI-powered judging
3. Test tool calls and verify function calls with specific arguments
4. Run automated tests and receive detailed pass/fail results
5. Debug failures by reviewing full conversation transcripts

## When Evals are Useful

- Pre-deployment testing for new assistant configurations
- Regression testing when prompt or tool changes occur
- Conversation flow validation for multi-turn interactions
- Tool calling verification with correct arguments
- Squad handoff testing for smooth transitions
- CI/CD integration for automated quality gates

## Prerequisites

You need:
- A Vapi account (sign up at dashboard.vapi.ai)
- An API key from the API Keys section in sidebar
- An existing assistant or squad to test

## Step 1: Create Your First Evaluation

### Via Dashboard

1. Log in to dashboard.vapi.ai
2. Click Evals in the left sidebar (under Observability)
3. Click Create Evaluation
4. Enter name: "Greeting Test"
5. Add description: "Verify assistant greets users appropriately"
6. Add a user message: "Hello"
7. Add an assistant message with Exact Match evaluation
8. Set expected content: "Hello! How can I help you today?"
9. Save the evaluation

### Via cURL

```bash
curl -X POST "https://api.vapi.ai/eval" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Greeting Test",
    "description": "Verify assistant greets users appropriately",
    "type": "chat.mockConversation",
    "messages": [
      {
        "role": "user",
        "content": "Hello"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "exact",
          "content": "Hello! How can I help you today?"
        }
      }
    ]
  }'
```

## Step 2: Run Your Evaluation

### Via Dashboard

1. Navigate to Evals in the sidebar
2. Click on "Greeting Test"
3. In the Run Test section, select Assistant or Squad
4. Choose your target from the dropdown
5. Click Run Evaluation
6. View results with pass/fail indicators and full transcripts

### Via cURL

Create an eval run:

```bash
curl -X POST "https://api.vapi.ai/eval/run" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "evalId": "550e8400-e29b-41d4-a716-446655440000",
    "target": {
      "type": "assistant",
      "assistantId": "your-assistant-id"
    }
  }'
```

Check results:

```bash
curl -X GET "https://api.vapi.ai/eval/run/eval-run-123" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

## Step 3: Understand Test Results

### Successful Evaluation

```json
{
  "status": "ended",
  "endedReason": "mockConversation.done",
  "results": [
    {
      "status": "pass",
      "messages": [
        {
          "role": "user",
          "content": "Hello"
        },
        {
          "role": "assistant",
          "content": "Hello! How can I help you today?",
          "judge": {
            "status": "pass"
          }
        }
      ]
    }
  ]
}
```

Pass indicators:
- `status` is "ended"
- `endedReason` is "mockConversation.done"
- `results[0].status` is "pass"
- All `judge.status` values are "pass"

### Failed Evaluation

```json
{
  "status": "ended",
  "endedReason": "mockConversation.done",
  "results": [
    {
      "status": "fail",
      "messages": [
        {
          "role": "user",
          "content": "Hello"
        },
        {
          "role": "assistant",
          "content": "Hi there! What can I do for you?",
          "judge": {
            "status": "fail",
            "failureReason": "Expected exact match: 'Hello! How can I help you today?' but got: 'Hi there! What can I do for you?'"
          }
        }
      ]
    }
  ]
}
```

## Step 4: Test Tool/Function Calls

### Basic Tool Call Validation

Test appointment booking with exact argument matching:

```bash
curl -X POST "https://api.vapi.ai/eval" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Appointment Booking Test",
    "type": "chat.mockConversation",
    "messages": [
      {
        "role": "user",
        "content": "Book me an appointment for next Monday at 2pm"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "exact",
          "toolCalls": [{
            "name": "bookAppointment",
            "arguments": {
              "date": "2025-01-20",
              "time": "14:00"
            }
          }]
        }
      },
      {
        "role": "tool",
        "content": "{\"status\": \"success\", \"confirmationId\": \"APT-12345\"}"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "regex",
          "content": ".*confirmed.*APT-12345.*"
        }
      }
    ]
  }'
```

### Tool Call Validation Modes

**Exact match - Full validation:**

Validates both function name AND all argument values exactly.

**Partial match - Name only:**

Validates only that the function was called (arguments can vary).

**Multiple tool calls:**

Validates multiple function calls in sequence.

## Step 5: Use Regex for Flexible Validation

### Common Regex Patterns

**Greeting variations:**

```json
{
  "judgePlan": {
    "type": "regex",
    "content": "^(Hello|Hi|Hey),? (I can|I'll|let me) help.*"
  }
}
```

**Responses with variables:**

```json
{
  "judgePlan": {
    "type": "regex",
    "content": ".*appointment.*confirmed.*[A-Z]{3}-[0-9]{5}.*"
  }
}
```

**Date patterns:**

```json
{
  "judgePlan": {
    "type": "regex",
    "content": ".*scheduled for (Monday|Tuesday|Wednesday|Thursday|Friday).*"
  }
}
```

**Case-insensitive matching:**

```json
{
  "judgePlan": {
    "type": "regex",
    "content": "(?i)booking confirmed"
  }
}
```

### Regex Tips

- Use `.*` to match any characters
- Use `(option1|option2)` for alternatives
- Use `\d` for digits, `\s` for whitespace
- Use `.*?` for non-greedy matching
- Test patterns with sample responses first

## Step 6: Use AI Judge for Semantic Validation

### AI Judge Structure

```json
{
  "role": "assistant",
  "judgePlan": {
    "type": "ai",
    "model": {
      "provider": "openai",
      "model": "gpt-4o",
      "messages": [
        {
          "role": "system",
          "content": "Your evaluation prompt here"
        }
      ]
    }
  }
}
```

### Writing Effective Judge Prompts

Template structure:

```
You are an LLM-Judge. Evaluate ONLY the last assistant message in the mock
conversation: {{messages[-1]}}.

Include the full conversation history for context: {{messages}}

Decision rule:
- PASS if ALL "pass criteria" are satisfied AND NONE of "fail criteria" triggered
- Otherwise FAIL.

Pass criteria:
- [Specific requirement 1]
- [Specific requirement 2]

Fail criteria (any one triggers FAIL):
- [Specific failure condition 1]
- [Specific failure condition 2]

Output format: respond with exactly one word: pass or fail
- No explanations
- No punctuation
- No additional text
```

Template variables:
- `{{messages}}` - The entire conversation history
- `{{messages[-1]}}` - The last assistant message only

### Supported AI Judge Providers

- **OpenAI:** gpt-4o, gpt-4-turbo, gpt-3.5-turbo (general-purpose evaluation)
- **Anthropic:** claude-3-5-sonnet-20241022, claude-3-opus-20240229 (nuanced evaluation)
- **Google:** gemini-1.5-pro, gemini-1.5-flash (multilingual content)
- **Groq:** llama-3.1-70b-versatile, mixtral-8x7b-32768 (fast evaluation)

### AI Judge Best Practices

- Be specific with pass/fail criteria (avoid ambiguous requirements)
- Use "ALL pass criteria must be met" logic
- Use "ANY fail criteria triggers fail" logic
- Include conversation context with `{{messages}}` syntax
- Request exact "pass" or "fail" output (no explanations)
- Test criteria with known good/bad responses before production
- Use consistent evaluation standards across similar tests

## Step 7: Control Flow with Continue Plan

### Exit on Failure

Stop the test immediately if a critical check fails:

```json
{
  "role": "assistant",
  "judgePlan": {
    "type": "exact",
    "content": "I can help you with that."
  },
  "continuePlan": {
    "exitOnFailureEnabled": true
  }
}
```

Use case: Skip expensive subsequent tests when initial validation fails.

### Override Responses on Failure

Provide fallback responses to continue testing even when validation fails:

```json
{
  "role": "assistant",
  "judgePlan": {
    "type": "exact",
    "content": "I've processed your request."
  },
  "continuePlan": {
    "exitOnFailureEnabled": false,
    "contentOverride": "Let me rephrase that...",
    "toolCallsOverride": [
      {
        "name": "retryProcessing",
        "arguments": { "retry": "true" }
      }
    ]
  }
}
```

Use case: Test error recovery paths or force specific tool calls for subsequent validation.

## Step 8: Test Complete Conversation Flows

### Complete Booking Flow Example

Multi-turn conversation structure:

1. **Turn 1 - Initial request:** User asks for appointment, assistant acknowledges
2. **Turn 2 - Provide details:** User gives time/date, assistant calls booking tool
3. **Turn 3 - Tool response:** Tool returns confirmation ID
4. **Turn 4 - Confirmation:** Assistant confirms with ID reference
5. **Turn 5 - Follow-up:** User asks for email, assistant sends confirmation

```bash
curl -X POST "https://api.vapi.ai/eval" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Complete Booking Flow",
    "description": "Test full appointment booking conversation",
    "type": "chat.mockConversation",
    "messages": [
      {
        "role": "user",
        "content": "I need to schedule an appointment"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "ai",
          "model": {
            "provider": "openai",
            "model": "gpt-4o",
            "messages": [{
              "role": "system",
              "content": "Evaluate: {{messages[-1]}}\n\nPASS if:\n- Response acknowledges appointment request\n- Response asks for details or preferences\n\nFAIL if:\n- Response is dismissive\n- Response ignores request\n\nOutput: pass or fail"
            }]
          }
        }
      },
      {
        "role": "user",
        "content": "Next Monday at 2pm"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "exact",
          "toolCalls": [{
            "name": "bookAppointment",
            "arguments": {
              "date": "2025-01-20",
              "time": "14:00"
            }
          }]
        }
      },
      {
        "role": "tool",
        "content": "{\"status\": \"success\", \"confirmationId\": \"APT-12345\"}"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "regex",
          "content": ".*confirmed.*APT-12345.*"
        }
      },
      {
        "role": "user",
        "content": "Can I get that via email?"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "exact",
          "toolCalls": [{
            "name": "sendEmail"
          }]
        }
      }
    ]
  }'
```

### System Message Injection

Inject system prompts mid-conversation to test dynamic behavior changes:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "regex",
        "content": ".*help.*"
      }
    },
    {
      "role": "system",
      "content": "You are now in urgent mode. Prioritize speed."
    },
    {
      "role": "user",
      "content": "I need immediate help"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "ai",
        "model": {
          "provider": "openai",
          "model": "gpt-4o",
          "messages": [
            {
              "role": "system",
              "content": "PASS if response shows urgency. FAIL if response is casual. Output: pass or fail"
            }
          ]
        }
      }
    }
  ]
}
```

### Multi-Turn Testing Tips

- Keep conversations focused (5-10 turns for most tests)
- Use exit-on-failure for early turns to save time
- Test one primary flow per evaluation
- Mix judge types (exact, regex, AI) for comprehensive validation
- Include tool responses to simulate real interactions

## Step 9: Manage Evaluations

### List All Evaluations

Via Dashboard:
1. Navigate to Evals in the sidebar
2. View all evaluations in a table with name, description, created date, last run status, and actions
3. Use search to filter by name
4. Sort by date or status

Via cURL:

```bash
curl -X GET "https://api.vapi.ai/eval" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Response includes results array with evaluation objects and pagination details.

### Update an Evaluation

Via Dashboard:
1. Navigate to Evals and click on an evaluation
2. Click Edit button
3. Modify conversation turns, judge plans, or settings
4. Click Save Changes
5. Previous test runs remain unchanged

Via cURL:

```bash
curl -X PATCH "https://api.vapi.ai/eval/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Greeting Test",
    "description": "Enhanced greeting validation",
    "messages": [
      {
        "role": "user",
        "content": "Hi there"
      },
      {
        "role": "assistant",
        "judgePlan": {
          "type": "regex",
          "content": "^(Hello|Hi|Hey).*"
        }
      }
    ]
  }'
```

### Delete an Evaluation

Via Dashboard:
1. Navigate to Evals
2. Click on an evaluation
3. Click Delete button
4. Confirm deletion

Note: Deleting an evaluation does NOT delete its run history. Past run results remain accessible.

Via cURL:

```bash
curl -X DELETE "https://api.vapi.ai/eval/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

### View Run History

Via Dashboard:
1. Navigate to Evals
2. Click on an evaluation
3. View Runs tab showing timestamp, target, status, and duration
4. Click any run to view detailed results

Via cURL:

List all runs:

```bash
curl -X GET "https://api.vapi.ai/eval/run" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

Filter by eval ID:

```bash
curl -X GET "https://api.vapi.ai/eval/run?evalId=550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Eval always fails | Verify exact match strings character-by-character. Consider using regex for flexibility |
| AI judge inconsistent | Make pass/fail criteria more specific and binary. Test with known examples |
| Tool calls not matching | Check argument types (string vs number). Ensure exact spelling of function names |
| Run stuck in "running" | Verify assistant configuration. Check for errors in assistant's tools or prompts |
| Timeout errors | Reduce conversation length or simplify evaluations. Check assistant response times |
| Regex not matching | Test regex patterns separately. Remember to escape special characters like `.` or `?` |
| Empty results array | Check `endedReason` field. Assistant may have encountered an error before completion |
| Missing judge results | Verify `judgePlan` is properly configured in assistant messages |

### Common Errors

**"mockConversation.done" not reached:**

- Check `endedReason` for actual error (e.g., "assistant-error", "pipeline-error-openai-llm-failed")
- Verify assistant configuration (model, voice, tools)
- Check API key validity and rate limits

**Judge validation fails unexpectedly:**

- Review actual vs expected output in `failureReason`
- For exact match: Check for extra spaces, punctuation, or case differences
- For regex: Test pattern with online regex validators
- For AI judge: Verify prompt clarity and binary pass/fail logic

**Tool calls not validated:**

- Ensure tool is properly configured in assistant
- Check argument types match exactly (string "14:00" vs number 14)
- Verify tool function names are spelled correctly

## Common Patterns

### Multiple Validation Types in One Eval

Combine exact, regex, and AI judges for comprehensive testing:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hello"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "exact",
        "content": "Hello! How can I help you?"
      }
    },
    {
      "role": "user",
      "content": "Book appointment for Monday"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "regex",
        "content": ".*(Monday|next week).*"
      }
    },
    {
      "role": "user",
      "content": "Thanks for your help"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "ai",
        "model": {
          "provider": "openai",
          "model": "gpt-4o",
          "messages": [
            {
              "role": "system",
              "content": "PASS if response is polite and acknowledges thanks. Output: pass or fail"
            }
          ]
        }
      }
    }
  ]
}
```

### Test Squad Handoffs

Validate smooth transitions between squad members:

```json
{
  "name": "Squad Handoff Test",
  "messages": [
    {
      "role": "user",
      "content": "I need technical support"
    },
    {
      "role": "assistant",
      "judgePlan": {
        "type": "exact",
        "toolCalls": [
          {
            "name": "transferToSquadMember",
            "arguments": {
              "destination": "technical-support-agent"
            }
          }
        ]
      }
    }
  ],
  "target": {
    "type": "squad",
    "squadId": "your-squad-id"
  }
}
```

## Success Tips

Best practices for reliable testing:

- Start simple with exact matches, then add complexity
- One behavior per evaluation turn keeps tests focused
- Use descriptive names that explain what's being tested
- Test both happy paths and edge cases
- Version control your evals alongside assistant configs
- Run critical tests first to fail fast
- Review failure reasons promptly and iterate
- Document why each test exists (use descriptions)

## Next Steps

- [Advanced testing strategies](/observability/evals-advanced) - Learn testing patterns, best practices, and CI/CD integration
- [Assistants guide](/assistants/quickstart) - Create and configure assistants to test
- [Tools documentation](/tools/custom-tools) - Build custom tools and validate their behavior
- [Eval API reference](/api-reference/eval/create) - Complete API documentation for evals

## Get Help

- [Eval API Reference](/api-reference/eval/eval-controller-create)
- [Discord Community](https://discord.gg/pUFNcf2WmH)
- [Support](mailto:support@vapi.ai)
