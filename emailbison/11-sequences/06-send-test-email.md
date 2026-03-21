# Send Test Email

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/sequence-steps/{sequence_step_id}/test-email:
    post:
      summary: Send Test Email
      deprecated: false
      description: 'Sends a test email for a specific sequence step.'
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
                - sender_email_id
                - to_email
              properties:
                sender_email_id:
                  type: integer
                  description: The ID of the sender email to use
                  example: 1
                to_email:
                  type: string
                  description: The recipient email address for the test
                  example: test@example.com
                use_dedicated_ips:
                  type: boolean
                  description: Whether to use dedicated IPs for sending
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: 'Test email sent successfully'
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
