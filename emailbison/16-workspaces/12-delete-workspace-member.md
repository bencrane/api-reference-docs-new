# Delete Workspace Member

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/members/{user_id}:
    delete:
      summary: Delete Workspace Member
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to remove a workspace member.

        This does not delete the user account. It only removes them from the workspace.

        The user must provide a valid authentication token in the request header
        and the ID of the workspace member.
      tags:
        - Workspaces
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the workspace member.
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
                        example: 'Successfully deleted team member John Doe'
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
