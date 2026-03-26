# SFMC Cloud Mode Integration

Send events to Salesforce Marketing Cloud using RudderStack cloud mode.

* * *

  * __4 minute read

  * 


After you have successfully instrumented Salesforce Marketing Cloud (SFMC) as a destination in RudderStack, follow this guide to correctly send your events in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/sfmc>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event to create or update contacts in SFMC.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not create or update contacts in SFMC if you turn on the **Do not create or update contacts** dashboard setting.

The following snippet demonstrates a sample `identify` call in RudderStack:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      title: "CEO",
      email: "alex@example.com",
      company: "Alex's Company",
      phone: "+1-202-555-0146",
      state: "Texas",
      city: "Houston",
      postalCode: "12345",
      country: "USA",
      street: "6649 N Blue Gum Street",
      state: "TX",
      createdAt: new Date().toJSON().slice(0, 10).replace(/-/g, "/")
    })
    

Note the following:

  * You must include the `userId` or `email` trait in every `identify` call. Otherwise, the event will fail.
  * SFMC does not permit colons (`:`) in its **Contact Key** field. Hence, you must remove any colons in your `userId` before sending the events.
  * Make sure to exclude nested objects in your events as SFMC cannot handle them.
  * SFMC accepts dates only in the ISO 8601 format and rejects any other format.


## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Purchased", {
      product_id: "ASIN3556",
      currency: "USD",
      revenue: 77
    })
    

### Map events to external key

You can send specific `track` events to your SFMC data extension to send events or push notifications using the [Map events to external key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sfmc/setup-guide/#track-call-settings>) dashboard setting.

Enter the `track` event name and the external key for the corresponding SFMC data extension where you want to send the data. You can add mappings for multiple `track` events by clicking the **Add More** button.

> ![info](/docs/images/info.svg)
> 
> You can find the external key for your data extension in the SFMC dashboard by going to **Contact Builder** > **Data Extensions**.

[![](/docs/images/event-stream-destinations/sfmc-track-settings-1.webp)](</docs/images/event-stream-destinations/sfmc-track-settings-1.webp>)

### Map events to primary key

A primary key is required for all `track` events going to an SFMC data extension. Use the [Map events to primary key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sfmc/setup-guide/#track-call-settings>) dashboard setting to map a `track` event to your own primary key. You can add multiple primary keys by comma-separating them.

Note that:

  * The primary key specified in the dashboard setting must match the primary key set in your SFMC data extension.
  * If you do not specify a primary key for a `track` event, RudderStack creates a primary key called `Contact Key` by default and maps it to the event’s `userId`. If `userId` is absent, RudderStack maps it to `email` instead.
  * The key specified in the dashboard settings should be present in your event properties.
  * Make sure to exclude colons (`:`) or single quotes (`'`) in the primary key field values. Otherwise, you will get a “Parameter {keys} is invalid” error.


### Map events to event definition key

Use the [Map events to event definition key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sfmc/setup-guide/#track-call-settings>) dashboard setting to map a `track` event to a specific event defintion key. RudderStack uses this setting to send the interaction events to SFMC by leveraging their [`/events`](<https://developer.salesforce.com/docs/marketing/marketing-cloud/references/mc_rest_interaction/postEvent.html>) endpoint.

You can find the event definition key in **Event Administration** section after you create and save the event in your SFMC dashboard.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include `id` and `email` in your `track` properties as these are mandatory Salesforce fields for the feature to work correctly.

### Set UUID as primary key

RudderStack lets you set an automatically-generated UUID as the primary key value for a `track` event.

To do so, enter the event in the **Event Name** field under [Track Call Settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sfmc/setup-guide/#track-call-settings>) and turn on the **UUID** setting.

To add multiple events, click the **Add more** button and toggle on the corresponding **UUID** toggle.

RudderStack automatically generates a UUID and passes it to SFMC as the value for a primary key called `Uuid` for those events.

Note that:

  * You must set `Uuid` as a primary key in your data extension before using this feature.
  * The UUID will override the primary key defined for the event in the Map events to primary key setting.

[![](/docs/images/event-stream-destinations/sfmc-track-settings-2.webp)](</docs/images/event-stream-destinations/sfmc-track-settings-2.webp>)

## Contextual field mappings

RudderStack automatically collects the [contextual properties](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) in your `identify` and `track` events and passes them to SFMC as data extension attributes. To use these fields, you must set the attributes in your SFMC data extension with the exact naming conventions as listed in the below table:

> ![info](/docs/images/info.svg)
> 
> RudderStack automatically formats the attributes/properties in camel case or snake case to title case.

RudderStack contextual field| SFMC attribute  
---|---  
`app.name`| `App Name`  
`app.version`| `App Version`  
`app.build`| `App Build`  
`campaign.name`| `UTM Campaign`  
`campaign.source`| `UTM Source`  
`campaign.medium`| `UTM Medium`  
`campaign.term`| `UTM Term`  
`campaign.content`| `UTM Content`  
`locale`| `Locale`  
`userAgent`| `User Agent`  
`ip`| `IP Address`  
`device.adTrackingEnabled`| `Ad Tracking Enabled`  
`device.manufacturer`| `Device Manufacturer`  
`device.model`| `Device-model`  
`device.name`| `Device Name`  
`device.type`| `Device Type`  
`network.bluetooth`| `Bluetooth Enabled`  
`network.carrier`| `Network Carrier`  
`network.cellular`| `Cellular Enabled`  
`network.wifi`| `Wifi Enabled`  
`screen.density`| `Screen Density`  
`screen.height`| `Screen Height`  
`screen.width`| `Screen Width`  
  
## FAQ

#### Why am I getting a “Parameter {keys} is invalid” error?

The “Parameter {keys} is invalid” error indicates the presence of `:` (colon) or `'` (single quote) in the primary key. Exclude these characters to resolve the issue.