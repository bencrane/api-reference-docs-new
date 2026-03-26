# Flush API in Mobile SDKs

Manually flush your stored events by leveraging the flush API in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide walks you through the `flush` API and the different event flushing policies supported by the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a `flush` API that lets you manually flush any stored events irrespective of the configured flush policies.

You can trigger a `flush` API call as follows:
    
    
    analytics.flush()
    

The corresponding Java snippet is shown below:
    
    
    analytics.flush();
    
    
    
    analytics.flush()
    

The corresponding Objective-C snippet is shown below:
    
    
    [analytics flush];
    

> ![warning](/docs/images/warning.svg)
> 
> If you have added a mobile device mode integration plugin, then a `flush` API call will also trigger the integration’s `flush` API, if it is supported.

## Flush policies

RudderStack supports three configurable flush policies. By default, all three policies are enabled.

### Count flush policy

The `CountFlushPolicy` triggers a `flush` call when a predefined threshold for the event count is reached.

Flush policies| Data type| Notes  
---|---|---  
`flushAt`| Integer| The value of this parameter must be within the range of `1` to `100` \- the default value is `30`.  
  
### Frequency flush policy

The `FrequencyFlushPolicy` automatically triggers a flush at the specified intervals.

Flush policies| Data type| Description  
---|---|---  
`flushIntervalInMillis`| Long| Minimum allowed value is`1 millisecond` \- the default value is `10 seconds`.  
  
### Startup flush policy

The `StartupFlushPolicy` automatically triggers a one-time `flush` API call after the Android (Kotlin) SDK is initialized.

## Set a flush policy

You can select and set a flush policy depending on your use case.

> ![warning](/docs/images/warning.svg)
> 
> Selecting a flush policy from the provided list overrides the default flush policy.

The following examples highlight how you can set the `FrequencyFlushPolicy` in Android (Kotlin) and iOS (Swift) SDKs:

### Android (Kotlin)

  1. Import the flush policy as shown:


    
    
    import com.rudderstack.sdk.kotlin.core.internals.policies.FrequencyFlushPolicy
    

  2. Add `FrequencyFlushPolicy` during the SDK initialization, as shown below. Replace the `WRITE_KEY` and `DATA_PLANE_URL` parameters in the below snippet with the Android (Kotlin) source write key and your data plane URL.


    
    
    analytics = Analytics(
        configuration = Configuration(
            writeKey = BuildConfig.WRITE_KEY,
            application = application,
            dataPlaneUrl = BuildConfig.DATA_PLANE_URL,
            flushPolicies = listOf(
                FrequencyFlushPolicy()
            )
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    FrequencyFlushPolicy frequencyFlushPolicy = new FrequencyFlushPolicy();
    ArrayList<FlushPolicy> listOfFlushPolicies = new ArrayList<>();
    listOfFlushPolicies.add(frequencyFlushPolicy);
    
    Configuration configuration = new ConfigurationBuilder(this, "WRITE_KEY", "DATA_PLANE_URL")
            .setFlushPolicies(listOfFlushPolicies)
            .build();
    
    analytics = new JavaAnalytics(configuration);
    

### iOS (Swift)

  1. Import the flush policy as shown:


    
    
    import RudderStackAnalytics
    

  2. Add `FrequencyFlushPolicy` during the SDK initialization. Replace the `WRITE_KEY` and `DATA_PLANE_URL` parameters in the below snippet with the iOS (Swift) source write key and your data plane URL.


    
    
    self.analytics = Analytics(configuration: Configuration(
        writeKey: "<WRITE_KEY>",
        dataPlaneUrl: "<DATA_PLANE_URL>",
        flushPolicies: [
            FrequencyFlushPolicy()
        ]
    ))
    

  1. Import the flush policy as shown:


    
    
    @import RudderStackAnalytics;
    

  2. Add `FrequencyFlushPolicy` during the SDK initialization. Replace the `WRITE_KEY` and `DATA_PLANE_URL` parameters in the below snippet with the iOS (Swift) source write key and your data plane URL.


    
    
    RSSConfigurationBuilder *builder = [[RSSConfigurationBuilder alloc]
        initWithWriteKey:@"<WRITE_KEY>"
           dataPlaneUrl:@"<DATA_PLANE_URL>"];
    
    [builder setFlushPolicies:@[
        [RSSFrequencyFlushPolicy new]
    ]];
    
    RSSAnalytics *analytics = [[RSSAnalytics alloc]
        initWithConfiguration:[builder build]];