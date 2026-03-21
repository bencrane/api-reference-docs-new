# Attach Sender Emails

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/attach-sender-emails:
    post:
      summary: Import sender emails by ID
      description: >-
        This endpoint allows the authenticated user to attach sender emails to a
        campaign.
      tags:
        - Campaigns
      operationId: importSenderEmailsByID
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
                    example: Sender emails successfully added to Campaign One.
              example:
                success: true
                message: Sender emails successfully added to Campaign One.
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
