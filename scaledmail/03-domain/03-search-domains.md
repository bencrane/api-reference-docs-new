# Search Domains

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/search-domains:
    post:
      summary: Search Domains
      deprecated: false
      description: |+
        You can pass a maximum of 10 domains in the request body per API call.
        This endpoint is rate-limited to 15 requests per minute.






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
              example:
                - domain: utscaledmail.net
                  status: available
                  price: 16.31
                  renewPrice: 16.31
                - domain: scaledmail.com
                  status: taken
                  price: null
                  renewPrice: null
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Domain
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18333873-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
