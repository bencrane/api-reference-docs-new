# Network Information Tracking in Mobile SDKs

Learn about the network information tracking feature available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide walks you through the network information tracking feature available in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs automatically track network-related information and attach it to the event payload. It enriches every outgoing event with network-related metadata like Wi-Fi status, cellular connectivity, Bluetooth status, and carrier name.

## Network parameters

RudderStack collects and attaches the following information in the `network` field of the event payload’s `context` object:

### Android (Kotlin)

Parameter| Description| Required permissions  
---|---|---  
`carrier`| Name of the mobile network carrier (if available).| -  
`cellular`| Determines whether the device is connected to a cellular network.| `ACCESS_NETWORK_STATE`  
`wifi`| Determines whether Wi-fi is enabled.| `ACCESS_WIFI_STATE` or `ACCESS_NETWORK_STATE`  
`bluetooth`| Determines whether Bluetooth is enabled.| `BLUETOOTH`  
  
### iOS (Swift)

Parameter| Description| Notes  
---|---|---  
`wifi`| Determines whether Wi-fi is enabled.| -  
`cellular`| Determines whether the device is connected to a cellular network.| -  
`bluetooth`| Determines whether Bluetooth is enabled.| Use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to add this value.  
  
See this [Sample plugin](<https://github.com/rudderlabs/rudder-sdk-swift/blob/main/Examples/SwiftUIExample/SwiftUIExample/CustomPlugins/BluetoothInfoPlugin.swift>) for more information.  
  
> ![info](/docs/images/info.svg)
> 
> Apple has deprecated access to the `carrier` information for privacy reasons.

## Add required permissions

The Android (Kotlin) and iOS (Swift) SDKs require some permissions in the app code to attach the above-mentioned parameters to the event payload.

### Android (Kotlin)

For Android (Kotlin) SDK, the `AndroidManifest.xml` file is responsible for managing these permissions. You can add these permissions in the manifest file as follows:
    
    
    <!-- Required -->
    <!-- Allows access to the internet for network communication -->
    <uses-permission android:name="android.permission.INTERNET"/>
    
    <!-- Optional --> 
    <!-- Allows access to track both WiFi and Cellular state -->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    
    <!-- Optional --> 
    <!-- Grants access only to track WiFi state if the above permission is not used -->
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
    
    <!-- Optional -->
    <!-- Required for Bluetooth functionality - allows access to track Bluetooth state -->
    <uses-permission android:name="android.permission.BLUETOOTH"/>
    

Note that:

  * The permissions marked as **Optional** in the above snippet are attached to the event payload only if the SDK is able to determine them based on the available permissions and the device running the app.
  * The SDK updates the `cellular`, `wifi` and `bluetooth` values dynamically for each event payload, that is, they represent the real-time status of these parameters at the time the event is triggered.


A sample JSON payload with the `network` field populated is shown below:
    
    
    {
      //...
      "context": {
        "network": {
          "carrier": "CarrierName",
          "cellular": true,
          "wifi": false,
          "bluetooth": true
        }
      }
      //...
    }
    

### iOS (Swift)

For the iOS (Swift) SDK, Bluetooth permissions must be declared in the app’s `Info.plist` file. The specific keys you add will depend on the type of Bluetooth access your app requires.

> ![warning](/docs/images/warning.svg)
> 
> Without these keys, your app will crash or be rejected when requesting Bluetooth access at runtime.
    
    
    <key>NSBluetoothAlwaysUsageDescription</key>
    <string>This app requires Bluetooth access to communicate with nearby devices.</string>
    
    <key>NSBluetoothPeripheralUsageDescription</key>
    <string>This app requires Bluetooth access to act as a peripheral device.</string>
    

Note that:

  * `NSBluetoothAlwaysUsageDescription` is required for general Bluetooth access.
  * `NSBluetoothPeripheralUsageDescription` is required if your app acts as Bluetooth peripheral.
  * The value of each key is a user-facing message explaining why your app needs Bluetooth access.
  * The SDK updates the `cellular`, `wifi` and `bluetooth` values dynamically for each event payload, that is, they represent the real-time status of these parameters at the time the event is triggered.


A sample JSON payload with the `network` field populated is shown below:
    
    
    {
      //...
      "context": {
        "network": {
          "cellular": true,
          "wifi": false,
          "bluetooth": true // Present when added via custom plugin
        }
      }
      //...
    }