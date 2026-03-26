# Tracking Plans

Monitor your event data with RudderStack tracking plans.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


**Tracking Plans** let you proactively monitor and act on non-compliant event data coming into your RudderStack sources based on predefined plans. This can help you prevent or de-risk situations where any missing or improperly configured event data can break your downstream destinations.

## Features

  * Set rules for `track` and non-`track` events (`identify`, `page`, `screen`, and `group`) that you want to send to downstream destinations. You can use these rules to:

    * Define which events should pass through, including events with and without properties.
    * Specify whether a property or attribute is required and assign the data type required to pass that event.
  * Use the [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) to evaluate your inbound events and metadata and compare them with your tracking plans.

  * Iteratively improve your tracking plans and have better control of your data with a robust versioning system.

  * Create and manage your tracking plans in the RudderStack dashboard or programmatically using the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>).


## Get started

See the following guides to learn more about the features and usage of tracking plans:

Guide| Description  
---|---  
[Create a Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/>)| Create a new tracking plan in the RudderStack dashboard.  
[View and Edit Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/>)| Manage your tracking plans in the RudderStack dashboard.  
[Code Generation (Codegen)](<https://www.rudderstack.com/docs/data-governance/tracking-plans/codegen/>)  
Beta| Generate language-specific code snippets based on your defined event schemas.  
[Tracking Plan Observability](<https://www.rudderstack.com/docs/data-governance/tracking-plans/observability/>)| Get complete visibility into the events passing through your tracking plan and any tracking plan violations.  
[Violation Management](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/>)| Learn about the different violation types in tracking plans and use the information to fix your event instrumentation and avoid future violations.  
[Migrate Tracking Plans from Spreadsheet](<https://www.rudderstack.com/docs/data-governance/tracking-plans/migration-guide/>)| Migrate tracking plans created using the tracking plan spreadsheet to the new format for easier management.  
  
## FAQ

#### Which RudderStack plans support the tracking plans feature?

The tracking plans feature is supported in all the [RudderStack plans](<https://rudderstack.com/pricing/>). However, note that you can create only one tracking plan in the Free plan.

#### Which events are supported by the tracking plans?

The tracking plans support [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>), and [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) events.

Note that the [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call is not supported.

#### Does RudderStack propagate the context related to any tracking plan violations?

RudderStack propagates any context related to the tracking plan violations to your destinations. You can use this context in your [transformations](<https://www.rudderstack.com/docs/transformations/overview/>) for filtering or modifying the events before they reach the destination.

#### Why do different events show different tracking plan versions in the live events viewer?

Different events may be validated against different tracking plan versions because RudderStack validates each event against the specific version that was used to instrument it.

This happens when:

  * You have multiple app versions deployed simultaneously
  * Each app version was instrumented using a different tracking plan version
  * The SDK sends the tracking plan version along with each event


This behavior ensures that each event is validated against the exact rules it was designed to follow, and prevents false validation errors when tracking plans evolve over time.

See [Tracking Plan observability](<https://www.rudderstack.com/docs/data-governance/tracking-plans/observability/#how-validation-works>) for more details.