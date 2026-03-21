# Bulk Create Leads from CSV

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/bulk/csv:
    post:
      summary: Bulk create leads using CSV
      deprecated: false
      description: 'Create multiple leads in a single request using a CSV.'
      tags:
        - Leads
      parameters: []
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                  description: 'The CSV file containing lead data.'
      responses:
        '201':
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
                          example: 9
                        name:
                          type: string
                          example: ''
                        status:
                          type: string
                          example: Unprocessed
                        leads_processed:
                          type: integer
                          example: 0
                        leads_succeeded:
                          type: integer
                          example: 0
                        leads_failed:
                          type: integer
                          example: 0
                        error_messages:
                          type: string
                          nullable: true
                          example: null
                        created_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
                        updated_at:
                          type: string
                          example: '2025-04-14T16:59:21.000000Z'
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
