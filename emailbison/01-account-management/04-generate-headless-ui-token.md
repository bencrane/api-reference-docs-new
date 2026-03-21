# Generate Headless UI Token

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/users/headless-ui-token:
    post:
      summary: Generate Headless UI Token (Beta)
      deprecated: false
      description: 'Generates a headless UI token valid for 120 minutes. Used for embedding email account connection views in iframes. The URL must be whitelisted. This endpoint is currently in beta.'
      tags:
        - Account Management
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      token:
                        type: string
                        example: 'headless_ui_token_rtG42rhsFhHq8rySjjaWh8RnaA'
          headers: {}
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
