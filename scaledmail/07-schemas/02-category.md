# Category

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
  securitySchemes: {}
servers: []
security: []

```
