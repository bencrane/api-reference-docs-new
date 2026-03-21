# Switch Workspace

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/switch-workspace:
    post:
      summary: Switch Workspace
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to switch to a different workspace.

        The user must provide a valid authentication token in the request header
        and the ID of the target workspace in the request body to access this endpoint.
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
                - team_id
              properties:
                team_id:
                  type: integer
                  description: The ID of the team (workspace) to switch.
                  example: 13
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
                        example: "John Doe's Second Team"
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
