# Bulk Update Email Signatures

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/signatures/bulk:
    patch:
      summary: Bulk update email signatures
      deprecated: false
      description: Update the signatures of multiple sender emails at once.
      tags:
        - Sender Emails
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sender_email_ids
                - email_signature
              properties:
                sender_email_ids:
                  type: array
                  description: An array of sender email IDs to update signatures for.
                  items:
                    type: integer
                  example: [1, 2]
                email_signature:
                  type: string
                  description: The HTML signature to use.
                  example: '<p><strong>{SENDER_FIRST_NAME}</strong> | Consultant</p>'
      responses:
        '200':
          description: success
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
                        example: 'Successfully updated email signatures. This could take a few minutes to process.'
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
