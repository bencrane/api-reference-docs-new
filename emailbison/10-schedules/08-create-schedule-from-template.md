# Create Campaign Schedule from Template

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/create-schedule-from-template:
    post:
      summary: Create campaign schedule from template
      description: >-
        This endpoint allows the authenticated user to create the schedule of
        the campaign from an existing schedule template.
      tags:
        - Schedules
      operationId: createCampaignScheduleFromTemplate
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - schedule_id
              properties:
                schedule_id:
                  type: integer
                  description: The ID of the schedule template.
                  example: 1
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
              example:
                data:
                  id: 1
                  type: Generated
                  monday: true
                  tuesday: true
                  wednesday: true
                  thursday: true
                  friday: true
                  saturday: false
                  sunday: false
                  start_time: '08:00'
                  end_time: '17:00'
                  timezone: America/New_York
                  created_at: '2025-04-14T16:59:21.000000Z'
                  updated_at: '2025-05-18T12:53:32.000000Z'
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
