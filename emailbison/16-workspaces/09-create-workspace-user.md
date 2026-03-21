# Create Workspace User

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/users:
    post:
      summary: Create User (and add to workspace)
      deprecated: false
      description: >-
        This endpoint provides a convenient way to create a new user on your instance, and
        add them to the current workspace. This provides an alternate flow where you want to mass
        create users.

        If you simply want to invite users and have them accept the invitation, or accept it
        programmatically, consider using the other endpoints.
      tags:
        - Workspaces
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - password
                - email
                - role
              properties:
                name:
                  type: string
                  description: The name of the user.
                  example: 'John Doe'
                password:
                  type: string
                  description: The password of the user.
                  example: 'securepasswordlol'
                email:
                  type: string
                  description: The email of the user.
                  example: 'example@example.com'
                role:
                  type: string
                  description: The role of the new team member.
                  example: admin
                  enum:
                    - admin
                    - editor
                    - client
                    - reseller
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
                      name:
                        type: string
                        example: 'tingz'
                      email:
                        type: string
                        example: 'listkittest@example.com'
                      workspace:
                        type: object
                        properties:
                          id:
                            type: integer
                            example: 1
                          name:
                            type: string
                            example: "Cody's Team"
                          personal_team:
                            type: boolean
                            example: true
                          main:
                            type: boolean
                            example: true
                          parent_id:
                            type: string
                            nullable: true
                            example: null
                          total_monthly_email_verification_credits:
                            type: integer
                            example: 2500
                          remaining_monthly_email_verification_credits:
                            type: integer
                            example: 2462
                          remaining_email_verification_credits:
                            type: integer
                            example: 250
                          total_email_verification_credits:
                            type: integer
                            example: 250
                          sender_email_limit:
                            type: integer
                            example: 0
                          warmup_limit:
                            type: integer
                            example: 50
                          warmup_filter_phrase:
                            type: string
                            example: 'qvwy7276'
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
                        example: 'https://ui-avatars.com/api/?name=t&color=7F9CF5&background=EBF4FF'
                      created_at:
                        type: string
                        example: '2025-04-14T16:59:21.000000Z'
                      updated_at:
                        type: string
                        example: '2025-05-18T12:53:32.000000Z'
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
