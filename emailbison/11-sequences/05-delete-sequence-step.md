# Delete Sequence Step

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/sequence-steps/{sequence_step_id}:
    delete:
      summary: Delete Sequence Step
      deprecated: false
      description: 'Deletes a specific sequence step.'
      tags:
        - Sequences
      parameters:
        - name: sequence_step_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sequence step to delete
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
                        example: 'Sequence step successfully deleted'
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
