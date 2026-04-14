# OpenAPI Specification v3.0.3 -- Paths and Operations

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.8--4.7.10)

---

## 4.7.8 Paths Object

Holds the relative paths to the individual endpoints and their operations. The path is appended to the URL from the Server Object in order to construct the full URL. The Paths MAY be empty, due to ACL constraints.

### 4.7.8.1 Patterned Fields

| Field Pattern | Type | Required? | Description |
|---|---|---|---|
| `/{path}` | [Path Item Object](#479-path-item-object) | No | A relative path to an individual endpoint. The field name MUST begin with a forward slash (`/`). The path is **appended** (no relative URL resolution) to the expanded URL from the Server Object's `url` field in order to construct the full URL. Path templating is allowed. When matching URLs, concrete (non-templated) paths would be matched before their templated counterparts. Templated paths with the same hierarchy but different templated names MUST NOT exist as they are identical. In case of ambiguous matching, it's up to the tooling to decide which one to use. |

This object MAY be extended with Specification Extensions.

### 4.7.8.2 Path Templating Matching

Assuming the following paths, the concrete definition, `/pets/mine`, will be matched first if used:

```
/pets/{petId}
/pets/mine
```

The following paths are considered identical and invalid:

```
/pets/{petId}
/pets/{name}
```

The following may lead to ambiguous resolution:

```
/{entity}/me
/books/{id}
```

### 4.7.8.3 Paths Object Example

**JSON:**

```json
{
  "/pets": {
    "get": {
      "description": "Returns all pets from the system that the user has access to",
      "responses": {
        "200": {
          "description": "A list of pets.",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/pet"
                }
              }
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
/pets:
  get:
    description: Returns all pets from the system that the user has access to
    responses:
      '200':
        description: A list of pets.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/pet'
```

---

## 4.7.9 Path Item Object

Describes the operations available on a single path. A Path Item MAY be empty, due to ACL constraints. The path itself is still exposed to the documentation viewer but they will not know which operations and parameters are available.

### 4.7.9.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `$ref` | `string` | No | Allows for an external definition of this path item. The referenced structure MUST be in the format of a Path Item Object. In case a Path Item Object field appears both in the defined object and the referenced object, the behavior is undefined. |
| `summary` | `string` | No | An optional, string summary, intended to apply to all operations in this path. |
| `description` | `string` | No | An optional, string description, intended to apply to all operations in this path. [CommonMark] syntax MAY be used for rich text representation. |
| `get` | [Operation Object](#4710-operation-object) | No | A definition of a GET operation on this path. |
| `put` | [Operation Object](#4710-operation-object) | No | A definition of a PUT operation on this path. |
| `post` | [Operation Object](#4710-operation-object) | No | A definition of a POST operation on this path. |
| `delete` | [Operation Object](#4710-operation-object) | No | A definition of a DELETE operation on this path. |
| `options` | [Operation Object](#4710-operation-object) | No | A definition of a OPTIONS operation on this path. |
| `head` | [Operation Object](#4710-operation-object) | No | A definition of a HEAD operation on this path. |
| `patch` | [Operation Object](#4710-operation-object) | No | A definition of a PATCH operation on this path. |
| `trace` | [Operation Object](#4710-operation-object) | No | A definition of a TRACE operation on this path. |
| `servers` | [[Server Object]] | No | An alternative `server` array to service all operations in this path. |
| `parameters` | [[Parameter Object] \| [Reference Object]] | No | A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a `name` and `location`. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's `components/parameters`. |

This object MAY be extended with Specification Extensions.

### 4.7.9.2 Path Item Object Example

**JSON:**

```json
{
  "get": {
    "description": "Returns pets based on ID",
    "summary": "Find pets by ID",
    "operationId": "getPetsById",
    "responses": {
      "200": {
        "description": "pet response",
        "content": {
          "*/*": {
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/Pet"
              }
            }
          }
        }
      },
      "default": {
        "description": "error payload",
        "content": {
          "text/html": {
            "schema": {
              "$ref": "#/components/schemas/ErrorModel"
            }
          }
        }
      }
    }
  },
  "parameters": [
    {
      "name": "id",
      "in": "path",
      "description": "ID of pet to use",
      "required": true,
      "schema": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "style": "simple"
    }
  ]
}
```

**YAML:**

```yaml
get:
  description: Returns pets based on ID
  summary: Find pets by ID
  operationId: getPetsById
  responses:
    '200':
      description: pet response
      content:
        '*/*' :
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Pet'
    default:
      description: error payload
      content:
        'text/html':
          schema:
            $ref: '#/components/schemas/ErrorModel'
parameters:
- name: id
  in: path
  description: ID of pet to use
  required: true
  schema:
    type: array
    items:
      type: string
  style: simple
```

---

## 4.7.10 Operation Object

Describes a single API operation on a path.

### 4.7.10.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `tags` | [`string`] | No | A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources or any other qualifier. |
| `summary` | `string` | No | A short summary of what the operation does. |
| `description` | `string` | No | A verbose explanation of the operation behavior. [CommonMark] syntax MAY be used for rich text representation. |
| `externalDocs` | [External Documentation Object] | No | Additional external documentation for this operation. |
| `operationId` | `string` | No | Unique string used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is **case-sensitive**. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions. |
| `parameters` | [[Parameter Object] \| [Reference Object]] | No | A list of parameters that are applicable for this operation. If a parameter is already defined at the Path Item, the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a `name` and `location`. The list can use the Reference Object to link to parameters that are defined at the OpenAPI Object's `components/parameters`. |
| `requestBody` | [Request Body Object] \| [Reference Object] | No | The request body applicable for this operation. The `requestBody` is only supported in HTTP methods where the HTTP 1.1 specification [RFC7231] Section 4.3.1 has explicitly defined semantics for request bodies. In other cases where the HTTP spec is vague, `requestBody` SHALL be ignored by consumers. |
| `responses` | [Responses Object] | **REQUIRED** | The list of possible responses as they are returned from executing this operation. |
| `callbacks` | Map[`string`, [Callback Object] \| [Reference Object]] | No | A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for the Callback Object. Each value in the map is a Callback Object that describes a request that may be initiated by the API provider and the expected responses. |
| `deprecated` | `boolean` | No | Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. Default value is `false`. |
| `security` | [[Security Requirement Object]] | No | A declaration of which security mechanisms can be used for this operation. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement (`{}`) can be included in the array. This definition overrides any declared top-level `security`. To remove a top-level security declaration, an empty array can be used. |
| `servers` | [[Server Object]] | No | An alternative `server` array to service this operation. If an alternative `server` object is specified at the Path Item Object or Root level, it will be overridden by this value. |

This object MAY be extended with Specification Extensions.

### 4.7.10.2 Operation Object Example

**JSON:**

```json
{
  "tags": [
    "pet"
  ],
  "summary": "Updates a pet in the store with form data",
  "operationId": "updatePetWithForm",
  "parameters": [
    {
      "name": "petId",
      "in": "path",
      "description": "ID of pet that needs to be updated",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "requestBody": {
    "content": {
      "application/x-www-form-urlencoded": {
        "schema": {
          "type": "object",
          "properties": {
            "name": {
              "description": "Updated name of the pet",
              "type": "string"
            },
            "status": {
              "description": "Updated status of the pet",
              "type": "string"
            }
          },
          "required": ["status"]
        }
      }
    }
  },
  "responses": {
    "200": {
      "description": "Pet updated.",
      "content": {
        "application/json": {},
        "application/xml": {}
      }
    },
    "405": {
      "description": "Method Not Allowed",
      "content": {
        "application/json": {},
        "application/xml": {}
      }
    }
  },
  "security": [
    {
      "petstore_auth": [
        "write:pets",
        "read:pets"
      ]
    }
  ]
}
```

**YAML:**

```yaml
tags:
- pet
summary: Updates a pet in the store with form data
operationId: updatePetWithForm
parameters:
- name: petId
  in: path
  description: ID of pet that needs to be updated
  required: true
  schema:
    type: string
requestBody:
  content:
    'application/x-www-form-urlencoded':
      schema:
       properties:
          name:
            description: Updated name of the pet
            type: string
          status:
            description: Updated status of the pet
            type: string
       required:
         - status
responses:
  '200':
    description: Pet updated.
    content:
      'application/json': {}
      'application/xml': {}
  '405':
    description: Method Not Allowed
    content:
      'application/json': {}
      'application/xml': {}
security:
- petstore_auth:
  - write:pets
  - read:pets
```
