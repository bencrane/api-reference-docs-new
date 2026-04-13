# Billing | Geocodio API

## Stable Address Key Lookups

Looking up a stable address key counts as a regular geocoding lookup. However, if you request field appends using a stable address key, the geocoding portion is free -- you only pay for the field appends. This allows you to enrich already-geocoded addresses with additional data without paying for geocoding again.

```terminal
# Field appends with a stable address key (does not count as a geocoding lookup):
curl "https://api.geocod.io/v1.12/geocode?q=gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3&fields=census,cd&api_key=YOUR_API_KEY"
```

## Address Formats

Geocodio supports geocoding the following address components:

- Streets with or without house numbers (requires a city or ZIP in conjunction)
- Intersections
- Cities
- ZIP codes
- Counties
- States
- PO Boxes (coordinates returned as a centroid of the ZIP code)
- Second address lines such as unit and apartment numbers (used for unit-level geocoding when data is available)

If a city is provided without a state, Geocodio automatically infers the most likely state. Shorthands for cities are accepted (e.g., `NYC`, `SF`).

### Query Format Examples

Geocoding queries can be formatted in various ways:

```
1109 N Highland St, Arlington VA
1109 N Highland Street, Arlington VA
1109 North Highland Street, Arlington VA
1109 N Highland St, 22201
Arlington, VA
Arlington
VA
22201
PO Box 4735, Tulsa OK
Santa Clara County
Santa Clara County, CA
1 Infinite Loop, Santa Clara County
1 Infinite Loop, Santa Clara County, CA
1 Infinite Loop, Santa Clara County, Cupertino CA
```

If no country is specified, the Geocodio engine assumes the country to be USA.

**Canadian address examples:**

```
525 University Ave, Toronto, ON, Canada
7515 118 Ave NW, Edmonton, AB T5B 0X2, Canada
```

## Intersections

You can geocode intersections by specifying two streets. Several separator formats are supported:

```
E 58th St and Madison Ave, New York, NY
Market and 4th, San Francisco
Commonwealth Ave at Washington Street, Boston, MA
Florencia & Perlita, Austin TX
Quail Trail @ Dinkle Rd, Edgewood, NM
8th St SE/I St SE, 20003
```

Intersection results include an additional `address_components_secondary` property. The rest of the response schema is the same as standard geocoding.

```json
{
  "results": [
    {
      "address_components": {
        "street": "4th",
        "suffix": "St",
        "formatted_street": "4th St",
        "city": "San Francisco",
        "county": "San Francisco County",
        "state": "CA",
        "zip": "94103"
      },
      "address_components_secondary": {
        "street": "Market",
        "suffix": "St",
        "formatted_street": "Market St",
        "city": "San Francisco",
        "county": "San Francisco County",
        "state": "CA",
        "zip": "94103"
      },
      "formatted_address": "4th St and Market St, San Francisco, CA 94103",
      "location": {
        "lat": 37.785725,
        "lng": -122.405807
      },
      "accuracy": 1,
      "accuracy_type": "intersection",
      "source": "TIGER/Line dataset from the US Census Bureau"
    }
  ]
}
```
