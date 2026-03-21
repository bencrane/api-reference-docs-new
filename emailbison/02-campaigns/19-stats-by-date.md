# Stats by Date

This endpoint is the same as [Campaign Events Stats](./21-campaign-events-stats.md) but filtered by a specific campaign ID. Use the `campaign_ids` query parameter to scope results to a single campaign.

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaign-events/stats:
    get:
      summary: Breakdown of events by date (per campaign)
      description: >-
        This endpoint retrieves stats by date for a given period, for a specific
        campaign. Use the `campaign_ids` parameter to filter by campaign.

        Drill down into campaign event stats based on dates, campaign IDs,
        and/or sender email IDs.

        The user must provide a valid authentication token in the request header
        to access this endpoint.

        Events returned: `Replied`, `Total Opens`, `Unique Opens`, `Sent`,
        `Bounced`, `Unsubscribed`, `Interested`.
      tags:
        - Campaigns
      operationId: breakdownOfEventsByDate
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
        - name: sender_email_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: List of sender email IDs to include.
        - name: campaign_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: integer
          description: List of campaign IDs to include.
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
                          items:
                            type: array
                          example:
                            - - '2025-05-03'
                              - 0
              example:
                data:
                  - label: Replied
                    color: '#f54842'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Total Opens
                    color: '#00E396'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Sent
                    color: '#3B82F6'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Unsubscribed
                    color: '#fffff2'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Bounced
                    color: '#fffff1'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Interested
                    color: '#fffff3'
                    dates:
                      - - '2025-05-03'
                        - 0
                  - label: Unique Opens
                    color: '#00d0ff'
                    dates:
                      - - '2025-05-03'
                        - 0
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
