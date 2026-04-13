# Stable Address Keys | Geocodio API

## Overview

Every geocoding result includes a `stable_address_key` -- a deterministic identifier that uniquely represents the geocoded address.

- For `rooftop`, `range_interpolation`, and other house number-level results, the key is unique to a specific house number on a street.
- For `street_center` results, the key is unique to a specific street.

### Example Response

```json
{
  "results": [
    {
      "address_components": { "..." : "..." },
      "formatted_address": "1109 N Highland St, Arlington, VA 22201",
      "location": {
        "lat": 38.886665,
        "lng": -77.094733
      },
      "accuracy": 1,
      "accuracy_type": "rooftop",
      "source": "Virginia GIS Clearinghouse",
      "stable_address_key": "gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3"
    }
  ]
}
```

---

## Unit Suffixes

When a secondary address component is provided (e.g. apartment, suite, or unit number), the stable address key includes a unit suffix appended with a dash separator.

```
gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3          -- the building at 734 Ave C, El Campo TX
gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3-a1b2c3   -- Unit A at 734 Ave C, El Campo TX
gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3-d4e5f6   -- Unit B at 734 Ave C, El Campo TX
```

The base key (before the dash) identifies the street address, while the suffix identifies the specific unit.

The full key with unit suffix can be used as input for geocoding and distance calculations. If the specific unit is not found in the database, the lookup falls back to the building-level result.

The unit suffix is computed regardless of whether unit-level coordinates exist. If a unit is specified in the input address, the suffix is always included in the key.

---

## Use Cases

Store the stable address key alongside your geocoded results. They are useful for:

- **Deduplication:** Two addresses that resolve to the same location share the same stable address key, making it easy to identify and deduplicate addresses in your database.
- **Updated results:** Store the key and use it to retrieve the latest geocoding data for an address in the future. For example, a `range_interpolation` result may be upgraded to `rooftop` as coverage improves.
- **Data enrichment:** Request additional field appends for previously geocoded addresses without paying for geocoding again (see Billing below).

---

## Guarantees

- **Persistent:** A stable address key, once issued, will always remain valid and can be used to look up the same address in the future.
- **Deterministic:** The same address will always produce the same stable address key, regardless of minor formatting differences (e.g. "Street" vs "St", "North" vs "N").
- **Cross-version:** Stable address keys work across all API versions.

---

## What to Expect

- **Results may improve over time:** The coordinates or accuracy type returned for a stable address key may change as data coverage improves. This is by design -- you will always get the best available result.
- **New keys may be issued:** As coverage expands, an address that previously returned a `street_center`-level key may return a more specific house number-level key in the future.

Treat the stable address key as an opaque string. Do not parse or rely on the internal format of the key, as it may change for newly issued keys. The length of the string is not guaranteed to be fixed. Existing keys will always remain valid.

---

## Using Stable Address Keys as Input

Pass a stable address key anywhere an address is accepted as input. This includes single geocoding, batch geocoding, distance endpoints, and list geocoding. Use it as the `q` parameter or as an item in a batch request.

### Geocoding with a Stable Address Key

```bash
curl "https://api.geocod.io/v1.12/geocode?q=gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3&api_key=YOUR_API_KEY"
```

### Field Appends with a Stable Address Key

Field appends using a stable address key do not count as a geocoding lookup -- only the field append cost applies.

```bash
curl "https://api.geocod.io/v1.12/geocode?q=gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3&fields=census,cd&api_key=YOUR_API_KEY"
```

---

## Billing

When you look up a stable address key, it counts as a regular geocoding lookup. However, if you request field appends using a stable address key, the geocoding portion is free and you only pay for the field appends. This means you can enrich already-geocoded addresses with additional data without paying for geocoding again.
