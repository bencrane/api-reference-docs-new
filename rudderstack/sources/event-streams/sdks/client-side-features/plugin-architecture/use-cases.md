# Custom Plugin Use Cases in Mobile SDKs

Learn about the different use cases for custom plugins in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide covers the different use cases for [custom plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs, along with the expected event payload and links to the source code.

## Overview

RudderStack maintains sample custom plugins in the [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/tree/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins>) and [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/tree/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins>) SDK sample applications. You can use these plugins as reference implementations to build your own custom plugins.

## User agent collection

These plugins add user agent information to the event context for better device identification. They populate the `context.userAgent` field.

### Android (Kotlin)

Use `UserAgentPlugin` to add user agent information to events.

Find the source code for this plugin [here](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/UserAgentPlugin.kt>).

### iOS (Swift)

Two plugins are available for user agent collection:

Name| Description| Source code  
---|---|---  
`DynamicUserAgentPlugin`| Fetches user agent information dynamically using WebKit.| [Here](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/DynamicUserAgentPlugin.swift>)  
`StaticUserAgentPlugin`| Adds platform-specific static user agent information to events.| [Here](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/StaticUserAgentPlugin.swift>)  
  
#### Sample payload
    
    
    {
    	// ....
      "context": {
    	   // ....
        "userAgent": "Dalvik/2.1.0 (Linux; U; Android 16; sdk_gphone64_arm64 Build/BE2A.250530.026.D1)"
      },
      // ....
    }
    

## Push notification token

Use `SetPushTokenPlugin` to add push notification tokens to the event’s device context for targeted messaging. It populates the `context.device.token` field.

Find the source code for this plugin in the following locations:

  * [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/SetPushTokenPlugin.kt>)
  * [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetPushTokenPlugin.swift>)


#### Sample payload
    
    
    {
      // ....
      "context": {
        // ....
        "device": {
          // ...
          "token": "<TOKEN_VALUE>",
          // ...
        },
        // ....
      },
      // ....
    }
    

## Override anonymous ID

Use `SetAnonymousIdPlugin` to replace the default SDK-generated anonymous ID with a custom value in the event payload. It populates the `anonymousId` field.

Find the source code for this plugin in the following locations:

  * [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/SetAnonymousIdPlugin.kt>)
  * [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetAnonymousIdPlugin.swift>)


## Global event options

The `OptionPlugin` adds global custom context, integrations, and external IDs to all events. It populates the following fields:

  * `context.externalId`
  * Custom context in `context`
  * `integrations`


Find the source code for this plugin in the following locations:

  * [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/OptionPlugin.kt>)
  * [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/OptionPlugin.swift>)


#### Sample payload
    
    
    {
      // ....
      "context": {
        // ....
        "externalId": [
          {
            "id": "someValue",
            "type": "globalExternalId"
          }
        ],
        "sampleKey": "sampleValue", // Custom context
        // ....
      },
      "integrations": {
        "All": true,
        "CleverTap": true
      },
      // ....
    }
    

## Collect advertising ID

Use the plugins in this section to collect and add the advertising ID and ad tracking status to events. They populate the following fields:

  * `context.device.advertisingId`
  * `context.device.adTrackingEnabled`


### Android (Kotlin)

Use `AndroidAdvertisingIdPlugin` to collect and add the Google Advertising ID (GAID) or Amazon Fire Advertising ID and ad tracking status.

Find the source code for this plugin [here](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/AndroidAdvertisingIdPlugin.kt>).

### iOS (Swift)

Use `AdvertisingIdPlugin` to collect and add the iOS Advertising Identifier (IDFA) with ATT compliance.

Find the source code for this plugin [here](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/AdvertisingIdPlugin.swift>).

#### Sample payload
    
    
    {
      // ....
      "context": {
        // ....
        "device": {
          "adTrackingEnabled": true,
          "advertisingId": "6934136c-002f-4b4d-8088-90cd71497a3a",
        },
        // ....
      },
      // ....
    }
    

## Event filtering

Use `EventFilteringPlugin` to filter out specific analytics events from being processed by the SDK.

Find the source code for this plugin in the following locations:

  * [Android (Kotlin)](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/main/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/EventFilteringPlugin.kt>)
  * [iOS (Swift)](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/EventFilteringPlugin.swift>)


## Add Bluetooth information (iOS)

> ![warning](/docs/images/warning.svg)
> 
> This plugin is available only for the iOS (Swift) SDK.

Use `BluetoothInfoPlugin` to add Bluetooth availability information to the network context. It populates the `context.network.bluetooth` field.

Find the source code for this plugin [here](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/BluetoothInfoPlugin.swift>).

#### Sample payload
    
    
    {
        // ....
        "context": {
            // ....
            "network": {
                "bluetooth": true,
            },
            // ....
        },
        // ....
    }
    

## Get ATT tracking status (iOS)

> ![warning](/docs/images/warning.svg)
> 
> This plugin is available only for the iOS (Swift) SDK.

Use `SetATTTrackingStatusPlugin` to set a custom App Tracking Transparency (ATT) status in the device context. It populates the `context.device.attTrackingStatus` field.

Find the source code for this plugin [here](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/SetATTTrackingStatusPlugin.swift>).

#### Sample payload
    
    
    {
        // ....
        "context": {
            // ....
            "device": {
                "attTrackingStatus": 0,
            },
        },
        // ....
    }
    

## See more

  * [Plugin Architecture in Mobile SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/>): Understand the plugin system and how to create custom plugins
  * [Create Custom Plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/create-custom-plugin/>): Steps to create a custom plugin
  * [How to Use Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/#add-custom-plugins-to-integrations>): Add custom plugins to device mode integrations