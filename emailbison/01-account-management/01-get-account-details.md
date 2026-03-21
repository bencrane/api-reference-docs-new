# Get Account Details

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/users:
    get:
      summary: Get Account Details
      deprecated: false
      description: 'Returns the authenticated user''s account information including team details, workspace limits, and verification credits.'
      tags:
        - Account Management
      parameters: []
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
                      name:
                        type: string
                        example: John Doe
                      email:
                        type: string
                        example: john@doe.com
                      team:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 1
                          name:
                            type: string
                            example: "John Doe's Team"
                          personal_team:
                            type: boolean
                            example: true
                          main:
                            type: boolean
                            example: true
                          parent_id:
                            type: integer
                            nullable: true
                            example: null
                          total_monthly_email_verification_credits:
                            type: integer
                            example: 0
                          remaining_monthly_email_verification_credits:
                            type: integer
                            example: 0
                          remaining_email_verification_credits:
                            type: integer
                            example: 0
                          total_email_verification_credits:
                            type: integer
                            example: 0
                          sender_email_limit:
                            type: integer
                            example: 100000
                          warmup_limit:
                            type: integer
                            example: 100000
                          warmup_filter_phrase:
                            type: string
                            nullable: true
                            example: null
                          has_access_to_warmup:
                            type: boolean
                            example: false
                          has_access_to_healthcheck:
                            type: boolean
                            example: false
                          created_at:
                            type: string
                            example: '2025-04-14T16:59:21.000000Z'
                          updated_at:
                            type: string
                            example: '2025-05-18T12:53:32.000000Z'
                      profile_photo_path:
                        type: string
                        nullable: true
                        example: null
                      profile_photo_url:
                        type: string
                        example: 'https://ui-avatars.com/api/?name=J&color=7F9CF5&background=EBF4FF'
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
