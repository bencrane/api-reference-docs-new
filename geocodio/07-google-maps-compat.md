# Google Maps Compatibility | Geocodio API

## Overview

Geocodio provides a Google Maps-compatible geocoding endpoint, enabling you to migrate from Google Maps with minimal code changes. Point your existing Google Maps SDK to `https://api.geocod.io` and use your Geocodio API key.

The compatibility layer returns responses in Google Maps' format, so your existing response parsing code continues to work unchanged.

For new integrations or to access Geocodio's full feature set (like data appends and batch geocoding), use the native Geocodio API instead.

---

## Endpoint

```
GET https://api.geocod.io/maps/api/geocode/json
```

## Request Parameters

| Parameter | Description | Required |
|---|---|---|
| `address` | The address to geocode (for forward geocoding) | Either `address` or `latlng` |
| `latlng` | Coordinates in `lat,lng` format (for reverse geocoding) | Either `address` or `latlng` |
| `key` | Your Geocodio API key | Yes |
| `components` | Address component filters (e.g. `country:US`) | No |

---

## Examples

### Forward Geocoding

```bash
curl "https://api.geocod.io/maps/api/geocode/json?address=1109+N+Highland+St,+Arlington+VA&key=YOUR_API_KEY"
```

### Reverse Geocoding

```bash
curl "https://api.geocod.io/maps/api/geocode/json?latlng=38.886665,-77.094733&key=YOUR_API_KEY"
```

### Using the Python Google Maps SDK

```python
# Install: pip install googlemaps
import googlemaps

# Configure client to use Geocodio endpoint
gmaps = googlemaps.Client(
    key='YOUR_GEOCODIO_API_KEY',
    base_url='https://api.geocod.io'
)

# Forward geocoding - same code as Google Maps
geocode_result = gmaps.geocode('1109 N Highland St, Arlington VA')
location = geocode_result[0]['geometry']['location']
print(f"Lat: {location['lat']}, Lng: {location['lng']}")

# Reverse geocoding - same code as Google Maps
reverse_result = gmaps.reverse_geocode((38.886665, -77.094733))
print(reverse_result[0]['formatted_address'])
```

### Using the Node.js Google Maps SDK

```javascript
// Install: npm install @googlemaps/google-maps-services-js
const { Client } = require("@googlemaps/google-maps-services-js");

const client = new Client({});

// Forward geocoding - add 'url' parameter to use Geocodio
client.geocode({
    params: {
        address: "1109 N Highland St, Arlington VA",
        key: "YOUR_GEOCODIO_API_KEY"
    },
    url: "https://api.geocod.io/maps/api/geocode/json"
})
.then(response => {
    const location = response.data.results[0].geometry.location;
    console.log(`Lat: ${location.lat}, Lng: ${location.lng}`);
});

// Reverse geocoding - add 'url' parameter to use Geocodio
client.reverseGeocode({
    params: {
        latlng: "38.886665,-77.094733",
        key: "YOUR_GEOCODIO_API_KEY"
    },
    url: "https://api.geocod.io/maps/api/geocode/json"
})
.then(response => {
    console.log(response.data.results[0].formatted_address);
});
```

---

## What's Supported

### Request Parameters

| Parameter | Status |
|---|---|
| `address` | Supported -- forward geocoding |
| `latlng` | Supported -- reverse geocoding |
| `key` | Supported -- API authentication |
| `components` | Supported -- address component filtering (see below) |

### Address Components

The endpoint transforms Geocodio's address components into Google Maps format with these component types:

| Google Maps Type | Geocodio Equivalent |
|---|---|
| `street_number` | House/building number |
| `route` | Street name (includes predirectional, prefix, street, suffix, postdirectional) |
| `locality` | City name |
| `administrative_area_level_2` | County |
| `administrative_area_level_1` | State/province (with full name expansion, e.g. VA to Virginia, ON to Ontario) |
| `country` | Country code and full name |
| `postal_code` | ZIP/postal code |

### Component Filtering

The `components` parameter supports filtering results:

| Filter | Description |
|---|---|
| `country:XX` | Filter by country code (`US`, `CA`, `MX`) |
| `postal_code:XXXXX` | Filter by postal code |
| `locality:CityName` | Filter by city/locality |
| `administrative_area:State` | Filter by state/province |
| `route:StreetName` | Filter by street name |

Multiple filters can be combined with a pipe: `components=country:US|postal_code:22201`

### Supported Countries

- United States (`US`)
- Canada (`CA`) -- with proper province expansion (e.g. ON to Ontario, QC to Quebec)
- Mexico (`MX`)

### Response Format

| Field | Status |
|---|---|
| `address_components` | Supported -- typed address component arrays with proper component types |
| `formatted_address` | Supported -- full formatted address string |
| `geometry.location` | Supported -- latitude and longitude coordinates |
| `geometry.location_type` | Supported -- accuracy indicator (`ROOFTOP`, `RANGE_INTERPOLATED`, `GEOMETRIC_CENTER`, `APPROXIMATE`) |
| `geometry.viewport` | Supported -- bounding box for the result |
| `types` | Supported -- result type indicators |
| `status` | Supported -- response status (`OK`, `ZERO_RESULTS`, `REQUEST_DENIED`, etc.) |
| `place_id` | Supported -- returns the Geocodio stable address key for each result |
| `partial_match` | Supported -- added when accuracy < 1.0 |

### Additional Features

- **State/Province Expansion** -- Short codes expanded to full names (VA to Virginia, ON to Ontario, QC to Quebec)
- **Street Components** -- Properly combines predirectional (N, S, E, W), street name, suffix (St, Ave), and postdirectional (NW, SE)
- **Location Type Mapping** -- Maps Geocodio accuracy to Google's location types (`ROOFTOP`, `RANGE_INTERPOLATED`, `GEOMETRIC_CENTER`, `APPROXIMATE`)
- **Partial Match Indicator** -- Automatically adds `partial_match: true` when accuracy is less than 1.0

---

## What's Different

### Response Differences

| Field | Notes |
|---|---|
| `place_id` | Returns the Geocodio stable address key (e.g. `gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3`). These are Geocodio identifiers, not Google Place IDs |
| `plus_code` | Not provided |
| `geometry.viewport` | Provided but approximated (not based on actual address boundaries) |

### Parameter Limitations

| Parameter | Status |
|---|---|
| `bounds` | Not supported -- viewport biasing parameter is ignored if provided |
| `region` | Not supported -- region biasing parameter is ignored if provided |
| `components` | Partially supported -- supports `country`, `postal_code`, `locality`, `administrative_area`, and `route` filtering. Other component types are not supported |

### Coverage

US, Canada, and Mexico only. Requests for addresses in other countries return `ZERO_RESULTS` status.

### Error Responses

All responses return HTTP 200 with status information in the response body (matching Google's behavior). Possible status values:

| Status | Meaning |
|---|---|
| `OK` | Request successful |
| `ZERO_RESULTS` | No results found |
| `REQUEST_DENIED` | Invalid API key |
| `INVALID_REQUEST` | Missing or invalid parameters |
| `OVER_QUERY_LIMIT` | Rate limit exceeded |
