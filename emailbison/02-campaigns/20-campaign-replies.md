# Campaign Replies

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/replies:
    get:
      summary: Get campaign replies
      description: This endpoint retrieves all replies associated with a campaign.
      tags:
        - Campaigns
      operationId: getCampaignReplies
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
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
          description: >-
            Filter by status. One of `interested`, `automated_reply`,
            `not_automated_reply`.
        - name: folder
          in: query
          required: false
          schema:
            type: string
          description: >-
            Filter by folder. One of `inbox`, `sent`, `spam`, `bounced`, `all`.
        - name: read
          in: query
          required: false
          schema:
            type: boolean
          description: Filter by read status.
        - name: sender_email_id
          in: query
          required: false
          schema:
            type: integer
          description: The ID of the sender email address.
        - name: lead_id
          in: query
          required: false
          schema:
            type: integer
          description: The id of an existing record in the leads table.
        - name: tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Array of tag IDs to filter by.
        - name: campaign_id
          in: query
          required: false
          schema:
            type: integer
          description: The ID of the campaign.
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
                          example: 9f7a2718-aa56-43k2-a52b-a44dc183a621
                        folder:
                          type: string
                          example: Inbox
                        subject:
                          type: string
                          example: yo test boy wassup G
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
                          example: yo whats good essssssey
                        raw_body:
                          type: string
                          example: null
                        headers:
                          type: string
                          example: null
                        date_received:
                          type: string
                          example: '2024-09-21T02:10:42.000000Z'
                        type:
                          type: string
                          example: Untracked Reply
                        tracked_reply:
                          type: boolean
                          example: false
                        scheduled_email_id:
                          type: integer
                          example: null
                        campaign_id:
                          type: integer
                          example: 123
                        lead_id:
                          type: integer
                          example: null
                        sender_email_id:
                          type: integer
                          example: 25057
                        raw_message_id:
                          type: string
                          example: '<CAHC2zCH-_M2e2PrRNr_DNWHd4WEC-94syh1UAvHc8yPHKxgsPA@mail.gmail.com>'
                        from_name:
                          type: string
                          example: Cody Smith
                        from_email_address:
                          type: string
                          example: cody@emailguard.io
                        primary_to_email_address:
                          type: string
                          example: usysows3w88c6ljx@eguardtest.com
                        to:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                                example: Chimma Tester
                              address:
                                type: string
                                example: usysows3w88c6ljx@eguardtest.com
                        cc:
                          type: string
                          example: null
                        bcc:
                          type: string
                          example: null
                        parent_id:
                          type: integer
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
                                example: 9f7a2718-aa56-43k2-a52b-a44dc183a621
                              reply_id:
                                type: integer
                                example: 45
                              file_name:
                                type: string
                                example: image.png
                              download_url:
                                type: string
                                example: 'http://localhost/reply-attachments/9f2e5a48-5ed6-4021-ae32-66e61908173d/download?signature=5374531e5a71a0c508b75678e53ea48e7d7dae22614bca3703c41cf199e21e67'
                              created_at:
                                type: string
                                example: '2025-06-18T02:38:40.000000Z'
                              updated_at:
                                type: string
                                example: '2025-06-18T02:38:40.000000Z'
              example:
                data:
                  - id: 45
                    uuid: 9f7a2718-aa56-43k2-a52b-a44dc183a621
                    folder: Inbox
                    subject: yo test boy wassup G
                    read: true
                    interested: false
                    automated_reply: false
                    html_body: '<div style="overflow: auto;"><div dir="ltr">yo whats good essssssey</div></div>'
                    text_body: yo whats good essssssey
                    raw_body: null
                    headers: null
                    date_received: '2024-09-21T02:10:42.000000Z'
                    type: Untracked Reply
                    tracked_reply: false
                    scheduled_email_id: null
                    campaign_id: 123
                    lead_id: null
                    sender_email_id: 25057
                    raw_message_id: '<CAHC2zCH-_M2e2PrRNr_DNWHd4WEC-94syh1UAvHc8yPHKxgsPA@mail.gmail.com>'
                    from_name: Cody Smith
                    from_email_address: cody@emailguard.io
                    primary_to_email_address: usysows3w88c6ljx@eguardtest.com
                    to:
                      - name: Chimma Tester
                        address: usysows3w88c6ljx@eguardtest.com
                    cc: null
                    bcc: null
                    parent_id: null
                    attachments:
                      - id: 213
                        uuid: 9f7a2718-aa56-43k2-a52b-a44dc183a621
                        reply_id: 45
                        file_name: image.png
                        download_url: 'http://localhost/reply-attachments/9f2e5a48-5ed6-4021-ae32-66e61908173d/download?signature=5374531e5a71a0c508b75678e53ea48e7d7dae22614bca3703c41cf199e21e67'
                        created_at: '2025-06-18T02:38:40.000000Z'
                        updated_at: '2025-06-18T02:38:40.000000Z'
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
