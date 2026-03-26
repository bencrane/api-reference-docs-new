# Closed Beta Features

Learn about the Closed Beta features available in RudderStack.

* * *

  * __3 minute read

  * 


This page lists the latest **Closed Beta** features supported by RudderStack. [Contact](<mailto:product@rudderstack.com>) the RudderStack Product team to learn more about these features.

## Overview

**Closed Beta** features are early-stage features available to a limited set of users for testing and feedback. These features are still under active development and require special access through RudderStack’s **Early Access Program**. They may have limited functionality or undergo significant changes before general availability.

> ![announcement](/docs/images/announcement.svg)
> 
> Closed Beta features are generally behind a feature flag.
> 
> [Contact the RudderStack team](<mailto:support@rudderstack.com?subject=I%20have%20a%20question%20about%20the%20Early%20Access%20Program>) to enable these features for your workspace.

The following sections list the **Closed Beta** features available in RudderStack.

## Features list

**Data governance**

  * Custom data types
  * Event blocking


**Beta integrations**

  * Custom Web Device Mode destination
  * Facebook Lead Ads source


## Data governance

The following sections explain each of the **Closed Beta** features that are a part of RudderStack’s [Data Governance](<https://www.rudderstack.com/docs/data-governance/overview/>) offering.

### Custom data types

  


With [Custom Types](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#custom-data-types>), you can build and manage a separate, centralized library of property rules, then apply them to multiple properties across your Data Catalog.

Custom data types give you the ability to:

  * More easily manage and apply the same rule across multiple properties.
  * Implement more complex rules for properties.


See the [Release Notes](<https://www.rudderstack.com/docs/releases/custom-types/>) for more information, or [Custom Data Types documentation](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#custom-data-types>) to get started.

### Event blocking

> ![announcement](/docs/images/announcement.svg)
> 
> Event blocking is available in the [Growth](<https://www.rudderstack.com/pricing/>) (up to 2 blocked events) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) (unlimited) plans.

RudderStack’s [Event Blocking](<https://www.rudderstack.com/docs/data-governance/event-blocking/>) feature prevents specific events from being ingested by RudderStack, helping you maintain clean data capture and control costs.

With this feature, you can:

  * Block unwanted events from entering your data pipelines entirely.
  * Reduce billable event volume by preventing unnecessary events.
  * Handle mobile lifecycle events, bug-related overflows, and deprecated events.
  * Configure event blocking through the Data Catalog interface.
  * Monitor blocked event metrics at the source level.


See the [Event Blocking documentation](<https://www.rudderstack.com/docs/data-governance/event-blocking/>) to get started.

## Integrations

The following sections explain the RudderStack integrations currently in **Closed Beta**.

### Custom Web Device Mode destination

Custom web device mode integrations run client-side in your users’ browsers ([device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)), giving you direct control over how events are transformed and sent to your chosen tools.

This approach is helpful when you need to:

  * **Connect to niche or proprietary tools** that aren’t part of RudderStack’s standard integration catalog.
  * **Implement custom business logic** for event transformation that goes beyond what configuration settings allow.
  * **Maintain real-time, client-side connections** to tools that require immediate data processing.
  * **Bridge legacy systems** that need specific data formats or authentication methods.


See the [Custom Web Device Mode Destination documentation](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/>) to get started.

### Facebook Lead Ads source

RudderStack’s [Facebook Lead Ads source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/fb-lead-ads/>) lets you ingest lead generation events from your Facebook Lead Ad campaigns directly into RudderStack.

Once you configure Facebook Lead Ads as a source, RudderStack automatically listens for new leads on your selected Facebook page and converts them into `identify` events — capturing form fields like email, phone number, name, and any custom fields you’ve defined. It also deduplicates events automatically to prevent duplicate records in your downstream destinations.

See the [Facebook Lead Ads Source documentation](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/fb-lead-ads/>) to get started.