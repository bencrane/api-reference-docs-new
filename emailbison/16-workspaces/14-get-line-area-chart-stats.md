# Get Line/Area Chart Stats

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/line-area-chart-stats:
    get:
      summary: Get full normalized stats by date
      deprecated: false
      description: >-
        This endpoint retrieves stats by date for a given period.

        The user must provide a valid authentication token in the request header to access this endpoint.

        Events returned: `Replied`, `Total Opens`, `Unique Opens`, `Sent`, `Bounced`, `Unsubscribed`, `Interested`.
      tags:
        - Workspaces
      parameters:
        - name: start_date
          in: query
          required: true
          schema:
            type: string
          description: The start date to fetch stats.
        - name: end_date
          in: query
          required: true
          schema:
            type: string
          description: The end date to fetch stats.
      responses:
        '200':
          description: success
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
                        label:
                          type: string
                          example: Replied
                        color:
                          type: string
                          example: '#f54842'
                        dates:
                          type: array
                          description: 'Array of [date, count] tuples.'
                          items:
                            type: array
                          example:
                            - ['2025-05-03', 0]
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
