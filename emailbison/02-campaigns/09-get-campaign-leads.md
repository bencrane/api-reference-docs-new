# Get Campaign Leads

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads:
    get:
      summary: Get all leads for campaign
      description: This endpoint retrieves all leads associated with a campaign.
      tags:
        - Campaigns
      operationId: getAllLeadsForCampaign
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
        - name: search
          in: query
          required: false
          schema:
            type: string
          description: Search term for filtering replies.
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
          description: >-
            Filter by lead campaign status. One of `in_sequence`,
            `sequence_finished`, `sequence_stopped`, `never_contacted`, `replied`.
        - name: filters.emails_sent
          in: query
          required: false
          schema:
            type: array
          description: Filter by the number of emails sent.
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
          description: Value for the number of emails sent.
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
          description: Value for the number of email opens.
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
          description: Value for the number of replies.
        - name: filters.verification_statuses
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            A verification status. Accepted values: `verifying`, `verified`,
            `risky`, `unknown`, `unverified`, `inactive`, `bounced`,
            `unsubscribed`.
        - name: filters.tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Filter by tag IDs.
        - name: filters.excluded_tag_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: Exclude leads by tag IDs.
        - name: filters.without_tags
          in: query
          required: false
          schema:
            type: boolean
          description: Only show leads that have no tags attached.
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
          description: Value for the created_at date. Must be a valid date in YYYY-MM-DD format.
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
          description: Value for the updated_at date. Must be a valid date in YYYY-MM-DD format.
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
                        id:
                          type: integer
                          example: 1138
                        first_name:
                          type: string
                          example: Tom
                        last_name:
                          type: string
                          example: Fisher
                        email:
                          type: string
                          example: bademail@example.com
                        title:
                          type: string
                          example: null
                        company:
                          type: string
                          example: null
                        notes:
                          type: string
                          example: null
                        status:
                          type: string
                          example: bounced
                        custom_variables:
                          type: array
                          example: []
                        lead_campaign_data:
                          type: object
                          properties:
                            status:
                              type: string
                              example: bounced
                            emails_sent:
                              type: integer
                              example: 1
                            replies:
                              type: integer
                              example: 0
                            opens:
                              type: integer
                              example: 0
                            interested:
                              type: boolean
                              example: false
                        overall_stats:
                          type: object
                          properties:
                            emails_sent:
                              type: integer
                              example: 1
                            opens:
                              type: integer
                              example: 0
                            replies:
                              type: integer
                              example: 0
                            unique_replies:
                              type: integer
                              example: 0
                            unique_opens:
                              type: integer
                              example: 0
                        created_at:
                          type: string
                          example: '2024-06-16T23:51:54.000000Z'
                        updated_at:
                          type: string
                          example: '2024-06-16T23:54:54.000000Z'
              example:
                data:
                  - id: 1138
                    first_name: Tom
                    last_name: Fisher
                    email: bademail@example.com
                    title: null
                    company: null
                    notes: null
                    status: bounced
                    custom_variables: []
                    lead_campaign_data:
                      status: bounced
                      emails_sent: 1
                      replies: 0
                      opens: 0
                      interested: false
                    overall_stats:
                      emails_sent: 1
                      opens: 0
                      replies: 0
                      unique_replies: 0
                      unique_opens: 0
                    created_at: '2024-06-16T23:51:54.000000Z'
                    updated_at: '2024-06-16T23:54:54.000000Z'
                  - id: 1139
                    first_name: Cody
                    last_name: Smith
                    email: cody@emailguard.io
                    title: null
                    company: null
                    notes: null
                    status: unverified
                    custom_variables: []
                    lead_campaign_data:
                      status: sequence_finished
                      emails_sent: 1
                      replies: 0
                      opens: 0
                      interested: false
                    overall_stats:
                      emails_sent: 1
                      opens: 0
                      replies: 0
                      unique_replies: 0
                      unique_opens: 0
                    created_at: '2024-06-16T23:51:54.000000Z'
                    updated_at: '2024-06-16T23:53:56.000000Z'
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
