# Create new instances.

`POST /accounts/{account_id}/ai-search/instances`

Create a new instances.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ai_gateway_id** (string, optional): 
- **ai_search_model** (string, optional):  Values: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/zai-org/glm-4.7-flash`, `@cf/meta/llama-3.1-8b-instruct-fast`, `@cf/meta/llama-3.1-8b-instruct-fp8`, `@cf/meta/llama-4-scout-17b-16e-instruct`, `@cf/qwen/qwen3-30b-a3b-fp8`, `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`, `@cf/moonshotai/kimi-k2-instruct`, `@cf/google/gemma-3-12b-it`, `anthropic/claude-3-7-sonnet`, `anthropic/claude-sonnet-4`, `anthropic/claude-opus-4`, `anthropic/claude-3-5-haiku`, `cerebras/qwen-3-235b-a22b-instruct`, `cerebras/qwen-3-235b-a22b-thinking`, `cerebras/llama-3.3-70b`, `cerebras/llama-4-maverick-17b-128e-instruct`, `cerebras/llama-4-scout-17b-16e-instruct`, `cerebras/gpt-oss-120b`, `google-ai-studio/gemini-2.5-flash`, `google-ai-studio/gemini-2.5-pro`, `grok/grok-4`, `groq/llama-3.3-70b-versatile`, `groq/llama-3.1-8b-instant`, `openai/gpt-5`, `openai/gpt-5-mini`, `openai/gpt-5-nano`, ``, ``
- **cache** (boolean, optional): 
- **cache_threshold** (string, optional):  Values: `super_strict_match`, `close_enough`, `flexible_friend`, `anything_goes`
- **chunk** (boolean, optional): 
- **chunk_overlap** (integer, optional): 
- **chunk_size** (integer, optional): 
- **custom_metadata** (array, optional): 
- **embedding_model** (string, optional):  Values: `@cf/qwen/qwen3-embedding-0.6b`, `@cf/baai/bge-m3`, `@cf/baai/bge-large-en-v1.5`, `@cf/google/embeddinggemma-300m`, `google-ai-studio/gemini-embedding-001`, `google-ai-studio/gemini-embedding-2-preview`, `openai/text-embedding-3-small`, `openai/text-embedding-3-large`, ``, ``
- **fusion_method** (string, optional):  Values: `max`, `rrf`
- **hybrid_search_enabled** (boolean, optional): 
- **id** (string, required): AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores.
- **indexing_options** (object, optional): 
- **max_num_results** (integer, optional): 
- **metadata** (object, optional): 
- **namespace** (string, optional): 
- **public_endpoint_params** (object, optional): 
- **reranking** (boolean, optional): 
- **reranking_model** (string, optional):  Values: `@cf/baai/bge-reranker-base`, ``, ``
- **retrieval_options** (object, optional): 
- **rewrite_model** (string, optional):  Values: `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/zai-org/glm-4.7-flash`, `@cf/meta/llama-3.1-8b-instruct-fast`, `@cf/meta/llama-3.1-8b-instruct-fp8`, `@cf/meta/llama-4-scout-17b-16e-instruct`, `@cf/qwen/qwen3-30b-a3b-fp8`, `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`, `@cf/moonshotai/kimi-k2-instruct`, `@cf/google/gemma-3-12b-it`, `anthropic/claude-3-7-sonnet`, `anthropic/claude-sonnet-4`, `anthropic/claude-opus-4`, `anthropic/claude-3-5-haiku`, `cerebras/qwen-3-235b-a22b-instruct`, `cerebras/qwen-3-235b-a22b-thinking`, `cerebras/llama-3.3-70b`, `cerebras/llama-4-maverick-17b-128e-instruct`, `cerebras/llama-4-scout-17b-16e-instruct`, `cerebras/gpt-oss-120b`, `google-ai-studio/gemini-2.5-flash`, `google-ai-studio/gemini-2.5-pro`, `grok/grok-4`, `groq/llama-3.3-70b-versatile`, `groq/llama-3.1-8b-instant`, `openai/gpt-5`, `openai/gpt-5-mini`, `openai/gpt-5-nano`, ``, ``
- **rewrite_query** (boolean, optional): 
- **score_threshold** (number, optional): 
- **source** (string, optional): 
- **source_params** (object, optional): 
- **token_id** (string, optional): 
- **type** (string, optional):  Values: `r2`, `web-crawler`, ``

## Response

### 201

Returns the created Object

- **result** (object): 
- **success** (boolean): 

### 400

Input Validation Error

- **errors** (array): 
- **success** (boolean):
