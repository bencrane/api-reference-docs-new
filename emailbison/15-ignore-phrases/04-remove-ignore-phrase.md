# Remove Ignore Phrase

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/ignore-phrases/{ignore_phrase_id}:
    delete:
      summary: Remove Ignore Phrase
      deprecated: false
      description: 'Removes an ignore phrase.'
      tags:
        - Ignore Phrases
      parameters:
        - name: ignore_phrase_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the ignore phrase.
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
                        example: Successfully removed ignore phrase
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
