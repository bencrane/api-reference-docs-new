# Sync Data from Reverse ETL Sources

Sync data as Identify or Track events from Reverse ETL sources to your destinations.

* * *

  * __2 minute read

  * 


RudderStack supports syncing data from the [Reverse ETL sources](<https://www.rudderstack.com/docs/sources/reverse-etl/#supported-reverse-etl-sources>) to the downstream destinations as [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) and [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) calls.

> ![warning](/docs/images/warning.svg)
> 
> You can send your data as `track` events while mapping your warehouse columns to the destination fields **only** using JSON mapping. RudderStack does not support [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) for this functionality.

## Key features

Some key features of syncing events from Reverse ETL sources are listed below:

  * **Ensure the reliability of your events** : Sometimes, your critical events (like purchases) may get blocked by things outside your control, like ad blockers. In such cases, you can send all the user activity residing in your warehouse or database to the downstream systems as a guaranteed source of truth.
  * **Simulate historical tracking of events** : You can replay the historical data from other data sources to your sales, support, and marketing systems to maintain business continuity.
  * **Fix bad data and replay it** : There is a possibility that your destination ends up with some bad data due to a bug in the tracking code or any other reason. In such cases, you can clear the bad data and replay a clean version by syncing the events.
  * **Test your transformations and integrations** : You can use a sample dataset to test an event stream for a new version of your transformation or a new integration using the `track` call.


## Use cases for sending `track` events

Some examples where you can use the `track` call to send events from your warehouse into the downstream destinations are:

  * Sending event data to engagement platforms such as Braze, Iterable, Customer.io, or Salesforce Marketing Cloud to trigger behavior or populate user actions.
  * Sending event data to the downstream systems that are configured to handle `track` calls, like Apache Kafka or Amazon Kinesis.
  * Replaying the fact table that might be the source of truth for user behavior to the downstream tools such as Statsig, Optimizely, etc.


## Steps for syncing data

To sync your data from a Reverse ETL source to a downstream destination, follow these steps:

  1. Set up your [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>). You can ingest the data from a warehouse table, [model](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>), or an [audience](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>).
  2. Connect the source to the desired destinations.
  3. Specify the data mappings and sync schedule based on how you want to ingest the data from the source.