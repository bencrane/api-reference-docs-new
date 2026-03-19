# Update

Updates the description and/or published version of the template with the given id. To update the template's html, create a new version of the template.

**AUTHORIZATIONS:** basicAuth

## PATH PARAMETERS

| Parameter | Type | Required | Pattern |
|-----------|------|----------|---------|
| tmpl_id | string (tmpl_id) | required | `^tmpl_[a-zA-Z0-9]+$` |

id of the template

## REQUEST BODY SCHEMA

Content types: `application/json`, `application/x-www-form-urlencoded`, `multipart/form-data`

| Field | Type | Description |
|-------|------|-------------|
| description | string or null (resource_description) <= 255 characters | An internal description that identifies this resource. Must be no longer than 255 characters. |
| published_version | string `^vrsn_[a-zA-Z0-9]+$` | The ID of the published version of a template you'd like to update. The published version is the one that will be used in any Print & Mail API requests that reference the specified template. Will err if the referenced `published_version` has been deleted or does not exist. |

## Responses

**200** Returns the updated template object

### RESPONSE HEADERS

| Header | Type | Description |
|--------|------|-------------|
| ratelimit-limit | integer | Example: `150`. The rate limit for a given endpoint. |
| ratelimit-remaining | integer | Example: `100`. The number of requests remaining in the current window. |
| ratelimit-reset | integer | Example: `1528749846`. The time at which the rate limit window resets in UTC epoch seconds. |

### RESPONSE SCHEMA: application/json

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string (tmpl_id) `^tmpl_[a-zA-Z0-9]+$` | required | Unique identifier prefixed with `tmpl_`. ID of a saved HTML template. |
| versions | Array of objects (template_version) | required | An array of all non-deleted version objects associated with the template. |
| published_version | object (template_version) | required | The template's currently published version. This version will be used in any Print & Mail API requests that reference the specified template. |
| description | string or null (resource_description) <= 255 characters | | An internal description that identifies this resource. Must be no longer than 255 characters. |
| object | string | | Default: `"template"` Value: `"template"`. Value is resource type. |
| metadata | object (metadata) <= 500 characters `[^"\\]{0,500}` | | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. |
| date_created | string \<date-time\> (date_created) | | A timestamp in ISO 8601 format of the date the resource was created. |
| date_modified | string \<date-time\> (date_modified) | | A timestamp in ISO 8601 format of the date the resource was last modified. |
| deleted | boolean (deleted) | | Only returned if the resource has been successfully deleted. |

**default** Error

## Request

```
POST /templates/{tmpl_id}
```

### Request Body Example

```json
{
  "description": "Updated Example",
  "published_version": "vrsn_a"
}
```

## Response Example

**200**

```json
{
  "id": "tmpl_c94e83ca2cd5121",
  "description": "Test Template",
  "versions": [
    {
      "id": "vrsn_362184d96d9b0c9",
      "suggest_json_editor": true,
      "description": "Test Template",
      "engine": "legacy",
      "html": "<html>HTML for {{name}}</html>",
      "date_created": "2017-11-07T22:56:10.962Z",
      "date_modified": "2017-11-07T22:56:10.962Z",
      "object": "version"
    }
  ],
  "published_version": {
    "id": "vrsn_362184d96d9b0c9",
    "suggest_json_editor": false,
    "description": "Test Template",
    "engine": "handlebars",
    "html": "<html>HTML for {{name}}</html>",
    "date_created": "2017-11-07T22:56:10.962Z",
    "date_modified": "2017-11-07T22:56:10.962Z",
    "object": "version"
  },
  "metadata": {},
  "date_created": "2017-11-07T22:56:10.962Z",
  "date_modified": "2017-11-07T22:56:10.962Z",
  "object": "template"
}
```