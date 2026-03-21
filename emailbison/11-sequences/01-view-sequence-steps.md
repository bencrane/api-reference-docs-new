# View Sequence Steps

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/v1.1/{campaign_id}/sequence-steps:
    get:
      summary: View Sequence Steps
      deprecated: false
      description: 'Retrieves all sequence steps for a specific campaign.'
      tags:
        - Sequences
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign
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
                      sequence_id:
                        type: integer
                        example: 1
                      sequence_steps:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            email_subject:
                              type: string
                              example: 'Hello {{first_name}}'
                            order:
                              type: integer
                              example: 1
                            email_body:
                              type: string
                              example: '<p>Hi {{first_name}},</p><p>Just reaching out...</p>'
                            wait_in_days:
                              type: integer
                              example: 3
                            variant:
                              type: boolean
                              example: false
                            variant_from_step_id:
                              type: integer
                              nullable: true
                              example: null
                            attachments:
                              type: array
                              items:
                                type: object
                              example: []
                            thread_reply:
                              type: boolean
                              example: false
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
