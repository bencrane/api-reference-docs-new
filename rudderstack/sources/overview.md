# Event Stream Sources Overview

Learn about the Event Stream and Reverse ETL source types supported by RudderStack.

* * *

  * __2 minute read

  * 


The event data originates via a **source** in RudderStack. The most common event sources are your apps and web properties, but can include third-party cloud apps, server integrations, and even your own data warehouse.

The following sections provide more detail on the available source types, with links to the setup guides for each source.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** If you’re new to RudderStack, go through the [Quickstart](<https://www.rudderstack.com/docs/get-started/quickstart/>) guide to create your first source.

## Event Streams

RudderStack’s [Event Streams](<https://www.rudderstack.com/docs/sources/event-streams/>) feature lets you collect event data from all your sites and applications and route it to a wide array of customer tools and data warehouses.

### SDKs

RudderStack provides open source [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for web, mobile, and server applications:

#### Web

Track customer event data from your website and web apps and send it to the specified destinations:

[![AMP logo](/docs/images/logos/sources/amp-logo.webp)AMP](</docs/sources/event-streams/sdks/rudderstack-amp-analytics/>)[![JavaScript logo](/docs/images/logos/sources/js-logo.webp)JavaScript](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)

#### Mobile

Use native mobile SDKs for the mobile operating systems and development frameworks:

[![Android \(Java\) — Legacy logo](/docs/images/logos/sources/android-legacy.svg)Android (Java) — Legacy](</docs/sources/event-streams/sdks/rudderstack-android-sdk/>)[![Android \(Kotlin\) logo](/docs/images/logos/sources/android-kotlin.svg)Android (Kotlin)](</docs/sources/event-streams/sdks/kotlin-sdk/>)[![Cordova logo](/docs/images/logos/sources/cordova-logo.webp)Cordova](</docs/sources/event-streams/sdks/rudderstack-cordova-sdk/>)[![Flutter logo](/docs/images/logos/sources/flutter-logo.webp)Flutter](</docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)[![iOS \(Obj-C\) — Legacy logo](/docs/images/logos/sources/ios-legacy.svg)iOS (Obj-C) — Legacy](</docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)[![iOS \(Swift\) logo](/docs/images/logos/sources/ios-swift.svg)iOS (Swift)](</docs/sources/event-streams/sdks/swift-sdk/>)[![React Native logo](/docs/images/logos/sources/reactnative-logo.webp)React Native](</docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>)[![Unity logo](/docs/images/logos/sources/unity-logo.webp)Unity](</docs/sources/event-streams/sdks/rudderstack-unity-sdk/>)

#### Server

Use server-side SDKs to track event data from your backend applications and send it to the specified destinations:

[![.NET logo](/docs/images/logos/sources/dotnet-logo.webp).NET](</docs/sources/event-streams/sdks/rudderstack-dotnet-sdk/>)[![Go logo](/docs/images/logos/sources/go-logo.webp)Go](</docs/sources/event-streams/sdks/rudderstack-go-sdk/>)[![Java logo](/docs/images/logos/sources/java-logo.webp)Java](</docs/sources/event-streams/sdks/rudderstack-java-sdk/>)[![Node.js logo](/docs/images/logos/sources/node-logo.webp)Node.js](</docs/sources/event-streams/sdks/rudderstack-node-sdk/>)[![PHP logo](/docs/images/logos/sources/php-logo.webp)PHP](</docs/sources/event-streams/sdks/rudderstack-php-sdk/>)[![Python logo](/docs/images/logos/sources/python-logo.webp)Python](</docs/sources/event-streams/sdks/rudderstack-python-sdk/>)[![Ruby logo](/docs/images/logos/sources/ruby-logo.webp)Ruby](</docs/sources/event-streams/sdks/rudderstack-ruby-sdk/>)[![Rust logo](/docs/images/logos/sources/rust-logo.webp)Rust](</docs/sources/event-streams/sdks/rudderstack-rust-sdk/>)

### Cloud Apps

RudderStack lets you ingest event data from your [cloud apps](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/>) and route it to the desired destinations.

[![Adjust logo](/docs/images/logos/sources/adjust-logo.svg)Adjust](</docs/sources/event-streams/cloud-apps/adjust/>)[![Apache Kafka logo](/docs/images/logos/sources/kafka-logo.svg)Apache Kafka](</docs/sources/event-streams/cloud-apps/kafka/>)[![AppsFlyer logo](/docs/images/logos/sources/appsflyer-logo.svg)AppsFlyer](</docs/sources/event-streams/cloud-apps/appsflyer/>)[![App Center logo](/docs/images/logos/sources/appcenter-logo.svg)App Center](</docs/sources/event-streams/cloud-apps/appcenter/>)[![Auth0 logo](/docs/images/logos/sources/auth0.webp)Auth0](</docs/sources/event-streams/cloud-apps/auth0/>)[![Braze logo](/docs/images/logos/sources/braze-logo.svg)Braze](</docs/sources/event-streams/cloud-apps/braze-currents/>)[![Canny logo](/docs/images/logos/sources/canny.svg)Canny](</docs/sources/event-streams/cloud-apps/canny/>)[![ClickUp logo](/docs/images/logos/sources/clickup.svg)ClickUp](</docs/sources/event-streams/cloud-apps/clickup/>)[![Close CRM logo](/docs/images/logos/sources/close.webp)Close CRM](</docs/sources/event-streams/cloud-apps/close-crm/>)[![Customer.io logo](/docs/images/logos/sources/customerio.svg)Customer.io](</docs/sources/event-streams/cloud-apps/customerio/>)[![Extole logo](/docs/images/logos/sources/extole.webp)Extole](</docs/sources/event-streams/cloud-apps/extole/>)[![Facebook Lead Ads logo](/docs/images/logos/sources/facebook.svg)Facebook Lead Ads](</docs/sources/event-streams/cloud-apps/facebook-lead-ads/>)[![Formsort logo](/docs/images/logos/sources/formsort.svg)Formsort](</docs/sources/event-streams/cloud-apps/formsort/>)[![Gainsight PX logo](/docs/images/logos/sources/gainsight.svg)Gainsight PX](</docs/sources/event-streams/cloud-apps/gainsight-px/>)[![Iterable logo](/docs/images/logos/sources/Iterable.svg)Iterable](</docs/sources/event-streams/cloud-apps/iterable/>)[![Looker logo](/docs/images/logos/sources/looker.webp)Looker](</docs/sources/event-streams/cloud-apps/looker/>)[![Mailjet logo](/docs/images/logos/sources/mailjet.svg)Mailjet](</docs/sources/event-streams/cloud-apps/mailjet/>)[![Mailmodo logo](/docs/images/logos/sources/mailmodo.svg)Mailmodo](</docs/sources/event-streams/cloud-apps/mailmodo/>)[![Monday logo](/docs/images/logos/sources/monday.svg)Monday](</docs/sources/event-streams/cloud-apps/monday/>)[![MoEngage logo](/docs/images/logos/sources/MoEngage.svg)MoEngage](</docs/sources/event-streams/cloud-apps/moengage/>)[![Olark logo](/docs/images/logos/sources/olark.svg)Olark](</docs/sources/event-streams/cloud-apps/olark/>)[![Ortto logo](/docs/images/logos/sources/ortto.svg)Ortto](</docs/sources/event-streams/cloud-apps/ortto/>)[![PagerDuty logo](/docs/images/logos/sources/pagerduty.svg)PagerDuty](</docs/sources/event-streams/cloud-apps/pagerduty/>)[![Pipedream logo](/docs/images/logos/sources/pipedream.svg)Pipedream](</docs/sources/event-streams/cloud-apps/pipedream/>)[![PostHog logo](/docs/images/logos/sources/posthog.svg)PostHog](</docs/sources/event-streams/cloud-apps/posthog/>)[![Refiner logo](/docs/images/logos/sources/refiner.svg)Refiner](</docs/sources/event-streams/cloud-apps/refiner/>)[![RevenueCat logo](/docs/images/logos/sources/revenuecat.webp)RevenueCat](</docs/sources/event-streams/cloud-apps/revenuecat/>)[![SatisMeter logo](/docs/images/logos/sources/satismeter.svg)SatisMeter](</docs/sources/event-streams/cloud-apps/satismeter/>)[![Segment logo](/docs/images/logos/sources/segment.svg)Segment](</docs/sources/event-streams/cloud-apps/segment/>)[![Shopify logo](/docs/images/logos/sources/shopify.webp)Shopify](</docs/sources/event-streams/cloud-apps/shopify/>)[![Signl4 logo](/docs/images/logos/sources/signl4.svg)Signl4](</docs/sources/event-streams/cloud-apps/signl4/>)[![Slack logo](/docs/images/logos/sources/slack.svg)Slack](</docs/sources/event-streams/cloud-apps/slack/>)

### HTTP source

You can also leverage the HTTP source to send events to RudderStack directly via [HTTP API calls](<https://www.rudderstack.com/docs/api/http-api/>) from your server-side applications:

[![HTTP logo](/docs/images/logos/sources/http-logo.webp)HTTP](</docs/sources/event-streams/http/>)

### Custom webhook

You can also add any source that supports a webhook, use it to ingest events, and send them to your preferred destinations via RudderStack.

[![Custom Webhook Source logo](/docs/images/logos/sources/webhook-logo.webp)Custom Webhook Source](</docs/sources/event-streams/cloud-apps/webhook-source/>)

## Reverse ETL

With RudderStack’s [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) capabilities, you can use your data warehouse as a data source. You can tap into your warehouse data and enrich data pipelines elsewhere in your stack, for enhanced customization, personalization, and targeting.

[![Amazon Redshift logo](/docs/images/logos/sources/redshift.svg)Amazon Redshift](</docs/sources/reverse-etl/amazon-redshift/>)[![Amazon S3 logo](/docs/images/logos/sources/s3.svg)Amazon S3](</docs/sources/reverse-etl/amazon-s3/>)[![Databricks logo](/docs/images/logos/sources/databricks.webp)Databricks](</docs/sources/reverse-etl/databricks/>)[![Google BigQuery logo](/docs/images/logos/sources/bigquery.svg)Google BigQuery](</docs/sources/reverse-etl/google-bigquery/>)[![MySQL logo](/docs/images/logos/sources/mysql.webp)MySQL](</docs/sources/reverse-etl/mysql/>)[![PostgreSQL logo](/docs/images/logos/sources/postgresql.svg)PostgreSQL](</docs/sources/reverse-etl/postgresql/>)[![Snowflake logo](/docs/images/logos/sources/snowflake.svg)Snowflake](</docs/sources/reverse-etl/snowflake/>)[![Trino logo](/docs/images/logos/sources/trino.webp)Trino](</docs/sources/reverse-etl/trino/>)

## API

It is recommended to use a native SDK for tracking and routing user events from your sources. RudderStack’s SDKs offer automatic tagging of user context, event batching, and retry functionality during delivery failure.

If you don’t see a supported SDK or library for your environment, you can send your data directly to RudderStack by configuring the [HTTP source](<https://www.rudderstack.com/docs/sources/event-streams/http/>).