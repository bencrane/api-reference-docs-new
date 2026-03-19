# Create

Creates a new template for use with the Print & Mail API. In Live mode, you can only have as many non-deleted templates as allotted in your current Print & Mail Edition. If you attempt to create a template past your limit, you will receive a 403 error. There is no limit in Test mode.

**AUTHORIZATIONS:** basicAuth

## REQUEST BODY SCHEMA: application/json

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| html | string (template_html) <= 100,000 characters | required | An HTML string of less than 100,000 characters to be used as the published_version of this template. See here for guidance on designing HTML templates. Please see endpoint specific documentation for any other product-specific HTML details: Postcards - front and back, Self Mailers - inside and outside, Letters - file, Checks - check_bottom and attachment, Cards - front and back. If there is a syntax error with your variable names within your HTML, then an error will be thrown, e.g. using a `{{#users}}` opening tag without the corresponding closing tag `{{/users}}`. |
| description | string or null (resource_description) <= 255 characters | | An internal description that identifies this resource. Must be no longer than 255 characters. |
| metadata | object (metadata) <= 500 characters `[^"\\]{0,500}` | | Use metadata to store custom information for tagging and labeling back to your internal systems. Must be an object with up to 20 key-value pairs. Keys must be at most 40 characters and values must be at most 500 characters. Neither can contain the characters `"` and `\`. i.e. `'{"customer_id" : "NEWYORK2015"}'` Nested objects are not supported. |
| engine | string or null (engine) | | Default: `"legacy"` Enum: `"legacy"` `"handlebars"`. The engine used to combine HTML template with merge variables: `legacy` - Lob's original engine, `handlebars`. |
| required_vars | Array of strings (template_required_vars) | | An array of required variables to be used in a template. Only available for handlebars templates. |

## Responses

**200** Returns a template object

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
POST /templates
```

### Request Body Example

```json
{
  "description": "demo",
  "html": "<html>HTML for {{name}}</html>",
  "metadata": {
    "spiffy": "true"
  },
  "engine": "handlebars"
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