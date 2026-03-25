# Structured Outputs Quickstart Documentation

## Overview
The documentation provides a comprehensive guide to implementing structured data extraction from phone calls using Vapi's structured outputs feature. As the guide explains, "Structured outputs are AI-powered analysis and extraction tools that intelligently process conversation data after calls end."

## Key Capabilities

The system enables several advanced functions beyond simple data extraction:
- Automatic customer information extraction (name, contact details, issues)
- Call outcome evaluation and success metrics
- Sentiment analysis and satisfaction scoring
- Intelligent conversation summarization
- CRM and database integration support

## Implementation Process

The quickstart outlines three primary steps:

**Step 1: Create Structured Output**
Users define extraction parameters using JSON Schema, specifying what information to capture. The documentation provides examples for a support ticket extraction including customer details, issue descriptions, and follow-up requirements.

**Step 2: Create and Test Calls**
After configuring the structured output and attaching it to an assistant, users conduct test calls to validate the extraction functionality.

**Step 3: Retrieve Extracted Data**
Once calls conclude, extracted information becomes available through the API or dashboard within seconds. The data appears in formatted JSON matching the defined schema.

## HIPAA Compliance Considerations

For healthcare applications, the guide emphasizes that "when HIPAA mode is enabled, Vapi does not store structured outputs by default." Storage can be enabled selectively for non-sensitive data like appointment bookings or satisfaction scores, but users must ensure no protected health information is included.

## Multiple Output Configuration

Assistants can attach multiple structured outputs simultaneously to extract different data categories, enabling comprehensive call analysis across customer details, appointment requests, and feedback metrics.
