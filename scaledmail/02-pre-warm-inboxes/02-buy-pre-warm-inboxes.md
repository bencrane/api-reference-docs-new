# Buy Pre Warm Inboxes

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /api/v1/buy-pre-warm-inboxes:
    post:
      summary: Buy Pre Warm Inboxes
      deprecated: false
      description: >-
        ### ⚠️ Requires a connected payment method



        A **subscription and pre‑warm inboxes will be created automatically** if
        available, once the request is successful.


        If **pre‑warm inboxes are available**, the system will automatically
        purchase and assign them to the provided domains.


        ---


        ## 📥 Request Body Parameters


        All parameters below must be sent in the **JSON body**.


        ---


        ### **`tag`** (optional)


        A custom tag to associate with this purchase.


        * Example: `"dnsimple_test"`

        * Can be used for internal tracking


        ---


        ### **`domains`** (required)


        An **array of domain objects** to be used for pre‑warm inbox creation.


        → If any domain is invalid or unavailable, the request will fail.


        Each domain object supports:


        #### **`id`** (required)


        The internal domain record ID.


        Example:


        ```json

        "id": "recscFIvHSqKwxfyp"

        ```


        #### **`domain`** (required)


        The domain name.


        Example:


        ```json

        "domain": "example.com"

        ```


        #### **`redirect`** (optional)


        A redirect URL for the domain.


        Example:


        ```json

        "redirect": "https://example.com"

        ```


        ---


        ### **`sequencer`** (optional)


        Used to automatically connect the purchased pre‑warm inboxes to an
        **email sequencer**.


        If provided, the system will configure the sequencer after inbox
        creation.


        Example structure:


        ```json

        "sequencer": {
          "provider": "Instantly",
          "username": "ross@instantly.ai",
          "password": "InstantlyRoss456!",
          "link": "https://app.instantly.ai",
          "workspace": "paleontology-outreach",
          "tag": "{{ID}}"
        }

        ```


        #### Sequencer Fields


        | Field       | Required | Description                           |

        | ----------- | -------- | ------------------------------------- |

        | `provider`  | ✅        | Sequencer provider (e.g. `Instantly`) |

        | `username`  | ✅        | Sequencer account username            |

        | `password`  | ✅        | Sequencer account password            |

        | `link`      | ✅        | Sequencer dashboard URL               |

        | `workspace` | ❌        | Workspace or account name             |

        | `tag`       | ❌        | Tag to apply inside the sequencer     |


        ---


        ### 🔖 Sequencer Tag Behavior


        If the sequencer `tag` is set to:


        ```json

        "tag": "{{ID}}"

        ```


        → The system will **automatically replace `{{ID}}`** with the **payment
        ID** generated during checkout.

        → That payment ID will be used as the **tag inside the sequencer**.


        ---


        ## 🧠 Behavior Summary


        * `tag` → optional, used for tracking

        * `domains` → required

        * `redirect` → optional per domain

        * `sequencer` → optional

        * If pre‑warm inboxes are available → they will be **automatically
        purchased and assigned**

        * If `sequencer.tag = "{{ID}}"` → payment ID will be injected
        automatically


        ---
      tags:
        - Pre Warm Inboxes
      parameters:
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
            example: |
              {
                "tag": "client1",
                "domains": [
                  {
                    "id": "recscFIvHSqKwxfyp",
                    "domain": "1apitestoutlook.com",
                    "redirect": "bello.com"
                  },
                  {
                    "id": "recLuIthqG59R4nmZ",
                    "domain": "1apitestgoogle.com"
                  }
                ]
                "sequencer": {
                  "provider": "Instantly",
                  "username": "ross@instantly.ai",
                  "password": "InstantlyRoss456!",
                  "link": "https://app.instantly.ai",
                  "workspace": "paleontology-outreach",
                  "tag": "{{ID}}"
                }
              }
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
      x-apidog-folder: Pre Warm Inboxes
      x-apidog-status: released
      x-run-in-apidog: https://app.apidog.com/web/project/925867/apis/api-26625050-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers: []
security: []

```
