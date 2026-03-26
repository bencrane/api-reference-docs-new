# Migrate Existing Segment Events

Migrate your existing Segment events by connecting Segment to RudderStack.

* * *

  * __3 minute read

  * 


Many users choose to start their migration by importing their existing Segment events. There are two primary benefits:

  1. Simplifying and speeding up the migration process
  2. De-risking data quality issues and enforcing granular data governance throughout the migration


> ![info](/docs/images/info.svg)
> 
> See the [Segment source documentation](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/segment/#getting-started>) for detailed steps on setting up Segment as a source in RudderStack.

RudderStack’s [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) feature can serve as a central repository for your events and properties flowing in from Segment, and is beneficial for teams to review or make changes before migrating.

You can also create a RudderStack [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) to apply data governance rules to your Segment events and manage any violations of those rules, ensuring strict data continuity during the migration.

In many cases, users also want to enhance or modify their events for cleaner tracking with RudderStack. RudderStack can transform Segment events in real time, which is particularly useful if you need to implement new naming or formatting conventions without updating code in your website or app.

## Segment source setup considerations

When setting up Segment as a source in RudderStack, you have a few critical decisions to make that will impact your data governance, event tracking, and user continuity:

### Starting fresh vs. leveraging existing events

One of the first decisions you will have to make is whether to start with a clean slate in RudderStack or use your existing Segment event taxonomy.

Most companies migrating from Segment have some things they want to clean up. It’s easy for your data schemas to get fragmented when multiple users and several years have elapsed.

The easiest thing to do is to use the [Segment source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/segment/>) in RudderStack to populate the RudderStack data catalog and tracking plans by importing your Segment events. This approach offers a few crucial benefits:

  * Maintains a historical record of your event taxonomy
  * Provides a foundation for future event planning and optimization
  * Allows for better data governance and consistency


### The user ID dilemma

Another critical consideration is migrating your existing Segment user IDs to RudderStack. Maintaining data continuity by migrating existing segment and ensuring a smooth transition is recommended. By carrying over your user IDs, you’ll be able to:

  * Preserve user profiles and journeys across tools
  * Avoid data discrepancies and duplication
  * Enable more accurate and insightful analysis


For more information, read the detailed section on [migrating user data](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/advanced-migration/#migrate-user-data>).

### Handling legacy app versions

If you have older app versions (like mobile, Roku or other TV apps) that will continue running the Segment SDK for a period of time until users update, you can use Segment as a source in RudderStack to ensure data continuity during your phased migration. This approach lets you:

  * Gradually sunset Segment SDKs without disrupting data flows (i.e., data for a small percentage of users running old apps will be ingested to RudderStack through Segment as a source)
  * Maintain a single source of truth in your warehouse (which enalbles comprehensive reporting across RudderStack and legacy app Segment data)
  * Minimize dependencies and simplify your overall data architecture


For more information, read the detailed section on [migrating legacy app versions](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/advanced-migration/#migrate-legacy-app-versions-running-the-segment-sdk>).

## Data governance advantages

One of the key advantages of migrating from Segment to RudderStack is the ability to uplevel your data governance. With RudderStack’s Tracking Plans and Data Catalog features, you can:

  * Standardize event naming and properties across your stack
  * Enforce data quality and consistency with validation rules
  * Gain full visibility into your event schema
  * Streamline data discovery and democratization for your teams


For more information, read the detailed section on [migrating legacy app versions](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/advanced-migration/#migrate-legacy-app-versions-running-the-segment-sdk>).

## Next steps

[Phase 1: Basic SDK, event and property migration](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/basic-migration/>)