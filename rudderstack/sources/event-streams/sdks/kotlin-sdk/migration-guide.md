# Android (Java) to Android (Kotlin) SDK Migration Guide

Learn how to migrate persisted SDK data from the legacy Android (Java) SDK to the Android (Kotlin) SDK.

* * *

  * __6 minute read

  * 


This guide walks you through migrating persisted SDK state data from the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. to the Android (Kotlin) SDK to maintain continuity of user identity, session tracking, and app info across SDK versions.

## Pre-migration considerations

You can migrate the following data from the legacy Android (Java) SDK to the Android (Kotlin) SDK:

  * `anonymousId`
  * `userId`
  * `traits`
  * `sessionId`
  * `lastActivityTime`
  * App version
  * App build
  * Manual session tracking status


Also, note that:

  * Events are not migrated in this process
  * The Android (Kotlin) SDK does not persist external IDs, so you do not need to migrate them
  * Opt status, opt in time, and opt out time are not supported in the Android (Kotlin) SDK
  * The Android (Kotlin) SDK does not persist the advertising ID — use a custom [AndroidAdvertisingId Plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/AndroidAdvertisingIdPlugin.kt>) instead
  * The Android (Kotlin) SDK manages server config independently, so you do not need to migrate the server config last update value


## Migration process overview

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You must run the migration **before** initializing the Android (Kotlin) SDK. The SDK reads persisted values on initialization, so migrated data must already be in place.
>   * Configure the migration code so that it runs **only once**.
> 


  1. Understand how storage works in the legacy Android (Java) SDK.
  2. Run pre-flight checks to verify that the migration is possible.
  3. Migrate the data from the legacy SDK to the Android (Kotlin) SDK (see the mapping table below).
  4. Write the migrated data to the Android (Kotlin) SDK’s `SharedPreferences` file.
  5. **Optional but recommended** : Clean up the legacy storage.
  6. Initialize the Android (Kotlin) SDK.


## Step 1: Understand legacy SDK storage

The legacy Android (Java) SDK and the Android (Kotlin) SDK store data in different `SharedPreferences` files:

SDK| `SharedPreferences` file  
---|---  
Legacy Android (Java) SDK| `rl_prefs`  
Android (Kotlin) SDK| `rl_prefs-{writeKey}`  
  


> ![info](/docs/images/info.svg)The Android (Kotlin) SDK scopes storage by write key.  
  
> ![warning](/docs/images/warning.svg)
> 
> **Data availability**
> 
> These values are available only if the legacy SDK-based app was not removed **before** installing the app version integrated with the Android (Kotlin) SDK.

## Step 2: Run pre-flight checks

The `runPreflightChecks()` method validates the following before the migration:

Aspect| Description  
---|---  
Legacy file exists| The `rl_prefs` `SharedPreferences` file must exist.  
Legacy storage has data| The file must contain at least one value.  
New storage doesn’t exist| Prevents accidentally overwriting existing data.  
      
    
    val migration = Migration(context = this, writeKey = writeKey)
    
    val canProceed = migration.runPreflightChecks()
    if (!canProceed) {
        Log.w("Migration", "Pre-flight checks failed - skipping migration")
        return
    }
    

> ![info](/docs/images/info.svg)
> 
> If any check fails, the method returns `false` and you should skip the migration.

## Step 3: Migrate the data

Follow these steps to migrate the existing values:

  1. Extract values from the legacy `SharedPreferences` storage.
  2. Transform values as needed — see the Storage key mapping table below.
  3. Write values to the Android (Kotlin) SDK’s `SharedPreferences` file.


    
    
    // Extract data from legacy storage
    val legacyData = migration.extract()
    Log.d("Migration", "Extracted: $legacyData")
    
    // Transform to new format
    val transformedData = migration.transform(legacyData)
    Log.d("Transformation", "Transformed: $transformedData")
    
    // Write to new storage
    val writeSuccess = migration.write(transformedData)
    if (!writeSuccess) {
        Log.e("Migration", "Failed to write migrated data")
        return
    }
    

#### Storage key mapping

After retrieving the values from the legacy storage, store each value using its corresponding Android (Kotlin) SDK key:

Field| Legacy Android (Java) SDK key| Android (Kotlin) SDK key| Transformation notes  
---|---|---|---  
Anonymous ID| `rl_anonymous_id_key`| `anonymous_id`| No transformation required  
User ID| `rl_traits`| `user_id`| Extract the `id` or `userId` value from the traits JSON string  
Traits| `rl_traits`| `traits`| 

  * Store as JSON string.
  * Remove `id`, `userId`, and `anonymousId` if present.

  
Session ID| `rl_session_id_key`| `session_id`| No transformation required  
Last Activity Time| `rl_last_event_timestamp_key`| `last_activity_time`| No transformation required  
App Version| `rl_application_version_key`| `rudder.app_version`| No transformation required  
App Build| `rl_application_build_key` or `rl_application_info_key`| `rudder.app_build`| 

  * Convert from `Int` to `Long`.
  * Check `rl_application_build_key` first (SDK v1.5.2+), fallback to `rl_application_info_key` (SDK v1.5.1 and earlier)

  
