# Get Master Inbox Settings

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/master-inbox-settings:
    get:
      summary: Get Master Inbox Settings
      deprecated: false
      description: >-
        This endpoint retrieves the master inbox settings for this workspace.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Workspaces
      parameters: []
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
                      sync_all_emails:
                        type: boolean
                        example: true
                      smart_warmup_filter:
                        type: boolean
                        example: true
                      auto_interested_categorization:
                        type: boolean
                        example: false
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
