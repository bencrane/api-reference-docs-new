# Buy Domains

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/buy-domains:
    post:
      summary: Buy Domains
      deprecated: false
      description: >-
        ⚠️ Requires a connected payment method.

        This endpoint will automatically charge the connected method upon
        successful domain purchase.


        ✅ You can pass a maximum of 10 domains in the request body per API call.


        ❌ All domains must be available for purchase. If any domain is
        unavailable, the entire request will fail with an error.


        ⏱️ This endpoint is rate-limited to 15 requests per minute.
      tags:
        - Domain
      parameters:
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
      requestBody:
        content:
          text/plain:
            schema:
              type: string
            example:
              domains:
                - scaledmail.com
                - beanstalk.com
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Domain
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18334132-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
