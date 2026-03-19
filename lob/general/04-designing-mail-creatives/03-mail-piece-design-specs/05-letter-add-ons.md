# Letter add-ons

{% hint style="info" %}
Letter add-ons are features exclusive to our Enterprise tier customers. Upgrade to the appropriate [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access, or contact our [sales team](https://www.lob.com/sales) to learn more. Add-ons are currently only available for 8.5" x 11" standard letters.&#x20;
{% endhint %}

## Add-on: Custom Envelopes&#x20;

Letter envelopes can be customized with branding, artwork, or messaging to communicate vital information to your recipients even before they open the envelope. Lob offers limited customization for some envelopes, including standard #10 outer envelopes (single-windowed) and #9 return envelopes (no window / single-windowed options).&#x20;

For more details, see [custom envelopes](https://help.lob.com/print-and-mail/designing-mail-creatives/letter-envelopes#custom-outer-envelopes-7).

## Add-on: Cards <a href="#using-card-affix-7" id="using-card-affix-7"></a>

Paper cards can now be affixed to letters, providing a compelling method to direct customers to special promotions and drive engagement, both online and in-store. Having “faux” cards can serve as a tangible and memorable reminder for any upcoming marketing promotion.  &#x20;

To get started with letters with card affix, check out our [API documentation](https://docs.lob.com/#tag/Cards) or visit our [Template Gallery](https://www.lob.com/template-gallery#letters) for inspiration.

### Card dimensions & design specs <a href="#card-dimensions-design-specs-8" id="card-dimensions-design-specs-8"></a>

<details>

<summary>Layout templates</summary>

Paper cards can only be affixed horizontally to the top fold of a tri-folded letter, and to the face letter on the first page.&#x20;

Reference our layout templates on where to place your design elements on the card, and the location of where the card will be affixed to any given letter.&#x20;

* [Letter design template with horizontal card affix](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/letters/letter_no10_double_window_card_affix.pdf)&#x20;
* [Card design template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/letters/Card_Affix_Template.pdf)

</details>

<details>

<summary>Card specs</summary>

* 2.125” x 3.375”, with 0.125” rounded corners&#x20;
* 18-24pt thickness, depending on paper availability&#x20;
* Coated 2 sides (gloss varnish) + full bleed&#x20;
* Affixing adhesive: medium tack fugitive glue

</details>

<details>

<summary>Card design &#x26; guidelines</summary>

Artwork can be featured on both sides of the card. In general, any critical design elements or text should be 0.125" away from the final trim line due to movement at press. There are also no color limitations for cards. Other considerations are:

* Double-check that all images are embedded into your document&#x20;
* Ensure all rasterized artwork (images, effects, copy, etc.) is created and saved at or above 300 dpi&#x20;
* Thin, small fonts with over 3 colors may fill in slightly or appear “fuzzy”&#x20;
* Line weights of 0.5 pt or more assure optimum print results&#x20;
* Any barcodes/QR codes provided need to be print-ready&#x20;
* CMYK document

Refer to our [image formatting guides](https://help.lob.com/print-and-mail/creative-formatting#image-formats-17) for more details on image prepping.

</details>

### Card ordering <a href="#card-ordering-11" id="card-ordering-11"></a>

{% hint style="warning" %}
Cards must be created, ordered, and printed, and available in your inventory *before* they can be utilized.&#x20;
{% endhint %}

Upload your front and back designs to create a new card, then order inventory for your card. Cards can be purchased as a one-off order or through auto-reordering.

{% hint style="success" %}

* Allow an estimated **20 business days** for cards to be available for use in your Lob dashboard.&#x20;
* The **minimum order quantity is 10,000 cards** per artwork design submitted.&#x20;
* Spoilage is an industry norm that occurs during print set-up and processing. Based on the industry average, **we recommend adding 2-3% to account for spoilage**.
  {% endhint %}

<details>

<summary>Order cards via the Lob dashboard</summary>

* Go to the [Cards section](https://dashboard.lob.com/cards) in the Lob dashboard and hit the Create button
* Upload a front and back design, and hit Create
* Once card details show, select the Order button at the bottom
* Add the desired number of cards and hit Order

</details>

<details>

<summary>Order cards via the Cards API</summary>

Send a request to the `/v1/cards` [endpoint](https://docs.lob.com/#tag/Cards) with the following fields:

* `Description (Required, string)`: A name to identify your card
* `Front (Required, string)`: A locally hosted PDF or hosted PDF URL for the front card artwork
* `Back (Optional, string)`: A locally hosted PDF or hosted PDF URL for the back card artwork

Send a request to the `/v1/cards/{id}/orders` [endpoint](https://docs.lob.com/#tag/Card-Orders) with the following field:

* `Quantity (Required, number)`: Number of cards you would like to order

</details>

<details>

<summary>Order &#x26; inventory management</summary>

See [inventory management](#inventory-management-for-letter-add-ons) for letter add-ons

</details>

{% hint style="warning" %}
Timing and delivery is dependent on order size and complexity, and may be additionally delayed by forces outside of Lob's control (e.g. USPS delays, printer site shutdowns due to Covid, paper shortages, extreme weather events).
{% endhint %}

### Affixing cards to letters

Once cards are ordered, they cannot be sent with letters until your Lob dashboard indicates they are fully stocked and available in your inventory. An email will notify you once your cards are in stock and are ready to be sent with letter campaigns.&#x20;

**The minimum send quantity is 5,000 cards per letter campaign.** If a letter campaign is created with a specified card ID that is not in stock, the request will be rejected. Affixing charges will be billed with each Letter API call made, which is separate from the initial card order.&#x20;

Special considerations when sending card-affixed letters:&#x20;

* Letters with card affix are limited to a single sheet at max (can be double-sided)&#x20;
* Cards can only be affixed horizontally to the top fold of a tri-folded letter, and to the face letter on the first page&#x20;
* Card-affixed letters will be sent in a standard #10 double-windowed envelope&#x20;
* Card-affixed letters cannot be sent with custom envelopes or buckslips at this time&#x20;
* Card-affixed letters cannot be used with Certified or Registered Mail at this time

<details>

<summary>Affix cards via the Campaigns dashboard</summary>

In “Configure Settings” Step 1 of the [Campaigns](https://dashboard.lob.com/campaigns/) Letter creation flow, choose “Card” as your add-on\
![](https://lh4.googleusercontent.com/zgvguq0TVrlnTX_eZpDJQ45W9bIhmvZG91JR13WI_7p2kgpMIl_WWnzkhdHKIxJmAymZePxVrvybQv9KYx-4O77Ky8DpB22fwsW5AumDv8c2fXRI1i88YjdLC2i9H5XTbuRYZtzRblKEm0tjJeRmssnV_BFsEHXs5YS3FCtccEUlyEhD2FFDWnomtg)

In “Choose Creative” Step 3 of your Campaign, select the card design that you’d like to use in your Letter campaign.&#x20;

* You cannot send cards if you have an insufficient amount in your inventory, as your campaign request will be rejected
* You cannot pair cards with other letter add-ons at this time

</details>

<details>

<summary>Affix cards via the Campaigns API</summary>

Adding cards to letters can be done via the [Campaign API](https://docs.lob.com/#tag/Campaigns):&#x20;

* When loading your creative assets, set the `details[cards][0]` parameter in your `POST` call to `https://api.lob.com/v1/creatives` to the desired `card_id`. The cards parameter is an array which accepts a single `card_id`.&#x20;
* In the future, we may begin accepting multiple `card_id`s, hence the array data type.&#x20;

Additionally, you can find all cards in your account by sending a `GET` call to `https://api.lob.com/v1/cards`

</details>

<details>

<summary>Affix cards via the Letters API</summary>

Affixing cards to letters can be done via the [single-endpoint Letters API](https://docs.lob.com/#tag/Letters), similar to Custom Envelopes

* Set the cards parameter in your `POST` call to `https://api.lob.com/v1/letters` to the desired card ID, which is found in your Lob dashboard
* Additionally, you can find all cards in your account by sending a `GET` call to `https://api.lob.com/v1/cards`

</details>

{% hint style="danger" %}
When using the Letters API single endpoint (`https://api.lob.com/v1/letters)`, cards must be sent in groups of **at least 5,000 card-affix letter API requests** during any 24-hour print-day period from 10AM PT to 10AM PT. If you do not, you may incur setup costs of **$250/day** on your monthly usage invoice. Reach out to your dedicated Customer Success Manager if you have questions.
{% endhint %}

### Card affix offering & variations <a href="#card-affix-offering-variations-17" id="card-affix-offering-variations-17"></a>

Currently we **do** provide the following card affix offering:

* Cards affixed to letters (one sheet total, front-side only)
* Static, non-personalized artwork designs for paper cards
* Horizontal card orientation in a single size
* Cards affixed to the top fold of a trifold letter towards the right
* Letters sent in standard #10 outer envelopes

We do **not** support the following offerings:

* Cards affixed to any other mail format (e.g. self-mailers)
* Cards affixed to letters that totals more than a single page, or on the back-side
* Dynamic, personalized artwork designs that are unique to the recipient
* Plastic cards (e.g. credit or loyalty cards)
* Vertical card orientation or different card sizes
* Cards affixed to any desired location on a letter
* Letters sent in customized #10 outer envelopes
* Card affix for Registered or Certified letters

## Add-on: Buckslips

Buckslips are small mail inserts that can be sent with letters to improve your ROI on marketing campaigns. These attention-grabbers can add pops of color in an otherwise plain-looking letter, and combined with compelling promotions, can be a very cost-effective solution to boost your response rates.

Buckslips can be sent through [Campaigns API](https://docs.lob.com/#tag/Campaigns) or the [Campaigns dashboard](https://dashboard.lob.com/campaigns), but NOT through the single-endpoint Letter API.&#x20;

{% hint style="success" %}
Anything sent with Buckslips will have a 4-day SLA.
{% endhint %}

### Getting started with Buckslips

Check out our:&#x20;

* Lob Dashboard: [Upload & order](https://dashboard.lob.com/buckslips) buckslips, or send with a [letter campaign](https://dashboard.lob.com/campaigns/live)&#x20;
* API documentation for [creating](https://docs.lob.com/#tag/Buckslips/operation/buckslip_create), [ordering](https://docs.lob.com/#tag/Buckslip-Orders) buckslips, or [sending letter campaigns](https://docs.lob.com/#tag/Campaigns/operation/campaign_create) with buckslips
* [Template Gallery](https://www.lob.com/template-gallery#buckslips) for design inspiration
* Or watch a quick demo of ordering buckslips and sending them with letters via the dashboard

{% embed url="<https://lob.wistia.com/medias/sr8sw4e2vb>" %}

### Buckslip dimensions & design specs

<details>

<summary>Layout templates</summary>

* [Buckslip design template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/letters/buckslip_template.pdf)

</details>

<details>

<summary>Buckslip paper specs</summary>

* 8.5” x 3.5” size&#x20;
* 80 lb. Text, Gloss or Matte finish&#x20;
* Double-sided, full bleed

</details>

<details>

<summary>Buckslip design &#x26; guidelines</summary>

Artwork can be featured on both sides of the buckslip. In general, any critical design elements or text should be 0.125" away from the final trim line due to movement at press. There are also no color limitations for buckslips.&#x20;

Other considerations are:&#x20;

* Double-check that all images are embedded into your document&#x20;
* Ensure all rasterized artwork (images, effects, copy, etc.) is created and saved at or above 300 dpi&#x20;
* Thin, small fonts with over 3 colors may fill in slightly or appear “fuzzy”&#x20;
* Line weights of 0.5 pt or more assure optimum print results&#x20;
* Any barcodes/QR codes provided need to be print-ready

Refer to our [image formatting guides](https://help.lob.com/print-and-mail/creative-formatting#image-formats-17) for more details on image prepping.

</details>

### Buckslip ordering

{% hint style="warning" %}
Buckslips must be created, ordered, and printed, and available in your inventory *before* they can be utilized.&#x20;
{% endhint %}

Upload your front and back designs to create a new buckslip, then order your inventory. **.** Buckslips can be purchased as an one-off order or through auto-reordering.&#x20;

{% hint style="success" %}

* The **minimum order quantity is 10,000 buckslips** per artwork design submitted
* Allow an estimated **10 business days** for buckslips to be available for use in your Lob dashboard.&#x20;
* Spoilage is an industry norm that occurs during print set-up and processing. Based on the industry average, **we recommend adding 2-3% to account for spoilage.**
  {% endhint %}

<details>

<summary>Order buckslips via the Lob dashboard</summary>

* Go to the [Buckslips](https://dashboard.lob.com/buckslips) section in the Lob dashboard, and hit the Create button&#x20;
* Upload a front and back design, and hit Create&#x20;
* Once buckslip details show, select the Order button at the bottom&#x20;
* Add the desired number of buckslips and hit Order

</details>

<details>

<summary><strong>Order buckslips via the Buckslips API</strong></summary>

Send a request to the `/v1/buckslips` [endpoint](https://docs.lob.com/#tag/Buckslips) with the following fields:&#x20;

* `Description (Required, string)`: A name to identify your buckslip&#x20;
* `Front (Required, string)`: A locally hosted PDF or hosted PDF URL for the front buckslip artwork&#x20;
* `Back (Optional, string)`: A locally hosted PDF or hosted PDF URL for the back buckslip artwork

Send a request to the `/v1/buckslips/{buckslip_id}/orders` [endpoint](https://docs.lob.com/#tag/Buckslip-Orders) with the following field:&#x20;

* `Quantity (Required, number)`: Number of buckslips you would like to order

</details>

<details>

<summary>Order &#x26; inventory management</summary>

See [inventory management](#inventory-management-for-letter-add-ons) for letter add-ons

</details>

### Sending letters with buckslips

Once buckslips are ordered, they cannot be sent with letters until your Lob dashboard reflects they are fully stocked and available in your inventory. An email will notify you once your buckslips are in stock and are ready to be sent with letter campaigns.&#x20;

**The minimum send quantity is 5,000 buckslips per letter campaign.** If a letter campaign is created with a specified buckslip ID that is not in stock, the campaign request will fail.&#x20;

Special considerations for sending letters with buckslips:&#x20;

* Only 1 buckslip max per letter request&#x20;
* Buckslips counts as one sheet in a letter&#x20;
* Any letter including a buckslip can have a maximum total of 6 sheets (5 letter sheets + 1 buckslip) to fit in a #10 standard envelope&#x20;
  * Said another way, a buckslip cannot be inserted in letters over 6 sheets, as it cannot be inserted in a flat envelope at this time&#x20;
* Custom envelopes (outer & return envelopes) are supported for letters with buckslips&#x20;
* Buckslips cannot be sent with card-affixed letters at this time&#x20;
* Buckslips cannot be used with Certified or Registered Mail at this time
* Buckslips cannot be sent using the single endpoint Letters API at this time

<details>

<summary>Send buckslips via the Campaigns dashboard</summary>

* In “Configure Settings” Step 1 of the [Campaigns](https://dashboard.lob.com/campaigns/) Letter creation flow, choose “Buckslip” as your add-on\
  ![](https://lh6.googleusercontent.com/zdEBhk81jmgaZiJoNOIoaP8v0lJsYx4EXsi11N2Q7WTFL4_eAC27KAYkuGRKEgCT8-9IiiRVH3V172NIV9OvEnqX8AKbG7PQJB5MLPnuB-tY4MvqV9t_EF_qYu6X4V0wRVUO6UvEMDrh9we-HvISdz2bFnBn1nKTCJQLa_2W_mWUFbdBn_EfRkcz5w)<br>
* In “Choose Creative” Step 3 of your Campaign, select the buckslip design that you’d like to use in your Letter campaign.&#x20;
  * You cannot send buckslips if you have an insufficient amount in your inventory, as your campaign request will be rejected

</details>

<details>

<summary>Send buckslips via the Campaigns API</summary>

Adding buckslips to letters can be done via the [Campaign API](https://docs.lob.com/#tag/Campaigns):&#x20;

* When loading your creative assets, set the `details[buckslips][0]` parameter in your `POST` call to `https://api.lob.com/v1/creatives` to the desired `buckslip_id`
  * The `buckslips` parameter is an array which accepts a single `buckslip_id`
  * In the future, we may begin accepting multiple `buckslip_id`’s, hence the array data type
* Additionally, you can find all buckslips in your account by sending a `GET` call to `https://api.lob.com/v1/buckslips`

</details>

## Inventory management for letter add-ons

For any letter add-on items (including buckslips, cards, or envelopes), you will have the ability to view existing orders and manage your own inventory for any designs that have been submitted. Go to your Lob dashboard and go to the section for [Buckslips](https://dashboard.lob.com/buckslips), [Cards](https://dashboard.lob.com/cards), or [Envelopes](https://dashboard.lob.com/envelopes).

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FvKGz8lIx9zM7M5rKO29O%2FScreen%20Shot%202022-11-10%20at%206.36.06%20PM.png?alt=media&#x26;token=6bdaf7a7-cd15-498b-b51c-6259c736b3b5" alt=""><figcaption><p>What your inventory management screen typically looks like (Envelope inventory in this example)</p></figcaption></figure>

### **Item details**

Depending on the custom mail type selected, you will see some of the following details of your ordered design:

* Design
* Size
* Type
* Finish

### **Inventory**

View the number of remaining custom items in your inventory and the number of orders that are still outstanding or fulfilled. Inventory statuses include:

* **Available:** Inventory currently in stock and ready to use&#x20;
* **Reserved:** Inventory allocated for scheduled campaigns&#x20;
* **Remaining:** Inventory available, less reserved inventory

Inventory for custom items will decrement as you send letters with the add-on item of a specific design, and increment if you cancel a letter request. It may take a few minutes for the inventory quantity to update after any action.&#x20;

Alternatively, use a `GET` call to the item endpoint to return a list of all items on your account, and any available and pending inventory.

* Buckslips: `https://api.lob.com/v1/buckslips`&#x20;
* Cards: `https://api.lob.com/v1/cards`&#x20;
* Envelopes: `https://api.lob.com/v1/envelopes`

### **Spoilage**

Accurate inventory management is essential for ensuring that we have the right products available to meet our customers' needs. Lob has automated tools and physical audits in place for regularly reconciling inventory, but we need to account for product spoilage. &#x20;

We are focused on addressing routine product spoilage that occurs during print set-up and assembly: Mailpieces generated during setup and testing are discarded along with any misprints or damaged pieces. For items printed on demand, this is not an issue, but for orders using pre-printed custom inventory, this ultimately impacts the accuracy of Lob's reported inventory.&#x20;

By addressing this issue and accounting for spoilage at the time of processing, we can improve the timeliness and accuracy of our inventory, to the benefit of your mail campaigns.

* **An auto-triggered overnight job will calculate spoilage from the previous production day and Lob will decrement it from your inventory accordingly.**
* **As a proactive measure, based on the industry average, we recommend adding 2-3% to account for spoilage when ordering custom inventory (custom envelopes, cards, buckslips).**

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FriYyIEZL1Am6NMGOrXIf%2FSpoilage_verbiage_in_UI.png?alt=media&#x26;token=5e7eeda2-909f-4b5b-bd1b-4b81b479c663" alt="" width="420"><figcaption><p>Sample spoilage message when ordering</p></figcaption></figure>

By addressing this issue and accounting for spoilage, we can improve the timeliness and accuracy of our inventory, to the benefit of your mail campaigns.

### **Auto-reordering**

Given add-on items require additional lead times for printing and stocking in inventory, we recommend enabling **auto-reordering** for any items that will be continuously utilized to ensure there will be no risk of running out. When reordering is turned on, a new order will be submitted whenever the remaining inventory quantity falls below 20%. A confirmation will show the reorder quantity and price that will be charged.

* **To turn on auto-reordering**:
  * Select the design you would like to auto-reorder&#x20;
  * Go to the Auto-Reorder Settings section, click Set Up, set auto-reorder to on, and hit Save&#x20;
  * Add a reorder quantity, the number of items to be ordered when your most recent order falls below 20% of the original order quantity, and hit Save
* **To turn off auto-reordering:**
  * Go into the same Auto-Reorder Settings&#x20;
  * Set the auto-reorder button to off, and hit Save

### **Order history**

Order details for any particular item design will be populated in the order history window once submitted, including order date, item ID, order quantity, inventory status, and expected availability date.

* **Order status**: Provides current item status&#x20;
  * Pending: Lob is reviewing the order submission&#x20;
  * In Production: The order is being fulfilled&#x20;
  * Available: Item is available in inventory and ready for use&#x20;
  * Expired: For envelopes only; indicates if envelopes expired (after 6mo)&#x20;
  * Canceled: Customer canceled order while status was pending
* **Estimated date**: Lob’s rough estimation of when items may be available in your inventory. However, an email confirmation will be sent when they are actually ready for use.&#x20;
* **Expand details**: Each order under a specific design can be expanded by clicking on the ‘+’ sign to the right in each row, where the expiration date (envelopes only), unit price, and total order cost will become visible<br>