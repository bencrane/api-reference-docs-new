# List Warmup Stats

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/warmup/sender-emails:
    get:
      summary: List Warmup Stats
      deprecated: false
      description: 'Returns a list of email accounts with their warmup statistics for the specified date range.'
      tags:
        - Warmup
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Search term to filter email accounts.
          example: 'john@example.com'
        - name: tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Filter by tag IDs.
        - name: excluded_tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Exclude email accounts with these tag IDs.
        - name: without_tags
          in: query
          required: false
          schema:
            type: boolean
          description: If true, only return email accounts without any tags.
        - name: warmup_status
          in: query
          required: false
          schema:
            type: string
            enum:
              - enabled
              - disabled
          description: Filter by warmup status.
        - name: mx_records_status
          in: query
          required: false
          schema:
            type: string
          description: Filter by MX records status.
        - name: start_date
          in: query
          required: true
          schema:
            type: string
          description: Start date for the warmup stats period.
          example: '2025-01-01'
        - name: end_date
          in: query
          required: true
          schema:
            type: string
          description: End date for the warmup stats period.
          example: '2025-01-31'
        - name: filters.excluded_tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Exclude email accounts with these tag IDs (filter variant).
        - name: filters.without_tags
          in: query
          required: false
          schema:
            type: boolean
          description: If true, only return email accounts without any tags (filter variant).
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
                        email:
                          type: string
                          example: 'john@example.com'
                        name:
                          type: string
                          example: 'John Doe'
                        domain:
                          type: string
                          example: 'example.com'
                        tags:
                          type: array
                          items:
                            type: object
                            properties:
                              id:
                                type: integer
                                example: 1
                              name:
                                type: string
                                example: 'Important'
                        warmup_emails_sent:
                          type: integer
                          example: 150
                        warmup_replies_received:
                          type: integer
                          example: 45
                        warmup_emails_saved_from_spam:
                          type: integer
                          example: 12
                        warmup_score:
                          type: number
                          example: 85.5
                        warmup_bounces_received_count:
                          type: integer
                          example: 2
                        warmup_bounces_caused_count:
                          type: integer
                          example: 0
                        warmup_disabled_for_bouncing_count:
                          type: integer
                          example: 0
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
