# Segment API [Pro]

## Overview

The Segment API automatically groups domains into segments based on business similarities. You can upload results from Discover or your own domain lists to identify ICP patterns, with each segment including a label and associated domains.

## Endpoint

```
POST https://api.discolike.com/v1/segment
```

## Parameters

Upload a CSV or Excel file with domains (maximum 1MB, 10,000 rows) using `Content-Type: multipart/form-data`.

| Parameter | Description |
|-----------|-------------|
| domain_column | Column containing domains (auto-detected if omitted) |
| max_segments | Maximum segments to create (auto if omitted) |

## Response Fields

Returns BizData profiles with additional segment fields:

| Field | Type | Description |
|-------|------|-------------|
| status | String | `in_progress`, `completed`, or `failed` |
| progress | Integer | Progress percentage |
| results | Array | BizData profiles with segment info |
| segment_id | Integer | Assigned segment ID |
| segment_description | String | AI-generated segment description |
| probability | Float | Confidence of segment assignment |

## Example Request

```bash
curl --form file='@data.csv' "https://api.discolike.com/v1/segment" \
  -H "x-discolike-key: API_KEY"
```

## Initial Response

```json
{
  "task_id": "e362cb75-35e2-4006-a239-3d87a7472872"
}
```

## Check Status

```bash
curl "https://api.discolike.com/v1/segment/status/{task_id}" \
  -H "x-discolike-key: API_KEY"
```

Response:

```json
{
  "status": "in_progress",
  "progress": 30
}
```

## Final Response

```json
{
  "status": "completed",
  "progress": 100,
  "results": [
    {
      "domain": "acmesecurity.com",
      "name": "Acme Security",
      "score": 450,
      "segment_id": 0,
      "segment_description": "Cybersecurity Platforms and Solutions",
      "probability": 1.0
    }
  ]
}
```
