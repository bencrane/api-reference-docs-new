# Get All Tags

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/tags:
    get:
      summary: Get All Tags
      deprecated: false
      description: 'Returns a list of all tags in the workspace.'
      tags:
        - Tags
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        name:
                          type: string
                          example: 'Important'
                        default:
                          type: boolean
                          example: false
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-05-18T12:53:32.000000Z'
          headers: {}
      security:
        - bearer: []
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://dedi.emailbison.com
security:
  - bearer: []
```
