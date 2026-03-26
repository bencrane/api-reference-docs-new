# Data Mapping with JSON

Specify data mappings for Reverse ETL connections via JSON.

* * *

  * __3 minute read

  * 


RudderStack provides the following options to map your warehouse columns to specific destination fields while importing the data:

  * Map with JSON
  * [Map with Visualizer](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>)


This guide lists the JSON mapping settings required to sync data from your warehouse sources to the specified destinations.

## Mapping configuration

  * **Sync mode** : Select the [sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) from **Upsert** or **Mirror** that RudderStack uses to sync your data.
  * **Use cursor column** : This setting is visible only if you have set the **Sync mode** setting to **Upsert**. When toggled on, it lets you specify a cursor column for managing incremental syncs. See [Cursor Column Support](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/cursor-column-support/>) guide for more information on this setting.
  * **Event Type** : Select from the `identify` or `track` event type depending on how you want to send the event data to the downstream destinations.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support `track` event type for **Mirror** mode.

If you select `track`, you also need to provide:

  * **Event Name** : Enter the event name which should be sent for all events to the downstream destinations:

[![Schema tab options in RudderStack](/docs/images/warehouse-actions-sources/event-name-track.webp)](</docs/images/warehouse-actions-sources/event-name-track.webp>)

You can also send different event names by enabling the **lookup event name by column** setting and specifying the column name which should be used to set the event name in the **Event Name** field:

[![Schema tab options in RudderStack](/docs/images/warehouse-actions-sources/event-name-table-track.webp)](</docs/images/warehouse-actions-sources/event-name-table-track.webp>)

> ![info](/docs/images/info.svg)
> 
> See [Syncing Events](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/syncing-events/>) for more information on sending event data as `identify` or `track` events.

  * **Choose user identifier** : Choose **at least** one user identifier from `user_id` and `anonymous_id` from the dropdown.


You can preview the data snippet which RudderStack sends to the destination. All the columns from the table are selected by default. However, you can choose to retain specific columns by searching and selecting or deselecting them.

You can also search the columns by a keyword and edit the **JSON Trait Key** column. RudderStack automatically generates the resulting preview on the right:

[![JSON data preview](/docs/images/retl-sources/json-data-preview.webp)](</docs/images/retl-sources/json-data-preview.webp>)

The resulting JSON payload carries the `user_id` and `anonymous_id` from the columns selected in the **Choose user identifier** section. Moreover, the traits are used from the columns selected in the **Column** section.

### Add Constant

You can also use the **Add Constant** option to add a constant key-value pair which is always sent in the JSON payload:

[![Add constant](/docs/images/retl-sources/add-constant.webp)](</docs/images/retl-sources/add-constant.webp>)

The new constant will appear in the table and also in the JSON preview inside the traits, as shown:

[![Updating table selection](/docs/images/warehouse-actions-sources/add-constant-in-json.webp)](</docs/images/warehouse-actions-sources/add-constant-in-json.webp>)

You can also use the dot notation to define a constant, as shown:

[![Updating table selection](/docs/images/warehouse-actions-sources/dot-notation-constant.webp)](</docs/images/warehouse-actions-sources/dot-notation-constant.webp>)

Once you have finalized the configuration, click **Save**.

## Update mapping configuration

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * You can update your mapping configuration irrespective of whether the connection is turned on or off.
>   * While updating the mapping configuration, you **cannot** change the **Sync mode** , **Event type** , and **User identifier** fields. You will have to delete the destination and connect a new destination from scratch to do so.
> 


  1. Go to the **Schema** tab of your Reverse ETL connection page.
  2. Update the mappings as required by selecting/deselecting the required fields.
  3. Click **Save** to update the configuration.

[![Update JSON mappings](/docs/images/retl-sources/update-json-mapping.webp)](</docs/images/retl-sources/update-json-mapping.webp>)