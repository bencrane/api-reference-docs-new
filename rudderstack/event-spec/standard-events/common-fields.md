# Common Fields

Understand the common fields that define the core RudderStack event data structure.

* * *

  * __11 minute read

  * 


RudderStack defines some common fields (event type, timestamps, and more) across all API calls that make up the core event data structure.

This guide covers the common and contextual fields in detail.

## Common fields

Name| Data type| Description  
---|---|---  
`userId`  
Required, if `anonymousId` is absent.| String| Unique identification for the user in the database  
`anonymousId`  
Required, if `userId` is absent.| String| Pseudo-identifier for the user in cases where `userId` is absent. This is the same as the device ID.  
`channel`  
Required| String| Identifies the source of the event. Permitted values are `mobile`, `web`, `server` and `sources`.  
`context`  
Required| Object| Contains all additional user information. The RudderStack SDKs populate this information automatically.  
`type`  
Required| String| Captures the type of event. Values can be either `identify`, `track`, `screen`, `page`, `group`, or `alias`.  
`originalTimestamp`  
Required| Timestamp| Records the actual time (in UTC) when the event occurred. Make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  
  
For example, `2022-02-01T19:14:18.381Z`.  
`sentAt`  
Required| Timestamp| Captures the time (in UTC) when the event was sent from the client to RudderStack. Make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  
  
For example, `2022-02-01T19:14:18.381Z`.  
`event`| String| Captures the user action that you want to record.  
`integrations`| Object| You can specify the destinations for which you want to enable/disable sending events.  
`messageId`| String| Unique identification for the event.  
`properties`| Object| Passes all relevant information associated with the event.  
  
RudderStack also sets the following fields automatically, so you **do not** have to set them explicitly:

Name| Data type| Description  
---|---|---  
`receivedAt`| Timestamp| Time in UTC when RudderStack ingests the event.  
`timestamp`| Timestamp| RudderStack calculates this field (in UTC) to account for any client-side clock skew using the formula: `timestamp` = `receivedAt` \- (`sentAt` \- `originalTimestamp`).  
  
See Clock skew considerations for more information.  
`request_ip`| String| User’s IP address. RudderStack automatically collects and sets this property as a common field.  
  
See How RudderStack collects IP address for more information.  
  
## Contextual fields

Contextual fields give additional information about a particular event. The following table describes the available contextual fields.

Name| Data type| Description  
---|---|---  
`app`| Object| Gives detailed information related to your app, like `build`, `name`, `namespace` and `version`.  
`campaign`| Object| Gives detailed information about campaigns, like `name`, `source`, `medium`, `content` and `term`.  
`device`| Object| Information about the device from which you are capturing the event. It contains the device `id`, `manufacturer`, `model`, `name` and `type`.  
`ip`| String| User’s IP address.  
  
See How RudderStack collects IP address for more information.  
`library`| Object| Details about the RudderStack SDK you are using, like `name` and `version`.  
`locale`| String| Captures the language of the device.  
`network`| Object| Contains information about the reachability of the device. Also, it gives you the status of the device’s `bluetooth`, `wifi`, `cellular` network and `carrier` name.  
`os`| Object| Captures the operating system details of the device you are tracking.  
  
