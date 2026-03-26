# iOS (Obj-C) to iOS (Swift) SDK Migration Guide

Learn how to migrate persisted user data from the legacy iOS (Obj-C) SDK to the iOS (Swift) SDK.

* * *

  * __5 minute read

  * 


This guide explains how to migrate persisted user data from the legacy iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. to the iOS (Swift) SDK so that your users maintain their identity when transitioning from the legacy iOS (Obj-C) SDK to the iOS (Swift) SDK.

## Pre-migration considerations

You can migrate the following values from the legacy iOS (Obj-C) SDK to the iOS (Swift) SDK:

  * `anonymousId`
  * `userId`
  * `traits`
  * Session tracking status
  * App version
  * App build


Also, note that:

  * Events are not migrated in this process
  * The iOS (Swift) SDK does not persist external IDs, so you do not need to migrate them
  * The iOS (Swift) SDK does not support opt status, opt in time, and opt out time
  * The iOS (Swift) SDK manages server config independently, so you do not need to migrate the server config last update value


## Migration process overview

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You must run the migration **before** initializing the iOS (Swift) SDK. The SDK reads persisted values on initialization, so migrated data must already be in place.
>   * Configure the migration code so that it runs **only once**.
> 


  1. Retrieve values from the legacy iOS (Obj-C) SDK storage location.
  2. Transform values as needed — see the Storage key mapping table below.
  3. Save values to the iOS (Swift) SDK-specific `UserDefaults` suite.
  4. Initialize the iOS (Swift) SDK.


For more details, refer to the migration helper class available in the iOS (Swift) SDK sample app.

## Step 1: Understand legacy SDK storage

The legacy iOS (Obj-C) SDK persists `anonymousId`, `userId`, `traits`, app version, app build number, and session-related information under their respective keys. This data is stored in a property list file named `rsDefaultsPersistence.plist`.

> ![info](/docs/images/info.svg)
> 
> **Version note**
> 
> If you are using an SDK version earlier than `v1.25.2`, retrieve the values from `UserDefaults.standard` instead of the `rsDefaultsPersistence.plist` file.

## Step 2: Review legacy SDK storage keys

> ![warning](/docs/images/warning.svg)
> 
> **Data availability**
> 
> The legacy values are available only if the legacy SDK-based app was not removed before installing the app version that integrates the iOS (Swift) SDK.

Use the following table to read values from the legacy SDK storage:

Field| Legacy storage key| Expected data type| Notes  
---|---|---|---  
Anonymous ID| `rl_anonymous_id`| `UUID`  
String| -  
Traits| `rl_traits`| `JSON`  
String| Contains `anonymousId`, `userId`, and `id` along with other trait values  
User ID| `rl_traits`| `String`| The `userId` value is embedded within the traits JSON string  
Session ID| `rl_session_id`| `NSNumber`  
UInt64| If not present, there is no active session in the legacy SDK  
Automatic session tracking| `rl_session_auto_track_status`| `NSNumber`  
Boolean| Indicates whether automatic session tracking is enabled  
Last event timestamp| `rl_last_event_time_stamp`| `NSNumber`  
Double| Timestamp of the most recent event recorded by the SDK  
Application version number| `rl_application_version_key`| `String`| `CFBundleShortVersionString` value from `info.plist`  
Application build number| `rl_application_build_key`| `String`| `CFBundleVersion` value from `info.plist`  
  
## Step 3: Map values to iOS (Swift) SDK

Once you retrieve the legacy values and have access to the iOS (Swift) SDK’s `UserDefaults` instance, store each value using its corresponding key:

#### Storage key mapping

Field| Legacy key| iOS (Swift) SDK key| Transformation notes  
---|---|---|---  
Anonymous ID| `rl_anonymous_id`| `anonymous_id`| Direct migration — no transformation required  
User ID| `rl_traits`| `user_id`| Extract the `userId` value from the traits JSON string  
Traits| `rl_traits`| `traits`| Store as JSON string  
  
Remove `anonymousId`, `id`, and `userId` if present in the retrieved value  
Session ID| `rl_session_id`| `session_id`| Convert the value to string format  
Automatic session status| `rl_session_auto_track_status`| `is_manual_session`| Store the **inverted** (toggled) Boolean value  
Last activity time| `rl_last_event_time_stamp`| `last_activity_time`| Requires timestamp conversion — see Timestamp conversion  
External ID| `rl_external_id`| -| No migration needed — the iOS (Swift) SDK does not persist external IDs  
Application version number| `rl_application_version_key`| `rudder.app_version`| `CFBundleShortVersionString` value from `info.plist` is migrated as a string  
Application build number| `rl_application_build_key`| `rudder.app_build`| `CFBundleVersion` value from `info.plist` is migrated as an integer  
  
## Step 4: Convert last activity timestamps

The legacy iOS (Obj-C) SDK and the iOS (Swift) SDK use different time reference systems for tracking the last activity time:

SDK| Time reference  
---|---  
Legacy iOS (Obj-C) SDK| Absolute timestamp (Unix epoch time) in seconds.  
iOS (Swift) SDK| Absolute timestamp (Unix epoch time) in milliseconds.  
  
#### Conversion steps

  1. Read the legacy timestamp (`legacyTimestamp`) in seconds.
  2. Validate the timestamp — it must be greater than `0` and not a future timestamp.
  3. Convert to milliseconds:


    
    
    lastActivityTime = legacyTimestamp * 1000
    

> ![info](/docs/images/info.svg)
> 
> **Edge case**
> 
> If the legacy timestamp is invalid (zero, negative, or a future timestamp), then conversion is not possible. In such cases, skip migrating the last activity time.

## Step 5: Apply values and initialize the iOS (Swift) SDK

Once you complete the above steps, save the transformed values in the iOS (Swift) SDK’s `UserDefaults` suite and then initialize the iOS (Swift) SDK.

## Migration helper class

RudderStack provides a persistence migration helper class — [PersistentMigratorFromV1](<https://github.com/rudderlabs/rudder-sdk-swift/blob/develop/Examples/SwiftUIExample/SwiftUIExample/PersistenceMigrator/FromV1/PersistentMigratorFromV1.swift>) — to help you migrate persisted values from earlier versions of the iOS (Swift) SDK.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use this helper if you are upgrading from the iOS (Obj-C) SDK and want to restore persisted values before the iOS (Swift) SDK initializes.

Note that:

  * The migrator is **optional** and intended to be used as a reference implementation
  * You can selectively rely on it based on the values you need to migrate
  * Make sure this step runs only once during app startup, **before** the SDK initialization
  * Alternatively, you can call `readPersistence()` to inspect the available values before performing the migration


#### Usage

Initialize the migrator and call `restorePersistence()` **before** initializing the iOS (Swift) SDK:
    
    
    PersistentMigratorFromV1(writeKey: "<IOS_SOURCE_WRITE_KEY>").restorePersistence()
    

## Troubleshooting

Issue| Possible cause| Solution  
---|---|---  
Legacy data not found| App was uninstalled before migration| No migration needed — the iOS (Swift) SDK generates new values automatically  
Timestamp conversion fails| The device was rebooted after the last legacy SDK event| Skip last activity time migration — the session resets naturally  
Traits parsing fails| Corrupt or invalid JSON in legacy storage| Log the error and skip traits migration — you can still migrate other values  
User ID not found in traits| The user was never identified in the legacy iOS (Obj-C) SDK| No action needed — `userId` remains `nil` until the user is identified