# Create Reply Template

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/reply-templates:
    post:
      summary: Create Reply Template
      deprecated: false
      description: 'Creates a new reply template. Attachments have a combined maximum size of 25MB, with each individual file limited to 10MB.'
      tags:
        - Reply Templates
      parameters: []
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - name
                - body
              properties:
                name:
                  type: string
                  description: The name of the reply template
                  example: 'Follow-up Template'
                body:
                  type: string
                  description: The HTML body of the reply template
                  example: '<p>Thank you for your reply.</p>'
                attachments:
                  type: array
                  description: 'File attachments (combined max 25MB, individual max 10MB)'
                  items:
                    type: string
                    format: binary
      responses:
        '200':
          description: ''
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
                        example: 1
                      uuid:
                        type: string
                        example: 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
                      user_id:
                        type: integer
                        example: 1
                      name:
                        type: string
                        example: 'Follow-up Template'
                      body:
                        type: string
                        example: '<p>Thank you for your reply.</p>'
                      replyTemplateAttachments:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: integer
                              example: 1
                            uuid:
                              type: string
                              example: 'f1e2d3c4-b5a6-7890-abcd-ef1234567890'
                            reply_template_id:
                              type: integer
                              example: 1
                            file_name:
                              type: string
                              example: 'proposal.pdf'
                            download_url:
                              type: string
                              example: 'https://dedi.emailbison.com/api/reply-templates/attachments/f1e2d3c4-b5a6-7890-abcd-ef1234567890/download'
                            size:
                              type: integer
                              example: 204800
                            created_at:
                              type: string
                              example: '2025-04-14T16:59:21.000000Z'
                            updated_at:
                              type: string
                              example: '2025-05-18T12:53:32.000000Z'
                      created_at:
                        type: string
                        example: '2025-04-14T16:59:21.000000Z'
                      updated_at:
                        type: string
                        example: '2025-05-18T12:53:32.000000Z'
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
