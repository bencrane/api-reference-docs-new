# Breaking Changes in Android (Kotlin) SDK

Learn about the breaking changes introduced in the Android (Kotlin) SDK.

* * *

  * __5 minute read

  * 


This guide walks you through the breaking changes introduced in the [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) SDK.

## Overview

The Android (Kotlin) SDK is built from scratch while retaining the core functionalities of the legacy Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. .

Note the following before upgrading your SDK:

  * This SDK does not support automatic data migration from the legacy [Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>).
  * Any data persisted by the Android (Java) SDK is not carried over automatically.


## SDK initialization

The way of initializing the Android (Kotlin) SDK has changed. See the following snippets for comparison:
    
    
    RudderClient rudderClient = RudderClient.getInstance(
        this,
        WRITE_KEY,
        RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .build()
    )
    
    
    
    val analytics: Analytics = Analytics(
        configuration = Configuration(
            writeKey = BuildConfig.WRITE_KEY,
            application = application,
            dataPlaneUrl = BuildConfig.DATA_PLANE_URL,
        )
    )
    

The Java snippet for SDK initialization is shown below:
    
    
    Configuration configuration = new ConfigurationBuilder(this, "WRITE_KEY", "DATA_PLANE_URL")
            .build();
    
    JavaAnalytics analytics = new JavaAnalytics(configuration);
    

## Event API changes

  * The following fields are updated in the Android (Kotlin) SDK:

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
`RudderTraits`| `Traits`  
`RudderProperty`| `Properties`  
  
> ![warning](/docs/images/warning.svg)
> 
> `RudderMessageBuilder` and `RudderMessage` are no longer used in the Android (Kotlin) SDK.

## `RudderOption` changes

The way for creating a `RudderOption` instance has changed in the Android (Kotlin) SDK:

In this SDK, a `RudderOption` instance was created using method chaining:
    
    
    val option = RudderOption()
              .putIntegration(CustomFactory.FACTORY, false)
              .putIntegration("Amplitude", false)
              .putExternalId("brazeExternalId", "<id>")
    
    val traits = RudderTraits()
              .put("key", "value")
    
    // Identify event is used just for demonstration purposes.
    rudderClient.identify("user 1", traits, option)
    

In Android (Kotlin) SDK, `RudderOption` is instantiated using the constructor arguments instead of method chaining:
    
    
    val option = RudderOption(
        customContext = buildJsonObject {
            put("key", "value")
        },
        integrations = buildJsonObject {
            put("Amplitude", true)
            put("INTERCOM", buildJsonObject {
                put("lookup", "phone")
            })
        },
        externalIds = listOf(
            ExternalId(type = "brazeExternalId", id = "<id>"),
        )
    )
    
    val traits = buildJsonObject {
        put("key-1", "value-1")
    }
    
    // Identify event is used just for demonstration purposes.
    RudderAnalyticsUtils.analytics.identify(
        userId = "User1",
        traits = traits,
        options = option
    )
    

The corresponding Java snippet is shown below:
    
    
    Map<String, Object> customContext = new HashMap<>();
    customContext.put("key", "value");
    
    Map<String, Object> nestedIntegrations = new HashMap<>();
    nestedIntegrations.put("lookup", "phone");
    Map<String, Object> integrations = new HashMap<>();
    integrations.put("Amplitude", true);
    integrations.put("INTERCOM", nestedIntegrations);
    
    List<ExternalId> externalIds = new ArrayList<>();
    externalIds.add(new ExternalId("brazeExternalId", "<id>"));
    
    RudderOption option = new RudderOptionBuilder()
            .setIntegrations(integrations)
            .setExternalId(externalIds)
            .setCustomContext(customContext)
            .build();
            
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("name", "Alex Keener");
    traits.put("email", "alex@example.com");
    
    
    analytics.identify("User1", traits, option);
    

## Other API changes

Method| Android (Java) — **Legacy**|  Android (Kotlin)  
---|---|---  
`putIntegration`| Accepted two arguments - `type` (String) and `enabled` (Boolean).| Converted into constructor arguments and renamed to `integrations` of a single `JsonObject` type.  
`putCustomContext`| Accepted two arguments - `type` (String) and `context` (Map).| Converted into constructor arguments and renamed to `customContext` of a single `JsonObject` type.  
`putExternalId`| Accepted two arguments - `type` (String) and `id` (String).| Converted into constructor arguments and renamed to `externalIds` of type `List<ExternalId>`, where `<ExternalId>` is a data class with a `type` (String) and `id` (String).  
  
