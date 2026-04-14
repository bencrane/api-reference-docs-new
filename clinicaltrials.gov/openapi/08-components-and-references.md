# OpenAPI 3.0.3 -- Components Object and Reference Object

Source: [OpenAPI Specification v3.0.3](https://spec.openapis.org/oas/v3.0.3), Sections 4.7.7 and 4.7.23.

---

## 4.7.7 Components Object

Holds a set of reusable objects for different aspects of the OAS. All objects defined within the components object will have no effect on the API unless they are explicitly referenced from properties outside the components object.

### 4.7.7.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| schemas | Map[string, Schema Object \| Reference Object] | No | An object to hold reusable Schema Objects. |
| responses | Map[string, Response Object \| Reference Object] | No | An object to hold reusable Response Objects. |
| parameters | Map[string, Parameter Object \| Reference Object] | No | An object to hold reusable Parameter Objects. |
| examples | Map[string, Example Object \| Reference Object] | No | An object to hold reusable Example Objects. |
| requestBodies | Map[string, Request Body Object \| Reference Object] | No | An object to hold reusable Request Body Objects. |
| headers | Map[string, Header Object \| Reference Object] | No | An object to hold reusable Header Objects. |
| securitySchemes | Map[string, Security Scheme Object \| Reference Object] | No | An object to hold reusable Security Scheme Objects. |
| links | Map[string, Link Object \| Reference Object] | No | An object to hold reusable Link Objects. |
| callbacks | Map[string, Callback Object \| Reference Object] | No | An object to hold reusable Callback Objects. |

This object MAY be extended with Specification Extensions.

### Component Key Regex Pattern

All the fixed fields declared above are objects that MUST use keys that match the regular expression: `^[a-zA-Z0-9\.\-_]+$`.

Field Name Examples:

- `User`
- `User_1`
- `User_Name`
- `user-name`
- `my.org.User`

### 4.7.7.2 Components Object Example

**JSON:**

```json
{
  "components": {
    "schemas": {
      "GeneralError": {
        "type": "object",
        "properties": {
          "code": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string"
          }
        }
      },
      "Category": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string"
          }
        }
      },
      "Tag": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int64"
          },
          "name": {
            "type": "string"
          }
        }
      }
    },
    "parameters": {
      "skipParam": {
        "name": "skip",
        "in": "query",
        "description": "number of items to skip",
        "required": true,
        "schema": {
          "type": "integer",
          "format": "int32"
        }
      },
      "limitParam": {
        "name": "limit",
        "in": "query",
        "description": "max records to return",
        "required": true,
        "schema": {
          "type": "integer",
          "format": "int32"
        }
      }
    },
    "responses": {
      "NotFound": {
        "description": "Entity not found."
      },
      "IllegalInput": {
        "description": "Illegal input for operation."
      },
      "GeneralError": {
        "description": "General Error",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GeneralError"
            }
          }
        }
      }
    },
    "securitySchemes": {
      "api_key": {
        "type": "apiKey",
        "name": "api_key",
        "in": "header"
      },
      "petstore_auth": {
        "type": "oauth2",
        "flows": {
          "implicit": {
            "authorizationUrl": "http://example.org/api/oauth/dialog",
            "scopes": {
              "write:pets": "modify pets in your account",
              "read:pets": "read your pets"
            }
          }
        }
      }
    }
  }
}
```

**YAML:**

```yaml
components:
  schemas:
    GeneralError:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
    Category:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
    Tag:
      type: object
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
  parameters:
    skipParam:
      name: skip
      in: query
      description: number of items to skip
      required: true
      schema:
        type: integer
        format: int32
    limitParam:
      name: limit
      in: query
      description: max records to return
      required: true
      schema:
        type: integer
        format: int32
  responses:
    NotFound:
      description: Entity not found.
    IllegalInput:
      description: Illegal input for operation.
    GeneralError:
      description: General Error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/GeneralError'
  securitySchemes:
    api_key:
      type: apiKey
      name: api_key
      in: header
    petstore_auth:
      type: oauth2
      flows:
        implicit:
          authorizationUrl: http://example.org/api/oauth/dialog
          scopes:
            write:pets: modify pets in your account
            read:pets: read your pets
```

---

## 4.7.23 Reference Object

A simple object to allow referencing other components in the specification, internally and externally.

The Reference Object is defined by JSON Reference and follows the same structure, behavior and rules.

For this specification, reference resolution is accomplished as defined by the JSON Reference specification and not by the JSON Schema specification.

### 4.7.23.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| $ref | string | **Yes** | REQUIRED. The reference string. |

This object cannot be extended with additional properties and any properties added SHALL be ignored.

### 4.7.23.2 Reference Object Example

**JSON:**

```json
{
  "$ref": "#/components/schemas/Pet"
}
```

**YAML:**

```yaml
$ref: '#/components/schemas/Pet'
```

### 4.7.23.3 Relative Schema Document Example

**JSON:**

```json
{
  "$ref": "Pet.json"
}
```

**YAML:**

```yaml
$ref: Pet.yaml
```

### 4.7.23.4 Relative Documents With Embedded Schema Example

**JSON:**

```json
{
  "$ref": "definitions.json#/Pet"
}
```

**YAML:**

```yaml
$ref: definitions.yaml#/Pet
```
