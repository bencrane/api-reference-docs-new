# Static Variables and Aliases

## Overview

Vapi tools enable two key features for deterministic data movement between tool calls:

1. **Static variables (parameters)** inject fixed or template-resolved values into every tool call, bypassing LLM interpretation
2. **Variable extraction (aliases)** extract specific fields from JSON responses for use in subsequent tool calls

As the documentation states: "Combined, these features enable **deterministic tool chaining** -- Tool A fetches data and extracts variables, Tool B receives those variables automatically."

## Static Variables (Parameters)

The `parameters` field defines key-value pairs merged into tool requests. Key characteristics:

- Composed of `{ key, value }` objects on the tool definition
- Values support Liquid templates (e.g., `{{ customer.number }}`)
- Merged **after** LLM-generated arguments, overriding duplicate keys
- Supported for `apiRequest` and `function` tool types only

### Supported Tool Types
| Tool Type | Support |
|-----------|---------|
| apiRequest | Yes |
| function | Yes |
| code | No |
| handoff | No |

**Key insight:** Static parameters remain "invisible to the LLM" and cannot be overridden by model-generated values.

## Variable Extraction (Aliases)

The `variableExtractionPlan` field stores named variables from tool responses using the `aliases` array:

- `key`: the variable name to store
- `value`: Liquid template expression referencing response fields
- Root context available as `$` (e.g., `{{ $.data.id }}`)
- Top-level properties accessible directly
- Supports Liquid filters: `{{ $.email | downcase }}`

### Supported Tool Types
| Tool Type | Support |
|-----------|---------|
| apiRequest | Yes |
| function | Yes |
| code | Yes |
| handoff | Yes |

## Deterministic Tool Chaining

Tools can be sequenced so responses from one automatically feed into the next without LLM involvement in data transfer. Extracted variables persist throughout the call and become available in subsequent tool configurations.

## Essential Tips

- Template expressions evaluate at execution time, not creation time
- Extracted variables are global to the call; use descriptive names to prevent collisions
- Variable extraction requires valid JSON responses; non-JSON responses fail silently
- Liquid filters enable response transformations within aliases
