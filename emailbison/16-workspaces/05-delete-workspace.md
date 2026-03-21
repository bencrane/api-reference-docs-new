# Delete Workspace

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/{team_id}:
    delete:
      summary: Delete Workspace
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to delete a workspace.

        The user must provide a valid super-admin authentication token in the request header
        and the ID of the target workspace in the query parameters to access this endpoint.
      tags:
        - Workspaces
      parameters:
        - name: team_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the workspace to delete.
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
                        example: 'Workspace being deleted. This might take a few minutes if you have a lot of data.'
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
