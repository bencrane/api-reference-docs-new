> Sources:
> - https://trigger.dev/docs/management/waitpoints/create
> - https://trigger.dev/docs/management/waitpoints/list
> - https://trigger.dev/docs/management/waitpoints/retrieve
> - https://trigger.dev/docs/management/waitpoints/complete
> - https://trigger.dev/docs/management/waitpoints/complete-callback

# Waitpoints API

## Create a waitpoint token

v3-openapi POST /api/v1/waitpoints/tokens
Creates a new waitpoint token that can be used to pause a run until an external event completes it. The token includes a `url` which can be called via HTTP POST to complete the waitpoint. Use the token ID with `wait.forToken()` inside a task to pause execution until the token is completed.

---

## List waitpoint tokens

v3-openapi GET /api/v1/waitpoints/tokens
Returns a paginated list of waitpoint tokens for the current environment. Results are ordered by creation date, newest first. Use cursor-based pagination with `page[after]` and `page[before]` to navigate pages.

---

## Retrieve a waitpoint token

v3-openapi GET /api/v1/waitpoints/tokens/{waitpointId}
Retrieves a waitpoint token by its ID, including its current status and output if it has been completed.

---

## Complete a waitpoint token

v3-openapi POST /api/v1/waitpoints/tokens/{waitpointId}/complete
Completes a waitpoint token, unblocking any run that is waiting for it via `wait.forToken()`. An optional `data` payload can be passed and will be returned to the waiting run. If the token is already completed, this is a no-op and returns `success: true`.

This endpoint accepts both secret API keys and short-lived JWTs (public access tokens), making it safe to call from frontend clients.

---

## Complete a waitpoint token via HTTP callback

v3-openapi POST /api/v1/waitpoints/tokens/{waitpointId}/callback/{callbackHash}
Completes a waitpoint token using the pre-signed callback URL returned in the `url` field when the token was created. No API key is required — the `callbackHash` in the URL acts as the authentication token.

This is designed to be given directly to external services (e.g. as a webhook URL) so they can unblock a waiting run without needing access to your API key. The entire request body is passed as the output data to the waiting run.

If the token is already completed, this is a no-op and returns `success: true`.

---
