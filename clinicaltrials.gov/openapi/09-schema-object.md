# OpenAPI 3.0.3 -- Schema Object, Discriminator Object, and XML Object

Source: [OpenAPI Specification v3.0.3](https://spec.openapis.org/oas/v3.0.3), Sections 4.7.24, 4.7.25, and 4.7.26.

---

## 4.7.24 Schema Object

The Schema Object allows the definition of input and output data types. These types can be objects, but also primitives and arrays. This object is an extended subset of the JSON Schema Specification Wright Draft 00. For more information about the properties, see JSON Schema Core and JSON Schema Validation. Unless stated otherwise, the property definitions follow the JSON Schema.

Alternatively, any time a Schema Object can be used, a Reference Object can be used in its place. This allows referencing definitions instead of defining them inline.

Additional properties defined by the JSON Schema specification that are not mentioned here are strictly unsupported.

This object MAY be extended with Specification Extensions.

### 4.7.24.1 Properties

The following properties are taken directly from the JSON Schema definition and follow the same specifications:

| Property | Type | Description |
|---|---|---|
| title | string | A title for the schema. |
| multipleOf | number | A numeric instance is valid only if division by this keyword's value results in an integer. Value MUST be strictly greater than 0. |
| maximum | number | An upper limit for a numeric instance. The instance is valid if it is less than or equal to this value. |
| exclusiveMaximum | boolean | If true, the instance is valid if it is strictly less than (not equal to) `maximum`. Default is false. |
| minimum | number | A lower limit for a numeric instance. The instance is valid if it is greater than or equal to this value. |
| exclusiveMinimum | boolean | If true, the instance is valid if it is strictly greater than (not equal to) `minimum`. Default is false. |
| maxLength | integer | The maximum length of a string instance. Value MUST be a non-negative integer. |
| minLength | integer | The minimum length of a string instance. Value MUST be a non-negative integer. Default is 0. |
| pattern | string | A string instance is valid if the regular expression matches the instance successfully. This string SHOULD be a valid regular expression, according to the Ecma-262 Edition 5.1 regular expression dialect. |
| maxItems | integer | The maximum length of an array instance. Value MUST be a non-negative integer. |
| minItems | integer | The minimum length of an array instance. Value MUST be a non-negative integer. Default is 0. |
| uniqueItems | boolean | If true, an array instance is valid if all of its elements are unique. Default is false. |
| maxProperties | integer | The maximum number of properties allowed in an object instance. Value MUST be a non-negative integer. |
| minProperties | integer | The minimum number of properties allowed in an object instance. Value MUST be a non-negative integer. Default is 0. |
| required | [string] | An array of strings. An object instance is valid if it contains all properties listed in this array. Elements of this array MUST be strings and MUST be unique. |
| enum | [any] | An instance validates successfully if its value is equal to one of the elements in this keyword's array value. Elements in the array SHOULD be unique. |

The following properties are taken from the JSON Schema definition but their definitions were adjusted to the OpenAPI Specification:

| Property | Type | Description |
|---|---|---|
| type | string | Value MUST be a string. Multiple types via an array are not supported. |
| allOf | [Schema Object] | Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. |
| oneOf | [Schema Object] | Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. |
| anyOf | [Schema Object] | Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. |
| not | Schema Object | Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. |
| items | Schema Object | Value MUST be an object and not an array. Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. `items` MUST be present if the `type` is `array`. |
| properties | Map[string, Schema Object] | Property definitions MUST be a Schema Object and not a standard JSON Schema (inline or referenced). |
| additionalProperties | boolean \| Schema Object | Value can be boolean or object. Inline or referenced schema MUST be of a Schema Object and not a standard JSON Schema. Consistent with JSON Schema, `additionalProperties` defaults to `true`. |
| description | string | CommonMark syntax MAY be used for rich text representation. |
| format | string | See Data Type Formats for further details. While relying on JSON Schema's defined formats, the OAS offers a few additional predefined formats. |
| default | any | The default value represents what would be assumed by the consumer of the input as the value of the schema if one is not provided. Unlike JSON Schema, the value MUST conform to the defined type for the Schema Object defined at the same level. For example, if `type` is `string`, then `default` can be `"foo"` but cannot be `1`. |

### 4.7.24.2 Fixed Fields

Other than the JSON Schema subset fields, the following fields MAY be used for further schema documentation:

| Field Name | Type | Required? | Description |
|---|---|---|---|
| nullable | boolean | No | A `true` value adds `"null"` to the allowed type specified by the `type` keyword, only if `type` is explicitly defined within the same Schema Object. Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of `null` as a value. A `false` value leaves the specified or default type unmodified. The default value is `false`. |
| discriminator | Discriminator Object | No | Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See Composition and Inheritance for more details. |
| readOnly | boolean | No | Relevant only for Schema `"properties"` definitions. Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as `readOnly` being `true` and is in the `required` list, the required will take effect on the response only. A property MUST NOT be marked as both `readOnly` and `writeOnly` being `true`. Default value is `false`. |
| writeOnly | boolean | No | Relevant only for Schema `"properties"` definitions. Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as `writeOnly` being `true` and is in the `required` list, the required will take effect on the request only. A property MUST NOT be marked as both `readOnly` and `writeOnly` being `true`. Default value is `false`. |
| xml | XML Object | No | This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property. |
| externalDocs | External Documentation Object | No | Additional external documentation for this schema. |
| example | Any | No | A free-form property to include an example of an instance for this schema. To represent examples that cannot be naturally represented in JSON or YAML, a string value can be used to contain the example with escaping where necessary. |
| deprecated | boolean | No | Specifies that a schema is deprecated and SHOULD be transitioned out of usage. Default value is `false`. |

### 4.7.24.2.1 Composition and Inheritance (Polymorphism)

The OpenAPI Specification allows combining and extending model definitions using the `allOf` property of JSON Schema, in effect offering model composition. `allOf` takes an array of object definitions that are validated independently but together compose a single object.

While composition offers model extensibility, it does not imply a hierarchy between the models. To support polymorphism, the OpenAPI Specification adds the `discriminator` field. When used, the discriminator will be the name of the property that decides which schema definition validates the structure of the model. As such, the `discriminator` field MUST be a required field. There are two ways to define the value of a discriminator for an inheriting instance:

1. Use the schema name.
2. Override the schema name by overriding the property with a new value. If a new value exists, this takes precedence over the schema name.

As such, inline schema definitions, which do not have a given id, cannot be used in polymorphism.

### 4.7.24.2.2 XML Modeling

The `xml` property allows extra definitions when translating the JSON definition to XML. The XML Object contains additional information about the available options.

### 4.7.24.3 Schema Object Examples

#### 4.7.24.3.1 Primitive Sample

**JSON:**

```json
{
  "type": "string",
  "format": "email"
}
```

**YAML:**

```yaml
type: string
format: email
```

#### 4.7.24.3.2 Simple Model

**JSON:**

```json
{
  "type": "object",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "type": "string"
    },
    "address": {
      "$ref": "#/components/schemas/Address"
    },
    "age": {
      "type": "integer",
      "format": "int32",
      "minimum": 0
    }
  }
}
```

**YAML:**

```yaml
type: object
required:
- name
properties:
  name:
    type: string
  address:
    $ref: '#/components/schemas/Address'
  age:
    type: integer
    format: int32
    minimum: 0
```

#### 4.7.24.3.3 Model with Map/Dictionary Properties

For a simple string to string mapping:

**JSON:**

```json
{
  "type": "object",
  "additionalProperties": {
    "type": "string"
  }
}
```

**YAML:**

```yaml
type: object
additionalProperties:
  type: string
```

For a string to model mapping:

**JSON:**

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/components/schemas/ComplexModel"
  }
}
```

**YAML:**

```yaml
type: object
additionalProperties:
  $ref: '#/components/schemas/ComplexModel'
