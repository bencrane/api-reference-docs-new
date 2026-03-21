# Remove Leads from Campaign

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: EmailBison API
  description: ''
  version: 1.0.0
paths:
  /api/campaigns/{campaign_id}/leads:
    delete:
      summary: Remove leads from a campaign
      description: >-
        This endpoint allows the authenticated user to remove leads from a
        campaign.

        **Hold on. You may not need to remove leads!**

        Please read carefully before attempting to delete.

        **I mapped the wrong custom variables for these leads**

        No problem! Simply re-upload the leads and we'll update the records in
        place. This is especially useful if you already have lead history like
        conversations, campaigns, etc.

        **I don't want to email these leads in this campaign anymore**

        You can simply click "stop future emails" instead.

        If you want to stop them from being emailed in any campaign, we recommend
        unsubscribing these leads instead. Bulk select -> Update Status ->
        Unsubscribe. This way, you can preserve the lead history and stats for
        future reports.

        **I want to update these leads with more data**

        Instead of deleting, simply re-upload the leads. We'll update the records
        in place. This includes all campaign emails too. If you delete, their
        history in this campaign will be reset.

        **If you still want to remove them from the campaign, please read
        carefully below.**

        - All future scheduled emails in this campaign will be stopped (for these
        leads). Your leads will no longer receive future emails from this campaign.

        - Existing campaign stats (for these leads) will be retained. You will
        still be able to pull data from this campaign for all past stats.

        - Lead conversations will remain. You will still be able to continue lead
        conversations through the master inbox.

        - These leads will no longer be accessible via API (for this campaign).

        - Future replies for these leads will not increment stats.

        - This action is permanent and cannot be reversed. If you removed these
        leads by accident and try to re-add them, the history will be totally
        reset.
      tags:
        - Campaigns
      operationId: removeLeadsFromACampaign
      parameters:
        - name: campaign_id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the campaign.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - lead_ids
              properties:
                lead_ids:
                  type: array
                  description: An array of lead IDs to remove.
                  example:
                    - 1
                    - 2
                    - 3
                  items:
                    type: integer
      responses:
        '200':
          description: success
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    example: true
                  message:
                    type: string
                    example: Leads successfully removed from Campaign One.
              example:
                success: true
                message: Leads successfully removed from Campaign One.
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
