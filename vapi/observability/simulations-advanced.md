# Simulations Advanced - Complete Documentation

## Overview

This guide explores sophisticated testing methodologies for AI voice agents, covering tool mocks, hooks, strategic testing patterns, CI/CD integration, and maintenance approaches.

## Advanced Scenario Configuration

### Tool Mocks

Mock tool responses at the scenario level to validate specific execution paths without invoking real APIs. This capability proves valuable for:

- Testing error handling mechanisms
- Simulating service unavailability scenarios
- Ensuring reproducible test outcomes
- Accelerating test execution by avoiding external API calls

**Dashboard Instructions:**
Navigate to Simulations → Scenarios, open your target scenario, scroll to Tool Mocks section, click Add Tool Mock, enter the exact function name (e.g., `bookAppointment`), provide JSON response data, toggle enabled status, and save.

**cURL Example:**
```bash
curl -X POST "https://api.vapi.ai/eval/simulation/scenario" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Book Appointment - API Error Path",
    "instructions": "Try to book an appointment and handle the error gracefully when the system is unavailable.",
    "toolMocks": [
      {
        "toolName": "bookAppointment",
        "result": "{\"error\": \"Service temporarily unavailable\", \"code\": \"503\"}",
        "enabled": true
      }
    ]
  }'
```

**Common Mock Patterns:**

- **Success:** Returns confirmation ID and datetime
- **Error:** Provides error message with available alternatives
- **Timeout:** Simulates request timeout scenarios
- **Partial Success:** Indicates mixed results with item-level details

**Best Practices:**
Tool names must match configuration exactly. Use realistic error responses reflecting actual API formats. Create separate scenarios for success and error paths. Disable mocks to test live APIs.

### Simulation Hooks

Trigger actions during simulation lifecycle events for:

- Notifying external systems about test execution
- Logging test data to custom systems
- Initiating follow-up automated workflows
- Collecting analytics and performance metrics

**Important Limitation:** "Hooks are only supported in voice mode" and require `vapi.websocket` transport, not `vapi.webchat`.

**Dashboard Steps:**
Access Simulations → Scenarios, open your scenario, navigate to Hooks section, click Add Hook, select event (`simulation.run.started` or `simulation.run.ended`), select webhook action type, enter server URL, and save.

**cURL Implementation:**
```bash
curl -X POST "https://api.vapi.ai/eval/simulation/scenario" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "hooks": [
      {
        "on": "simulation.run.started",
        "do": [
          {
            "type": "webhook",
            "server": {
              "url": "https://your-server.com/webhooks/simulation-started"
            }
          }
        ]
      }
    ]
  }'
```

**Webhook Payloads:**

Started event includes: event type, simulation ID, run ID, and timestamp.

Ended event includes: completion status, duration in seconds, transcript (if enabled), messages array (if enabled), and recording URL (if enabled).

### Existing Structured Outputs

Reference previously created structured outputs instead of defining inline evaluations to achieve:

- Evaluation criteria reusability across scenarios
- Centralized management of assessment standards
- Consistent data extraction methodology

**Dashboard Method:**
Access Structured Outputs sidebar, create or locate existing output, copy ID, select "Use Existing" in scenario evaluations, paste ID.

**cURL Approach:**
First create reusable structured output, receive ID in response, then reference that ID in scenario evaluations using `structuredOutputId` parameter.

**Usage Guidelines:**
Use existing outputs when identical evaluation criteria span multiple scenarios. Apply inline definitions for scenario-specific assessments.

## Testing Strategies

### Smoke Tests

Quick validation confirming core functionality operates before comprehensive testing.

**Characteristics:**
- Minimal evaluation criteria
- Fast execution with simple instructions
- Executed before detailed test suites
- Optimized for chat mode speed

**Appropriate Use Cases:**
- Pre-testing expensive voice suites
- Validating configuration changes
- Health checks during monitoring
- Development validation

**Example:**
```json
{
  "name": "Smoke Test - Basic Response",
  "instructions": "Say hello and ask if the assistant can hear you.",
  "evaluations": [
    {
      "structuredOutput": {
        "name": "assistant_responded",
        "schema": {
          "type": "boolean",
          "description": "Whether the assistant provided any response"
        }
      },
      "comparator": "=",
      "value": true
    }
  ]
}
```

### Regression Tests

Ensure prior fixes and updates maintain existing functionality. These validate that "known issues stay fixed and features keep working."

**Best Practices:**
- Name tests with "Regression:" prefix
- Include relevant ticket/issue numbers
- Document what was previously fixed
- Execute full regression suite before major releases

**cURL Example:**
```bash
curl -X POST "https://api.vapi.ai/eval/simulation/scenario" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Regression: Date Parsing Bug #1234",
    "instructions": "Request an appointment for 3/15. The assistant should correctly parse this as March 15th."
  }'
```

