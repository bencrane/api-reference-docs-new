# Simulations Quickstart - Complete Documentation

## Overview

This guide helps you test AI assistants and squads using realistic, AI-powered callers. Vapi's Simulations framework enables systematic testing through defined scenarios and structured output evaluations.

### What are Simulations?

Simulations recreate real conversations to measure whether your assistant behaves correctly. The testing process involves:

1. Creating personalities (full assistant configurations for AI testers)
2. Defining scenarios (instructions and evaluations using structured outputs)
3. Creating simulations (pairing scenarios with personalities)
4. Running simulations (executing tests in voice or chat mode)
5. Reviewing results (analyzing pass/fail outcomes)

### When are Simulations Useful?

- Pre-deployment validation of new configurations
- Regression testing after prompt or tool changes
- Multi-turn conversation flow validation
- Personality-based testing for different caller types
- Squad handoff verification
- Success rate monitoring over time

### Voice vs Chat Mode

**Voice mode** provides full audio simulation with realistic end-to-end testing and produces call recordings. **Chat mode** offers text-based simulation that's faster and lower-cost, ideal for rapid iteration.

> Recommendation: "Use chat mode during development for quick iteration, then switch to voice mode for final validation before deployment."

## Prerequisites

- Vapi account at [dashboard.vapi.ai](https://dashboard.vapi.ai)
- API key from **API Keys** in sidebar
- Existing assistant or squad to test

## Step 1: Create a Personality

Personalities define the AI tester's behavior through full assistant configuration including voice, model, and system prompt.

### Dashboard Instructions

1. Navigate to **Simulations** > **Personalities** tab
2. Click **Create Personality**
3. Enter name: "Impatient Customer"
4. Configure assistant:
   - Model: Select preferred LLM (e.g., GPT-4o)
   - System Prompt: Define personality behavior
   - Voice: Select voice for tester (optional for chat)
5. Click **Save**

### cURL Example

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/personality" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Impatient Customer",
    "assistant": {
      "model": {
        "provider": "openai",
        "model": "gpt-4o",
        "messages": [
          {
            "role": "system",
            "content": "You are an impatient customer who wants quick answers. Speak directly and may interrupt if responses are too long. You expect immediate solutions to your problems."
          }
        ]
      },
      "voice": {
        "provider": "cartesia",
        "voiceId": "sonic-english"
      }
    }
  }'
```

Response includes personality `id` for later use in simulations.

> Tip: "Start with the built-in default personalities to get familiar with the system before creating custom ones."

### Personality Types to Consider

- Decisive buyers
- Confused users
- Detail-oriented customers
- Frustrated callers

## Step 2: Create a Scenario

Scenarios contain instructions for the tester and evaluations using structured outputs to validate outcomes.

### Dashboard Instructions

1. Navigate to **Simulations** > **Scenarios** tab
2. Click **Create Scenario**
3. Enter name: "Book Appointment"
4. Define instructions for what the tester should accomplish
5. Add evaluations:
   - Click **Add Evaluation**
   - Create structured output (e.g., "appointment_booked" as boolean)
   - Set comparator: `=`
   - Set expected value: `true`
   - Mark as required
6. Click **Save Scenario**

### cURL Example

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/scenario" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Book Appointment",
    "instructions": "You are calling to book an appointment for next Monday at 2pm. Confirm your identity when asked and provide any required information. End the call once you receive a confirmation number.",
    "evaluations": [
      {
        "structuredOutput": {
          "name": "appointment_booked",
          "schema": {
            "type": "boolean",
            "description": "Whether an appointment was successfully booked"
          }
        },
        "comparator": "=",
        "value": true,
        "required": true
      },
      {
        "structuredOutput": {
          "name": "confirmation_provided",
          "schema": {
            "type": "boolean",
            "description": "Whether a confirmation number was provided"
          }
        },
        "comparator": "=",
        "value": true,
        "required": true
      }
    ]
  }'
```

### Evaluation Structure

