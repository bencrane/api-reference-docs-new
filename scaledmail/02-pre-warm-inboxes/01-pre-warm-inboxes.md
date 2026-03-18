# Pre Warm Inboxes

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/pre-warm-inboxes:
    get:
      summary: Pre Warm Inboxes
      deprecated: false
      description: >-
        This endpoint returns all available pre-warmed inboxes for Google and
        Outlook, including their pricing details and warm-up age (in months).
      tags:
        - Pre Warm Inboxes
      parameters:
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
              example:
                total: 4
                google:
                  - warmup_age: 1
                    id: recLuIthqG59R4nmZ
                    domain: 1apitestgoogle.com
                    emailMailboxCount: 2
                    pricing:
                      oneTimePrice: 23
                      monthlyPrice: 8
                    emailMailbox:
                      - first_name: James
                        last_name: Smith
                        alias: james.smith
                      - first_name: James
                        last_name: Smith
                        alias: james
                  - warmup_age: 2
                    id: reckPXxVGMsaL3yKs
                    domain: wisescalegrowth.com
                    emailMailboxCount: 2
                    pricing:
                      oneTimePrice: 23
                      monthlyPrice: 8
                    emailMailbox:
                      - first_name: James
                        last_name: Smith
                        alias: james.smith
                      - first_name: James
                        last_name: Smith
                        alias: james
                outlook:
                  - warmup_age: 2
                    id: rec0tZOQtwjJwYutj
                    domain: forgepathbase.com
                    emailMailboxCount: 25
                    pricing:
                      oneTimePrice: 30
                      monthlyPrice: 50
                  - warmup_age: 1
                    id: rec1yaWEUxTiqJ97H
                    domain: clarityhubpoint.com
                    emailMailboxCount: 25
                    pricing:
                      oneTimePrice: 30
                      monthlyPrice: 50
                    emailMailbox:
                      - first_name: Michael
                        last_name: Smith
                        alias: michael.smith
                      - first_name: Michael
                        last_name: Smith
                        alias: michael
                      - first_name: Michael
                        last_name: Smith
                        alias: m.smith
                      - first_name: Michael
                        last_name: Smith
                        alias: michaelsmith
                      - first_name: Michael
                        last_name: Smith
                        alias: michael.s
                      - first_name: Jennifer
                        last_name: Johnson
                        alias: jennifer.johnson
                      - first_name: Jennifer
                        last_name: Johnson
                        alias: jenniferjohnson
                      - first_name: Jennifer
                        last_name: Johnson
                        alias: jennifer
                      - first_name: Jennifer
                        last_name: Johnson
                        alias: j.johnson
                      - first_name: Jennifer
                        last_name: Johnson
                        alias: jennifer.j
                      - first_name: David
                        last_name: Williams
                        alias: david.williams
                      - first_name: David
                        last_name: Williams
                        alias: d.williams
                      - first_name: David
                        last_name: Williams
                        alias: davidwilliams
                      - first_name: David
                        last_name: Williams
                        alias: david.w
                      - first_name: David
                        last_name: Williams
                        alias: david
                      - first_name: Sarah
                        last_name: Brown
                        alias: sarah.brown
                      - first_name: Sarah
                        last_name: Brown
                        alias: s.brown
                      - first_name: Sarah
                        last_name: Brown
                        alias: sarahb
                      - first_name: Sarah
                        last_name: Brown
                        alias: s.b
                      - first_name: Sarah
                        last_name: Brown
                        alias: sarah
                      - first_name: Christopher
                        last_name: Davis
                        alias: christopher.davis
                      - first_name: Christopher
                        last_name: Davis
                        alias: chris.davis
                      - first_name: Christopher
                        last_name: Davis
                        alias: c.davis
                      - first_name: Christopher
                        last_name: Davis
                        alias: christopher
                      - first_name: Christopher
                        last_name: Davis
                        alias: cdavis
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Pre Warm Inboxes
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-26623539-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
