# Introduction to Knowledge Bases

## Overview

Vapi's Knowledge Base is described as "a collection of custom files that contain information on specific topics or domains." By incorporating one into your AI assistant, you enable it to deliver responses grounded in your proprietary data rather than relying solely on general training knowledge.

## Key Benefits

The documentation highlights four main advantages:

- **Accuracy improvements**: Responses derive from your verified information sources
- **Domain expertise**: Assistants can address sophisticated, specialized inquiries with detailed context
- **Tailored responses**: Configure your system for particular industries or subjects
- **Current content**: You maintain control, ensuring your assistant accesses the latest materials

## Creation Methods

### Dashboard Approach

The simpler path involves three steps: uploading files through `Build > Files`, associating them with your assistant in the configuration panel, and publishing. Supported formats include `.txt`, `.pdf`, `.docx`, `.csv`, `.md`, `.yaml`, `.json`, `.xml`, and `.log` files.

When published, Vapi automatically generates a default query tool incorporating your selected files.

### API Approach

For advanced implementations, developers can programmatically manage Knowledge Bases through API endpoints. This enables:

- File upload and ID retrieval
- Custom query tool creation with specialized configurations
- Multiple knowledge base integration within single tools
- Advanced retrieval parameters

## Optimization Guidelines

The documentation recommends maintaining files under 300KB, organizing content with logical hierarchies, employing accessible language, and conducting thorough testing. Regular updates and sufficient contextual information within documents improve retrieval quality.

## Current Limitations

Knowledge Base functionality presently supports Google/Gemini models for retrieval operations.