| Field | Description |
|-------|-------------|
| `structuredOutputId` | Reference to existing structured output |
| `structuredOutput` | Inline structured output definition |
| `comparator` | Comparison operator: `=`, `!=`, `>`, `<`, `>=`, `<=` |
| `value` | Expected value (string, number, or boolean) |
| `required` | Whether this evaluation must pass (default: true) |

### Comparator Options

| Comparator | Description | Supported Types |
|-----------|-------------|-----------------|
| `=` | Equals | string, number, integer, boolean |
| `!=` | Not equals | string, number, integer, boolean |
| `>` | Greater than | number, integer |
| `<` | Less than | number, integer |
| `>=` | Greater than or equal | number, integer |
| `<=` | Less than or equal | number, integer |

> Note: "Evaluations only support primitive schema types: string, number, integer, boolean. Objects and arrays are not supported."

> Tip: "Use boolean structured outputs for pass/fail checks like appointment_booked or issue_resolved. Use numeric outputs with comparators for metrics like satisfaction_score >= 4."

## Step 3: Create a Simulation

Simulations pair a scenario with a personality. The target assistant or squad is specified when running the simulation.

### Dashboard Instructions

1. Navigate to **Simulations** > **Simulations** tab
2. Click **Create Simulation**
3. Enter optional name: "Appointment Booking - Impatient Customer"
4. Select scenario: "Book Appointment"
5. Select personality: "Impatient Customer"
6. Click **Save Simulation**

### cURL Example

```bash
curl -X POST "https://api.vapi.ai/eval/simulation" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Appointment Booking - Impatient Customer",
    "scenarioId": "550e8400-e29b-41d4-a716-446655440002",
    "personalityId": "550e8400-e29b-41d4-a716-446655440001"
  }'
```

Response includes simulation `id` for use in running tests.

> Note: "Create several simulations with different personality and scenario combinations to thoroughly test your assistant across various conditions."

## Step 4: Create a Simulation Suite (Optional)

Simulation suites group multiple simulations into a single batch that runs together.

### Dashboard Instructions

1. Navigate to **Simulations** > **Suites** tab
2. Click **Create Suite**
3. Enter name: "Appointment Booking Regression Suite"
4. Click **Add Simulations**
5. Select simulations to include
6. Click **Save Suite**

### cURL Example

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/suite" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Appointment Booking Regression Suite",
    "simulationIds": [
      "550e8400-e29b-41d4-a716-446655440003",
      "550e8400-e29b-41d4-a716-446655440004",
      "550e8400-e29b-41d4-a716-446655440005"
    ]
  }'
```

> Tip: "Group related simulations together. For example, create separate suites for Booking Tests, Cancellation Tests, and Rescheduling Tests."

## Step 5: Run a Simulation

Execute simulations against your assistant or squad. You can run individual simulations or entire suites.

### Dashboard Instructions

1. Navigate to your simulation or suite
2. Click **Run**
3. Select **Target** (Assistant or Squad)
4. Configure **Transport** (optional):
   - Voice: `vapi.websocket` (default)
   - Chat: `vapi.webchat` (faster, no audio)
5. Set **Iterations** (optional)
6. Click **Start Run**
7. Monitor progress in **Runs** tab
8. For voice mode, click **Listen** on running tests to hear calls live

### cURL Examples

**Run single simulation in voice mode:**

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/run" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "simulations": [
      {
        "type": "simulation",
        "simulationId": "550e8400-e29b-41d4-a716-446655440003"
      }
    ],
    "target": {
      "type": "assistant",
      "assistantId": "your-assistant-id"
    },
    "transport": {
      "provider": "vapi.websocket"
    }
  }'
```

**Run simulation in chat mode:**

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/run" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "simulations": [
      {
        "type": "simulation",
        "simulationId": "550e8400-e29b-41d4-a716-446655440003"
      }
    ],
    "target": {
      "type": "assistant",
      "assistantId": "your-assistant-id"
    },
    "transport": {
      "provider": "vapi.webchat"
    }
  }'
