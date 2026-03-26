# Migrate Tracking Plans from Spreadsheet

Migrate Tracking Plans created using the Tracking Plan spreadsheet to the new format for easier management.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


This guide will help you migrate your Tracking Plans created using the [Tracking Plan Spreadsheet](<https://www.rudderstack.com/docs/data-governance/tracking-plans/tracking-plan-spreadsheet/>) to the new format.

## Overview

RudderStack lets you easily migrate your Tracking Plans created using the [Tracking Plan Spreadsheet](<https://www.rudderstack.com/docs/data-governance/tracking-plans/tracking-plan-spreadsheet/>) to the new format where you can edit events, properties, and Tracking Plan rules in the RudderStack dashboard.

## Migrate Tracking Plans

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can migrate Tracking Plans.
>   * Make sure to see the Migration considerations before you migrate your Tracking Plans.
> 


You will see the **Migration now available** banner below the Tracking Plans created using the spreadsheet:

[![Tracking Plan migration banner](/docs/images/data-governance/tracking-plan-migration-banner.webp)](</docs/images/data-governance/tracking-plan-migration-banner.webp>)

Go to the Tracking Plan and click **Migrate** to start the migration process.

[![Tracking Plan migration process](/docs/images/data-governance/tracking-plan-migration-process.webp)](</docs/images/data-governance/tracking-plan-migration-process.webp>)

Once the Tracking Plan is migrated successfully, you can view all the events and properties in the dashboard, and [make changes](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/>) as required.

## Migration considerations

Once you migrate, note that:

  * RudderStack deletes the old Tracking Plan.
    * You **cannot** use the spreadsheet to view or manage the newly created Tracking Plan.
    * You can manage your Tracking Plans via the dashboard or the [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>).
  * You will **not see** the historical violations or event counts once you migrate your Tracking Plan to the new format in the RudderStack dashboard.
  * RudderStack supports up to [three levels of nesting](<https://www.rudderstack.com/docs/data-governance/tracking-plans/view-edit-tracking-plans/#add-nested-event-properties>) in the event properties of object or array data type. The Tracking Plan **cannot** be migrated if one or more of your event mappings have more than three levels of nesting and you will see the following error:

[![Tracking Plan migration error](/docs/images/data-governance/tracking-plan-migration-error.webp)](</docs/images/data-governance/tracking-plan-migration-error.webp>)

  * RudderStack does not permit certain keywords in the event’s JSON schema. You will get an “**Unsupported rules found for event** ” error if you try to migrate Tracking Plans having these keywords.


## FAQ

#### Which keywords are not supported while migrating the Tracking Plan to the new format in the dashboard?

While migrating your Tracking Plans to the new format, you will encounter an error if your Tracking Plan rules contain any of the following advanced keywords as event property names:

  * `oneOf` / `allOf`
  * `if` / `then` / `else`
  * `$def` / `$ref`
  * `const`
  * `default`


See the [JSON schema](<https://www.rudderstack.com/docs/api/data-catalog-api/json-schema/>) guide for the list of all supported keywords.