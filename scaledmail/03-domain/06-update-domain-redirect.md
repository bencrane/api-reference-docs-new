# Update Domain Redirect

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/swap-redirect/{domain}:
    post:
      summary: Update Domain Redirect
      deprecated: false
      description: >-
        ### 🔑 Query Parameters


        * **`domain`** (required):
          The **current domain name** whose redirect you want to update.

        ---


        ### 📥 Request Body Parameters


        All parameters below must be included in the **JSON body** of the
        request.


        * **`new_redirect`** (required):
          The **new domain name** to redirect to.
          → This can be either a **third-party (external) domain** or an **available purchased domain** retrieved from the `/purchased-domains` endpoint.

        ---


        ### ⚠️ Important Notes


        * If the **domain is not found**, the request will fail.

        * If a **redirect update is already in progress**, the request will be
        rejected.

        * No **new order** will be created for domain redirect update requests.
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
      requestBody:
        content:
          text/plain:
            schema:
              type: string
            example:
              new_redirect: scaledmail.com
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
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-27391635-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```