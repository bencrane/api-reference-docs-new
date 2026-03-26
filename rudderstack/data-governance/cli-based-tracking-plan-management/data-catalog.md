# Manage Data Catalog using Rudder CLI Alpha

Manage events, properties, and custom data types in Data Catalog using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This section explains how to create and manage events, properties, and custom data types in Data Catalog using Rudder CLI.

> ![info](/docs/images/info.svg)
> 
> **Important**
> 
> Data Catalog management via Rudder CLI is a push-only feature, meaning you can only push changes to your RudderStack workspace. You cannot pull changes from your workspace to your local system.

## Overview

RudderStack’s [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) feature lets you centrally define and manage the events, properties, and data structures that power your data collection strategy. It serves as a single source of truth for your organization’s data schema, helping teams maintain consistency across different platforms and applications.

Data Catalog helps you:

  * Standardize event definitions and properties across all platforms
  * Create reusable data validation patterns with custom types
  * Maintain data quality through centralized schema management
  * Ensure consistency between different teams and applications
  * Track schema changes through version control


### Data Catalog components

The Data Catalog consists of the following components:

  * **Events** : Events represent specific user actions or occurrences you want to track in your application. They can be events related to user actions (`track`), user identification (`identify`), view tracking (`page`/`screen`), or organization/account tracking (`group`).
  * **Properties** : Properties are the attributes associated with events. They provide additional context about the event and can include user properties, event-specific properties, and contextual properties shared across events.
  * **Custom Types** : Custom types are reusable validation patterns and data structures that you can use across multiple properties.


You can use these components to configure [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) that enforce consistent data collection practices.

## How it works

Rudder CLI lets you manage the following Data Catalog components through YAML configuration files in your project:

  * [Events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>) that represent user actions or occurrences you want to track
  * [Event Categories](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/categories/>) that group events into logical categories
  * [Properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) that provide additional context and attributes for events
  * [Custom Types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) for reusable validation patterns and data structures


> ![info](/docs/images/info.svg)
> 
> You can reference custom types across multiple properties, ensuring consistent data validation, standardized formats, and reduced duplication.

You can then use Rudder CLI to:

  * Add and validate definitions for these components locally
  * Deploy the Catalog components to your workspace
  * Manage changes through version control


## In this section

See the following guides to start creating and managing your Data Catalog project in Rudder CLI:

Guide| Description  
---|---  
[Project Setup](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>)| Set up your Data Catalog project in Rudder CLI.  
[Events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>)| Define and manage your events and event categories via YAML files.  
[Event Categories](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/categories/>)| Group events into logical categories.  
[Properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>)| Create and manage properties in your Data Catalog via YAML files.  
[Custom Types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>)| Create reusable validation patterns and reference them in your properties.  
[YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>)| Complete YAML reference for defining and using your Data Catalog resources.