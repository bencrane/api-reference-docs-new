# Data Pipelines Overview

Collect, unify, and activate your data using RudderStack.

* * *

  * __2 minute read

  * 


RudderStack’s pipelines simplify customer data collection and integration across your entire stack, eliminating expensive data wrangling and custom solutions. We offer two types of pipelines:

  * [Event Stream](<https://www.rudderstack.com/docs/data-pipelines/event-stream/>): Collect granular user event and identification data from web, mobile, server, and other sources, then automatically forward it to your data warehouse, data lake, and 200+ cloud destination integrations.
  * [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>): Sync the customer data in your data warehouse to all your operational systems, including analytics, sales, and marketing tools.

[![Data pipelines in RudderStack](/docs/images/data-pipelines/rudderstack-pipelines.webp)](</docs/images/data-pipelines/rudderstack-pipelines.webp>)

## Features

RudderStack’s data pipelines offer the following features:

  * **Simplified, central integration management** : RudderStack offers flexible [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) and [APIs](<https://www.rudderstack.com/docs/api/http-api/>) for collecting data from any source. It also offers over [200 destination integrations](<https://www.rudderstack.com/docs/destinations/overview/>) for sending data to your entire stack, even as it changes over time.
  * **Reliable data flow** : RudderStack’s event ingestion and delivery mechanisms ensure there is no data loss at any point. In case of bottlenecks like network-related issues or downtime, it provides a [replay mechanism](<https://www.rudderstack.com/docs/user-guides/administrators-guide/event-replay/>) to resend the impacted data to the desired destinations.
  * **Real-time processing** : Many businesses often require real-time data to drive personalization and customer experiences. You can leverage the [Event Stream](<https://www.rudderstack.com/docs/data-pipelines/event-stream/>) pipeline to capture and route event data in real-time.
  * **Real-time event transformation** : RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/>) feature allows you to operate on event payloads in real-time, enabling use cases for data quality, enrichment via API, customizing integrations, and more.
  * **Warehouse activation** : Warehouses are often the single source of truth for businesses. You can activate the enriched user data residing in your warehouse by sending it to downstream tools like Braze, Customer.io, etc., by leveraging RudderStack’s [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>) pipelines.
  * **Data quality and consistency** : RudderStack offers tools for cleaning and [validating](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) your data, preventing any errors arising from inconsistent or inaccurate data.
  * **Data governance** : You can enforce strict security measures and [data governance](<https://www.rudderstack.com/docs/data-governance/overview/>) policies on the data coming through your pipelines to ensure compliance with various regulations like GDPR and CCPA, protect sensitive user information, and maintain users’ data privacy.
  * **Troubleshooting and monitoring** : With RudderStack’s [event monitoring](<https://www.rudderstack.com/docs/data-governance/health-dashboard/>) capabilities, you can proactively identify and troubleshoot any data delivery issues in your pipeline and promptly address them.