```

**Run suite with multiple iterations:**

```bash
curl -X POST "https://api.vapi.ai/eval/simulation/run" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "simulations": [
      {
        "type": "simulationSuite",
        "simulationSuiteId": "550e8400-e29b-41d4-a716-446655440006"
      }
    ],
    "target": {
      "type": "assistant",
      "assistantId": "your-assistant-id"
    },
    "iterations": 3
  }'
```

**Check run status:**

```bash
curl -X GET "https://api.vapi.ai/eval/simulation/run/550e8400-e29b-41d4-a716-446655440007" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

## Step 6: Review Results

Analyze simulation run results to understand assistant performance.

### Successful Run

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440007",
  "status": "ended",
  "itemCounts": {
    "total": 3,
    "passed": 3,
    "failed": 0,
    "running": 0,
    "queued": 0,
    "canceled": 0
  },
  "startedAt": "2024-01-15T09:50:05Z",
  "endedAt": "2024-01-15T09:52:30Z"
}
```

**Pass criteria:**
- Status is "ended"
- Passed count equals total count
- All required evaluations show pass

### Failed Run

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440008",
  "status": "ended",
  "itemCounts": {
    "total": 3,
    "passed": 2,
    "failed": 1,
    "running": 0,
    "queued": 0,
    "canceled": 0
  }
}
```

**Failure indicators:**
- Failed count greater than 0
- Run items show which evaluations failed and why

### Dashboard Review Steps

1. Navigate to **Runs** tab
2. Click on completed run for details
3. Click on failed simulation to investigate
4. Review full conversation transcript
5. Check actual vs expected evaluation values
6. For voice mode, click **Listen to Recording** for full call audio
7. View historical runs to monitor trends

### cURL Review Commands

**List all runs:**

```bash
curl -X GET "https://api.vapi.ai/eval/simulation/run" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

**Get detailed results:**

```bash
curl -X GET "https://api.vapi.ai/eval/simulation/run/550e8400-e29b-41d4-a716-446655440007" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

**Filter runs by status:**

```bash
curl -X GET "https://api.vapi.ai/eval/simulation/run?status=ended" \
  -H "Authorization: Bearer $VAPI_API_KEY"
```

> Note: "Full conversation transcripts are available for all simulation runs, making it easy to understand exactly what happened during each test."

## Next Steps

Explore these additional resources:

- **Advanced simulation testing** - Learn about tool mocks, hooks, and CI/CD integration at `/observability/simulations-advanced`
- **Assistants guide** - Create and configure assistants to test at `/assistants/quickstart`
- **Evals quickstart** - Learn about chat-based testing at `/observability/evals-quickstart`
- **Structured outputs** - Define outputs for evaluations at `/assistants/structured-outputs`

## Tips for Success

- Use chat mode first for rapid iteration before voice validation
- Model test callers after actual customer types
- Define specific, measurable structured outputs
- Organize suites by feature or user flow
- Track pass rates over time to catch regressions
- Run simulation suites after updating prompts or tools
- Listen to call recordings to reveal issues metrics miss
- Use failed tests to improve both assistant and test design

## Frequently Asked Questions

### How many concurrent simulations can I run?

Simulation concurrency follows your organization's call concurrency limits. Each voice simulation uses 2 concurrent call slots (one for AI tester, one for assistant). Chat mode simulations are more efficient since they don't require audio processing. Contact support for higher concurrency limits.

### What's the difference between Simulations and Evals?

Simulations use AI-powered testers that have actual conversations, producing real call recordings and transcripts. Evals use mock conversations with predefined messages. Use Simulations for realistic end-to-end testing; use Evals for faster, more controlled validation.

### Can I use my own structured outputs?

Yes! Define inline structured outputs in scenario evaluations, or reference existing outputs by ID using the `structuredOutputId` field.

### How do I test squad handoffs?

Create a simulation targeting a squad instead of an assistant. Use `target.type: "squad"` and `target.squadId` fields when creating a run.

## Get Help

- [Discord Community](https://discord.gg/pUFNcf2WmH)
- [Support](mailto:support@vapi.ai)
