# New Features in iOS (Swift) SDK

Learn about the new and improved features in iOS (Swift) SDK compared to the iOS (Obj-C) SDK.

* * *

  * __2 minute read

  * 


This section highlights the new and improved features in the iOS (Swift) SDK compared to the iOS (Obj-C) SDK.

## New features

The iOS (Swift) SDK introduces several features not available in the iOS (Obj-C) SDK.

### Modern Swift concurrency

The iOS (Swift) SDK is built with `async-await` and structured concurrency. It uses reactive state management for better performance and reliability, and non-blocking operations for improved app responsiveness.

### Enhanced platform support

The SDK adds native support for macOS 12.0+ and provides a unified API across all Apple platforms. It leverages the latest iOS 15.0+, macOS 12.0+, tvOS 15.0+, and watchOS 8.0+ features.

### Custom plugins

Custom plugins let you intercept and transform events at any point in the analytics pipeline. With this feature, you can:

  * Enrich events with device context
  * Filter out sensitive data or drop specific information (for example, `Application Opened` and `Application Backgrounded` events) before it leaves the device.


The new plugin system lets you add, remove, or modify custom plugins at runtime.
    
    
    // Create custom plugins
    import RudderStackAnalytics
    
    final class CustomEventFilter: Plugin {
        var pluginType: PluginType = .onProcess
        var analytics: Analytics?
        
        func setup(analytics: Analytics) {
            self.analytics = analytics
        }
        
        func intercept(event: any Event) -> (any Event)? {
            // Custom filtering logic
            return event
        }
    }
    
    analytics.add(plugin: CustomEventFilter())
    

See the [Custom plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) guide for more information.

### Multiple analytics instances

You can create and manage multiple analytics instances with different configurations.

Each instance maintains its own independent state, storage, and configuration — this is particularly useful for multi-tenant applications or tracking different data streams.

See the [Multiple Instance Support](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/multiple-instance-support/>) guide for more information.

### Custom logger

Use a centralized custom logger abstraction with pluggable implementations and global log-level configuration.

See the [Logging APIs in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/logging-apis/>) guide for more information.

### Custom plugins in integrations

You can add custom plugins to any [supported integration](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/device-mode-integrations/>) to enhance event handling and processing.

See [Add custom plugins to integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/#add-custom-plugins-to-integrations>) for more information.

### Shutdown API

You can explicitly shut down the `analytics` instance to terminate all ongoing operations. The SDK automatically removes all registered plugins and releases allocated resources. All events recorded before shutdown are persisted and processed on the next startup.
    
    
    analytics.shutdown()
    

See the [Shutdown API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/shutdown/>) guide for more information.