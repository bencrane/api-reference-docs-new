# AV FAQs

### What are some address verification use cases?

Some customers love to use our address verification API to ensure addresses are accurate, deliverable and USPS standardized. Others love to use it for front-end autocompletion and to practice good data hygiene to prevent downstream bottlenecks. The possibilities are endless!&#x20;

### How often does Lob update their Address Verification API?&#x20;

It depends! For US verifications, our API updates on the 15th of every month, in accordance with USPS’s update schedule. For international verifications, our API updates in accordance with that specific country’s update schedule. For the update schedule by country, check out our Global Address Coverage page.&#x20;

### Why are my verified addresses returning in capital letters?&#x20;

By default Lob returns addresses in uppercase, to adhere with USPS' preference. If you prefer proper case you can configure this by changing the \[case] to "proper." Changing the case is only available to users sending in API requests programmatically. For more information, check our docs.&#x20;

### How do I keep track of the amount of verifications I’ve done?&#x20;

If you want to check how many verifications you completed in a given timeframe, there are two ways to get this done:&#x20;

1. Look at the Overview tab once you sign in to your Lob Dashboard and hover over the chart below the “API REQUESTS (BY CREATION DATE)” section. If you want to customize the time frame, then select a Start and End date, and hover over the chart for date or month-specific verification information.&#x20;
2. If you also want to see current month per-piece pricing:
   * Log in to your Lob Dashboard and click on Billing in the left navigation menu.
   * Click on “Editions”
   * Select the product you’d like to review usage for Select the product you’d like to review usage for
   * You should be able to see your usage settings under the “Current Month Usage”&#x20;

### Why is my address undeliverable?

There are various reasons an address can be deemed undeliverable, roughly grouped into four buckets below.&#x20;

* ZIP Code Types - components \[`zip_code_type`]&#x20;
* Record Types - components \[`record_type`]&#x20;
* Carrier Route Types - components \[`carrier_route_type`]&#x20;
* DPV Footnotes - deliverability\_analysis \[`dpv_footnotes`]&#x20;

The full list of detailed definitions for various fields in the US Verification object can be found in our [API docs](https://docs.lob.com/#tag/US-Verification-Types).&#x20;

### Why did my address verification fail when Google Maps was able to successfully find it?

Our API focuses on whether or not addresses are valid delivery points for receiving mail. Google Maps focuses on locality and walking/driving directions, and therefore should not be relied on for verifying the validity of a mailing address. An address that can be located on a map is not necessarily an officially recognized address by the USPS.

### What are the rate limits for the Address Verification API?

US and international verification of a single address (`v1/us_verifications` and `v1/intl_verifications`) allow 300 API calls per 5 second interval.

However, our bulk endpoints for US and interational verification have the following rate limits:

* US bulk verifications (`v1/bulk/us_verifications`) — 70 API calls per 10 second interval, passing a maximum of 20 addresses per API call
* International bulk verifications (`v1/bulk/intl_verifications`) — 30 API calls per 10 second interval, passing a maximum of 20 addresses per API call