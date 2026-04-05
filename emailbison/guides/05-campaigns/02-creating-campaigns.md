# Creating Campaigns

**URL:** https://docs.emailbison.com/campaigns/creating-campaigns

This page will walk you through creating a campaign from the API.

**Creating a Campaign:**
Send a POST request to `/api/campaigns`. You must pass 1 body parameter, name, which corresponds to the name of the campaign you wish to create. If successful, you will receive a 200 OK with the campaign ID as part of the response.

**Campaign Settings:**
You can get the ID for a campaign using the UI by navigating to the campaign, clicking on the Actions dropdown, and then clicking Copy ID for API. Alternatively, campaign IDs can be acquired with a GET request to `/api/campaigns`. Each campaign has individual settings that can be changed. You can view the settings with a GET request to `/api/campaigns/{id}` where {id} is the campaign ID.

If you need to change the settings, send a POST request to `/api/campaigns/{id}/update` where {id} is the campaign ID.

This request takes a JSON body with the following fields:
- **max_emails_per_day** (integer|null, default: "1000") - The maximum number of emails that can be sent per day
- **max_new_leads_per_day** (integer|null, default: "1000") - The maximum number of new leads that can be added per day
- **plain_text** (boolean|null, default: "false") - Whether the email content should be plain text
- **open_tracking** (boolean|null, default: "false") - Whether open tracking should be enabled
- **reputation_building** (boolean|null, default: "false") - Spam protection
- **can_unsubscribe** (boolean|null, default: "false") - Whether recipients can unsubscribe using a one-click link
- **unsubscribe_text** (string|null) - The text that will be shown in the unsubscribe link

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/{id}/update' \
  --request PATCH \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "max_emails_per_day": 500,
    "max_new_leads_per_day": 100,
    "plain_text": true,
    "open_tracking": true,
    "reputation_building": true,
    "can_unsubscribe": true,
    "unsubscribe_text": "Click here to unsubscribe"
  }'
```

**Campaign Schedule:**
If you have created a schedule for a campaign in the past, you can re-use it provided you've saved it as a template. If you have a schedule template you wish to use: Get the schedule ID by sending a GET request to `/api/campaigns/schedule/templates`. Once you've acquired the ID, send a POST to `/api/campaigns/{campaign_id}/create-schedule-from-template`. The request requires 1 body field, schedule_id.

If you don't have a schedule template you wish to use: send a POST request to `/api/campaigns/{campaign_id}/schedule`.

JSON body fields for schedule:
- **monday** (boolean, required)
- **tuesday** (boolean, required)
- **wednesday** (boolean, required)
- **thursday** (boolean, required)
- **friday** (boolean, required)
- **saturday** (boolean, required)
- **sunday** (boolean, required)
- **start_time** (string, required) - The start time in HH:MM format. Example: 09:00
- **end_time** (string, required) - The end time in HH:MM format. Example: 17:00
- **timezone** (string, required) - The timezone of the schedule (full list of timezone strings available in docs, e.g., "America/New_York", "America/Los_Angeles", "Europe/London", etc.)
- **save_as_template** (boolean, required) - Whether the created schedule should be saved as template

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/{campaign_id}/schedule' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "monday": true,
    "tuesday": true,
    "wednesday": true,
    "thursday": true,
    "friday": true,
    "saturday": false,
    "sunday": false,
    "start_time": "09:00",
    "end_time": "17:00",
    "timezone": "America/New_York",
    "save_as_template": false
  }'
```

**Campaign Sequence:**
The sequence of the campaign is the emails that will be sent out. To create your sequence, send a POST request to `/api/campaigns/{campaign_id}/sequence-steps`. The request can take only 2 fields in the body JSON: title and sequence_steps. title is a string, and sequence_steps is an array with the following fields:

- **title** (string, required) - The title of the sequence
- **email_subject** (string, required) - The subject of the email. To include variables, type them in uppercase and wrap them with curly braces. Example: "This is an email subject with a {VARIABLE}."
- **email_body** (string, required) - The body of the email. Variables same as above.
- **wait_in_days** (integer, required) - How many days before the sequence moves to the next step
- **variant** (boolean|null) - Whether the step is a variant
- **variant_from_step** (integer|null) - Required if variant is true. The ID of the step this step is a variant of.
- **thread_reply** (boolean, required) - Whether the step should be a reply from the previous step

Example:
```
curl 'https://dedi.emailbison.com/api/campaigns/{campaign_id}/sequence-steps' \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_SECRET_TOKEN' \
  --data '{
    "title": "test sequence",
    "sequence_steps": [
      {
        "email_subject": "Hey {FIRST_NAME}",
        "order": 1,
        "email_body": "You should check this {PRODUCT} out!",
        "wait_in_days": 1,
        "variant": true,
        "variant_from_step": 223
      },
      {
        "email_subject": "EmailBison is awesome!",
        "order": 2,
        "email_body": "Try it now!",
        "wait_in_days": 1,
        "variant": true,
        "variant_from_step": 1,
        "thread_reply": true
      }
    ]
  }'
```

**Launching Campaign:**
After creating a campaign, updating its settings, creating or choosing a schedule, and creating a sequence, you have completed all the necessary steps in creating a campaign. You can send these requests to check the details of a campaign:
- `GET /api/campaigns/{campaign_id}`: retrieves the campaign you created and its settings.
- `GET /api/campaigns/{campaign_id}/schedule`: retrieves the campaign schedule.
- `GET /api/campaigns/{campaign_id}/sequence-steps`: retrieves the campaign sequence steps.

Once you're ready to launch your campaign, send a PATCH request to `/api/campaigns/{campaign_id}/resume`. You can pause the campaign by sending a PATCH request to `/api/campaigns/{campaign_id}/pause`.
