# Multilingual Support Agent Documentation

## Overview

This guide demonstrates how to construct a customer support agent for GlobalTech International that identifies and responds in customers' preferred languages (English, Spanish, French) with automatic detection and real-time adaptation capabilities.

## Key Components

### 1. Knowledge Base Setup
The implementation requires three CSV files containing customer data, product information, and support articles. These files are uploaded to the Vapi platform and assigned file IDs for reference in tool configurations.

### 2. Assistant Configuration
The core agent, named "Maria," operates with a comprehensive system prompt emphasizing:
- Fluency across three languages with culturally appropriate communication styles
- English: "Direct, friendly, professional" approach
- Spanish: "Warm, respectful" with initial formal address conventions
- French: "Polite, courteous, professional" following formal greeting protocols

### 3. Transcription Setup
Deepgram (Nova 2/3) with "multi" language setting or Google's multilingual model enables automatic language detection without manual selection.

### 4. Voice Synthesis
Azure provides 400+ voices across 140+ languages, supporting language-specific speakers like "en-US-AriaNeural" for English and "es-ES-ElviraNeural" for Spanish.

### 5. Multilingual Tools
Three primary functions support the assistant:
- **lookup_customer**: Retrieves customer information including language preferences
- **get_product_info**: Delivers product details in customer languages
- **search_support_articles**: Returns troubleshooting guides in preferred languages

### 6. Phone Integration
The configuration includes creating a Vapi phone number linked to the assistant, enabling inbound calls with recording and voicemail detection.

## Alternative Approach

A squad-based workflow offers structured language selection where customers explicitly choose their language, routing them to dedicated conversation paths optimized for each language.

## Provider Compatibility

**Transcription providers** supporting multilingual detection include Gladia and Deepgram, while others require single-language configuration. **Voice synthesis** is available across Azure, ElevenLabs, OpenAI, and PlayHT with extensive language support. All major language models natively support multilingual functionality.
