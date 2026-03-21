# Update Lead Status

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}/update-status:
    patch:
      summary: Update lead status
      deprecated: false
      description: 'Update the status of a lead.'
      tags:
        - Leads
      parameters:
        - name: lead_id
          in: path
          required: true
          schema:
            type: integer
          description: 'The ID of the lead to update.'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - status
              properties:
                status:
                  type: string
                  description: 'The status to apply to the lead.'
                  example: inactive
                  nullable: false
                  enum:
                    - verified
                    - unverified
                    - unknown
                    - risky
                    - inactive
      responses:
        '200':
          description: ''
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
                        example: 326217
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
                        example: John Doe Company
                      notes:
                        type: string
                        example: Important client
                      status:
                        type: string
                        example: inactive
                      custom_variables:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              example: another one
                            value:
                              type: string
                              example: baddye
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
                        example: '2024-07-29T02:10:45.000000Z'
                      updated_at:
                        type: string
                        example: '2024-07-29T02:10:45.000000Z'
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
