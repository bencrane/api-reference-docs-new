# Resource Proofs - Update

Updates the specified resource proof.

## Authorization
`basicAuth`

## HTTP Request
```
PATCH /resource_proofs/{res_prf_id}
```

## Path Parameters

| Parameter | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `res_prf_id` | string (res_prf_id) | Yes | `^res_prf_[a-zA-Z0-9]+$` | id of the resource proof |

## Request Body (`application/json`)

| Property | Type | Description |
|----------|------|-------------|
| `template_id` | string or null | The template ID to associate with the resource proof. |

## Response (200) - Returns an updated resource proof object

**Content type:** `application/json`

### Response Schema

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | string (res_prf_id) | Yes | Unique identifier prefixed with `res_prf_`. Pattern: `^res_prf_[a-zA-Z0-9]+$` |
| `resource_type` | string (res_prf_resource_type) | Yes | Enum: `"postcard"`, `"letter"`, `"self_mailer"`. The type of resource to generate a proof for. |
| `status` | string (res_prf_status) | Yes | Enum: `"processing"`, `"completed"`, `"failed"`. The processing status of the resource proof. |
| `thumbnails` | Array of objects (thumbnail) | Yes | Thumbnail images of the resource proof. |
| `errors` | Array of objects (issue_entry) | Yes | Errors encountered during processing. |
| `date_created` | string \<date-time\> (date_created) | Yes | A timestamp in ISO 8601 format of the date the resource was created. |
| `date_modified` | string \<date-time\> (date_modified) | Yes | A timestamp in ISO 8601 format of the date the resource was last modified. |
| `object` | string | Yes | Default: `"resource_proof"`. Value is resource type. |
| `template_id` | string or null | No | The template ID associated with the resource proof, if any. |
| `url` | string or null | No | A URL to the resource proof PDF. |

## Request Sample (Payload)

```json
{
  "template_id": "tmpl_a1234dddg"
}
```

## Response Sample (200)

```json
{
  "id": "res_prf_example123",
  "template_id": null,
  "resource_type": "postcard",
  "status": "completed",
  "thumbnails": [
    {
      "small": "https://lob-assets.com/resource-proofs/res_prf_example123_thumb_small_1.png",
      "medium": "https://lob-assets.com/resource-proofs/res_prf_example123_thumb_medium_1.png",
      "large": "https://lob-assets.com/resource-proofs/res_prf_example123_thumb_large_1.png"
    }
  ],
  "url": "https://lob-assets.com/resource-proofs/res_prf_example123.pdf",
  "errors": [],
  "date_created": "2017-11-07T22:56:10.962Z",
  "date_modified": "2017-11-07T22:56:10.962Z",
  "object": "resource_proof"
}
```