# Get OAuth Access Token

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/{senderEmailId}/oauth-access-token:
    get:
      summary: Get email account oAuth access token
      deprecated: false
      description: >-
        This endpoint retrieves the OAuth access token for a sender email account (Google or Microsoft accounts only).

        If a token has expired, a new one is automatically retrieved and returned using the saved refresh token.
      tags:
        - Sender Emails
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
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
                        example: 2938
                      email:
                        type: string
                        example: 'red@emailguard.io'
                      status:
                        type: string
                        example: Connected
                      type:
                        type: string
                        example: microsoft_oauth
                      oauth_access_token:
                        type: string
                        example: 'hg27Csjq0GWRu5ChiEjNhzyDDuk9YR08gIwvnsfTkqoOISPb9ZEJcFGs6yrEZZ5l...'
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
