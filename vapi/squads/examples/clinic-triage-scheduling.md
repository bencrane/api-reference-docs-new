# Clinic Triage and Scheduling Squad

## Overview

This documentation describes building a multi-assistant clinic experience using Squads. The system orchestrates three specialized assistants: one for initial patient assessment, another for urgent situations, and a third for booking appointments.

The core capabilities include "Structured triage evaluation and safety gates," "Emergency detection → immediate handoff," and the ability to match providers with scheduling tools while maintaining conversation history during transfers.

## Squad Architecture

The example defines three members:

1. **Triage Assistant** - Uses GPT-4o to identify concerning symptoms and routes patients appropriately
2. **Emergency Assistant** - Handles urgent cases with brief interactions and immediate connection protocols
3. **Scheduler Assistant** - Books appointments with tool access for availability and provider lookup

## Implementation Approaches

The documentation provides code examples for:

- **TypeScript**: Using the Vapi Server SDK to create transient squads for web or phone calls, with an option to create and reuse persistent squads
- **Python**: Similar patterns using the Vapi Python client library
- **cURL**: Direct HTTP requests to the Vapi API endpoints

Each approach supports embedding squad configuration directly in call creation or referencing a pre-created squad by ID.

## Transfer Logic

The system routes patients from Triage to either Emergency (when red flags appear) or Scheduler (for routine needs), with context preserved throughout transfers.

## Getting Started

Implementation requires configuring assistant system prompts, enabling transfer rules, and testing both urgent and routine patient flows with an attached phone number.
