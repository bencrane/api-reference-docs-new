# Create Order

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/create-order/{price_id}:
    post:
      summary: Create Order
      deprecated: false
      description: >-
        ### ⚠️ Requires a connected payment method


        A **subscription will be created automatically** upon a successful
        request.


        ---


        ## 🔑 Query Parameters


        ### **`price_id`** (required)


        The **ID of the package** you want to purchase.

        → Retrieve valid `price_id` values from the `/packages` endpoint.


        ### **`provider`** (required)


        Specifies the source of the domains:

        → `"scaledmail"` — Domains purchased through ScaledMail

        → `"other"` — Domains from external providers like **Porkbun**,
        **Namecheap**, or **DNSimple**


        ---


        ## 📥 Request Body Parameters


        All parameters below must be included in the **JSON body**.


        ### **`quantity`** (optional)


        The number of package units you want to purchase.


        * Default: **1**

        * You can increase it if you need multiple units of the same package.


        ---


        ### **`domains`** (required)


        An **array of domain objects** to assign to the package.


        → Get available domains from `/purchased-domains`.

        → The number of domains must **exactly match** the domain count required
        by the selected package.

        → If any domain is already used or unavailable, the request will fail.


        Each domain object can include:


        #### **`domain`** (required)


        Example: `"example.com"`


        #### **`redirect`** (optional)


        A redirect URL for the domain.


        #### **Profile Picture Options**


        You may include:


        ```json

        "profile_picture": "link1.com"

        ```


        * If added **at the domain level**, this image will be used for **all
        aliases** created under that domain.

        * You may also specify a different `profile_picture` inside each alias.


        ---


        ### 👤 Aliases Handling


        You now have **two ways** to provide alias information:


        ---


        ### **1. Pass `first_name` and `last_name`**


        If you include:


        ```json

        "first_name": "John",

        "last_name": "Doe"

        ```


        → The system will **automatically generate aliases** for this domain.


        ---


        ### **2. Pass an `aliases` array directly**


        If you already have pre-generated aliases, you can send them like this:


        ```json

        "aliases": [
          { 
            "first_name": "User1",
            "last_name": "Test",
            "alias": "alias1",
            "profile_picture": "link1.com"
          }
        ]

        ```


        → When the `aliases` array is provided, the system **will not
        auto-generate** aliases.

        → You are free to include custom names, aliases, and profile pictures.


        ---


        ### **`hosting`** (conditionally required)


        Required **only when** `provider = "other"`.


        Must include the relevant:


        * SMTP/IMAP credentials

        * DNS configuration

        * Account credentials

        * Any required verification details


        Not required when using `"scaledmail"` as the provider.
      tags:
        - Order
      parameters:
        - name: price_id
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
        - name: coupon
          in: query
          description: Valid Coupon
          required: false
          schema:
            type: string
      requestBody:
        content:
          text/plain:
            schema:
              type: string
            examples:
              '1':
                value:
                  hosting:
                    provider: Hosting Provier Name Here
                    username: username
                    password: password
                  sequencer:
                    provider: Sequencer Name Here
                    username: username
                    password: password
                  domains:
                    - domain: scaledmail.net
                      first_name: Dean
                      last_name: Fiacoo
                      redirect: scaledmail.com
                    - domain: scaledmail.us
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.org
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.io
                      first_name: Dean
                      last_name: Fiacoo
                summary: Other Domain Provider
              '2':
                value:
                  domains:
                    - domain: scaledmail.net
                      first_name: Dean
                      last_name: Fiacoo
                      redirect: scaledmail.com
                    - domain: scaledmail.us
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.org
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.io
                      first_name: Dean
                      last_name: Fiacoo
                summary: Scaledmail Domain Provier
              '3':
                value:
                  quantity: 1
                  domains:
                    - domain: waynoifterfsddea.torg
                      aliases:
                        - first_name: User1
                          last_name: Test
                          alias: alias1
                          profile_picture: link1.com
                        - first_name: User2
                          last_name: Test
                          alias: alias2
                        - first_name: User3
                          last_name: Test
                          alias: alias3
                        - first_name: User4
                          last_name: Test
                          alias: alias4
                        - first_name: User5
                          last_name: Test
                          alias: alias5
                        - first_name: User6
                          last_name: Test
                          alias: alias6
                        - first_name: User7
                          last_name: Test
                          alias: alias7
                        - first_name: User8
                          last_name: Test
                          alias: alias8
                        - first_name: User9
                          last_name: Test
                          alias: alias9
                        - first_name: User10
                          last_name: Test
                          alias: alias10
                        - first_name: User11
                          last_name: Test
                          alias: alias11
                        - first_name: User12
                          last_name: Test
                          alias: alias12
                        - first_name: User13
                          last_name: Test
                          alias: alias13
                        - first_name: User14
                          last_name: Test
                          alias: alias14
                        - first_name: User15
                          last_name: Test
                          alias: alias15
                        - first_name: User16
                          last_name: Test
                          alias: alias16
                        - first_name: User17
                          last_name: Test
                          alias: alias17
                        - first_name: User18
                          last_name: Test
                          alias: alias18
                        - first_name: User19
                          last_name: Test
                          alias: alias19
                        - first_name: User20
                          last_name: Test
                          alias: alias20
                        - first_name: User21
                          last_name: Test
                          alias: alias21
                        - first_name: User22
                          last_name: Test
                          alias: alias22
                        - first_name: User23
                          last_name: Test
                          alias: alias23
                        - first_name: User24
                          last_name: Test
                          alias: alias24
                        - first_name: User24
                          last_name: Test
                          alias: alias25
                summary: Aliases
              '4':
                value:
                  hosting:
                    provider: Hosting Provier Name Here
                    username: username
                    password: password
                  sequencer:
                    provider: Sequencer Name Here
                    username: username
                    password: password
                  domains:
                    - domain: scaledmail.net
                      first_name: Dean
                      last_name: Fiacoo
                      redirect: scaledmail.com
                      profile_picture: link.com
                    - domain: scaledmail.us
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.org
                      first_name: Dean
                      last_name: Fiacoo
                    - domain: scaledmail.io
                      first_name: Dean
                      last_name: Fiacoo
                summary: Profile Picture
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
      x-apidog-folder: Order
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-18334152-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
