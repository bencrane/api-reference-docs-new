# Accept Workspace Invitation

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/accept/{team_invitation_id}:
    post:
      summary: Accept Workspace Invitation
      deprecated: false
      description: >-
        This endpoint allows the user to accept an invitation to join a workspace.

        The user must provide a valid authentication token in the request header
        and the ID of the workspace invitation.
      tags:
        - Workspaces
      parameters:
        - name: team_invitation_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the workspace invitation.
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
                        example: 'Successfully accepted the invitation'
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
