# Device Mode Integrations in Mobile SDKs

Learn about device mode integrations in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __2 minute read

  * 


Device mode integrations let you send events directly to third-party destinations from your mobile apps. These integrations use native destination SDKs for real-time event tracking.

## How device mode integrations work

When you add a device mode integration to your app, RudderStack wraps the destination’s native SDK. Events are sent directly from your app to the destination, bypassing RudderStack’s servers.

### Use cases

Device mode integrations are suitable for scenarios requiring:

  * Real-time event delivery to destinations
  * Access to destination-specific features (install attribution, in-app messaging, etc.)
  * Better privacy control over data flow
  * Reduced dependency on RudderStack’s servers


## Standard vs custom device mode integrations

RudderStack offers two types of device mode integrations:

### Standard integrations

Standard integrations are officially supported and maintained by RudderStack.

Note that these integrations:

  * Receive configuration from the RudderStack dashboard
  * Are automatically updated with SDK releases
  * Include built-in error handling and optimization
  * If supported by the destination, map standard events (including standard ecommerce events) and properties to the destination’s standard events and properties. For example, `Order Completed` to `Purchase`


See the supported device mode destinations in the [Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/device-mode-integrations/>) and [iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/device-mode-integrations/>).

### Custom integrations

Custom device mode integrations let you wrap any third-party destination SDK that is not officially supported. They:

  * Use hardcoded or custom configuration
  * Require manual maintenance and updates
  * Give you full control over implementation


## In this section

Guide| Description  
---|---  
[How to Use Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/>)| Learn how to add and use device mode integrations  
[How to Build Custom Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/custom-integrations/>)| Create custom integrations for unsupported destinations  
[Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>)| Complete reference for device mode integration APIs