# Billing

You can manage Lob Credits, payment methods, plans & usage, billing groups (if applicable), and preferences from the **Billing** tab in the Lob dashboard.

## How Lob's billing model works <a href="#how-lobs-billing-model-works-0" id="how-lobs-billing-model-works-0"></a>

Lob's billing includes three components for both our Print & Mail and Address Verification products:

1. **Subscriptions**: Recurring subscriptions to access our premium technology platform. Subscriptions are billed upfront, either annually or monthly, at the start of the chosen billing cycle.&#x20;
2. **Mail piece usage cost & add-on charges:** Funded via [Lob Credits](https://help.lob.com/account-management/billing/lob-credits) and priced per your plan's [mail piece unit pricing](https://help.lob.com/print-and-mail/ready-to-get-started/pricing-details#mail-piece-unit-pricing-3) inclusive of printing, postage, and delivery costs; includes add-on or overage charges if applicable.&#x20;
3. **Premium support charge** (if applicable): Billed monthly at the start of each calendar month.

## Lob's billing cycle <a href="#lobs-billing-cycle-1" id="lobs-billing-cycle-1"></a>

Lob’s recurring platform subscription will be billed monthly or annually, depending on your plan.&#x20;

* For subscriptions that do not start on the first of a month, **monthly subscriptions** for Print & Mail will be charged at a prorated amount for the first month and a recurring full monthly charge on the 1st of each subsequent month. Charges for mail pieces and add-on charges will be applied to your bill every month.
* **Annual subscriptions** will be charged at the time of purchase. The payment covers the prorated amount for the current month and the subsequent eleven months. The upfront annual subscription fee will be charged every subsequent year. Charges for mail pieces and add-on charges will be applied to your bill monthly.
* Once a subscription plan is purchased, it will renew automatically at the start of each billing cycle (monthly or yearly) unless you perform an upgrade, downgrade, or cancel.&#x20;

{% hint style="info" %}
**Usage counts** for mailing volumes are applied based on calendar months and will reset on the first of each month at 12:00AM UTC.
{% endhint %}

## Adding a corporate billing address

Ensuring that your corporate billing address is on file and remains updated is an important step in accurately calculating your [sales tax](https://help.lob.com/account-management/billing/sales-tax-faq).&#x20;

* Your **Billing Address** (noted in [Payment Methods](https://dashboard.lob.com/settings/payment) under Billing) is the address registered in your bank and listed to your credit card details.&#x20;
* This is different from your **company address** (noted under [Account](https://help.lob.com/account-settings#account), located in Settings), which is the address that is registered to the company that conducts business with Lob.&#x20;
* For SMBs or private individuals, the billing and company addresses may be the same.  &#x20;

Account administrators can add or edit their primary corporate billing address information at the bottom of the [Payment Methods](https://dashboard.lob.com/settings/payment) tab under Billing, by clicking on the 'edit' icon to the right of the Billing Address section title.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F7PEylcfpXEg0bPrQhzI6%2Fbilling%20address.png?alt=media&#x26;token=8975f72e-d24c-4178-82b1-6c8c40b7fe15" alt=""><figcaption></figcaption></figure>

## Payment Methods <a href="#adding-a-payment-method-2" id="adding-a-payment-method-2"></a>

### Adding a payment method

Only account administrators can add a payment method under [Payment Methods](https://dashboard.lob.com/billing/payments) (nested under Billing) in the Lob dashboard. Lob accepts two kinds of payment types: **Automated Clearing House (ACH)** and **credit cards**.&#x20;

A payment method must be added to your account to use the Live API key to make live Print & Mail API requests.&#x20;

The exception is that a payment method is not required for the first 300 live Address Verification API requests per month to the `/v1/us_verifications` endpoint. After the first 300 verification requests, you will begin receiving errors with status code `403`.

#### Automated Clearing House (ACH) <a href="#automated-clearing-house-ach-3" id="automated-clearing-house-ach-3"></a>

If you are sending at high volumes, we *recommend* you set up electronic ACH payments. If you are spending over $2,000 a month, we will *require* that you set up ACH.

For any future updates to your bank account (ACH) beyond the initial setup, you will need to contact <support@lob.com> to change the bank account on file.

If you are sending checks to customers, you must also set up and verify a bank account under your profile's [Bank Accounts](https://dashboard.lob.com/bank-accounts) section (nested under Print & Mail in the dashboard) from which to originate your checks. Once the bank account is set up, see our [Checks API documentation](https://docs.lob.com/#tag/Checks), or the [mail piece designs on checks](https://help.lob.com/print-and-mail/designing-mail-creatives/mail-piece-design-specs/checks), for more information.

#### Credit cards  <a href="#credit-cards-4" id="credit-cards-4"></a>

We accept the following international and domestic credit cards:

* American Express
* China UnionPay (CUP)
* Discover & Diners
* Japan Credit Bureau (JCB)
* Mastercard
* Visa

{% hint style="info" %}
For details on each payment method (including funds availability timelines) reference this [Lob Payment Methods ](https://help.lob.com/account-management/billing/lob-payment-methods)Help Center article.
{% endhint %}

## Plans & Usage <a href="#adding-a-payment-method-2" id="adding-a-payment-method-2"></a>

**Current plan details:** Toggle between Print & Mail, US or Int'l Verifications, or Premium Support plans to see the details of your current Lob plan and preview other available plans

**Current month usage:** Find a more granular breakdown of the prices + mail piece volumes sent, or verifications made, from all your API requests within the last calendar month, aggregated by your Lob plan

## Invoices <a href="#viewing-paying-invoices-5" id="viewing-paying-invoices-5"></a>

### Viewing invoices <a href="#viewing-paying-invoices-5" id="viewing-paying-invoices-5"></a>

You can view your invoices, both current and historical, at any time in the [Invoices tab](https://dashboard.lob.com/settings/invoices) (nested under Billing) in the dashboard as shown below.

* **Invoice Summary** will download an invoice summary for the select period in PDF format.
* **Invoice Details** will download a .csv file separating out the value of postage from the total sales price. (Note: Invoice Details is only available for invoices starting January 2023.)
* **YTD Sales Tax Summary:** will download a .csv file separating out usage per product per tax jurisdiction and associated sales tax charges. Refer here for more information on [sales taxes.](https://help.lob.com/account-management/billing/sales-tax-faq)

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FkhOtkcGAboRBFTwd3XYY%2Finvoices_home.png?alt=media&#x26;token=aeacfb18-8279-44e7-8057-7cf27517eafa" alt=""><figcaption></figcaption></figure>

### Paying invoices

If you have an ACH or credit card payment method on file, you can pay an outstanding invoice by reaching out to support via email at <support@lob.com> with your invoice number and stating your desire to recharge the outstanding balance.

## Billing Groups <a href="#modifying-your-invoicing-structure-7" id="modifying-your-invoicing-structure-7"></a>

{% hint style="info" %}
Access to this feature is exclusive to Enterprise Edition customers. Upgrade to the appropriate [Print & Mail Edition](https://dashboard.lob.com/#/settings/editions) to gain access.
{% endhint %}

For Enterprise edition customers, Lob can address specialized billing needs by allowing greater flexibility to generate invoices that are more reflective of your Lob Print & Mail usage. This can simplify fractional charges between the different parts of your organization that send mail, and provide data-driven visibility that unlocks new revenue potential based on a “pay for what you use” billing structure.&#x20;

**Specialized billing needs** may be defined by (but not limited to):

* Separating annual subscriptions vs consumption-based monthly usage charges&#x20;
* Differentiating monthly usage between different cost centers or end-customers
  * Examples: Different campaign objectives within a marketing team, different teams or departments, offices/entities located across multiple states, or white-labeling Lob&#x20;

To simplify your cost calculations by customizing your billing structure, a detailed request should be made to your Account Manager. Once this request is reviewed and approved by our Finance team, our team will be able to provide further instructions on how to modify your invoice and fulfill your needs at the start of the following billing period.&#x20;

Refer to our [API documentation](https://docs.lob.com/#tag/Billing-Groups) for more information on creating flexible billing groups from the API. Customers with access to this feature can create a billing group from the Lob Dashboard [here](https://dashboard.lob.com/settings/billing-management).  If you are an Enterprise edition customer who is interested in enabling this billing modification, reach out to your Account Manager.

## Billing Preferences <a href="#redeeming-account-credits-6" id="redeeming-account-credits-6"></a>

You can add or update Accounts Payable emails:

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FO1jtKEXTeycIgrHI1Ak1%2Fimage.png?alt=media&#x26;token=a02f7ed2-f0c7-4471-ac05-0ae7fdec5f6b" alt="" width="235"><figcaption></figcaption></figure>

You can also indicate if you would like to receive a notification when your Lob Credits goes below a certain threshold.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FNOgWWvjuu14RtNIQ1mDD%2Fthreshold_notification.png?alt=media&#x26;token=8b2bbadf-97df-4913-9062-4188ddd4ba39" alt="" width="375"><figcaption></figcaption></figure>

## Billing FAQs

<details>

<summary>How is the Estimated Campaign Cost calculated?</summary>

Having visibility of the cost of your direct mail campaign before ordering it empowers you to make strategic decisions, optimize your budget, and maximize the ROI of your marketing efforts.

In Step 4 (Review campaign) of the Lob Campaigns product in your dashboard, you can see the breakdown of the **estimated** cost of your campaign.&#x20;

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FCxOJf8JZrB61XG4mIFMy%2FEstimatedCost.png?alt=media&#x26;token=83d9d6fc-97e6-4622-b7f2-e71f364c8744" alt="" data-size="original">

The estimated campaign cost is comprised of the following:&#x20;

1. **Cost per mailpiece**: includes the materials, postage, and production cost.&#x20;

   Depending on what mailpiece you are sending, Lob may provide a further breakdown of the cost per mailpiece.&#x20;

   * Postcards and self-mailers pricing will vary on the size of the mailpiece and the postage type selected.
   * Letters pricing varies on the sheets of paper, color, the postage type selected. Letters can be sent with additional mail services like Certified or Registered mail, which can also contribute to a higher cost.&#x20;
2. **Recipients:** number of mailpieces
3. **Sales tax estimate:** The sales tax estimate is based on your historical rolling 12-month average with an additional 0.5% buffer. For new customers who have not yet sent mail, we use a 9% placeholder when estimating sales tax. ([learn more about Sales tax](https://help.lob.com/account-management/billing/sales-tax-faq))

After a campaign is ordered, we will calculate the final cost. The final cost could differ from the estimated campaign cost due to the following reasons:&#x20;

* Mailpieces that are never produced will not incur a cost; examples include recipients identified as undeliverable (thus mailpieces not created), or mailpieces whose creative fails to render.
* A different sales tax estimate based on the specifics of your campaign. [You can learn more about sales tax here](https://help.lob.com/account-management/billing-and-invoices/sales-tax-faq).

</details>

<details>

<summary>How long do micro deposits take to show in my account?</summary>

To use checks, setting up and [verifying a bank account](https://help.lob.com/print-and-mail/designing-mail-creatives/mail-piece-design-specs/checks#verifying-your-bank-account-4) for check origination is a required step. Typically, [micro-deposits](https://help.lob.com/print-and-mail/designing-mail-creatives/mail-piece-design-specs/checks#verifying-your-bank-account-4) take between 2 and 3 business days to hit your bank account. If you still have not received the micro-deposits after this timeframe, we recommend removing the bank account and then re-adding it. This will trigger a new set of micro-deposits which you can use to verify the account.&#x20;

As we do not control or hold these micro-deposits, if it takes longer for the micro-deposits to show up, it is fully up to your bank's discretion. As a security measure, we are not able to reissue micro-deposits for accounts once they are originally issued.

</details>

<details>

<summary>What happens if I reach a feature limit or usage limit in my subscription?</summary>

Lob will prevent you from completing any action that would cause you to exceed your subscription’s **feature limit** (such as user seats, address book entries, webhooks, HTML templates, etc.) and will throw an error message, notifying you that you’ve hit a limit. If you would like greater access, we encourage you to upgrade to a higher edition subscription. You can do this from the [Billing > Plans & Usage](https://dashboard.lob-staging.com/billing/editions/print-mail) tab in the Lob dashboard.&#x20;

If you need help on which subscription may work best for you, please reach out to <support@lob.com> so we can help recommend one that suits your needs.

If you reach a **mailpiece usage** limit in a given month, Lob will not prevent the mailpieces from being mailed out as we do not intend to disrupt your mailing operations. Lob will, however, reach out to get you onto the subscription best suited for your mailing needs. Lob also reserves the right to apply the corresponding subscription pricing that corresponds to your usage in the month you exceeded your mailing limit.

Lob also reserves the right to apply the corresponding plan pricing that corresponds to your usage in the month you exceeded your mailing limit or may suspend your Lob account if you repeatedly exceed your maximum monthly mailings.

</details>

<details>

<summary>How do I request a refund or credit?</summary>

Lob does not refund for production or service-related issues.

However, not to be confused with [Lob Credits](https://help.lob.com/account-management/billing/lob-credits), we may issue account credits that are redeemable in the following billing cycle. If you would like to know if your production or service issue qualifies for a credit, contact <support@lob.com>.

**To receive a credit, you must submit a claim by opening a support ticket with Lob through <support@lob.com> or using our Support messaging widget in the bottom right corner of your Lob Dashboard.**

To be eligible, the credit request must be received by Lob Support by the end of the next calendar month after which the incident occurred and must include:

* The words "SLA Credit Request" in the subject line;
* The dates and times of the incident occurred and the mailpiece IDs that were impacted and how
* The affected Lob APIs
* Your account’s logs that document the errors and corroborate your claimed outage or production issue (any confidential or sensitive information in these logs should be removed or replaced with asterisks)

Your failure to provide the request logs and other information as required above will disqualify you from receiving a Service or Production Credit.

Our customers must understand and agree that Service Credits are its sole and exclusive remedy for any breach of SLA by Lob.

Credits are exclusively up to Lob’s discretion to accept or deny the processing of a refund or credit depending on the circumstances.&#x20;

</details>

<details>

<summary>Redeeming account credits</summary>

Not to be confused with [Lob Credits](https://help.lob.com/account-management/billing/lob-credits), Lob may issue account credits for any transaction or item eligible for crediting (like a billing error). In the [Lob dashboard](https://dashboard.lob.com/), under Settings and then the [Account tab](https://dashboard.lob.com/settings/account), you can view any credit amounts issued to your account, along with their associated expiration date.&#x20;

Any existing credit for the current month will be reflected and automatically deducted in your next billing cycle's invoice. This credit will be represented in the "Other Charges" section of the invoices, and listed as "Account Credit." This credit cannot be applied retroactively.

</details>