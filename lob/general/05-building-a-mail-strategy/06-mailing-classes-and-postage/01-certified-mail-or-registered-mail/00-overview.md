# Certified Mail or Registered Mail

### Certified Mail  <a href="#certified-mail-electronic-return-receipts-5" id="certified-mail-electronic-return-receipts-5"></a>

Certified Mail is an add-on service offered by USPS for First Class mail that provides proof of mailing to the sender. With electronic USPS [tracking](https://help.lob.com/getting-data-and-results/tracking-your-mail#tracking-information-for-registered-certified-mail-14), the sender is notified when the mailing was delivered or that a delivery attempt was made. An electronic return receipt showing the recipient's signature is also available for Certified Mail only. Both the Certified Mail and the electronic return receipt add-ons are only available for First Class mail sent domestically within the US.

You send letters as Certified Mail through the Lob API by passing the value `certified` in the `extra_services` parameter of the [create letter request](https://docs.lob.com/#operation/letter_create). You may similarly opt for an electronic return receipt by passing `certified_return_receipt` in the `extra_services` parameter in the [API](https://docs.lob.com/#operation/letter_create).

Tracking events are viewable directly within the Lob dashboard or via the API, similar to how they are for non-Certified letters, and you can also subscribe to webhook events for Certified letters. When you make a request for Certified Mail you will immediately receive a carrier tracking number (retrievable via your Lob dashboard), which can be used to track the mail via the carrier’s website - or you can choose to track the mail via the scan events within your Lob dashboard. The resulting screen should appear in your dashboard:

![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FQomFRb6j5FWeFyds23oV%2Fimage.png?alt=media\&token=5d0f16b4-a5ba-48fa-a3d3-98caa426a42a)

{% hint style="info" %}
Tracking events for Certified Mail are **different** from tracking events received for regular mail types; see the full list in our [API documentation for Certified tracking event details](https://docs.lob.com/#tag/Tracking-Events).&#x20;
{% endhint %}

Visit the [Certified Mail envelopes section](https://help.lob.com/designing-mail-creatives/mail-piece-design-specs/letter-envelopes#certified-mail-envelopes-1) for more guidance around sending Certified Mail.

### Electronic Return Receipts

An Electronic Return Receipt is available to the sender as a USPS [add-on](https://help.lob.com/ready-to-get-started/pricing-details#letters-6) to Certified Mail. This receipt will allow you to download a digital copy of the recipient's signature used to sign for the delivery of the letter. You opt for an Electronic Return Receipt by passing `certified_return_receipt` in the `extra_service` parameter of [creating a letter](https://docs.lob.com/#tag/Letters/operation/letter_create).

The return receipt will be accessible via the certified tracking number from the [USPS homepage](https://www.usps.com/). However, if you would like to receive the signature PDF via email, follow these steps:

* Visit [www.usps.com](http://www.usps.com/)
* Enter the Certified tracking number into the Track a Package box
* Click the "Return Receipt Email" dropdown and fill the required fields in the form

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FIT3cNArAtDQeGwuY4ytW%2Fexpected_delivery.png?alt=media&#x26;token=2dfab7a6-45c6-42ab-9c7e-906a372fcd89" alt=""><figcaption></figcaption></figure>

* The USPS will send you an email with the signature file like the below example

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Fok9tayGKPqp8GxSa4sQ7%2FPOD.png?alt=media&#x26;token=3a788df6-42d9-4b44-8990-d3e2c659fb4b" alt=""><figcaption></figcaption></figure>

### Registered Mail <a href="#registered-mail-6" id="registered-mail-6"></a>

{% hint style="success" %}
The USPS Registered Mail add-on is only available for First Class mail and can only be sent (and tracked) domestically.
{% endhint %}

Registered Mail is an add-on service offered by USPS that provides extra protection for high-value letters and packages. When you send a letter by Registered Mail, the USPS establishes a chain of custody that [tracks](https://help.lob.com/getting-data-and-results/tracking-your-mail#tracking-information-for-registered-certified-mail-14) and secures your shipment throughout the entire transit process—from the moment it is dropped off at the Post Office until the moment it’s delivered.

You can send letters as Registered Mail through the Lob API by passing the value `registered` in the `extra_services` parameter of the [create letter request](https://docs.lob.com/#operation/letter_create).

Letters sent as `registered` will receive a different set of scan events compared to regular First or Standard Class mail. Registered Mail will instead receive a carrier tracking number and link, which is an add-on that will be available 3 business days following the mailer’s `send_date`. This tracking number can be used to track the mailer via the carrier’s website.