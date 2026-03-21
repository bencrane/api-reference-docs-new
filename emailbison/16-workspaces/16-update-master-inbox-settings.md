# Update Master Inbox Settings

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/workspaces/v1.1/master-inbox-settings:
    patch:
      summary: Update Master Inbox Settings
      deprecated: false
      description: >-
        This endpoint updates the master inbox settings for this workspace.

        The user must provide a valid authentication token in the request header to access this endpoint.
      tags:
        - Workspaces
      parameters: []
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                sync_all_emails:
                  type: boolean
                  description: >-
                    If set to true, all emails (incoming and outgoing) will be synced.
                    If set to false, only replies to your campaign emails will be synced.
                    Only set to false if you are managing your master inbox in another app and want to reduce noise.
                  example: false
                smart_warmup_filter:
                  type: boolean
                  description: >-
                    If set to true, we will check each email for hyphenated words (eg. strong-bison),
                    and automatically discard them from being synced.
                  example: true
                auto_interested_categorization:
                  type: boolean
                  description: >-
                    If set to true, we will use GPT-4o-mini to check the contents
                    of your email to determine if the response is interested or not.
                    This categorization only runs for the first unique reply from a contact.
                  example: true
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
                      sync_all_emails:
                        type: boolean
                        example: true
                      smart_warmup_filter:
                        type: boolean
                        example: true
                      auto_interested_categorization:
                        type: boolean
                        example: false
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
