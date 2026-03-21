# Mark as Automated or Not Automated

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/replies/{reply_id}/mark-as-automated-or-not-automated:
    patch:
      summary: Mark as automated or not automated
      deprecated: false
      description: >-
        This endpoint marks a specific reply as automated or not automated.

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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - automated
              properties:
                automated:
                  type: boolean
                  description: Whether to mark the reply as automated or not automated.
                  example: true
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
                        example: 239
                      uuid:
                        type: string
                        example: '9f7a2718-aa56-43k2-a52b-a44dc183a621'
                      folder:
                        type: string
                        example: Sent
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
                        example: 238
                      attachments:
                        type: array
                        items:
                          type: object
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
