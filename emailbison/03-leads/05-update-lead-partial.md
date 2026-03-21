# Update Lead (Partial)

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}:
    patch:
      summary: Update lead (partial)
      deprecated: false
      description: >-
        Update the details of a specific lead.
        Fields passed in the request will be updated. Fields and custom variables not passed will remain unchanged.
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
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                first_name:
                  type: string
                  description: 'The first name of the contact.'
                  example: John
                  nullable: false
                last_name:
                  type: string
                  description: 'The last name of the contact.'
                  example: Doe
                  nullable: false
                email:
                  type: string
                  description: 'The email address of the contact. Must be in a valid email format.'
                  example: john@doe.com
                  nullable: false
                title:
                  type: string
                  description: 'The title of the contact.'
                  example: Engineer
                  nullable: true
                company:
                  type: string
                  description: 'The company name of the contact.'
                  example: John Doe company
                  nullable: true
                notes:
                  type: string
                  description: 'Additional notes about the contact.'
                  example: Important client
                  nullable: true
                custom_variables:
                  type: array
                  description: 'Array of custom variable objects.'
                  items:
                    type: object
                    nullable: true
                    properties:
                      name:
                        type: string
                        description: 'Name of the custom variable field.'
                        example: phone number
                        nullable: false
                      value:
                        type: string
                        description: 'Value of the custom variable.'
                        example: '9059999999'
                        nullable: true
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
                        example: unverified
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
