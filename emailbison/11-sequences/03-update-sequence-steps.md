# Update Sequence Steps

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/v1.1/sequence-steps/{sequence_id}:
    put:
      summary: Update Sequence Steps
      deprecated: false
      description: 'Updates sequence steps for an existing sequence.'
      tags:
        - Sequences
      parameters:
        - name: sequence_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sequence
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - title
                - sequence_steps
              properties:
                title:
                  type: string
                  description: The title of the sequence
                  example: 'My Outreach Sequence'
                sequence_steps:
                  type: array
                  description: An array of sequence step objects
                  items:
                    type: object
                    required:
                      - id
                      - email_subject
                      - order
                      - email_body
                      - wait_in_days
                    properties:
                      id:
                        type: integer
                        description: The ID of the existing sequence step
                        example: 1
                      email_subject:
                        type: string
                        description: The subject line of the email
                        example: 'Hello {{first_name}}'
                      email_subject_variables:
                        type: array
                        description: Variables used in the email subject
                        items:
                          type: string
                        example:
                          - first_name
                      order:
                        type: integer
                        description: The order of the step in the sequence
                        example: 1
                      email_body:
                        type: string
                        description: The HTML body of the email
                        example: '<p>Hi {{first_name}},</p><p>Just reaching out...</p>'
                      wait_in_days:
                        type: integer
                        description: Number of days to wait before sending this step
                        example: 3
                      variant:
                        type: boolean
                        description: Whether this step is a variant (A/B test)
                        example: false
                      variant_from_step:
                        type: integer
                        description: The order number of the step this variant is based on
                        example: 1
                      variant_from_step_id:
                        type: integer
                        description: The saved step ID of the step this variant is based on
                        example: 10
                      attachments:
                        type: string
                        format: binary
                        description: File attachments for this step
                      thread_reply:
                        type: boolean
                        description: Whether this step should be sent as a thread reply
                        example: false
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
                      id:
                        type: integer
                        example: 1
                      type:
                        type: string
                        example: Campaign sequence
                      title:
                        type: string
                        example: 'My Outreach Sequence'
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
