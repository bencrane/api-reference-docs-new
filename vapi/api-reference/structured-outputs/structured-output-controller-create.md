# Create Structured Output - API Reference

## Endpoint Details

**Method:** POST
**URL:** `https://api.vapi.ai/structured-output`
**Content-Type:** `application/json`

## Description

This endpoint enables creation of structured data extraction configurations that can be applied to conversations. The system supports two extraction types: AI-based (using language models) and regex-based pattern matching.

## Authentication

**Header Parameter:** `Authorization`
- **Type:** string
- **Required:** true
- **Description:** Retrieve your API Key from Dashboard (dashboard.vapi.ai).

## Request Body Schema

The request uses the `CreateStructuredOutputDTO` schema with the following properties:

### Required Fields

- **name** (string): Identifier for the structured output configuration
- **schema** (JsonSchema): JSON Schema definition specifying extraction structure

### Optional Fields

- **type** (string): Extraction methodology
  - `ai` (default): Uses an LLM for intelligent extraction
  - `regex`: Pattern-based extraction without model inference

- **description** (string): Documentation of extraction purpose and usage

- **regex** (string): Pattern for regex-type extraction. Supports raw patterns (`\d+`) and literal format (`/\d+/gi`). Uses RE2 syntax.

- **model** (object): Specifies the language model for AI extraction. Supports:
  - OpenAI models (GPT-4.1 default)
  - Anthropic Claude variants
  - Google Gemini models
  - Custom LLM providers

- **compliancePlan** (object): Optional compliance overrides for sensitive data handling

- **assistantIds** (array): Links this output to specific assistants

- **workflowIds** (array): Links this output to workflow executions

## Response Schema

**Status:** 201 Created

The response returns a `StructuredOutput` object containing:

- **id** (string): Unique identifier
- **orgId** (string): Organization ownership identifier
- **createdAt** (string): ISO 8601 timestamp
- **updatedAt** (string): ISO 8601 timestamp
- **name** (string): Configuration name
- **schema** (JsonSchema): Extraction structure definition
- **type** (string): Extraction type used
- **description** (string): Configuration documentation
- **model** (object): Model configuration employed
- **regex** (string): Pattern if regex-based
- **assistantIds** (array): Linked assistant identifiers
- **workflowIds** (array): Linked workflow identifiers

## Code Example

```python
from vapi import Vapi, JsonSchema

client = Vapi(token="YOUR_TOKEN_HERE")

client.structured_outputs.structured_output_controller_create(
    schema=JsonSchema(type="string")
)
```

## JsonSchema Properties

- **type** (required): Defines output data type (string, number, integer, boolean, array, object)
- **items**: Schema for array contents (when type is array)
- **properties**: Object property definitions (when type is object)
- **description**: Guidance for model understanding
- **pattern**: Regex validation for string values
- **format**: Predefined formats (date-time, email, uuid, etc.)
- **required**: List of mandatory properties (for objects)
- **enum**: Restricted value options
- **title**: Schema name
