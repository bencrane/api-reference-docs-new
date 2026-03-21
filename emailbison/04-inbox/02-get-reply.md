# Get Reply

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{id}:
    get:
      summary: Get reply
      deprecated: false
      description: >-
        This endpoint retrieves a specific reply by its ID.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Inbox
      parameters:
        - name: id
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
                        example: '<div style="overflow: auto;"><div dir="ltr">yo whats good essssssey</div></div>'
                      text_body:
                        type: string
                        example: 'yo whats good essssssey'
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
                        nullable: true
                        example: null
                      lead_id:
                        type: integer
                        nullable: true
                        example: null
                      sender_email_id:
                        type: integer
                        example: 25057
                      raw_message_id:
                        type: string
                        example: '<CAHC2zCH-_M2e2PrRNr_DNWHd4WEC-94syh1UAvHc8yPHKxgsPA@mail.gmail.com>'
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
                              example: 'Chimma Tester'
                            address:
                              type: string
                              example: 'usysows3w88c6ljx@eguardtest.com'
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
                              example: 8
                            uuid:
                              type: string
                              example: '9f2e5a48-5ed6-4021-ae32-66e61908173d'
                            reply_id:
                              type: integer
                              example: 45
                            file_name:
                              type: string
                              example: 'sample.pdf'
                            download_url:
                              type: string
                              example: 'https://dedi.emailbison.com/reply-attachments/9f2e5a48-5ed6-4021-ae32-66e61908173d/download'
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
