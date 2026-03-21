# Remove Sender Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/remove-sender-emails:
    delete:
      summary: Remove sender emails by ID
      description: >-
        This endpoint allows the authenticated user to remove sender emails from
        a draft or paused campaign.
      tags:
        - Campaigns
      operationId: removeSenderEmailsByID
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - sender_email_ids
              properties:
                sender_email_ids:
                  type: array
                  description: An array of sender emails IDs to attach.
                  example:
                    - 1
                    - 2
                    - 3
                  items:
                    type: string
      responses:
        '200':
          description: success
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  message:
                    type: string
                    example: Sender emails sent for deletion. This may take a moment.
              example:
                success: true
                message: Sender emails sent for deletion. This may take a moment.
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
