# OpenAPI Specification v3.0.3 -- Responses and Response Objects

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.16--4.7.17)

---

## 4.7.16 Responses Object

A container for the expected responses of an operation. The container maps a HTTP response code to the expected response.

The documentation is not necessarily expected to cover all possible HTTP response codes because they may not be known in advance. However, documentation is expected to cover a successful operation response and any known errors.

The `default` MAY be used as a default response object for all HTTP codes that are not covered individually by the specification.

The `Responses Object` MUST contain at least one response code, and it SHOULD be the response for a successful operation call.

### 4.7.16.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `default` | [Response Object](#4717-response-object) \| [Reference Object] | No | The documentation of responses other than the ones declared for specific HTTP response codes. Use this field to cover undeclared responses. A Reference Object can link to a response that the OpenAPI Object's `components/responses` section defines. |

### 4.7.16.2 Patterned Fields

| Field Pattern | Type | Required? | Description |
|---|---|---|---|
| [HTTP Status Code] | [Response Object](#4717-response-object) \| [Reference Object] | No | Any HTTP status code can be used as the property name, but only one property per code, to describe the expected response for that HTTP status code. A Reference Object can link to a response that is defined in the OpenAPI Object's `components/responses` section. This field MUST be enclosed in quotation marks (for example, `"200"`) for compatibility between JSON and YAML. To define a range of response codes, this field MAY contain the uppercase wildcard character `X`. For example, `2XX` represents all response codes between `[200-299]`. Only the following range definitions are allowed: `1XX`, `2XX`, `3XX`, `4XX`, and `5XX`. If a response is defined using an explicit code, the explicit code definition takes precedence over the range definition for that code. |

This object MAY be extended with Specification Extensions.

### 4.7.16.3 Responses Object Example

A 200 response for a successful operation and a default response for others (implying an error):

**JSON:**

```json
{
  "200": {
    "description": "a pet to be returned",
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/Pet"
        }
      }
    }
  },
  "default": {
    "description": "Unexpected error",
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ErrorModel"
        }
      }
    }
  }
}
```

**YAML:**

```yaml
'200':
  description: a pet to be returned
  content:
    application/json:
      schema:
        $ref: '#/components/schemas/Pet'
default:
  description: Unexpected error
  content:
    application/json:
      schema:
        $ref: '#/components/schemas/ErrorModel'
```

---

## 4.7.17 Response Object

Describes a single response from an API Operation, including design-time, static `links` to operations based on the response.

### 4.7.17.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `description` | `string` | **REQUIRED** | A short description of the response. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation. |
| `headers` | Map[`string`, [Header Object] \| [Reference Object]] | No | Maps a header name to its definition. [RFC7230](https://tools.ietf.org/html/rfc7230#page-22) states header names are case insensitive. If a response header is defined with the name `"Content-Type"`, it SHALL be ignored. |
| `content` | Map[`string`, [Media Type Object]] | No | A map containing descriptions of potential response payloads. The key is a media type or [media type range](https://tools.ietf.org/html/rfc7231#appendix-D) and the value describes it. For responses that match multiple keys, only the most specific key is applicable. e.g. `text/plain` overrides `text/*` |
| `links` | Map[`string`, [Link Object] \| [Reference Object]] | No | A map of operations links that can be followed from the response. The key of the map is a short name for the link, following the naming constraints of the names for Component Objects. |

This object MAY be extended with Specification Extensions.

### 4.7.17.2 Response Object Examples

Response of an array of a complex type:

**JSON:**

```json
{
  "description": "A complex object array response",
  "content": {
    "application/json": {
      "schema": {
        "type": "array",
        "items": {
          "$ref": "#/components/schemas/VeryComplexType"
        }
      }
    }
  }
}
```

**YAML:**

```yaml
description: A complex object array response
content:
  application/json:
    schema:
      type: array
      items:
        $ref: '#/components/schemas/VeryComplexType'
```

Response with a string type:

**JSON:**

```json
{
  "description": "A simple string response",
  "content": {
    "text/plain": {
      "schema": {
        "type": "string"
      }
    }
  }
}
```

**YAML:**

```yaml
description: A simple string response
content:
  text/plain:
    schema:
      type: string
```

Plain text response with headers:

**JSON:**

```json
{
  "description": "A simple string response",
  "content": {
    "text/plain": {
      "schema": {
        "type": "string",
        "example": "whoa!"
      }
    }
  },
  "headers": {
    "X-Rate-Limit-Limit": {
      "description": "The number of allowed requests in the current period",
      "schema": {
        "type": "integer"
      }
    },
    "X-Rate-Limit-Remaining": {
      "description": "The number of remaining requests in the current period",
      "schema": {
        "type": "integer"
      }
    },
    "X-Rate-Limit-Reset": {
      "description": "The number of seconds left in the current period",
      "schema": {
        "type": "integer"
      }
    }
  }
}
```

**YAML:**

```yaml
description: A simple string response
content:
  text/plain:
    schema:
      type: string
    example: 'whoa!'
headers:
  X-Rate-Limit-Limit:
    description: The number of allowed requests in the current period
    schema:
      type: integer
  X-Rate-Limit-Remaining:
    description: The number of remaining requests in the current period
    schema:
      type: integer
  X-Rate-Limit-Reset:
    description: The number of seconds left in the current period
    schema:
      type: integer
```

Response with no return value:

**JSON:**

```json
{
  "description": "object created"
}
```

**YAML:**

```yaml
description: object created
```
