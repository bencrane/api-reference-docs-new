# BigQuery Stream

Send your event data from RudderStack to BigQuery via Google’s streaming API.

* * *

  * __6 minute read

  * 


[Google BigQuery](<https://cloud.google.com/bigquery>) offers a [streaming API](<https://cloud.google.com/bigquery/docs/samples/bigquery-table-insert-rows>) which lets you insert data into BigQuery in near real-time and have it ready for analysis in no time.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/bqstream>).

## Prerequisites

Before you set up BigQuery Stream as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>), make sure to obtain the required access to write to BigQuery.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends creating a service account in your [Google Cloud Console](<https://console.cloud.google.com>) with the **BigQuery Data Editor** role.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **BigQuery Stream** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **BigQuery Stream** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Project ID| Enter your BigQuery project ID.  
Dataset ID| Enter the ID of the project dataset associated with the **Project ID** above.  
Table ID| Provide the ID of the table into which you want to stream the event data.  
Insert ID| This is an **optional** field. Enter the `insertId` used by Google to deduplicate the data sent to BigQuery.  
  
See Deduplicate data for more information on this setting.  
Credentials| Enter the contents of the credentials JSON you downloaded after creating your service account.  
  
The following screenshot shows the fields associated with the Project ID, Dataset ID, and Table ID settings listed above:

[![BigQuery Stream connection settings](/docs/images/event-stream-destinations/bqstream-3.webp)](</docs/images/event-stream-destinations/bqstream-3.webp>)

## Send events to BigQuery Stream

RudderStack supports sending only [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events to BigQuery Stream.

> ![warning](/docs/images/warning.svg)
> 
> Note the following:
> 
>   * Make sure your `track` event payload format matches the table schema corresponding to **Table ID** specified in the dashboard settings.
>   * RudderStack does not support the `templateSupportSuffix` feature which creates a table schema during a streaming insert action.
> 


Suppose you want to stream the events from your web source to BigQuery and the table schema in your BigQuery dataset is as follows:

[![BigQuery table schema](/docs/images/event-stream-destinations/bqstream-5.webp)](</docs/images/event-stream-destinations/bqstream-5.webp>)

To successfully stream the events, the event tracked from your JavaScript SDK should look like the following:
    
    
    rudderanalytics.track("event", {
      productId: 10,
      productName: `Product-10`,
      count: 12
    });
    

Note that the `track` properties in the above payload match with the fields specified in your table schema. Once streamed, you can view this event in your BigQuery console by running the following SQL command :

[![BigQuery result](/docs/images/event-stream-destinations/bqstream-6.webp)](</docs/images/event-stream-destinations/bqstream-6.webp>)

## Deduplicate data

Google leverages the `insertId` to deduplicate the data sent to BigQuery. `insertId` is essentially an event property that uniquely identifies an event.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently supports only **numeric** or **string** values as `insertId`.

For more information on the deduplication process in BigQuery, refer to the [BigQuery documentation](<https://cloud.google.com/bigquery/streaming-data-into-bigquery#dataconsistency>).

### Use case

Consider the following table schema:

[![BigQuery table schema](/docs/images/event-stream-destinations/bqstream-5.webp)](</docs/images/event-stream-destinations/bqstream-5.webp>)

When sending an `Insert Product` event to BigQuery, you can use the `productId` field to uniquely identify the product. Upon setting `productId` as the `insertId`, BigQuery uses it to deduplicate the data.

## Configure `insertId` dynamically

> ![info](/docs/images/info.svg)
> 
> Use this feature if you are [dynamically configuring BigQuery Stream via the event payload](<https://www.rudderstack.com/docs/user-guides/how-to-guides/dynamic-destination-configuration/>).

To dynamically configure `insertId` via the event payload, make sure that `insertId` is the column name present in your schema (or in the `properties` object in the event payload) used to uniquely identify an event.

Consider the following schema:

[![BigQuery table schema](/docs/images/event-stream-destinations/bqstream-5.webp)](</docs/images/event-stream-destinations/bqstream-5.webp>)

Suppose you have a dynamic configuration like `{{ message.uniqueId || "productId" }}` for the above schema. There are three cases to consider here:

#### Case 1: Unique ID is sent as a value which is not a key in the event properties

Consider the following payload:
    
    
    {
      "properties": {
        "productId": 212,
        "productName": "my product",
        "count": 24
      },
      ...,
      "uniqueId": <some_value> ,
      ...
    }
    

In the above case, deduplication **is not applicable** as the event properties do not contain `<some_value>` present in the payload.

#### Case 2: Unique ID is sent as a value which is a key in the event properties

Consider the following payload:
    
    
    {
      "properties": {
        "productId": 212,
        "productName": "my product",
        "count": 24
      },
      ...,
      "uniqueId": "productId",
      ...
    }
    

In this case, deduplication **is applicable** as RudderStack sends the `productId` value (`212`) as the `insertId` to Google.

#### Case 3: Unique ID is not sent in the event payload

Consider the following payload:
    
    
    {
      "properties": {
        "productId": 212,
        "productName": "my product",
        "count": 24
      },
      ...
    }
    

In this case, deduplication **is applicable** as RudderStack sends the `productId` value (`212`) as the `insertId` to Google.

If you use the dynamic destination configuration for `insertId` by passing a random value (e.g. `1234`) in the above payload, deduplication will **not be applicable** as the `properties` object does not contain the value `1234`.

## Create a service account

To create a service account in your [Google Cloud Console](<https://console.cloud.google.com>), follow these steps:

  1. In the left sidebar, go to **APIs & Services** > **Credentials**.
  2. Then, click **CREATE CREDENTIALS** > **Service account** :

[![Service account under Create Credentials](/docs/images/event-stream-destinations/bqstream-service-account-1.webp)](</docs/images/event-stream-destinations/bqstream-service-account-1.webp>)

  3. Enter the service account details and click **CREATE AND CONTINUE**.
  4. In the **Select a role** field, search and select the **BigQuery Data Editor** role and click **CONTINUE**.

[![BigQuery User role](/docs/images/event-stream-destinations/bqstream-service-account-4.webp)](</docs/images/event-stream-destinations/bqstream-service-account-4.webp>)

  5. Click **DONE** to finish the setup.
  6. Next, you need the service account credentials JSON required for RudderStack to send the data to BigQuery. To obtain this JSON, go to your service account.

[![Service account](/docs/images/event-stream-destinations/bqstream-service-account-2.webp)](</docs/images/event-stream-destinations/bqstream-service-account-2.webp>)

  7. Then, go to **KEYS** > **ADD KEY** > **Create new key**.
  8. Select the **Key type** as **JSON** and click **CREATE**.

[![Service account type](/docs/images/event-stream-destinations/bqstream-service-account-3.webp)](</docs/images/event-stream-destinations/bqstream-service-account-3.webp>)

Your JSON key will be automatically downloaded. Copy and paste the contents of this JSON key in the **Credentials** field while configuring BigQuery Stream as a destination in RudderStack.

## Considerations

Note the following before sending your event data to the BigQuery Stream destination:

  * You must ensure that the instrumented event aligns with the BigQuery table schema. You can leverage [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to modify the event.

  * For fields defined as JSON and RECORD types in the BigQuery table, there are additional aspects to consider:

    * **JSON** : For fields defined as JSON, the element should be stringified before sending to BigQuery — you can leverage [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to do this.
    * **RECORD** : For fields defined as RECORD, the JSON object can be sent as-is. However, it should only include the fields explicitly defined within the RECORD schema.
  * During ingestion, RudderStack does not fetch or validate the schema — the payload is forwarded as received.


## Troubleshooting

See the [BigQuery documentation](<https://cloud.google.com/bigquery/docs/error-messages>) for troubleshooting the different errors you might encounter while sending your event data to BigQuery Stream.

## FAQ

#### How much time does it take for RudderStack (client) to see the new DDL changes?

RudderStack doesn’t fetch the schema. However, when the DDL of a BigQuery table is updated, it may take a few seconds for those changes to propagate in BigQuery.

During this window, clients may still encounter failures until the updated schema is fully applied and visible to the client.