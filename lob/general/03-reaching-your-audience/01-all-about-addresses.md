# All about addresses

## Anatomy of a mailpiece <a href="#ispasted" id="ispasted"></a>

When you send an API request to Lob, you are sending 3 pieces of information:&#x20;

1. the "To" address,&#x20;
2. the "From" address, and&#x20;
3. the content.

Below are some best practices to follow around **formatting your address data** with Lob.

## What's an address? <a href="#whats-an-address-0" id="whats-an-address-0"></a>

An address gives the location of a structure or land using identifiers to help with navigation to that location. They also aid in the routing of mail.

The delivery address is the most important information on your mail piece. Use the following format for your delivery addresses:

1. Name (or attention)
2. Company\* (if applicable)
3. Delivery address: Line 1, and Line 2\* (if applicable)
4. City, State, ZIP Code, Country\*

Items marked with a **\*** are optional.&#x20;

{% hint style="success" %}
For more details on character limits etc., reference our [API docs](https://docs.lob.com/#tag/Addresses/operation/address_create) or see the [Formatting fields and record values](https://help.lob.com/print-and-mail/campaign-audience-guide#formatting-field-and-record-values) in our Campaigns audience guide.
{% endhint %}

## Address book <a href="#address-book-1" id="address-book-1"></a>

The Address Book is a collection of a customer’s addresses uploaded and stored in our system, which can be accessed in the [Lob dashboard](https://dashboard.lob.com/addresses) or you can leverage the `address_id` to [retrieve](https://docs.lob.com/#operation/address_retrieve) that entry's information programmatically. Rather than passing the full address + mail information in one API call, customers can also pass the `address_id` (provided upon creating the address in the address book) that will look for the associated address information. This makes requests faster and simpler.

### Standardization & verification <a href="#standardization-verification-2" id="standardization-verification-2"></a>

We cleanse all newly created addresses in order to optimize for maximum deliverability.&#x20;

* All US addresses will be automatically standardized, cleansed, and verified through our [CASS-Certified Address Verification system](https://lob.com/solutions/address-verification) before being returned back to you in the API response.&#x20;
* All international addresses will simply be standardized by being transformed to all uppercase.&#x20;

Mail requests will be run through [CASS](#coding-accuracy-support-systems-cass-3) and [NCOA](#national-change-of-address-ncoalink-r), as these are requirements for sending with USPS. This may result in the final mailing address being different from the ones you see in your API requests and Dashboard.

#### Coding Accuracy Support Systems (CASS™) <a href="#coding-accuracy-support-systems-cass-3" id="coding-accuracy-support-systems-cass-3"></a>

The [Coding Accuracy Support Systems (CASS™)](https://postalpro.usps.com/certifications/cass) certification process is designed in cooperation with the mailing industry to improve the accuracy of postal codes, i.e., Five-Digit ZIP Code, ZIP+4, delivery point codes (DPCs), and carrier route codes that appear on mail pieces.

Lob is CASS™ certified [(Cycle O)](https://postalpro.usps.com/CASS_CycleO_Summary) to ensure your addresses are standardized before any mail is sent.

#### National Change of Address (NCOALink®)

[National Change of Address (NCOALink)](https://postalpro.usps.com/mailing-and-shipping-services/NCOALink) is a service offered by the USPS, which allows individuals or businesses who have recently moved to have any mail forwarded from their previous address to their new address.&#x20;

Addresses will be corrected to reflect an individual's or business's new address in the case that they have moved (only if they have registered an NCOA with the USPS). The National Change of Address (NCOALink) database check only runs for US-based addresses. It does not run for non-US addresses or for non-deliverable US addresses. [For more visibility of address changes, learn more about additional NCOA functionality offered here.](https://help.lob.com/print-and-mail/reaching-your-audience/additional-lob-ncoa-functionality)

### Adding & deleting addresses <a href="#adding-deleting-addresses-4" id="adding-deleting-addresses-4"></a>

You cannot edit any existing addresses via the dashboard or API request. You can however delete the current address and add a new one with the updated information. For more details on adding a new address to your address book, refer to the [API documentation](https://docs.lob.com/#tag/Addresses).

If you are interested in mass-deleting addresses, you will need to set up a delete address request script. See more details on deleting in our [API documentation](https://docs.lob.com/#operation/address_delete).

Note that Lob is not permitted to add or delete addresses on behalf of customers.

## Autoverify <a href="#autoverify-5" id="autoverify-5"></a>

Autoverify is included in all US Print & Mail subscriptions. Lob verifies the deliverability of all addresses before sending a request to our print partners.&#x20;

### Strictness settings <a href="#strictness-settings-6" id="strictness-settings-6"></a>

Depending on what business logic you'd like to take, based on your verification result, you can toggle your US address strictness settings in your [Lob dashboard](https://dashboard.lob.com/#/settings/account). There are three possible strictness levels: **Strict**, **Normal**, and **Relaxed**.&#x20;

Learn more about the importance of [mail strictness settings](https://help.lob.com/building-a-mail-strategy/managing-mail-settings#us-mail-strictness-settings-2) and how to adjust them as required by your business.

## Using "Current Resident" as the recipient

The purpose of including "Current Resident" as the recipient of your mailpiece is to ensure that your message reaches its intended audience. This serves well in a case in which you're uncertain that the person(s) living at that address are the intended recipients and you do not wish to risk offending the current residents by potentially sending someone else's mail. Using the phrase "Current Resident" can be a good idea if your mailpiece is time-sensitive and the recipient may be variable.

To make an informed decision on whether or not to include the phrase, consider the purpose of your mailpiece and your target audience:&#x20;

* If your mailpiece is intended to be a personal communication or a marketing message that relies on building a relationship with your audience, then you **may want to avoid** using the phrase "Current Resident." Learn more about [dynamic personalization](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/dynamic-personalization) here.
* On the other hand, if your mailpiece is informational and the message is more important than the recipient, then you **may want to include** the phrase, as any recipient can still respond.

To indicate your recipient as "Current Resident," simply provide that as the `name` value where you would normally input a recipient's full name.