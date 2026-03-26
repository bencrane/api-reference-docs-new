# Shopify Cloud Extract Source Deprecated

Sync data from Shopify to your warehouse destination via RudderStack.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Shopify](<https://www.shopify.com/in>) is a popular ecommerce platform that gives you all tools to start, run, and grow your business effectively. It offers online retailers a variety of services around digital payments, marketing, product shipping, customer engagement and retention, and more.

This document guides you in setting up Shopify as a source in RudderStack. Once configured, RudderStack automatically ingests your Shopify data and routes it to your specified data warehouse destination.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting started

To set up Shopify as a source in RudderStack, follow these steps:

  1. Log into your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Sources** > **New source** > **Cloud Extract** and select **Shopify** from the list of sources.
  3. Assign a name to your source and click **Continue**.


### Connection settings

Enter the following connection credentials to set up the Shopify source

[![Shopify credentials](/docs/images/cloud-extract-sources/shopify-creds.webp)](</docs/images/cloud-extract-sources/shopify-creds.webp>)

  * **Shopify Store** : Enter the name of your Shopify store from the URL. For example, if your URL is `https://NAME.myshopify.com`, then the store name would be `NAME`.
  * **Replication Start Date** : Select the date from when RudderStack should ingest your Shopify data. RudderStack will **not replicate** any data before this date.
  * **API Password** : Enter the Admin API access token which you can obtain by following the below steps:


  1. Log in to your [Shopify account](<https://accounts.shopify.com/store-login>).
  2. In the left sidebar, go to **Apps** > **App and sales channel settings**.[![Shopify settings](/docs/images/cloud-extract-sources/shopify-settings.webp)](</docs/images/cloud-extract-sources/shopify-settings.webp>)
  3. Click **Develop apps** > **Create an app**.
  4. Enter a name for the app.
  5. Select the relevant developer in the App developer dropdown menu.
  6. Click **Create app** > **Create Custom App**.
  7. From the app configuration screen, select the event version as `2022-10`.
  8. Configure the following [Admin API scopes](<https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes>):
     * `read_customers`
     * `read_draft_orders`
     * `read_inventory`
     * `read_locations`
     * `read_orders`
     * `read_price_rules`
     * `read_products`
     * `read_shopify_payments_payouts`
     * `read_content`
     * `read_fulfillments`
     * `read_assigned_fulfillment_orders`
     * `read_merchant_managed_fulfillment_orders`
     * `read_third_party_fulfillment_orders`
     * `read_discounts`
     * `read_script_tags`
     * `read_themes`
     * `read_files`
     * `read_publications`
     * `read_online_store_pages`
     * `read_product_feeds`
  9. Click **Install App**.
  10. You can see the Admin API access token in the **API credentials** tab.


### Destination settings

The following settings specify how RudderStack sends the data ingested from Shopify to the connected warehouse destination:

  * **Table prefix** : RudderStack uses this prefix to create a table in your data warehouse and loads all your Shopify data into it.


> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add special characters like `-` or `_` to the prefix by default. Hence, you need to specify it while setting the prefix.

  * **Schedule Settings** : RudderStack gives you three options to ingest the data from Shopify:
    * **Basic** : Runs the syncs at the specified time interval.
    * **CRON** : Runs the syncs based on the user-defined CRON expression.
    * **Manual** : You are required to run the syncs manually.


> ![info](/docs/images/info.svg)
> 
> For more information on the schedule types, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/>) guide.

### Selecting the data to import

You can choose the Shopify data you want to ingest by selecting the required resources. The below table mentions the sync type, API endpoints and the required scopes for these resources where `id` is a common primary key for all:

Resource| Sync type| Shopify API endpoint  
---|---|---  
`Articles`| Incremental| `/articles.json`  
`MetafieldArticles`| Incremental| `/articles/[object_id]/metafields.json`  
`Blogs`| Incremental| `/blogs.json`  
`MetafieldBlogs`| Incremental| `/blogs/[object_id]/metafields.json`  
`Customers`| Incremental| `/customers.json`  
`MetafieldCustomers`| Incremental| `/customers/[object_id]/metafields.json`  
`Orders`| Incremental| `/orders.json`  
`MetafieldOrders`| Incremental| `/orders/[object_id]/metafields.json`  
`DraftOrders`| Incremental| `/draft_orders.json`  
`MetafieldDraftOrders`| Incremental| `/draft_orders/[object_id]/metafields.json`  
`Products`| Incremental| `/products.json`  
`MetafieldProducts`| Incremental| `/products/[object_id]/metafields.json`  
`ProductImages`| Incremental| `/products/{product_id}/images.json`  
`MetafieldProductImages`| Incremental| `/product_images/{image_id}/metafields.json`  
`ProductVariants`| Incremental| `products/{product_id}/variants.json`  
`MetafieldProductVariants`| Incremental| `variants/{variant_id}/metafields.json`  
`AbandonedCheckouts`| Incremental| `checkouts.json`  
`CustomCollections`| Incremental| `custom_collections.json`  
`SmartCollections`| Incremental| `smart_collections`  
`MetafieldSmartCollections`| Incremental| `/smart_collections/[object_id]/metafields.json`  
`Collects`| Incremental| `collects.json`  
`Collections`| Incremental| `collections/{collection_id}.json`  
`MetafieldCollections`| Incremental| `collections/{object_id}/metafields.json`  
`BalanceTransactions`| Incremental| `shopify_payments/balance/transactions.json`  
`OrderRefunds(Sub resource)`| Incremental| `orders/{order_id}/refunds.json`  
`OrderRisks`| Incremental| `orders/{order_id}/risks.json`  
`Transactions`| Incremental| `orders/{order_id}/transactions.json`  
`TenderTransactions`| Incremental| `tender_transactions.json`  
`Pages`| Incremental| `pages.json`  
`MetafieldPages`| Incremental| `/pages/[object_id]/metafields.json`  
`PriceRules`| Incremental| `price_rules.json`  
`DiscountCodes`| Incremental| `price_rules/{price_rule_id}/discount_codes.json`  
`Locations`| Full Refresh| `locations.json`  
`MetafieldLocations`| Incremental| `/locations/[object_id]/metafields.json`  
`InventoryLevels`| Incremental| `locations/{location_id}/inventory_levels.json`  
`InventoryItems`| Incremental| `inventory_items.json?ids={ids}`  
`FulfillmentOrders`| Incremental| `orders/{order_id}/fulfillment_orders.json`  
`Fulfillments`| Incremental| `orders/{order_id}/fulfillments.json`  
`Shop`| Full Refresh| `shop.json`  
`MetafieldShops`| Incremental| `metafields.json`  
  
> ![info](/docs/images/info.svg)
> 
> For more information on the **Full Refresh** and **Incremental** sync modes, refer to the [Common Settings](<https://www.rudderstack.com/docs/sources/extract/common-settings/#sync-modes>) guide.

Shopify is now configured as a source. RudderStack will start ingesting data from Shopify as per your specified schedule and frequency.

You can further connect this source to your data warehouse by clicking on **Add Destination** , as shown:

[![Adding a destination](/docs/images/cloud-extract-sources/add-destination.webp)](</docs/images/cloud-extract-sources/add-destination.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Use Existing Destination** option if you have an already-configured data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, select the **Create New Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.