# Breaking Changes in iOS (Swift) SDK

Learn about the breaking changes introduced in the iOS (Swift) SDK.

* * *

  * __6 minute read

  * 


This document outlines the breaking changes introduced in the iOS (Swift) SDK when migrating from the legacy iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .

> ![info](/docs/images/info.svg)
> 
> See the [iOS SDK v2 to iOS (Swift) SDK Breaking Changes](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/breaking-changes/ios-v2/>) guide for more information on the breaking changes when migrating from the legacy iOS SDK v2 to the iOS (Swift) SDK.

## Overview

The iOS (Swift) SDK is built from scratch while retaining the core functionalities of the iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .

Note the following before upgrading your SDK:

  * This SDK does not support automatic data migration from the previous iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .
  * Any data persisted by the iOS (Obj-C) SDK is not carried over automatically.
  * The iOS (Swift) SDK requires a higher minimum platform version (iOS 15.0+ vs iOS 12.0+).


## SDK initialization

The way of initializing the iOS (Swift) SDK has changed. See the following snippets for comparison:
    
    
    import Rudder
    
    let builder: RSConfigBuilder = RSConfigBuilder()
                .withDataPlaneUrl("<DATA_PLANE_URL>")
    
    RSClient.getInstance("<WRITE_KEY>", config: builder.build())
    
    
    
    import RudderStackAnalytics
    
    let config = Configuration(
        writeKey: "<WRITE_KEY>",
        dataPlaneUrl: "<DATA_PLANE_URL>"
    )
    let analytics = Analytics(configuration: config)
    

> ![info](/docs/images/info.svg)
> 
> The iOS (Swift) SDK does not follow a singleton pattern. You will need to manage the `Analytics` instance yourself.

## `RudderOption` changes

The way of creating a `RudderOption` instance has changed in the iOS (Swift) SDK:

In the iOS (Obj-C) SDK, an `RSOption` instance was created using method chaining:
    
    
    let option = RSOption()
            .putIntegration("Amplitude", isEnabled: false)
            .putExternalId("brazeExternalId", withId: "some_external_id_1")
            .putCustomContext(["key": "value"], withKey: "customKey")
            
    let traits = ["name": "John", "email": "john@example.com"]
            
    RSClient.sharedInstance()?.identify("user123", traits: traits, options: option)
    

In the iOS (Swift) SDK, a `RudderOption` instance is created using constructor arguments:
    
    
    let externalId = ExternalId(type: "brazeExternalId", id: "some_external_id_1")
    let option = RudderOption(
        integrations: ["Amplitude": false],
        customContext: ["customKey": ["key": "value"]],
        externalIds: [externalId]
    )
    
    let traits = ["name": "John", "email": "john@example.com"]
    
    // Identify event is used just for demonstration purposes.
    analytics.identify(userId: "user123", traits: traits, options: option)
    

## Other API changes

Method| iOS (Obj-C) — Legacy| iOS (Swift)  
---|---|---  
`putIntegration`| Accepts two arguments — `type` (String) and `enabled` (Boolean).| Converted into constructor arguments and renamed to `integrations` of a single Dictionary type.  
`putCustomContext`| Accepts two arguments — `type` (String) and `context` (Dictionary).| Converted into constructor arguments and renamed to `customContext` of a single Dictionary type.  
`putExternalId`| Accepts two arguments — `type` (String) and `id` (String).| Converted into constructor arguments and renamed to `externalIds` of type `[ExternalId]`, where `ExternalId` is a class with a `type` (String) and `id` (String).  
`sharedInstance`| Singleton pattern for accessing the client.| No singleton pattern - you manage the `Analytics` instance.  
`getInstance`| Static method to initialize the client.| Direct initialization with `Analytics(configuration:)`.  
`reset()`| Deprecated method without parameters.| Replaced with `reset()` that always clears `anonymousId`.  
`reset:(BOOL)clearAnonymousId`| Method with Boolean parameter to control `anonymousId` clearing.| Use a custom plugin to retain `anonymousId` if needed.  
  
## SDK configuration changes