Manual session tracking status| `rl_auto_session_tracking_status_key`| `is_session_manual`| Store the **inverted** boolean value  
External ID| `rl_external_id`| -| Migration not required  
  
Android (Kotlin) SDK does not persist external IDs  
Opt Status| `rl_opt_status`| -| Not supported  
Opt In Time| `rl_opt_in_time`| -| Not supported  
Opt Out Time| `rl_opt_out_time`| -| Not supported  
Advertising ID| `rl_advertising_id_key`| -| Do not migrate  
  
Android (Kotlin) SDK does not persist advertising ID. Use a custom [AndroidAdvertisingId Plugin](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/customplugins/AndroidAdvertisingIdPlugin.kt>) instead  
Server Config Last Update| `rl_server_last_updated`| -| Migration not required  
  
Android (Kotlin) SDK manages server config independently  
  
## Step 4: Clean up legacy storage

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Cleanup is optional but recommended after a successful migration.

After a successful write, clean up the legacy storage:
    
    
    migration.cleanup()
    

## Step 5: Initialize the Android (Kotlin) SDK

After completing the migration, you can safely initialize the Android (Kotlin) SDK. The SDK reads the migrated values from `SharedPreferences` on initialization.

## Complete example

The following example shows the complete migration flow in `Application.onCreate()`, **before** SDK initialization:
    
    
    // In Application.onCreate(), BEFORE SDK initialization
    class MyApplication : Application() {
        override fun onCreate() {
            super.onCreate()
    
            val writeKey = "YOUR_NEW_SDK_WRITE_KEY"
    
            Migration(context = this, writeKey = writeKey).run {
                if (!runPreflightChecks()) return@run
    
                extract()
                    .let(::transform)
                    .let(::write)
                    .also { success -> if (success) cleanup() }
            }
    
            // NOW safe to initialize the SDK
            initializeRudderSDK()
        }
    }
    

## Selective migration

You can migrate only specific values by passing a set of `MigratableValue` options to the `extract()` method:
    
    
    val legacyData = migration.extract(
        values = setOf(
            MigratableValue.ANONYMOUS_ID,
            MigratableValue.USER_ID,
            MigratableValue.TRAITS
        )
    )
    

The available `MigratableValue` options are:

  * `ANONYMOUS_ID`
  * `USER_ID`
  * `TRAITS`
  * `SESSION_ID`
  * `LAST_ACTIVITY_TIME`
  * `APP_VERSION`
  * `APP_BUILD`
  * `IS_SESSION_MANUAL`
  * `ALL` (automatically includes all of the above)


## Migration helper class

RudderStack provides a migration helper class — [Migration](<https://github.com/rudderlabs/rudder-sdk-kotlin/blob/develop/app/src/main/java/com/rudderstack/sampleapp/analytics/migration/Migration.kt>) — in the sample app to help you migrate persisted values from the legacy Android (Java) SDK.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use this helper if you are upgrading from the legacy Android (Java) SDK and want to restore persisted values before initializing the Android (Kotlin) SDK.

Note that:

  * Use the Android (Kotlin) SDK’s write key (not the legacy Android (Java) SDK’s write key).
  * Handle device reboots gracefully — the session resets naturally.


## Migrate integration SDKs

When migrating from legacy Android (Java) integration SDKs to Android (Kotlin) integration SDKs, the destination SDK (Braze, Adjust, AppsFlyer, etc.) handles its own data migration. The RudderStack migration process only migrates RudderStack SDK state data, not destination SDK data.

RudderStack recommends the following:

  * **Check destination SDK migration documentation** : Each destination SDK may have its own migration requirements when upgrading versions. Refer to the official documentation for Braze, Adjust, AppsFlyer, Facebook, and Firebase for version-specific migration steps.
  * **The destination SDK manages its own data** : The RudderStack migration process does not touch destination SDK data stored on the device. This data is managed entirely by the destination SDKs themselves.


> ![danger](/docs/images/danger.svg)
> 
> If you are running both the legacy Android (Java) SDK and the Android (Kotlin) SDK simultaneously (during a gradual rollout), configure each integration in only **one** of the SDKs.
> 
> Having the same integration active in both SDKs can lead to unpredictable behavior.

## Troubleshooting

Issue| Possible cause| Solution  
---|---|---  
Legacy data not found| App was uninstalled before migration| No migration needed — the Android (Kotlin) SDK generates new values automatically  
Pre-flight checks fail| Android (Kotlin) SDK was already initialized| Ensure migration runs before initializing the Android (Kotlin) SDK  
Traits parsing fails| Corrupted or invalid JSON in legacy storage| Skip traits migration and make a new `identify` call to restore user traits  
User ID not found in traits| User was never identified in the legacy SDK| No action needed — `userId` will remain null until the user is identified