# Sales Tax FAQ

## Overview of Sales Tax <a href="#overview-of-sales-tax" id="overview-of-sales-tax"></a>

Lob’s rapid expansion of our physical footprint combined with our business growth in the past few years have resulted in Lob’s obligation to collect and remit sales tax on sales generated in all US states. For the 2023 tax year and going forward, Lob will collect state sales/use tax from our customers.&#x20;

## Are any actions required from Lob's customers? <a href="#are-any-actions-required-from-lobs-customers" id="are-any-actions-required-from-lobs-customers"></a>

Yes! Lob is actively undertaking several initiatives to minimize our customers’ tax obligations.

* **Mail Use Type**: Many states directly exempt or allow an exemption certificate for marketing, advertising, and promotional mail. Lob requires users to declare a Mail Use type for all mail sent to allow customers to take advantage of these types of exemptions.
* **Postage**: Many states exempt postage from tax, under certain circumstances. Lob has implemented a feature in our invoices that will allow Lob to separate the value of postage from the total sales price that is subject to tax in all states that allow it.
* **Customer Exemption Management System**: For those customers with exemption certificates, we will be tracking your exemptions and applying them to the sales tax calculations.

Some of these features require customers to take the following steps:

1. Confirm your corporate billing address: in the [Billing Address section in the Payments tab](https://dashboard.lob.com/settings/payment) of the Lob Dashboard.
2. [Declare your mail’s use type](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/declaring-mail-use-type) at the appropriate level based on your organization's usage (at the account, campaign, or mailpiece level)

   -For customers who use an API integration to send direct mail, this should be included in the API call.

   -For customers who use the Dashboard to send direct mail, you will be prompted to fill in the required information during the submission process.
3. Submit a tax exemption form; read more on tax exemption below.&#x20;

## **What will be taxed, and how does it impact me?**&#x20;

Generally speaking, everything sold by Lob is *potentially* taxable. This includes our SaaS subscription charges, mail pieces, and other service offerings. We are not legally able to provide you a proforma or estimated sales tax. However, following is some general guidance that will allow you to estimate and plan until we send you an actual invoice for the taxes. &#x20;

1. **State and Local Tax Rates:** State tax rates vary between 5%-10%; note that sales tax is assessed at a zip code level.&#x20;
2. **Exemption Certificates:** An exemption certificate has the biggest impact on whether Lob is legally obligated to collect Sales tax on your invoices.  Examples of exemption certificates include: Resale Certificate, Sales & Use Tax exemption, Direct Pay Permit, Tax-Exempt Entity Certificate. Please email certificates to <tax@lob.com> to ensure we can apply these exemptions accordingly.
3. **Lob Products**:&#x20;

* **Subscriptions and services:** Sales tax will be calculated based on the customer’s billing address on file. [See the list of states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/subscriptions-and-services) that charge sales tax on subscriptions and services.

* **Lob Audiences:** [See the list of states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/lob-audience) that charge sales tax on information retrieval systems and products.

* **Marketing mail:** Sales tax on mailers that are sent for marketing, advertising, and promotional purposes is based on where the individual mail pieces were delivered. Lob will analyze each mail piece to determine the proper tax owed. These [38 states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/delivery-location-for-marketing-mail) tax marketing mail based on the delivery address of the individual mail piece. Additionally,[ these states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/postage-exemption) provide a postage cost sales tax exemption. Lob will be breaking out postage costs on your invoices for your reference.

  For your budget and cash planning purposes, you can estimate sales tax by determining which states your marketing mail will be delivered to, and apply the state tax rate and postage exemptions.&#x20;

  **Example:** Customer purchases $100 of marketing direct mail that is to be delivered to TX. TX is a state that provides a [postage exemption](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/postage-exemption).

  $30 Print \* TX Combined State & Local Tax rate = Sales Tax

  $70 Postage = $0 Sales Tax (Because TX exempts postage from sales tax)

* **Operational mail:** Sales tax on other mail, typically transactional or functional in nature, such as invoices, adverse action notices, statements, and other confidential mail that include sensitive PII/PHI data is based on the location of where the mail piece was printed, the customer’s billing address on file and where the individual mail pieces were delivered to. Lob will analyze each mail piece to determine the proper tax owed. There are [48 states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/delivery-location-for-operational-mail) that tax on operational mail. Additionally, [these states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/postage-exemption) provide a postage cost sales tax exemption. Lob will be breaking out postage costs on your invoices for your reference.&#x20;

  For your budget and cash planning purposes, you can estimate sales tax by the following general guidelines for operational mail:

  * If your billing address is in one of [these states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/customer-billing-address-for-operational-mail), the sales tax rate for your operational direct mail will be based on the customer billing state on file.
  * If not, then sales tax will be calculated based on where it was delivered in [these states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/delivery-location-for-operational-mail).
  * If your delivery state does not meet either of the above conditions, your mail piece is not taxable. &#x20;

  \
  **Example:** Customer has a billing address in MD, and purchases $100 of operational direct mail that is to be delivered to CO. Both MD and CO are states that provide a postage exemption.&#x20;

  * Because MD billing address is not on [this list](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/customer-billing-address-for-operational-mail), then the sales tax rate would be based on the delivery state, which is CO, and follow the postage exemption rules of CO.
  * $30 Print \* CO Combined State & Local Tax rate = Sales Tax

    $70 Postage = $0 Sales Tax (Because CO exempts postage from sales tax)

4. **Prefund Invoices:** Prefund Invoices are not taxable when invoiced or paid.
5. **Prepaid Inventory (Custom Envelopes, Card Affix, Buckslips, etc.)**: These prepaid inventory are considered tangible personal property and are taxable at the state's tax rate.
6. **Professional Services:** [See the list of states](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/professional-services) that charge sales tax on computer programming services.

## If I only subscribe to the Address Verification API service, does any of this affect me?

For customers who **only** subscribe to Lob's Address Verification API service, be advised that your subscription may be subject to tax, which is dependent on your primary billing address on file. \[See the 19 states listed  under [Subscriptions and Services](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/subscriptions-and-services)]&#x20;

If you have exemption certificates, you may send them to <tax@lob.com>. Customers that do not use the Print & Mail API service will not be affected by the mail use type product changes.

## Does Lob accept exemption certificates and/or exempt entities? <a href="#does-lob-accept-exemption-certificates-and-or-exempt-entities" id="does-lob-accept-exemption-certificates-and-or-exempt-entities"></a>

Yes! Please email exemption certificates to <tax@lob.com>. Be sure to include your Lob Account ID in order to receive sales tax exemption for the applicable Lob products and services. See our [Tax Exemption Guide](https://help.lob.com/account-management/billing/sales-tax-faq/tax-exemption-guide) for more information.&#x20;

Examples of common exemption certificates:

* **Marketing mail**:&#x20;
  * Some states will tax marketing mail based on the state that the mail was *printed in* (ie. originated), regardless of its destination. Therefore, these mail pieces that are sent outside of the US ***would*** be taxed.&#x20;
  * However, most states will tax marketing mail based on where the mail is *delivered*; therefore; these mail pieces sent outside of the US ***would*** ***not*** be taxed.

    &#x20;
* **Operational mail**:&#x20;
  * About half of the states will tax operational mail based on where the mail was *printed* or the customer's *billing address*, **regardless of its destination**, which means that these mail pieces sent outside of the US ***would*** be taxed.&#x20;
  * The rest of the states will tax operational mail based on where the mail was *delivered*, which means that these mail pieces sent outside of the US ***would not*** be taxed.

## I'm a non-US entity, am I tax-exempt?

For customers who have billing addresses outside of the US, be advised that your purchases from Lob may be subject to US sales tax.

**Subscription and services:** If your primary billing address on file is outside of the US, subscriptions and services, address verification, premium support is **not** taxable.

**Direct Mail:** Due to the Supreme court decision *South Dakota v. Wayfair*, individual states in the US assess sales tax based on the volume of business done in that state, regardless of the seller’s physical presence. This means that for customers who have primary billing addresses on file that are outside of the US, sales tax for direct mail is based on where the mail is delivered and whether that state taxes based on delivery location.

These states tax direct mail that is delivered to these states, regardless of the company’s billing address:&#x20;

* States that tax on [delivery location for operational mail](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/delivery-location-for-operational-mail)
* States that tax on [delivery location for marketing mail](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/delivery-location-for-marketing-mail)
* Additionally, [these states do not tax on postage costs.](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/postage-exemption) Lob will be breaking out postage costs on your invoices for your reference.

For your budget and cash planning purposes, you can estimate sales tax by determining which states your direct mail will be delivered to, and apply the state tax rate and postage exemptions.&#x20;

**Example:** Customer purchases $100 of marketing direct mail that is to be delivered to TX. TX is a state that provides a [postage exemption](https://help.lob.com/account-management/billing/sales-tax-faq/applicable-sales-tax-by-state/postage-exemption).

$30 Print \* TX Combined State & Local Tax rate = Sales Tax\
$70 Postage = $0 Sales Tax (Because TX exempts postage from sales tax)

## I’m a Lob Resale Partner. Am I expected to pass sales tax liabilities to our customers?

It is highly recommended that Resellers provide Lob with a resale certificate to remove tax from their invoices from Lob. In this scenario, the Reseller will then be responsible for collecting and remitting state and local sales tax from their end customer based on the Reseller’s own filing obligations in each state.

Lob highly recommends these customers reach out to their tax advisors for assistance with characterizing these transactions and identifying the most advantageous way to manage their sales tax payment and collection obligations.&#x20;

See the [Tax Exemption Guide](https://help.lob.com/account-management/billing/sales-tax-faq/tax-exemption-guide) for further information on sales tax exemption certificates.

## Can you advise me on my tax liabilities?&#x20;

Lob cannot provide tax advice. Please consult an appropriate tax professional.

## I have more questions; who can I talk to?&#x20;

Please reach out to <tax@lob.com>.&#x20;