**Note** : While the JavaScript SDK does not populate this information automatically, you can get it using the [`uaChTrackLevel`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#uachtracklevel>) `load` API option.  
`screen`| Object| Gives you the screen dimensions of the device, i.e. `height`, `width` and the `density`.  
`timezone`| String| Captures the timezone of the user you are tracking.  
`traits`| Object| Captures any additional relevant information about the user. RudderStack fills in the `anonymousId` for you. You can also associate the [traits](</docs/event-spec/standard-events/identify/#identify-traits>) from the previously-made `identify` call from the SDK.  
`userAgent`| String| The user agent of the device that you are tracking.  
  
### Automatically collected contextual fields

The following table describes contextual fields that are automatically collected and populated by the RudderStack SDKs:

Field| JavaScript| Android (Kotlin)| iOS (Swift)| Android (Java)| iOS  
(Obj-C)  
---|---|---|---|---|---  
`app.name`  
Application name| -| Yes| Yes| Yes| Yes  
`app.version`  
Application version| -| Yes| Yes| Yes| Yes  
`app.build`  
Application build| -| Yes| Yes| Yes| Yes  
`campaign.name`  
Campaign name| Yes| -| -| -| -  
`campaign.source`  
Campaign source| Yes| -| -| -| -  
`campaign.medium`  
Campaign medium| Yes| -| -| -| -  
`campaign.term`  
Campaign term| Yes| -| -| -| -  
`campaign.content`  
Campaign content| Yes| -| -| -| -  
`device.type`  
Device type| -| Yes| Yes| Yes| Yes  
`device.id`  
Device ID| -| Yes| Yes| Yes| Yes  
`device.advertisingId`  
Advertising ID| -| No**| No**| Yes| Yes  
`device.adTrackingEnabled`  
Whether ad tracking is enabled on the device| -| -| No**| -| Yes  
`device.manufacturer`  
Device manufacturer| -| Yes| Yes| Yes| Yes  
`device.model`  
Device model| -| Yes| Yes| Yes| Yes  
`device.name`  
Device name| -| Yes| Yes| Yes| Yes  
`library.name`  
Library name| Yes| Yes| Yes| Yes| Yes  
`library.version`  
Library version| Yes| Yes| Yes| Yes| Yes  
`locale`  
User’s locale string| Yes| Yes| Yes| Yes| Yes  
`network.bluetooth`  
Bluetooth information| -| Yes*| No**| Yes*| -  
`network.carrier`  
Network carrier information| -| Yes| -| Yes| Yes  
`network.cellular`  
Network’s cellular information| -| Yes| -| Yes| Yes  
`network.wifi`  
Network’s WiFi information| -| Yes| Yes| Yes| Yes  
`os.name`  
Operating System name| -  
  
Use the [`uaChTrackLevel`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#uachtracklevel>) `load` API option| Yes| Yes| Yes| Yes  
`os.version`  
Operating System version| -  
  
Use the [`uaChTrackLevel`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#uachtracklevel>) `load` API option| Yes| Yes| Yes| Yes  
`page.path`  
Path of the current page in the browser| Yes| -| -| -| -  
`page.initial_referrer`  
Initial referrer of the current page| Yes| -| -| -| -  
`page.initial_referring_domain`  
Initial referring domain of the current page| Yes| -| -| -| -  
`page.referrer`  
Referrer of the current page| Yes| -| -| -| -  
`page.referring_domain`  
Referring domain of the current page| Yes| -| -| -| -  
`page.search`  
Search of the current page| Yes| -| -| -| -  
`page.title`  
Page title| Yes| -| -| -| -  
`page.url`  
Canonical URL of the page (if present)| Yes| -| -| -| -  
`page.tab_url`  
URL of the current page| Yes| -| -| -| -  
`screen.density`  
Screen density of the device| Yes| Yes| Yes| Yes| Yes  
`screen.height`  
Screen height of the device| Yes| Yes| Yes| Yes| Yes  
`screen.width`  
Screen width of the device| Yes| Yes| Yes| Yes| Yes  
`screen.innerWidth`  
Screen inner width of the device| Yes| -| -| -| -  
`screen.innerHeight`  
Screen inner height of the device| Yes| -| -| -| -  
`traits`  
User traits| -| Yes| Yes| Yes| Yes  
`userAgent`  
User agent information about the device making the request| Yes| No**| No**| Yes| -  
`timezone`  
User’s timezone| Yes| Yes| Yes| Yes| Yes  
  
Note that:

  * For Android (Kotlin) and iOS (Swift) SDKs, you can still collect the fields marked as **No**** by adding [Custom Plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/use-cases/>) maintained by RudderStack in the sample applications of the [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/tree/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins>) and [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/tree/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins>) SDKs on GitHub.
  * For Android (Kotlin) SDK and Android (Java) SDK v1.6.0 and above, the Bluetooth status is collected in the `network.bluetooth` field **only if** the Bluetooth permission is present in the app.
  * For iOS (Obj-C) SDK v1.6.3 and above, the Bluetooth status is **not collected** in the `network.bluetooth` field as it is a runtime permission.


### Sample payload with contextual fields

The following sample payload highlights the usage of the common and contextual fields in web and mobile modes:
    
    
    {
      "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8fab",
      "channel": "web",
      "context": {
        "campaign": {
          "name": "sales campaign",
          "source": "google",
          "medium": "medium",
          "term": "event data",
          "content": "Make sense of the modern data stack"
        },
        "ip": "192.0.2.0",
        "library": {
          "name": "RudderLabs JavaScript SDK",
          "version": "2.9.1"
        },
        "locale": "en-US",
        "page": {
          "path": "/best-seller/1",
          "initial_referrer": "https://www.google.com/search",
          "initial_referring_domain": "google.com",
          "referrer": "https://www.google.com/search?q=estore+bestseller",
          "referring_domain": "google.com",
          "search": "estore bestseller",
          "title": "The best sellers offered by EStore",
          "url": "https://www.estore.com/best-seller/1"
        },
        "screen": { 
          "density": 420, 
          "height": 1794, 
          "width": 1080, 
          "innerHeight": 200, 
          "innerWidth": 100 
          },
        "userAgent": "Dalvik/2.1.0 (Linux; U; Android 9; Android SDK built for x86 Build/PSR1.180720.075)"
      },
      "event": "Product Reviewed",
      "integrations": { 
        "All": true 
        },
      "messageId": "1578564113557-af022c68-429e-4af4-b99b-2b9174056383",
      "properties": {
        "review_id": "review_id_1",
        "product_id": "product_id_1",
        "rating": 5.0,
        "review_body": "It's the greatest!"
      },
      "originalTimestamp": "2020-01-09T10:01:53.558Z",
      "type": "track",
      "sentAt": "2020-01-09T10:02:03.257Z"
    }
    
    
    
    {
      "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8fab",
      "channel": "mobile",
      "context": {
        "app": {
          "name": "RudderAndroidClient",
          "version": "1.0",
          "build": "1"
        },
        "device": {
          "type": "android",
          "id": "78c53c15-32a1-4b65-adac-bec2d7bb8fab",
          "advertisingId":"435o4GRlm",
          "manufacturer": "Google",
          "model": "Android SDK built for x86",
          "name": "generic_x86",
        },
        "ip": "192.0.2.0",
        "library": {
          "name": "com.rudderstack.android.sdk.core",
          "version": "0.1.4"
        },
        "locale": "en-US",
        "network": {
          "bluetooth": false,
          "carrier": "Android",
          "cellular": true,
          "wifi": true
        },
        "os": { 
          "name": "Android", 
          "version": "9" 
          },
        "screen": { 
          "density": 420, 
          "height": 1794, 
          "width": 1080 
          },
         "traits": { 
          "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8fab" 
          },
        "timezone": "Asia/Mumbai",
        "userAgent": "Dalvik/2.1.0 (Linux; U; Android 9; Android SDK built for x86 Build/PSR1.180720.075)"
      },
      "event": "Product Reviewed",
      "integrations": { 
        "All": true 
        },
      "messageId": "1578564113557-af022c68-429e-4af4-b99b-2b9174056383",
      "properties": {
        "review_id": "review_id_1",
        "product_id": "product_id_1",
        "rating": 5.0,
        "review_body": "It's the greatest!"
      },
      "originalTimestamp": "2020-01-09T10:01:53.558Z",
      "type": "track",
      "sentAt": "2020-01-09T10:02:03.257Z"
    }
    
    
    
    {
      "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8fab",
      "channel": "mobile",
      "context": {
        "app": {
          "name": "RudderSampleAppObjC",
          "version": "1.0",
          "build": "1"
        },
        "device": {
          "type": "iOS",
          "id": "78c53c15-32a1-4b65-adac-bec2d7bb8fab",
          "advertisingId":"435o4GRlm",
          "adTrackingEnabled": false,
          "manufacturer": "Apple",
          "model": "iPhone",
          "name": "iPhone 12",
        },
        "ip": "192.0.2.0",
        "library": {
          "name": "rudder-ios-library",
          "version": "1.5.0"
        },
        "locale": "en-US",
        "network": {
          "carrier": "unavailable",
          "cellular": false,
          "wifi": true
        },
        "os": { 
          "name": "iOS", 
          "version": "15.2" 
          },
        "screen": { 
          "height": 1794, 
          "width": 1080 
          },
         "traits": { 
          "anonymousId": "78c53c15-32a1-4b65-adac-bec2d7bb8fab" 
          },
        "timezone": "Asia/Mumbai"
      },
      "event": "Product Reviewed",
      "integrations": { 
        "All": true 
        },
      "messageId": "1643629072-8ce81faf-7489-4508-b21b-659e81510991",
      "properties": {
        "review_id": "review_id_1",
        "product_id": "product_id_1",
        "rating": 5.0,
        "review_body": "It's the greatest!"
      },
      "originalTimestamp": "2020-01-09T10:01:53.558Z",
      "type": "track",
      "sentAt": "2020-01-09T10:02:03.257Z"
    }
    

## How RudderStack collects IP address

RudderStack automatically collects the user’s IP address in the `request_ip` property as a common field.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `request_ip` field is available in the final event received at the destination and in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>).
>   * RudderStack leverages the automatically collected IP address for [Geolocation Enrichment](<https://www.rudderstack.com/docs/data-governance/geolocation-service/>) if enabled, allowing RudderStack to look up geographic information based on that IP address.
> 


### Set custom IP address

You can set a custom IP address or anonymize it in your events using two methods:

#### Method 1: Include IP in the `context` object (Recommended)

Set the IP address in the `context.ip` field:
    
    
    rudderanalytics.identify(
      "1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        firstName: "Alex",
        lastName: "Keener",
        email: "alex@example.com",
        phone: "+1-202-555-0146"
      }, {
        context: {
          ip: "192.0.2.0"
        }
      },
      () => {
        console.log("Identify event successfully submitted to the RudderStack SDK.");
      }
    );
    

#### Method 2: Include IP in the `request_ip` field

Set the IP address directly in the `request_ip` field in the event payload:
    
    
    {
      "type": "track",
      "event": "Page Viewed",
      "userId": "1hKOmRA4GRlm",
      "properties": {
        "page": "/home"
      },
      "request_ip": "192.168.1.100"  // Custom IP address
    }
    

#### How RudderStack prioritizes IP address collection

RudderStack prioritizes the below fields when determining which IP address to use:

  1. `context.ip` (if provided)
  2. `request_ip` (if provided)
  3. **Fallback** : Automatically detected IP from the request


> ![info](/docs/images/info.svg)
> 
> RudderStack only adds the automatically captured IP address if no `request_ip` field exists, even if `context.ip` is already present in the event.

## Clock skew considerations

RudderStack considers the time at its end to be absolute and assumes any differences are on the client-side. Thus, the client clock skew is relative.

Note that all the below timestamps are in UTC.

Field| Description  
---|---  
`originalTimestamp`| Time, client-side, when the event occurred at the source.  
`sentAt`| Time, client-side, when the event was sent from the client to RudderStack.  
`receivedAt`| Time when the event is received(ingested) by the RudderStack server.  
`timestamp`| Calculated by RudderStack to account for the client clock skew, if the user does not explicitly specify it in the payload.  
`uuid_ts`| Time when RudderStack loads the data into the warehouse.  
  
Note that:  
  


  * RudderStack recommends using this timestamp when processing data incrementally within a data warehouse.
  * In case of the [Google BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>) destination, RudderStack also adds the `loaded_at` field along with `uuid_ts` in the final event payload for [Segment compatibility](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/>).

  
  
> ![warning](/docs/images/warning.svg)
> 
> **Important considerations for using timestamps in analysis**
> 
>   * RudderStack does not recommend using `originalTimestamp` and `sentAt` for analysis as they both reflect client-side clock skew. Likewise, `receivedAt` does not guarantee preservation of the chronological order of events, and should not be used for analysis where chronological order is needed.
>   * When importing historical events, use the `timestamp` field to preserve the chronological order.
> 


### SDK sources

If you do not specify the `timestamp` field in the payload for [SDK sources](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>), RudderStack calculates it based on the `originalTimestamp` and `sentAt` to account for the client clock skew.

`sentAt` > `originalTimestamp` is **always true**. However, `timestamp` can be greater or less than the `originalTimestamp`:

**Case 1** : `originalTimestamp` < `receivedAt`

When the client-side time is less than the time registered by RudderStack:

originalTimestamp| sentAt| receivedAt| timestamp = receivedAt - (sentAt - originalTimestamp)  
---|---|---|---  
2020-04-26 07:00:43.400| 2020-04-26 07:00:45.124| 2020-04-26 07:00:45.558| 2020-04-26 07:00:43.834  
  
In this case, `timestamp` will be **greater** than `originalTimestamp`.

**Case 2** : `originalTimestamp` > `receivedAt`

When the client-side time is greater than the time registered by RudderStack:

originalTimestamp| sentAt| receivedAt| timestamp = receivedAt - (sentAt - originalTimestamp)  
---|---|---|---  
2020-04-26 07:00:45.558| 2020-04-26 07:00:46.124| 2020-04-26 07:00:43.400| 2020-04-26 07:00:42.834  
  
In this case, `timestamp` will be **less** than `originalTimestamp`.

### HTTP/Webhook-based sources

RudderStack does not consider any clock skew for HTTP/Webhook-based sources and uses the `timestamp` passed in the `timestamp` payload field.

**Case 1** : When the client-side time is less than the time registered by RudderStack:

originalTimestamp| sentAt| receivedAt| timestamp = receivedAt - (sentAt - originalTimestamp)| timestamp (payload field)  
---|---|---|---|---  
NA| NA| 2020-04-26 07:00:49.400| NA| 2020-04-26 07:00:46.400  
  
**Case 2** : When the client-side time is greater than the time registered by RudderStack:

originalTimestamp| sentAt| receivedAt| timestamp = receivedAt - (sentAt - originalTimestamp)| timestamp (payload field)  
---|---|---|---|---  
NA| NA| 2020-04-26 07:00:43.400| NA| 2020-04-26 07:00:47.400  
  
In the above cases, `timestamp` is the same as specified in the payload. RudderStack sets the `originalTimestamp` as the `currentTime`. You can add a [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to correct the clock skew.

**Case 3** : If none of the `originalTimestamp`, `sentAt`, `receivedAt`, and `timestamp` fields are passed in the payload:

originalTimestamp| sentAt| receivedAt| timestamp = receivedAt - (sentAt - originalTimestamp)| timestamp (payload field)  
---|---|---|---|---  
Set as current time| Set as current time| current time| current time| NA  
  
RudderStack sets the `originalTimestamp` and `sentAt` fields to the current time and calculates `timestamp` (same as `receivedAt`/current time).

### Destinations

RudderStack gives priority to the `timestamp` field over `originalTimestamp`. Refer to the [destination documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.

## Timestamp mapping for Reverse ETL sources

When you map your warehouse columns to destination fields using [JSON mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>), RudderStack prefers the timestamp to be set in the following event traits/properties (in the exact preference order):

Event type| JSON key for timestamp  
---|---  
`track`| `properties.timestamp`  
`identify`| 

  1. `context.timestamp`
  2. `context.traits.timestamp`
  3. `traits.timestamp`
  4. `timestamp`
  5. `originalTimestamp`

  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If the timestamp is not present in any of the outermost timestamp fields, RudderStack takes the timestamp value from the [`originalTimestamp`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#clock-skew-considerations>) field (at the outermost level in the event payload).
>   * RudderStack generates the root level `timestamp` field and it changes every time a full sync is triggered.
>