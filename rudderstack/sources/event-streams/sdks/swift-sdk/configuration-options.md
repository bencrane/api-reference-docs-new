# iOS (Swift) SDK Configuration Options Reference

Complete reference for the configuration options available in the RudderStack iOS (Swift) SDK.

* * *

  * __3 minute read

  * 


The iOS (Swift) SDK provides various configuration options to customize its behavior according to your requirements. This guide covers all the available configuration options and their usage.

## Configuration class

The `Configuration` class is used to initialize the SDK in your Apple platform application. It defines the required parameters and optional configuration settings to customize the SDK behavior.

## SDK configuration options

Parameter| Type| Description  
---|---|---  
`writeKey`  
Required| String| The source write key obtained from the RudderStack dashboard used for authentication.  
`dataPlaneUrl`  
Required| String| The URL of your RudderStack data plane (backend) where the events are sent.  
`controlPlaneUrl`| String| URL for remote configuration management.  
  
**Default value:** `https://api.rudderlabs.com`  
`gzipEnabled`| Boolean| Enables or disables Gzip compression for network requests.  
  
**Default value:** `false`  
`flushPolicies`| Array of flush policies| Specifies when and how events are sent to the RudderStack backend.  
  
See [Flush policies in iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/flush-api/#flush-policies>) for more information.  
  
**Default value:** `[StartupFlushPolicy(), FrequencyFlushPolicy(), CountFlushPolicy()]`  
`collectDeviceId`| Boolean| Enables automatic collection of the device’s unique ID.  
  
**Default value:** `true`  
`trackApplicationLifecycleEvents`| Boolean| Enables automatic tracking of [application lifecycle events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/lifecycle-events-tracking/>) (app start, background, and foreground transitions).  
  
**Default value:** `true`  
`sessionConfiguration`| SessionConfiguration| Configuration settings for managing user sessions.  
  


  * See [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/session-tracking/>) for more information on session management in the iOS (Swift) SDK.
  * See Session configuration for more information on the session configuration options and their default values.

  
  
## Session configuration

The `SessionConfiguration` class provides the following parameters to customize session management:

Parameter| Type| Description  
---|---|---  
`automaticSessionTracking`| Boolean| Enables automatic session tracking.  
  
**Default value:** `true`  
`sessionTimeoutInMillis`| UInt64| Sets the timeout duration for automatic session tracking in milliseconds. It is the time between the app closed or backgrounded to being foregrounded or relaunched again.  
  
The SDK times out a session and starts a new session after this time has elapsed.  
  
**Default value:** `300000` (5 minutes)  
  
## Device ID collection

When you enable `collectDeviceId`, the iOS (Swift) SDK retrieves a unique device ID and includes it in the event payload under the `device.id` field in the event’s `context` object.

In the iOS, watchOS, and tvOS platforms, the SDK uses the device’s `identifierForVendor` field. In macOS, it derives the ID from the device’s MAC address.

> ![warning](/docs/images/warning.svg)
> 
> If the SDK retrieves an empty or invalid value for the device ID, it will not include the `device.id` field in the event payload’s `context`.

## Request compression

When you set `gzipEnabled` to `true`, all `/batch` requests sent by the SDK will have their payloads compressed using Gzip compression, thereby reducing the size of the network requests.

## Sample SDK initialization

The following snippet demonstrates how to initialize the iOS (Swift) SDK with the supported configuration options:
    
    
    let analytics = Analytics(
        configuration: Configuration(
            // Required parameters
            writeKey: "YOUR_WRITE_KEY",
            dataPlaneUrl: "YOUR_DATA_PLANE_URL",
            
            // Optional parameters
            controlPlaneUrl: "https://api.rudderlabs.com",
            gzipEnabled: true,
            flushPolicies: [
                StartupFlushPolicy(),
                CountFlushPolicy(flushAt: 20),
                FrequencyFlushPolicy(flushIntervalInMillis: 30000)
            ], // Sets custom flush policies
            collectDeviceId: true,
            trackApplicationLifecycleEvents: true,
            sessionConfiguration: SessionConfiguration(
                automaticSessionTracking: true,
                sessionTimeoutInMillis: 300000 // 5 minutes
            )
        )
    )
    
    
    
    RSSConfigurationBuilder *builder = [[RSSConfigurationBuilder alloc]
    // Required parameters
              initWithWriteKey:@"YOUR_WRITE_KEY"
    					dataPlaneUrl:@"YOUR_DATA_PLANE_URL"];
    					
    // Optional parameters
    [builder setControlPlaneUrl: @"https://api.rudderlabs.com"];
    [builder setGzipEnabled: YES];
    [builder setFlushPolicies: @[
            [RSSStartupFlushPolicy new],
            [[RSSCountFlushPolicy alloc] initWithFlushAt: 20],
            [[RSSFrequencyFlushPolicy alloc] initWithFlushIntervalInMillis: 30000]
    ]];
    [builder setCollectDeviceId: YES];
    [builder setTrackApplicationLifecycleEvents: YES];
    
    // Prepare Session Configuration
    RSSSessionConfigurationBuilder *sessionBuilder = [RSSSessionConfigurationBuilder new];
    [sessionBuilder setAutomaticSessionTracking: YES];
    [sessionBuilder setSessionTimeoutInMillis: @30000];
        
    [builder setSessionConfiguration: [sessionBuilder build]];
    
    RSSAnalytics *analytics = [[RSSAnalytics alloc] 
    																			initWithConfiguration:[builder build]];