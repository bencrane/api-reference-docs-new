# US AV product suite

Lob's Address Verification API is able to correct and identify over 156 million US domestic addresses (and more globally) to determine whether or not these physical addresses are deliverable. This is because Lob is [CASS (Coding Accuracy Support System) Certified](https://postalpro.usps.com/certifications/cass), meaning the API has been thoroughly tested by the USPS to ensure that it can accurately correct and validate street addresses. When our API confirms that a physical address is deliverable, you can be much more confident that your mail will be delivered.

## US Verifications <a href="#us-verifications-0" id="us-verifications-0"></a>

Validate, automatically correct, and standardize US domestic addresses based on USPS's [Coding Accuracy Support System (CASS)](https://postalpro.usps.com/certifications/cass). See our [API reference](https://docs.lob.com/#tag/US-Verifications) for more details.

If your addresses are returning as `undeliverable`, refer to the various fields in the US verification object in our [API reference](https://docs.lob.com/#tag/US-Verifications) for detailed definitions and explanations.

<details>

<summary>Supported US States &#x26; Territories</summary>

Our US Address Verification API supports the following states and territories:

* All 50 states
* Washington, D.C. (District of Columbia)
* Armed Forces (Africa - AE, Americas - AA, Canada - AE, Europe - AE, Middle East - AE and Pacific - AP)
* American Samoa
* Federated States of Micronesia
* Guam
* Marshall Islands
* Commonwealth of the Northern Mariana Islands
* Palau
* Puerto Rico
* The U.S. Virgin Islands

</details>

## US Autocomplete <a href="#us-autocomplete-2" id="us-autocomplete-2"></a>

Given partial address information, including optional input of city, state, and zip code, US Autocomplete returns up to 10 full US address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](https://docs.lob.com/#operation/verification_us). See our [API reference](https://docs.lob.com/#tag/US-Autocompletions) for more details.

Use of the US Autocomplete API is included with every Address Verification subscription. See our pricing page for different [Address Verification editions](https://help.lob.com/address-verification/ready-to-start-av/av-pricing) for more information.

## Reverse Geocode Lookup <a href="#reverse-geocode-lookup-3" id="reverse-geocode-lookup-3"></a>

Find a list of zip codes associated with a valid US location via latitude and longitude; a live API key is required to use this feature. See our [API reference](https://docs.lob.com/#tag/Reverse-Geocode-Lookups) for more details.&#x20;

## Zip Lookups <a href="#zip-lookups-4" id="zip-lookups-4"></a>

Lob's Zip Lookup tool can verify US zip codes without having to provide a full address. If the inputted zip code is real, Lob can return information about the zip code including a list of cities, states, and other associated information. If it's not a real zip code, Lob will return an "`invalid zip code`" error message. See our [API reference](https://docs.lob.com/#tag/Zip-Lookups) for more details.

## AV Elements <a href="#av-elements-8" id="av-elements-8"></a>

Lob Address Verification Elements verifies an address by intercepting the original form submission and pre-validating the address fields with Lob. Thus our APIs can be leveraged in customers' address entry workflows without any major rewrite required--just a few additional attributes to add to any existing markup, and it'll be running with a few minutes of work.

See our [AV Elements Quickstart guide](https://help.lob.com/address-verification/av-integrations-and-libraries/av-elements) to get started.

## Lob Confidence Score <a href="#lob-confidence-score-9" id="lob-confidence-score-9"></a>

The Lob Confidence Score is an object returned from the US verification endpoint that provides a value between 0-100 of the likelihood of the address being deliverable. Lob leverages its extensive insights, having sent mail to more than 1 in 2 US households, to generate a confidence score and provide more comprehensive address deliverability data.

Score definitions

* 70-100% - This address has received one or more successful deliveries
* 40-68% - This address has both mail returned to sender and successful deliveries
* 0-39% - This address has more mail returned to sender than successful deliveries
* None ("") - Lob does not have data on this address

Note that high scores do not guarantee deliverability. These are estimates based on Lob’s extensive mail tracking data.

See our [API reference](https://docs.lob.com/#operation/us_verification) under the JSON object `lob_confidence_score` for more details.