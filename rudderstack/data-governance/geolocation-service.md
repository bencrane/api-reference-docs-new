# Geolocation Enrichment at Source

Enrich source events with geolocation data.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


With RudderStack’s geolocation enrichment feature, you can enrich your incoming source events with the following geolocation information:

  * City
  * Country
  * Region
  * Location
  * Postal code
  * Timezone


> ![warning](/docs/images/warning.svg)
> 
> This feature sends geolocation-enriched events to all the destinations connected to the source. However, the destinations may or may not accept the geolocation-enriched properties depending on the event format they support.
> 
> See FAQ for more information on the supported destinations.

## Enable geolocation enrichment at source

> ![announcement](/docs/images/announcement.svg)
> 
> If you’re hosting RudderStack on-premise, contact [RudderStack Support](<mailto:support@rudderstack.com>) to enable this feature for your account.

To enrich your source events with geolocation data, [add a source](<https://www.rudderstack.com/docs/dashboard-guides/sources/>) in your RudderStack dashboard. Then, go to the **Settings** tab and turn on the **Enable geolocation enrichment** toggle.

[![Geolocation at source](/docs/images/features/geolocation-at-source.webp)](</docs/images/features/geolocation-at-source.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Turning on the **Enable geolocation enrichment** toggle sends the enriched events to **all** the destinations connected to the source.

## How source-level geolocation enrichment works

The following workflow assumes you have turned on the **Enable geolocation enrichment** toggle in the RudderStack dashboard:

  1. RudderStack ingests the incoming source event.
  2. It picks the first non-blank value from [`ip`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#how-rudderstack-collects-ip-address:~:text=and%20type.-,ip,-String>) passed by the user in the `context` object of the event payload or [`request_ip`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#how-rudderstack-collects-ip-address:~:text=for%20more%20information.-,request_ip,-String>) (automatically collected by RudderStack).
  3. RudderStack enriches the event with the geolocation information at a hardcoded location within the `context` section (`context.geo`). A sample geolocation-enriched object is shown:


    
    
    {
      ...
      "context": {
        "geo": {
          "city": "Gurugram",
          "country": "IN",
          "ip": "223.190.82.63",
          "location": "28.459700,77.028200",
          "postal": "122001",
          "region": "Haryana",
          "timezone": "Asia/Kolkata"
        },
        "ip": "223.190.82.63"
      },
      ...
    }
    

Note the following:

  * Ideally, the `context` object should be a valid map for RudderStack to attach the geolocation enrichment information.


> ![warning](/docs/images/warning.svg)
> 
> If the object is not a valid map but of some other data type, RudderStack will **not** change its data type or format. In this case, the `context` object will remain unchanged and RudderStack will **not** add the enriched geolocation information in `context.geo`.

  * If the first non-blank value is **invalid** , RudderStack updates `context.geo` as follows:


    
    
    "context": {
      "geo": {
        "city": "",
        "country": "",
        "ip": "invalid",
        "location": "",
        "postal": "",
        "region": "",
        "timezone": ""
      }
    },
    

  * If the event payload already has a `geo` field within the `context` object, RudderStack will not perform geolocation enrichment. It will **not** override the existing `geo` field with the enriched data.


  4. RudderStack then transforms the event into the destination-specific format.

[![Geolocation enrichment process](/docs/images/features/geolocation-enrichment-process.webp)](</docs/images/features/geolocation-enrichment-process.webp>)

## License

This feature leverages the GeoLite2 data created by MaxMind, available from [<https://www.maxmind.com>](<https://www.maxmind.com>).

For more information, see [Maxmind license agreement](<https://dev.maxmind.com/geoip/geolite2-free-geolocation-data#license>).

## FAQ

#### Do all the destinations accept the geolocation-enriched source events?

The following destinations accept the geolocation-enriched source events as is:

  * [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)
  * [Object storage destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/#object-storage>)
  * [Streaming platforms](<https://www.rudderstack.com/docs/destinations/streaming-destinations/#streaming>) like Apache Kafka, Amazon Kinesis, etc.
  * [Serverless platforms](<https://www.rudderstack.com/docs/destinations/streaming-destinations/#serverless>) like AWS Lambda and Google Cloud Functions.
  * [Webhooks](<https://www.rudderstack.com/docs/destinations/webhooks/>)


The other cloud destinations may or not accept the geolocation-enriched event properties, depending on the event format they support.

#### I want to send the geolocation-enriched events to selective destinations and not all destinations connected to the source. Is this feature helpful?

This feature sends the geolocation-enriched events to **all** the destinations that are connected to the source. To send events to selective destinations, you can connect the [geolocation enrichment transformation](<https://www.rudderstack.com/docs/transformations/geolocation-enrichment/>) to those destinations instead.

  1. Go to the destination in the dashboard. Click the **Transformation** tab and click **Add a transformation** :
  2. Click **Create Transformation**.
  3. Under **New Transformation** , click **Custom transformation**.

[![Add a new transformation](/docs/images/features/custom-transformation.webp)](</docs/images/features/custom-transformation.webp>)

  4. Add the [geolocation enrichment transformation](<https://www.rudderstack.com/docs/transformations/geolocation-enrichment/>) code.
  5. Test your transformation and click **Save**.


#### What happens if `context` object is absent in the event payload?

RudderStack adds the `context` object and includes the enriched geolocation information in it.

#### What happens if I toggle off the geolocation enrichment setting?

Once you toggle off the **Enable geolocation enrichment** setting, RudderStack stops the enrichment process almost instantly, even if you have valid IPs coming in your source events.