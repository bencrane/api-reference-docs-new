# Mail analytics

## Overview <a href="#overview-0" id="overview-0"></a>

Our [Mail Analytics](https://dashboard.lob.com/analytics/mail-speed) feature in the Dashboard provides insights to empower you to fine-tune targeting, enhance engagement, and optimize the overall effectiveness of your direct mail campaigns. You can slice and dice your data by certain filters to view a full deliverability report, all directly from your Dashboard.

To access this feature, sign in to your Dashboard and click the "[Mail Analytics](https://dashboard.lob.com/analytics/)" tab in the left navigation bar.&#x20;

{% hint style="info" %}
We also offer [campaign-specific analytics](https://help.lob.com/send-mail/launch-your-first-campaign#campaign-analytics). Similar to the metrics below, these are visible from any Live campaign's details page.&#x20;
{% endhint %}

## Tracking events <a href="#tracking-events-3" id="tracking-events-3"></a>

Lob is the only intelligent platform that tracks each piece of mail as it moves through the USPS delivery process. This section gives you full visibility into where all the mail you've sent in any given time period sits in the mail stream. As you send higher volumes of mail with Lob, you may need to analyze the status and deliverability of your mail on a more aggregate basis.

The Tracking Events tab displays a visual breakdown of all tracking events applicable to the mail pieces within the filter parameters.&#x20;

{% hint style="success" %}
You can export all tracking events data into a CSV file; [see more details on exporting mail data here.](https://help.lob.com/print-and-mail/getting-data-and-results/exporting-mail-data)
{% endhint %}

### Tracking event stepper

The tracking stepper at the top of the dashboard displays the different stages in your mail's delivery process:

![Tracking stepper (Mail Analytics -> Tracking Events)](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FD8sVBUU7MmkGM8DzAD9l%2Ftracking_stepper_ananalytics.png?alt=media\&token=3a752909-615a-4c2a-914b-f8fc282ba3c3)

* **Sent:** This is a count of non-deleted mailings that you have sent to Lob in the specified time frame based on the date for which a piece was scheduled (the piece's `send_date`), not the date the API request was made.
* **In production:** Mail piece instructions were dispatched to Lob's printer network and the request is now being printed/cut, soon to be handed off to the USPS or a mail carrying partner for fulfillment.
* **Mailed\*:** This bucket is a count of all pieces that have received a [Mailed](#tracking-events-3) event, which represents handoff to USPS or a mail carrying partner. Access to "Mailed" Events is exclusive to certain customers. Upgrade to the appropriate [Print & Mail Edition ](https://dashboard.lob.com/#/settings/editions)to gain access.
* **In Mailstream**: This bucket is an aggregate of two tracking events, In Transit and In Local Area. These are the first two scans that a piece will receive—representing that it's in the mailstream and on the way to its destination.
* **Processed for Delivery:** This bucket is represents pieces that have received a Processed for Delivery scan. This scan means that the piece has been approved for delivery at the destination's nearest postal facility and will likely be delivered in 1-2 business days.
* **Delivered**: This bucket represents pieces that have received a Delivered scan, meaning they were delivered to the end recipient. The final scan is generated when the mail carrier's GPS unit leaves the delivery area.&#x20;
* **Re-Routed:** If a piece is re-routed due to recipient change of address, address errors, or USPS relabeling of barcode/ID tag area, it will receive this scan.
* **Returned to Sender:** A piece will receive a Returned to Sender scan if delivery was attempted, but failed due to barcode, ID tag area, or address errors.

Each mail piece will be counted once in each bucket for which it receives a scan. For example, if a letter has these tracking events:

* "In Transit"
* "In Local Area"
* "Processed for Delivery"

Then it will be counted once in the "Sent", "In Mailstream", and "Processed for Delivery" buckets.

### Reading the graph <a href="#reading-the-graph-6" id="reading-the-graph-6"></a>

Under the Tracking Event statistics on the dashboard, we also provide a graph that provides an even further breakdown of your mail by day, week, or month. Time periods are grouped by the date a piece was sent, not by the date of the API request. As with all other dates within the Lob system, the UTC time zone is used.

Hover over a specific column to view a full tracking breakdown for that time period. Use this breakdown to narrow down your data for even further analysis.

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Fc8JMVDG5PtyHZ9GErq2m%2FMA_tracking_events_graph.png?alt=media\&token=1479c54e-928b-4867-b4f0-ba09727fe253)

### Benchmarks <a href="#benchmarks-7" id="benchmarks-7"></a>

Over time, you can expect to see tracking events for 98-100% of your mailings. The numbers below are benchmarks for when you should start seeing scans. Keep in mind that these timings and percentages may vary based on the volume of mail you've sent, where you're sending to, and the quality of your address set.

For First Class mail, you'll start to see mailings reach the "In Mailstream" bucket in 2-3 business days and the "Processed for Delivery" bucket 1 business day afterward. After about 4 business days total, you should expect almost all of your mailings to be in the "In Mailstream" state. After about 5 business days total, almost all of your mailings should be in the "Processed for Delivery" state.

For Standard Class mail, which is inherently slower, the timing is a bit different. You'll start to see mailings reach the "In Mailstream" bucket in 4-5 business days and the "Processed for Delivery" bucket 2 business days afterward. After about 10-11 business days total, you should expect almost all of your mailings to be in the "In Mailstream" state. After about 12-13 business days total, almost all of your mailings should be in the "Processed for Delivery" state.

{% hint style="warning" %}
Certified and Registered letters are excluded from this dashboard because they are [tracked via their own external tracking numbers](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letters#certified-mail-electronic-return-receipts-5) with USPS.
{% endhint %}

<details>

<summary>The tracking data in my mail analytics dashboard doesn't seem right, what can I do? </summary>

**Tracking Events:** If you notice that the tracking events on your mail analytics dashboard are missing or not up to date, it is because USPS didn't scan the mailpieces. However, note that if USPS doesn't scan the mailpiece in the first place, then there is no way for Lob, to recover the tracking events to display on the dashboard as we receive this tracking information from USPS.&#x20;

**No 'Mailed' Event:** (Note, [Mailed](https://help.lob.com/print-and-mail/tracking-your-mail#mailed-tracking-event-details) event is an Enterprise feature only). It could be that these mail pieces were sent out as metered mail by USPS, which makes it unmeasurable in our system even though the mailpiece is en route to its destination.&#x20;

**Ingestion Issue:** Delay in receiving Tracking events data from USPS cause the tracking events data to not be reflected on the mail analytics dashboard. In these cases, once we receive the data from USPS we will backfill these events.&#x20;

**Certified Letters:** Only mail sent through First Class or Standard class mail will be displayed on the Dashboard. To see the current status of the letter, you would have to click on the USPS Tracking Number that USPS provides.

</details>

## Engagement

### QR Code Engagement

If you have sent any mail containing QR Codes, the next step is learning the engagement rates associated with these mailpieces. The [Engagement tab](https://dashboard.lob.com/analytics/attribution-analytics) will track how all mailpieces you’ve sent with QR Codes are performing over a selected period of time. (You can see QR engagement analytics for any [specific campaign](https://help.lob.com/send-mail/launch-your-first-campaign#campaign-analytics) on that campaign's detail/ status page.)

<figure><img src="https://lh7-us.googleusercontent.com/thp0x4R3uhkMjO3Ee_VMGM6Fr1eRZSEdUu7VQe1uLjQdI6MVdqVuJdnvxy4kOKWb3xIBy8EDdmNL-Xo7rYFr0nMg76o7YTAXAANVFw4rQ38K6kRS_JuEt-SC6YD4fW8xvNPxpGs_nZ5GYFYYJHhZSLg6hA=nw" alt="" width="375"><figcaption></figcaption></figure>

In this tab you can:

* Filter by a date range and form factor
* See the number of mailpieces sent with QR Codes during that time period
* See the number of QR Codes that have been scanned during that time period
* See a graph of QR Code scans over a selected date range
* Filter for more specific subsets of your mail by leveraging [metadata](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/using-metadata).

To receive more detailed analytics, such as time of scan, IP Address, etc, reference [QR Analytics endpoint](https://docs.lob.com/#tag/QR-Codes) in our API documentation.

### Informed Delivery

We offer engagement metrics for each Informed Delivery campaign.  It's important to remember not every member of your audience may be subscribed to Informed Delivery daily emails. As such, here you will see how many emails were sent for your campaign, and the engagement rate. &#x20;

* Mail pieces sent
* Emails Sent&#x20;
* Open Rate&#x20;
* Click Through Rate

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FMZBx6SuJ5Bl93jN9mJM5%2FInformedDeliveryAnalytics.png?alt=media&#x26;token=d7e1a225-e82e-4f4f-a2a8-f5c82157f9f0" alt="" width="375"><figcaption></figcaption></figure>

## Mail speed <a href="#mail-speed-1" id="mail-speed-1"></a>

{% hint style="info" %}
Access to this feature is exclusive to Enterprise plan customers. Upgrade to the appropriate [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions) to gain access.
{% endhint %}

Track how quickly your mail moves from being sent to marked as processed for delivery, pinpointing efficiency and flagging any delays.

The Mail Speed tab shows the number of business days it took from a mail piece's `send_date` to the date the mail piece was marked as `processed_for_delivery` by the USPS.

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FdVQR3O6ztGkTahwMmY0N%2FMA_mail_speed.png?alt=media\&token=f57ecc67-6d1c-4929-8f3c-d47e4f9b9efb)

The Mail Speed graph respects all applied filters and shows the average and median mail speed for all the mail pieces that fall within the filter. Mail pieces that have yet to receive a `processed_for_delivery` tracking event are not counted in the metrics above the graph.&#x20;

Please note, the graph is for US mail only.

## Mail distribution <a href="#mail-distribution-2" id="mail-distribution-2"></a>

{% hint style="info" %}
Access to this feature is exclusive to Enterprise plan customers. Upgrade to the appropriate [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions) to gain access.
{% endhint %}

Analyze where your mail is going and how fast it gets there with a breakdown of mail pieces by state, helping you optimize your future send strategies.

The Mail Distribution tab shows the number of mail pieces sent to each US state (and Washington D.C., but excludes US territories). A state's color corresponds to how many mail pieces have been sent to that state.&#x20;

Hovering over a state will provide more details like how many mail pieces have received a `processed_for_delivery` tracking event, as well as average and median mail speeds (calculated the same way as the [Mail Speed ](#mail-speed-1)tab).

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FPbP69csQG3DoHIvSy7gI%2FMA_mail_distro.png?alt=media\&token=bc9ca90b-0b5f-4b85-b5fe-5365c3527f66)

You can also view the data in a table format. The table shows the same data as the map, where each state's data corresponds to a row. Clicking on a column header will sort the values in that column. To search by state name, click on the search icon and input a value to filter the table.

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F01Yjm3OFN7ocJD8vdrFb%2FMA_mail_distro2.png?alt=media\&token=fcec5f5d-6183-4669-a526-6533526670ac)

## Filtering <a href="#filtering-5" id="filtering-5"></a>

On your Mail Analytics Dashboard, you can slice-and-dice your data by various other aspects of your mailings, including: product type, recipient ZIP code, template used, and more. You can use these filters to compare deliverability between your different campaigns, recipients, and more.

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FT5dLox47tUGqvHOxsvoh%2FMA_filtering.png?alt=media\&token=eb5290e3-2a3a-459b-b36c-6279b687183f)

Be sure to leverage Lob's [metadata feature](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/using-metadata) more deeply tag your Lob mailings with any internal data you may have, such as a customer ID or campaign ID. Then, you can easily filter by that metadata within the Analytics Dashboard to view different deliverability reports based on those factors.

For mail sent to [international destinations](https://help.lob.com/building-a-mail-strategy/international-mail#mail-tracking), we only expect to get either "In Transit" or "In Local Area" scans. For this reason, we've added a top level filter where you can compare US and international mailings, with the last three tracking buckets disabled for international mail.

{% hint style="success" %}
You can export analytics data (svg, png, csv) by clicking the hamburger menu located at the top right of the graph. [For more details on exporting mail data see here.](https://help.lob.com/print-and-mail/getting-data-and-results/exporting-mail-data)
{% endhint %}