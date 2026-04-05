# Campaigns Overview

**URL:** https://docs.emailbison.com/campaigns/overview

Campaigns orchestrate the emails that will be sent, who they will be sent to, and when they will be sent.

**Campaign Scheduler:** The campaign scheduler will run and schedule emails to be sent out every time the campaign is resumed, as well as at the end of every sending day for the campaign. If you need to manually run the campaign scheduler before the end of the sending day, you can pause and resume the campaign.

**Smart Scheduling:** EmailBison uses a smart scheduling pattern to avoid automation detection. Campaign emails are sent on a random pattern throughout your sending window -- decided by the campaign's schedule.

**ESP Matching:** EmailBison takes an unopinionated approach to ESP matching. It is left to the user to decide if ESP matching or mis-matching is better for their deliverability. EmailBison provides you with the tools to achieve this by tagging every lead with their ESP.

**Relationship between Leads and Sender Emails:** Once a lead has been sent an email in a campaign, the same Sender Email will send the remaining steps for that lead, as well as emails sent to the lead from a followup campaign.
