# Using the Query Tool for Knowledge Bases

## Overview

The Query Tool allows AI assistants to access custom knowledge bases. It enables retrieval of information from uploaded files, improving response accuracy through domain-specific data rather than general knowledge.

## Key Benefits

The documentation highlights three main advantages:

- **Contextual Understanding**: Assistants can answer specialized questions using specific knowledge
- **Accuracy**: Responses derive from verified information sources
- **Customization**: Multiple knowledge bases support different topics

## Configuration Process

### Step 1: File Upload

Files form the foundation of knowledge bases. The documentation provides two methods:

**Dashboard Method**: Navigate to Files, click Upload File, select documents, and note generated file IDs.

**API Method**: Use curl with your API key to upload files programmatically.

### Step 2: Create Query Tool

After uploading, create the tool by:

1. Selecting "Query" as tool type
2. Naming it appropriately (e.g., "Product Query")
3. Adding knowledge bases with descriptive names and file IDs
4. Including descriptions explaining content purpose

### Step 3: Attach to Assistant

Connect the tool to your assistant and update its system prompt with explicit instructions about when to use it.

## Important Configuration Notes

The documentation emphasizes that "descriptions help your assistant understand when to use particular knowledge bases." However, system prompt instructions are essential—descriptions alone are insufficient for tool activation.

## Advanced Features

- Configure multiple knowledge bases within one query tool
- Organize by topic for improved retrieval
- Use specific tool names in system prompts

## Best Practices

Keep files under 300KB, use descriptive naming conventions, test thoroughly, and maintain current information.
