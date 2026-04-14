# OpenAPI Specification v3.0.3 -- Parameters

Source: https://spec.openapis.org/oas/v3.0.3.html (Section 4.7.12)

---

## 4.7.12 Parameter Object

Describes a single operation parameter.

A unique parameter is defined by a combination of a [name](#parameterName) and [location](#parameterIn).

### 4.7.12.1 Parameter Locations

There are four possible parameter locations specified by the `in` field:

- **path** -- Used together with Path Templating, where the parameter value is actually part of the operation's URL. This does not include the host or base path of the API. For example, in `/items/{itemId}`, the path parameter is `itemId`.
- **query** -- Parameters that are appended to the URL. For example, in `/items?id=###`, the query parameter is `id`.
- **header** -- Custom headers that are expected as part of the request. Note that [RFC7230] Page 22 states header names are case insensitive.
- **cookie** -- Used to pass a specific cookie value to the API.

### 4.7.12.2 Fixed Fields

The following fixed fields define the parameter identity and basic metadata:

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `name` | `string` | **Yes** | The name of the parameter. Parameter names are _case sensitive_. If `in` is `"path"`, the `name` field MUST correspond to a template expression occurring within the path field in the Paths Object. See Path Templating for further information. If `in` is `"header"` and the `name` field is `"Accept"`, `"Content-Type"` or `"Authorization"`, the parameter definition SHALL be ignored. For all other cases, the `name` corresponds to the parameter name used by the `in` property. |
| `in` | `string` | **Yes** | The location of the parameter. Possible values are `"query"`, `"header"`, `"path"` or `"cookie"`. |
| `description` | `string` | No | A brief description of the parameter. This could contain examples of use. CommonMark syntax MAY be used for rich text representation. |
| `required` | `boolean` | No (but see note) | Determines whether this parameter is mandatory. If the parameter location is `"path"`, this property is **REQUIRED** and its value MUST be `true`. Otherwise, the property MAY be included and its default value is `false`. |
| `deprecated` | `boolean` | No | Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is `false`. |
| `allowEmptyValue` | `boolean` | No | Sets the ability to pass empty-valued parameters. This is valid only for `query` parameters and allows sending a parameter with an empty value. Default value is `false`. If `style` is used, and if behavior is `n/a` (cannot be serialized), the value of `allowEmptyValue` SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision. |

The rules for serialization of the parameter are specified in one of two ways. For simpler scenarios, a `schema` and `style` can describe the structure and syntax of the parameter.

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `style` | `string` | No | Describes how the parameter value will be serialized depending on the type of the parameter value. Default values (based on value of `in`): for `query` -- `form`; for `path` -- `simple`; for `header` -- `simple`; for `cookie` -- `form`. |
| `explode` | `boolean` | No | When this is true, parameter values of type `array` or `object` generate separate parameters for each value of the array or key-value pair of the map. For other types of parameters this property has no effect. When `style` is `form`, the default value is `true`. For all other styles, the default value is `false`. |
| `allowReserved` | `boolean` | No | Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986] Section 2.2 `:/?#[]@!$&'()*+,;=` to be included without percent-encoding. This property only applies to parameters with an `in` value of `query`. The default value is `false`. |
| `schema` | Schema Object \| Reference Object | No (but see note) | The schema defining the type used for the parameter. |
| `example` | Any | No | Example of the parameter's potential value. The example SHOULD match the specified schema and encoding properties if present. The `example` field is mutually exclusive of the `examples` field. Furthermore, if referencing a `schema` that contains an example, the `example` value SHALL _override_ the example provided by the schema. To represent examples of media types that cannot naturally be represented in JSON or YAML, a string value can contain the example with escaping where necessary. |
| `examples` | Map[`string`, Example Object \| Reference Object] | No | Examples of the parameter's potential value. Each example SHOULD contain a value in the correct format as specified in the parameter encoding. The `examples` field is mutually exclusive of the `example` field. Furthermore, if referencing a `schema` that contains an example, the `examples` value SHALL _override_ the example provided by the schema. |

For more complex scenarios, the `content` property can define the media type and schema of the parameter. A parameter MUST contain either a `schema` property, or a `content` property, but not both. When `example` or `examples` are provided in conjunction with the `schema` object, the example MUST follow the prescribed serialization strategy for the parameter.

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `content` | Map[`string`, Media Type Object] | No (but see note) | A map containing the representations for the parameter. The key is the media type and the value describes it. The map MUST only contain one entry. |

This object MAY be extended with Specification Extensions.

### 4.7.12.3 Style Values

In order to support common ways of serializing simple parameters, a set of `style` values are defined.

