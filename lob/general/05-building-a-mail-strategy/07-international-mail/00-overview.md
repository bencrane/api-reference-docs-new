# International mail

{% hint style="info" %}
This page is regarding mail that **originates in the US** and is mailed abroad by the USPS. If you have further questions about sending mail internationally, [contact us](mailto:support@lob.com).
{% endhint %}

## General considerations

### **Mail formats**

* [Postcards](https://docs.lob.com/#tag/Postcards) and [letters](https://docs.lob.com/#tag/Letters) created using the individual mail creation endpoints can be sent internationally, Campaigns UI (non-custom formats) and Campaigns API (non-custom formats); see below for [format-specific considerations](#format-specific-considerations-2)
* No checks can be sent (or cashed) abroad

### **Mailing class**

* Only USPS First Class Mail is available for international delivery
* Expect international mail to take an additional 5-7 business days
* Registered Mail is not supported internationally
* Certified Mail is not supported internationally
* Standard class (Bulk/Marketing Mail), Nonprofit stamps, or First Class Presort are not permitted in international mail and will be returned to sender

### **Destination address**

* Lob follows [USPS standards](https://pe.usps.com/text/imm/immc1_008.htm) for sending international mail
* International address data is available in over 240 countries, and the complete list of countries and territories can be found in our [global address coverage](https://www.lob.com/global-address-coverage) page
* To pass country codes in the API, use the specific two-letter convention identified by the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) convention (e.g., ‘US’ for United States of America, or ‘CA’ for Canada)
* Lob follows USPS’s guidance on [international service disruptions ](https://about.usps.com/newsroom/service-alerts/international/welcome.htm)that affect First Class Mail delivery abroad
  * Our Print & Mail API will be periodically updated to exclude country-specific mail delivery suspensions. If you attempt to send mail to a suspended destination, you will receive a `422` error.&#x20;
  * We will lift service restrictions in accordance with any USPS-provided guidance.&#x20;
  * Temporary service disruptions (due to conditions like wildfires or COVID-19 for example) are subject to change.

### **Non-Latin/non-standard character support**

**For the address box:**

* Name and company will remain as-is within their respective character sets
* If our Address Verification can validate and translate the address portion, it will return the address in English
* All international mail will not receive CASS processing beyond US borders by default, so be sure to have accurate addresses if sending with your respective character set&#x20;

**For the content of the HTML body:**

* Must be using a typeface (font) that supports the character set
* Must include meta element with utf-8 charset: \
  `<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>`
* Example:

<pre class="language-html"><code class="lang-html"><strong>&#x3C;html>
</strong><strong>&#x3C;meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</strong>&#x3C;body>
&#x3C;b>Chinese characters in UTF-8&#x3C;/b>&#x3C;br/>
Simplified characters: 简体中文网页&#x3C;br/>
Traditional characters: 繁體中文網頁&#x3C;br/>
Korean characters: 빠른 갈색 여우가 게으른 개를 뛰어 넘다&#x3C;br/>
Arabic characters: الثعلب البني السريع يقفز فوق الكلب &#x3C;br/>
Vietnamese characters: Ăă
&#x3C;/body>
&#x3C;/html>
</code></pre>

### **Return address**

* US-based return addresses are **required** on all outbound international mail, regardless of the mail service used
* All outbound mail pieces (“`to`” address is international) must bear a complete return address in the country of origin (e.g. where you pay postage)
* Since Lob mail is originated in the US, the return **must** have a US-based address

### **Mail tracking**

* For international mailings originated in the US, [tracking events](https://help.lob.com/getting-data-and-results/tracking-your-mail#tracking-events-2) will not appear and tracking data cannot be accessed via the USPS’s website beyond the final scan in the US, "International Exit"
  * Note: USPS does not appear to scan the majority of their international mail, which means this "International Exit" event is unreliable and thus infrequently surfaced   &#x20;
* On rare occasion, international mailings may receive an "In Transit" or "Process for Delivery" scan, indicating that the mail piece has been processed at the entry/origin facility outside of the US&#x20;
  * However, because delivery occurs in a foreign country outside the control of the USPS, international mailings do not receive scans beyond that, and cannot be tracked through the mailstream&#x20;
* In short, Lob is unable to provide reliable scans for international mail, especially beyond US borders

## Format-specific considerations  <a href="#format-specific-considerations-2" id="format-specific-considerations-2"></a>

### Postcards <a href="#postcards-3" id="postcards-3"></a>

* [Per USPS](https://pe.usps.com/text/dmm100/mailing-international.htm), only 4x6" size postcards can be sent internationally via First Class Mail

### Letters <a href="#letters-4" id="letters-4"></a>

* File limit is 6 sheets single-sided or 12 pages double-sided (totaling 6 sheets)
  * PDFs that surpass the file limit will error
  * HTML that renders more pages than the file limit will be trimmed
* While Registered Mail International service items also ***cannot*** be tracked, it does provide [delivery status or attempted delivery information](https://faq.usps.com/s/article/What-is-Registered-Mail-International#tracked) which can be obtained through USPS in three ways:
  * Go to [www.usps.com](http://www.usps.com/). Select "[USPS Tracking](https://tools.usps.com/go/TrackConfirmAction_input)." By entering the tracking number shown on the mailing receipt into the lookup field, you can view the delivery status of the article
  * By calling the USPS Tracking telephone number found at [Contact USPS](https://www.usps.com/help/contact-us.htm?_gl=1*b4xkq3*_ga*MTgzMzI1ODc5NC4xNjU3NTY0NTg4*_ga_3NXP3C8S9V*MTY1NzU2NDU4OC4xLjAuMTY1NzU2NDU4OC4w#kilo)
  * By bulk electronic file transfer for mailers who provide an electronic manifest to the United States Postal Service

### Checks <a href="#checks-5" id="checks-5"></a>

* Checks cannot be sent internationally, and the API will return an error if `address_country` is not the US.

### Campaigns UI specific considerations <a href="#checks-5" id="checks-5"></a>

* Start your campaign and choose "Includes International" on the first step. This tells the system you want to follow international mailing rules.
* The Campaigns UI will then guide you through the USPS requirements. This ensures your maipiece is properly formatted and is set up for successful delivery.&#x20;

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FlMkiIJTXaViZCMTKJKqN%2FScreenshot%202024-10-16%20at%2011.29.55%E2%80%AFAM.png?alt=media&#x26;token=d4931a18-ce4e-4f6e-a94d-d8965d488a4f" alt=""><figcaption></figcaption></figure>