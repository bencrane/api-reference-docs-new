# One-time campaigns or triggered sends?

## One-time campaigns

A common approach to sending direct mail is to send a single, large campaign to a target audience.&#x20;

**At Lob,** **a "one-time" campaign is a one-to-many method of mail distribution to a broad audience using a single set of mailing instructions.**&#x20;

{% hint style="success" %}
Popular use cases for one-time campaigns include sending acquisition or cross-sell mailers, retail promotions, annual policy updates, end-of-life notices for a sunsetting product, referral campaigns, etc.&#x20;
{% endhint %}

Traditionally, sending a campaign meant negotiating RFPs for every project, long lead times with lots of back-and-forth with the printer, imperfect audience lists, and use of generic creatives that lacked personalization, if any.&#x20;

With Lob, you can create campaigns using our flexible settings and guidance, choose from various delivery options, and apply dynamic personalization at unprecedented granular levels.&#x20;

One-time campaign execution is easy in the Lob Dashboard via [Campaigns](https://help.lob.com/print-and-mail/send-mail/launch-your-first-campaign), or programmatically via our [Campaigns API](https://help.lob.com/print-and-mail/send-mail/send-campaigns-via-the-campaigns-api).  &#x20;

<table data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><mark style="color:blue;"><strong>Send via the Lob Dashboard</strong></mark></td><td></td><td></td><td><a href="../send-mail/launch-your-first-campaign">launch-your-first-campaign</a></td><td><a href="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FQXS1kUWxq8QQ99VpP7FQ%2FScreenshot%202023-02-08%20at%204.00.50%20PM.png?alt=media&#x26;token=060498d2-8008-47f7-a843-23c8a7748c57">Screenshot 2023-02-08 at 4.00.50 PM.png</a></td></tr><tr><td><mark style="color:blue;"><strong>Send via Campaigns API</strong></mark></td><td></td><td></td><td><a href="../send-mail/send-campaigns-via-the-campaigns-api">send-campaigns-via-the-campaigns-api</a></td><td><a href="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F6ETFF3amovfuR5dvIz8e%2F0_ljyW1QItACx67HVd.jpeg?alt=media&#x26;token=0e1d2058-f6df-4880-9b77-4f8eef756fdb">0_ljyW1QItACx67HVd.jpeg</a></td></tr></tbody></table>

<details>

<summary>Campaign FYIs</summary>

* Some advanced campaign features or mail formats are only available to Enterprise-tier customers, and may have mail piece minimums to qualify for a campaign send.&#x20;
  * Letter add-ons (envelopes, cards, buckslips) must be ordered in advance and be fully stocked in your inventory in order for your campaign to be successfully sent
  * Target Delivery, cards or buckslips have different campaign send minimums&#x20;
* Some campaign-specific settings may override your account-level settings, such as merge variable strictness or cancellation windows
* You can send most domestic mail formats offered by Lob in Campaigns, except checks and extra service mailers (Certified & Registered Mail). No campaigns can be sent abroad.

</details>

## Automated campaigns (trigger-based)

Another common way to send direct mail is to individually dispatch mail, usually initiated by pre-programmed logic or event within an orchestration workflow.&#x20;

**"Triggered" mail is an automated process that sends mail to a single recipient when they meet a pre-set condition or take a defined set of actions within a certain timeline.**&#x20;

Lob refers to these event- or trigger-based campaigns as automated campaigns. &#x20;

{% hint style="success" %}
Popular triggered use cases include post-signup onboarding mail, abandoned cart recovery, order notices or monthly statements, product retargeting, and follow-up confirmations. &#x20;
{% endhint %}

Using Lob's single endpoint APIs, you can create a custom trigger automation from scratch, or take advantage of popular pre-built [API integrations](https://help.lob.com/print-and-mail/integrations/api-integrations) to connect to a platform you already use for your digital channels. Or for a less technical lift, you can automate your sends [directly from the Lob dashboard](https://help.lob.com/print-and-mail/integrations/no-code-integrations).

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>API integrations</strong></td><td></td><td></td><td><a href="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FUeQNvafIfcVfC2wH2Iyw%2Fexternal_integrations.png?alt=media&#x26;token=2596a320-258b-4e2e-80f9-f73048512633">external_integrations.png</a></td><td><a href="../integrations/api-integrations">api-integrations</a></td></tr><tr><td><strong>No-code integrations</strong></td><td></td><td></td><td><a href="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FFFo6XLWbdOR8BSGPndxq%2Finternal_integrations.png?alt=media&#x26;token=bb8dc3bd-3efc-4e80-9230-9c24f0e4fd4b">internal_integrations.png</a></td><td><a href="../integrations/no-code-integrations">no-code-integrations</a></td></tr></tbody></table>