```

#### 4.7.24.3.4 Model with Example

**JSON:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "example": {
    "name": "Puma",
    "id": 1
  }
}
```

**YAML:**

```yaml
type: object
properties:
  id:
    type: integer
    format: int64
  name:
    type: string
required:
- name
example:
  name: Puma
  id: 1
```

#### 4.7.24.3.5 Models with Composition

**JSON:**

```json
{
  "components": {
    "schemas": {
      "ErrorModel": {
        "type": "object",
        "required": [
          "message",
          "code"
        ],
        "properties": {
          "message": {
            "type": "string"
          },
          "code": {
            "type": "integer",
            "minimum": 100,
            "maximum": 600
          }
        }
      },
      "ExtendedErrorModel": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ErrorModel"
          },
          {
            "type": "object",
            "required": [
              "rootCause"
            ],
            "properties": {
              "rootCause": {
                "type": "string"
              }
            }
          }
        ]
      }
    }
  }
}
```

**YAML:**

```yaml
components:
  schemas:
    ErrorModel:
      type: object
      required:
      - message
      - code
      properties:
        message:
          type: string
        code:
          type: integer
          minimum: 100
          maximum: 600
    ExtendedErrorModel:
      allOf:
      - $ref: '#/components/schemas/ErrorModel'
      - type: object
        required:
        - rootCause
        properties:
          rootCause:
            type: string
```

