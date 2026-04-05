# Attaching Leads to Untracked Replies

**URL:** https://docs.emailbison.com/master-inbox/attaching-leads-to-untracked-replies

Untracked replies in the master inbox will show up with a button to Attach Contact. This action can be done on a larger scale using the API.

**Getting all scheduled emails for a lead:**
Send a GET request to the following endpoint: `/api/scheduled-emails/{lead_id_or_email}`

**Attaching scheduled emails to a reply:**
Once you have the scheduled email IDs you can attach them to replies with their ID. Send a POST request to the following endpoint: `/api/replies/{reply_id}/attach-email-to-reply`

The following are the parameters for the request:
- **scheduled_email_id** (integer, required) - The ID of the scheduled email you want to attach to the reply.
