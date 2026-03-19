# AV best practices

One of the most prized value propositions of our Address Verification solution is our access to detailed USPS deliverability data which provides a clear, binary value as to whether or not an address is capable of receiving mail. Because Lob sends millions of mailpieces, we also have the data and the intelligence to provide more context that can be useful when considering whether or not to send mail to a specific address.

This useful information is returned to you in the Address Verification API response; [see a response sample here](https://docs.lob.com/#tag/US-Verifications/operation/us_verification).

## What you’ll see in the AV API response

### Deliverability

The USPS returns empirical data to Lob on whether or not an address is deliverable (returned in the `deliverability` field), but it’s important to keep in mind the term “deliverable” is literal here— while the address itself may literally be deliverable, it does not guarantee the intended recipient can/will accept mail upon delivery attempt.

This is where it becomes important to make further analysis of the API response.

### Address Type

While evaluation on this metric doesn’t really have a bearing on the number of successful deliveries in your campaign, under `components`, the `address_type` field contains human-readable definitions for the type of the specified address.

Address type may be very relevant, depending on the goal of your campaign. For example:

* Realtors may only be interested in addresses with an `address_type` of “residential”
* A startup pitching to companies may only be interested in those noted as “commercial”
* Those who wish to opt-out of sending mail to more rural areas would want to filter out address types returned as “rural route”

A full list of address types can be found [here.](https://docs.lob.com/#section/US-Verifications-Test-Env)

### Delivery Point Validation (DPV)

Under `deliverability_analysis` we provide more information about addresses. [Delivery Point Validation](https://postalpro.usps.com/address-quality/dpv) provides the highest level of address accuracy-checking: the address is checked against the USPS Address Management System (AMS) data file to ensure that it exists as an active delivery point to where mail can be delivered. DPV is intended to confirm USPS addresses but also identify potential addressing issues that may hinder delivery. Several sub-fields are included in DPV data to provide additional context on the given address; these fields are one of many variables factored into USPS decision-making when determining deliverability.

The `dpv_active` field corresponds to the USPS field `dpv_no_stat`. Even if an address is deliverable by definition, it could still be flagged as "`N`" for inactive. "`N`" indicates an address is not receiving deliveries for one reason or another:

* the address has been vacated recently
* the address has been unoccupied for 90+ days, thus considered temporarily vacant
* the address does not wish to receive mail for unspecified reasons

{% hint style="danger" %}
**Remember:** If an address returns a `dpv_active` status of “`N,`” any mail sent to this address is at risk of being returned to sender.
{% endhint %}

### Lob Confidence Scores

The[ Lob Confidence Score](https://help.lob.com/address-verification/ready-to-start-av/us-av-product-suite#lob-confidence-score) (`lob_confidence_score`) is our prediction of successful delivery based on our historical data for an address. If we sent 10 mailpieces to an address, and all 10 were successfully delivered, the address would have a score of 100. If we sent 10 mailpieces to an address, but 8 were [returned to sender](https://help.lob.com/print-and-mail/getting-data-and-results/tracking-your-mail#undeliverable-mail-9), it would have a much lower score of 20. Our Confidence Scores are updated monthly to reflect new delivery attempts.

You may want to consider using the Confidence Score based on the [type of mail](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#mail-use-type-1) that you send:

* If you are sending operational mail, you may only need proof that the mailpiece was sent to a valid address on file, and successful delivery may not be as important.
* **If** **you are sending marketing mail, it is strongly suggested that you consider this field before sending**, as addresses with Confidence Scores under 100 indicate the address has rejected mail before.&#x20;

## Return to sender (RTS) rates

Without validation, the industry average RTS rate is 5-10%, but through the use of our AV solutions, we see customers with an average RTS rate of 2% or less. Historically, mail campaigns have been prone to imperfection, but through the use of the best practices provided, return-to-sender rates can be driven lower.

## Cache if you can!

Lastly, for customers working with full tech stacks, we highly recommend caching responses to our AV endpoint, as prices are made per API call. So, if an end-user has made a request for the validation of an address (ex: “210 King St, San Francisco, CA”), cache this result internally for at least 24 hours. Now, if another customer attempts to validate that same address, you can pull it from the cache instead and are only charged for the original API call.