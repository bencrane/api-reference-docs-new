# Delete Tag

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/tags/{tag_id}:
    delete:
      summary: Delete Tag
      deprecated: false
      description: 'Deletes a specific tag by ID.'
      tags:
        - Tags
      parameters:
        - name: tag_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the tag to delete.
          example: 1
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: 'Important was successfully removed'
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
