# Letter envelopes

## Standard letter outer envelopes <a href="#standard-letter-outer-envelopes-0" id="standard-letter-outer-envelopes-0"></a>

Letters printed by Lob are sent in a plain Standard #10 double-windowed outer envelope, or in a flat envelope when letter pages exceed 6 pages. These are automatically included when a Letter API request is made, and no special request will need to be made to utilize them. These standard outer envelopes cannot be customized by default.

#### **Standard #10 outer envelope (double-windowed)**&#x20;

<details>

<summary>Design templates</summary>

* [Letter template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_template.pdf) for standard letter & check orders (tri-folded)&#x20;

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 4.125 x 9.5"
* Window #1 (Top):
  * Window size: 0.875 x 3.25"
  * Position from left edge: 0.625"
  * Position from bottom edge: 2.375"
* Window #2 (Bottom):
  * Window size: 1 x 4"
  * Position from left edge: 0.625"
  * Position from bottom edge: 1"
* Embossed 24# White Wove with a [vertical grooved pattern](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/no10_env_view.jpg)
* Contains blue inside security tint
* Fits up to 6 sheets of tri-folded `8.5 x 11"` paper / 12 duplexed pages

</details>

#### **9 x 12" Flat outer envelope (single window)**

<details>

<summary>Design templates</summary>

* [Letter template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_flat_template.pdf) for standard letter & check orders (full page)

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 9 x 12"&#x20;
* Window #1:
  * Window size: 4 x 3.375"
  * Position from left edge: 0.5"
  * Position from top edge: 0.625"
* 24# White Wove
* Contains blue inside security tint
* Fits between 7 to 60 sheets of `8.5 x 11"` paper / up to 120 duplexed pages

</details>

## Certified Mail envelopes <a href="#certified-mail-envelopes-1" id="certified-mail-envelopes-1"></a>

