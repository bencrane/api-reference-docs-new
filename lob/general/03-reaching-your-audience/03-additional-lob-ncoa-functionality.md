# Additional Lob NCOA functionality

{% hint style="info" %}
Customers must meet certain requirements to access this additional NCOA functionality. Please review the below and reach out to your Account Manager to see if you are eligible.
{% endhint %}

## NCOA overview <a href="#national-change-of-address-ncoa-7" id="national-change-of-address-ncoa-7"></a>

National Change of Address (NCOA) is a [service offered by the USPS](https://postalpro.usps.com/mailing-and-shipping-services/NCOALink), which allows individuals or businesses who have recently moved within the US to have any mail forwarded from their previous address to their new address.

As a CASS-certified Address Verification Provider, all mail sent through Lob Mail will be run through CASS and NCOA, as these are requirements for sending with USPS. Addresses will be corrected to reflect an individual's or business's new address in the case that they have moved (only if they have registered an NCOA with the USPS). The National Change of Address (NCOALink) database check only runs for US-based addresses. It does not run for non-US addresses or for non-deliverable US addresses.

## Additional Lob NCOA functionality

Lob also offers additional NCOA functionality to our Print & Mail customers, providing more visibility. Customers must meet certain requirements in order to access this functionality; please review the below and reach out to your Account Manager to see if you are eligible.

## Signing a Processing Acknowledgement Form (PAF) <a href="#signing-a-processing-acknowledgement-form-paf-8" id="signing-a-processing-acknowledgement-form-paf-8"></a>

In order to have the Lob NCOA report feature enabled, our customers must sign a Processing Acknowledgement Form (PAF), which is required by the USPS. NCOA reporting cannot be enabled if a PAF has not been signed.

Reach out to your Account Manager to see if you are eligible to sign a PAF.

## API-related changes <a href="#endpoints-affected-9" id="endpoints-affected-9"></a>

Due to privacy concerns and USPS constraints, for customers with the NCOA feature enabled, our API responses for a limited set of endpoints differ slightly in the case when an address has been changed through NCOA.

### Endpoints affected <a href="#endpoints-affected-9" id="endpoints-affected-9"></a>

With Lob NCOA feature enabled, there are no changes to API requests sent to Lob. This is true whether you are using our client-facing libraries, or making raw HTTP(S) requests to our API. If you have Lob NCOA reporting enabled, all live API requests to the following endpoints will be run through NCOA. However, there are some changes to the API responses for the following endpoints:

* `POST /v1/addresses`
* `POST /v1/checks`
* `POST /v1/letters`
* `POST /v1/self_mailers`
* `POST /v1/postcards`
* `POST /v1/campaigns`&#x20;
* `POST /v1/uploads`

### Response format <a href="#response-format-10" id="response-format-10"></a>

Though there are no changes to API requests received, there are significant changes to our API responses, but only in the event that an address has been changed through NCOA. If an address has not been changed through NCOA, the response would be identical to our standard API responses, except with the addition of a `recipient_moved` field, which is `false` for unchanged addresses.

Due to the USPS constraints mentioned above, if an address has been changed through NCOA, we are required to suppress the following response fields for that address:

* `address_line1`
* `address_line2`
* The +4 portion of the ZIP+4 (5-digit ZIP code will still be present).

**How do I know if an address went through NCOA?**

The black boxes in the address block mean the address went through our National Change of Address (NCOA) process. If you ever see the primary and secondary lines blotted out but not the city, state, and zip (without plus 4), that likely means it has gone through NCOA. If you’d like to know if an address went through NCOA, you’re also welcome to reach out to Lob support.

Below is an example of how this would look like in your Lob dashboard.

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FfnvCsIteLs5AiEF8TldX%2FScreenshot%202023-05-09%20at%2012.53.13%20PM.png?alt=media\&token=e97fb5da-4d63-4957-9ba2-c61d83b55423)

