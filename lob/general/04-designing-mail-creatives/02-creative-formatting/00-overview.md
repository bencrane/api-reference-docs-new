# Creative formatting

Every form factor starts with your creative, or the content of your mail piece. Lob’s core technology is built around modern APIs that remove the typical complexities and limitations of the print and mail industry. We can accept static PDFs, but similar to email sends, HTML enables dynamic personalization so each and every mail piece is unique.&#x20;

{% hint style="warning" %}
Please be sure to note that because you are ultimately responsible for ensuring compliance with all applicable laws and regulations, Lob can't offer guidance on the legality of your mailpieces and their content. For any questions of that nature, we always recommend consulting with the USPS and/or a qualified attorney.
{% endhint %}

## Example mail pieces <a href="#file-and-font-formats-12" id="file-and-font-formats-12"></a>

Artboard or layout templates can be found under each mail format (see [Mail piece design specs](https://help.lob.com/print-and-mail/designing-mail-creatives/mail-piece-design-specs)). Or, visit Lob's [Template Gallery](https://www.lob.com/template-gallery) on our website for pre-designed templates to help you get started; you can download these to use as inspiration and a guide to create your own designs.

## File formats for creative

### HTML for dynamic creatives <a href="#html-13" id="html-13"></a>

We recommend designing your direct mail in HTML to enable personalized content at scale. HTML allows you to include dynamic merge variables, similar to how you would personalize an email campaign, to maximize engagement and conversions.&#x20;

{% hint style="info" %}
See [dynamic personalization](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/dynamic-personalization) for more details on how to take advantage of HTML and merge variables.&#x20;
{% endhint %}

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FT0NWx2h7V4Y6xZYnUHm4%2FScreen%20Shot%202022-12-19%20at%2011.13.46%20AM.png?alt=media&#x26;token=307ca679-28a5-4069-914d-58d3be17fc46" alt=""><figcaption><p>Example translation of HTML for a postcard front</p></figcaption></figure>

### PDFs for static creatives <a href="#pdf-guidelines-14" id="pdf-guidelines-14"></a>

You can submit your creative file in PDF format, but keep in mind that PDFs are static and don’t support personalization.&#x20;

We ask that you follow our PDF formatting guidelines outlined in our [PDF preflight checklist](https://help.lob.com/print-and-mail/designing-mail-creatives/creative-formatting/pdf-preflight-checklist) to help ensure successful and accurate printing. Here are some tips to [create print-ready PDFs with InDesign.](https://help.lob.com/print-and-mail/designing-mail-creatives/creative-formatting/exporting-pdfs-from-indesign)

## Font formats <a href="#supported-font-formats-16" id="supported-font-formats-16"></a>

### Supported fonts <a href="#supported-font-formats-16" id="supported-font-formats-16"></a>

All fonts in any PDFs you provide should be embedded. Embedding a font in a PDF ensures that the final printed product will look as it was designed. Fonts can vary greatly in size and shape, even within the same family. If the exact font used to design the artwork is not used to print, the look and placement of the text is not guaranteed to be the same.

We make an exception for "standard fonts," a set of fonts that we have identified as being common. Otherwise, the request will be rejected. See our full list of [supported PDF Fonts](https://docs.lob.com/#section/Standard-PDF-Fonts) in our API docs.

We support the following web font formats:

* TTF
* SVG
* EOT
* Google web fonts
* Custom fonts within your HTML templates (any links must be [accessible](https://help.lob.com/print-and-mail/designing-mail-creatives/rendering-errors#html) to Lob)

### Unsupported fonts

* OTF  ([Can be converted](https://cloudconvert.com/otf-to-ttf) into another type we support)
* Type 1 fonts (Exception: standard base14 fonts)
* Type 3 fonts
* [Adobe (Typekit) fonts](https://en.wikipedia.org/wiki/Adobe_Fonts) (These fonts require white-listing a specific domain, which Lob is unable to do. We recommend hosting the font yourself and using it within your HTML, or finding an appropriate non-Typekit font to replace it with.)

## Image formats <a href="#image-formats-17" id="image-formats-17"></a>

**PNG:** This is a raster image format that can have a transparent background. It is generally of higher quality than other image formats.

**JPEG:** This is a raster image format that is often used for photographs. It does not allow for a transparent background.

When using PNGs or JPEGs with Lob, we require a minimum of 300 dpi. The dpi is calculated as (width of image in pixels) / (width of product in inches) and (length of image in pixels) / (length of product in inches). For example: `1275px x 1875px` image used to create a `4.25" x 6.25"` postcard has a dpi of 300. It is also recommended that you don't greatly exceed 300 dpi, as this will result in unnecessary additional file size.

Submitted images must have the same length-to-width ratio as the chosen product. Images will not be cropped or stretched by the API.

## Hosting content <a href="#hosting-content-20" id="hosting-content-20"></a>

When you pass an image or send HTML in your API request, Lob will then render and host the content.&#x20;

If you are sending at high volumes, we recommend you host the content yourself on a performant file hosting provider, such as Amazon S3, and send Lob a hosting URL to the content in your API request. This will reduce your API request time.

{% hint style="success" %}
All URLs must be accessible. For example, broken links,  missing files, and incorrect permissions will all cause mail pieces to fail.  See here if you are experiencing [rendering errors.](https://help.lob.com/print-and-mail/designing-mail-creatives/creative-formatting/rendering-errors)
{% endhint %}

## Design tools <a href="#rendering-best-practices-21" id="rendering-best-practices-21"></a>

We highly recommend using the Adobe Creative Suite (Adobe Illustrator, Photoshop, or InDesign) to design your content. This will give you design flexibility and multiple export options.&#x20;

{% hint style="warning" %}
Please note that PNG files are RGB only—to prepare a file for printing, our rendering engine must convert this color profile to CMYK. During this conversion, there may be a slight variance in color that would impact the print result. If you require a very specific color experience (to abide by brand guidelines for example), then we recommend providing a PDF file and/or evaluating the color in Adobe Photoshop Pro.&#x20;
{% endhint %}

#### Converting from PDF to HTML <a href="#converting-from-pdf-to-html-26" id="converting-from-pdf-to-html-26"></a>

If you want to take advantage of the personalization opportunities of HTML, we recommend using a developer to convert your PDF designs to HTML. We'd estimate 15 minutes to 2 hours of development time for the average file. Some applications like Adobe Illustrator come with HTML export options, but note that their exports won't typically produce HTML that conforms to Lob's requirements.

{% hint style="success" %}
**Need help with converting your creative files to HTML?** You can now easily import your creative from popular design programs and quickly spin up merge variables. See [Creative conversion tools](https://help.lob.com/print-and-mail/integrations/creative-conversion-tools) for more info on our design tool integrations.
{% endhint %}

## Proofing <a href="#rendering-best-practices-21" id="rendering-best-practices-21"></a>

To see how your HTML is rendered, create a Test API request either through the API or view a preview in the dashboard (HTML templates). Lob's HTML renderer is based on Webkit. For this reason, using the Safari browser will show previews more accurately.&#x20;

This works for PDFs as well as long as the submitted PDF follows [our guidelines.](https://help.lob.com/print-and-mail/designing-mail-creatives/creative-formatting/pdf-preflight-checklist) If a PDF not following guidelines is submitted, the rendered proof may not reflect the final printed product.

If using Campaigns in the dashboard, the Creative Proof will render and present a single mail piece. (It will include merge variables, address block, Lob carbon-neutral logo, and indicia, plus return address and QR codes if included.)

{% hint style="success" %}
We highly recommend sending yourself a printed piece to validate the mail piece's appearance.
{% endhint %}

<details>

<summary>Why does my design render differently with Lob than it does with my design tool?</summary>

This difference is likely due to variations found in the rendering engine of your design tool vs. web-based browser, which seemingly results in slight deviations.

* Design tools and web browsers are different mediums with different font-rendering engines. Put simply, design tools do not render based on CSS and HTML, as they are not web browsers. Different browsers (e.g., Safari vs. Chrome browsers) will show variations in rendering as well.
* Points, for measuring typeface, are not a precise measurement. Point size (or ‘pt’) refers to the bounding box of the letter — not the letter itself. Differences in font files and rendering engines may also add to the rendering discrepancy.
  * For example, if you create a PDF in Adobe InDesign, that tool’s rendering engine will define “11pt” font differently than what Lob’s web-based rendering engine defines “11pt” to be. Points, for measuring typeface, are not a precise measurement. In metal type, point size refers to the height of the metal body on which a typeface’s character is cast. In digital typefaces, the metal body is replaced by an invisible box known as the em square. Each character fits inside that em square or em box. The em size of a font is equal to its point size. The point size is also used to measure leading (line-height), line length and other elements, apart from font size.
  * Given the point size system is not based on a universal standard, any differences that exist are likely due to rendering engines. It is best practice to review requests in your Test Environment, prior to requesting them in the Live environment.
* The rendered image can also vary based on the DPI (Dots per Inch: a measure of the resolution of a printed document or digital scan) and zoom settings of your design tool vs. your web browser.

</details>

<details>

<summary>Why is the content of my mail missing?</summary>

If you are receiving a blank PDF when trying to render content, but the content of the link is not blank, it may be that the link was not performant. In order to avoid such issues, we recommend using a performant service, such as Amazon S3, to host the content.&#x20;

In order for this content to be visible, ensure that the link is set to public viewing, and not private, as this is one of the common reasons why content may appear as missing or blank in your creative.

</details>

<details>

<summary>What are these smudges on my postcards and/or self-mailers? </summary>

[Smears and smudges](https://blog.click2mail.com/articles/view/hey-how-did-that-happen-why-your-mail-gets-damaged-sometimes) are an industry-wide issue that has been extensively researched by our Production team. We've found that the USPS's high-speed sorting machines are what typically cause these scuff marks. If postcards or self-mailers get exposed to the belts for a millisecond longer than they're supposed to, they're at the risk of getting abrasions. This is not an isolated incident for our printer or for our mailers. Below links are a few articles that further explain the issue with examples of how these would look like.

&#x20;We are unfortunately unable to provide a refund or credits for these smudge marks.

</details>