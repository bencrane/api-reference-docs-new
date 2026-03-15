# Prospeo - Account Information API

## Account Information API

This endpoint allows you to retrieve information about the current user's usage, remaining credits, current plan, and next quota renewal date.

> This endpoint is free to use.

## Endpoint

```
GET https://api.prospeo.io/account-information
```

- **URL:** `https://api.prospeo.io/account-information`
- **Method:** `GET`
- **Headers:**
  - `X-KEY`: your_api_key

## Parameters

This endpoint does not require any parameters.

## Response

A successful request will return the following information:

```json
{
    "error": false,
    "response": {
        "current_plan": "STARTER",
        "current_team_members": 1,
        "remaining_credits": 99,
        "used_credits": 1,
        "next_quota_renewal_days": 25,
        "next_quota_renewal_date": "2023-06-18 20:52:28+00:00"
    }
}
```

| Property | Type | Description |
|---|---|---|
| `current_plan` | string | The current plan you are subscribed to. |
| `remaining_credits` | integer | The number of credits remaining. |
| `current_team_members` | integer | The number of team members in your team. |
| `used_credits` | integer | The number of credits already used. |
| `next_quota_renewal_days` | integer | The number of days until the next quota renewal. |
| `next_quota_renewal_date` | string | The date and time of the next quota renewal. |

## Error Codes

| HTTP Code | `error_code` Property | Meaning |
|---|---|---|
| 401 | `INVALID_API_KEY` | Invalid API key, check your X-KEY header. |
| 429 | `RATE_LIMITED` | You hit the rate limit for your current plan. |
| 400 | `INVALID_REQUEST` | The request you submitted is invalid. |
| 400 | `INTERNAL_ERROR` | An error occurred on our side, please contact the support. |

---

If you need further assistance, feel free to contact us at [contact@prospeo.io](mailto:contact@prospeo.io).