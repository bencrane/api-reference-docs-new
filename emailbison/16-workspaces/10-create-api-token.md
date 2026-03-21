# Create API Token for Workspace

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/{team_id}/api-tokens:
    post:
      summary: Create API token for workspace
      deprecated: false
      description: >-
        This endpoint lets you create an API token for a given workspace.

        Requires a "super admin" API token.
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
                  description: The name of the API token.
                  example: 'New token'
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
                        example: 39
                      name:
                        type: string
                        example: 'tingz'
                      plain_text_token:
                        type: string
                        example: '39|RYHi6oE6o0fVuEPEDSUe6dN7tCFJwvJ6cAytBKxq69deeeee'
                      token_hash:
                        type: string
                        example: '4d2a4cd30dbc1f30047a8c1341c5aebdfece35eafd8b43f17411e46cd4c6e36d'
                      abilities:
                        type: array
                        items:
                          type: string
                        example: ['*']
                      created_at:
                        type: string
                        example: '2025-03-10T04:29:09.000000Z'
                      updated_at:
                        type: string
                        example: '2025-03-10T04:29:09.000000Z'
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
