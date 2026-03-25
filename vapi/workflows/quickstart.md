# Workflows Quickstart - Complete Documentation

## Overview
This guide teaches you to build a voice agent using Vapi's visual workflow builder that performs greeting, information collection, and demonstrates core concepts like variable extraction and conditional routing.

## Key Warning
**Workflows are no longer recommended for new builds.** The documentation states: "Use **Assistants** for most cases or **Squads** for multi-assistant setups." Existing workflow content remains available for reference purposes.

## Prerequisites
- Active Vapi account at dashboard.vapi.ai
- API key from Dashboard (for SDK usage)
- Optional: Vapi CLI for terminal-based workflow management

## Project Structure

The quickstart builds a workflow with these capabilities:

- User greeting and voice agent needs inquiry
- Extraction and storage of user information (name, city)
- Dynamic responses using variable templates
- Human escalation capability

## Implementation Steps

### 1. Workflow Creation
Choose your approach:
- **Dashboard**: Navigate to Workflows section, click Create Workflow, select blank template
- **SDKs/APIs**: Use TypeScript, Python, or cURL to programmatically create workflows with initial conversation nodes

### 2. Start Node Configuration
Configure initial greeting node with:
- First message: "Hey there!"
- System prompt requesting voice agent use case details
- Test via dashboard Call button

### 3. Information Collection
Add conversation node that:
- Acknowledges the user's use case
- Requests first name and city
- Extracts variables with specified types and descriptions
- Connects with conditional edge triggering on user description

### 4. Dynamic Response Node
Implement template-based responses using: "Thanks {{first_name}}, {{city}} is great!" followed by contextual remarks and follow-up assistance offers.

### 5. Global Escalation
Add escalation pathway featuring:
- Global conversation node detecting human transfer requests
- Transfer call node routing to specified destination
- Pre-transfer message summarizing conversation context

### 6. Call Termination
Implement end-call node with farewell message and condition-based triggering when user declines further assistance.

### 7. Testing
Verify complete workflow through dashboard testing interface, confirming all conversation flows, variable extraction accuracy, escalation triggers, and termination logic.

## Code Examples Available

Documentation provides complete implementation code in:
- TypeScript (Server SDK)
- Python (Server SDK)
- cURL commands

## Next Learning Resources

- Workflows overview documentation
- Pre-built workflow examples
- Custom Tools integration guide
- Dynamic Variables and personalization techniques
