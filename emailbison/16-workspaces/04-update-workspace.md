# Update Workspace

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/{team_id}:
    put:
      summary: Update Workspace
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to update their workspace information,
        specifically the workspace name.

        The user must provide a valid authentication token in the request header
        and the ID of the target workspace, along with the details of the new workspace
        in the request body to access this endpoint.
      tags:
        - Workspaces
      parameters:
        - name: team_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the workspace.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: The new workspace name.
                  example: 'New name'
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
                        example: 'J.D Workspace'
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
