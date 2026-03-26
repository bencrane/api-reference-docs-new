# Event Usage Details

View your monthly event usage across Event Stream, ETL, and Reverse ETL pipelines.

* * *

  * __2 minute read

  * 


RudderStack provides a comprehensive reporting feature that lets you view the monthly event volume across your Event Stream, ETL, and Reverse ETL pipelines. You can also view your event usage across time and break it down by source.

This guide walks you through the reporting feature in detail.

## View events usage

To use the reporting feature, log in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and navigate to **Settings** > **Organization** > **Usage**.

Here, you get an overview of your organization’s event usage by product.

[![Usage tab in RudderStack dashboard](/docs/images/dashboard-guides/usage/usage-tab.webp)](</docs/images/dashboard-guides/usage/usage-tab.webp>)

### Usage and monthly event limit

In this section, you will see your current RudderStack plan and the monthly event limit.

[![RudderStack plan and monthly event limit](/docs/images/dashboard-guides/usage/plan-monthly-limit.webp)](</docs/images/dashboard-guides/usage/plan-monthly-limit.webp>)

If your plan has support for multiple workspaces, you will also see a **All workspaces** tab. Here, you can filter your monthly event usage data by workspace.

[![Filter metrics by workspace](/docs/images/dashboard-guides/usage/workspaces.webp)](</docs/images/dashboard-guides/usage/workspaces.webp>)

### Monthly event usage

This section gives you a quick overview of the event volume for the **current month** by product type (Event Stream, ETL, and Reverse ETL).

[![Monthly event usage overview](/docs/images/dashboard-guides/usage/monthly-event-usage-latest.webp)](</docs/images/dashboard-guides/usage/monthly-event-usage-latest.webp>)

You can also see the details on event volume used till date and the option to upgrade your plan (applicable for [Free and Starter](<https://rudderstack.com/pricing/>) plans).

[![Monthly event usage overview for self-serve](/docs/images/dashboard-guides/usage/monthly-event-usage-free-latest.webp)](</docs/images/dashboard-guides/usage/monthly-event-usage-free-latest.webp>)

### Usage by source type

In the **Usage overview** section, you get tabbed charts that reflect your events usage by product type (Event Stream, Reverse ETL, and ETL). You also get details on the top five sources by event volume. Note that all the remaining sources are grouped into **All other sources**.

[![Usage overview by source](/docs/images/dashboard-guides/usage/usage-overview-latest.webp)](</docs/images/dashboard-guides/usage/usage-overview-latest.webp>)

You can also filter the event usage data by source and time period (day, week, or month). Hover on the chart to see the following metrics:

  * Source name
  * Number of ingested events
  * Percentage of event volume
  * Workspace associated with the source


> ![info](/docs/images/info.svg)
> 
> You can filter data for up to 10 sources.

[![Usage overview by source type](/docs/images/dashboard-guides/usage/filter-metrics-latest.webp)](</docs/images/dashboard-guides/usage/filter-metrics-latest.webp>)

### Usage breakdown by source

To view the events usage breakdown by source for the selected time period, click the **View Breakdown** option:

[![Usage overview by source type](/docs/images/dashboard-guides/usage/filter-metrics-latest-1.webp)](</docs/images/dashboard-guides/usage/filter-metrics-latest-1.webp>)

Here, you will see a detailed event usage breakdown for all the sources in your workspace for the selected time period, including number of ingested events (not events sent to the destination).

[![Usage breakdown by source](/docs/images/dashboard-guides/usage/view-breakdown-source.webp)](</docs/images/dashboard-guides/usage/view-breakdown-source.webp>)