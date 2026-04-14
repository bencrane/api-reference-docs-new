# OpenAPI Specification v3.0.3 -- Request Body and Media Types

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.13--4.7.15)

---

## 4.7.13 Request Body Object

Describes a single request body.

### 4.7.13.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `description` | `string` | No | A brief description of the request body. This could contain examples of use. CommonMark syntax MAY be used for rich text representation. |
| `content` | Map[`string`, Media Type Object] | **Yes** | The content of the request body. The key is a media type or media type range, see [RFC7231] Appendix D, and the value describes it. For requests that match multiple keys, only the most specific key is applicable. e.g. `text/plain` overrides `text/*`. |
| `required` | `boolean` | No | Determines if the request body is required in the request. Defaults to `false`. |

This object MAY be extended with Specification Extensions.

### 4.7.13.2 Request Body Examples

**A request body with a referenced model definition.**

JSON:

```json
{
  "description": "user to add to the system",
  "content": {
    "application/json": {
      "schema": {
        "$ref": "#/components/schemas/User"
      },
      "examples": {
          "user" : {
            "summary": "User Example",
            "externalValue": "http://foo.bar/examples/user-example.json"
          }
        }
    },
    "application/xml": {
      "schema": {
        "$ref": "#/components/schemas/User"
      },
      "examples": {
          "user" : {
            "summary": "User example in XML",
            "externalValue": "http://foo.bar/examples/user-example.xml"
          }
        }
    },
    "text/plain": {
      "examples": {
        "user" : {
            "summary": "User example in Plain text",
            "externalValue": "http://foo.bar/examples/user-example.txt"
        }
      }
    },
    "*/*": {
      "examples": {
        "user" : {
            "summary": "User example in other format",
            "externalValue": "http://foo.bar/examples/user-example.whatever"
        }
      }
    }
  }
}
```

YAML:

```yaml
description: user to add to the system
content:
  'application/json':
    schema:
      $ref: '#/components/schemas/User'
    examples:
      user:
        summary: User Example
        externalValue: 'http://foo.bar/examples/user-example.json'
  'application/xml':
    schema:
      $ref: '#/components/schemas/User'
    examples:
      user:
        summary: User Example in XML
        externalValue: 'http://foo.bar/examples/user-example.xml'
  'text/plain':
    examples:
      user:
        summary: User example in text plain format
        externalValue: 'http://foo.bar/examples/user-example.txt'
  '*/*':
    examples:
      user:
        summary: User example in other format
        externalValue: 'http://foo.bar/examples/user-example.whatever'
```

**A body parameter that is an array of string values:**

JSON:

```json
{
  "description": "user to add to the system",
  "content": {
    "text/plain": {
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

YAML:

```yaml
description: user to add to the system
required: true
content:
  text/plain:
    schema:
      type: array
      items:
        type: string
```

---

## 4.7.14 Media Type Object

Each Media Type Object provides schema and examples for the media type identified by its key.

### 4.7.14.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `schema` | Schema Object \| Reference Object | No | The schema defining the content of the request, response, or parameter. |
| `example` | Any | No | Example of the media type. The example object SHOULD be in the correct format as specified by the media type. The `example` field is mutually exclusive of the `examples` field. Furthermore, if referencing a `schema` which contains an example, the `example` value SHALL _override_ the example provided by the schema. |
| `examples` | Map[`string`, Example Object \| Reference Object] | No | Examples of the media type. Each example object SHOULD match the media type and specified schema if present. The `examples` field is mutually exclusive of the `example` field. Furthermore, if referencing a `schema` which contains an example, the `examples` value SHALL _override_ the example provided by the schema. |
| `encoding` | Map[`string`, Encoding Object] | No | A map between a property name and its encoding information. The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to `requestBody` objects when the media type is `multipart` or `application/x-www-form-urlencoded`. |

This object MAY be extended with Specification Extensions.

### 4.7.14.2 Media Type Examples

JSON:

```json
{
  "application/json": {
    "schema": {
         "$ref": "#/components/schemas/Pet"
    },
    "examples": {
      "cat" : {
        "summary": "An example of a cat",
        "value":
          {
            "name": "Fluffy",
            "petType": "Cat",
            "color": "White",
            "gender": "male",
            "breed": "Persian"
          }
      },
      "dog": {
        "summary": "An example of a dog with a cat's name",
        "value" :  {
          "name": "Puma",
          "petType": "Dog",
          "color": "Black",
          "gender": "Female",
          "breed": "Mixed"
        },
      "frog": {
          "$ref": "#/components/examples/frog-example"
        }
      }
    }
  }
}
```

YAML:

```yaml
application/json:
  schema:
    $ref: "#/components/schemas/Pet"
  examples:
    cat:
      summary: An example of a cat
      value:
        name: Fluffy
        petType: Cat
        color: White
        gender: male
        breed: Persian
    dog:
      summary: An example of a dog with a cat's name
      value:
        name: Puma
        petType: Dog
        color: Black
        gender: Female
        breed: Mixed
    frog:
      $ref: "#/components/examples/frog-example"
```

### 4.7.14.3 Considerations for File Uploads

In contrast with the 2.0 specification, `file` input/output content in OpenAPI is described with the same semantics as any other schema type. Specifically:

```yaml
# content transferred with base64 encoding
schema:
  type: string
  format: base64
```

```yaml
# content transferred in binary (octet-stream):
schema:
  type: string
  format: binary
