# Update Password

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/users/password:
    put:
      summary: Update Password
      deprecated: false
      description: 'Updates the authenticated user''s password.'
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
                - current_password
                - password
                - password_confirmation
              properties:
                current_password:
                  type: string
                  description: The user's current password.
                  example: 'oldPassword123'
                password:
                  type: string
                  description: The new password.
                  example: 'newPassword456'
                password_confirmation:
                  type: string
                  description: Confirmation of the new password. Must match the password field.
                  example: 'newPassword456'
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: 'Successfully updated your profile password'
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
