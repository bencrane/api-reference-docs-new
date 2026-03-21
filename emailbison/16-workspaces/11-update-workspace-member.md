# Update Workspace Member

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/members/{user_id}:
    put:
      summary: Update Workspace Member
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to update the role of a workspace member.

        The user must provide a valid authentication token in the request header
        and the ID of the workspace member and the new role in the request body.
      tags:
        - Workspaces
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the workspace member.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - role
              properties:
                role:
                  type: string
                  description: The new role of the team member.
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: 'Successfully updated team member John Doe role'
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
