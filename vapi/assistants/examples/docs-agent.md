# Documentation Agent Guide

## Overview
This guide explains how to build a voice-powered documentation assistant using Vapi and Claude. The system combines speech recognition, retrieval-augmented generation (RAG), and natural language processing to answer user questions about your documentation.

## Key Components

**Initial Setup Requirements:**
- Vapi account with API access
- Documentation files (ideally in llms.txt format)
- LlamaCloud account for indexing

## Implementation Steps

### 1. Documentation Indexing
Index your docs in LlamaCloud using text-embedding-3-small with 512-token chunks and 50-token overlap. Note your pipeline ID and API credentials for later use.

### 2. RAG Tool Creation
Create an API request tool named "docsquery" that connects to your LlamaCloud pipeline. The tool accepts search queries and retrieves relevant documentation sections.

### 3. Assistant Configuration
Build an assistant using Claude 3.5 Sonnet with:
- The docsquery tool attached
- System prompt emphasizing helpful, concise responses
- Deepgram's nova-2 transcriber for speech-to-text
- Vapi's Harry voice for responses
- Analysis plans for call summaries and success evaluation

### 4. Web Integration
Deploy using Vapi's Web SDK to create an interactive voice widget. The component manages call lifecycle, displays real-time transcripts, and handles user interactions.

### 5. Continuous Improvement
Access call analysis through logs to review summaries and success metrics. Use patterns identified in conversation data to refine prompts and improve retrieval quality over time.

## Key Features
- Real-time voice conversations with documentation-backed answers
- Automatic call analysis with success scoring
- Support for multiple programming languages (TypeScript, Python, cURL)
- Dashboard and programmatic configuration options
