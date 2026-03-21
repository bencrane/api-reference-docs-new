# Delete Lead

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/leads/{lead_id}:
    delete:
      summary: Delete a lead
      deprecated: false
      description: >-
        Permanently delete a lead and its associated data.


        **Hold on. You may not need to delete leads.** You may be able to simply re-upload leads instead.


        **I mapped the wrong custom variables for these leads** -
        No problem! Simply re-upload the leads and we'll update the records in place. This is especially useful if you already have lead history like conversations, campaigns, etc.


        **I don't want to email these leads anymore** -
        We recommend unsubscribing these leads instead. Bulk select -> Update Status -> Unsubscribe. This way, you can preserve the lead history and stats for future reports.


        **I want to update these leads with more data** -
        Instead of deleting, simply re-upload the leads. We'll update the records in place. This includes all campaign emails too.


        **I attached the wrong tags** -
        You can simply bulk select and remove tags instead of deleting the entire leads.


        **I don't want to use too much data** -
        We have no limits on lead storage. You can store as many leads as you want. We recommend keeping the leads in your workspace for future campaigns.


        **Why is it recommended to not delete leads?** -
        We build up history for every lead record you upload. There's no harm in keeping it in the workspace. If you delete leads, future responses from that lead will be untracked and not tied to any campaigns. This can be harder to manage for your team.


        **If you still want to delete leads, please read below carefully:**


        - Leads will be removed from campaigns. This will stop all future emails for the selected leads and remove them from all campaigns.

        - Previous campaign stats will be preserved.

        - Past and future lead conversations will be affected. Past conversations will no longer be tied to these leads.

        - Leads will no longer be accessible via API.

        - Future campaign stats will not be tracked.

        - We recommend unsubscribing these leads instead.
      tags:
        - Leads
      parameters:
        - name: lead_id
          in: path
          required: true
          schema:
            type: integer
          description: 'The ID of the lead to delete.'
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
                        example: 'Lead deletion process started. This might take some time depending on how much data you have.'
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
