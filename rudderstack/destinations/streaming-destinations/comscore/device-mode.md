# comScore Device Mode Integration

Send events to comScore using RudderStack device mode.

* * *

  * __4 minute read

  * 


After you have successfully [set up comScore as a destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/comscore/setup-guide/>) in RudderStack, follow this guide to correctly send your events to comScore in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

## Add device mode integration

Follow these steps to add comScore to your project depending on your integration platform:

To add comScore to your Android project:

  1. Open your `app/build.gradle` (Module: app) file and add the following under `dependencies`:


    
    
    implementation 'com.rudderstack.android.sdk:core:[1.17.0, 2.0.0)'
    implementation 'com.rudderstack.android.integration:comscore:[1.1.0,)'
    
    // It enables Comscore to collect a privacy-friendly publisher-specific device identifier, App Set ID, for estimating the number of unique users for audience research purposes.
    implementation 'com.google.android.gms:play-services-appset:16.+'
    

  2. Change the SDK initialization in your `Application` class:


    
    
    val rudderClient = RudderClient.getInstance(
                this,
                WRITE_KEY,
                RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withFactories(ComscoreIntegrationFactory.FACTORY)
                    .build()
            )
    

To add comScore to your iOS project:

  1. Add the following line to your CocoaPods `Podfile`:


    
    
    pod 'Rudder-Comscore'
    

  2. After adding the dependency, register `RudderComscoreFactory` with your SDK initialization as a `factory` or `RudderConfig`. To do so, import the `RudderComScoreFactory.h` in your `AppDelegate.m` file:


    
    
    #import "RudderComscoreFactory.h"
    

  3. Change the SDK initialization to:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [configBuilder withFactory:[RudderComscoreFactory instance]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    

## Supported events

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack supports sending only `page` events in web device mode.
>   * You can send the other events (Identify, Track, Screen, Reset) in mobile device mode.
> 


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to set the user ID and traits as persistent labels in comScore.

RudderStack maps the `identify` events to comScore’s `addPersistentLabels` API, followed by making a call to comScore’s `notifyHiddenEvent` API.

A sample `identify` call is shown:
    
    
    RudderClient.getInstance()?.identify(
                "1hKOmRA4GRlm",
                RudderTraits()
                    .putEmail("alex@example.com")
                    .put("trait_key_1", "trait_value_1")
                    .put("trait_key_2", 4567),
                null
            )
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record user actions. RudderStack also sends any associated properties as labels to comScore.

RudderStack maps the `track` events to comScore’s `notifyHiddenEvent` API.

A sample `track` call is shown:
    
    
    RudderClient.getInstance()?.track(
                "Event name",
                RudderProperty()
                    .putValue("property_track_key_1", "property_value_1")
                    .putValue("property_track_key_2", 987654)
                    .putValue("prop3", "value3")
            )
    

## Page

> ![info](/docs/images/info.svg)
> 
> RudderStack supports sending only `page` events in web device mode.

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record page views and capture any properties about the viewed page.

A sample `page` call is shown:
    
    
    rudderanalytics.page({
      category: "Category",
      name: "Sample",
    })
    

RudderStack maps the following comScore Publisher Tag parameters:

comScore ID| Description| Notes  
---|---|---  
`C1`  
Required| Tag type| Pre-populated with a constant value of `2`.  
`C2`  
Required| comScore Client ID| Set as the Publisher ID obtained from the dashboard.  
  
### Default mappings

If you do not specify any mappings in the [**Map RudderStack page properties to comScore parameters**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/comscore/setup-guide/#web-sdk-settings>) dashboard setting, RudderStack uses the following default mappings for the `page` event:

RudderStack page property| Data type| comScore parameter  
---|---|---  
`properties.url`| String| `C4`  
`name`| String| `C5`  
  
> ![info](/docs/images/info.svg)
> 
> All [other parameters](<https://direct-support.comscore.com/hc/en-us/articles/360007162413-Tag-Code-and-Tag-ID-parameters>) get auto-populated by comScore.

See the [comScore documentation](<https://direct-support.comscore.com/hc/en-us/articles/360007162413-Tag-Code-and-Tag-ID-parameters>) for more information on the Publisher Tag parameters you can send for improved classification and reporting.

### Pass consent

You can pass consent information to comScore in any of the following ways:

  * By leveraging RudderStack’s [consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) feature.
  * Via the `integrations` object


#### Via RudderStack’s consent management feature

You can pass the consent information to comScore by leveraging RudderStack’s [consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) feature. Make sure to specify the [consent settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/comscore/setup-guide/#other-settings>) in the dashboard.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack recommends initializing the JavaScript SDK [only after the consent is obtained](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#post-consent-user-tracking>).

#### Via the `integrations` object

RudderStack supports passing the consent information manually while loading the SDK, by including the `integrations` object during initialization — this object includes a `consent` field where you can pass the consent status.

A sample `integrations` object is shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: Boolean, // Default is true
        COMSCORE: {
          consent: {
            cs_ucfr: true // Consent value forwarded to comScore
          }
        },
        ...
      }
    });
    

## Screen

You can use the [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record whenever a user views their mobile screen and capture any properties about the viewed screen.

RudderStack maps the `screen` events to comScore’s `notifyViewEvent` API.

A sample `screen` call is shown:
    
    
    RudderClient.getInstance()?.screen(
                "Screen event name",
                RudderProperty()
                    .putValue("property_screen_key_1", "property_value_2")
                    .putValue("property_screen_key_2", 9876542)
            )
    

> ![info](/docs/images/info.svg)
> 
> For both `track` and `screen` events, RudderStack maps the event name with comScore’s `name` field. It sends all the other properties to comScore as is, without any modifications.

## Reset

Use the `reset` call to reset `userId` and the associated traits.

A sample `reset` call is shown:
    
    
    RudderClient.getInstance()?.reset(true)
    

## FAQ

#### Where can I find the comScore Publisher ID?

You can find the comScore Publisher ID by logging in to your comScore Direct account.

##### **Mobile**

  1. Log in to your [comScore Direct account](<https://direct.comscore.com/>).
  2. Go to the **Mobile app** tab.
  3. Click **Get Tag** and copy the C2 value.

[![comScore Publisher ID](/docs/images/event-stream-destinations/comscore-c2-value.webp)](</docs/images/event-stream-destinations/comscore-c2-value.webp>)

##### **Web**

  1. Log in to your [comScore Direct account](<https://direct.comscore.com/clients/Default.aspx>).
  2. Click **Get Tag**.

[![comScore Get Tag option](/docs/images/event-stream-destinations/get-tag-comscore.webp)](</docs/images/event-stream-destinations/get-tag-comscore.webp>)

  3. In the **Website Tag** popup, copy the value corresponding to the **C2** field.

[![comScore Publisher ID](/docs/images/event-stream-destinations/comscore-publisher-id-tag.webp)](</docs/images/event-stream-destinations/comscore-publisher-id-tag.webp>)