## SDK configuration changes

The following table maps the SDK configuration options available in the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. to the new Android (Kotlin) SDK:

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
`withLogLevel`| Set it directly using the `LoggerAnalytics` class.  
  
See [Logging APIs in Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/logging-apis/>) for more information.  
`withDataPlaneUrl`| `dataPlaneUrl`  
`withTrackLifecycleEvents`| `trackApplicationLifecycleEvents`  
`withNewLifecycleEvents`| `trackApplicationLifecycleEvents`  
`withTrackDeepLinks`| `trackDeepLinks`  
`withAutoSessionTracking`| `sessionConfiguration`  
`withSessionTimeoutMillis`| `sessionConfiguration`  
`withRecordScreenViews`| `trackActivities`  
`withGzip`| `gzipEnabled`  
`withCollectDeviceId`| `collectDeviceId`  
`withFactory`| Handled via plugins. For example, `analytics.add(BrazeIntegration())`  
`withControlPlaneUrl`| `controlPlaneUrl`  
`withFlushQueueSize`| `CountFlushPolicy`  
`withSleepcount`| `FrequencyFlushPolicy`  
`withEventDispatchSleepInterval`| `FrequencyFlushPolicy`  
  
## Removed features

The following features are removed in the Android (Kotlin) SDK:

  * [Database encryption](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#dbencryption>)
  * [Worker manager support](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/flushing-events-periodically/>) \- `withFlushPeriodically` configuration option is no longer available.


## Feature updates

This section covers the different feature updates introduced in the Android (Kotlin) SDK:

### Reset API

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
`reset(true)` clears `anonymousId`| `analytics.reset()` clears `anonymousId`  
`reset(false)` retains `anonymousId`| You can also use the `reset` API to perform a selective reset, that is, specify which values to reset.  
  
See the [Reset API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/reset/#selective-reset>) guide for more information.  
  
### Flush configuration

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
The following configuration options are available:  
  


  * `withSleepcount`
  * `withFlushQueueSize`
  * `withEventDispatchSleepInterval`

| The following [flush policies](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/flush-api/#flush-policies>) are available:  
  


  * `FrequencyFlushPolicy`
  * `CountFlushPolicy`
  * `StartupFlushPolicy`

  
  
### Gzip event requests

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Enabled by default| Disabled by default  
  
### Override anonymous ID

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Use the [`putAnonymousId` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#overriding-anonymous-id>).| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/SetAnonymousIdPlugin.kt>) for more information.  
  
### Get user traits after `identify` call

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Use the following snippet: `val traits =`  
  
`rudderClient!!.getRudderContext().getTraits()`| Use the following snippet: `val traits = analytics.traits`  
  
### Set external ID / custom ID

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Use the `identify` call to set `externalId`.| You can set `externalId` for all events including the application lifecycle events by leveraging a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/OptionPlugin.kt>) for more information.  
The SDK persisted the `externalId`.| You must persist the `externalId` manually.  
  
### Set the Android device token

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Use the [`putDeviceToken` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#setting-the-android-device-token>).| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/SetPushTokenPlugin.kt>) for more information.  
  
### Set custom context

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
You can pass custom context during the SDK initialization.| Support for this feature is removed. Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to set custom context for all events including automatically-tracked events (for example, lifecycle events).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/OptionPlugin.kt>) for more information.  
  
### Set advertising ID

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Use the [`putAdvertisingId` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#setting-the-advertisement-id>) to set the advertisement ID.| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to automatically collect and set the advertisement ID.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/AndroidAdvertisingIdPlugin.kt>) for more information.  
  
### Enable/disable events for specific destinations

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
You can enable or disable event delivery for specific destination across all events while [initializing the SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#1-while-initializing-the-sdk>) or while [sending events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#2-while-sending-events>).| Use a custom plugin to enable or disable event delivery for specific destinations across all event calls, including automatically tracked events (like lifecycle events) using the SDK.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/OptionPlugin.kt>) for more information.  
  
### Session tracking and lifecycle events dependency

Android (Java) — **Legacy**|  Android (Kotlin)  
---|---  
Session tracking is [tightly coupled](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#tracking-user-sessions>) with automatic tracking of lifecycle events. That means you cannot use session tracking if automatic lifecycle tracking is disabled.| Session tracking is decoupled with automatic tracking of lifecycle events. That means you can use the session tracking and automatic lifecycle event tracking mechanisms independently.