#### 4.7.24.3.6 Models with Polymorphism Support

**JSON:**

```json
{
  "components": {
    "schemas": {
      "Pet": {
        "type": "object",
        "discriminator": {
          "propertyName": "petType"
        },
        "properties": {
          "name": {
            "type": "string"
          },
          "petType": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "petType"
        ]
      },
      "Cat": {
        "description": "A representation of a cat. Note that `Cat` will be used as the discriminator value.",
        "allOf": [
          {
            "$ref": "#/components/schemas/Pet"
          },
          {
            "type": "object",
            "properties": {
              "huntingSkill": {
                "type": "string",
                "description": "The measured skill for hunting",
                "default": "lazy",
                "enum": [
                  "clueless",
                  "lazy",
                  "adventurous",
                  "aggressive"
                ]
              }
            },
            "required": [
              "huntingSkill"
            ]
          }
        ]
      },
      "Dog": {
        "description": "A representation of a dog. Note that `Dog` will be used as the discriminator value.",
        "allOf": [
          {
            "$ref": "#/components/schemas/Pet"
          },
          {
            "type": "object",
            "properties": {
              "packSize": {
                "type": "integer",
                "format": "int32",
                "description": "the size of the pack the dog is from",
                "default": 0,
                "minimum": 0
              }
            },
            "required": [
              "packSize"
            ]
          }
        ]
      }
    }
  }
}
```

**YAML:**

```yaml
components:
  schemas:
    Pet:
      type: object
      discriminator:
        propertyName: petType
      properties:
        name:
          type: string
        petType:
          type: string
      required:
      - name
      - petType
    Cat:  ## "Cat" will be used as the discriminator value
      description: A representation of a cat
      allOf:
      - $ref: '#/components/schemas/Pet'
      - type: object
        properties:
          huntingSkill:
            type: string
            description: The measured skill for hunting
            enum:
            - clueless
            - lazy
            - adventurous
            - aggressive
        required:
        - huntingSkill
    Dog:  ## "Dog" will be used as the discriminator value
      description: A representation of a dog
      allOf:
      - $ref: '#/components/schemas/Pet'
      - type: object
        properties:
          packSize:
            type: integer
            format: int32
            description: the size of the pack the dog is from
            default: 0
            minimum: 0
        required:
        - packSize
```

---

## 4.7.25 Discriminator Object

When request bodies or response payloads may be one of a number of different schemas, a discriminator object can be used to aid in serialization, deserialization, and validation. The discriminator is a specific object in a schema which is used to inform the consumer of the specification of an alternative schema based on the value associated with it.

When using the discriminator, inline schemas will not be considered.

### 4.7.25.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| propertyName | string | **Yes** | REQUIRED. The name of the property in the payload that will hold the discriminator value. |
| mapping | Map[string, string] | No | An object to hold mappings between payload values and schema names or references. |

The discriminator object is legal only when using one of the composite keywords `oneOf`, `anyOf`, `allOf`.

### Discriminator Usage Details

In OAS 3.0, a response payload MAY be described to be exactly one of any number of types:

