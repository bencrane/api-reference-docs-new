# Multilingual Support Workflow Documentation

## Overview

This guide demonstrates building a structured multilingual customer support system using Vapi's workflow builder. The system enables customers to select their preferred language at call start, then routes them through dedicated conversation paths optimized for English, Spanish, and French support.

## Key Components

### Language Selection Node
The workflow begins with a multilingual greeting: "Hello! Hola! Bonjour! Welcome to GlobalTech International support." Customers can indicate their language preference by saying the language name or pressing number keys (1 for English, 2 for Spanish, 3 for French).

### Language-Specific Support Paths
Each language receives its own conversation node configured with:
- **Dedicated voice**: Azure's language-specific voice options
- **Cultural context**: Tone and formality adjusted per language
- **Native prompts**: System instructions written in the target language

### Implementation Steps

**1. Knowledge Base Setup**
Upload three CSV files containing customer data, product information, and support articles through the Files section.

**2. Workflow Configuration**
Create nodes for:
- Initial language selection with variable extraction
- English support path (voice: en-US-AriaNeural)
- Spanish support path (voice: es-ES-ElviraNeural)
- French support path (voice: fr-FR-DeniseNeural)

**3. Routing Logic**
Conditional edges direct customers to appropriate language paths based on their selection: "Customer selected English language support" as a routing condition.

**4. Phone Integration**
Configure an inbound phone number with workflow assignment, call recording, and maximum duration settings.

## Important Note

The documentation includes a warning stating: "This example uses Workflows. For new builds, use a Squad with language-specific assistants." The squad-based approach represents the recommended current methodology.

## Benefits

This workflow approach provides structured language selection without automatic detection, clear analytics by language, and easier maintenance through separated conversation logic for each supported language.
