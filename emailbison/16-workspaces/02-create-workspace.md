# Create Workspace

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1:
    post:
      summary: Create Workspace
      deprecated: false
      description: >-
        This endpoint allows the authenticated user to create a new workspace.

        The user must provide a valid authentication token in the request header
        and the details of the new workspace in the request body.
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
                      id:
                        type: integer
                        example: 1
                      name:
                        type: string
                        example: "John Doe's Second Team"
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
                        example: 0
                      remaining_monthly_email_verification_credits:
                        type: integer
                        example: 0
                      remaining_email_verification_credits:
                        type: integer
                        example: 0
                      total_email_verification_credits:
                        type: integer
                        example: 0
                      sender_email_limit:
                        type: integer
                        example: 100000
                      warmup_limit:
                        type: integer
                        example: 100000
                      warmup_filter_phrase:
                        type: string
                        nullable: true
                        example: null
                      sender_email_limit_disabled:
                        type: boolean
                        example: false
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