```yaml
MyResponseType:
  oneOf:
  - $ref: '#/components/schemas/Cat'
  - $ref: '#/components/schemas/Dog'
  - $ref: '#/components/schemas/Lizard'
```

which means the payload MUST, by validation, match exactly one of the schemas described by Cat, Dog, or Lizard. In this case, a discriminator MAY act as a "hint" to shortcut validation and selection of the matching schema which may be a costly operation, depending on the complexity of the schema. We can then describe exactly which field tells us which schema to use:

```yaml
MyResponseType:
  oneOf:
  - $ref: '#/components/schemas/Cat'
  - $ref: '#/components/schemas/Dog'
  - $ref: '#/components/schemas/Lizard'
  discriminator:
    propertyName: petType
```

The expectation now is that a property with name `petType` MUST be present in the response payload, and the value will correspond to the name of a schema defined in the OAS document. Thus the response payload:

```json
{
  "id": 12345,
  "petType": "Cat"
}
```

Will indicate that the `Cat` schema be used in conjunction with this payload.

In scenarios where the value of the discriminator field does not match the schema name or implicit mapping is not possible, an optional `mapping` definition MAY be used:

```yaml
MyResponseType:
  oneOf:
  - $ref: '#/components/schemas/Cat'
  - $ref: '#/components/schemas/Dog'
  - $ref: '#/components/schemas/Lizard'
  - $ref: 'https://gigantic-server.com/schemas/Monster/schema.json'
  discriminator:
    propertyName: petType
    mapping:
      dog: '#/components/schemas/Dog'
      monster: 'https://gigantic-server.com/schemas/Monster/schema.json'
```

Here the discriminator value of `dog` will map to the schema `#/components/schemas/Dog`, rather than the default (implicit) value of `Dog`. If the discriminator value does not match an implicit or explicit mapping, no schema can be determined and validation SHOULD fail. Mapping keys MUST be string values, but tooling MAY convert response values to strings for comparison.

When used in conjunction with the `anyOf` construct, the use of the discriminator can avoid ambiguity where multiple schemas may satisfy a single payload.

In both the `oneOf` and `anyOf` use cases, all possible schemas MUST be listed explicitly. To avoid redundancy, the discriminator MAY be added to a parent schema definition, and all schemas comprising the parent schema in an `allOf` construct may be used as an alternate schema.

For example:

```yaml
components:
  schemas:
    Pet:
      type: object
      required:
      - petType
      properties:
        petType:
          type: string
      discriminator:
        propertyName: petType
        mapping:
          dog: Dog
    Cat:
      allOf:
      - $ref: '#/components/schemas/Pet'
      - type: object
        # all other properties specific to a `Cat`
        properties:
          name:
            type: string
    Dog:
      allOf:
      - $ref: '#/components/schemas/Pet'
      - type: object
        # all other properties specific to a `Dog`
        properties:
          bark:
            type: string
    Lizard:
      allOf:
      - $ref: '#/components/schemas/Pet'
      - type: object
        # all other properties specific to a `Lizard`
        properties:
          lovesRocks:
            type: boolean
```

a payload like this:

```json
{
  "petType": "Cat",
  "name": "misty"
}
```

will indicate that the `Cat` schema be used. Likewise this schema:

```json
{
  "petType": "dog",
  "bark": "soft"
}
```

will map to `Dog` because of the definition in the `mappings` element.

---

## 4.7.26 XML Object

A metadata object that allows for more fine-tuned XML model definitions.

When using arrays, XML element names are not inferred (for singular/plural forms) and the `name` property SHOULD be used to add that information. See examples for expected behavior.

### 4.7.26.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| name | string | No | Replaces the name of the element/attribute used for the described schema property. When defined within `items`, it will affect the name of the individual XML elements within the list. When defined alongside `type` being `array` (outside the `items`), it will affect the wrapping element and only if `wrapped` is `true`. If `wrapped` is `false`, it will be ignored. |
| namespace | string | No | The URI of the namespace definition. Value MUST be in the form of an absolute URI. |
| prefix | string | No | The prefix to be used for the name. |
| attribute | boolean | No | Declares whether the property definition translates to an attribute instead of an element. Default value is `false`. |
| wrapped | boolean | No | MAY be used only for an array definition. Signifies whether the array is wrapped (for example, `<books><book/><book/></books>`) or unwrapped (`<book/><book/>`). Default value is `false`. The definition takes effect only when defined alongside `type` being `array` (outside the `items`). |