### Edge Case Testing

Test boundary conditions and unusual inputs encompassing:

- **Ambiguous requests:** Vague or underspecified instructions
- **Topic switches:** Rapid conversation direction changes
- **Interruptions:** Handling mid-sentence interruptions (voice mode)
- **Invalid data:** Non-conforming formats and impossible values
- **Input boundaries:** Empty fields, maximum lengths, special characters
- **Data format variations:** Malformed numbers, unusual names, alternative date formats
- **Conversation patterns:** Contradictions, topic pivots, interruptions
- **Emotional scenarios:** Frustrated, confused, or impatient callers

## Best Practices

### Evaluation Design Principles

**Single Responsibility:** Each evaluation tests one specific outcome. Good example: "Was the appointment booked?" Bad example: "Was the appointment booked, confirmed, and email sent?"

**Clear Naming:** Use descriptive titles explaining what's evaluated. Good: "Booking - Handles Unavailable Slot" vs. Bad: "Test 1"

**Realistic Personalities:** Model test personas after actual customer types including decisive, confused, impatient, detail-oriented, and non-native speakers.

**Measurable Criteria:** Employ boolean or numeric outputs producing clear pass/fail results, avoiding subjective assessments.

### Voice vs Chat Mode Selection

| Scenario | Recommended | Reason |
|----------|-------------|--------|
| Development iteration | Chat | Faster, cheaper |
| Speech recognition testing | Voice | Tests actual STT |
| Voice/TTS quality | Voice | Tests actual TTS |
| Interruption handling | Voice | Requires audio |
| CI/CD pipelines | Chat | Speed and cost |
| Pre-production validation | Voice | Full end-to-end |
| Hooks/webhooks | Voice | Requires voice mode |

## CI/CD Integration

Automate simulation execution within deployment pipelines.

**Basic Workflow:**
```yaml
name: Test Assistant Changes
on:
  pull_request:
    paths:
      - 'assistants/**'

jobs:
  run-simulations:
    runs-on: ubuntu-latest
    steps:
      - name: Run smoke tests
        run: |
          RUN_ID=$(curl -s -X POST "https://api.vapi.ai/eval/simulation/run" \
            -H "Authorization: Bearer ${{ secrets.VAPI_API_KEY }}" \
            -d '{"simulations": [...], "transport": {"provider": "vapi.webchat"}}' \
            | jq -r '.id')
```

**Advanced Patterns:**

- **Staging validation:** Run comprehensive tests against staging environments before production promotion
- **Scheduled regression:** Execute full regression suites nightly with failure notifications
- **Quality gates:** Block deployments when pass rates fall below thresholds (e.g., 95%)

## Maintenance Strategies

### Regular Review Cycle

**Weekly:** Investigate failed tests, updating requirements or fixing assistant behavior.

**Monthly:** Audit coverage completeness—verify critical flows are tested, new features have tests, deprecated features are removed.

**Quarterly:** Refactor duplicates, update outdated scenarios, optimize personalities for cost efficiency, document test rationale.

### Update Triggers

| Trigger | Action |
|---------|--------|
| Prompt changes | Review affected simulations |
| New feature | Create simulations for feature |
| Bug fixed | Add regression test |
| User feedback | Add edge case simulation |
| Business change | Update evaluation criteria |

## Troubleshooting

### Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Always fails | Overly strict criteria | Review schema and expected values |
| Stuck "running" | No response | Check configuration and credentials |
| Inconsistent results | Non-deterministic behavior | Increase iterations, refine instructions |
| No audio | Chat mode used | Switch to `vapi.websocket` |
| Hooks inactive | Chat mode | Hooks require voice transport |
| Mocks fail | Wrong name | Verify exact tool name match |

### Debugging Steps

1. Check run status via API
2. Review individual run item statuses
3. Examine full conversation transcripts in Dashboard
4. Manually test assistant in Dashboard

### Support Resources

Include these details when reporting issues:
- Simulation run ID
- Scenario and personality IDs
- Transport mode (voice/chat)
- Expected vs. actual behavior
- Assistant configuration

## Next Steps

Explore the Simulations Quickstart, Evals Quickstart, Structured Outputs guide, and Assistants guide for complementary information.

## Summary

Advanced simulation testing requires:

**Configuration:** Implement tool mocks for error paths, leverage hooks for notifications (voice mode), and reference existing structured outputs for consistency.

**Testing Strategy:** Progress from smoke tests through regression to edge cases. Use chat for speed, voice for final validation. Base personalities on real customer archetypes.

**CI/CD:** Automate smoke tests in PR pipelines, run comprehensive regression pre-deployment, establish quality gate thresholds.

**Maintenance:** Review failures weekly, audit coverage monthly, add regression tests when fixing issues.
