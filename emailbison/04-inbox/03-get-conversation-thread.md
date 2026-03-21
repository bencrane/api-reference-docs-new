# Get Conversation Thread

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/conversation-thread:
    get:
      summary: Get reply conversation thread
      deprecated: false
      description: >-
        This endpoint gets you a reply object with all previous and newer messages to build out an email thread.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Inbox
      parameters:
        - name: reply_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the reply.
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
                      current_reply:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 239
                          uuid:
                            type: string
                            example: '8d7a2718-aa56-43k2-a52b-a44dc183a621'
                          folder:
                            type: string
                            example: Inbox
                          subject:
                            type: string
                            example: 'Email 3: Lab Cleanup Reminder'
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
                            example: '2024-12-01T03:43:15.000000Z'
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
                            nullable: true
                            example: null
                          lead_id:
                            type: integer
                            nullable: true
                            example: null
                          sender_email_id:
                            type: integer
                            example: 25065
                          raw_message_id:
                            type: string
                          from_name:
                            type: string
                            example: 'Teddy Frank'
                          from_email_address:
                            type: string
                            example: 'teddy.frank@bisonemails.com'
                          primary_to_email_address:
                            type: string
                            example: 'ross.rhea@bisonemails.com'
                          to:
                            type: array
                            items:
                              type: object
                              properties:
                                name:
                                  type: string
                                  example: 'Ross Rhea'
                                address:
                                  type: string
                                  example: 'ross.rhea@bisonemails.com'
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
                            example: 238
                          attachments:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: integer
                                  example: 8
                                uuid:
                                  type: string
                                  example: '9f2e5a48-5ed6-4021-ae32-66e61908173d'
                                reply_id:
                                  type: integer
                                  example: 239
                                file_name:
                                  type: string
                                  example: 'sample.pdf'
                                download_url:
                                  type: string
                                created_at:
                                  type: string
                                  example: '2025-06-18T02:38:40.000000Z'
                                updated_at:
                                  type: string
                                  example: '2025-06-18T02:38:40.000000Z'
                          created_at:
                            type: string
                            example: '2025-06-18T02:38:40.000000Z'
                          updated_at:
                            type: string
                            example: '2025-06-18T02:38:40.000000Z'
                      older_messages:
                        type: array
                        description: Array of reply objects representing older messages in the thread.
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                            uuid:
                              type: string
                            folder:
                              type: string
                            subject:
                              type: string
                            read:
                              type: boolean
                            interested:
                              type: boolean
                            automated_reply:
                              type: boolean
                            html_body:
                              type: string
                            text_body:
                              type: string
                            date_received:
                              type: string
                            type:
                              type: string
                            from_name:
                              type: string
                            from_email_address:
                              type: string
                            primary_to_email_address:
                              type: string
                            parent_id:
                              type: integer
                              nullable: true
                            attachments:
                              type: array
                              items:
                                type: object
                      newer_messages:
                        type: array
                        description: Array of reply objects representing newer messages in the thread.
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                            uuid:
                              type: string
                            folder:
                              type: string
                            subject:
                              type: string
                            read:
                              type: boolean
                            interested:
                              type: boolean
                            automated_reply:
                              type: boolean
                            html_body:
                              type: string
                            text_body:
                              type: string
                            date_received:
                              type: string
                            type:
                              type: string
                            from_name:
                              type: string
                            from_email_address:
                              type: string
                            primary_to_email_address:
                              type: string
                            parent_id:
                              type: integer
                              nullable: true
                            attachments:
                              type: array
                              items:
                                type: object
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
