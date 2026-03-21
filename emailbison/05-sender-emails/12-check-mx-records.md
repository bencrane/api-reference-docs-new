# Check MX Records

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/sender-emails/{senderEmailId}/check-mx-records:
    post:
      summary: Check MX records
      deprecated: false
      description: >-
        Checks the email host for a given email address and returns the host + all MX records.
        Results are not cached, and if a valid return is returned, the Sender Email account will be updated.
      tags:
        - Sender Emails
      parameters:
        - name: senderEmailId
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the sender email account.
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
                      email:
                        type: string
                        example: 'john@doe.com'
                      email_host:
                        type: string
                        example: Google
                      mx_records_valid:
                        type: string
                        example: 'true'
                      mx_records:
                        type: array
                        items:
                          type: object
                          properties:
                            host:
                              type: string
                              example: 'domain.com'
                            priority:
                              type: integer
                              example: 300
                            class:
                              type: string
                              example: IN
                            type:
                              type: string
                              example: MX
                            pri:
                              type: integer
                              example: 0
                            target:
                              type: string
                              example: 'domain-com.mail.protection.outlook.com'
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
