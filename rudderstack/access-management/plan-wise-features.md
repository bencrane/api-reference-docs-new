# Plan-wise Access Management Features

Learn about the Access Management features available across different RudderStack plans.

* * *

  * __3 minute read

  * 


This reference provides a complete breakdown of Access Management feature availability and limits across all RudderStack Cloud plans.

## Overview

The following table provides an overview of the Access Management features available across different RudderStack plans:

Feature| Free| Starter| Growth| Enterprise  
---|---|---|---|---  
Member management|  __  
  
Limited to 10 members per organization|  __  
  
Limited to 10 members per organization|  __  
  
Unlimited members|  __  
  
Unlimited members  
Configurable Workspace Default Policy|  __| __| __| __  
Groups|  __| __| __  
  
Limited to 3 groups per organization|  __  
  
Unlimited groups  
Granular resource permissions|  __| __| __| __  
Granular PII access controls|  __| __| __| __  
  
## Member management

All RudderStack plans include [member management](<https://www.rudderstack.com/docs/access-management/member-management/>) capabilities with different limits.

### Member limits

Plan| Member limit  
---|---  
Free| 10 members per organization  
Starter| 10 members per organization  
Growth| Unlimited  
Enterprise| Unlimited  
  
### Available roles

All plans include the following organization roles:

Role| Access  
---|---  
Admin| Full organization access.  
Member| Effective set of permissions within a workspace, computed by aggregating:  
  


  * [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>) that the member is a part of
  * [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>) configured for the member

  
  
## Groups

Groups enable creation of custom roles and streamline permissions configuration for large teams.

Plan| Availability| Group limit  
---|---|---  
Free|  __| Not available  
Starter|  __| Not available  
Growth|  __| 3  
  
You can create up to 3 groups per organization  
Enterprise|  __| No limit  
  
## Baseline Workspace Policy

[Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>) allows Admins to configure the default workspace policy beyond view-only access for all members.

Plan| Availability| Notes  
---|---|---  
Free|  __| Admins**cannot** configure the Baseline Workspace Policy  
Starter|  __| Admins**cannot** configure the Baseline Workspace Policy  
Growth|  __| Admins**cannot** configure the Baseline Workspace Policy  
Enterprise|  __| Admins can configure the Baseline Workspace Policy  
  
Admins in RudderStack **Free** , **Starter** , and **Growth** plans will see a greyed out **Baseline Workspace Policy** tab with the following message:

“[Upgrade](<https://www.rudderstack.com/pricing/>) to access this feature and additional capabilities.”

## Granular resource permissions

Granular permissions let Admins control access to specific resources within your workspace.

Plan| Availability| Resource selection| Access to future resources  
---|---|---|---  
Free|  __| **Select all** and **Include all future resources** are selected by default and cannot be toggled off| Automatic inclusion  
Starter|  __| **Select all** and **Include all future resources** are selected by default and cannot be toggled off| Automatic inclusion  
Growth|  __| **Select all** and **Include all future resources** are selected by default and cannot be toggled off| Automatic inclusion  
Enterprise|  __| Admins can select specific resources and choose whether to include future resources|  Configurable  
  
Admins in RudderStack **Free** , **Starter** , and **Growth** plans will see the individual resources greyed out with only the option to select/deselect all resources, as seen in the below image. The toggle for giving access to any new resources created in the future will be enabled by default and it cannot be toggled off.

[![Granular resource permissions](/docs/images/access-management/plan-wise-features/granular-resource-permissions.webp)](</docs/images/access-management/plan-wise-features/granular-resource-permissions.webp>)

## Granular PII access controls

PII (Personally Identifiable Information) access controls let you restrict access to sensitive data features, ensuring compliance with data regulations like SOC2, GDPR, CCPA, and HIPAA.

> ![announcement](/docs/images/announcement.svg)
> 
> The ability to configure PII permissions is available in RudderStack’s [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan only.
> 
> **All** members of an organization in **non-Enterprise** plans will have all PII permissions by default.

Admins in RudderStack **Enterprise** plan will see the **PII** section with the option to configure PII permissions for specific resources, as seen in the below image.

[![Granular PII permissions](/docs/images/access-management/plan-wise-features/granular-pii-permissions-new.webp)](</docs/images/access-management/plan-wise-features/granular-pii-permissions-new.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Admins in RudderStack **Free** , **Starter** , and **Growth** plans will not see the **PII** section as [Limited PII Access](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#limiting-access-to-pii-related-features>) is available only in RudderStack’s [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plan.

## References

  * [Access Management Overview](<https://www.rudderstack.com/docs/access-management/overview/>)
  * [Member Management](<https://www.rudderstack.com/docs/access-management/member-management/>)
  * [Baseline Workspace Policy](<https://www.rudderstack.com/docs/access-management/baseline-workspace-policy/>)
  * [Group Workspace Policies](<https://www.rudderstack.com/docs/access-management/groups/>)
  * [Member Workspace Policy](<https://www.rudderstack.com/docs/access-management/members/>)
  * [RudderStack Pricing](<https://www.rudderstack.com/pricing/>)