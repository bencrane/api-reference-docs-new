# Authentication | Geocodio API

## API Keys

All requests require an API key. Register at [dash.geocod.io](https://dash.geocod.io) to obtain one.

Accounts can have multiple API keys. This is useful for separating projects, revoking access per-project, or tracking usage per key. A CSV of usage and fees per API key is available on the dashboard.

## Using Query Parameter

The simplest authentication method. Include `api_key` as a query parameter on every request:

```terminal
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St,+Arlington+VA&api_key=YOUR_API_KEY"
```

## Using Authorization Header

Alternatively, supply the API key via the `Authorization` HTTP header:

```terminal
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St,+Arlington+VA" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Permissions

By default, an API key can only access single and batch geocoding endpoints. These endpoints are write-only, meaning a compromised key cannot be used to retrieve previously geocoded data from your account.

The following endpoints require explicit permission to be enabled on the [Geocodio dashboard](https://dash.geocod.io):

- **Lists API** -- list geocoding endpoints
- **Distance API** -- distance calculation endpoints

Geocodio recommends creating separate API keys for single/batch endpoints and for GET/DELETE access to lists/jobs.

### 403 Forbidden Response

A `403 Forbidden` status code is returned when the API key is valid but lacks permission for the requested endpoint:

```json
{
  "error": "This API key does not have permission to access this feature. API key permissions can be changed in the Geocodio dashboard at https://dash.geocod.io/apikey"
}
```
