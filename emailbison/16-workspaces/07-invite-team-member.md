# Invite Team Member

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/invite-members:
    post:
      summary: Invite Team Member
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to invite a new member to their team.

        The user must provide a valid authentication token in the request header
        and the email and role of the new team member in the request body.
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
                - email
                - role
              properties:
                email:
                  type: string
                  description: The email of the new team member.
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
                      id:
                        type: integer
                        example: 11
                      uuid:
                        type: string
                        example: '9e656435-3ad8-4685-9973-b07f92f7025f'
                      workspace_id:
                        type: integer
                        example: 1
                      email:
                        type: string
                        example: 'example+teaminvite@example.com'
                      role:
                        type: string
                        example: admin
                      created_at:
                        type: string
                        example: '2025-03-10T05:05:00.000000Z'
                      updated_at:
                        type: string
                        example: '2025-03-10T05:05:00.000000Z'
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
