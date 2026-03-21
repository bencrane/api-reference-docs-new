# List Leads

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads:
    get:
      summary: Get all leads
      deprecated: false
      description: 'Retrieve a list of all leads for the authenticated user.'
      tags:
        - Leads
      parameters:
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: 'Search term for filtering replies.'
        - name: filters
          in: query
          required: false
          schema:
            type: object
          description: ''
        - name: filters.lead_campaign_status
          in: query
          required: false
          schema:
            type: string
          description: 'Filter by lead campaign status. One of `in_sequence`, `sequence_finished`, `sequence_stopped`, `never_contacted`, `replied`.'
        - name: filters.emails_sent
          in: query
          required: false
          schema:
            type: array
          description: 'Filter by the number of emails sent.'
        - name: filters.emails_sent.criteria
          in: query
          required: false
          schema:
            type: string
          description: 'Comparison operator for emails sent. One of `=`, `>=`, `>`, `<=`, `<`.'
        - name: filters.emails_sent.value
          in: query
          required: false
          schema:
            type: integer
          description: 'Value for the number of emails sent.'
        - name: filters.opens
          in: query
          required: false
          schema:
            type: object
          description: ''
        - name: filters.opens.criteria
          in: query
          required: false
          schema:
            type: string
          description: 'Comparison operator for email opens. One of `=`, `>=`, `>`, `<=`, `<`.'
        - name: filters.opens.value
          in: query
          required: false
          schema:
            type: integer
          description: 'Value for the number of email opens.'
        - name: filters.replies
          in: query
          required: false
          schema:
            type: object
          description: ''
        - name: filters.replies.criteria
          in: query
          required: false
          schema:
            type: string
          description: 'Comparison operator for replies. One of `=`, `>=`, `>`, `<=`, `<`.'
        - name: filters.replies.value
          in: query
          required: false
          schema:
            type: integer
          description: 'Value for the number of replies.'
        - name: filters.verification_statuses
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: 'A verification status. Accepted values: `verifying`, `verified`, `risky`, `unknown`, `unverified`, `inactive`, `bounced`, `unsubscribed`.'
        - name: filters.tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: 'Filter by tag IDs.'
        - name: filters.excluded_tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: 'Exclude leads by tag IDs.'
        - name: filters.without_tags
          in: query
          required: false
          schema:
            type: boolean
          description: 'Only show leads that have no tags attached.'
        - name: filters.created_at
          in: query
          required: false
          schema:
            type: object
          description: ''
        - name: filters.created_at.criteria
          in: query
          required: false
          schema:
            type: string
          description: 'Comparison operator for the created_at date. One of `=`, `>=`, `>`, `<=`, `<`.'
        - name: filters.created_at.value
          in: query
          required: false
          schema:
            type: string
          description: 'Value for the created_at date. Must be a valid date in YYYY-MM-DD format.'
        - name: filters.updated_at
          in: query
          required: false
          schema:
            type: object
          description: ''
        - name: filters.updated_at.criteria
          in: query
          required: false
          schema:
            type: string
          description: 'Comparison operator for the updated_at date. One of `=`, `>=`, `>`, `<=`, `<`.'
        - name: filters.updated_at.value
          in: query
          required: false
          schema:
            type: string
          description: 'Value for the updated_at date. Must be a valid date in YYYY-MM-DD format.'
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
                        first_name:
                          type: string
                          example: John
                        last_name:
                          type: string
                          example: Doe
                        email:
                          type: string
                          example: john@doe.com
                        title:
                          type: string
                          example: Engineer
                        company:
                          type: string
                          example: John Doe company
                        notes:
                          type: string
                          example: Important client
                        status:
                          type: string
                          example: verified
                        custom_variables:
                          type: array
                          items:
                            type: object
                            properties:
                              name:
                                type: string
                                example: company_website
                              value:
                                type: string
                                example: 'https://company.com'
                        lead_campaign_data:
                          type: array
                          example: []
                        overall_stats:
                          type: object
                          properties:
                            emails_sent:
                              type: integer
                              example: 3
                            opens:
                              type: integer
                              example: 0
                            replies:
                              type: integer
                              example: 1
                            unique_replies:
                              type: integer
                              example: 1
                            unique_opens:
                              type: integer
                              example: 0
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