In addition, if an address has been changed through NCOA, the address will have a `recipient_moved: true` flag. For more details about the response format, see the NCOA information in our [API docs](https://docs.lob.com/#tag/National-Change-of-Address).

In addition to our API responses, the suppressed fields will (almost) always be suppressed in other places within the Lob platform as well. This includes:

* In the PDF proofs and thumbnails generated for Print & Mail requests
* In Exports for Postcards, Self-Mailers, Letters, Checks and Addresses resources
* API Logs & Event Logs
* Webhooks
* Dashboard Search

There are two locations where these fields are not suppressed:

* In the physical mail piece that will be sent to your customer.
* In an NCOA export from the Lob Dashboard (discussed in more detail below).

The NCOA export is the only way in which you will be able to access the suppressed response data for addresses that have been changed through NCOA.

## Accessing suppressed data <a href="#accessing-suppressed-data-11" id="accessing-suppressed-data-11"></a>

In order to allow our customers to access NCOA'd data, the USPS has given us the following constraint:

{% hint style="danger" %}
Customers must send at least 100 addresses through NCOA within one week in order to gain access to NCOA'd data.
{% endhint %}

This means that in order to access this data, you must send at least 100 live API requests in a one-week time span to any of the following endpoints:

* `POST /v1/addresses`
* `POST /v1/checks`
* `POST /v1/letters`
* `POST /v1/self_mailers`
* `POST /v1/postcards`
* `POST /v1/campaigns`&#x20;
* `POST /v1/uploads`

Additionally, the USPS has defined a "week" to be the following time ranges:

* 1st-7th of the month (inclusive)
* 8th-14th of the month (inclusive)
* 15th-21st of the month (inclusive)
* 22nd-28th of the month (inclusive)
* 29th-30th or 31st of the month (inclusive, when a month has more than 28 days)

Once you have sent at least 100 live API requests in a one-week time span, you can access suppressed data through an NCOA export, which can be accessed in the Lob Dashboard Settings, under the [Reporting](https://dashboard.lob.com/settings/reporting) tab.

Once in the Reporting Tab, you can select any week from the previous month or the current month, and generate an export for that week. Additionally, you have the option of only exporting addresses that have been changed during the NCOA process. This option is selected by default, as this tends to be the more useful option.

Once you have clicked the "Export" button, an email should arrive in your inbox with the exported data. Depending on how many requests you've sent and how many addresses have been changed through NCOA, this can take anywhere from a few seconds to a few hours.

The export is a CSV, which has the following fields:

* `id` - The Address ID (not the mailpiece ID) for the address that has been changed.
* `name` - The `name` passed with the API request.
* `company` - The `company` passed with the API request.
* `phone` - The `phone` passed with the API request.
* `email` - The `email` passed with the API request.
* `address_line1` - The full, unsuppressed `address_line1`, which represents the new address for the recipient.
* `address_line2` - The full, unsuppressed `address_line2`, part of the new address for the recipient.
* `address_city` - The city of the recipient's new address.
* `address_state` - The state of the recipient's new address.
* `address_zip` - The ZIP code (including the +4) of the recipient's new address.
* `address_country` - The country of the recipient's new address. Always `UNITED STATES`.
* `metadata` - The metadata associated with this address.
* `date_created` - The timestamp this address was created.

One important thing to note is that the export only includes an address ID, and not a resource (postcard/self-mailer/letter/check) ID. This means that you must keep track of address ID for inline addresses created in Postcard, Self-Mailer, Letter and Check requests.

Usually, NCOA records get updated once every two weeks contingent on USPS updating their internal database. **Since this is a recipient-led process, Lob does not have control over how often NCOA changes happen nor how often the database is updated by USPS.**

Whenever you send a mailing through Lob, you reap the benefits of accurate address cleansing and verification powered by our [CASS-Certified Address Verification API](https://docs.lob.com/#tag/US-Verifications). Verifying addresses is a necessary part of sending mail at scale, to optimize the efficiency and accuracy of your mail delivery.