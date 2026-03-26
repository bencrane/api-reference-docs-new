# Create Tracking Plan in RudderStack

Create a new Tracking Plan in the RudderStack dashboard.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __7 minute read

  * 


This guide will help you create a new tracking plan in the RudderStack dashboard.

## Overview

You can create a new Tracking Plans using any of the following approaches:

  * From an existing Event Stream source
  * Using a Tracking Plan template
  * From the events and properties in the Data Catalog


> ![success](/docs/images/tick.svg)
> 
> You can also use the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>) to create and manage your Tracking Plans programmatically.

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage Tracking Plans.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) in their workspace policy:

Resource| Permission| Description  
---|---|---  
Tracking Plans| **Edit**|  Make changes to the configuration of Tracking Plans  
Tracking Plans| **Create & Delete**| Create or delete Tracking Plans  
Tracking Plans| **Connect**|  Connect a Tracking Plan to a source  
  


> ![warning](/docs/images/warning.svg)To make a connection, that is, connect a Tracking Plan to a source, the member must have both **Edit** and **Connect** permissions on both the resources.  
  
Data Catalog| **Edit**|  Make changes to the configuration of Data Catalog  
  


> ![info](/docs/images/info.svg)This permission is required to create Tracking Plans via the following methods:  
>   
> 
> 
>   * From an Existing Event Stream source
>   * Using a Tracking Plan template
> 
  
  
**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to create Tracking Plans in RudderStack dashboard](/docs/images/access-management/tracking-plan-permissions.webp)![Data Catalog permissions to create Tracking Plans](/docs/images/access-management/data-catalog-permissions.webp)  


The following image summarizes the required permissions for creating Tracking Plans using the three methods explained in this guide:

[![Tracking plan creation permissions summary](/docs/images/access-management/tracking-plans-permissions-summary.webp)](</docs/images/access-management/tracking-plans-permissions-summary.webp>)

#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to create and manage Tracking Plans
  * Members with the **Connections Admin** role in their workspace policy can create and manage Tracking Plans
  * Members with the **Connections Editor** role in their workspace policy can only connect Tracking Plans to Event Stream sources

![Tracking plan creation permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)

## 1\. From an existing Event Stream source

You can create a Tracking Plan from an existing event data source. This option leverages the [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) to import the events and properties tracked by the event data source and generates an initial plan.

> ![warning](/docs/images/warning.svg)
> 
> Before you proceed, make sure the **Event Audit API** setting is turned on in your [RudderStack dashboard](<https://app.rudderstack.com/>).
> 
> Go to **Settings** > **Workspace** and click the **Data Management** tab. Scroll down to the **Data governance** section and turn on the **Event Audit API** toggle.
> 
> ![Event Audit API setting in RudderStack dashboard](/docs/images/api/event-audit-api-dashboard.webp)
> 
> See [Enable Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/#enable-event-audit-api>) section for more information.

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>) and go to **Govern** > **Tracking Plans** option in the left sidebar.
  2. Click **Create Tracking Plan**.

[![Create blank Tracking Plan](/docs/images/data-governance/create-tracking-plan.webp)](</docs/images/data-governance/create-tracking-plan.webp>)

  3. Select **Pull from source** on the next screen.

[![Create blank Tracking Plan](/docs/images/data-governance/pull-from-source.webp)](</docs/images/data-governance/pull-from-source.webp>)

  4. Select the event stream source from which you want to import the tracked events and properties and click **Continue**.
  5. Enter a unique name and description for your Tracking Plan and click **Continue**.
  6. Select events tracked from the source and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * The events and properties listed here are obtained from the [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>).
>   * RudderStack automatically adds these events and properties to the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) if they do not exist already.
> 


[![Select events for the Tracking Plan](/docs/images/data-governance/pull-from-source-select-events.webp)](</docs/images/data-governance/pull-from-source-select-events.webp>)

  7. In the **Map properties to events** section, RudderStack displays the list of events selected in the above step with the associated properties.

[![Map properties for the Tracking Plan](/docs/images/data-governance/tracking-plans/event-property-mapping-source.webp)](</docs/images/data-governance/tracking-plans/event-property-mapping-source.webp>)

  8. You can also add more properties to an event from the Data Catalog:


  * Go to the **Add Properties** tab.
  * Select the **Event** from the dropdown.
  * Click the **Add** button next to the properties you want to add.


