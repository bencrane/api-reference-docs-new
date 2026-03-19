# Account settings

## Account info & settings <a href="#account-info-settings-0" id="account-info-settings-0"></a>

In the Lob [dashboard](https://dashboard.lob.com), you can access your [Account Settings](https://dashboard.lob.com/settings) to view your account details or configure various account settings. You can access these from the bottom of the left navigation menu under "Settings."

![](https://lh7-us.googleusercontent.com/qdmQp0RPnobqYZD2GZsP90jly3o0HU7Xd93L3Bbz9RlKXOcp0JEZGaYjtoVWt5-jJWF1OoaGS0Y3PwKULbakcfnf4VQ70DvWinPpsi7LjAQ7hrrmog4Yu5Q7BDrFNYg8rAs36qBWRNJHbnIbmi7fv-TgJQ=nw)

{% hint style="info" %}
You must be on certain platform editions or have Administrator-level access to be able to view or update certain tabs or settings mentioned below. &#x20;
{% endhint %}

**All users** can find the following tabs in their dashboard:

{% tabs %}
{% tab title="Account" %}

* **Account Information**: Update your company name and address here. You can find your **account ID** here, which is useful to reference when reaching out to Lob support.
* **Strictness settings & cancellation windows \[Admin only]**: Adjust these settings to ensure that your account's ability to send mail accurately reflects the requirements of your business. See [Mail send settings](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings).
* **Use type \[Admin only]**: Set at the account level whether you tend to send more marketing or operational (eg. non-promotional) mail. [Mail use type](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#mail-use-type-1) can be overridden at the campaign or individual mail piece level.&#x20;
  * This field does not appear visible to non-Admin users&#x20;
* **Webhook payloads \[Admin only]**: Choose whether to redact webhook payloads in fields that may contain sensitive PII/PHI data, or to keep the fields unredacted. See [Webhook JSON schema](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#webhooks-json-schema-2) for response examples.&#x20;
  * Lob is unable to retroactively provide any redacted payload information for any period of time when this account setting is set to "redacted"
* **Single Sign-On (SSO) \[Admin only]**: Create an active SSO integration with Lob by entering your SSO URL and IDP metadata. See [Signing into Lob](https://help.lob.com/account-management/signing-into-lob) for how to set up your Lob SSO.
* **Rate limits**: To prevent misuse, Lob enforces a rate limit on an API Key and endpoint basis, similar to how many other APIs enforce rate limits. Your default rate limits for your APIs and AV endpoints can be found in this section. See [Rate limiting](https://docs.lob.com/#tag/Rate-Limiting).&#x20;
* **Account credits**: View any credit amounts currently available, along with their expiration dates. See [Billing & invoices](https://help.lob.com/account-management/billing).
  {% endtab %}

{% tab title="User" %}

* **User information**: Change your name, email, phone number or password, or adjust your Lob email subscriptions.
* **Time zone settings**: Note that all timestamps currently shown within Lob are provided in the UTC time-zone. Lob does not timestamp in local-time zones.
  {% endtab %}

{% tab title="Team" %}

* See the list of team members that have been provisioned access to the Lob dashboard, and those who have been invited but remain pending.&#x20;
* See [User settings](https://help.lob.com/account-management/user-settings)
  {% endtab %}
  {% endtabs %}

Users with **Administrator-level** **access** will find additional tabs visible in their dashboard:

{% tabs %}
{% tab title="API Keys" %}

* **API version**: View your current version; full list of API versions can be found in our [API changelog](https://docs.lob.com/#tag/Versioning-and-Changelog)&#x20;
* **API keys**: Find your Secret and Publishable [API keys](https://help.lob.com/account-management/api-keys) for both test and live environments here
  {% endtab %}

{% tab title="Logs" %}

* See the [Audit logs](#audit-logs-8) section below&#x20;
  {% endtab %}

{% tab title="Reporting" %}

* **National Change of Address reports**: See the [NCOA section](#ncoa-export-10) below&#x20;
  {% endtab %}
  {% endtabs %}

## Changing your account <a href="#changing-your-account-1" id="changing-your-account-1"></a>

### Upgrading API versions     <a href="#upgrading-api-versions-2" id="upgrading-api-versions-2"></a>

When backward-incompatible changes are made to the API, a new dated version is released. You can view your version and upgrade to the latest version in your [dashboard under the API Keys tab](https://dashboard.lob.com/settings/api-keys).

We highly recommend upgrading to the latest API version. Upgrading allows you to keep up to date the with the latest features, bug fixes, and performance improvements.

To test a newer version of the API, you need to specify a version in the HTTP header as shown in the [API documentation](https://docs.lob.com/#tag/Versioning-and-Changelog). The API will return an error if a version older than your current one is passed in.

{% hint style="info" %}
Any API version prior to 2020-02-11 has been sunsetted.
{% endhint %}

### Upgrading or downgrading subscriptions     <a href="#upgrading-or-downgrading-subscriptions-3" id="upgrading-or-downgrading-subscriptions-3"></a>

In the [Plans & Usage tab](https://dashboard.lob.com/settings/editions/print-mail) in your [Lob dashboard](https://dashboard.lob.com/settings/account), go to the desired subscription (Print & Mail, Address Verification, or Support) you'd like to upgrade/downgrade in the toggle bar. Under the Available Plans section, change to your desired edition. If you are already subscribed to an Enterprise edition, speak with your Customer Success Manager if you'd like to discuss your subscription.  &#x20;

If you **purchase an edition and start it immediately**, you will gain access to the upgraded edition’s features and limits immediately. If you purchase an edition and choose for it to **start on the 1st of the next month**, you will gain access to upgraded edition’s features and limits on the first day of the following calendar month.

If you decide to **upgrade to a higher edition** during the month, we prorate the price difference between your original and new plan. At the end of your first month, your plan will continue to renew at the start of each subsequent month for the full amount.

If you **upgrade to an annual plan** from your original monthly plan in the middle of the month, you will be charged upfront for 11 months worth of subscription fees plus a prorated charge for the current month. The current month will count as the first month of your subscription.

If you **downgrade to a lower edition** during the month, you will retain the features of your current edition through the end of the current calendar month. Lob will snapshot your account’s settings as they currently are and allow you to continue using any existing templates/webhooks/settings created or set prior to the downgrade. Once the new lower-tiered edition takes effect at the start of the next billing cycle (e.g. start of next calendar month), you will no longer be able to add/adjust the lost features.

{% hint style="warning" %}
Usage counts for mailing volumes are applied based on calendar months and will reset on the first day of each month at **12:00AM UTC.**
{% endhint %}

### Closing or deleting your account     <a href="#closing-or-deleting-your-account-4" id="closing-or-deleting-your-account-4"></a>

If you would like to close your account, you can reach out to <support@lob.com> with your Account ID and reason for closing the account. You may locate your Account ID in the [Account tab](https://dashboard.lob.com/settings/account) of your dashboard under Settings. Deletions will only be processed if all outstanding invoices have been paid and there is no unbilled usage for the current billing period.

Alternatively, you may opt to downgrade to the Developer edition ($0 monthly subscription fee) and still keep your account with Lob open. This will allow you to return to Lob at any time in the future while ensuring that you do not get charged a platform fee. Downgrading only applies to accounts under a paying subscription (Startup, Growth, etc).

### Account bans/suspensions     <a href="#account-banssuspensions-5" id="account-banssuspensions-5"></a>

As part of our security measures, we regularly screen activity on our platform. If an account is flagged for suspicious activity, it will be suspended. If you would like to appeal the suspension you can contact <support@lob.com>, who will ask you for supporting documentation, and we will work with our Security team in an attempt to verify the integrity of the account.