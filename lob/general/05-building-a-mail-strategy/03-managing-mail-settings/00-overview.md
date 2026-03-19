# Managing mail settings

As you use the Lob API to send mail programmatically, it is important that you manage your account settings to send mail so that they accurately reflect the needs of your business workflows and the frequency of your customer engagements and outreach. Most of the following settings can be adjusted via the API or in your [Lob dashboard](https://dashboard.lob.com/#/settings).

## Mail use type <a href="#mail-use-type-1" id="mail-use-type-1"></a>

For any mail piece that is sent through Lob, you will need to indicate which mail use type is being sent. This helps Lob populate the right mail settings and postage options to ensure your mail is produced and delivered in an optimal way.&#x20;

The following use type options are available for your mail pieces:&#x20;

* **Marketing mail**: These are mail pieces sent for promotional purposes, such as for acquisition, cross-sell, retention, or win-back campaigns.
* **Operational mail**: These are mail pieces sent for transactional purposes as part of your trusted business outreach and customer communications, such as account notifications, invoices and payment, policy changes, service announcements, or other similar reasons. &#x20;

See [Declaring mail use type](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/declaring-mail-use-type) for details.

## US mail strictness settings <a href="#us-mail-strictness-settings-2" id="us-mail-strictness-settings-2"></a>

Depending on what business logic you’d like to take based on your verification result, you can toggle your US Address Strictness Settings in your [dashboard](https://dashboard.lob.com/#/settings/account). Each level of strictness determines how much you'd like for our platform to use internal data on deliverability to restrict mail from being created and delivered to potentially invalid addresses. There are 3 possible Strictness Levels:

* **Strict**: Only US addresses that Lob and the USPS deem deliverable can be successfully used as the `to` address for postcard, letter or check resources. Mail piece requests sent with non-deliverable addresses will return a `422` (Unprocessable Entity) error. This maps to a `deliverability` value of `deliverable` (see [API documentation](https://docs.lob.com/#tag/US-Verifications)). If addresses have never been run through verification (i.e. were created in the past), they will also err when used as the to address.
* **Normal**: Mail pieces will be created for addresses that Lob and the USPS deem deliverable, as well as addresses for which secondary information is extraneous or missing. Otherwise, you will receive a `422` (Unprocessable Entity) error. This maps to the `deliverability` values of `deliverable`, `deliverable_unnecessary_unit`, `deliverable_incorrect_unit` and `deliverable_missing_unit` (see [API documentation](https://docs.lob.com/#tag/US-Verifications)). If addresses have never been run through verification (i.e. were created in the past), they will also err when used as the to address.
* **Relaxed**: All mail pieces will be successfully created and mail delivery will be attempted, regardless of address validity. You will not receive a `422` (Unprocessable Entity) for Address Strictness reasons.

Ultimately, this allows you completely control the destiny of your final pieces. Only want to send to addresses that are guaranteed to be deliverable? Pick "Strict" mode. Confident that your addresses are right and want us to mail them out anyway? Use "Relaxed" mode. We want to give you the power to decide when Lob should be sending mail or when we should be rejecting based on deliverability. Ultimately, this reduces the amount of undeliverable mail you send and saves you money.

## Merge variable strictness setting <a href="#merge-variable-strictness-setting-3" id="merge-variable-strictness-setting-3"></a>

Depending on how much control you'd like over your HTML integration, we offer two different account settings that affect how we treat merge variables. This account setting affects the `POST /v1/postcards`, `POST /v1/self_mailers`, `POST /v1/letters`, and `POST /v1/checks` single endpoints in both test and live mode:

* **Strict**: Lob will send a `422` error if you define a merge variable in your HTML that is not passed in the `merge_variables` field of that request. Pass `''` or `null` to have a particular defined variable not render.
* **Relaxed**: Lob will not send an error if you define a merge variable in your HTML that is not included in the `merge_variables` field of that request. Instead, we will simply render nothing in the HTML in place of that merge variable.

Note that in the [Campaigns](https://dashboard.lob.com/campaigns) feature, you have additional flexibility to set merge variable strictness settings specific to each campaign, which will override your account-level settings. If you set campaign-level settings to 'Strict', any individual mail pieces that do not have a merge variable input value will not be sent. However, it is also possible to use a substitution value to replace missing merge variable input data, which will allow your mail pieces to be sent with generic values.&#x20;

Regardless of your strictness setting, if you pass merge variables keys that are not defined in your HTML, no error will be thrown. Your HTML will simply be rendered as normal without substituting the extra variable(s).

{% hint style="warning" %}
**NOTE**: On the 2020-02-11 and later API versions which support JSON in merge variables, merge variable strictness will still apply to the nested object keys, i.e. if a nested merge variable is undefined on the strict setting, then Lob will send an error.
{% endhint %}

## Cancellation windows <a href="#cancellation-windows-4" id="cancellation-windows-4"></a>

By default, all new accounts have a 4-hour cancellation window for any single mail piece that is created. Within this buffer timeframe, you can cancel mailings, free of charge. This gives you the flexibility to quickly QA your mailings before they are finally sent to production.

Note that in the [Campaigns](https://dashboard.lob.com/campaigns) feature, you have additional flexibility to establish cancellation windows specific to each campaign, which will override your account-level cancellation window settings.

Once the cancellation time window has passed for any single mail piece or for a batch of mail pieces within a campaign, the mailing is **no longer cancelable** and has been sent to our printers for production.&#x20;

{% hint style="info" %}
Customers on higher editions can customize their cancellation windows by mail product in their [dashboard settings](https://dashboard.lob.com/#/settings). Upgrade to the appropriate [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) if interested in gaining access to this ability.&#x20;
{% endhint %}

### Editing your cancellation windows <a href="#editing-your-cancellation-windows-5" id="editing-your-cancellation-windows-5"></a>

Growth edition customers and above can customize their cancellation windows. If you have access to this feature, your cancellation window can be anything from 0 minutes (no cancellation window) to up to 3 days.

Keep in mind that when you edit your cancellation window settings, any changes made will only apply to mailings created after the update was made. If you find yourself constantly changing your cancellation window for different use cases, we recommend using our [scheduling mailings‍](https://help.lob.com/print-and-mail/choosing-a-delivery-strategy#scheduled-mailings-15) feature instead.

### Canceling your mailings <a href="#canceling-your-mailings-6" id="canceling-your-mailings-6"></a>

Within your chosen cancellation window, any single mail piece or batch of mail pieces within the Mail Campaign feature is cancelable. This means that they will be completely removed from production and that they will not count towards your monthly usage for billing purposes.

To cancel a mailing, either use the [API endpoint](https://docs.lob.com/#operation/postcard_delete) or cancel the mailing from the dashboard. In either case, the mailing will only be cancelable if its `send_date` has not yet passed.

To cancel a list of mailings, you can use a combination of our `LIST` and `DELETE` endpoints to paginate through results and attempt to delete mailings that meet the specific criteria you set.

### Bypassing cancellation window with scheduled mailings <a href="#bypassing-cancellation-window-with-scheduled-mailings-7" id="bypassing-cancellation-window-with-scheduled-mailings-7"></a>

Even if you have a cancellation window set on your account, using the [scheduling mailings‍](https://help.lob.com/print-and-mail/choosing-a-delivery-strategy#scheduled-mailings-15) feature to schedule a mailing will override your cancellation window and the `send_date` passed will be used instead.

Not only is this useful for scheduling mailings far off in the future, but it is also handy for completely bypassing any cancellation window you might have and sending one mailing or batch off to production immediately.

### Best practices on establishing cancellation windows <a href="#best-practices-on-establishing-cancellation-windows-8" id="best-practices-on-establishing-cancellation-windows-8"></a>

* Upgrade to a Growth edition or above to take advantage of configurable cancellation windows. Adjust this window to a time that works for you so you have time to cancel on your end
* Have your developer build in buffer time into your Lob integration to give your team extra buffer time to cancel before submitting a live production request to Lob
  * Protip: configure different cancellation windows per mail format / use case individually in your [dashboard settings](https://dashboard.lob.com/settings/account)
* If you were unable to stop a check sent through Lob, you can still prevent it from being deposited by contacting your bank and placing a stop payment on the check. This can be done by contacting and providing your bank with the check number.
* Give yourself a longer buffer while your team becomes familiar with the Lob platform, especially when sending through the Mail Campaigns feature, as sending large-scale mail volumes may amplify the magnitude (and costs) of any errors committed. Once you've become familiar with Lob and its functionalities, gradually adjust your buffer time in order to send your mail to production sooner.&#x20;
* Cancellation windows on your account will delay the sending of any outgoing mail by the desired time window. Make sure to account for cancellation windows when considering [daily production cutoff times](https://help.lob.com/print-and-mail/mailing-classes-and-postage#mail-collection-cut-off-times-11) of 10am PT.
  * For example, if you want to make the cutoff time of 10am PT and your cancellation window is 60 minutes, your cutoff time is actually 9am PT.&#x20;
  * If you want to bypass your cancellation window for a certain send, you can do so by scheduling your mailings. &#x20;

## Idempotent requests <a href="#idempotent-requests-12" id="idempotent-requests-12"></a>

Idempotent Requests are requests that can be called many times without producing different outcomes. `GET` and `DELETE` requests are idempotent by definition, meaning the same backend work will occur no matter how many times the same request is issued. `POST` requests, however, are not idempotent. Sending a successful `POST` request once will result in a newly created object. If you send the same `POST` request 5 times, you will create 5 resources, assuming none of those requests err. If a network error occurs, there is no deterministic way to ensure the exact number of resources created.

For this reason, we have added a feature that will allow you to safely resend the same `POST` request to single endpoints (such as `/v1/postcards`, `/v1/self_mailers`, `/v1/letters`, or `/v1/checks`) and ensure that duplicate products are not created. To perform an idempotent `POST` request, you simply need to provide an additional `Idempotency-Key` header that uniquely identifies that resource. See our [API documentation](https://docs.lob.com/#section/Idempotent-Requests) for more specific information.

### Generating idempotency keys <a href="#generating-idempotency-keys-13" id="generating-idempotency-keys-13"></a>

The [Idempotency Key](https://lob.com/docs#idempotent-requests) is a feature that allows you to pass a unique key along with each request and guarantee that only one mailer is created and sent to prevent any duplicate mailings from being created. You can safely retry the same request with the same Idempotency Key and be assured that no duplicates are created even if the API is called multiple times within 24 hours.

We suggest using [V4 UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29) or another appropriately random string, but how you create the unique keys is up to you. For example, if you would like to associate a check with an internal unique ID of the user you are sending the check to, you may use that user id and the transaction date as an Idempotency Key (as long as you can guarantee the uniqueness of each Idempotency Key across requests to the same product). This **key will expire after 24 hours**, meaning if you resend the same request with the same Idempotency Key after 24 hours, a second resource will be created. Ultimately, it is up to you to make sure that you are appropriately setting the uniqueness of your keys based on your business logic. See resources below for help generating V4 UUIDs in various languages.

### Sending requests on retry <a href="#sending-requests-on-retry-14" id="sending-requests-on-retry-14"></a>

In case of failure, we recommend following something akin to an [exponential backoff algorithm](https://en.wikipedia.org/wiki/Exponential_backoff) for retrying your idempotent requests. This ensures that you aren't retrying continuously on a downed server, thereby contributing to the issue at hand.

### Resources <a href="#resources-15" id="resources-15"></a>

Below are resources we recommend in various languages for generating V4 UUIDs.

* Node: <https://www.npmjs.com/package/uuid>&#x20;
* Ruby: <https://rubygems.org/gems/uuid/>&#x20;
* Python: <https://docs.python.org/3/library/uuid.html>&#x20;
* PHP: <http://php.net/manual/en/function.uniqid.php>&#x20;
* Java: <https://docs.oracle.com/javase/7/docs/api/java/util/UUID.html>