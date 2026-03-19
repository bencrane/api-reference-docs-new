# Measuring attribution

Marketing attribution is important in measuring performance for any channel, online or offline, because it helps to understand the specific impact of any certain content that is driving lead conversions, and thus driving revenue. In the context of multi-channel campaigns, direct attribution allows you to know for certain whether a direct mail touch was the one that drove a conversion.&#x20;

Traditional channels are historically challenging to target and measure, with direct mail being an 'Exhibit A' example of this issue. However, as a modern direct mail platform, Lob offers various approaches to measure attribution as best possible and to provide greater visibility in a rather opaque channel.&#x20;

## Embedding customized CTAs&#x20;

Similar to email, direct mail campaigns can measure direct attribution by creating a customized call-to-action CTA that's unique to the end-recipient of the mail piece. This can be a [URL](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/short-urls), coupon code, phone number, or [QR code](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/adding-qr-codes). Ideally, each CTA should be as dynamically generated and unique as possible, and can be tracked individually if it is followed. If not down to the individual level, creating unique CTAs for each campaign (or cohorts within it) would allow a better understanding of how specific campaigns or cohorts are driving better conversions. &#x20;

## Triggering downstream workflows with webhooks &#x20;

[Webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks) allow real-time notifications of mail status for individual mail pieces (generated in the form of [tracking events](https://help.lob.com/print-and-mail/getting-data-and-results/tracking-your-mail)) as it progresses through the USPS mailstream. The two most impactful scanned events are the "Processed for Delivery" and "Delivered" events, which means that a USPS courier is about to deliver mail within the next day, or has successfully delivered the mail piece, respectively. If you have a multichannel campaign in progress, you can design for either of these events to trigger an additional sequence of events downstream, such as reinforcement reminders using other digital channels, a limited-time-only action, or some other action or acknowledgment that's unique to your business workflow.&#x20;

These webhooks and ensuing downstream triggers can indirectly impact your mail piece's broader success or conversion, along with the overall campaign involving the direct mail touch.&#x20;

## Assigning metadata to retrieve data

[Metadata](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/using-metadata) can be used to identify, locate, and "tag" mail pieces or particular campaigns. While metadata is not directly responsible for attribution, appropriately tagging mail pieces is a critical step in measuring attribution at a more granular level.&#x20;

Learn more about [metadata](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/using-metadata) and how it can help measure conversion and attribution through various ways of tagging in our Lob systems.

## Lob engagement analytics

Engagement metrics provide insights into what content resonates with which audiences; this is essential to optimizing your campaigns (so you can do more of what works!)&#x20;

Include [Lob-generated QR Codes](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/adding-qr-codes) on your mailpieces to view engagement analytics in the following ways:

* In the Lob dashboard: Under the Mail Analytics section, see the [Engagement](https://help.lob.com/print-and-mail/mail-analytics#engagement) tab for an aggregate view. Or, view [campaign-specific analytics](https://help.lob.com/send-mail/launch-your-first-campaign#campaign-analytics) on any individual campaign's detail page, under QR Code Engagement.
* Via API: Receive detailed analytics via our [QR Analytics endpoint](https://docs.lob.com/#tag/QR-Codes).