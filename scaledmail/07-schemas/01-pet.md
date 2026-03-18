# Pet

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths: {}
components:
  schemas:
    Tag:
      type: object
      properties:
        id:
          type: integer
          format: int64
          minimum: 1
          description: Tag ID
        name:
          type: string
          description: Tag Name
      x-apidog-orders:
        - id
        - name
      x-apidog-folder: ''
    Category:
      type: object
      properties:
        id:
          type: integer
          format: int64
          minimum: 1
          description: Category ID
        name:
          type: string
          description: Category Name
      x-apidog-orders:
        - id
        - name
      x-apidog-folder: ''
    Pet:
      required:
        - name
        - photoUrls
        - id
        - category
        - tags
        - status
      type: object
      properties:
        id:
          type: integer
          format: int64
          minimum: 1
          description: Pet ID
        category:
          $ref: '#/components/schemas/Category'
          description: group
        name:
          type: string
          description: name
          examples:
            - doggie
        photoUrls:
          type: array
          items:
            type: string
          description: image URL
        tags:
          type: array
          items:
            $ref: '#/components/schemas/Tag'
          description: tag
        status:
          type: string
          description: Pet Sales Status
          enum:
            - available
            - pending
            - sold
      x-apidog-orders:
        - id
        - category
        - name
        - photoUrls
        - tags
        - status
      x-apidog-folder: ''
  securitySchemes: {}
servers: []
security: []

```