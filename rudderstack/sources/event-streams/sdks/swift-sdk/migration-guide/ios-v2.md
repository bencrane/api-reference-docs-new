# iOS SDK v2 to iOS (Swift) SDK Migration Guide

Learn how to migrate persisted user data from the legacy iOS SDK v2 to the iOS (Swift) SDK.

* * *

  * __4 minute read

  * 


This section provides instructions for migrating persisted user data from the legacy iOS SDK v2 to the iOS (Swift) SDK to maintain continuity of user identity, session tracking, and custom traits across SDK versions.

## Overview

You can migrate the following values from the legacy iOS SDK v2 to the iOS (Swift) SDK:

  * `anonymousId`
  * `userId`
  * `traits`
  * Session-related values
  * App version
  * App build


Note that:

  * The iOS (Swift) SDK does not persist external IDs, so you do not need to migrate them.
  * The iOS SDK v2 does not persist the `anonymousId` anywhere — it uses the current device’s `identifierForVendor` instead.


## Step 1: Understand legacy SDK storage

The legacy iOS SDK v2 persists `userId`, `traits`, app version, app build number, and session-related information under their respective keys in `UserDefaults.standard`.

The following table explains how to read values from the legacy SDK storage:

Field| Legacy storage key| Value type| Notes  
---|---|---|---  
Anonymous ID| -| `UUID`  
String| `anonymousId` is not stored anywhere.  
  
Instead, the current device’s `identifierForVendor` is used.  
Traits| `rs_traits`| `JSON`  
String| Stored as keyed-archived dictionary data.  
User ID| `rs_user_id`| `String`| -  
Session ID| `rl_session_id`| `NSNumber`  
UInt64| If not present, there is no active session in the legacy SDK  
Manual session status| `rl_session_manual_track_status`| `NSNumber`  
Boolean| Indicates whether automatic session tracking is enabled  
Last event timestamp| `rl_last_event_time_stamp`| `NSNumber`  
Double| Timestamp of the most recent event recorded by the SDK  
App version number| `rs_application_version_key`| `String`| `CFBundleShortVersionString` value from `info.plist`  
App build number| `rs_application_build_key`| `String`| `CFBundleVersion` value from `info.plist`  
  
> ![warning](/docs/images/warning.svg)
> 
> **Data availability**
> 
> These values are available only if the legacy SDK based app was not removed **before** installing the app version integrated with the iOS (Swift) SDK.

## Step 2: Migration

Follow these steps to migrate the existing values:

  1. Retrieve values from the legacy storage location.
  2. Transform values as needed — see the Storage key mapping table below.
  3. Save values to the iOS (Swift) SDK-specific `UserDefaults` suite.
  4. Initialize the iOS (Swift) SDK.


### Storage key mapping

After retrieving the legacy values, store each value in the iOS (Swift) SDK’s `UserDefaults` instance using its corresponding key:

Field| Legacy key| iOS (Swift) SDK key| Transformation notes  
---|---|---|---  
Anonymous ID| -| `anonymous_id`| Migrates the current device’s `identifierForVendor`  
User ID| `rs_user_id`| `user_id`| Extract the `userId` value from the traits JSON string  
Traits| `rs_traits`| `traits`| Store as JSON string; remove `anonymousId`, `id` and `userId` if present in the retrieved value  
Session ID| `rl_session_id`| `session_id`| Converts the value to String format  
Automatic session status| `rl_session_manual_track_status`| `is_manual_session`| Stores the **inverted** (toggled) Boolean value  
Last activity time| `rl_last_event_time_stamp`| `last_activity_time`| Requires timestamp conversion — see Timestamp conversion section below  
External ID| `rl_external_id`| -| No need to migrate as the iOS (Swift) SDK does not persist external IDs  
Application version number| `rs_application_version_key`| `rudder.app_version`| The `CFBundleShortVersionString` value from `info.plist` will be migrated as a `String`  
Application build number| `rs_application_build_key`| `rudder.app_build`| The `CFBundleVersion` value from `info.plist` will be migrated as an `Int`  
  
### Timestamp conversion

The legacy SDK and iOS (Swift) SDK use different time reference systems for tracking the last activity time:

SDK| Time reference  
---|---  
Legacy iOS v2 SDK| Absolute timestamp (Unix epoch time) in seconds  
iOS (Swift) SDK| Absolute timestamp (Unix epoch time) in milliseconds  
  
#### How to convert the legacy timestamp to the iOS (Swift) SDK format

  1. Read the legacy timestamp (`legacyTimestamp`, in seconds).
  2. Validate the timestamp — it must be greater than 0 and not a future timestamp.
  3. Convert to milliseconds:


    
    
    lastActivityTime = legacyTimestamp * 1000
    

> ![info](/docs/images/info.svg)
> 
> **Edge case**
> 
> If the legacy timestamp is invalid (zero, negative, or a future timestamp), then conversion is not possible. In such cases, skip migrating the last activity time.

## Migration helper class

RudderStack provides a persistence migration helper class — [PersistentMigratorFromV2](<https://github.com/rudderlabs/rudder-sdk-swift/blob/develop/Examples/SwiftUIExample/SwiftUIExample/PersistenceMigrator/FromV2/PersistentMigratorFromV2.swift>) — to help you migrate persisted values from earlier versions of the iOS (Swift) SDK.

Note that:

  * The migrator is **optional** and intended to be used as a reference implementation.
  * You can selectively rely on it based on the values you need to migrate.
  * Make sure this step runs only once during app startup, before the SDK initialization.
  * Alternatively, you can call `readPersistence()` to inspect the available values before performing the migration.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use this helper if you are upgrading from the legacy iOS SDK v2 and want to restore persisted values before initializing the iOS (Swift) SDK.

#### Usage

Initialize the migrator and call `restorePersistence()` **before** initializing the iOS (Swift) SDK:
    
    
    PersistentMigratorFromV2(writeKey: "swift-sdk-write-key").restorePersistence()
    

## Troubleshooting

Issue| Possible cause| Solution  
---|---|---  
Legacy data not found| The app was uninstalled before migration| No migration needed — the iOS (Swift) SDK will generate new values automatically  
Timestamp conversion fails| The device was rebooted after the last legacy SDK event| Skip last activity time migration — the session will reset naturally  
Traits parsing fails| Corrupted or invalid JSON in legacy storage| Log the error and skip traits migration — other values can still be migrated  
User ID not found in traits| User was never identified in the legacy SDK| No action needed — `userId` will remain `nil` until the user is identified