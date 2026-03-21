# Attach Scheduled Email to Reply

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/attach-scheduled-email-to-reply:
    post:
      summary: Attach scheduled email to reply
      deprecated: false
      description: >-
        This endpoint attaches a scheduled email to a reply (and lead). You can use this for untracked replies where
        headers may have been missing when the email was received. This will take care of incrementing all stats too.
      tags:
        - Inbox
      parameters:
        - name: reply_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - scheduled_email_id
              properties:
                scheduled_email_id:
                  type: integer
                  description: The ID of the scheduled email.
                  example: 3
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
                        example: 'Scheduled email successfully attached to reply'
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
