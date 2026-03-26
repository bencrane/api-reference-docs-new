# Data Catalog Categories

Create and manage event categories in your Data Catalog.

* * *

  * __less than a minute

  * 


This guide walks you through creating and managing your event categories in your Data Catalog.

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
  * Members must have the **Connections Admin** role in their workspace policy to manage event categories in the Data Catalog

[![Data Catalog permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## Manage event categories

You can associate an event in the Data Catalog with a category it best fits into.

  1. Go to the **Events** tab and click **Select category**.
  2. Choose a category from the dropdown.

[![Data catalog categories](/docs/images/data-governance/categories.webp)](</docs/images/data-governance/categories.webp>)

RudderStack provides the following categories by default:

  * Conversion
  * General
  * Marketing
  * Onboarding


## Assign a custom category

Apart from the default categories mentioned above, you can also assign a custom category to an event by clicking **Select category** and entering the required category name.

[![Data catalog custom category](/docs/images/data-governance/custom-category.webp)](</docs/images/data-governance/custom-category.webp>)