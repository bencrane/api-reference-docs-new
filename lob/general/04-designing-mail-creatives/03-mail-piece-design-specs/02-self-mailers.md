# Self-Mailers

Self-mailers can grab attention with their creative design unfolding to tell your brand's story. They offer more room for your messaging but are folded to a compact size. Their all-in-one format eliminates the need for envelopes, encouraging immediate engagement from recipients and facilitating a quicker response.

{% hint style="info" %}
Self-mailers are exclusive to Enterprise edition customers. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this mail format, or reach out to our [sales team](https://www.lob.com/sales) to learn more.
{% endhint %}

Check out the following resources to get started with self-mailers

* API documentation: [Self-Mailers API](https://docs.lob.com/#tag/Self-Mailers) or [Campaigns API](https://docs.lob.com/#tag/Campaigns)&#x20;
* Lob dashboard: [Self-mailer](https://dashboard.lob.com/self-mailers) section or [Campaigns](https://dashboard.lob.com/campaigns/) for self-mailer campaigns&#x20;
* [GitHub library](https://github.com/lob/examples/) for HTML templates
* [Template Gallery](https://www.lob.com/template-gallery#folded-self-mailers) for ready-to-use creatives and design inspiration

## Self-mailer formats

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FFIbDeZDtSEvJy2EFffo2%2F23.10%20Trifold%20Chart%20Final%20Version.png?alt=media\&token=2f379c76-4cf6-4fa4-aa46-02c5927a7d3a)

## Layout dimensions & specs  <a href="#dimensions-and-specs-7" id="dimensions-and-specs-7"></a>

### Layout dimensions

Lob currently supports the following self-mailers:

* [6x18” bifold template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/6x18_sfm_bifold_template.pdf): measures 6x9” when folded in half, no offset of panels, and unfolds horizontally
* [12x9” bifold template](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/12x9_sfm_bifold_template.pdf): measures 6x9” when folded in half, no offset of panels, and unfolds vertically&#x20;
* [11x9" bifold template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/11x9_sfm_bifold_template.pdf): measures 6x9" when folded in half, has a 1" offset between the top and bottom panels when folded, and only unfolds vertically
* [17.75x9" trifold template](https://s3.us-west-2.amazonaws.com/public.lob.com/assets/Updated+9x17.75+Trifold+SFM.pdf): measures 6”x9" when c-folded inward, has a .25" offset on the bottom panel when folded, and only unfolds vertically.

Follow our design templates carefully to ensure you place your design elements for each permutation, including the location of the adhesive, in the appropriate location. (For example, there are four panels available to customize for all bifolds, wherein one of the outside panels must have an [ink-free zone](#ink-free-zone-dimensions-8) for the address and postage area.)&#x20;

{% hint style="warning" %}
**Make sure all artwork submissions are facing upright for both inside and outside panels.** Our printers will invert the inside panel of submitted customer artwork during the production phase.&#x20;
{% endhint %}

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887499459-1641887499459.png)

### Paper specs

We use a few pre-approved papers across our commercial printer network. In ensuring uniform quality and consistency across all of our mail pieces, each paper source specification must fall within a small range. The specification/value range pairs are listed below:

* Basis Weight: 80# Cover with Gloss
* GSM: 218
* Full Bleed
* 1 Side UV Gloss

### Ink-free zone dimensions <a href="#ink-free-zone-dimensions-8" id="ink-free-zone-dimensions-8"></a>

* 6x18" bifold self-mailer
  * W x H: 4 x 2.375"
  * 0.15" from the center fold line
  * 0.25" from the bottom edge (including bleed)
  * Placement: Left panel outside
* 12x9" bifold self-mailer
  * W x H: 4 x 2.375"
  * 0.15" from the center fold line
  * 0.25" from the right edge (including bleed)
  * Placement: Top panel outside
* 11x9" bifold self-mailer
  * W x H: 4 x 2.375"
  * 0.15" from the center fold line
  * 0.25" from the right edge (including bleed)
  * Placement: Top panel outside
* 17.75x9" trifold self-mailer&#x20;
  * W x H: 4 x 2.375" 0.15" from the center fold line&#x20;
  * 0.25" from the right edge (including bleed)&#x20;
  * Placement: Top panel outside&#x20;
  * Glue zone 9”x.5” (at 12” score)

{% hint style="info" %}
A Carbon Neutral Mail certification will automatically be included within the official use address block on the backside for all bifold self-mailers printed by Lob. Read more about how you can send mail in a more environmentally responsible way with Lob in our [Carbon Neutral Mail](https://help.lob.com/print-and-mail/artboard-layout#carbon-neutral-mail-certification-9) section.
{% endhint %}

## Self-mailer adhesives <a href="#self-mailer-adhesives-9" id="self-mailer-adhesives-9"></a>

Stain-resistant, low tack, clear fugitive glue is used for adhesives on the folded self-mailers.

Glue is positioned within 0.25" of the opening edges and placed opposite the final fold. Glue is applied by one of the following methods:

* Continuous glue line at least 0.125" wide&#x20;
* Three or four glue spots at least 0.375" in diameter
* Three or four elongated glue lines

## Self-mailer best practices <a href="#design-best-practices-10" id="design-best-practices-10"></a>

Ensure your self-mailers get to their final destination by following these guidelines:

* The `from` field is required for all self-mailers, regardless of the destination
* Self-mailers should not contain any PII outside of the [no-ink zone](https://help.lob.com/print-and-mail/artboard-layout#address-block-postage-8)
* Avoid any [prohibited artwork](https://help.lob.com/print-and-mail/artboard-layout#prohibited-artwork-11) to ensure your mail does not get rejected by USPS &#x20;
* HIPAA-compliant self-mailers are not offered at this time, as self-mailers are not placed in envelopes
* [Mailing Class](https://help.lob.com/building-a-mail-strategy/mailing-classes-and-postage#available-mailing-class-options-5) options may differ based on destination and use type (e.g. promotional vs non-promotional)
* We do not recommend placing promotional address information in your creative in the bottom 2.375" of a mailpiece opposite the address panel. This will prevent the USPS from accidentally scanning the wrong side of the mailpiece.  [Learn more here. ](https://help.lob.com/print-and-mail/artboard-layout#address-zone-warning)