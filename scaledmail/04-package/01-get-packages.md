# Get Packages

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/packages:
    get:
      summary: Get Packages
      deprecated: false
      description: ''
      tags:
        - Package
      parameters: []
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                total: 3
                packages:
                  - id: price_1RwQijBUS24WVOL3fBhLhYPp
                    tier: low-sending
                    name: SM Google 70% - SM MS 30%
                    mode: subscription
                    price: 199
                    domains: 12
                    google:
                      mailbox: 20
                    microsoft:
                      mailbox: 100
                      domains: 2
                    frequency: /monthly
                  - id: price_1RwQoGBUS24WVOL3Py9UrJpq
                    tier: medium-sending
                    mode: subscription
                    name: SM - Google
                    price: 245
                    domains: 35
                    google:
                      mailbox: 70
                    frequency: /monthly
                  - id: price_1QhZ1JBUS24WVOL3lBcDjtDw
                    tier: high-sending
                    mode: subscription
                    name: SM - Microsoft
                    price: 597
                    domains: 12
                    microsoft:
                      mailbox: 300
                      domains: 12
                    frequency: /monthly
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Package
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18333850-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
