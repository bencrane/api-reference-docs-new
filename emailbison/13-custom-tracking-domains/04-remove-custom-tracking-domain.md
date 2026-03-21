# Remove Custom Tracking Domain

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/custom-tracking-domain/{custom_tracking_domain_id}:
    delete:
      summary: Remove Custom Tracking Domain
      deprecated: false
      description: 'Removes a custom tracking domain.'
      tags:
        - Custom Tracking Domains
      parameters:
        - name: custom_tracking_domain_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the custom tracking domain.
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
                      success:
                        type: boolean
                        example: true
                      message:
                        type: string
                        example: Successfully removed custom tracking domain
          headers: {}
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: The given data was invalid.
                  errors:
                    type: object
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
