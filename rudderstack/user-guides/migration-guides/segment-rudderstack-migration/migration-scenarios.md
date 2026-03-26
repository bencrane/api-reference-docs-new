# Migration Scenarios and Time Estimates

Understand the common scenarios users encounter while migrating from Segment to RudderStack.

* * *

  * __2 minute read

  * 


It is helpful to think about two broad categories for migrations to estimate the resources and time you will need to migrate:

**Simple migrations** \- Simple migrations generally involve a lower number of sources and destinations, without heavy use of Segment’s more advanced features or customization.

**Advanced migrations** \- Advanced migrations often involve a large number of sources and/or destinations and some level of customization of the Segment configuration.

## Simple migration

> ![info](/docs/images/info.svg)
> 
> This migration is relatively quick due to the minimal complexity involved in the process.

For a straightforward migration scenario, consider a company using Segment with a few sources and a handful of destinations, like a website and mobile app feeding into a CRM, email marketing tool, and customer success system. The process typically involves mapping these sources to their corresponding destinations in RudderStack.

This migration includes the following steps:

  * Configuring source and destination to match existing integrations
  * Updating SDKs across platforms, and
  * Ensuring data consistency between Segment and RudderStack before switching off Segment.


Estimated timelines for a simple migration:

  * **Initial assessment and planning** : 1 week
  * **Configuration and setup** : 1 week
  * **Testing and validation** : 1 week
  * **Deployment** : 1 week


**Summary** : Typically 2-4 weeks (1 sprint)

## Complex migration

> ![info](/docs/images/info.svg)
> 
> This process requires careful consideration of data integrity, backward compatibility, and ongoing support for legacy systems during the transition.

A more complex migration often involves numerous data sources, diverse destinations, custom configurations, and legacy app versions utilizing Segment. In addition to migrating pipelines, this migration may include:

  * Implementing additional changes like introducing a new analytics tool
  * Re-instrumenting events for better event tracking and analysis
  * Migrating any customization work (i.e., customized integration configurations)


Estimated timelines for a complex migration:

  * **Comprehensive assessment** of Segment implementation and planning: 2 weeks
  * **Customization and migration** : 4 weeks
  * **Testing across multiple environments** : 2 weeks
  * **Deployment and phased rollout** : 4 weeks


**Summary** : Typically 8-12 weeks (4-6 sprints)

> ![info](/docs/images/info.svg)
> 
> Note that this timeline is only an estimate, and assumes dedicated resources focused on the project. Timelines can be longer for highly complex Segment configrations, especially when legacy apps need to be incrementally deprecated over a multi-month period, or technical debt is addressed as part of the migration.

## Next steps

[Migration Timeline and Cutover Best Practices](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/timelines-cutover/>)