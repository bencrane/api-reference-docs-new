# Update Profile Picture

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/users/profile-picture:
    post:
      summary: Update Profile Picture
      deprecated: false
      description: 'Updates the authenticated user''s profile picture. Accepts a base64 encoded image (jpg, jpeg, or png, max 1MB).'
      tags:
        - Account Management
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - photo
              properties:
                photo:
                  type: string
                  description: 'Base64 encoded image string. Supported formats: jpg, jpeg, png. Maximum size: 1MB.'
                  example: 'data:image/png;base64,iVBORw0KGgo...'
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
                        example: 'profile-photos/abc123.png'
                      profile_photo_url:
                        type: string
                        example: 'https://dedi.emailbison.com/storage/profile-photos/abc123.png'
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
