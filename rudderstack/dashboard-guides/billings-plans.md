# Manage RudderStack Plan and Billing

Manage your RudderStack plan and billing information in the dashboard.

Available Plans

  * free
  * starter


* * *

  *  __4 minute read

  * 


RudderStack provides an intuitive UI to manage your [plan](<https://www.rudderstack.com/pricing/>). With the **Billing & plans** feature, you can:

  * Update your RudderStack plan seamlessly.
  * Manage your payment and billing contact information.
  * View past invoices.
  * Get complete visibility into your purchases, including the pro-rated amount billed for the current month.


## Access billing and plan

Go to **Settings** > **Organization** > **Billing & plans** to access the current billing and payment information and manage your RudderStack plan.

> ![warning](/docs/images/warning.svg)
> 
> **Why can’t I see the Billing & plans tab in my dashboard?**
> 
> The **Billing & plans** feature is available only in the [Free and Starter plans](<https://rudderstack.com/pricing/>).
> 
> If you are on one of these plans and still cannot see the **Billing & plans** tab, contact [RudderStack support](<mailto:support@rudderstack.com>).

[![Billing and plans tab](/docs/images/dashboard-guides/billings-plans/billings-plans.webp)](</docs/images/dashboard-guides/billings-plans/billings-plans.webp>)

## Current plan

In this view, you get a summary of the currently active RudderStack plan and the monthly event usage. You can also manage your payment and billing contact information by clicking the edit button next to each section.

[![Current plan](/docs/images/dashboard-guides/billings-plans/current-plan.webp)](</docs/images/dashboard-guides/billings-plans/current-plan.webp>)

### View past invoices

Click the **Invoices** button to view past invoices.

[![Invoices button](/docs/images/dashboard-guides/billings-plans/invoices.webp)](</docs/images/dashboard-guides/billings-plans/invoices.webp>)

### Monthly event usage

The **Monthly event usage** section shows the number of events consumed in the current month.

### Add payment information

This option lets you add, remove, and set a default payment method.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You cannot remove the default payment method.
>   * By providing your card information, you allow RudderStack to charge your card for future payments in accordance with RudderStack’s terms.
> 


[![Payment method](/docs/images/dashboard-guides/billings-plans/payment-method.webp)](</docs/images/dashboard-guides/billings-plans/payment-method.webp>)

### Billing email

This option lets you update the email address where you will receive all the RudderStack plan invoices.

## Manage RudderStack plan

In this view, you can update your current RudderStack plan. You can also compare it with other plans to decide whether your plan suits your event volume and feature requirements.

To update your RudderStack plan, choose the relevant plan from the dropdown and select **Update plan**. Alternatively, you can click the **Manage plan** button on the right.

[![Manage plan](/docs/images/dashboard-guides/billings-plans/manage-plan.webp)](</docs/images/dashboard-guides/billings-plans/manage-plan.webp>)

You can make changes to your RudderStack plan in this view. You also get the option to set the payment method used for the transaction.

[![Update plan](/docs/images/dashboard-guides/billings-plans/update-plan.webp)](</docs/images/dashboard-guides/billings-plans/update-plan.webp>)

Click **Confirm** to confirm your choice.

> ![warning](/docs/images/warning.svg)
> 
> The updated RudderStack plan will not come into effect if you do not confirm your choice.

### Purchase summary

RudderStack also gives you a clear purchase summary of the amount it will charge you from the next billing cycle and the pro-rated amount for the current month.

> ![info](/docs/images/info.svg)
> 
> RudderStack’s billing cycle resets on the 1st day of every month.

[![Purchase summary](/docs/images/dashboard-guides/billings-plans/purchase-summary.webp)](</docs/images/dashboard-guides/billings-plans/purchase-summary.webp>)

### Cancel plan

Click **Cancel plan** to cancel your current RudderStack plan.

[![Cancel plan](/docs/images/dashboard-guides/billings-plans/cancel-plan.webp)](</docs/images/dashboard-guides/billings-plans/cancel-plan.webp>)

If you choose to continue and cancel your plan, note that:

  * Your plan will be cancelled and changed to the [RudderStack Free plan](<https://www.rudderstack.com/pricing/>) plan with a monthly limit of 250K events.
  * You can still use your current plan until the end of your billing period, that is, 1st day of the following month.


For more information on RudderStack plans and billing-related queries, contact [RudderStack support](<mailto:support@rudderstack.com>).

## Event limit overages

RudderStack charges overage fees when your organization reaches the event limit for your current plan.

A summary of event overage fees is as follows:

  * For the [Free plan](<https://www.rudderstack.com/pricing/>), data processing stops on the second consecutive overage.
  * For the [Starter plans](<https://www.rudderstack.com/pricing/>), the overage fee is calculated as the difference between the next tier’s pricing and the current tier’s pricing. See the below table for the overage fee calculation:

Plan| Monthly price  
(per month)| Overage charges  
(per month)  
---|---|---  
Free| $0| -  
1M Starter| $220| $440  
3M Starter| $660| $330  
7M Starter| $990| $370  
10M Starter| $1,360| $270  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Overage fees apply at the start of the next billing cycle.
>   * In case of Starter plans, there will be escalated warnings after two months of consecutive overages.
> 


### When data processing stops

RudderStack stops processing data when you exceed your event limit for consecutive months — **this threshold varies by plan** :

Plan| When data processing stops  
---|---  
Free| Second consecutive overage  
1M, 3M, 7M and 10M Starter| Fourth consecutive overage  
  
> ![warning](/docs/images/warning.svg)
> 
> To avoid overage fees and service disruption, upgrade your plan before reaching the event limit or contact the Sales team to discuss your requirements.