# Get Lead Replies

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}/replies:
    get:
      summary: Get all replies for lead
      deprecated: false
      description: >-
        This endpoint retrieves all replies for a specific lead.
        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Leads
      parameters:
        - name: lead_id
          in: path
          required: true
          schema:
            type: integer
          description: 'The ID of the lead.'
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: 'Search term for filtering replies.'
        - name: status
          in: query
          required: false
          schema:
            type: string
          description: 'Filter by status. One of `interested`, `automated_reply`, `not_automated_reply`.'
        - name: folder
          in: query
          required: false
          schema:
            type: string
          description: 'Filter by folder. One of `inbox`, `sent`, `spam`, `bounced`, `all`.'
        - name: read
          in: query
          required: false
          schema:
            type: boolean
          description: 'Filter by read status.'
        - name: campaign_id
          in: query
          required: false
          schema:
            type: integer
          description: 'The ID of the campaign.'
        - name: sender_email_id
          in: query
          required: false
          schema:
            type: integer
          description: 'The ID of the sender email address.'
        - name: tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: 'Array of tag IDs to filter by.'
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
                          example: 'Re: Hello'
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
                          example: '<div>Reply content</div>'
                        text_body:
                          type: string
                          example: 'Reply content'
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
                          type: string
                          nullable: true
                          example: null
                        campaign_id:
                          type: string
                          nullable: true
                          example: null
                        lead_id:
                          type: integer
                          example: 990
                        sender_email_id:
                          type: integer
                          example: 25057
                        raw_message_id:
                          type: string
                          example: '<CAHC2zCH-_M2e2PrRNr_DNWHd4WEC@mail.gmail.com>'
                        from_name:
                          type: string
                          example: 'John Doe'
                        from_email_address:
                          type: string
                          example: john@doe.com
                        primary_to_email_address:
                          type: string
                          example: recipient@example.com
                        to:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                                example: 'Recipient Name'
                              address:
                                type: string
                                example: recipient@example.com
                        cc:
                          type: string
                          nullable: true
                          example: null
                        bcc:
                          type: string
                          nullable: true
                          example: null
                        parent_id:
                          type: string
                          nullable: true
                          example: null
                        attachments:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: integer
                                example: 213
                              uuid:
                                type: string
                                example: '9f7a2718-aa56-43k2-a52b-a44dc183a621'
                              reply_id:
                                type: integer
                                example: 45
                              file_name:
                                type: string
                                example: image.png
                              download_url:
                                type: string
                                example: 'https://dedi.emailbison.com/reply-attachments/{uuid}/download'
                              created_at:
                                type: string
                                example: '2025-06-18T02:38:40.000000Z'
                              updated_at:
                                type: string
                                example: '2025-06-18T02:38:40.000000Z'
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
