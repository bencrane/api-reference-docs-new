# Gainsight PX Web Device Mode Integration

Send events to Gainsight PX using RudderStack web device mode.

* * *

  * __2 minute read

  * 


After you have successfully [instrumented](<https://www.rudderstack.com/docs/destinations/streaming-destinations/gainsight-px/setup-guide/>) Gainsight PX as a destination in RudderStack, follow this guide to correctly send your events to Gainsight PX in the [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Gainsight PX native SDK from the `https://web-sdk.aptrinsic.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Gainsight PX SDK successfully.

## Identify

Use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in Gainsight PX.

When you send an `identify` call, RudderStack passes that user’s information to Gainsight PX with `userId` as the Gainsight PX user ID and the user traits are mapped to the visitor metadata.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      email: "alex@example.com",
      name: "Alex Keener",
      gender: "Male",
      countryName: "USA",
      countryCode: "US",
      city: "New Orleans",
      score: 100,
      hobbyCustomField: "Painting",
      title: "Doctor",
    })
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the associated properties.

A sample `track` call is shown:
    
    
    rudderanalytics.track("User Tracked", {
      description: "Sample user tracking event",
      status: "Demo",
    })
    

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update an account in Gainsight PX.

When you send a `group` call, RudderStack sets the `groupId` as the Gainsight PX account ID and maps the group traits to the account metadata.

> ![warning](/docs/images/warning.svg)
> 
> Your `group` calls must contain the `groupId` and `traits` if you are using your Gainsight PX account data.

A sample `group` call is shown:
    
    
    rudderanalytics.group("group18", {
      name: "Sample Group",
      industry: "Online Streaming",
      numberOfEmployees: 10000,
      website: "www.example-group.com",
      cultureCustomField: "customfield01",
    })