# Using webhooks

## Overview <a href="#overview-0" id="overview-0"></a>

Webhooks are a way for one service to send real-time updates or data to another service automatically, without any need for the user to check for new information manually. They work like a notification system, instantly alerting the receiving system when something happens in the sending system.

Webhooks are an easy way to get proactive alerts or notifications on events that are happening within Lob, including the tracking events we receive from the USPS. ([See full list of events here](https://docs.lob.com/#tag/Webhooks).) Some common use cases for integrating webhooks are:

* Receiving notification of improperly submitted mailpieces that fail to be rendered by Lob.
* Downloading PDF previews or thumbnails automatically once they are rendered
* Sending end-users notifications about mail traveling through the postal stream as a part of an omnichannel approach
* Triggering specific downstream workflows and actions based on the final receipt confirmation of mail with the "Delivered" event
* Receiving notifications about erroneous scan events, such as "Re-Routed" or "Returned to Sender"
* Internal logging and reconciliation

When an [event](https://docs.lob.com/#tag/Events) occurs within our architecture and you have a webhook subscribed to that event type in that environment (Test vs. Live), we will attempt to make a `POST` request with the [entire event object](https://docs.lob.com/#event_object) to the URL provided.&#x20;

## Subscribing to a webhook in the Lob dashboard <a href="#receiving-a-webhook-1" id="receiving-a-webhook-1"></a>

1. Select Webhooks from the left navigation bar.&#x20;
2. Choose Test or Live environment and click 'Create.'

{% hint style="info" %}
In Live mode, you can only have as many non-deleted webhooks as allotted in your current [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions). There is no limit in Test mode.
{% endhint %}

3. Add the webhook name in the ‘Description’ field.
4. Indicate the URL of the web server that will [receive the webhook](#receiving-a-webhook-1-1).
5. Edit your [rate limit ](#rate-limits-5)as applicable.
6. Select your event type. (See [here](https://docs.lob.com/#all_event_types) for a full list of all available event types.)

* For example, if you are setting up a webhook to be notified any time a postcard gets re-routed in the delivery process, then select the “postcard.re-routed” event type from the Postcards section.

7. Save the webhook by clicking on the 'Create' button.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FDkWJV6F0zffc1CVqzB59%2Fsubscribe_webhook.png?alt=media&#x26;token=87407eef-3f0d-43c8-bed4-cb1e54f53d66" alt="" width="563"><figcaption></figcaption></figure>

Once created you can click on any webhook in your menu to access Webhook Details page to view summary information and webhook attempts. Here you can also replay events, debug, edit, or delete the webhook.

## Receiving a webhook <a href="#receiving-a-webhook-1" id="receiving-a-webhook-1"></a>

To receive webhooks from Lob, you need to create another endpoint on your web server that will accept a `POST` request with a content type of `application/json`. Keep in mind that it will need to be accessible by Lob, so if there's anything that could prevent Lob from access, it should be disabled for this endpoint. See our recommendations on [securing your endpoint](#security-9) below.

To confirm delivery of the webhook, Lob expects a `2xx` status code returned in a timely manner. We will consider any other status code (or lack of status code) to be erroneous and attempt to retry the delivery. If your webhook endpoint has any additional complex logic to perform, we recommend immediately returning a `2xx` to let Lob know that you do not want to receive this event again, and then performing that logic afterwards. This should aid in preventing unwanted retry attempts caused by unexpected network timeouts.

Any other information sent back to Lob in the response will be captured and stored (regardless of status code) for you to view on your Dashboard, though we won't perform any processing on it. Therefore, we recommend responding with any information that you may find useful for debugging purposes. While you can return anything (including HTML), we've found it most helpful to return a concise JSON object with anything that could be relevant.

**Lob will send webhook events as soon as they become available. However, customers should not assume all webhooks will be sent in real-time, and may occasionally experience some delays.**&#x20;

For example when subscribing to the `postcard.processed_for_delivery` event, you will receive a response with the previous tracking events such as `postcard.in_local_area`, `postcard.in_transit`, `postcard.mailed`.&#x20;

{% hint style="info" %}
Although events may not be sent in real-time, for tracking events you can get the USPS timestamp of the event under `tracking_events[].time`.
{% endhint %}

## Webhooks JSON schema <a href="#webhooks-json-schema-2" id="webhooks-json-schema-2"></a>

Our mailpiece creation API responses contain unredacted information about your mailpiece. With each webhook sent for a given mailpiece, Lob redacts fields that could potentially contain Personally Identifiable Information (PII) or Protected Health Information (PHI). Fields that will be redacted include:

**For all mail formats:**

* “`From`” address for all form factors & events
* “`To`” address for all form factors & events
* Mailpiece URLs
* Metadata
* Description
* Merge variables

**For Checks only:**

* “`Memo`” field
* Everything in the “`Bank Account`” property (routing, account number, bank name, etc)

To preview what a sample redacted payload will look like, select “Webhooks” from the left-hand navigation menu in the dashboard, then select the “Debugger” button on the Webhook dashboard or individual webhook subscription page.

You can then select the “Event Object” tab at the bottom of the screen to see what information will be redacted.

<figure><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1649313614969-1649313614969.png" alt=""><figcaption></figcaption></figure>

\
Below is an example webhook response:

```json
{
  "event_type": {
    "resource": "self mailers",
    "enabled_for_test": true,
    "id": "self_mailer.rendered_thumbnails",
    "object": "event_type"
  },
  "reference_id": "sfm_c29bbbca5f7bd489",
  "date_created": "2021-12-16T01:34:18.159Z",
  "id": "evt_d47ff1b815373f67",
  "body": {
    "id": "sfm_c29bbbca5f7bd489",
    "description": "self mailer create",
    "metadata": {
      "secretId": "REDACTED",
      "subObject": {
        "subId": "REDACTED"
      }
    },
    "to": {
      "id": "REDACTED",
      "description": "REDACTED",
      "name": "REDACTED",
      "company": "REDACTED",
      "phone": "REDACTED",
      "email": "REDACTED",
      "address_line1": "REDACTED",
      "address_line2": "REDACTED",
      "address_city": "REDACTED",
      "address_state": "REDACTED",
      "address_zip": "REDACTED",
      "address_country": "REDACTED",
      "metadata": {
        "arrayTest": [
          "REDACTED",
          {
            "keyInArray": "REDACTED",
            "key2": "REDACTED"
          },
          {
            "keyInArray2": "REDACTED"
          }
        ]
      },
      "date_created": "REDACTED",
      "date_modified": "REDACTED",
      "deleted": "REDACTED",
      "object": "REDACTED"
    },
    "from": {
      "id": "REDACTED",
      "description": "REDACTED",
      "name": "REDACTED",
      "company": "REDACTED",
      "phone": "REDACTED",
      "email": "REDACTED",
      "address_line1": "REDACTED",
      "address_line2": "REDACTED",
      "address_city": "REDACTED",
      "address_state": "REDACTED",
      "address_zip": "REDACTED",
      "address_country": "REDACTED",
      "metadata": {},
      "date_created": "REDACTED",
      "date_modified": "REDACTED",
      "deleted": "REDACTED",
      "object": "REDACTED"
    },
    "url": "REDACTED",
    "outside_template_id": null,
    "inside_template_id": null,
    "inside_template_version_id": null,
    "outside_template_version_id": null,
    "carrier": "USPS",
    "tracking_events": [],
    "thumbnails": [
      {
        "small": "REDACTED",
        "medium": "REDACTED",
        "large": "REDACTED"
      },
      {
        "small": "REDACTED",
        "medium": "REDACTED",
        "large": "REDACTED"
      }
    ],
    "merge_variables": "REDACTED",
    "size": "6x18_bifold",
    "mail_type": "usps_first_class",
    "expected_delivery_date": "2021-12-27",
    "target_delivery_date": null,
    "date_created": "2021-12-16T01:34:12.087Z",
    "date_modified": "2021-12-16T01:34:14.469Z",
    "send_date": "2021-12-16T01:39:12.078Z",
    "object": "self_mailer"
  },
  "object": "event"
}
```

Fields that may contain any sensitive PII/PHI information will be redacted by default. However, you may adjust your redaction settings in your [Settings](https://dashboard.lob.com/settings/account) in the Lob dashboard under Account > "Webhooks Payload."

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Fk6zpkzDkNwYZiCkXTWvT%2Fimage.png?alt=media&#x26;token=53d6cd43-8d23-4e21-9472-03a48dba7921" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Lob is unable to retrieve any payload information retroactively during the time when this Webhooks Payload account setting is marked "Redacted."
{% endhint %}

## Test vs Live environment <a href="#test-vs-live-environment-3" id="test-vs-live-environment-3"></a>

Events are created in both your Test and Live Environment, and webhooks can also be created in both.&#x20;

* Webhooks created in the Test Environment will be triggered off events from your Test API Key

Because [tracking events](https://docs.lob.com/#tag/Tracking-Events) only exist in the Live Environment, these event types cannot be subscribed to in the Test Environment. If you are looking to debug these types of events, you can trigger a mock event to your server by using our [Debugger](https://dashboard.lob.com/#/webhooks/debugger) tool.

* Webhooks created in the Live Environment will be triggered off events from your Live API Key.

## Integration tips <a href="#integration-tips-4" id="integration-tips-4"></a>

When first starting out, we recommend using our [Debugger tool](https://dashboard.lob.com/#/webhooks/debugger). This allows you to trigger a generated event body to your specified URL on command. This should mainly be used to determine JSON structure when integrating. Since the event bodies sent are fake, all IDs and URLs within them are inaccessible and do not map to real resources in your account.

Once you've started local development of the web server that will be handling these requests, we recommend using a tool that provides local tunneling, such as [ngrok](https://ngrok.com/). This allows you to expose your locally running server to the Internet so we can access it without you needing to deploy your application.

## Webhook rate limits <a href="#rate-limits-5" id="rate-limits-5"></a>

If your server or gateway has an associated rate limit, or if you would like to control the speed at which Lob sends you webhooks for any other reason, you can configure the rate limit for each webhook subscription.

To do this, Account Administrators can go to the [webhook dashboard](https://dashboard.lob.com/webhooks) and either: (1) enter the rate limit when [creating a new webhook](#receiving-a-webhook-1) or (2) select an existing webhook subscription to modify the rate limit. Click the “Edit” button on the right-hand side of the screen, and enter your desired rate limit (per 5-second interval) and click “Update.” This change will take effect immediately.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F9t2VnnJt0yADfFmnMr8r%2FEdit_webhook.png?alt=media&#x26;token=f0242622-7944-435e-bbf8-2db4604eddb9" alt=""><figcaption></figcaption></figure>

## Replaying webhooks <a href="#replaying-webhooks-6" id="replaying-webhooks-6"></a>

Sometimes, a change or issue in your internal environment may cause a webhook subscription to begin failing. Once the issue is resolved, you can replay failed webhooks easily through the dashboard.&#x20;

To replay events, account admins can select a webhook subscription on the [webhooks dashboard](https://dashboard.lob.com/webhooks) to modify. Select the “Replay Events” button on the right-hand side of the screen. Enter a start date and click “Replay Events.” All non-`2XX` events will be queued to replay between the date selected and now.&#x20;

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FIOQ9hZgcj0d7KmYGlRd2%2Freplay_webhook.png?alt=media&#x26;token=deac1343-7cfc-40f1-b87b-13ceb8831f2c" alt=""><figcaption></figcaption></figure>

## Retry policy <a href="#retry-policy-7" id="retry-policy-7"></a>

When webhook attempts executed by Lob do not succeed (e.g. do not receive a `2xx` status code, hit a SSL/TLS error, DNS issue, etc), we will continue to try to deliver the same event according to a schedule with an increasing backoff. This policy is meant to give you time to rectify the issue without losing any events.

We will reattempt at the following intervals until we either receive a `2xx` status code or all attempts below have been executed:

<table><thead><tr><th width="133.86471068267818">Attempt #</th><th width="192.2714526853374">Time since last attempt</th><th width="178.43973090362823">Time since first attempt</th><th>Example</th></tr></thead><tbody><tr><td>1</td><td>Immediately</td><td>0 min</td><td>2022-01-01T00:00:00Z</td></tr><tr><td>2</td><td>5 sec</td><td>5 sec</td><td>2022-01-01T00:00:05Z</td></tr><tr><td>3</td><td>5 min</td><td>~5 min</td><td>2022-01-01T00:05:05Z</td></tr><tr><td>4</td><td>30 min</td><td>~35 min</td><td>2022-01-01T00:35:05Z</td></tr><tr><td>5</td><td>2 hr</td><td>~2 hr 35 min</td><td>2022-01-01T02:35:05Z</td></tr><tr><td>6</td><td>5 hr</td><td>~7 hr 35 min</td><td>2022-01-01T07:35:05Z</td></tr><tr><td>7</td><td>10 hr</td><td>~17 hr 35 min</td><td>2022-01-01T17:35:05Z</td></tr><tr><td>8</td><td>10 hr</td><td>~27 hr 35 min</td><td>2022-01-02T03:35:05Z</td></tr></tbody></table>

After the 8th attempt, we will not attempt to deliver the webhook again. If all of your webhooks for a single subscription fail for 5 consecutive days, the subscription will be disabled.

## Disabling policy <a href="#disabling-policy-8" id="disabling-policy-8"></a>

If your webhook endpoint does not consistently respond with a `2xx` status code, we will automatically disable the webhook and stop sending events to the endpoint. Webhooks are automatically disabled after 5 consecutive days of failures. The “clock” starts after the first failure and a single successful webhook to a given endpoint will reset the clock. You will receive an email notification when the webhook has been disabled.

Disabled webhooks can be re-enabled in the [dashboard](https://dashboard.lob.com/#/webhooks) by editing the webhook.

## Security <a href="#security-9" id="security-9"></a>

We understand that security is an important concern when granting external access. You need to make sure that Lob is able to reach your endpoint without incurring the risk of accessibility to bad actors, so there are certain features that you can enable on your end to ensure this is possible.

### TLS <a href="#tls-10" id="tls-10"></a>

We enforce HTTPS for all webhook URLs. Securing your endpoint with TLS ensures all data being sent to and from your server is encrypted. Make sure that you're using a fully-chained certificate, or else the request will never make it to your server and the attempt will fail. To make sure they are fully-chained, you should use the [Debugger](https://dashboard.lob.com/#/webhooks/debugger) and see if the request successfully goes through.

### Webhook signatures <a href="#webhook-signatures-11" id="webhook-signatures-11"></a>

Lob webhooks include a signature to allow you to verify their authenticity. Verifying this signature within your webhook endpoints allows you to ensure that the webhooks originate from Lob and not from a third party.

Webhooks include `Lob-Signature` and `Lob-Signature-Timestamp` headers. `Lob-Signature` is generated by computing HMAC-SHA256 on a signature input and a secret. The signature input is generated by concatenating `Lob-Signature-Timestamp` (as a string), the `.` character, and the webhook request's JSON payload (as a string). The secret is unique for each webhook and can be found in the details page for the respective webhook in the dashboard.

A static, fixed secret is used for webhooks for requests sent out using the webhook debugger. In these cases, the secret used in generating the signature is the string `secret`.

{% hint style="warning" %}
When using Lob's webhook debugger and validating the Lob Signature for events sent via the debugger do not use the uniquely generated secret. Instead **use the word "secret"** as your secret.
{% endhint %}

The addition of the `Lob-Signature-Timestamp` in the headers and as the input to HMAC-SHA256 allows you to prevent users from performing replay attacks. In a replay attack, an attacker intercepts webhooks and retransmits them. By verifying that the signature is valid and the timestamp is within some tolerance (we recommend 5 minutes), you can ensure that the request is not an older request being duplicated by an attacker.

In order to verify the `Lob-Signature` and `Lob-Signature-Timestamp` headers, follow the steps below.

1. **Step 1: Prepare the signature input**\
   Concatenate the `Lob-Signature-Timestamp` (as a string), the `.` character, and the raw request body (as a string). \
   Note: any parsing/stringification done to the request body could potentially alter the original string, so it is recommended to always use the raw request body as-is.
2. **Step 2: Generate the expected signature**\
   Compute the HMAC with SHA-256 using the webhook secret from the dashboard as the key and the signature input as the message. Convert to a string in base-16, hexidecimal format.
3. **Step 3: Compare signatures**\
   Compare the expected signature with the `Lob-Signature` header. If the strings are equal, then the webhook is valid.
4. **Step 4: \[Optional] Check the timestamp**\
   If you are concerned about replay-attacks, check that `Lob-Signature-Timestamp` is not older than your tolerance.

### Basic authentication <a href="#basic-authentication-12" id="basic-authentication-12"></a>

You can also use Basic Authentication to guard your endpoint from public access. This can be used in addition to or instead of webhook signature verification. For the best level of security, we highly recommend verifying webhook signatures, rather than relying solely on HTTP Basic Authentication.

When creating your webhook, insert the username and password to the URL using the following format: `https://username:password@example.com/webhooks`. This will be converted on our end to the appropriate `Authorization` header when we make the request.

### CSRF <a href="#csrf-13" id="csrf-13"></a>

A common feature that is enabled by default for some frameworks is [cross-site request forgery](https://owasp.org/index.php/CSRF). This is a valuable security measure to ensure that authenticated users aren't performing actions that aren't intended. However, having it enabled on your webhook endpoint could prevent our events from being processed. Instead of disabling it completely, you should just exempt this endpoint from CSRF validation.

## API versions <a href="#api-versions-14" id="api-versions-14"></a>

We will always send events based on the [API Version on your account](https://dashboard.lob.com/#/settings/keys) at the time of event creation. If your account is set to an older API version but a request is sent with a [hard-coded header](https://docs.lob.com/#version), the Event generated will still be based on the API Version on your account at that time. Event objects in the past will not be updated if you upgrade your API Version - only subsequent events will follow the new Version's structure.

## Return envelope tracking <a href="#return-envelope-tracking-15" id="return-envelope-tracking-15"></a>

{% hint style="info" %}
For Enterprise edition customers, Lob offers access to return envelope tracking via webhooks for USPS Courtesy Reply Mail.
{% endhint %}

For [return envelopes with tracking](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letter-envelopes#return-envelope-tracking-4) enabled, once the envelope enters the mailstream and is scanned by the USPS, the customer can start receiving notifications to mail tracking events, which will be surfaced via webhooks.

The following is a list of mail tracking event labels and descriptions available:

* `Created`: Return envelope is first created (should be simultaneous with Letter creation)
* `In transit`: Return envelope is being processed at the entry/origin facility
* `In local area`: Return envelope is being processed at the destination facility
* `Processed for delivery`: Return envelope is greenlit for delivery at the end recipient's nearest postal facility. The mailpiece should reach the mailbox within 1 business day of this tracking event.
* `Re-routed`: Return envelope is re-routed due to recipient change of address, address errors, or USPS relabeling of barcode/ID tag area
* `Returned to sender`: Return envelope is undeliverable and is being returned to sender due to barcode, ID tag area, or address errors.

Return envelope tracking is currently only accessible via Lob webhooks, and the Event Logs node in the Lob dashboard. Tracking events will appear in the `Letters` Events portion of the original individual mail piece in the dashboard as soon as they become available, or can be downloaded using the “Export” button that’s located at the top of the Letters section in the dashboard.

### View tracking events for return envelopes <a href="#view-tracking-events-for-return-envelopes-16" id="view-tracking-events-for-return-envelopes-16"></a>

Enterprise edition customers can now access [return envelope tracking](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letter-envelopes#return-envelope-tracking-4) for USPS Courtesy Reply Mail (for letters only). Once the returned mail piece enters the mailstream, the customer can start receiving notifications to tracking events via our webhooks.&#x20;

&#x20;You can view your return envelope tracking events by setting up your webhooks:

1. Log into your [dashboard](https://dashboard.lob.com/)
2. Filter to [return envelope tracking events](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letter-envelopes#return-envelope-tracking-4) via API Requests > Event Logs tab
3. Select the tracking event of interest for return envelopes
   1. Click on Filters at the left top
   2. Select Letters under Resources dropdown
   3. Select the event types you'd like to view (starts with `letter.return_envelope`) and hit Apply<br>

      <figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FHKGGTvBpn3NzBveuehEZ%2Fletter.return_envelope.png?alt=media&#x26;token=2bedeafa-d204-4ce7-9204-a8db9ecb0499" alt=""><figcaption></figcaption></figure>
   4. Select a return envelope tracking event to reveal more details about associated mail piece

      <figure><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1635806456397-1635806456397.jpeg" alt=""><figcaption></figcaption></figure>