| `style` | `type` | `in` | Comments |
|---|---|---|---|
| `matrix` | `primitive`, `array`, `object` | `path` | Path-style parameters defined by [RFC6570] Section 3.2.7 |
| `label` | `primitive`, `array`, `object` | `path` | Label style parameters defined by [RFC6570] Section 3.2.5 |
| `form` | `primitive`, `array`, `object` | `query`, `cookie` | Form style parameters defined by [RFC6570] Section 3.2.8. This option replaces `collectionFormat` with a `csv` (when `explode` is false) or `multi` (when `explode` is true) value from OpenAPI 2.0. |
| `simple` | `array` | `path`, `header` | Simple style parameters defined by [RFC6570] Section 3.2.2. This option replaces `collectionFormat` with a `csv` value from OpenAPI 2.0. |
| `spaceDelimited` | `array` | `query` | Space separated array values. This option replaces `collectionFormat` equal to `ssv` from OpenAPI 2.0. |
| `pipeDelimited` | `array` | `query` | Pipe separated array values. This option replaces `collectionFormat` equal to `pipes` from OpenAPI 2.0. |
| `deepObject` | `object` | `query` | Provides a simple way of rendering nested objects using form parameters. |

### 4.7.12.4 Style Examples

Assume a parameter named `color` has one of the following values:

```
string -> "blue"
array -> ["blue","black","brown"]
object -> { "R": 100, "G": 200, "B": 150 }
```

The following table shows examples of rendering differences for each value.

| `style` | `explode` | `empty` | `string` | `array` | `object` |
|---|---|---|---|---|---|
| matrix | false | `;color` | `;color=blue` | `;color=blue,black,brown` | `;color=R,100,G,200,B,150` |
| matrix | true | `;color` | `;color=blue` | `;color=blue;color=black;color=brown` | `;R=100;G=200;B=150` |
| label | false | `.` | `.blue` | `.blue.black.brown` | `.R.100.G.200.B.150` |
| label | true | `.` | `.blue` | `.blue.black.brown` | `.R=100.G=200.B=150` |
| form | false | `color=` | `color=blue` | `color=blue,black,brown` | `color=R,100,G,200,B,150` |
| form | true | `color=` | `color=blue` | `color=blue&color=black&color=brown` | `R=100&G=200&B=150` |
| simple | false | n/a | `blue` | `blue,black,brown` | `R,100,G,200,B,150` |
| simple | true | n/a | `blue` | `blue,black,brown` | `R=100,G=200,B=150` |
| spaceDelimited | false | n/a | n/a | `blue%20black%20brown` | `R%20100%20G%20200%20B%20150` |
| pipeDelimited | false | n/a | n/a | `blue\|black\|brown` | `R\|100\|G\|200\|B\|150` |
| deepObject | true | n/a | n/a | n/a | `color[R]=100&color[G]=200&color[B]=150` |

### 4.7.12.5 Parameter Object Examples

**A header parameter with an array of 64 bit integer numbers:**

JSON:

```json
{
  "name": "token",
  "in": "header",
  "description": "token to be passed as a header",
  "required": true,
  "schema": {
    "type": "array",
    "items": {
      "type": "integer",
      "format": "int64"
    }
  },
  "style": "simple"
}
```

YAML:

```yaml
name: token
in: header
description: token to be passed as a header
required: true
schema:
  type: array
  items:
    type: integer
    format: int64
style: simple
```

**A path parameter of a string value:**

JSON:

```json
{
  "name": "username",
  "in": "path",
  "description": "username to fetch",
  "required": true,
  "schema": {
    "type": "string"
  }
}
```

YAML:

```yaml
name: username
in: path
description: username to fetch
required: true
schema:
  type: string
```

**An optional query parameter of a string value, allowing multiple values by repeating the query parameter:**

JSON:

```json
{
  "name": "id",
  "in": "query",
  "description": "ID of the object to fetch",
  "required": false,
  "schema": {
    "type": "array",
    "items": {
      "type": "string"
    }
  },
  "style": "form",
  "explode": true
}
```

YAML:

```yaml
name: id
in: query
description: ID of the object to fetch
required: false
schema:
  type: array
  items:
    type: string
style: form
explode: true
```

**A free-form query parameter, allowing undefined parameters of a specific type:**

JSON:

```json
{
  "in": "query",
  "name": "freeForm",
  "schema": {
    "type": "object",
    "additionalProperties": {
      "type": "integer"
    }
  },
  "style": "form"
}
```

YAML:

```yaml
in: query
name: freeForm
schema:
  type: object
  additionalProperties:
    type: integer
style: form
```

**A complex parameter using `content` to define serialization:**

JSON:

```json
{
  "in": "query",
  "name": "coordinates",
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "required": [
          "lat",
          "long"
        ],
        "properties": {
          "lat": {
            "type": "number"
          },
          "long": {
            "type": "number"
          }
        }
      }
    }
  }
}
```

YAML:

```yaml
in: query
name: coordinates
content:
  application/json:
    schema:
      type: object
      required:
        - lat
        - long
      properties:
        lat:
          type: number
        long:
          type: number
```
