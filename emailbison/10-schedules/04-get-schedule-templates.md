# Get Schedule Templates

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/schedule/templates:
    get:
      summary: Get Schedule Templates
      deprecated: false
      description: 'Returns a list of saved schedule templates.'
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
                        id:
                          type: integer
                          example: 1
                        type:
                          type: string
                          example: Generated
                        monday:
                          type: boolean
                          example: true
                        tuesday:
                          type: boolean
                          example: true
                        wednesday:
                          type: boolean
                          example: true
                        thursday:
                          type: boolean
                          example: true
                        friday:
                          type: boolean
                          example: true
                        saturday:
                          type: boolean
                          example: false
                        sunday:
                          type: boolean
                          example: false
                        start_time:
                          type: string
                          example: '08:00'
                        end_time:
                          type: string
                          example: '17:00'
                        timezone:
                          type: string
                          example: America/New_York
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-05-18T12:53:32.000000Z'
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
