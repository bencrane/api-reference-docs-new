# Get Email Account Campaigns

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/{senderEmailId}/campaigns:
    get:
      summary: Show Email Account Campaigns
      deprecated: false
      description: Retrieves a collection of campaigns where this email account is being used.
      tags:
        - Sender Emails
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
      responses:
        '200':
          description: success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                          example: 1
                        uuid:
                          type: string
                          example: '9h8ef374-e986-4221-b432-2902b4826r83'
                        name:
                          type: string
                          example: 'John Doe Campaign'
                        status:
                          type: string
                          example: Active
                        emails_sent:
                          type: integer
                          example: 7
                        opened:
                          type: integer
                          example: 2
                        unique_opens:
                          type: integer
                          example: 1
                        replied:
                          type: integer
                          example: 2
                        unique_replies:
                          type: integer
                          example: 1
                        bounced:
                          type: integer
                          example: 1
                        unsubscribed:
                          type: integer
                          example: 2
                        interested:
                          type: integer
                          example: 3
                        total_leads_contacted:
                          type: integer
                          example: 7
                        max_emails_per_day:
                          type: integer
                          example: 7
                        max_new_leads_per_day:
                          type: integer
                          example: 2
                        plain_text:
                          type: boolean
                          example: true
                        open_tracking:
                          type: boolean
                          example: false
                        can_unsubscribe:
                          type: boolean
                          example: true
                        unsubscribe_text:
                          type: string
                          example: 'Unsubscribe here'
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-05-18T12:53:32.000000Z'
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
