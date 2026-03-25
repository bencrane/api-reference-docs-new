# E-commerce Order Management Squad

## Overview

This documentation describes a multi-assistant system using Squads that separates customer support responsibilities across specialized roles. The approach divides operations into three distinct assistants: one handling order inquiries, another managing returns, and a third providing premium customer service.

**Core Capabilities:**

The system supports order tracking functionality, return eligibility verification and label generation, customer tier-based routing, and smooth handoffs between assistants that preserve conversation context.

## 1. Member Definition

The squad configuration requires defining three assistants, each with specific system prompts and capabilities:

- **Orders Assistant**: "Orders specialist. Handle tracking and delivery questions."
- **Returns Assistant**: "Returns specialist. Check eligibility and generate labels."
- **VIP Assistant**: "VIP concierge. Prioritize premium customers and coordinate resolutions."

The Orders assistant includes an initial greeting and initiates conversations first.

## 2. Transfer Logic

The system implements directional routing:
- Orders assistant escalates to Returns when customers request refunds
- Any assistant can escalate to VIP for high-value accounts or negative sentiment
- Complex cases route to human representatives with conversation summaries

## 3. Implementation Examples

Three code examples demonstrate initialization across different platforms: TypeScript SDK, Python SDK, and direct HTTP requests. Each creates a call with the squad configuration specifying OpenAI's GPT-4o model for all assistants.

## 4. Testing Approach

Validation involves assigning a phone number to the squad and simulating various customer scenarios across all three support pathways.

## Resources

Additional documentation links to custom tool development for extending assistant functionality.