```

These examples apply to either input payloads of file uploads or response payloads.

A `requestBody` for submitting a file in a `POST` operation may look like the following example:

```yaml
requestBody:
  content:
    application/octet-stream:
      schema:
        # a binary file of any type
        type: string
        format: binary
```

In addition, specific media types MAY be specified:

```yaml
# multiple, specific media types may be specified:
requestBody:
  content:
      # a binary file of type png or jpeg
    'image/jpeg':
      schema:
        type: string
        format: binary
    'image/png':
      schema:
        type: string
        format: binary
```

To upload multiple files, a `multipart` media type MUST be used:

```yaml
requestBody:
  content:
    multipart/form-data:
      schema:
        properties:
          # The property name 'file' will be used for all files.
          file:
            type: array
            items:
              type: string
              format: binary
```

### 4.7.14.4 Support for x-www-form-urlencoded Request Bodies

To submit content using form url encoding via [RFC1866], the following definition may be used:

```yaml
requestBody:
  content:
    application/x-www-form-urlencoded:
      schema:
        type: object
        properties:
          id:
            type: string
            format: uuid
          address:
            # complex types are stringified to support RFC 1866
            type: object
            properties: {}
```

In this example, the contents in the `requestBody` MUST be stringified per [RFC1866] when passed to the server. In addition, the `address` field complex object will be stringified.

When passing complex objects in the `application/x-www-form-urlencoded` content type, the default serialization strategy of such properties is described in the Encoding Object's `style` property as `form`.

### 4.7.14.5 Special Considerations for multipart Content

It is common to use `multipart/form-data` as a `Content-Type` when transferring request bodies to operations. In contrast to 2.0, a `schema` is REQUIRED to define the input parameters to the operation when using `multipart` content. This supports complex structures as well as supporting mechanisms for multiple file uploads.

When passing in `multipart` types, boundaries MAY be used to separate sections of the content being transferred. Thus, the following default `Content-Type`s are defined for `multipart`:

- If the property is a primitive, or an array of primitive values, the default Content-Type is `text/plain`
- If the property is complex, or an array of complex values, the default Content-Type is `application/json`
- If the property is a `type: string` with `format: binary` or `format: base64` (aka a file object), the default Content-Type is `application/octet-stream`

Examples:

```yaml
requestBody:
  content:
    multipart/form-data:
      schema:
        type: object
        properties:
          id:
            type: string
            format: uuid
          address:
            # default Content-Type for objects is `application/json`
            type: object
            properties: {}
          profileImage:
            # default Content-Type for string/binary is `application/octet-stream`
            type: string
            format: binary
          children:
            # default Content-Type for arrays is based on the `inner` type (text/plain here)
            type: array
            items:
              type: string
          addresses:
            # default Content-Type for arrays is based on the `inner` type (object shown, so `application/json` in this example)
            type: array
            items:
              type: '#/components/schemas/Address'
```

An `encoding` attribute is introduced to give you control over the serialization of parts of `multipart` request bodies. This attribute is only applicable to `multipart` and `application/x-www-form-urlencoded` request bodies.

---

## 4.7.15 Encoding Object

A single encoding definition applied to a single schema property.

### 4.7.15.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `contentType` | `string` | No | The Content-Type for encoding a specific property. Default value depends on the property type: for `string` with `format` being `binary` -- `application/octet-stream`; for other primitive types -- `text/plain`; for `object` -- `application/json`; for `array` -- the default is defined based on the inner type. The value can be a specific media type (e.g. `application/json`), a wildcard media type (e.g. `image/*`), or a comma-separated list of the two types. |
| `headers` | Map[`string`, Header Object \| Reference Object] | No | A map allowing additional information to be provided as headers, for example `Content-Disposition`. `Content-Type` is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a `multipart`. |
| `style` | `string` | No | Describes how a specific property value will be serialized depending on its type. See Parameter Object for details on the `style` property. The behavior follows the same values as `query` parameters, including default values. This property SHALL be ignored if the request body media type is not `application/x-www-form-urlencoded`. |
| `explode` | `boolean` | No | When this is true, property values of type `array` or `object` generate separate parameters for each value of the array, or key-value-pair of the map. For other types of properties this property has no effect. When `style` is `form`, the default value is `true`. For all other styles, the default value is `false`. This property SHALL be ignored if the request body media type is not `application/x-www-form-urlencoded`. |
| `allowReserved` | `boolean` | No | Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986] Section 2.2 `:/?#[]@!$&'()*+,;=` to be included without percent-encoding. The default value is `false`. This property SHALL be ignored if the request body media type is not `application/x-www-form-urlencoded`. |

This object MAY be extended with Specification Extensions.

### 4.7.15.2 Encoding Object Example

```yaml
requestBody:
  content:
    multipart/mixed:
      schema:
        type: object
        properties:
          id:
            # default is text/plain
            type: string
            format: uuid
          address:
            # default is application/json
            type: object
            properties: {}
          historyMetadata:
            # need to declare XML format!
            description: metadata in XML format
            type: object
            properties: {}
          profileImage:
            # default is application/octet-stream, need to declare an image type only!
            type: string
            format: binary
      encoding:
        historyMetadata:
          # require XML Content-Type in utf-8 encoding
          contentType: application/xml; charset=utf-8
        profileImage:
          # only accept png/jpeg
          contentType: image/png, image/jpeg
          headers:
            X-Rate-Limit-Limit:
              description: The number of allowed requests in the current period
              schema:
                type: integer
```
