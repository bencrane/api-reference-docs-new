# Update Domain Name

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/swap-domain/{domain}:
    post:
      summary: Update Domain Name
      deprecated: false
      description: >-
        ### 🔑 Query Parameters


        * **`domain`** (required):
          The **old domain name** you want to swap out.

        * **`provider`** (required):
          Specifies the source of the new domain:
          → `"scaledmail"` — Domain purchased through ScaledMail
          → `"other"` — Domain from external providers like **Porkbun**, **Namecheap**, or **DNSimple**

        ---


        ### 📥 Request Body Parameters


        All parameters below must be included in the **JSON body** of the
        request.


        * **`new_domain`** (required):
          The **name of the new domain** you want to assign.
          → This can be either a **third-party domain** (external) or an **available purchased domain** retrieved from the `/purchased-domains` endpoint.

        * **`hosting`** (conditionally required):
          Required only when `provider = "other"` (i.e., for third-party domains).
          → **Not required** if `provider = "scaledmail"` — ScaledMail handles hosting automatically.
      tags:
        - Domain
      parameters:
        - name: domain
          in: path
          description: ''
          required: true
          schema:
            type: string
        - name: organization_id
          in: query
          description: Organization ID
          required: true
          schema:
            type: string
        - name: provider
          in: query
          description: Domain Provider
          required: true
          schema:
            type: string
            examples:
              - other
              - scaledmail
      requestBody:
        content:
          text/plain:
            schema:
              type: string
            examples:
              '1':
                value: |
                  {
                    "hosting": {
                      "provider": "Hosting Provier Name Here",
                      "username": "username",
                      "password": "password"
                    },
                    "new_domain":"scaledmailgo.com",
                  }
                summary: Other Domain Provider
              '2':
                value:
                  new_domain: scaledmailgo.com
                summary: Scaledmail Domain Provier
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apidog-name: Success
      security:
        - bearer: []
      x-apidog-folder: Domain
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18547274-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
