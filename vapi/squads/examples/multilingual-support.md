# Multilingual Support Squad

## Overview
This documentation describes a Squad implementation that delivers structured customer support across multiple languages. The system presents users with a language selection prompt, then routes them to dedicated assistants configured for English, Spanish, or French with appropriate system prompts and localized voices.

## Key Features
The Squad offers:
- "Explicit language choice for clarity"
- Language-specific prompts and voices
- Seamless handoffs while preserving context

## Architecture

### Squad Members
The implementation defines three assistant members:

1. **English Support** - Uses OpenAI's GPT-4o with an Azure Aria neural voice, featuring the opening line "Hello! How can I help you today?" and configured to speak first
2. **Soporte Español** - Spanish-language assistant with culturally appropriate greeting protocols
3. **Support Français** - French assistant emphasizing formal politeness

Each member uses the same GPT-4o model but with distinct system prompts tailored to language norms and communication styles.

## Implementation Options

The documentation provides three approaches:
- TypeScript Server SDK
- Python Server SDK
- cURL command-line interface

All three methods configure the Squad with identical member definitions and transport settings.

## Setup Process

Users should:
1. Define squad members with language-specific configurations
2. Create an entrance flow for language selection
3. Deploy using preferred SDK or API method
4. Test each language pathway with a dedicated phone number

## Related Resources
The documentation references an alternative approach: "Multilingual agent" for assistants handling multiple languages within a single instance.
