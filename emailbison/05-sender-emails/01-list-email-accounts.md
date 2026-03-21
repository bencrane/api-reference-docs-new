# List Email Accounts

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails:
    get:
      summary: List email accounts
      deprecated: false
      description: Retrieves a collection of email accounts associated with the authenticated workspace.
      tags:
        - Sender Emails
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Search term for filter by.
        - name: tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Array of tag IDs to filter by.
        - name: excluded_tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Exclude email accounts by tag IDs.
        - name: without_tags
          in: query
          required: false
          schema:
            type: boolean
          description: Only show email accounts that have no tags attached.
        - name: status
          in: query
          required: false
          schema:
            type: string
          description: The status of the email account.
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
                        name:
                          type: string
                          example: 'John Doe'
                        email:
                          type: string
                          example: 'john@doe.com'
                        email_signature:
                          type: string
                          example: '<p><strong>John Doe</strong> | Consultant</p>'
                        imap_server:
                          type: string
                          example: 'imap.server'
                        imap_port:
                          type: integer
                          example: 110
                        smtp_server:
                          type: string
                          example: 'smtp.server'
                        smtp_port:
                          type: integer
                          example: 112
                        daily_limit:
                          type: integer
                          example: 5
                        type:
                          type: string
                          example: Inbox
                        status:
                          type: string
                          example: Connected
                        warmup_enabled:
                          type: boolean
                          example: true
                        emails_sent_count:
                          type: integer
                          example: 100
                        total_replied_count:
                          type: integer
                          example: 10
                        total_opened_count:
                          type: integer
                          example: 25
                        unsubscribed_count:
                          type: integer
                          example: 0
                        bounced_count:
                          type: integer
                          example: 0
                        unique_replied_count:
                          type: integer
                          example: 7
                        unique_opened_count:
                          type: integer
                          example: 7
                        total_leads_contacted_count:
                          type: integer
                          example: 50
                        interested_leads_count:
                          type: integer
                          example: 3
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-05-18T12:53:32.000000Z'
                        tags:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: integer
                                example: 1
                              name:
                                type: string
                                example: Google
                              default:
                                type: boolean
                                example: true
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
