# Artboard layout

{% hint style="info" %}
**Note**: All measurements are in inches, denoted by the double prime symbol (e.g. 4"x6").
{% endhint %}

## Artboard components <a href="#artboard-components-2" id="artboard-components-2"></a>

<div align="left"><figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FKcGo7YgH2PQd6zBtUlfy%2FScreen%20Shot%202022-12-19%20at%2010.15.38%20AM.png?alt=media&#x26;token=965d1fcb-ebb5-4999-8eb4-f3f6a6080e13" alt="" width="375"><figcaption><p>Example artboard: 4"x6" postcard</p></figcaption></figure> <figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FY2b7K0DfuTNNZNYTR3xm%2FArtboard-letter-6pagsorless.png?alt=media&#x26;token=864077c9-0cc5-4938-a9cc-2cffc6ec5a26" alt=""><figcaption><p>Example artboard 8.5"x11" letter</p></figcaption></figure></div>

### Mail piece size <a href="#mail-piece-size-6" id="mail-piece-size-6"></a>

The sizes of our mail pieces and their respective print layout requirements can be found in each respective section of the [Mailpiece design specs](https://help.lob.com/print-and-mail/designing-mail-creatives/mail-piece-design-specs) in the Help Center. Note that the API will return an error if you input a non-HTML file with the incorrect dimensions.

### Bleed area <a href="#bleed-area-3" id="bleed-area-3"></a>

In the above postcard, you'll notice that the file that you are sending to Lob is actually 4.25" x 6.25" instead of 4" x 6". This extra space is what we call the Bleed Area. The Bleed Area is included in postcards and self-mailers to ensure that creatives get printed all the way to the edge. This is because the creative gets printed with slightly larger dimensions than the actual card area and is subsequently trimmed down in production. Backgrounds and graphics should be extended into the Bleed Area. If they don't extend into the Bleed Area, it can result in a white or unprinted border on the edge of the postcard or self-mailer.

There is no need to include [crop marks](https://help.lob.com/print-and-mail/creative-formatting#avoiding-printers-marks-15) in your submitted content.

### Trim zone <a href="#trim-zone-4" id="trim-zone-4"></a>

The Trim Zone captures the finished size of a mail piece, which will result from the printer trimming down a larger sheet of paper. Artwork that extends into the Bleed Area will be trimmed down to the size of the actual mail piece.

### Safe zone <a href="#safe-zone-5" id="safe-zone-5"></a>

Keep all critical text and artwork within 1/8" from the edge of the final size to ensure no important content is ever trimmed off.

## No-ink zones <a href="#no-ink-zones-7" id="no-ink-zones-7"></a>

### Address block & postage <a href="#address-block-postage-8" id="address-block-postage-8"></a>

On our artboard templates, there is a space marked as **\*RED: INK-FREE AREA\*** on the backside of the mail piece. Anything in this area will not be printed, as this space is where the postage and address information will be printed during the production process.&#x20;

Address blocks for `4" x 6"` postcards measure `2.375" x 3.2835"`, and all other postcard, self-mailer, and snap pack blocks measure `2.375" x 4.0"`.

On letters, the address block is `3.15" x 2"` and is located 0.6" from the left edge and 0.84" from the top edge. A white box will be printed, upon which will be printed the address and barcode information. Any content in this area will be covered and will not be visible. &#x20;

On checks, the check itself will be printed at the `8.5" x 3.625"` area at the top. This area must thus be left blank. Anything printed in this area will not be printed to leave room for check details, including address information, payment amount, signature, and bank routing numbers. All text and important information should be included within the safe zone of the check bottom or check attachment pages. Special characters, such as emojis, should not be submitted for the address block.

### Carbon Neutral Mail Certification  <a href="#carbon-neutral-mail-certification-9" id="carbon-neutral-mail-certification-9"></a>

Lob is committed to setting a new [sustainability](https://help.lob.com/resources/sustainability) standard for direct mail and helping our customers and partners meet their sustainability goals. Lob has partnered with USPS to include a [Carbon Neutral Mail certification](https://www.lob.com/sustainable-direct-mail) to help customers demonstrate to their end-recipients that they are sending mail in an environmentally responsible way.

The Carbon Neutral Mail certification will automatically be included within the official use address block of postcards and self-mailers. (Support of this certification may be expanded to other mail types printed by Lob in the future.) **It will not impact your workflow or the way you design your creatives in any way.**

<table data-header-hidden><thead><tr><th width="229"></th><th></th></tr></thead><tbody><tr><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F1uDK9wiGvUIq5UtWLOiE%2FLob%20carbon%20neutral%20emblem%201.png?alt=media&#x26;token=35cbdc23-9de6-4eee-8d70-a09d53bb5c1f" alt=""></td><td>The certification measures <code>0.349" x 0.349"</code>, and is printed in either full color or black &#x26; white, depending on the letter settings. Address block placement and measurements for applicable formats can be found below. You will be able to see the Carbon Neutral Mail logo in the proof PDF.</td></tr></tbody></table>

For any questions on our Carbon Neutral Mail certification, reach out to your CSM or <support@lob.com>.

#### **Placement on postcards & self-mailers** <a href="#psc-sfm-placement" id="psc-sfm-placement"></a>

On postcards or self-mailers, the Carbon Neutral Mail certification will be placed between the return address, postage indicia, and IMb, within the [address block](#address-block-postage-8).&#x20;

This red area in our templates represent a white box, which will be printed on top of all submitted artwork to hold return and recipient addresses as well as the IMb information.

{% hint style="warning" %}
Be mindful of where the red address box of ink-free zone is placed on different-sized postcards and self-mailers in relation to the edge of the actual mailpiece (trim), as well as the middle fold for folded self-mailers.
{% endhint %}

<table><thead><tr><th width="350">Placement for 4x6" postcards only</th><th>Placement for all other postcards &#x26; self-mailers</th></tr></thead><tbody><tr><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FBnylMSfD45Pg0zckcAI8%2FScreen%20Shot%202022-12-19%20at%2010.18.39%20AM.png?alt=media&#x26;token=978fbdab-88a6-42e8-941e-798012d2508d" alt=""></td><td><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FaNBHdz77hT6Ti6cmmrP4%2FScreen%20Shot%202022-12-19%20at%2010.19.04%20AM.png?alt=media&#x26;token=7b807733-98c9-441f-a449-d50e1b376af0" alt=""></td></tr><tr><td><p>Address block size: <strong>2.375" x 3.2835"</strong></p><p></p><p>Placement <strong>within red box</strong>:</p><ul><li>From right: <strong>1.33"</strong></li><li>From bottom: <strong>1.69"</strong></li></ul></td><td><p>Address block size: <strong>2.375" x 4.0"</strong></p><p></p><p>Placement <strong>within red box</strong>:</p><ul><li>From right: <strong>1.33"</strong></li><li>From bottom: <strong>1.69"</strong></li></ul></td></tr></tbody></table>

### QR codes & sequence ID numbers <a href="#qr-codes-sequence-id-numbers-10" id="qr-codes-sequence-id-numbers-10"></a>

On letters and checks, there is a small QR code and a set of sequence IDs that will be printed on the bottom left corner during the mail production process, which are used as part of Lob's internal quality control process. These codes get scanned by cameras on our printers to ensure that the correct pages go into each corresponding mail piece as they get inserted into envelopes. They will both appear on each page that contains content, and cannot be removed.

<table data-header-hidden><thead><tr><th width="330"></th><th></th></tr></thead><tbody><tr><td><div><figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FzqC9J71QUaDmfa2kZ6oc%2FScreen%20Shot%202022-03-14%20at%203.07.05%20PM.png?alt=media&#x26;token=8e39b6cc-768d-4bc6-97ae-e95b82b021c4" alt=""><figcaption></figcaption></figure></div></td><td><p>While the red zone around the QR code is <code>0.5" x 0.5"</code> large, keep a <code>0.58" x 0.58"</code> sized area at the bottom left corner of the letter clear of any content as it will be covered and obscured by a white box that will be printed around the QR code.   </p><p></p><p>Sequence IDs itself are <code>1.45" x 0.09"</code> long, and is located 0.3" from the left edge and 2.2375" from the bottom edge of the page. Any content behind the sequence ID will be covered and obscured by a white box that will be printed to make the ID legible.</p></td></tr></tbody></table>

Plan your artwork submissions accordingly by avoiding printing any important text or artwork in the area saved for the printer QR code and sequence numbers.

## Intelligent Mail barcode <a href="#intelligent-mail-barcode-11" id="intelligent-mail-barcode-11"></a>

The [Intelligent Mail barcode (IMb)](https://postalpro.usps.com/mailing/intelligent-mail-barcode) is a 65-bar US Postal Service barcode used for mail sorting and tracking. It includes the routing ZIP and tracking information. USPS requires the use of the IMb in order for Lob's mail to benefit from automated processes.

## Prohibited artwork <a href="#prohibited-artwork-11" id="prohibited-artwork-11"></a>

**Stamp or indicia artwork**: There is a risk that the USPS will reject mail that includes artwork that resembles a stamp or fake indicia.&#x20;

* **Postcards & self-mailers**: Indicias are automatically printed within the [address block](#no-ink-zones-7) (see above section). Fake indicias should not be part of your submitted artwork elsewhere.
* **Custom envelopes**: There is no need to include indicia outlines in your artwork for the risk of rejection.

**Artwork near the indicia**: Artwork (such as eagles or American flags) is sometimes added to the left of an indicia box to add a sense of importance or urgency to a mailed piece. A 0.125" clearance on all sides from the indicia is necessary for this addition. &#x20;

<table><thead><tr><th width="316" align="center">Example: Fake indicia on postcard</th><th align="center">Example: Artwork too close to indicia</th></tr></thead><tbody><tr><td align="center"><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FwOVriUsKXVbDncia5RUc%2Fimage.png%2016-41-15-209.png?alt=media&#x26;token=fd2a290e-2420-4fd5-b3ec-5d65329b7658" alt=""></td><td align="center"><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1663702772720-Screen%20Shot%202022-09-20%20at%2012.39.11%20PM.png" alt="" data-size="original"></td></tr><tr><td align="center">Lob will print the actual indicia in the address block area. </td><td align="center">Leave enough space near indicia. No need to show the indicia box in artwork submissions, as Lob will print the indicia at the time of printing.</td></tr></tbody></table>

## Address "zone" warning

{% hint style="warning" %}
We do not recommend placing any address in your creative in the bottom 2.375" of a mailpiece opposite the address panel. This will prevent the USPS from accidentally scanning the wrong side of the mailpiece.
{% endhint %}

In the following example, promotional text (in the form of an address) included on the opposite side of the postcard could be mistaken by USPS scanners for the "To:" address.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FhYMgdIbaxc2AvUBMQmp9%2FBAD%20example.png?alt=media&#x26;token=0ca96fd1-38ae-4a20-83ca-eba7b0f66004" alt=""><figcaption></figcaption></figure>

Instead, if you would like to include a promotional address in your creative, we recommend you:

* Place it above 2.375" from the bottom OR&#x20;
* Choose light text on a dark background  (to clearly distinguish from the address/postage block)

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FQ05lYAdrO6CK3CL9tdlG%2FGOOD%20example%201.png?alt=media&#x26;token=0bb36b8a-1665-4475-ba1a-e62cd970d906" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FGU8WPRH7zM7kHYfmYXbN%2FGOOD%20example%202.png?alt=media&#x26;token=a443291b-e795-4aa6-a490-bdb4541ed44e" alt="" width="375"><figcaption></figcaption></figure>