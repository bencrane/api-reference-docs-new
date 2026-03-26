# New Features in Android (Kotlin) SDK

Learn about the new and improved features in Android (Kotlin) SDK compared to the Android (Java) SDK.

* * *

  * __2 minute read

  * 


This section highlights the new and improved features in the Android (Kotlin) SDK compared to the Android (Java) SDK.

## New features

The Android (Kotlin) SDK introduces several features not available in the Android (Java) SDK.

### Modern Kotlin concurrency

The Android (Kotlin) SDK leverages Kotlin coroutines and structured concurrency for non-blocking, main-thread-safe operations. Reactive state management ensures predictable state updates and thread-safe data access.

### Custom plugins

Custom plugins let you intercept and transform events at any point in the analytics pipeline. With this feature, you can:

  * Enrich events with device context
  * Filter out sensitive data or drop specific information (for example, `Application Opened` and `Application Backgrounded` events) before it leaves the device.


The new plugin system lets you add, remove, or modify custom plugins at runtime.
    
    
    // Create custom plugins
    class CustomEventFilter : Plugin {
        override val pluginType: Plugin.PluginType = Plugin.PluginType.OnProcess
    
        override suspend fun intercept(event: Event): Event? {
            // Custom filtering logic
            return event
        }
    }
    
    analytics.add(CustomEventFilter())
    

See the [Custom plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) guide for more information.

### Multiple analytics instances

You can create and manage multiple analytics instances with different configurations.

Each instance maintains its own independent state, storage, and configuration — this is particularly useful for multi-tenant applications or tracking different data streams.

See the [Multiple Instance Support](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/multiple-instance-support/>) guide for more information.

### Custom logger

Allows custom logger implementations so you can route SDK logs to crash reporters, remote services, or your app’s existing logging system.

See the [Logging APIs in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/logging-apis/>) guide for more information.

### Custom plugins in integrations

You can add custom plugins to any [supported integration](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/device-mode-integrations/>) to enhance event handling and processing.

See [Add custom plugins to integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/#add-custom-plugins-to-integrations>) for more information.

### Automatic screen tracking with `NavController`

The Android (Kotlin) SDK now supports automatic screen tracking for Jetpack Navigation. The legacy Android (Java) SDK had no built-in support for this — you had to manually call `screen` API for each navigation destination.

See the [Automatic Screen Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/automatic-screen-tracking/#navigation-destination-tracking>) guide for more information.

### Shutdown API

You can explicitly shut down the `analytics` instance to terminate all ongoing operations. The SDK automatically removes all registered plugins and releases allocated resources. All events recorded before shutdown are persisted and processed on the next startup.
    
    
    analytics.shutdown()
    

See the [Shutdown API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/shutdown/>) guide for more information.