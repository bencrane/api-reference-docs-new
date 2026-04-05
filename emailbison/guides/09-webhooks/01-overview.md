# Webhooks Overview

**URL:** https://docs.emailbison.com/webhooks/overview

A webhook is an HTTP request that is automatically sent by a source of data when an event is triggered. In this case, the source of data is your EmailBison instance. EmailBison provides you with many events to trigger a webhook request. To view all the events available, navigate to Settings -> Webhooks -> New Webhook URL. The different events contain sample payloads under the toggle for you to preview the data sent.

**Sending Test Events:** To test your automations, you can send a test webhook natively in app by navigating to Settings -> Webhooks -> New Webhook URL or click Edit on a webhook, and then click on Send test webhook. You can also send a test event through the API by sending a POST request at the following endpoint: `/api/webhook-events/test-event`
