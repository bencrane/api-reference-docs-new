# Letters

Letters are highly effective for direct marketing due to their personal touch and tangible presence, enhancing recipient engagement. They also serve well for transactional or operational communications, offering a formal and reliable delivery of important information that stands out from digital clutter.

Lob offers two sizes of letters: 8.5x11" and 8.5x14".&#x20;

To get started with sending letters, check out our [Letters API documentation](https://docs.lob.com/#tag/Letters), our [GitHub library](https://github.com/lob/examples/), or Lob's [Template Gallery](https://www.lob.com/template-gallery#letters) for inspiration.&#x20;

## Layout dimensions & specs <a href="#dimensions-specs-1" id="dimensions-specs-1"></a>

### **Layout dimensions**

**8.5x11" letters**

Lob offers `8.5" x 11"` letters in both black & white and in color, which can be printed single or double-sided. Letters and checks not exceeding 6 tri-folded sheets of paper in total will be sent in standard [#10 double-windowed outer envelopes](https://help.lob.com/print-and-mail/designing-mail-creatives/letter-envelopes#standard-10-double-windowed-outer-envelope). Letters and checks over 6 sheets of paper but not exceeding 60 total sheets of paper will be mailed in a [flat envelope](https://help.lob.com/print-and-mail/designing-mail-creatives/letter-envelopes#9-x-12-single-window-flat-outer-envelope).&#x20;

Reference our design templates on where to place your design elements for letters; carefully note the placement of the address block.

* [Letter design template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/letter_template_updated+4_25.pdf) (for 6 sheets of paper or less)
* [Letter design template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/letter_flat_template_updated+4_25.pdf) (for over 6 sheets of paper but not exceeding 60)

Lob standard letters cannot accommodate letters that bleed or print edge-to-edge. All text and design must be 1/16” from all sides leaving the required 1/16” clear space on all sides.

<details>

<summary>What is that small QR code printed on my letters? </summary>

What looks like a small QR code printed on letters is a data matrix, a type 2D barcode used by our print partners to encode information to facilitate efficient sorting, tracking, and delivery. Recipient attempts to scan this code won't direct anywhere, but cameras read these small barcodes during the automation process. Typically, this appears on the lower corner of letters (as noted on our templates), though some print partners may place it in the address block area (as shown below).

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FCy09g0n0is5N5tQpqw8Z%2Fsample2D_addressblock.png?alt=media\&token=352e2014-5947-467f-af79-6aa4797977f1)

</details>

<details>

<summary>What is the difference between a page and a sheet of paper?</summary>

A "page" in the context of a Lob letter is a PDF page, while a "sheet" refers to the physical paper that is used to print the letter. Lob charges based on the length of a letter in PDF pages, while the length of a letter in sheets is used to determine what envelope a letter uses.&#x20;

</details>

**8.5x14” Letters (“Legal letters”)**

{% hint style="info" %}
Legal letters are exclusive to Enterprise edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this mail format, or reach out to our [sales team](https://www.lob.com/sales) to learn more.
{% endhint %}

{% hint style="success" %}
Legal letters currently have a 4-day SLA.
{% endhint %}

Lob offers 8.5x14" letters in both black & white and in color, which can be printed single or double-sided.

Using two parallel folds, a legal-sized letter is folded in half, then folded again *with a slight overlap* (two edge panels will be slightly larger than the middle panels); this allows it to fit in a standard #10 double-windowed outer envelope. Legal letters cannot exceed 3 sheets of paper at this time.&#x20;

Reference our design templates on where to place your design elements for letters; carefully note the placement of the address block.

* [Legal letter design template ](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/Legal_Letter_updated_4_25.pdf)(3 sheets of paper or less)

Lob Legal letters cannot accommodate letters that bleed or print edge-to-edge. All text and design must be 1/16” from all sides leaving the required 1/16” clear space on all sides.

<details>

<summary>What is that small QR code printed on my letters? </summary>

What looks like a small QR code printed on letters is a data matrix, a type 2D barcode used by our print partners to encode information to facilitate efficient sorting, tracking, and delivery. Recipient attempts to scan this code won't direct anywhere, but cameras read these small barcodes during the automation process. Typically, this appears on the lower corner of letters (as noted on our templates), though some print partners may place it in the address block area (as shown below).

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FCy09g0n0is5N5tQpqw8Z%2Fsample2D_addressblock.png?alt=media\&token=352e2014-5947-467f-af79-6aa4797977f1)

</details>

### Paper specs&#x20;

We use a few pre-approved papers across our commercial printer network. In ensuring uniform quality and consistency across all of our mail pieces, each paper source specification must fall within a small range. The specification/value range pairs are:

* 8.5" x 11" B\&W & color letters
  * Basis Weight: 60# text
  * C-fold letters
* 8.5" x 14" B\&W & color letters
  * Basis Weight: 60# text
  * Double parallel fold

### Address placement <a href="#address-placement-2" id="address-placement-2"></a>

If you do not follow these address guidelines, your letter will be printed incorrectly.

The `address_placement` parameter specifies the location of the address information that will show through the double-window envelope. Options are `top_first_page` and `insert_blank_page`.

By default, Lob selects `address_placement = top_first_page`, meaning Lob will print address information at the top of your provided first page. Make sure to leave ample space for the address information to be printed, which will show through our standard double-windowed envelope. To see how this will impact your letter design, view our [letter template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_template.pdf) (6 sheets or less).

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F4UJ6M1fAHr0vSu1oo7uh%2Fletter%206%20pages%20or%20less.png?alt=media&#x26;token=e78bdc7e-40a4-414b-bd79-04dee0e44289" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Letters may shift slightly within their envelope during transit. As such, we do not recommend putting any sensitive content close to the window area.
{% endhint %}

If you pass `address_placement = insert_blank_page`, a blank address page will be inserted at the beginning of your file where we will print the address information to show through our standard double-windowed envelope.&#x20;

{% hint style="danger" %}
If a blank address page is inserted, note that you *will* be charged for the extra page. Reference the [Letter Unit Pricing section](https://help.lob.com/ready-to-get-started/pricing-details#letters-6) for charges you will incur based on your tier.&#x20;
{% endhint %}

### Logo placement <a href="#mailing-letters-3" id="mailing-letters-3"></a>

Your logo should be entirely within the blue box of the letter template, with no overlap of the red box, in order to print appropriately.&#x20;

If you're looking to print a color logo then ensure you're setting the color parameter to 'true' if you would like to print in color otherwise you can set it to false.

## Letter best practices <a href="#mailing-letters-3" id="mailing-letters-3"></a>

Ensure your letters get to their final destination by following these guidelines:

* The `from` field is required for all letters, regardless of the destination
* Letters may contain PII as envelopes have an [interior security tint](https://help.lob.com/print-and-mail/designing-mail-creatives/letter-envelopes#standard-letter-outer-envelopes-0) for privacy
* [Mailing class](https://help.lob.com/building-a-mail-strategy/mailing-classes-and-postage#available-mailing-class-options-5) options may differ based on the destination and use case (e.g. promotional vs transactional)

## &#x20;<a href="#using-certified-mail-or-registered-mail-4" id="using-certified-mail-or-registered-mail-4"></a>