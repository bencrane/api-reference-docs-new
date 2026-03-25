# Calculate Expected LLM Usage

## Endpoint Overview

The ElevenLabs API provides a POST endpoint at `https://api.elevenlabs.io/v1/convai/agent/{agent_id}/llm-usage/calculate` that calculates expected number of LLM tokens needed for the specified agent.

## Request Parameters

The endpoint accepts three optional body parameters:

- **prompt_length** (integer): Character count of the prompt
- **number_of_pages** (integer): Pages in PDFs or URLs within the agent's Knowledge Base
- **rag_enabled** (boolean): Indicates whether Retrieval-Augmented Generation is active

An optional `xi-api-key` header can be included for authentication.

## Response Structure

A successful 200 response returns an object containing `llm_prices` -- an array of objects, each specifying:
- **llm**: The model identifier (from an extensive list including Claude, GPT, and Gemini variants)
- **price_per_minute**: Cost as a numeric value

## Supported Models

The API supports numerous LLM models including Claude variants (claude-sonnet-4-5, claude-haiku-4-5), OpenAI models (gpt-4o, gpt-5 series), Google Gemini models, and others.

## Code Examples

The documentation includes SDK implementations for TypeScript, Python, Go, Ruby, Java, PHP, C#, and Swift, all demonstrating the basic usage pattern with minimal parameters.
