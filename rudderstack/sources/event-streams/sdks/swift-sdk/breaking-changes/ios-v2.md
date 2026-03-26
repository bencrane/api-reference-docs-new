# Breaking Changes in iOS (Swift) SDK

Learn about the breaking changes introduced in the iOS (Swift) SDK when migrating from the legacy iOS SDK v2.

* * *

  * __3 minute read

  * 


This document outlines the breaking changes introduced in the iOS (Swift) SDK when migrating from the legacy [iOS SDK v2](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/ios-v2/>).

## Package & import changes

The SDK has been renamed from `Rudder` to `RudderStackAnalytics`. Update your package dependencies and import statements throughout your codebase.
    
    
    // Old
    .package(url: "git@github.com:rudderlabs/rudder-sdk-ios.git", from: "2.5.1-beta")
    .product(name: "Rudder", package: "rudder-sdk-ios")
    
    // New
    .package(url: "https://github.com/rudderlabs/rudder-sdk-swift.git", from: "1.0.0")
    .product(name: "RudderStackAnalytics", package: "rudder-sdk-swift")
    
    
    
    // Old
    import Rudder
    
    // New
    import RudderStackAnalytics
    

## Initialization

The singleton pattern (`RSClient.sharedInstance()`) has been replaced with an instance-based approach.
    
    
    let config = RSConfig(writeKey: "WRITE_KEY")
        .dataPlaneURL("<https://data-plane.com>")
    RSClient.sharedInstance().configure(with: config)
    
    // Usage anywhere
    RSClient.sharedInstance().track("Event")
    
    
    
    let configuration = Configuration(
        writeKey: "WRITE_KEY",
        dataPlaneUrl: "<https://data-plane.com>"
    )
    let analytics = Analytics(configuration: configuration)
    
    // Store and use the instance
    analytics.track(name: "Event")
    

## Public classes renamed

All public classes have been renamed to remove the `RS` prefix in favor of clearer, more descriptive names. Find and replace all references in your codebase.

Old| New  
---|---  
`RSClient`| `Analytics`  
`RSConfig`| `Configuration`  
`RSOption`| `RudderOption`  
`RSMessage`| `Event`  
`RSPlugin`| `Plugin`  
`RSEventPlugin`| `EventPlugin`  
`RSDestinationPlugin`| `IntegrationPlugin`  
`RSLogLevel`| `LogLevel`  
  
## API method signatures

All tracking methods now use explicit named parameters for better code readability and Swift conventions. The first parameter is no longer anonymous, and `option` has been renamed to `options`.

Method| iOS SDK v2 — Legacy| iOS (Swift)  
---|---|---  
Track| `track(_:properties:option:)`| `track(name:properties:options:)`  
Identify| `identify(_:traits:option:)`| `identify(userId:traits:options:)`  
Screen| `screen(_:category:properties:option:)`| `screen(screenName:category:properties:options:)`  
Group| `group(_:traits:option:)`| `group(groupId:traits:options:)`  
Alias| `alias(_:option:)`| `alias(newId:previousId:options:)`  
Reset| `reset()`| `reset(options:)`  
  
## Type changes

Several numeric types have changed to `UInt64` for consistency and to support larger values. Note that flush interval units changed from seconds to milliseconds for finer control.

Field| iOS SDK v2 — Legacy| iOS (Swift)  
---|---|---  
Session ID| `Int`| `UInt64`  
Session timeout| `Int`  
Milliseconds| `UInt64`  
Milliseconds  
Flush interval| `Int`  
Seconds| `UInt64`  
Milliseconds  
  
An example for session management is shown below:
    
    
    // Old
    RSClient.sharedInstance().startSession(1234567890)  // Int
    
    // New
    analytics.startSession(sessionId: 1234567890)  // UInt64
    

## Plugin execution stages

Plugin execution stages have been renamed to better describe their purpose in the event processing pipeline. The `.after` stage has been removed — use `.terminal` or `.utility` instead.

iOS SDK v2 — Legacy| iOS (Swift)  
---|---  
`.before`| `.preProcess`  
`.enrichment`| `.onProcess`  
`.destination`| `.terminal`  
`.after`| **Removed**  
`.utility`| `.utility`  
  
## Configuration mappings

The builder pattern (`RSConfig().method().method()`) has been replaced with a standard Swift initializer. Session-related settings are now grouped in a separate `SessionConfiguration` object.

Use the below table as a reference when updating your configuration code:

iOS SDK v2 — Legacy (`RSConfig`)| iOS (Swift) SDK (`Configuration`)  
---|---  
`writeKey`| `writeKey`  
`dataPlaneURL(_:)`| `dataPlaneUrl`  
`controlPlaneURL(_:)`| `controlPlaneUrl`  
`loglevel(_:)`| Handled via `LoggerAnalytics` class  
`trackLifecycleEvents(_:)`| `trackApplicationLifecycleEvents`  
`recordScreenViews(_:)`| Not available. User can handle via custom plugins  
`flushQueueSize(_:)`| `CountFlushPolicy`  
`sleepTimeOut(_:)`| Handled via `FrequencyFlushPolicy`  
`dbCountThreshold(_:)`| Handled via `CountFlushPolicy`  
`autoSessionTracking(_:)`| Handled via `SessionConfiguration.automaticSessionTracking`  
`sessionTimeout(_:)`| Handled via `SessionConfiguration.sessionTimeoutInMillis`  
  
## Removed features

The following features are removed in the iOS (Swift) SDK:

  * `MessageContext` and `context` call are no longer available.
  * `CocoaPods` is not supported — only Swift Package Manager is supported.


## Migration from iOS v2 SDK

See the [Migration Guide](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/migration-guide/ios-v2/>) for detailed instructions on migrating from the legacy iOS SDK v2 to the iOS (Swift) SDK.