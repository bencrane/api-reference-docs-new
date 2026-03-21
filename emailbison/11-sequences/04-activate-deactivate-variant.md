# Activate or Deactivate Variant

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/sequence-steps/{sequence_step_id}/activate-or-deactivate:
    patch:
      summary: Activate or Deactivate Variant
      deprecated: false
      description: 'Activates or deactivates a sequence step variant.'
      tags:
        - Sequences
      parameters:
        - name: sequence_step_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sequence step
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - active
              properties:
                active:
                  type: boolean
                  description: Whether to activate or deactivate the variant
                  example: true
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
                        example: 'Sequence step variant successfully activated.'
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
