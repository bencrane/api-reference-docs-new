# OpenAPI Specification v3.0.3 -- Supplementary Objects

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.11, 4.7.21, 4.7.22)

---

## 4.7.11 External Documentation Object

Allows referencing an external resource for extended documentation.

### 4.7.11.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `description` | `string` | No | A short description of the target documentation. CommonMark syntax MAY be used for rich text representation. |
| `url` | `string` | **Yes** | The URL for the target documentation. Value MUST be in the format of a URL. |

This object MAY be extended with Specification Extensions.

### 4.7.11.2 External Documentation Object Example

**JSON:**

```json
{
  "description": "Find more info here",
  "url": "https://example.com"
}
```

**YAML:**

```yaml
description: Find more info here
url: https://example.com
```

---

## 4.7.21 Header Object

The Header Object follows the structure of the [Parameter Object](#4712-parameter-object) with the following changes:

1. `name` MUST NOT be specified, it is given in the corresponding `headers` map.
2. `in` MUST NOT be specified, it is implicitly in `header`.
3. All traits that are affected by the location MUST be applicable to a location of `header` (for example, `style`).

Because the Header Object inherits the Parameter Object structure (minus `name` and `in`), the following fixed fields apply:

### Fixed Fields (inherited from Parameter Object, excluding `name` and `in`)

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `description` | `string` | No | A brief description of the header. This could contain examples of use. CommonMark syntax MAY be used for rich text representation. |
| `required` | `boolean` | No | Determines whether this header is mandatory. Default value is `false`. |
| `deprecated` | `boolean` | No | Specifies that a header is deprecated and SHOULD be transitioned out of usage. Default value is `false`. |
| `allowEmptyValue` | `boolean` | No | Sets the ability to pass empty-valued headers. Default value is `false`. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision. |

The rules for serialization of the header are specified in one of two ways. For simpler scenarios, a `schema` and `style` can describe the structure and syntax of the header.

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `style` | `string` | No | Describes how the header value will be serialized. Default value (and only valid value for headers) is `simple`. |
| `explode` | `boolean` | No | When this is true, header values of type `array` or `object` generate separate parameters for each value of the array or key-value pair of the map. For other types of parameters this property has no effect. Default value is `false` (since the only valid style for headers is `simple`). |
| `schema` | Schema Object \| Reference Object | No (but see note) | The schema defining the type used for the header. |
| `example` | Any | No | Example of the header's potential value. The example SHOULD match the specified schema and encoding properties if present. The `example` field is mutually exclusive of the `examples` field. Furthermore, if referencing a `schema` that contains an example, the `example` value SHALL _override_ the example provided by the schema. To represent examples of media types that cannot naturally be represented in JSON or YAML, a string value can contain the example with escaping where necessary. |
| `examples` | Map[`string`, Example Object \| Reference Object] | No | Examples of the header's potential value. Each example SHOULD contain a value in the correct format as specified in the header encoding. The `examples` field is mutually exclusive of the `example` field. Furthermore, if referencing a `schema` that contains an example, the `examples` value SHALL _override_ the example provided by the schema. |

For more complex scenarios, the `content` property can define the media type and schema of the header. A header MUST contain either a `schema` property, or a `content` property, but not both. When `example` or `examples` are provided in conjunction with the `schema` object, the example MUST follow the prescribed serialization strategy for the header.

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `content` | Map[`string`, Media Type Object] | No (but see note) | A map containing the representations for the header. The key is the media type and the value describes it. The map MUST only contain one entry. |

This object MAY be extended with Specification Extensions.

**Key constraints for Header Object vs. Parameter Object:**
- The fields `name` and `in` are NOT used in the Header Object.
- The field `allowReserved` does not apply (it is only for `query` parameters).
- The only valid `style` value for headers is `simple`.
- The default value of `explode` is `false` (since `simple` style defaults to `false`).

### 4.7.21.1 Header Object Example

A simple header of type `integer`:

**JSON:**

```json
{
  "description": "The number of allowed requests in the current period",
  "schema": {
    "type": "integer"
  }
}
```

**YAML:**

```yaml
description: The number of allowed requests in the current period
schema:
  type: integer
```

---

## 4.7.22 Tag Object

Adds metadata to a single tag that is used by the Operation Object. It is not mandatory to have a Tag Object per tag defined in the Operation Object instances.

### 4.7.22.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `name` | `string` | **Yes** | The name of the tag. |
| `description` | `string` | No | A short description for the tag. CommonMark syntax MAY be used for rich text representation. |
| `externalDocs` | External Documentation Object | No | Additional external documentation for this tag. |

This object MAY be extended with Specification Extensions.

### 4.7.22.2 Tag Object Example

**JSON:**

```json
{
  "name": "pet",
  "description": "Pets operations"
}
```

**YAML:**

```yaml
name: pet
description: Pets operations
```
