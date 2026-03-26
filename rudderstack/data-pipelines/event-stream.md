# Event Stream

Ingest your event data into RudderStack using cloud apps and SDKs.

* * *

  * __3 minute read

  * 


RudderStack’s **Event Stream** pipeline offers a comprehensive solution for collecting real-time user event data and sending it to [integrations](<https://www.rudderstack.com/docs/destinations/overview/>) across your stack, including cloud tools, [data warehouses](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>), and data processing tools.

Top Event Stream use cases include:

  * Simplifying event collection through a single [SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>)
  * Syncing raw event data to [data warehouses](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) and data lakes
  * [Cleaning, enriching, and transforming](<https://www.rudderstack.com/docs/transformations/overview/>) events in real-time
  * [Identifying anonymous and known users](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>)
  * Implementing [cookieless tracking](<https://www.rudderstack.com/docs/data-governance/cookieless-tracking/>)
  * Building and managing [custom integrations](<https://www.rudderstack.com/docs/destinations/http-webhook/>)
  * Automating integration management in a centralized platform


You can see how Event Stream pipelines work in this self-paced product tour:

## Event Stream sources

Our [Event Stream pipeline](<https://www.rudderstack.com/docs/data-pipelines/overview/>) can ingest events from:

  * 16 source-available SDKs for [web](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>), [mobile](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>), and [server-side](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) platforms
  * [Cloud apps](<https://www.rudderstack.com/docs/sources/extract/>) that support event emission
  * Any custom source that can send data to a [RudderStack Webhook source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/webhook-source/>)


RudderStack offers a suite of versatile source-available SDKs designed to integrate seamlessly with your web, mobile, and server-side applications. These SDKs enable developers to reliably track and manage event data across various platforms, ensuring a secure and reliable data platform that scales with your technology stack.

### Web SDKs

RudderStack provides source-available SDKs for robust and reliable web data collection. Our [Web SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) allow you to capture and send high-fidelity customer event data from your websites and web apps without compromising on site performance.

[![AMP logo](/docs/images/logos/sources/amp-logo.webp)AMP](</docs/sources/event-streams/sdks/rudderstack-amp-analytics/>)[![JavaScript logo](/docs/images/logos/sources/js-logo.webp)JavaScript](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)

### Mobile SDKs

Use the native RudderStack SDKs for the [iOS](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>), [Android](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>), and cross-platform development frameworks allowing you to harness device-specific functionalities and optimize mobile user engagement.

[![Android \(Java\) — Legacy logo](/docs/images/logos/sources/android-legacy.svg)Android (Java) — Legacy](</docs/sources/event-streams/sdks/rudderstack-android-sdk/>)[![Android \(Kotlin\) logo](/docs/images/logos/sources/android-kotlin.svg)Android (Kotlin)](</docs/sources/event-streams/sdks/kotlin-sdk/>)[![Cordova logo](/docs/images/logos/sources/cordova-logo.webp)Cordova](</docs/sources/event-streams/sdks/rudderstack-cordova-sdk/>)[![Flutter logo](/docs/images/logos/sources/flutter-logo.webp)Flutter](</docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)[![iOS \(Obj-C\) — Legacy logo](/docs/images/logos/sources/ios-legacy.svg)iOS (Obj-C) — Legacy](</docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)[![iOS \(Swift\) logo](/docs/images/logos/sources/ios-swift.svg)iOS (Swift)](</docs/sources/event-streams/sdks/swift-sdk/>)[![React Native logo](/docs/images/logos/sources/reactnative-logo.webp)React Native](</docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>)[![Unity logo](/docs/images/logos/sources/unity-logo.webp)Unity](</docs/sources/event-streams/sdks/rudderstack-unity-sdk/>)

### Server SDKs

Use the [server-side SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) to track event data from your backend applications and ensure secure, comprehensive event tracking for your server-side transactions with the ability to monitor system health at every step.

[![.NET logo](/docs/images/logos/sources/dotnet-logo.webp).NET](</docs/sources/event-streams/sdks/rudderstack-dotnet-sdk/>)[![Go logo](/docs/images/logos/sources/go-logo.webp)Go](</docs/sources/event-streams/sdks/rudderstack-go-sdk/>)[![Java logo](/docs/images/logos/sources/java-logo.webp)Java](</docs/sources/event-streams/sdks/rudderstack-java-sdk/>)[![Node.js logo](/docs/images/logos/sources/node-logo.webp)Node.js](</docs/sources/event-streams/sdks/rudderstack-node-sdk/>)[![PHP logo](/docs/images/logos/sources/php-logo.webp)PHP](</docs/sources/event-streams/sdks/rudderstack-php-sdk/>)[![Python logo](/docs/images/logos/sources/python-logo.webp)Python](</docs/sources/event-streams/sdks/rudderstack-python-sdk/>)[![Ruby logo](/docs/images/logos/sources/ruby-logo.webp)Ruby](</docs/sources/event-streams/sdks/rudderstack-ruby-sdk/>)[![Rust logo](/docs/images/logos/sources/rust-logo.webp)Rust](</docs/sources/event-streams/sdks/rudderstack-rust-sdk/>)

### Cloud App sources

Ingest event data from your [cloud apps](<https://www.rudderstack.com/docs/sources/extract/>) and route it to the specified destinations with ease. RudderStack’s intelligent data pipelines can handle high volumes of data inflow, ensuring that your event data is collected seamlessly from various cloud applications and services.

[![Adjust logo](/docs/images/logos/sources/adjust-logo.svg)Adjust](</docs/sources/event-streams/cloud-apps/adjust/>)[![Apache Kafka logo](/docs/images/logos/sources/kafka-logo.svg)Apache Kafka](</docs/sources/event-streams/cloud-apps/kafka/>)[![AppsFlyer logo](/docs/images/logos/sources/appsflyer-logo.svg)AppsFlyer](</docs/sources/event-streams/cloud-apps/appsflyer/>)[![App Center logo](/docs/images/logos/sources/appcenter-logo.svg)App Center](</docs/sources/event-streams/cloud-apps/appcenter/>)[![Auth0 logo](/docs/images/logos/sources/auth0.webp)Auth0](</docs/sources/event-streams/cloud-apps/auth0/>)[![Braze logo](/docs/images/logos/sources/braze-logo.svg)Braze](</docs/sources/event-streams/cloud-apps/braze-currents/>)[![Canny logo](/docs/images/logos/sources/canny.svg)Canny](</docs/sources/event-streams/cloud-apps/canny/>)[![ClickUp logo](/docs/images/logos/sources/clickup.svg)ClickUp](</docs/sources/event-streams/cloud-apps/clickup/>)[![Close CRM logo](/docs/images/logos/sources/close.webp)Close CRM](</docs/sources/event-streams/cloud-apps/close-crm/>)[![Customer.io logo](/docs/images/logos/sources/customerio.svg)Customer.io](</docs/sources/event-streams/cloud-apps/customerio/>)[![Extole logo](/docs/images/logos/sources/extole.webp)Extole](</docs/sources/event-streams/cloud-apps/extole/>)[![Facebook Lead Ads logo](/docs/images/logos/sources/facebook.svg)Facebook Lead Ads](</docs/sources/event-streams/cloud-apps/facebook-lead-ads/>)[![Formsort logo](/docs/images/logos/sources/formsort.svg)Formsort](</docs/sources/event-streams/cloud-apps/formsort/>)[![Gainsight PX logo](/docs/images/logos/sources/gainsight.svg)Gainsight PX](</docs/sources/event-streams/cloud-apps/gainsight-px/>)[![Iterable logo](/docs/images/logos/sources/Iterable.svg)Iterable](</docs/sources/event-streams/cloud-apps/iterable/>)[![Looker logo](/docs/images/logos/sources/looker.webp)Looker](</docs/sources/event-streams/cloud-apps/looker/>)[![Mailjet logo](/docs/images/logos/sources/mailjet.svg)Mailjet](</docs/sources/event-streams/cloud-apps/mailjet/>)[![Mailmodo logo](/docs/images/logos/sources/mailmodo.svg)Mailmodo](</docs/sources/event-streams/cloud-apps/mailmodo/>)[![Monday logo](/docs/images/logos/sources/monday.svg)Monday](</docs/sources/event-streams/cloud-apps/monday/>)[![MoEngage logo](/docs/images/logos/sources/MoEngage.svg)MoEngage](</docs/sources/event-streams/cloud-apps/moengage/>)[![Olark logo](/docs/images/logos/sources/olark.svg)Olark](</docs/sources/event-streams/cloud-apps/olark/>)[![Ortto logo](/docs/images/logos/sources/ortto.svg)Ortto](</docs/sources/event-streams/cloud-apps/ortto/>)[![PagerDuty logo](/docs/images/logos/sources/pagerduty.svg)PagerDuty](</docs/sources/event-streams/cloud-apps/pagerduty/>)[![Pipedream logo](/docs/images/logos/sources/pipedream.svg)Pipedream](</docs/sources/event-streams/cloud-apps/pipedream/>)[![PostHog logo](/docs/images/logos/sources/posthog.svg)PostHog](</docs/sources/event-streams/cloud-apps/posthog/>)[![Refiner logo](/docs/images/logos/sources/refiner.svg)Refiner](</docs/sources/event-streams/cloud-apps/refiner/>)[![RevenueCat logo](/docs/images/logos/sources/revenuecat.webp)RevenueCat](</docs/sources/event-streams/cloud-apps/revenuecat/>)[![SatisMeter logo](/docs/images/logos/sources/satismeter.svg)SatisMeter](</docs/sources/event-streams/cloud-apps/satismeter/>)[![Segment logo](/docs/images/logos/sources/segment.svg)Segment](</docs/sources/event-streams/cloud-apps/segment/>)[![Shopify logo](/docs/images/logos/sources/shopify.webp)Shopify](</docs/sources/event-streams/cloud-apps/shopify/>)[![Signl4 logo](/docs/images/logos/sources/signl4.svg)Signl4](</docs/sources/event-streams/cloud-apps/signl4/>)[![Slack logo](/docs/images/logos/sources/slack.svg)Slack](</docs/sources/event-streams/cloud-apps/slack/>)

## Event Stream destinations

Once events are ingested, you can forward them to over [200 destinations](<https://www.rudderstack.com/docs/destinations/overview/>) in our integrations library, or to your own [custom destinations](<https://www.rudderstack.com/docs/destinations/http-webhook/>) (using the Webhook destination integration).

Browse the [destination integration library](<https://www.rudderstack.com/docs/destinations/overview/>).

## Advanced features and use cases

This section covers two important advanced use cases you can implement on your Event Stream data - [**Transformations**](<https://www.rudderstack.com/docs/transformations/overview/>) and [**Identity Resolution**](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>).

### Transformations

RudderStack can [transform](<https://www.rudderstack.com/docs/transformations/overview/>) events in real-time using [Python](<https://www.rudderstack.com/docs/transformations/create/#python-transformations>) or [JavaScript](<https://www.rudderstack.com/docs/transformations/create/#javascript-transformations>) to customize your data flows. It can also ensure data integrity and consistency across your pipelines with [centralized tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) that provide full visibility into your customer data’s journey.

### User identification and identity resolution

You can also assign unique IDs for anonymous users via [Identity Stitching](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>) and reconcile unified customer [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) in your data warehouse.