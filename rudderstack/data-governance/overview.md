# Data Governance Overview

Learn about RudderStack’s data governance offerings related to data quality and compliance.

* * *

  * __5 minute read

  * 


RudderStack’s data governance feature lets you set controls in place to ensure the quality and integrity of your data in a secure and compliant manner.

Some key features of RudderStack’s data governance offerings include:

  * **Data quality**: RudderStack guarantees clean data collection at the source, eliminating time-consuming cleaning and wrangling work downstream.
  * **Data compliance**: RudderStack’s data compliance toolkit makes it easy to manage consent, collection, storage, and deletion - all in one central platform.
  * **Monitoring and alerting**: RudderStack’s robust monitoring and alerting features help you get complete observability on the data entering your systems and take quick actions on potential issues.


## Data quality

Bad customer data leads to more time spent on data cleaning and wrangling. It limits your ability to support business teams effectively, undermines your AI efforts, and ultimately hinders growth.

RudderStack’s data quality toolkit equips you to collect clean data at the source, so you can spend less time wrangling and more time helping your business drive revenue. You can use it to collaborate on event definitions, manage violations with custom rules, monitor quality, and fix schemas in real time.

[![Data quality](/docs/images/data-governance/data-quality.webp)](</docs/images/data-governance/data-quality.webp>)

### Data Catalog

RudderStack provides the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) feature to build a comprehensive event catalog that you can use to set standardized data definitions for your tracking plans.

RudderStack automatically builds an event catalog from all events ingested into the system via your sources. You can also create custom events and properties and add them to your catalog.

While creating a new tracking plan, you can add the events and properties from your event catalog and avoid wasting time defining the tracking plan rules.

See the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) guide for more details on this feature.

### Event Audit API

RudderStack’s [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) allows you to diagnose inconsistencies in your event data programmatically. The feature gives you access to information on all your events and their metadata, including event schema, event payload versions, data types, and more. With this access, your teams can quickly pinpoint the specific nature and source of event data inconsistencies.

See the [Event Audit API reference](<https://www.rudderstack.com/docs/api/event-audit-api/>) for more details.

### Tracking Plans

[Tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) let you proactively monitor and act on non-compliant event data coming into your RudderStack sources based on predefined plans. This helps minimize the risk of improperly configured event data breaking your downstream systems.

Tracking plans evaluate each incoming event for any inconsistencies and automatically flag violations like unplanned events, erroneous key/value properties, etc. You can also configure your plans to decide what to do with such events, whether to deliver them with a flag, deliver them to a specific destination, or drop them entirely.

### Real-time schema fixes

If errors are propagated in events, you can use that information in the schema to customize schema fixes for each individual downstream destination. For example, you can fix a data type, delete a property, etc., to deliver a valid event payload.

You can apply these fixes in the pipeline by leveraging RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature to transform faulty event payloads, meaning no dev tickets have to be opened to fix instrumentation upstream in websites and apps.

## Data compliance

As privacy regulations tighten and businesses focus on protecting their customers’ sensitive information, data teams often feel the pain of inflexible infrastructure. Cumbersome processes and complex implementations to meet compliance standards create tedious work that slows down product and marketing teams.

RudderStack’s warehouse-native architecture and robust data compliance toolkit make it easy to manage consent-based data collection, storage, and deletion all in one centralized platform.

[![Data compliance](/docs/images/data-governance/data-compliance.webp)](</docs/images/data-governance/data-compliance.webp>)

### Consent management

RudderStack’s holistic approach to consent management lets you:

  * Implement both client-side and server-side consent categorization for each downstream integration.
  * Set the pre- and post-consent SDK behavior, minimizing any data loss related to attribution, acquisition, and the overall user journey.
  * Be fully compliant with the internal requirements and region-specific regulatory laws on a tool-by-tool basis, while simplifying implementation.
  * Maintain granular control over the cookie and storage settings, in which you can map each downstream integration to specific consent categories.


RudderStack offers a fully integrated consent solution with popular consent management tools like OneTrust, Ketch, and other custom-built systems.

See the [Consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/>) guide for more details.

### Cookieless tracking

Cookies are useful in gathering valuable insights that help in personalizing user experiences. However, gathering these insights while adhering to the stringent privacy norms can be a significant challenge.

RudderStack’s cookieless tracking feature provides an efficient way of gathering user data without relying on cookies. It gives you complete control over what user information to store (`userId`, `anonymousId`, etc.) and where to store it (local storage, browser’s cookies, or not storing it at all) while loading the JavaScript SDK.

See [Cookieless Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>) to learn more and explore various configurations to use it.

### User Suppression API

RudderStack provides a [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>) that lets you programmatically create regulations to suspend data collection and delete data for specific users. You can apply these regulations across multiple destination integrations simultaneously and simplify the process of implementing compliance requests.

See the [User Suppression API reference](<https://www.rudderstack.com/docs/api/user-suppression-api/>) for more details.

## Monitoring and alerting

Managing data quality across a number of sources and destinations isn’t easy, especially in a complex data infrastructure. RudderStack’s monitoring and alerting capabilities help you track event volume trends, violations, and get a holistic view of your system’s health. You can also configure thresholds for key alerts across your data stack.

### Health dashboard

RudderStack’s intuitive health dashboard provides a global view of data health across all your pipelines and integrations, including metrics on data ingestion, delivery, and tracking plan violations.

The health dashboard is a central place to track trends in data volume and violations so you can identify and fix potential problems before they become acute and impact your downstream systems.

See the [Health Dashboard](<https://www.rudderstack.com/docs/data-governance/health-dashboard/>) guide for more details.

### Configurable alerts

RudderStack’s alerting capabilities let you set up alerts for critical data issues so you get notified immediately and can take immediate remedial actions before they escalate into major issues.

See the [Configurable Alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) guide for more information.