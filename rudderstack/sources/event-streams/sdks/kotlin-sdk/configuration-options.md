# Android (Kotlin) SDK Configuration Options Reference

Complete reference for the configuration options available in the RudderStack Android (Kotlin) SDK.

* * *

  * __3 minute read

  * 


The RudderStack Android (Kotlin) SDK provides various configuration options to customize its behavior according to your requirements. This guide covers all the available configuration options and their usage.

## Configuration class

The `Configuration` class is used to initialize the RudderStack SDK in your Android application. It defines the required parameters and optional configuration settings to customize the SDK behavior.

## SDK configuration options

Parameter| Type| Description  
---|---|---  
`writeKey`  
Required| String| The source write key obtained from the RudderStack dashboard used for authentication.  
`application`  
Required| Application| The Android `Application` instance used to initialize the SDK. It is used for accessing Android-specific functionality and tracking lifecycle events.  
`dataPlaneUrl`  
Required| String| The URL of your RudderStack data plane (backend) where the events are sent.  
`trackApplicationLifecycleEvents`| Boolean| Enables automatic tracking of [application lifecycle events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/lifecycle-events-tracking/>) (app start, background, and foreground transitions).  
  
**Default value:** `true`  
`trackDeepLinks`| Boolean| Enables automatic tracking of [deep link events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/deep-link-tracking/>).  
  
**Default value:** `true`  
`trackActivities`| Boolean| Enables [automatic tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/automatic-screen-tracking/#activity-tracking>) of the activity lifecycle, triggering `screen` events for each activity.  
  
**Default value:** `false`  
`collectDeviceId`| Boolean| Enables automatic collection of the device’s unique ID.  
  
**Default value:** `true`  
`sessionConfiguration`| SessionConfiguration| Configuration settings for managing user sessions.  
  


  * See [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/session-tracking/>) for more information on session management in the Android (Kotlin) SDK.
  * See Session configuration for more information on the session configuration options and their default values.

  
`controlPlaneUrl`| String| URL for remote configuration management.  
  
**Default value:** `https://api.rudderlabs.com`  
`flushPolicies`| List of flush policies| Specifies when and how events are sent to the RudderStack backend.  
  
See [Flush policies in Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/flush-api/#flush-policies>) for more information.  
  
**Default value:** `listOf(CountFlushPolicy(), FrequencyFlushPolicy(), StartupFlushPolicy())`  
`gzipEnabled`| Boolean| Enables or disables Gzip compression for network requests.  
  
**Default value:** `false`  
  
## Session configuration

The `SessionConfiguration` class provides the following parameters to customize session management:

Parameter| Type| Description  
---|---|---  
`automaticSessionTracking`| Boolean| Enables automatic session tracking.  
  
**Default value:** `true`  
`sessionTimeoutInMillis`| Long| Sets the timeout duration for automatic session tracking in milliseconds. It is the time between the app closed or backgrounded to being foregrounded or relaunched again.  
  
The SDK times out a session and starts a new session after this time has elapsed.  
  
**Default value:** `300000` (5 minutes)  
  
## Device ID collection

When you enable `collectDeviceId`, the SDK retrieves a unique device ID using the `Settings.Secure.ANDROID_ID` API and includes it in the event payload under the `device.id` field in the event’s `context` object.

> ![warning](/docs/images/warning.svg)
> 
> If the SDK retrieves an empty or invalid value for the device ID, it will not include the `device.id` field in the event payload’s `context`.

## Request compression

When you set `gzipEnabled` to `true`, all `/batch` requests sent by the SDK will have their payloads compressed using Gzip compression, thereby reducing the size of the network requests.

## Sample SDK initialization

The following snippet demonstrates how to initialize the Android (Kotlin) SDK with the supported configuration options:
    
    
    val analytics = Analytics(
        configuration = Configuration(
            // Required parameters
            application = application,
            writeKey = "YOUR_WRITE_KEY",
            dataPlaneUrl = "YOUR_DATA_PLANE_URL",
            
            // Optional parameters
            controlPlaneUrl = "YOUR_CONTROL_PLANE_URL",
            trackApplicationLifecycleEvents = true,
            trackDeepLinks = true,
            trackActivities = true,
            collectDeviceId = true,
            sessionConfiguration = SessionConfiguration(
                automaticSessionTracking = true,
                sessionTimeoutInMillis = 3000
            ),
            gzipEnabled = true,
            flushPolicies = listOf(CountFlushPolicy(flushAt = 10)) // Sets custom flush policies
        )
    )