> ![info](/docs/images/info.svg)
> 
> You can also define nested properties for an event in your Tracking Plan.
> 
> Based on the schema sampled from the incoming events, RudderStack shows up to **three levels** of nesting for a property of Object or Array data type. See Nested properties for Tracking Plans created from source for more information.

[![Additional properties for the events](/docs/images/data-governance/tracking-plans/event-property-mapping-source-1.webp)](</docs/images/data-governance/tracking-plans/event-property-mapping-source-1.webp>)

In addition, you can:

  * Configure the event settings to allow unplanned properties.
  * Remove an event from the Tracking Plan.
  * Mark the property as optional or required by clicking the **Optional** /**Required** option.
  * Remove specific properties from the event.

[![Event and property mapping options while creating Tracking Plan](/docs/images/data-governance/tracking-plans/event-property-options.webp)](</docs/images/data-governance/tracking-plans/event-property-options.webp>)

  9. Select the sources you want to connect to the Tracking Plan and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> You can connect a Tracking Plan to multiple sources. However, note that a source can have only one Tracking Plan connected to it at a given time.

  10. Configure the tracking plan settings for specific event types and click **Create Tracking Plan**.

[![Create Tracking plan](/docs/images/data-governance/create-tracking-plan-settings.webp)](</docs/images/data-governance/create-tracking-plan-settings.webp>)

  11. (**Optional but Recommended**) Use [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) for autocomplete and linting.


## 2\. Using a Tracking Plan template

Use this option to import your event and property mappings from a default RudderStack template:

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>) and go to **Govern** > **Tracking Plans** option in the left sidebar.
  2. Click **Create Tracking Plan**.

[![Create blank Tracking Plan](/docs/images/data-governance/create-tracking-plan.webp)](</docs/images/data-governance/create-tracking-plan.webp>)

  3. Click **Use template**.

[![Create blank Tracking Plan](/docs/images/data-governance/pull-from-source.webp)](</docs/images/data-governance/pull-from-source.webp>)

  4. Select the RudderStack template and click **Continue**.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports the **Ecommerce** Tracking Plan template.

  5. Add a Tracking Plan name and description and click **Continue**.
  6. In the **Map properties to events** section, RudderStack displays the list of events and properties inherited from the Tracking Plan template. You can customize these events and their associated properties for the Tracking Plan as per your requirement.

[![Map properties for the Tracking Plan](/docs/images/data-governance/tracking-plans/event-property-mapping-source.webp)](</docs/images/data-governance/tracking-plans/event-property-mapping-source.webp>)

  7. You can also add more properties to an event from the Data Catalog:


  * Go to the **Add Properties** tab.
  * Select the **Event** from the dropdown.
  * Click the **Add** button next to the property you want to add.


> ![info](/docs/images/info.svg)
> 
> You can also add [nested properties](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#add-nested-event-properties>) for an event in your Tracking Plan. You can add up to three levels of nesting for a property of Object or Array data type.

[![Additional properties for the events](/docs/images/data-governance/tracking-plans/event-property-mapping-source-1.webp)](</docs/images/data-governance/tracking-plans/event-property-mapping-source-1.webp>)

In addition, you can:

  * Add or remove an event from the Tracking Plan.
  * Configure the event settings to allow unplanned properties.
  * Remove specific properties from the event.

[![Event and property mapping options while creating Tracking Plan](/docs/images/data-governance/tracking-plans/event-property-options.webp)](</docs/images/data-governance/tracking-plans/event-property-options.webp>)

  8. Connect the Tracking Plan to the required sources.


> ![warning](/docs/images/warning.svg)
> 
> You can connect a Tracking Plan to multiple sources. However, note that a source can have only one Tracking Plan connected to it at a given time.

  9. Configure the tracking plan settings for specific event types and click **Create Tracking Plan**.

[![Create Tracking plan](/docs/images/data-governance/create-tracking-plan-settings.webp)](</docs/images/data-governance/create-tracking-plan-settings.webp>)

  10. (**Optional but Recommended**) Use [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) for autocomplete and linting.


## 3\. From the Data Catalog

You can create a Tracking Plan from scratch using the events and properties defined in the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) section:

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>) and go to **Govern** > **Tracking Plans** option in the left sidebar.
  2. Click **Create Tracking Plan**.

[![Create blank Tracking Plan](/docs/images/data-governance/create-tracking-plan.webp)](</docs/images/data-governance/create-tracking-plan.webp>)

  3. Select **From Data Catalog** on the next screen.

[![Create blank Tracking Plan from Data Catalog](/docs/images/data-governance/pull-from-source.webp)](</docs/images/data-governance/pull-from-source.webp>)

  4. Enter a unique name and description for your Tracking Plan.
  5. Choose the required events from the displayed events list (populated from the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>)) and click **Continue**.

[![Select events for Tracking Plan](/docs/images/data-governance/select-events-new.webp)](</docs/images/data-governance/select-events-new.webp>)

  6. In the **Map properties to events** section, add properties (populated from [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>)) to map to each event by clicking the **Add properties** button.


> ![info](/docs/images/info.svg)
> 
> You can also add [nested properties](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#add-nested-event-properties>) for an event in your Tracking Plan. You can add up to three levels of nesting for a property of Object or Array data type.

[![Create blank Tracking Plan](/docs/images/data-governance/event-property-mapping-new.webp)](</docs/images/data-governance/event-property-mapping-new.webp>)

  7. Click the **Add** button next to the property you want to add.

[![Add properties for the events](/docs/images/data-governance/event-property-mapping-source-new.webp)](</docs/images/data-governance/event-property-mapping-source-new.webp>)

In addition, you can:

  * Add or remove an event from the Tracking Plan.
  * Configure the event settings to allow unplanned properties.
  * Remove specific properties from the event.
  * Mark a property as **Optional** or **Required**.

[![Event and property mapping options while creating Tracking Plan](/docs/images/data-governance/tracking-plans/event-property-options.webp)](</docs/images/data-governance/tracking-plans/event-property-options.webp>)

  8. Select the sources you want to connect to the Tracking Plan and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> You can connect a Tracking Plan to multiple sources. However, note that a source can have only one Tracking Plan connected to it at a given time.

  9. Configure the tracking plan settings for specific event types and click **Create Tracking Plan**.

[![Create Tracking plan](/docs/images/data-governance/create-tracking-plan-settings.webp)](</docs/images/data-governance/create-tracking-plan-settings.webp>)

  10. (**Optional but Recommended**) Use [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) for autocomplete and linting.


## Configure tracking plan settings

When creating a new tracking plan, you can define how RudderStack processes events that do not adhere to the tracking plan rules.

[![Create Tracking plan](/docs/images/data-governance/create-tracking-plan-settings.webp)](</docs/images/data-governance/create-tracking-plan-settings.webp>)

The settings are described below:

Setting| Description  
---|---  
Event type| Select the event type (**Track** , **Identify** , **Group** , **Page** , or **Screen**) for which you want to configure the tracking plan settings.  
Drop events with unplanned event names| Toggle on this setting to drop events that do not match the events defined in your tracking plan.  
Drop events with unplanned event properties| Toggle on this setting to drop all events that contain properties which do not match the list of properties defined for that event in your tracking plan.  
Drop events with violations| Toggle on this setting to drop events that have any [validation errors](<https://www.rudderstack.com/docs/data-governance/tracking-plans/violation-management/#violation-types>).  
Propagate errors| Toggle on this setting to propagate any tracking plan error messages in your event payload. RudderStack recommends turning this setting on to assess the performance of your tracking plans.  
  
## Tracking plan version validation

When you connect a source to a tracking plan, RudderStack validates incoming events against the specific tracking plan version that was used to instrument each event. This version-aware validation ensures:

  * **Accurate validation** : Events are validated against the exact rules they were designed to follow
  * **Multi-version support** : Different app versions can run simultaneously without validation conflicts
  * **Evolution safety** : Tracking plan changes don’t break existing app versions


This behavior is particularly important when using [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) for type-safe instrumentation, as it embeds the tracking plan version in the generated code.

See [Tracking Plan observability](<https://www.rudderstack.com/docs/data-governance/tracking-plans/observability/#how-validation-works>) for more details.