# Get Available Timezones

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/schedule/available-timezones:
    get:
      summary: Get Available Timezones
      deprecated: false
      description: 'Returns a list of all available timezones that can be used when creating or updating a campaign schedule.'
      tags:
        - Schedules
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
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                          example: '(GMT-12:00) International Date Line West'
                        id:
                          type: string
                          example: Pacific/Kwajalein
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
