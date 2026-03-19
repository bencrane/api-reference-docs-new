# Create Upload

Creates a new upload with the provided properties.

**Method:** `POST /uploads`

## Authorization

`basicAuth`

## Request Body Schema

Content type: `application/json`

| Parameter | Type | Required | Description |
|---|---|---|---|
| `campaignId` | string (Campaign id) `^cmp_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `cmp_`. |
| `requiredAddressColumnMapping` | object (Required Address Columns) | No | The mapping of column headers in your file to Lob-required fields for the resource created. See our Campaign Audience Guide for additional details. |
| `optionalAddressColumnMapping` | object (Optional Address Columns) | No | The mapping of column headers in your file to Lob-optional fields for the resource created. See our Campaign Audience Guide for additional details. |
| `metadata` | object (Metadata) | No | Default: `{"columns":[]}`. The list of column headers in your file as an array that you want as metadata associated with each mailpiece. See our Campaign Audience Guide for additional details. |
| `mergeVariableColumnMapping` | object or null (Merge Variable Mapping) | No | Default: `null`. The mapping of column headers in your file to the merge variables present in your creative. See our Campaign Audience Guide for additional details. If a merge variable has the same "name" as a "key" in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects, then they CANNOT have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects. The redirect URLs for QR codes can also be customized using this mapping. If the URL has a variable and the variable mapping exists here, then data from the respective column in the audience file will be merged into the URL template. |

## Responses

### 201 - Upload created successfully

**Response Schema:** `application/json`

| Field | Type | Required | Description |
|---|---|---|---|
| `campaignId` | string (Campaign id) `^cmp_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `cmp_`. |
| `id` | string (upl_id) `^upl_[a-zA-Z0-9]+$` | **Yes** | Unique identifier prefixed with `upl_`. |
| `accountId` | string (Account ID) | **Yes** | Account ID that made the request. |
| `requiredAddressColumnMapping` | object (Required Address Columns) | **Yes** | The mapping of column headers in your file to Lob-required fields for the resource created. See our Campaign Audience Guide for additional details. |
| `optionalAddressColumnMapping` | object (Optional Address Columns) | **Yes** | The mapping of column headers in your file to Lob-optional fields for the resource created. See our Campaign Audience Guide for additional details. |
| `metadata` | object (Metadata) | **Yes** | Default: `{"columns":[]}`. The list of column headers in your file as an array that you want as metadata associated with each mailpiece. See our Campaign Audience Guide for additional details. |
| `mergeVariableColumnMapping` | object or null (Merge Variable Mapping) | **Yes** | Default: `null`. The mapping of column headers in your file to the merge variables present in your creative. See our Campaign Audience Guide for additional details. If a merge variable has the same "name" as a "key" in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects, then they CANNOT have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects. The redirect URLs for QR codes can also be customized using this mapping. If the URL has a variable and the variable mapping exists here, then data from the respective column in the audience file will be merged into the URL template. |
| `mode` | string | **Yes** | Enum: `"test"` `"live"`. The environment in which the mailpieces were created. Today, will only be `live`. |
| `state` | string (Upload State) | **Yes** | Default: `"Draft"`. Enum: `"Preprocessing"` `"Draft"` `"Ready for Validation"` `"Validating"` `"Scheduled"` `"Cancelled"` `"Errored"`. The state property on the upload object. As the file is processed, the state will change from Ready for Validation to Validating and then will be either Scheduled (successfully processed) or Errored (unsuccessfully processed). |
| `totalMailpieces` | integer (Total Mailpieces) | **Yes** | Total number of recipients for the campaign. |
| `failedMailpieces` | integer (Failed Mailpieces) | **Yes** | Number of mailpieces that failed to create. |
| `validatedMailpieces` | integer (Validated Mailpieces) | **Yes** | Number of mailpieces that were successfully created. |
| `bytesProcessed` | integer (Bytes Processed) | **Yes** | Number of bytes processed in your CSV. |
| `dateCreated` | string \<date-time\> (Date Created) | **Yes** | A timestamp in ISO 8601 format of the date the upload was created. |
| `dateModified` | string \<date-time\> (Date Modified) | **Yes** | A timestamp in ISO 8601 format of the date the upload was last modified. |
| `failuresUrl` | string (Failures URL) | No | Url where your campaign mailpiece failures can be retrieved. |
| `originalFilename` | string (Original Filename) | No | Filename of the upload. |

### 422 - Validation Error

## Request Samples

### Payload

```json
{
  "campaignId": "cmp_1933ad629bae1408",
  "requiredAddressColumnMapping": {
    "name": "recipient_name",
    "address_line1": "primary_line",
    "address_city": "city",
    "address_state": "state",
    "address_zip": "zip_code"
  },
  "optionalAddressColumnMapping": {
    "address_line2": "secondary_line",
    "company": "company",
    "address_country": "country"
  },
  "metadata": {
    "columns": [
      "recipient_name"
    ]
  },
  "mergeVariableColumnMapping": {
    "name": "recipient_name",
    "gift_code": "code",
    "qr_code_redirect_url": "redirect_url"
  }
}
```

## Response Samples

### 201

```json
{
  "id": "upl_71be866e430b11e9",
  "accountId": "fa9ea650fc7b31a89f92",
  "campaignId": "cmp_1933ad629bae1408",
  "mode": "live",
  "failuresUrl": "http://www.example.com",
  "originalFilename": "my_audience.csv",
  "state": "Draft",
  "totalMailpieces": 100,
  "failedMailpieces": 5,
  "validatedMailpieces": 95,
  "bytesProcessed": 17628,
  "dateCreated": "2017-09-05T17:47:53.767Z",
  "dateModified": "2017-09-05T17:47:53.767Z",
  "requiredAddressColumnMapping": {
    "name": null,
    "address_line1": null,
    "address_city": null,
    "address_state": null,
    "address_zip": null
  },
  "optionalAddressColumnMapping": {
    "address_line2": null,
    "company": null,
    "address_country": null
  },
  "mergeVariableColumnMapping": null,
  "metadata": {
    "columns": []
  }
}
```