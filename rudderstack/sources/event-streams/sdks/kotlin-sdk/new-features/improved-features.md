# Improved Features in Android (Kotlin) SDK

Learn about the improved features in Android (Kotlin) SDK compared to the Android (Java) SDK.

* * *

  * __4 minute read

  * 


This guide highlights the features that have been improved in the Android (Kotlin) SDK compared to the Android (Java) SDK.

## Improved features

This section highlights the features enhanced in the Android (Kotlin) SDK as compared to the Android (Java) SDK.

### Configuration

The Android (Kotlin) SDK uses **direct initialization** for a simpler and more intuitive setup.
    
    
    // Android (Kotlin) SDK
    val analytics = Analytics(configuration = Configuration(
        writeKey = "WRITE_KEY",
        application = application,
        dataPlaneUrl = "DATA_PLANE_URL"
    ))
    

### Independent session and lifecycle management

The legacy Android (Java) SDK coupled session tracking with lifecycle events, meaning sessions could only work when lifecycle tracking was enabled.

In the new Android (Kotlin) SDK, session tracking is decoupled from lifecycle events, ensuring sessions can work independently even when lifecycle tracking is turned off.

> ![info](/docs/images/info.svg)
> 
> The Android (Kotlin) SDK also provides a dedicated `SessionConfiguration` object to configure session tracking independently.
    
    
    // New SDK - configure independently
    val configuration = Configuration(
        writeKey = "WRITE_KEY",
        application = application,
        dataPlaneUrl = "DATA_PLANE_URL",
        trackApplicationLifecycleEvents = false,  // Lifecycle events off
        sessionConfiguration = SessionConfiguration(
            automaticSessionTracking = true       // Sessions still work
        )
    )
    

See the [Session Tracking in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/session-tracking/>) guide for more information.

### Granular reset with selective data clearing

The legacy Android (Java) SDK offered limited reset control — just a single Boolean to optionally clear or retain the anonymous ID.

The Android (Kotlin) SDK provides **fine-grained control** over which data points to reset, by configuring the `ResetOptions` object.

See the [Reset API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/reset/>) guide for more information.

### Destination-ready callbacks with success and failure handling

The Android (Kotlin) SDK provides structured result handling for destination initialization, replacing the legacy Android (Java) SDK’s simple callback approach.

See the [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>) guide for more information.

### Direct access to destination instances

The Android (Kotlin) SDK provides direct access to destination instances via the `getDestinationInstance()` method, without requiring a callback to be registered immediately after SDK initialization, unlike the legacy approach.

See the [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>) guide for more information.

### Custom context

The legacy Android (Java) SDK provided a `putCustomContext()` method that accepted `Map<String, Object>` as the value, requiring you to always pass a nested map structure.

The Android (Kotlin) SDK accepts any JSON value type, including simple strings.

See [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#customcontext>) guide for more information.

### Enhanced integration options

The legacy Android (Java) SDK provided a `putIntegration()` method that accepted only a Boolean value to enable or disable a destination integration.

The Android (Kotlin) SDK accepts any JSON value, allowing you to pass destination-specific configuration objects to specific integrations.

See [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations>) guide for more information.

### `externalId` support for all event types

The Android (Kotlin) SDK lets you set `externalId` via `RudderOption` in all event types: `track`, `screen`, `group`, `alias` and `identify`. The legacy Android (Java) SDK only supported the `identify` event type.

See the [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#externalid>) guide for more information.

### Enhanced retry logic

The Android (Kotlin) SDK has an improved retry behavior for failed network requests:

Aspect| Android (Java) — Legacy| Android (Kotlin)  
---|---|---  
Backoff strategy| Mixed (Linear and Exponential)| Consistent exponential backoff  
Error handling| Limited error classification| Smart classification — only retries recoverable errors  
Cool-off period| None| 30 minutes cool-off after repeated failures  
Storage cleanup| Events left orphaned on invalid write key errors| Clears **all persisted data** on the invalid write key errors  
Event deletion| Events retained on all errors| Deletes batches that can never succeed (for example, malformed or oversized payloads)  
  
See the [Event Retry Mechanism](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/event-retry-mechanism/>) guide for more information.

### Enhanced identity management

You can access identity properties directly.
    
    
    val userId = analytics.userId             // String?
    val traits = analytics.traits             // JsonObject?
    

> ![info](/docs/images/info.svg)
> 
> The Android (Java) SDK supports accessing `traits` and `userId` via `rudderClient.rudderContext` API.

See the [User Identity APIs in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/user-identity-apis/>) guide for more information.

### Cleaner event payload

The Android (Kotlin) SDK removes redundant user identity fields from `context.traits` that were unnecessarily duplicated in the legacy Android (Java) SDK, thereby reducing payload size and eliminating unnecessary data inconsistency risks.
    
    
    {
      "anonymousId": "anon-123",
      "userId": "user-456",
      "context": {
        "traits": {
          "anonymousId": "anon-123",
          "id": "user-456",
          "userId": "user-456",
          "email": "alex@example.com",
          "name": "Alex Keener"
        }
      }
    }
    
    
    
    {
      "anonymousId": "anon-123",
      "userId": "user-456",
      "context": {
        "traits": {
          "email": "alex@example.com",
          "name": "Alex Keener"
        }
      }
    }