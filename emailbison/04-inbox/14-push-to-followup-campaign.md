# Push to Followup Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/followup-campaign/push:
    post:
      summary: Push reply (and lead) to "reply followup campaign"
      deprecated: false
      description: >-
        This endpoint lets you push a reply to a "reply followup campaign".
        The goal is to followup with interested leads in a templated, automated manner.
        Followups are done in the same conversation thread, and we take the last message from the
        conversation to continue the process.

        Caveats: the reply must have a sender email attached. If you deleted a sender email, then you
        will need to add this lead into a separate outbound campaign since we cannot send an email in the same thread.
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
                - campaign_id
              properties:
                campaign_id:
                  type: integer
                  description: The ID of the followup campaign.
                  example: 9
                force_add_reply:
                  type: boolean
                  description: "Set this to true if you want to ignore the lead's unsubscribed or bounced status."
                  example: false
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
                        example: 'Adding lead to followup campaign. This may take a moment to process.'
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
