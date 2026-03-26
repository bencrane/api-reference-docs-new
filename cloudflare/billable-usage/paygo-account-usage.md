# Get PayGo Account Billable Usage (Beta)

`GET /accounts/{account_id}/billing/usage/paygo`

Returns billable usage data for PayGo (self-serve) accounts.
When no query parameters are provided, returns usage for the current
billing period.
This endpoint is currently in beta and access is restricted to select
accounts.


## Parameters

- **account_id** (string, required) [path]: Identifies the account.
- **from** (string, optional) [query]: Defines the start date for the usage query (e.g., 2025-02-01).
- **to** (string, optional) [query]: Defines the end date for the usage query (e.g., 2025-03-01).

## Response

### 200

Indicates PayGo account usage data was successfully retrieved.

- **errors** (array): Contains error details if the request failed.
- **messages** (array): Contains informational notices about the response.
- **result** (array): Contains the array of billable usage records.
- **success** (boolean): Indicates whether the API call was successful.

### 4XX

Indicates the request failed.

- **errors** (array): Contains error details describing why the request failed.
- **messages** (array): Contains informational notices about the response.
- **result** (object): Contains the response payload (always null on failure).
- **success** (boolean): Indicates whether the API call was successful.
