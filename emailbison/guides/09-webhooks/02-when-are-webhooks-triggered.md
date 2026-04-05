# When are Webhooks Triggered

**URL:** https://docs.emailbison.com/webhooks/when-are-webhooks-triggered

On this page you will find all the webhooks available in EmailBison, and their trigger conditions.

- **Email Sent** - Triggered only when a campaign email is sent.
- **Manual Email Sent** - Triggered only when a manual email sent. This includes replying and composing new emails -- both from the master inbox or the API.
- **Contact First Emailed** - Triggered only when a contact received the first campaign email on this workspace.
- **Contact Replied** - Triggered every time a lead that was emailed from a campaign replies. Will not trigger if the campaign the lead is in has the setting Include auto replies in stats is toggled off and it is an automated reply.
- **Contact Interested** - Will trigger if a reply gets marked as interested through the master inbox, the API, or automatically if Auto AI categorization is toggled on in the general master inbox settings.
- **Contact Unsubscribed** - Triggered when a lead is unsubscribed from campaigns.
- **Untracked Reply Received** - Triggered when a new email or a reply is received, and it is not associated with a scheduled email that was sent from a campaign.
- **Email Opened** - Triggered when an email is opened, this needs the campaign to have track opens toggled on.
- **Email Bounced** - Triggered when a campaign email bounces.
- **Email Account Added** - Triggered every time a sender email is connected for the first time.
- **Email Account Removed** - Triggered every time a sender email is removed (deleted).
- **Email Account Disconnected** - Triggered every time a sender email is disconnected. This will also trigger if it is a Microsoft account and the refresh token has expired.
- **Email Account Reconnected** - Triggered every time a sender email is reconnected, after it has been disconnected.
- **Tag Attached** - Triggered every time a custom tag is attached to a taggable (lead, sender email, or campaign). This will send one webhook per tag attached, per taggable.
- **Tag Removed** - Triggered every time a custom tag is removed from a taggable (lead, sender email, or campaign). This will send one webhook per tag removed, per taggable.
- **Warmup Disabled Causing Bounces** - Triggered when warmup for a sender email was disabled for causing too many bounces.
- **Warmup Disabled Receiving Bounces** - Triggered when warmup for a sender email was disabled for receiving too many bounces.