The following table maps the SDK configuration options available in the iOS (Obj-C) SDK to the new iOS (Swift) SDK:

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
`withDataPlaneUrl`| `dataPlaneUrl`  
`withControlPlaneUrl`| `controlPlaneUrl`  
`withLogLevel`| Handled via `LoggerAnalytics` class  
`withDBCountThreshold`| Handled via `CountFlushPolicy`  
`withSleepTimeout`| Handled via `FrequencyFlushPolicy`  
`withConfigRefreshInterval`| Handled internally  
`withTrackLifecycleEvents`| `trackApplicationLifecycleEvents`  
`withRecordScreenViews`| Not available. User can handle via custom plugins  
`withCollectDeviceId`| `collectDeviceId`  
`withGzip`| `gzipEnabled`  
`withAutomaticSessionTracking`| Handled via `SessionConfiguration.automaticSessionTracking`  
`sessionInActivityTimeOut`| Handled via `SessionConfiguration.sessionTimeoutInMillis`  
`withFactory`| Handled via plugins. For example, `analytics.add(plugin: BrazeIntegration())`  
`flushQueueSize`| `CountFlushPolicy`  
  
## Removed features

The following features are removed in the iOS (Swift) SDK:

  * [Database encryption](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#dbencryption>) \- The `dbEncryption` configuration option is no longer available.
  * Background Mode - The `enableBackgroundMode` option is no longer available.
  * Direct context access - `RSContext` and `getContext` method are no longer available.
  * `CocoaPods` support - Only Swift Package Manager is supported.


## Feature updates

This section covers the different feature updates introduced in the iOS (Swift) SDK:

### Reset API

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
`reset(true)` resets all values| `analytics.reset()` resets all values  
`reset(false)` retains `anonymousId` and clears all other values| You can also use the `reset` API to perform a selective reset, that is, specify which values to reset.  
  
See the [Reset API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/reset/#selective-reset>) guide for more information.  
  
### Flush configuration

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
The following configuration options are available:  
  


  * `withSleepTimeout`
  * `withDBCountThreshold`
  * `flushQueueSize`

| The following [flush policies](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/flush-api/#flush-policies>) are available:  
  


  * `FrequencyFlushPolicy`
  * `CountFlushPolicy`
  * `StartupFlushPolicy`

  
  
### Override anonymous ID

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
Use the [`putAnonymousId` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#overriding-anonymous-id>).| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetAnonymousIdPlugin.swift>) for more information.  
  
### Get user traits after `identify` call

iOS (Legacy)| iOS (Swift) SDK  
---|---  
Use the following snippet: `RSContext *context = [[RSClient sharedInstance] context];`  
  
`NSDictionary *traits = context.traits;`| Use the following snippet: `let traits = analytics.traits`  
  
### Set external ID or custom ID

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
Use the `identify` call to set `externalId`.| You can set `externalId` for all events including the application lifecycle events by leveraging a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/OptionPlugin.swift>) for more information.  
The SDK persisted the `externalId`.| You must persist the `externalId` manually or use a custom plugin.  
  
### Set iOS device token

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
Use the [`putDeviceToken` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#setting-the-ios-device-token>).| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetPushTokenPlugin.swift>) for more information.  
  
### Set custom context

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
You can pass custom context during the SDK initialization and via `putCustomContext` method.| Support for global custom context during initialization is removed. Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to set custom context for all events including automatically-tracked events.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/OptionPlugin.swift>) for more information.  
  
### `attTrackingStatus`

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
The `attTrackingStatus` field is always present in `context.device` field. You can update it using the below API:  
  
`[[[RSClient sharedInstance] context] putAppTrackingConsent:RSATTAuthorize];`| The `attTrackingStatus` field is not added by default — use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to do so.  
  
See this [sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/develop/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetATTTrackingStatusPlugin.swift>) for more information.  
  
### Set advertising ID

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
Use the [`putAdvertisingId` method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#setting-the-advertisement-id>) to set the advertisement ID.| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to automatically collect and set the advertisement ID.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/AdvertisingIdPlugin.swift>) for more information.  
  
### Filter events for specific destinations

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
You can enable or disable event delivery for specific destinations across all events while [initializing the SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#1-passing-destinations-while-initializing-sdk>) or while [sending events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#2-passing-destinations-while-making-event-calls>) via `RSOption`.| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to enable or disable event delivery for specific destinations across all event calls, including automatically tracked events (like lifecycle events) using the SDK.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/OptionPlugin.swift>) for more information.  
  
### Session tracking and lifecycle events

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
Session tracking is tightly coupled with automatic tracking of lifecycle events. That means you cannot use session tracking if automatic lifecycle tracking is disabled.| Session tracking is decoupled with automatic tracking of lifecycle events. That means you can use the session tracking and automatic lifecycle event tracking mechanisms independently.  
  
### Platform support

iOS (Obj-C) — Legacy| iOS (Swift) SDK  
---|---  
  
  * iOS 12.0+
  * tvOS 11.0+
  * watchOS 7.0+

| 

  * iOS 15.0+
  * macOS 12.0+
  * tvOS 15.0+
  * watchOS 8.0+