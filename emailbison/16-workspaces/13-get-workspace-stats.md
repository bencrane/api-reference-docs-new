# Get Workspace Stats

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/stats:
    get:
      summary: Get workspace stats (summary)
      deprecated: false
      description: >-
        This endpoint retrieves overall stats for this workspace between two given dates.

        The user must provide a valid authentication token in the request header to access this endpoint.
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
                    type: object
                    properties:
                      emails_sent:
                        type: string
                        example: '10'
                      total_leads_contacted:
                        type: string
                        example: '5'
                      opened:
                        type: string
                        example: '5'
                      opened_percentage:
                        type: string
                        example: '50'
                      unique_opens_per_contact:
                        type: string
                        example: '5'
                      unique_opens_per_contact_percentage:
                        type: string
                        example: '50'
                      unique_replies_per_contact:
                        type: string
                        example: '5'
                      unique_replies_per_contact_percentage:
                        type: string
                        example: '50'
                      bounced:
                        type: string
                        example: '0'
                      bounced_percentage:
                        type: string
                        example: '0'
                      unsubscribed:
                        type: string
                        example: '5'
                      unsubscribed_percentage:
                        type: string
                        example: '50'
                      interested:
                        type: string
                        example: '5'
                      interested_percentage:
                        type: string
                        example: '50'
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
