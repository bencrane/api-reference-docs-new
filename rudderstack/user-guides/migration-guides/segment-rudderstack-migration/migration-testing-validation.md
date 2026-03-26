# Phase 3: Test and Validate Your Migration

Verify data flow, identify and resolve discrepancies, and monitor for post-migration anomalies.

* * *

  * __3 minute read

  * 


Thorough testing and validation are critical to successfully migrating from Segment to RudderStack. This guide covers some critical steps to verify your data flow, identify and resolve discrepancies, and monitor for any post-migration anomalies.

## Verify successful event streaming to destinations

**Use RudderStack Live Events for real-time event monitoring**

RudderStack’s [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) feature allows you to monitor your event stream in real-time, helping you verify that events are being successfully captured and forwarded to your destinations.

Use the destination live event viewer to inspect individual event payloads, check event volumes, and identify any gaps or delays in your data flow.

**Debugging and troubleshooting**

If you encounter any issues with your event streaming, RudderStack has this helpful article to help you quickly identify and resolve the problem. RudderStack provides detailed logs and error messages for each event, helping you pinpoint the source of the issue and take corrective action.

## Compare data between Segment and RudderStack

**Set up data validation workflows**

To ensure that your data is being accurately migrated from Segment to RudderStack, set up data validation workflows that compare your Segment and RudderStack data side-by-side. This can involve running SQL queries on your Segment and RudderStack warehouses to compare event counts, property values, and user traits.

**Identify and resolve data discrepancies**

If you identify any discrepancies between your Segment and RudderStack data during the validation process, investigate the root cause and take corrective action. This may involve updating your RudderStack SDK implementation, modifying your data transformation logic, or adjusting your destination configurations.

**Integrate and validate data in your cloud tools**

While data warehouse validation is crucial, double-checking your data in downstream tools like Amplitude, Braze, and Google Analytics is also essential. Spot-checking key metrics and dimensions can cause any discrepancies to surface early on. Also, make sure to double-check RudderStack documentation.

RudderStack’s native integrations often take a different approach than Segment with additional configuration and features. Some examples are:

  * **Google Analytics (GA4)** : Hybrid mode is a [RudderStack connection mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>), allowing you to send your event data to Google Analytics 4 (GA4) via the native SDK (device mode) and the Google Analytics 4 Measurement Protocol. In hybrid mode, RudderStack sends specific event data to the destination directly from your client (like UTM parameters) while routing the remaining events through the RudderStack server (like page call information). RudderStack then stitches both data sources together automatically.
  * **Braze** : RudderStack’s [Braze deduplication](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/trait-deduplication/>) feature prevents duplicate data from being sent to Braze, thereby saving data points and avoiding unnecessary billing overages. This feature is handy in Reverse ETL scenarios where a large number of rows are sent with duplicate columns. It is available in both cloud and device mode for Event Stream and for Reverse ETL pipelines.


## Monitor for post-migration anomalies

**Define key metrics and thresholds**

Once you have fully migrated to RudderStack, define a set of key metrics and thresholds that you can use to monitor the health and quality of your data. This may include metrics such as event volume, property completeness, and user trait consistency.

**Set up alerts for data quality issues**

Use RudderStack’s alerting features to set up notifications for when your key metrics fall outside of your defined thresholds. This helps you quickly identify and respond to any data quality issues that may arise post-migration, ensuring that your data remains accurate and actionable.

Implementing a robust testing and validation process and monitoring your data quality post-migration can ensure a smooth and successful transition from Segment to RudderStack.