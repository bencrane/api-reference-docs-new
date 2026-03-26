# Data Catalog Events

Create and manage events in your Data Catalog.

* * *

  * __2 minute read

  * 


This guide walks you through creating and managing your events in the Data Catalog.

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to manage event properties in the Data Catalog.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the following [permission](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) in their workspace policy:

Resource| Permission| Description  
---|---|---  
Data Catalog| **Edit**|  Make changes to the configuration of Data Catalog  
  
**Click here to see how these permissions appear in the workspace policy**.  
![Data Catalog permissions to manage properties](/docs/images/access-management/data-catalog-permissions.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) have full access to manage the Data Catalog
  * Members must have the **Connections Admin** role in their workspace policy to manage events in the Data Catalog

[![Data Catalog permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## Add event

RudderStack provides two ways of creating and adding events to your Data Catalog:

  * In the Data Catalog itself
  * While editing your tracking plan


### In Data Catalog

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com/>) and go to **Govern** > **Data Catalog** in the left sidebar.
  2. In the **Events** tab, click **Add event**.

[![Add new event](/docs/images/data-governance/data-catalog-add-event.webp)](</docs/images/data-governance/data-catalog-add-event.webp>)

  3. Select event type from the dropdown. Note that you **cannot** update the event type later.
  4. Specify the event name and description.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You cannot set a blank event name - it must be at least 1 character long.
> 
>   * RudderStack supports all UTF-8 characters in event names.
> 
>   * The event name can start with a letter, number, or special character. Some examples of valid event names:
> 
>     * `Test Event`
>     * `5Test Event`
>     * `@4Test Event`
> 


  5. Optionally, specify the [event category](<https://www.rudderstack.com/docs/data-governance/data-catalog/categories/#manage-event-categories>) from the dropdown.
  6. Click **Save**.

[![Add new event](/docs/images/data-governance/new-event.webp)](</docs/images/data-governance/new-event.webp>)

### While editing a tracking plan

You can also create a new event while [adding a new event schema](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#add-a-new-event-schema>) to your tracking plan configuration.

> ![info](/docs/images/info.svg)
> 
> RudderStack automatically adds this event to your Data Catalog.

  1. Go to **Govern** > **Tracking Plans** to see all the tracking plans in your workspace.
  2. Click the **Add event schema** button.

[![Tracking Plan schema tab](/docs/images/data-governance/tracking-plans/tracking-plan-schema.webp)](</docs/images/data-governance/tracking-plans/tracking-plan-schema.webp>)

  3. Click **Create a new event**.

[![Tracking Plan build schema event options](/docs/images/data-governance/tracking-plans/build-schema.webp)](</docs/images/data-governance/tracking-plans/build-schema.webp>)

  4. Specify the event type, name, description, and category.
  5. Click **Create event schema**.

[![Tracking Plan create a new event](/docs/images/data-governance/tracking-plans/create-new-event.webp)](</docs/images/data-governance/tracking-plans/create-new-event.webp>)

## Event details

Click an event in the Data Catalog to see the following information:

  * Event details.
  * Connections to tracking plans, along with the connected sources and associated properties (only visible after you use the event to create a tracking plan).
  * Option to delete the event. Note that you **cannot** delete any event that is already connected to any tracking plan.


You can also make any changes to the event and click **Save** for the changes to take effect:

[![View event details in Data Catalog](/docs/images/data-governance/view-event.webp)](</docs/images/data-governance/view-event.webp>)