This object MAY be extended with Specification Extensions.

### 4.7.26.2 XML Object Examples

The examples of the XML object definitions are included inside a property definition of a Schema Object with a sample of the XML representation of it.

#### 4.7.26.2.1 No XML Element

Basic string property:

**JSON:**

```json
{
  "animals": {
    "type": "string"
  }
}
```

**YAML:**

```yaml
animals:
  type: string
```

**XML:**

```xml
<animals>...</animals>
```

Basic string array property (`wrapped` is `false` by default):

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string"
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
```

**XML:**

```xml
<animals>...</animals>
<animals>...</animals>
<animals>...</animals>
```

#### 4.7.26.2.2 XML Name Replacement

**JSON:**

```json
{
  "animals": {
    "type": "string",
    "xml": {
      "name": "animal"
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: string
  xml:
    name: animal
```

**XML:**

```xml
<animal>...</animal>
```

#### 4.7.26.2.3 XML Attribute, Prefix and Namespace

In this example, a full model definition is shown.

**JSON:**

```json
{
  "Person": {
    "type": "object",
    "properties": {
      "id": {
        "type": "integer",
        "format": "int32",
        "xml": {
          "attribute": true
        }
      },
      "name": {
        "type": "string",
        "xml": {
          "namespace": "http://example.com/schema/sample",
          "prefix": "sample"
        }
      }
    }
  }
}
```

**YAML:**

```yaml
Person:
  type: object
  properties:
    id:
      type: integer
      format: int32
      xml:
        attribute: true
    name:
      type: string
      xml:
        namespace: http://example.com/schema/sample
        prefix: sample
```

**XML:**

```xml
<Person id="123">
    <sample:name xmlns:sample="http://example.com/schema/sample">example</sample:name>
</Person>
```

#### 4.7.26.2.4 XML Arrays

**Changing the element names:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string",
      "xml": {
        "name": "animal"
      }
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
    xml:
      name: animal
```

**XML:**

```xml
<animal>value</animal>
<animal>value</animal>
```

**The external `name` property has no effect on the XML:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string",
      "xml": {
        "name": "animal"
      }
    },
    "xml": {
      "name": "aliens"
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
    xml:
      name: animal
  xml:
    name: aliens
```

**XML:**

```xml
<animal>value</animal>
<animal>value</animal>
```

**Even when the array is wrapped, if a name is not explicitly defined, the same name will be used both internally and externally:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "xml": {
      "wrapped": true
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
  xml:
    wrapped: true
```

**XML:**

```xml
<animals>
    <animals>value</animals>
    <animals>value</animals>
</animals>
```

**To overcome the naming problem in the example above, the following definition can be used:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string",
      "xml": {
        "name": "animal"
      }
    },
    "xml": {
      "wrapped": true
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
    xml:
      name: animal
  xml:
    wrapped: true
```

**XML:**

```xml
<animals>
    <animal>value</animal>
    <animal>value</animal>
</animals>
```

**Affecting both internal and external names:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string",
      "xml": {
        "name": "animal"
      }
    },
    "xml": {
      "name": "aliens",
      "wrapped": true
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
    xml:
      name: animal
  xml:
    name: aliens
    wrapped: true
```

**XML:**

```xml
<aliens>
    <animal>value</animal>
    <animal>value</animal>
</aliens>
```

**If we change the external element but not the internal ones:**

**JSON:**

```json
{
  "animals": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "xml": {
      "name": "aliens",
      "wrapped": true
    }
  }
}
```

**YAML:**

```yaml
animals:
  type: array
  items:
    type: string
  xml:
    name: aliens
    wrapped: true
```

**XML:**

```xml
<aliens>
    <aliens>value</aliens>
    <aliens>value</aliens>
</aliens>
```
