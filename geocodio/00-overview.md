# Overview | Geocodio API

## Introduction

Geocodio provides RESTful API endpoints for forward and reverse geocoding lookups, with simultaneous data enrichment. The API supports individual, batch, and list (CSV) geocoding.

Data appends (fields) include Census geographies and data, electoral districts, timezones, school districts, and more.

All HTTP responses (including errors) are returned as JSON. New properties may be added to the output in the future, but existing properties will not be changed or removed without a new API version release.

## Base URL

```
https://api.geocod.io/v1.12/
```

The versioning prefix is required for all requests.

## Supported Countries

| Capability | United States | Canada | Mexico |
|---|---|---|---|
| Forward geocoding | Yes | Yes | Yes |
| Reverse geocoding | Yes | Yes | Yes |
| Distance | Yes | Yes | Yes |

## Specifying Country

**Default behavior:** For individual lookups, the country is inferred from the address format. The fallback is United States.

Use the `country` query parameter to specify the country explicitly. Supported values: `USA`, `Canada`, or `Mexico`.

```terminal
# US address (explicit)
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St,+Arlington+VA&country=USA&api_key=YOUR_API_KEY"

# Canadian address (explicit)
curl "https://api.geocod.io/v1.12/geocode?q=525+University+Ave,+Toronto+ON&country=Canada&api_key=YOUR_API_KEY"

# Mexican address (explicit)
curl "https://api.geocod.io/v1.12/geocode?q=Paseo+de+la+Reforma+505,+Ciudad+de+Mexico&country=Mexico&api_key=YOUR_API_KEY"
```

## Address Format Differences

**United States**
- State: 2-letter abbreviation (e.g., `VA`, `CA`)
- ZIP Code: 5 or 9 digits (e.g., `22201` or `22201-1234`)

**Canada**
- Province: 2-letter abbreviation (e.g., `ON`, `BC`)
- Postal Code FSA: 3 characters with space (e.g., `M5G`)

**Mexico**
- State: Varies (e.g., `CDMX`, `Jal.`, `Jalisco`)
- Postal Code: 5 digits (e.g., `06500`)

## Geocoding Methods

Geocodio supports three methods for processing geocoding data. Single and batch methods are synchronous (results returned directly in the response). List geocoding is asynchronous (requires a second request to download results).

| Name | Batch size | Type | Format | Supports data appends (fields) | Supports forward & reverse geocoding |
|---|---|---|---|---|---|
| Single geocoding | 1 | Synchronous | JSON | Yes | Yes |
| Batch geocoding | Up to 10,000 | Synchronous | JSON | Yes | Yes |
| List geocoding | Up to 10,000,000+ | Asynchronous | CSV/TSV/Excel | Yes | Yes |

## Distance Methods

Geocodio's distance API calculates driving time, driving distance, and straight line (haversine) distance between addresses or coordinates. One-to-one, one-to-many, and many-to-many matrices are supported, and results can be limited to a specified radius.

For distance, batch size is the total number of calculations (origins x destinations).

| Name | Batch size (calculations) | Type | Format | Supports addresses & coordinates |
|---|---|---|---|---|
| Single origin distance | 100 | Synchronous | JSON | Yes |
| Distance matrix | Up to 10,000 | Synchronous | JSON | Yes |
| Distance jobs | Up to 50,000 | Asynchronous | JSON | Yes |
