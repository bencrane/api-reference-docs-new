# Tag

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
  securitySchemes: {}
servers: []
security: []

```
