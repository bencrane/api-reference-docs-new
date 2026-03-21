# Get Email Account Replies

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/{senderEmailId}/replies:
    get:
      summary: Get email account replies
      deprecated: false
      description: This endpoint retrieves all replies associated with a given email account.
      tags:
        - Sender Emails
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Search term for filtering replies.
        - name: status
          in: query
          required: false
          schema:
            type: string
            enum:
              - interested
              - automated_reply
              - not_automated_reply
          description: 'Filter by status. One of `interested`, `automated_reply`, `not_automated_reply`.'
        - name: folder
          in: query
          required: false
          schema:
            type: string
            enum:
              - inbox
              - sent
              - spam
              - bounced
              - all
          description: 'Filter by folder. One of `inbox`, `sent`, `spam`, `bounced`, `all`.'
        - name: read
          in: query
          required: false
          schema:
            type: boolean
          description: Filter by read status.
        - name: campaign_id
          in: query
          required: false
          schema:
            type: integer
          description: The ID of the campaign.
        - name: lead_id
          in: query
          required: false
          schema:
            type: integer
          description: The ID of an existing record in the leads table.
        - name: tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Array of tag IDs to filter by.
        - name: sender_email_id
          in: query
          required: false
          schema:
            type: integer
          description: The ID of the sender email address.
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
                          example: 45
                        uuid:
                          type: string
                          example: '9f7a2718-aa56-43k2-a52b-a44dc183a621'
                        folder:
                          type: string
                          example: Inbox
                        subject:
                          type: string
                          example: 'yo test boy wassup G'
                        read:
                          type: boolean
                          example: true
                        interested:
                          type: boolean
                          example: false
                        automated_reply:
                          type: boolean
                          example: false
                        html_body:
                          type: string
                        text_body:
                          type: string
                        raw_body:
                          type: string
                          nullable: true
                          example: null
                        headers:
                          type: string
                          nullable: true
                          example: null
                        date_received:
                          type: string
                          example: '2024-09-21T02:10:42.000000Z'
                        type:
                          type: string
                          example: 'Untracked Reply'
                        tracked_reply:
                          type: boolean
                          example: false
                        scheduled_email_id:
                          type: integer
                          nullable: true
                          example: null
                        campaign_id:
                          type: integer
                          example: 123
                        lead_id:
                          type: integer
                          nullable: true
                          example: null
                        sender_email_id:
                          type: integer
                          example: 25057
                        from_name:
                          type: string
                          example: 'Cody Smith'
                        from_email_address:
                          type: string
                          example: 'cody@emailguard.io'
                        primary_to_email_address:
                          type: string
                          example: 'usysows3w88c6ljx@eguardtest.com'
                        to:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                              address:
                                type: string
                        cc:
                          type: array
                          nullable: true
                          example: null
                        bcc:
                          type: array
                          nullable: true
                          example: null
                        parent_id:
                          type: integer
                          nullable: true
                          example: null
                        attachments:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: integer
                              uuid:
                                type: string
                              reply_id:
                                type: integer
                              file_name:
                                type: string
                              download_url:
                                type: string
                              created_at:
                                type: string
                              updated_at:
                                type: string
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
