# Reverse ETL

Enable seamless activation of data from cloud data warehouses to downstream destinations.

* * *

  * __5 minute read

  * 


RudderStack’s **Reverse ETL** feature empowers you to route the enriched customer data residing in your data warehouse to all your operational systems, including analytics, sales, and marketing tools. With this feature, you can set up your data warehouse as a source in the [RudderStack dashboard](<https://app.rudderstack.com/>), choose the data to import, and then seamlessly synchronize it to your preferred destinations.

See how Reverse ETL pipelines work in this self-paced product tour:

## Why use Reverse ETL

Cloud data warehouses have revolutionized data management, centralizing information, and transforming it for powerful analytics. Yet, the true power of data lies in activation, turning those insights into real-world decisions and experiences. This requires getting clean data out of the warehouse into operational systems.

However, the common issues with this are:

  * Data warehouses are only accessible to technical, SQL users.
  * Moving data from the warehouse to operational systems often involves manual processes, scripting, and maintenance, which can be time-consuming and error-prone.
  * Important metrics and features from data warehouses might only make it outside in the form of reports or dashboards.


This is where the Reverse ETL functionality comes into picture.

## What is Reverse ETL

Reverse ETL is the process of delivering data from a company’s data warehouse to operational systems and SaaS tools. This empowers businesses to act upon the data, personalizing customer experiences effectively.

A data warehouse contains business critical data from where important metrics and features like LTV, revenue, CAC, ROI, conversion rate, churn, etc. can be derived. Hence, it becomes important to ensure that the warehouse data is activated. Reverse ETL unlocks this data activation by putting the right data in the right operational tools.

### ETL vs Reverse ETL

Traditional ETL primarily focuses on integrating data, often in a unidirectional manner, from various disparate sources into a centralized data warehouse. This data is then transformed and combined for analytical purposes, such as customer profiling.

Reverse ETL is a specific type of ETL that flows in the opposite direction from a warehouse [source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) towards operational or SaaS tools as a [destination](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/>), establishing a bidirectional flow of data in and out of the data warehouse.

Another key difference is that traditional ETL focuses on ingesting data tables whereas Reverse ETL focuses on syncing specific rows, often updating fields only if data has changed since the last sync. This entails data deduplication and comparison of current warehouse data values with downstream tools.

## How Reverse ETL works

Reverse ETL queries your data warehouse and writes the query results to a downstream operational tool or system. RudderStack’s Reverse ETL pipeline includes the following core components:

  * **Sources** : Usually a cloud data warehouse like Snowflake or BigQuery which contains the centralized data you want to sync to the operational system.
  * **Import Data** : Data to be synced from the source. For RudderStack that can be a warehouse table, a [model (SQL query)](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>), or an [audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>).
  * **Sync Type** : Defines how to sync the data to the destination, such as [Upsert](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#upsert-mode>) or [Mirror](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) mode.
  * **Destinations** : Location to write the synced data. This is the operational system where business users consume data (for example, Salesforce, Google Ads, Iterable, Blaze, etc.)


> ![success](/docs/images/tick.svg)
> 
> You can connect a Reverse ETL source to multiple destinations.

  * **Schedule** : Determines how often RudderStack [syncs](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) the data to the destinations.


These components collectively overlay on your cloud data warehouse enabling you to activate any data within your data models and warehouse.

## How RudderStack charges for Reverse ETL

Every record sent from a Reverse ETL source is considered as an event.

When sending data from a Reverse ETL source to multiple destinations, RudderStack sends the record to each destination separately — this means you will be charged on a **per connection basis**.

For example, if you have a Reverse ETL source connected to 3 destinations, and you send 100 records from the source to each of these destinations, then you will be charged for 300 events.

## Use cases

Reverse ETL plays a crucial role in unlocking the full potential of your data assets by bridging the gap between analytics and operations, enabling businesses to drive better decision-making and gain competitive advantage.

### Marketing teams

Marketing teams can employ Reverse ETL to ensure continuous updates of CRM systems with the latest customer data, enriching customer profile information. It can also be used to define segments or audiences and sync them across all marketing platforms for enhanced tracking, personalized marketing, and experimentation.

### Sales teams

Sales teams require access to behavioral and product usage data in the warehouse. Reverse ETL enables pushing this data into sales platforms (e.g. CRM), offering detailed customer insights for proactive real-time responses. Additionally, you can setup Reverse ETL to trigger notifications in communication apps like Slack, ensuring your sales reps are notified of important customer actions in your product/app.

### Product teams

Product teams can leverage Reverse ETL to send up-to-date customer data and attributes to production databases, personalizing customers’ in-product experiences. This can be as simple as showing current billing information or updating offerings based on past purchases.

### Customer Success teams

Reverse ETL allows customer success teams to get key metrics and predictive features, like LTV, ARR, and likelihood to churn, into their support tools. This capability enables them to prioritize tickets based on impact and reduce churn among critical customers.