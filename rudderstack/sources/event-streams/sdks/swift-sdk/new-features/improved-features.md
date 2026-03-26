# Improved Features in iOS (Swift) SDK

Learn about the improved features in iOS (Swift) SDK compared to the iOS (Obj-C) SDK.

* * *

  * __4 minute read

  * 


This guide highlights the features that have been improved in the iOS (Swift) SDK compared to the iOS (Obj-C) SDK.

## Configuration

The iOS (Swift) SDK uses **direct initialization** for a simpler and more intuitive setup.
    
    
    // iOS (Swift) SDK
    import RudderStackAnalytics
    
    // Initialize the RudderStack Analytics SDK
    let config = Configuration(
        writeKey: "<WRITE_KEY>",
        dataPlaneUrl: "<DATA_PLANE_URL>"
    )
    
    let analytics = Analytics(configuration: config)
    

## Independent session and lifecycle management

The legacy iOS (Obj-C) SDK coupled session tracking with lifecycle events, meaning sessions could only work when lifecycle tracking was enabled.

In the new iOS (Swift) SDK, session tracking is decoupled from lifecycle events, ensuring sessions can work independently even when lifecycle tracking is turned off.

> ![info](/docs/images/info.svg)
> 
> The iOS (Swift) SDK also provides a dedicated `SessionConfiguration` object to configure session tracking independently.
    
    
    // New SDK - configure independently
    let configuration = Configuration(
        writeKey: "WRITE_KEY",
        dataPlaneUrl: "DATA_PLANE_URL",
        trackApplicationLifecycleEvents: false,  // Lifecycle events off
        sessionConfiguration: SessionConfiguration(
            automaticSessionTracking: true       // Sessions still work
        )
    )
    let analytics = Analytics(configuration: configuration)
    

See the [Session Tracking in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/session-tracking/>) guide for more information.

## Granular reset with selective data clearing

The legacy iOS (Obj-C) SDK offered limited reset control — just a single Boolean to optionally clear or retain the anonymous ID.

The iOS (Swift) SDK provides **fine-grained control** over which data points to reset, by configuring the `ResetOptions` object.

See the [Reset API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/reset/>) guide for more information.

## Destination-ready callbacks with success and failure handling

The iOS (Swift) SDK provides structured result handling for destination initialization, replacing the legacy iOS (Obj-C) SDK’s simple callback approach.

See the [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>) guide for more information.

## Direct access to destination instances

The iOS (Swift) SDK provides direct access to destination instances via the `getDestinationInstance()` method, without requiring a callback to be registered immediately after SDK initialization, unlike the legacy approach.

See the [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>) guide for more information.

## Custom context

The legacy iOS (Obj-C) SDK provided a `putCustomContext()` method that accepted `Map<String, Object>` as the value, requiring you to always pass a nested map structure.

The iOS (Swift) SDK accepts any JSON value type, including simple strings.

See [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#customcontext>) guide for more information.

## Enhanced integration options

The legacy iOS (Obj-C) SDK provided a `putIntegration()` method that accepted only a Boolean value to enable or disable a destination integration.

The iOS (Swift) SDK accepts any JSON value, allowing you to pass destination-specific configuration objects to specific integrations.

See [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations>) guide for more information.

## `externalId` support for all event types

The iOS (Swift) SDK lets you set `externalId` via `RudderOption` in all event types: `track`, `screen`, `group`, `alias` and `identify`. The legacy iOS (Obj-C) SDK only supported the `identify` event type.

See the [Event Payload Customization Options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#externalid>) guide for more information.

## Enhanced retry logic

The iOS (Swift) SDK has an improved retry behavior for failed network requests:

Aspect| iOS (Obj-C) — Legacy| iOS (Swift)  
---|---|---  
Backoff strategy| Mixed (Linear and Exponential)| Consistent exponential backoff  
Error handling| Limited error classification| Smart classification — only retries recoverable errors  
Cool-off period| None| 30 minutes cool-off after repeated failures  
Storage cleanup| Events left orphaned on invalid write key errors| Clears **all persisted data** on the invalid write key errors  
Event deletion| Events retained on all errors| Deletes batches that can never succeed (for example, malformed or oversized payloads)  
  
See the [Event Retry Mechanism](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/event-retry-mechanism/>) guide for more information.

## Enhanced identity management

You can access identity properties directly.
    
    
    let userId = analytics.userId             // String?
    let traits = analytics.traits             // [String: Any]?
    

> ![info](/docs/images/info.svg)
> 
> The iOS (Obj-C) SDK supports accessing `traits` and `userId` via `rudderClient.context` API.

See the [User Identity APIs in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/user-identity-apis/>) guide for more information.

## Cleaner event payload

The iOS (Swift) SDK removes redundant user identity fields from `context.traits` that were unnecessarily duplicated in the legacy iOS (Obj-C) SDK, thereby reducing payload size and eliminating unnecessary data inconsistency risks.
    
    
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