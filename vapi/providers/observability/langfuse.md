# Langfuse Integration with Vapi

## Overview

Vapi offers native integration with Langfuse, an open-source LLM engineering platform. This connection allows developers to transmit traces directly to Langfuse for comprehensive telemetry analysis of voice AI applications.

## About Langfuse

Langfuse specializes in providing "observability and evaluations into AI applications," helping teams monitor, analyze, and visualize AI interaction traces for improved performance optimization and debugging.

## Setup Process

**Step 1: Obtain Credentials**
Users need to gather three items from Langfuse:
- Secret Key
- Public Key
- Host URL

These are available through Langfuse Cloud or self-hosted deployments.

**Step 2: Configure in Vapi**
Navigate to Vapi's dashboard Integrations section and locate the Observability Providers area. Input your Langfuse credentials with the appropriate Host URL based on your data region (US or EU).

**Step 3: Monitor Traces**
After saving credentials, conversation traces automatically appear in the Langfuse dashboard.

**Step 4: Leverage Tools**
Utilize Langfuse's evaluation and debugging capabilities to enhance voice AI agent performance.

## Enriching Traces

Vapi supports customization through metadata and tags:

- **Metadata**: Attach custom key-value pairs using the `observabilityPlan.metadata` field
- **Tags**: Add searchable labels via the `observabilityPlan.tags` field

Default metadata includes call details, assistant configuration, and variable values automatically.
