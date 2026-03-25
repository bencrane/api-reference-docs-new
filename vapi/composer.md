# Composer Documentation

## Overview
Composer is Vapi's AI assistant enabling users to construct and configure voice agents through conversational interaction rather than manual technical setup. The tool comprehends voice agent architecture and Vapi's capabilities, supporting agent creation, phone number configuration, integration setup, troubleshooting, and feature inquiries.

**Key Benefits:**
- Accelerated development timelines
- Integrated best practices
- Lower technical entry requirements
- Built-in diagnostic support

## Getting Started

The four-step implementation process involves:

1. **Access** — Navigate to the Vapi dashboard and select Composer
2. **Description** — Communicate your requirements in natural language
3. **Clarification** — Address follow-up questions from the assistant
4. **Testing** — Validate and refine the created agent iteratively

## Capabilities and Constraints

**Supported Functions:**
- Assistant creation and customization
- Phone number provisioning
- Webhook and integration configuration
- Prompt modification
- Technical issue diagnosis
- Feature guidance

**Intentional Limitations:**
- Resource deletion is manually managed through the dashboard interface
- External system access remains unavailable
- Business logic determination remains user-controlled
- Agent testing requires manual validation
- Production deployment remains user-directed

## Safety Mechanisms

The platform incorporates protective features preventing unintended modifications. Specifically, "Composer cannot delete any resources" to protect against permanent data loss. Resource updates require explicit user approval through interface buttons, with approval tokens expiring after ten minutes and remaining specific to individual modifications.

## Optimization Strategies

Effective usage involves providing industry-specific context, implementing features progressively, maintaining single-task focus per conversation, and directly requesting technical explanations when needed.
