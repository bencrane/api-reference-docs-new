# Create a Geocoding List | Geocodio API

## Overview

Upload a CSV, TSV, Excel, or other spreadsheet file to be geocoded asynchronously on Geocodio's infrastructure. The file is processed as a background job and can be downloaded when complete. Data is automatically deleted 72 hours after processing completes.

## Endpoint

```
POST https://api.geocod.io/v1.12/lists
```

## URL Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | Yes | Your Geocodio API key |
| `fields` | string | No | Additional field appends to request |

## Form Data Parameters

The request body must be sent as `multipart/form-data`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | file/string | Yes | The file to geocode. Can be uploaded as a form-data file or sent inline |
| `filename` | string | Conditional | Required only if file contents are sent inline. The file extension determines format. Valid formats: `csv`, `tsv`, `xls`, `xlsx`. A zip file containing exactly one supported file can also be uploaded |
| `direction` | string | Yes | `forward` for address-to-coordinate geocoding, or `reverse` for coordinate-to-address geocoding |
| `format` | string | Yes | Template for how addresses or coordinates should be read from the spreadsheet (see format syntax below) |
| `callback` | string | No | A valid HTTPS URL to receive a webhook notification when processing completes |

## Format Syntax

The `format` parameter uses a templating syntax where spreadsheet columns are referenced by their letter enclosed in double curly brackets.

| Scenario | Format Value |
|----------|-------------|
| Full address in column A | `{{A}}` |
| Street in column A, zip in column D | `{{A}} {{D}}` |
| Street in column A, all in Washington DC | `{{A}} Washington DC` |
| Canadian addresses: street (A), city (B), province (C) | `{{A}} {{B}} {{C}} Canada` |
| Reverse geocoding: latitude in A, longitude in B | `{{A}},{{B}}` |

## Example: Upload a File

```bash
curl "https://api.geocod.io/v1.12/lists?api_key=YOUR_API_KEY" \
  -F "file=@sample_list.csv" \
  -F "direction=forward" \
  -F "format={{A}} {{B}} {{C}} {{D}}" \
  -F "callback=https://example.com/my-callback"
```

## Example: Upload Inline Data

```bash
curl "https://api.geocod.io/v1.12/lists?api_key=YOUR_API_KEY" \
  -F "file=$'Zip\n20003\n20001'" \
  -F "filename=file.csv" \
  -F "direction=forward" \
  -F "format={{A}}" \
  -F "callback=https://example.com/my-callback"
```

## Example Response

```json
{
  "id": 48,
  "file": {
    "headers": [
      "address",
      "city",
      "state",
      "zip"
    ],
    "estimated_rows_count": 24,
    "filename": "sample_list.csv"
  }
}
```

## Callback Webhook

When a `callback` URL is provided, Geocodio sends a POST request to that URL upon job completion. The URL must be publicly accessible and served over HTTPS with a valid SSL certificate. Up to 3 delivery attempts are made.

### Webhook POST Body

```json
{
  "id": 49,
  "fields": ["cd"],
  "file": {
    "geocoded_rows_count": 39809,
    "filename": "sample_list.csv"
  },
  "download_url": "https://api.geocod.io/v1.12/lists/49/download"
}
```

## Notes

- Maximum file size is 1GB.
- Recommended maximum of 10 million lookups per list batch. Larger batches should be split into multiple jobs.
- The response `id` is used to check processing status and download results.
