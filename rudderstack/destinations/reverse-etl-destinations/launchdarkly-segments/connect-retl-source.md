# Connect Reverse ETL Source to LaunchDarkly Segments

Configure a Reverse ETL source with your LaunchDarkly Segments destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the LaunchDarkly Segments destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your LaunchDarkly Segments destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/setup-guide/#connection-settings>) for LaunchDarkly Segments destination and click **Continue**.


> ![info](/docs/images/info.svg)
> 
> To successfully sync the data, make sure to enter the **Access Token** , **Client Side ID** , **Audience ID** , and **Audience Name** while configuring your LaunchDarkly Segments destination.

  2. In the **Where do you want to sync data to?** section, select the **Object**.
  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to LaunchDarkly.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific LaunchDarkly fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/launchdarkly-identifier-map-fields.webp)](</docs/images/event-stream-destinations/launchdarkly-identifier-map-fields.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.

#### How do I view the synced segments in LaunchDarkly?

You can view the synced segments in LaunchDarkly in the **Segments** list with the RudderStack logo in the name:

[![](/docs/images/event-stream-destinations/view-synced-segments-launchdarkly-1.webp)](</docs/images/event-stream-destinations/view-synced-segments-launchdarkly-1.webp>)

Click the segment to view the sync details:

[![](/docs/images/event-stream-destinations/view-synced-segments-launchdarkly-2.webp)](</docs/images/event-stream-destinations/view-synced-segments-launchdarkly-2.webp>)