All [Certified Mail](https://help.lob.com/print-and-mail/designing-mail-creatives/letters#using-certified-mail-or-registered-mail-4) printed by Lob are sent in a large single-windowed Standard #10 Certified Mail envelope with an inside security tint. These Certified Mail envelopes cannot be customized.

<details>

<summary>Design templates</summary>

* [Design template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/envelopes/no_10_certified_mail_env.pdf) for Certified single-window #10 envelope&#x20;
* [Design template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_certified_template.pdf) for Certified letter orders (tri-folded)&#x20;

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 4.125 x 9.5"
* Window #1:
  * Window size: 3 x 8"
  * Position from left & right edges: 0.75"&#x20;
  * Position from top & bottom edges: 0.5625"
* 28# White Wove
* Contains inside security tint
* Fits up to 6 sheets of tri-folded `8.5 x 11"` paper / 12 duplexed pages

</details>

## Return envelopes <a href="#return-envelopes-2" id="return-envelopes-2"></a>

{% hint style="info" %}
Aspects of this feature are exclusive to higher edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this form factor, or reach out to our [sales](https://www.lob.com/sales) team.
{% endhint %}

Lob offers two options for USPS reply mail for our letter form factors only:

* **Courtesy Reply Mail**, available to all customers
* **Business Reply Mail**, available to Enterprise edition customers only

Both reply mail options will be sent in a standard #9 return envelope (single-windowed), which are available to all customers by default. They are blank, come without prepaid postage, and will expire in 6 months. No custom artwork is permitted on the front or back sides of these plain #9 envelopes. See our [Template Gallery](https://www.lob.com/template-gallery#custom-envelopes) for design examples.&#x20;

<details>

<summary>Design templates</summary>

* [#9 Standard return envelope (single window)](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/no9_single_env_template.pdf)
* [Perforated letter template for custom return envelopes](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf)

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 3.875 x 8.875"&#x20;
* Window #1:
  * Window size: 1.125 x 4.5"&#x20;
  * Position from left edge: 0.875"
  * Position from bottom edge: 0.5"
* Contains inside security tint
* Expiration: 6 months (to ensure the integrity of adhesives)
* Fits up to 6 sheets of `8.5 x 11"` paper / 12 duplexed pages (+ letter [perforation](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf) required)

</details>

To include a return envelope with your mail pieces, you will need to send a Letter API request with `return_envelope` and `perforated_page` options completed:

* `return_envelope = true`
* `perforated_page`, specifying the page that will have tear-off slips with a remittance slip and return address for the reply mail

Once the return envelope setting is activated, letter designs will automatically include a bottom perforation if including a return envelope.&#x20;

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FLqdWKbLOLYAXlOnJBlUk%2FScreenshot%202023-05-10%20at%204.06.01%20PM.png?alt=media&#x26;token=d6a54f9b-0b5f-4c8e-b871-8c4ac93ab680" alt=""><figcaption></figcaption></figure>

For customer's who want to further customize their #9 envelope artwork, please reach out to your Customer Success Representative.

### Sending Business Reply Mail (BRM) <a href="#sending-business-reply-mail-brm-3" id="sending-business-reply-mail-brm-3"></a>

{% hint style="info" %}
This feature is exclusive to Enterprise edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this form factor, or reach out to our [sales](https://www.lob.com/sales) team.
{% endhint %}

* A valid BRM permit must be obtained from USPS before you can start using a BRM mail piece and receive BRM mail
* BRM users also need a unique Zip+4Code assigned by the USPS to qualify for volume discounts
  * Assigned Zip+4 Codes are unique to the category of Reply Mail used
* Customers sending Business Reply Mail (BRM) must use Business Return Envelopes (BREs). BREs are [#9 return envelopes (no windows)](#standard-9-return-envelope-no-window-and-single-window-options) with inside security tint
  * A USPS-approved design must be used in BREs; no custom artwork is allowed&#x20;
  * Postage must be prepaid
  * Letter perforation is required

{% hint style="warning" %}
Business Return Envelopes (BREs) cannot be ordered through the dashboard; please reach out to your account manager to facilitate.
{% endhint %}

### Return envelope tracking <a href="#return-envelope-tracking-4" id="return-envelope-tracking-4"></a>

{% hint style="info" %}
This feature is exclusive to higher edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this form factor, or reach out to our [sales](https://www.lob.com/sales) team.
{% endhint %}

Lob offers return envelope tracking for their USPS Courtesy Reply Mail services. Return tracking information is only available via webhooks for standard return envelopes (non-custom single-windowed envelopes only).

To access this feature, enterprise customers need to send an API request for a letter with `return_envelope`, `return_address` and `perforated_page` options completed:

* `return_envelope = true`, or \
  `return_envelope = no_9_single_window`, if custom return envelopes are enabled on the account
* `perforated_page`, specifying the page that will have tear-off slips with a remittance slip and return address for the reply mail
* `return_address`, specifying the return address the return envelope customers should send remittance slips to

This will result in the return address and associated Intelligent Mail Barcode (IMb) tracking code to be placed within the window area of the perforated page. The #9 return envelope will be mailed to the customer along with the letter including the perforated page and return address in a #10 standard outer envelope. Note that no custom outer envelopes can be used with this feature at this time.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F7FTjR26BFlBKfCU8RcVb%2Fimage%20(2).png?alt=media&#x26;token=37b65bd8-df54-4640-b32e-c007786bd363" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
It is possible to send Courtesy Reply mail without enabling return envelope tracking, as they are two separate features. To use normal reply mail *without* tracking, make sure to skip the `return_address` field. This means only the return address (and no IMb) will be rendered in the window area of the perforated page.&#x20;
{% endhint %}

#### **Tracking event notifications**

Once the returned envelope enters the mail stream and is scanned by the USPS, the customer can start receiving notifications to mail tracking events, which will be surfaced via webhooks.

The following is a list of mail tracking event labels and descriptions available for reply mail:

* **Created**: Return envelope is first created (should be simultaneous with Letter creation)
* **In transit**: Return envelope is being processed at the entry/origin facility
* **In local area**: Return envelope is being processed at the destination facility
* **Processed for delivery**: Return envelope is greenlit for delivery at the end recipient's nearest postal facility. The mailpiece should reach the mailbox within 1 business day of this tracking event.
* **Re-routed**: Return envelope is re-routed due to recipient change of address, address errors, or USPS relabeling of barcode/ID tag area
* **Returned to sender**: Return envelope is undeliverable and is being returned to sender due to barcode, ID tag area, or address errors.

Return envelope tracking is accessible via our [webhooks](https://dashboard.lob.com/webhooks), and the [Event Logs](https://dashboard.lob.com/events) node in the Lob dashboard. Tracking events will appear in the `Letters` Events portion of the original individual mailpiece in the dashboard as soon as they become available, or can be downloaded using the Export button that’s located at the top of the [Letters section](https://dashboard.lob.com/letters) in the dashboard.

Note: As USPS does not return the `Delivered` mail tracking event for return envelopes, Lob is unable to surface this event via webhooks.

#### **Best practices**

Return addresses that are passed into the `return_address` field will be used *exactly as passed in*. We do not run this address through any verification services like NCOA or CASS. This helps ensure that remittance slips are sent to the business address provided. Customers must take extra care to ensure that the address information provided matches their desired delivery address.

Additionally, we recommend supplying ZIP+4 codes in the return address specified to ensure the fastest, most accurate mailing possible. This can speed up USPS processing and delivery by up to as much as 2 days.

## Custom envelopes <a href="#custom-outer-envelopes-7" id="custom-outer-envelopes-7"></a>

{% hint style="info" %}
This feature is exclusive to Enterprise edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this feature, or contact our [sales](https://www.lob.com/sales) team.
{% endhint %}

### Overview <a href="#envelope-dimensions-designs-8" id="envelope-dimensions-designs-8"></a>

Lob allows customization of select #10 outer envelopes and #9 return envelopes. Envelopes must be created, ordered, printed and made available in your inventory *before* they can be utilized with Letter API call requests. Envelope orders and inventory can be fully managed in the [Lob dashboard](https://dashboard.lob.com/envelopes). Note that custom envelopes are only supported for letters, and are unavailable for checks or postcards.

To start creating letters with custom envelopes, refer to our [Letters API documentation](https://docs.lob.com/#tag/Letters) or see our [Template Gallery](https://www.lob.com/template-gallery#custom-envelopes) for inspiration.&#x20;

### Envelope dimensions & specs <a href="#envelope-dimensions-designs-8" id="envelope-dimensions-designs-8"></a>

#### **Standard #10 outer envelope (single-window only)**

<details>

<summary><strong>Design templates</strong></summary>

* [Custom #10 outer envelope template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/no10_env_template.pdf)
* [Letter template for custom envelopes](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_custom_envelope.pdf)

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 4.125 x 9.5"
* Window #1:
  * Window size: 1.125 x 4.5"
  * Position from left edge: 0.875"
  * Position from bottom edge: 0.5"
* 24# White Wove
* Contains inside security tint
* Expiration: 6 months (due to ensure adhesive's integrity)
* Fits up to 6 sheets of tri-folded `8.5 x 11`" paper / 12 duplex pages

</details>

#### **Standard #9 return envelope (no-window & single-window options)**&#x20;

<details>

<summary>Design templates</summary>

* [#9 Standard return envelope (no window)](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/no9_standard_env_template.pdf)
* [#9 Standard return envelope (single window)](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/no9_single_env_template.pdf)
* [Perforated letter template for custom return envelopes](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf)

</details>

<details>

<summary>Envelope specs</summary>

* Envelope face size: 3.875 x 8.875"&#x20;
* Window #1 (if single-windowed option):
  * Window size: 1.125 x 4.5"&#x20;
  * Position from left edge: 0.875"
  * Position from bottom edge: 0.5"
* Contains inside security tint
* Expiration: 6 months (to ensure the integrity of adhesives)
* Fits up to 6 sheets of tri-folded `8.5 x 11`"paper / 12 duplexed pages (+ letter [perforation](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf) required)

</details>

### **Design placement**

Follow the guidelines below to achieve optimal results for your envelope designs, and to ensure a smooth creation process.

<details>

<summary><strong>Layout considerations</strong></summary>

* Bleeds should extend 0.125" past the trim line
* Any other artwork should be 0.125" away from trim line due to movement at press
* Custom envelopes will not be printed outside of the safe zone, nor on the flap

</details>

<details>

<summary>Accepted image submission formats</summary>

* Preferred: PDF file (.pdf)
* Secondary: Adobe Illustrator (.ai), Indesign (.indd), Photoshop (.psd)&#x20;

</details>

<details>

<summary>Artwork considerations</summary>

* Outline all fonts: differences in kerning, font versions, anti-aliasing, etc., can cause small variations between what you see on your screen and what we output to press
* Double-check that all images are embedded into your document
* Ensure all rasterized artwork (images, effects, copy, etc.) is created and saved at or above 300 dpi
* All images must be at or under 25% ink saturation
* Type should be no smaller than 5 pt
* Thin, small fonts with over 3 colors may fill in slightly or appear “fuzzy”
* Line weights of 0.5 pt or more assure optimum print results
* It is preferred that barcodes/QR codes are vector/editable
* CMYK documents are preferred over RGB

</details>

<details>

<summary>Envelope window placement</summary>

The envelope window is where your recipient address information will be visible. Reference our [letter template for custom envelopes](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_custom_envelope.pdf) to ensure that your recipient’s address is visible. No design within the envelope window will be printed.

</details>

<details>

<summary>Stamp placement</summary>

Postage will be placed in the upper right corner of the envelope. No design will be printed in this space. Refer to our [custom envelope template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/no10_env_template.pdf) for stamp placement.

</details>

<details>

<summary>Return address placement</summary>

USPS prefers that return addresses are placed in the upper left portion of the mail piece, on the side of the piece bearing postage. USPS does not require that all mail include a return address; however, mail sent without a return address cannot be returned.

</details>

### Ordering envelopes <a href="#ordering-17" id="ordering-17"></a>

{% hint style="warning" %}
Envelopes must be created, ordered, printed, and available in your inventory *before* they can be utilized.
{% endhint %}

First, create an envelope design by uploading your artwork in the '[Envelope](https://dashboard.lob.com/envelopes)' section of the Lob dashboard. Hit “Create”, and in the new envelope creation screen, select the envelope size & design and the desired postage option for #10 outer envelopes. Any #9 return envelope selection will default to USPS Standard Class postage.&#x20;

| #10 custom outer envelopes (front & back options)                                                                                                         | #9 custom return envelopes (front-side only)                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1661930462135-Screen%20Shot%202022-08-31%20at%2012.20.51%20AM.png) | <p><br><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1661929856303-Screen%20Shot%202022-08-31%20at%2012.09.58%20AM.png" alt=""></p> |

Once envelope designs are uploaded into the dashboard, an order must be placed to make them available in your inventory for later use. Envelopes can be purchased as one-off orders or through auto-reordering directly in the Lob dashboard.&#x20;

**First-time orders**:&#x20;

{% hint style="success" %}

* New envelope designs take time for quoting, production, and shipment; please **allow up to 25 days** for any new design orders to be fulfilled.
* The **minimum order quantity for any custom envelope order is 10,000 envelopes** per artwork design submitted.&#x20;
* Spoilage is an industry norm that occurs during print set-up and processing. Based on the industry average, **we recommend adding 2-3% to account for spoilage**.
  {% endhint %}

**Auto-reordering**:&#x20;

* When the auto-reordering function is turned on, a new order will be submitted whenever the remaining envelope quantity in inventory **falls below 20%**. A confirmation will show the reorder quantity and price that will be charged.

**Plan ahead**:&#x20;

* Given additional lead times, we recommend enabling auto-reorder for envelopes that will be continuously utilized to ensure there will be no risk of running out.
* Additionally, custom envelopes have a 6-month expiration date to ensure the adhesive's integrity. Any unused envelopes that have expired will be discarded by Lob.&#x20;

### Sending letters with custom envelopes <a href="#sending-letters-with-custom-envelopes-18" id="sending-letters-with-custom-envelopes-18"></a>

Envelopes cannot be used until the dashboard indicates that they have been made available, and any preemptive API requests that include your unique envelope ID will fail. Once an envelope order is available in your inventory, it can be utilized with Letter API call requests.&#x20;

To use a custom envelope with your mail piece, you will need to set the `custom_envelope` parameter in your `POST` call to `https://api.lob.com/v1/letters` to the desired custom envelope ID, which can be found in your dashboard.&#x20;

If a letter is created with a specified envelope ID that is not in stock, the letter request will be rejected. If a letter is created with a specified envelope ID and is 7+ sheets, the letter will be sent instead in a blank, [flat envelope](#9-x-12-flat-outer-envelope-single-window), and the custom envelope inventory will not be decremented. Additionally, custom envelopes have an expiration date, which ensures the envelope's integrity.

{% hint style="warning" %}
When using the single endpoint Letter API, the minimum quantity of envelopes that can be sent during any 24-hour production-day period (10AM PT - 10AM PT) is **4,000 envelopes**. For any customer that fails to send over the 4,000 envelope minimum (with corresponding Letter API calls) will incur a **flat surcharge of $375/day** on your month-end usage invoice.&#x20;

Reach out to your dedicated Customer Success Manager if you have any questions.
{% endhint %}

### Inventory management <a href="#inventory-management-18" id="inventory-management-18"></a>

#### **Envelope details**

Return to the dashboard at any given time to view existing order designs, the number of remaining envelopes, the number of orders that are still outstanding or fulfilled, and mailing class/postage type selected. Inventory will decrease with each API call made for a specific custom envelope design corresponding to a unique envelope ID.

#### **Auto-reorder settings**

When the auto-reordering function is turned on, a new order will be submitted whenever the remaining envelope quantity in inventory falls below 20%. A confirmation will show the reorder quantity and price that will be charged.

Given that custom envelopes have additional lead times, we recommend enabling auto-reorder for envelopes that will be continuously utilized to ensure there will be no risk of running out.

#### **Order history**

View previously submitted orders, and order details once any order is submitted. Rough expected date of availability for submitted orders provides an approximate time of when envelopes may be available, while an email confirmation will be sent when envelopes are actually ready for use.

Custom letter envelopes are set to expire in 6 months (due to adhesives). Expiration dates of ordered designs that still remain in your inventory can be viewed. Once envelopes are expired, customers will not be able to access any remaining inventory of the particular design order in their dashboard.