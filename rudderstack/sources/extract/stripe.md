# Stripe Cloud Extract Source Deprecated

Sync data from Stripe to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Stripe](<https://www.stripe.com/>) is an online payment processing system for businesses. It offers cutting-edge software and APIs, allowing thousands of businesses to manage online payments.

This document guides you in setting up Stripe as a source in RudderStack. Once configured, RudderStack automatically ingests your Stripe data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Stripe as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Stripe** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

To set up Stripe as a Cloud Extract source, configure the following settings:

  * **Account ID** : Enter your Stripe account ID (usually starts with `acct_`). You can get it by logging in to your [Stripe dashboard](<https://dashboard.stripe.com/>) and going to your **Account** settings. For more information on finding your account ID, refer to the [Stripe documentation](<https://stripe.com/docs/dashboard/basics#find-account-id>).
  * **Secret Key** : Enter your Stripe API key (usually starts with `sk_live_`). You can get it by going to the [API keys](<https://dashboard.stripe.com/apikeys>) page. For more information on the secret keys, refer to the [Stripe documentation](<https://stripe.com/docs/keys>).
  * **Replication start date** : Select the date from when RudderStack should ingest your Stripe data.
  * **Lookback window in days** : This setting corresponds to the number of days from when RudderStack starts fetching the data. For example, if you set **Lookback window in days** to `1`, RudderStack fetches data from **Replication start date** \- 1.


> ![info](/docs/images/info.svg)
> 
> Use this setting if your data is frequently updated.

  * **Data request time increment in days** : Specify the time window used by RudderStack when requesting the data from Stripe. For example, if you set **Replication start date** to `Jan 01, 2022` and **Data request time increment in days** is set to 365 days, RudderStack fetches data from `Jan 01, 2022` to `Jan 01, 2023`. By default, RudderStack sets this field to `365` days, which is ideal for most use cases.


> ![info](/docs/images/info.svg)
> 
> Note that a higher value for the **Data request time increment in days** setting corresponds to lesser API requests and faster syncs.

### Destination settings

The following settings specify how RudderStack sends the data ingested from Stripe to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Stripe data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Stripe:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Stripe data you want to ingest by selecting the required resources. The below table mentions the syncs supported by these resources from Stripe to your warehouse destination where `id` is a common primary key for all:

Resource| Sync type| Stripe API endpoint  
---|---|---  
Balance Transactions| Incremental| [`/balance_transactions`](<https://stripe.com/docs/api/balance_transactions>)  
Bank Accounts| Full Refresh| [`/customers`](<https://stripe.com/docs/api/customer_bank_accounts>)  
Charges| Incremental| [`/charges`](<https://stripe.com/docs/api/charges>)  
Checkout Sessions| Incremental| [`/checkout`](<https://stripe.com/docs/api/checkout/sessions>)  
Checkout Sessions Line Items| Incremental| [`/checkout`](<https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-line_items>)  
Coupons| Incremental| [`/coupons`](<https://stripe.com/docs/api/coupons>)  
Customer Balance Transactions| Full Refresh| [`/customers`](<https://stripe.com/docs/api/customer_balance_transactions>)  
Customers| Incremental| [`/customers`](<https://stripe.com/docs/api/customers>)  
Disputes| Incremental| [`/disputes`](<https://stripe.com/docs/api/disputes>)  
Events| Incremental| [`/events`](<https://stripe.com/docs/api/events>)  
Invoice Items| Incremental| [`/invoiceitems`](<https://stripe.com/docs/api/invoiceitems>)  
Invoice Line Items| Full Refresh| [`/invoices`](<https://stripe.com/docs/api/invoices/line_item>)  
Invoices| Incremental| [`/invoices`](<https://stripe.com/docs/api/invoices>)  
Payment Intents| Incremental| [`/payment_intents`](<https://stripe.com/docs/api/payment_intents>)  
Payouts| Incremental| [`/payouts`](<https://stripe.com/docs/api/payouts>)  
Promotion Code| Incremental| [`/promotion_codes`](<https://stripe.com/docs/api/promotion_codes>)  
Plans| Incremental| [`/plans`](<https://stripe.com/docs/api/plans>)  
Products| Incremental| [`/products`](<https://stripe.com/docs/api/products>)  
Subscription Items| Full Refresh| [`/subscription_items`](<https://stripe.com/docs/api/subscription_items>)  
Subscriptions| Incremental| [`/subscriptions`](<https://stripe.com/docs/api/subscriptions>)  
Transfers| Incremental| [`/transfers`](<https://stripe.com/docs/api/transfers>)  
  
RudderStack captures the updates for the following resources using the [Events API](<https://stripe.com/docs/api/events>):

  * Charges
  * Customers
  * Disputes
  * Invoices
  * Invoice Items
  * Plans
  * Products
  * Subscriptions
  * Transfers


> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Stripe is now configured as a source. RudderStack will start ingesting data from Stripe as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** :

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack implements a feature wherein it associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.