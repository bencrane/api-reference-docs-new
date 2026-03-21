# Delete Reply Template

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/reply-templates/{reply_template_id}:
    delete:
      summary: Delete Reply Template
      deprecated: false
      description: 'Deletes a specific reply template.'
      tags:
        - Reply Templates
      parameters:
        - name: reply_template_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply template to delete
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
                        example: 'Successfully deleted reply template'
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
