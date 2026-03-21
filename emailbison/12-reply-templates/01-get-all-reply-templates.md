# Get All Reply Templates

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/reply-templates:
    get:
      summary: Get All Reply Templates
      deprecated: false
      description: 'Returns a paginated list of reply templates.'
      tags:
        - Reply Templates
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Search query to filter reply templates by name
      responses:
        '200':
          description: ''
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
                  links:
                    type: object
                    properties:
                      first:
                        type: string
                        example: 'https://dedi.emailbison.com/api/reply-templates?page=1'
                      last:
                        type: string
                        example: 'https://dedi.emailbison.com/api/reply-templates?page=1'
                      prev:
                        type: string
                        nullable: true
                        example: null
                      next:
                        type: string
                        nullable: true
                        example: null
                  meta:
                    type: object
                    properties:
                      current_page:
                        type: integer
                        example: 1
                      from:
                        type: integer
                        example: 1
                      last_page:
                        type: integer
                        example: 1
                      links:
                        type: array
                        items:
                          type: object
                          properties:
                            url:
                              type: string
                              nullable: true
                            label:
                              type: string
                            active:
                              type: boolean
                      path:
                        type: string
                        example: 'https://dedi.emailbison.com/api/reply-templates'
                      per_page:
                        type: integer
                        example: 15
                      to:
                        type: integer
                        example: 1
                      total:
                        type: integer
                        example: 1
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
