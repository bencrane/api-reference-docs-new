# Tracking your mail

One of the most powerful advantages of using Lob is that you can have visibility of any individual mail piece as it moves across the entire print production and delivery process. Gain complete transparency into your mail’s journey from print production to final delivery, ensuring you stay informed every step of the way.

Lob will surface notable actions or **events** within the Lob architecture. Examples include when a mailpiece is created, fails the rendering process, or when a Lob QR code is scanned.&#x20;

Additionally, each U.S. mail piece is printed with a unique  [Intelligent Mail Barcode (IMb)](https://help.lob.com/designing-mail-creatives/artboard-layout#intelligent-mail-barcode-11), similar to a package tracking number. For USPS First or Standard Class mail, Lob processes data from our commercial printers and mail partners, along with USPS scan events, to surface **tracking events** as your mail moves through the delivery process.&#x20;

You can access this data in the Lob dashboard at the individual mailpiece, campaign, or aggregate level. You can also [subscribe to webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks) in the Lob Dashboard or via the API to get proactive notifications. See the full list of [events](https://help.lob.com/print-and-mail/getting-data-and-results/broken-reference) (including [tracking events](https://docs.lob.com/#tag/Tracking-Events)) you can access in our API documentation.

## Tracking events <a href="#mail-tracking-events-1" id="mail-tracking-events-1"></a>

{% hint style="info" %}
Note that any mail pieces sent in the Test Environment will not receive tracking events.
{% endhint %}

Tracking events are a subset of [all Events](https://docs.lob.com/#tag/Events); below is a list of each tracking event label and description, as recorded by Lob:

* **Received** - The API call for the mail piece was made and received by Lob. (Event will be displayed in dashboard at individual mailpiece level; no webhook available.)
* **In production** - Mail piece instructions were dispatched to Lob's printer network and the request is now being printed/cut, soon to be handed off to the USPS or a mail carrying partner for fulfillment. (Event will be displayed in dashboard at individual mailpiece level; no webhook available.)
* **Mailed** - Confirmation that mail has been handed off to USPS or a mail carrying partner from our printers.&#x20;
  * This feature exclusive to Enterprise edition customers. For non-Enterprise customers, the Mailed event in your dashboard view of tracking events will be greyed out in the tracking event stepper.
  * The ability to accurately surface the "Mailed" tracking event is a unique feature to Lob, and can be utilized to monitor Lob’s SLA adherence as well as provide auditable proof for time of mailing.&#x20;
  * The “Mailed” tracking event appears at earliest two business days after sending your Lob API request. In some instances, it can take longer for this “Mailed” event to become visible, but when surfaced, it will accurately reflect the actual date of mail handoff from our printers.
* **In Transit** - The mail piece is being processed at the USPS entry/origin facility or commingler.
* **In Local Area** - The mail piece is being processed at the USPS destination facility.
* **International Exit** - The mail piece has been processed to ship to a destination abroad. This is typically the last scan a US-originated international mail piece will receive from the USPS. *Note this scan is historically inconsistent, but if it occurs, Lob will surface.* &#x20;
* [**Processed for Delivery**](#how-to-know-if-your-mail-was-delivered-5) - The mail piece has been greenlit for delivery at the recipient's nearest USPS postal facility. The mail piece should reach the mailbox within 1 business day of this tracking event.
* **Delivered** - The mail piece has been delivered to the recipient’s address. This event is generated when the USPS mail carrier's GPS unit leaves the delivery area. *USPS does not guarantee every event for each mail piece, thus Processed for Delivery is more reliable.*
* [**Re-routed**](#re-routed-mail-8) - The mail piece is re-routed due to recipient change of address, address errors, or USPS relabeling of barcode/ID tag area.
* [**Returned to Sender (RTS)**](#undeliverable-mail-9) - The mail piece is being returned to sender due to barcode, ID tag area, or address errors.

### Scanned events <a href="#scanned-events-3" id="scanned-events-3"></a>

Following production, all mail pieces will be handed off from our printers to USPS and will enter the USPS mail stream. All subsequent events are subject to USPS accurately scanning the mail piece as it travels to its destination in the mail stream, hence called "scanned" events.&#x20;

For tracking events from USPS (i.e., all events listed after the "[Mailed](#mailed-tracking-events-4)" event), expect to start seeing your first tracking event appear within:

* 3 business days after your Send Date for First Class Mail
* 4-5 business days after your Send Date for Standard Class Mail

In addition to accessing this mail tracking data via our API or Dashboard, you can receive real-time notifications by [using webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).&#x20;

### Missing or out-of-sequence scans <a href="#missing-or-out-of-sequence-scans-7" id="missing-or-out-of-sequence-scans-7"></a>

All USPS scan events are dependent on the local postal offices and how they process/sort mail. Similarly, the delivery of those mail pieces is also under the full control of the local post office.&#x20;

We do not have added visibility or control over the actual mail pieces once they are handed off to USPS—we can only monitor their progress by surfacing mail tracking events that are visible on your dashboard.&#x20;

{% hint style="warning" %}
Lob does not have any control over the accuracy of scans, nor can Lob go back and reconcile scan events as it is purely a USPS-owned process.&#x20;

While scans are not guaranteed by USPS, we do see scans on over 99% of our mailings. If more than 5 business days have passed and you don't have any tracking events, send an email to <support@lob.com> and our team will be able to confirm whether the mail piece has been mailed.
{% endhint %}

## Tracking for special mail types <a href="#metered-mail-10" id="metered-mail-10"></a>

{% hint style="info" %}
Reminder that mail pieces sent in the Test Environment will not receive a tracking events.
{% endhint %}

### Metered Mail <a href="#metered-mail-10" id="metered-mail-10"></a>

The minimum volume to qualify for Presort mail is 200 pieces (or 50 lbs) of Marketing Mail or 500 pieces of First Class mail, which is a USPS requirement. Some mail is sent out metered if that day's volume from one of Lob’s production partners does not meet the minimum volume per mail type, as required by USPS. This means the mail pieces are not able to be batched with the other mail pieces and have to be mailed separately.&#x20;

Historically these mailpieces have been difficult to track without a batch ID. But beginning July 12, 2023, the “Mailed” event for Metered mail is available in our webhooks for tracking events and included in mail counts within the Mail Analytics Dashboard.&#x20;

Please note we would not expect to populate any other tracking events for Metered mail.

### PO Box Mail

While we typically see all scans for the majority of our mailings, it is not unusual to see mail sent to a PO box with tracking that ends at the **“In Local Area”** scan event, even though the recipient has physically received the piece.&#x20;

“In Local Area” scan indicates receipt and processing by the post office most local to the final delivery point. Typically the next scan would be “Processed for Delivery,” to indicate a mailpiece has been cleared for a final delivery attempt (and is likely loaded directly onto the mail delivery vehicle). However, a PO box does not need to be loaded onto a vehicle for the final delivery, as the PO box itself is located at the post office already. In this case, postal workers can simply hand-deliver the mailpiece to its final destination—so there will be no "Processed for Delivery" scan.

### Unique ZIP codes

This is a ZIP Code that belongs to some entity (for example, a university, a government agency, etc) which is responsible for sorting its own mail. These ZIP codes are classified by the USPS as a “Unique” ZIP Code (code [U1](https://lob.com/docs#us_verification_details)), and we often do not see delivery scan events for these ZIP codes. This is because the entity itself is responsible for the final stage of delivery of their mail, rather than USPS.&#x20;

### Registered & Certified Mail <a href="#tracking-information-for-registered-certified-mail-14" id="tracking-information-for-registered-certified-mail-14"></a>

Letters sent as Registered do not receive the same scan events as regular First or Standard Class mail. Registered Mail will instead receive a carrier tracking number and link, which is an add-on that will be available three (3) business days following the mailer’s `send_date`. This tracking number can be used to track the mailer via the carrier’s website.

If you decide to send Certified Mail through Lob, you will receive a carrier tracking number and tracking link retrievable via your Lob dashboar&#x64;**,** which can be used to track the mail piece via USPS’s website. You can also track the mail via scan events within your Lob dashboard. Sometimes certified mail tracking will be available immediately, or as late as 3 days after sending the mail piece.&#x20;

See here for more details on [tracking for Certified or Registered Mail](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage/certified-mail-or-registered-mail).

### Return envelope tracking for Reply Mail <a href="#return-envelope-tracking-for-reply-mail-12" id="return-envelope-tracking-for-reply-mail-12"></a>

Enterprise edition customers can now access return envelope tracking for USPS Courtesy Reply Mail (for letters only). Once the returned mail piece enters the mailstream, the customer can start receiving notifications to tracking events via our webhooks.

For more information, see how to [enable return envelope tracking](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letter-envelopes#return-envelope-tracking-4), and how to [view return envelope tracking events](https://help.lob.com/print-and-mail/using-webhooks#return-envelope-tracking-15) via webhooks.

## How to confirm USPS received your mail&#x20;

[Using webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks), a user can confirm USPS possession for the majority of First Class/Standard mail pieces. (If proof of USPS possession is crucial to your organization, Lob offers [Registered and Certified Mail](#tracking-information-for-registered-certified-mail-14).)

1. The following mailpiece webhooks indicate USPS possession:

* xxx.delivered
* xxx.in\_local\_area
* xxx.in\_transit
* xxx.processed\_for\_delivery
* xxx.re-routed
* xxx.returned\_to\_sender

<figure><img src="https://lh7-us.googleusercontent.com/h5bvKlZkaAiJ6wa1glORDt5pdCaWjIi9xoW5xltSj7IWOTXzzf9iBEN3EOyXz46sfTtwH1IYIMJGmVCwzAoslWQMYGP-ZWROyQE1R7G7xAnLSClWU49WBQo17S1mLVkUqJy8QfC3vGGSJgBopSePVe0" alt=""><figcaption><p>Also applies to self-mailers</p></figcaption></figure>

2. USPS may not consistently scan all mail pieces at every stage; Lob is only able to capture and surface scans received from USPS itself. (Lob sees USPS scans for the majority of mail pieces; that is, a very small percentage of mail pieces receive no scans at all.)
3. ​​Lob will send webhook events as soon as they become available. However, users should not assume all webhooks will be sent in real-time, and may occasionally experience some delays; they may also be received out of order.
4. That said, **receipt of any of the events noted above confirms that a mail piece is in USPS possession.**

* The inverse is not necessarily true; i.e., NOT receiving any of these events is not a guarantee that the piece is NOT in the mainstream.&#x20;

5. Although events may not be sent in real-time, for tracking events you can get the USPS timestamp of the event under `tracking_events[].time`.

* The earliest time stamp of any of these events would equate to the earliest (recorded) possession by USPS.

See our technical use case [ingesting tracking events with webhooks](https://help.lob.com/developer-docs/use-case-guides/ingesting-tracking-events-with-webhooks) for a deep dive on how to ingest events for a specific mail piece, run a monthly data pull from Lob's system for mail pieces that don't have a certain event, or get real-time updates as your mail piece goes through the mail stream.

## How to know if your mail was delivered <a href="#how-to-know-if-your-mail-was-delivered-5" id="how-to-know-if-your-mail-was-delivered-5"></a>

For First and Standard Class mailings, "Delivered" is typically the last event that USPS provides. When your mail piece receives this event, this means that a USPS courier has delivered the mail piece.

{% hint style="info" %}
The "Delivered" event is generated when the USPS mail carrier's GPS unit leaves the delivery area; it is not guaranteed by the USPS. **If a “Delivered” event hasn’t yet surfaced for your mail piece, but you have received a “Processed for Delivery” scan, this indicates that USPS is expected to attempt delivery within one business day.**
{% endhint %}

For international mailings originating in the US, see [International Mail](https://help.lob.com/building-a-mail-strategy/international-mail#mail-tracking) for details on tracking mail pieces abroad.

### Delivery timelines & delayed pieces <a href="#delivery-timelines-delayed-pieces-6" id="delivery-timelines-delayed-pieces-6"></a>

Delivery times for mail will vary depending on [mail class](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage) and destination:&#x20;

* **First Class Mail**: US domestic mail delivery typically takes 5-7 business days, and international mailings take an additional 7-9 business days.&#x20;
* **Standard Class Mail**: Delivery times can take anywhere from 7-21 business days. USPS does not provide delivery time guarantees for Standard Mail.

{% hint style="warning" %}
Delivery times quoted are estimates; Lob uses USPS as our primary carrier and USPS experiences delays from time to time. To see the most up-to-date status of your mailing, check the tracking information of your particular mailing.
{% endhint %}

### Re-routed mail <a href="#re-routed-mail-8" id="re-routed-mail-8"></a>

If you receive a "**Re-routed**" scan, this indicates that USPS attempted delivery at the original address, but re-routed it because your recipient no longer resides at that address. In these cases, USPS will attempt to deliver to your recipient at their new address (if they filed a National Change of Address).&#x20;

### Undeliverable mail / Return to Sender (RTS) <a href="#undeliverable-mail-9" id="undeliverable-mail-9"></a>

If you received a "**Return to Sender (RTS)**" event scan, this indicates that USPS attempted delivery of the mail piece at the original address, was unsuccessful, and the mail is being re-routed back to the return address after being deemed [undeliverable or misdeliverable](https://faq.usps.com/s/article/How-is-Undeliverable-and-Misdelivered-Mail-Handled) as originally addressed.

This results in a yellow sticker being affixed to the mailing by USPS for tracking purposes called a [NIXIE](https://postalpro.usps.com/undeliverable-addressed-uaa-mail/CFS_Nixie_Label) label. The NIXIE label is affixed by the USPS if they are unable to complete delivery. (In rare cases, RTS without a NIXIE label is possible due to either the neglect of the USPS agent, or because the recipient had chosen to return it themselves.)

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FLIW08grSHkZb4MhS8BMp%2FScreen%20Shot%202021-08-05%20at%2011.20.10%20AM.png?alt=media&#x26;token=60db5898-6f4b-4299-90bd-918974959dc8" alt=""><figcaption><p>Example of a USPS Return to Sender sticker (NIXIE label)</p></figcaption></figure>

<details>

<summary>Common RTS reasoning codes on NIXIE label</summary>

* **Attempted Not Known (ANK):** Delivery attempted, addressee not known at place of address
* **Deceased (DEC):** Used only when the addressee is deceased and mail is not properly deliverable to another person
* **In Dispute (DIS):** Cannot be determined which disputing party has better right to mail
* **Insufficient Address (IA):** Necessary address details are omitted and the correct address not known
* **Illegible (ILL):** Address not readable
* **No Mail Receptacle (NMR):** Addressee failed to provide a receptacle for receipt of mail
* **No Such Number (NSN):** Addressed to nonexistent number and correct number not known
* **No Such Street (NSS):** Addressed to nonexistent street and correct street not known
* **Refused (REF):** Addressee refused to accept mail or pay postage charges
* **Unclaimed (UNC):** Addressee abandoned or failed to call for mail
* **Not Deliverable As Addressed - Unable to Forward (UTF):** Mail undeliverable at the address given; no change-of-address order on file; forwarding order expired
* **Vacant (VAC):** House, apartment, office, or building not occupied

</details>

After the RTS event scan, the mail piece is then treated as a new letter that is going to a new destination and will be tracked to the reroute location. This may be why the same mail piece may receive new scans after receiving the RTS event.&#x20;

A multi-delivery attempt is translated into scans in “Delivery Attempt 1 and 2” below, compared to a standard delivery where the mail piece makes it to its final destination in a single attempt (Col 1):

<table data-header-hidden><thead><tr><th width="278.3333333333333"></th><th width="221"></th><th></th></tr></thead><tbody><tr><td><strong>Standard Delivery Process</strong></td><td><strong>Delivery Attempt 1</strong></td><td><strong>Re-Routed Attempt 2</strong></td></tr><tr><td>Received</td><td>Received</td><td>-</td></tr><tr><td>In Production</td><td>In Production</td><td>-</td></tr><tr><td>Mailed</td><td>Mailed</td><td>-</td></tr><tr><td>In Transit</td><td>In Transit</td><td>-</td></tr><tr><td>Processed for Delivery</td><td>Return to Sender --> </td><td>In Transit [+Yellow Sticker]</td></tr><tr><td>Delivered</td><td>-</td><td>Processed for Delivery</td></tr><tr><td> </td><td>-</td><td>Delivered</td></tr></tbody></table>

{% hint style="danger" %}
USPS may not consistently scan all mail pieces at every stage; Lob is only able to capture and surface scans received from USPS itself.
{% endhint %}

Because RTS scans are not necessarily an 'end-state scan', you should not track whether it was the last scan received when trying to calculate the percentage of RTS mail, as it may have been marked as such and still received additional scan events. Instead, you should try calculating the percentage based on whether the RTS scan event was ever received, regardless of its place in the sequence of scan events.

Furthermore, we recommend you confirm the updated address with the intended recipient and submitting a new request to have it printed and mailed. There is currently no way to re-initiate an existing request in Lob.&#x20;

## Visibility of tracking events <a href="#exporting-tracking-events-11" id="exporting-tracking-events-11"></a>

{% hint style="info" %}
You can **export** all tracking events data into a CSV file; [see more details on exporting mail data here.](https://help.lob.com/print-and-mail/getting-data-and-results/exporting-mail-data)
{% endhint %}

### **Where can I see mail piece tracking?**

You can see tracking events under the detailed pages within Print & Mail and/or Campaigns in the dashboard.&#x20;

Additionally, under Mail Analytics (accessed via the left navigation bar in the dashboard),[ the Tracking Events tab](https://help.lob.com/print-and-mail/mail-analytics#tracking-events-3) displays a visual breakdown of all tracking events applicable to the mail pieces within the filter parameters.&#x20;

### **How can I get notified of events?**

Real-time progress of mail pieces can be accessed by [using webhooks,](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks) an easy way to get notifications on events happening asynchronously on Lob's side. Once webhooks are successfully set up on the dashboard, Lob will "push" you notifications when mail pieces are created, when they receive USPS scans such as "In Local Area" or "Processed for Delivery", or any other event you subscribe to.

Enterprise edition customers can also access [return envelope tracking](#return-envelope-tracking-for-reply-mail-12) for USPS Courtesy Reply Mail (for letters only). Once the returned mailpiece enters the mailstream, the customer can start receiving notifications to tracking events via our webhooks.&#x20;

The full list of event types available for subscription can be found [here](https://docs.lob.com/#tag/Events).

### What should I do if my mail piece does not receive a tracking event?

If your mail piece doesn’t have a tracking event, first check to see how much time has elapsed between your mail piece Send Date and the current date. Typically, it’ll take 3 business days (for First Class Mail), or 4-5 business days (for Standard Class Mail) from the time of your Send Date for USPS tracking events to appear.

If more than 5 business days have elapsed since your Send Date and you don’t have any tracking events, send an email to <support@lob.com>. Our team will be able to confirm whether the mail piece has been mailed.

Note: If it has been more than 30 days, Lob will not have access to the API logs which track mailpiece tracking events, but you should be able to see the date when the mail piece was scanned by clicking on 'View details' in your dashboard.