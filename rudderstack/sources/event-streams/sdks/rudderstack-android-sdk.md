# RudderStack Android (Java) SDK

Use RudderStack’s Android (Java) SDK using Android Studio to send events from your Android device to various destinations.

* * *

  * __29 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Android (Java) SDK is legacy and will be deprecated soon.**
> 
>   * For new implementations, RudderStack recommends using the [Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) instead.
>   * If you are planning to migrate your existing implementation from the Android (Java) SDK to the Android (Kotlin) SDK, see the [Breaking Changes in Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/breaking-changes/>) first.
> 


With RudderStack’s Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. , you can track events from your Android applications and send them to your specified destinations.

See the [GitHub codebase](<https://github.com/rudderlabs/rudder-sdk-android>) for more information on the SDK and its architecture.

[![Github Badge](https://img.shields.io/maven-central/v/com.rudderstack.android.sdk/core?style=flat)](<https://central.sonatype.com/artifact/com.rudderstack.android.sdk/core>)

## SDK setup requirements

  * [Android Studio](<https://developer.android.com/studio>) installed on your system.
  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up an Android source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the RudderStack dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> In the dashboard, the **Setup** tab for the source has an SDK installation snippet containing both the write key and the data plane URL. You can use it to integrate the Android (Java) SDK into your project.

## Installing the SDK

> ![info](/docs/images/info.svg)
> 
> As Bintray has sunset from 1st May, we’re moving the Android (Java) SDK to Maven Central. All the versions from 1.0.10 are available in Maven Central only.

We distribute the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. through [Maven Central](<https://search.maven.org>). The recommended and easiest way to add the SDK to your project is through the Android Gradle build system.

Follow these steps:

  * Open your project level `build.gradle` file, and add the following lines of code:


    
    
    buildscript {
        repositories {
            mavenCentral()
        }
    }
    allprojects {
        repositories {
            mavenCentral()
        }
    }
    

  * Then open your `app/build.gradle` and add the dependency under `dependencies` as shown below:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.7+'
    // add the following line if you don't have Gson included already
    implementation 'com.google.code.gson:gson:2+'
    

> ![info](/docs/images/info.svg)
> 
> It is recommended to use the core Android (Java) SDK without any `device-mode` destination SDKs as you will have a better view on the captured data from the SDK.

## Setting Android permissions

Add this line to your `AndroidManifest.xml` file of your application for `internet` permission:
    
    
    <uses-permission android:name="android.permission.INTERNET"/>
    

We also declare `android.permission.BLUETOOTH` and `android.permission.ACCESS_WIFI_STATE` as optional by mentioning `required="false"` . If we get these permissions, we’ll capture the Bluetooth status and the WiFi status of the device and pass it under `context.network`.

### Android ProGuard rules

Add the following lines to your Android ProGuard rules if you are using Proguard full mode to optimize your app:

> ![info](/docs/images/info.svg)
> 
> Add the below rules if you are using the Android (Java) SDK older than v1.20.0.
> 
> Note that the rules are bundled in the SDK itself from v1.20.0 onwards.
    
    
    // Reporter Module
    
    -keep class com.rudderstack.android.ruddermetricsreporterandroid.models.LabelEntity { *; }
    -keep class com.rudderstack.android.ruddermetricsreporterandroid.models.MetricEntity { *; }
    -keep class com.rudderstack.android.ruddermetricsreporterandroid.models.ErrorEntity { *; }
    
    // Required for the usage off TypeToken class in Utils.converToMap, Utils.convertToList
    
    -keep class com.google.gson.reflect.TypeToken { *; }
    -keep class * extends com.google.gson.reflect.TypeToken
    
    // Required for the serialization of SourceConfig once it is downloaded.
    
    -keep class com.google.gson.internal.LinkedTreeMap { *; }
    -keep class * implements java.io.Serializable { *; }
    -keep class com.rudderstack.rudderjsonadapter.RudderTypeAdapter { *; }
    -keep class * extends com.rudderstack.rudderjsonadapter.RudderTypeAdapter
    
    // Required to ensure the DefaultPersistenceProviderFactory is not removed by Proguard
    // and works as expected even when the customer is not using encryption feature.
    
    -dontwarn net.sqlcipher.Cursor
    -dontwarn net.sqlcipher.database.SQLiteDatabase$CursorFactory
    -dontwarn net.sqlcipher.database.SQLiteDatabase
    -dontwarn net.sqlcipher.database.SQLiteOpenHelper
    -keep class com.rudderstack.android.sdk.core.persistence.DefaultPersistenceProviderFactory { *; }
    
    // Required for the usage of annotations across reporter and web modules
    
    -dontwarn com.fasterxml.jackson.annotation.JsonIgnore
    -dontwarn com.squareup.moshi.Json
    -dontwarn com.fasterxml.jackson.annotation.JsonProperty
    
    // Required for Device Mode Transformations
    
    -keep class com.rudderstack.android.sdk.core.TransformationResponse { *; }
    -keep class com.rudderstack.android.sdk.core.TransformationResponseDeserializer { *; }
    -keep class com.rudderstack.android.sdk.core.TransformationRequest { *; }
    

## Initializing the RudderStack client

Import the library on the classes you desire to use `RudderClient` library
    
    
    import com.rudderstack.android.sdk.core.*;
    

Add the following code to the `onCreate` method in your `Application` class:
    
    
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withTrackLifecycleEvents(true)
                .withRecordScreenViews(true)
                .build()
        )
    
    
    
    RudderClient rudderClient = RudderClient.getInstance(
            this,
            WRITE_KEY,
            new RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withTrackLifecycleEvents(true)
                    .withRecordScreenViews(true)
                    .build()
    );
    

> ![info](/docs/images/info.svg)
> 
>   * See Configuring your RudderStack client for more information on the methods supported by the `RudderConfig` object.
>   * See [Adding an application class to your Android application](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/adding-an-application-class/>) for more information.
> 


#### OneTrust consent

The Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. integrates with the OneTrust consent manager and lets you specify the user’s consent during initialization. For more information, refer to the [OneTrust Consent Management for Android](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/android/>) guide.

## Configuring your RudderStack client

You can configure your client based on the following methods using `RudderConfig.Builder`:

Method| Type| Description  
---|---|---  
`withLogLevel`| Integer| Controls the log details you want to capture using the SDK.  
  
**Default value** : `RudderLogger.RudderLogLevel.NONE`  
`withDataPlaneUrl`| String| Your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>)  
`withDbThresholdCount`| Integer| Number of events to be saved in the `SQLite` database. Once the limit is reached, older events are deleted from the database.  
  
**Default value** : `10000`  
`withSleepcount`| Integer| Minimum waiting time to flush the events to the RudderStack server. The minimum value can be set to `1 second`.  
  
**Default value** : `10 seconds`  
`withEventDispatchSleepInterval`| Integer| Duration (in seconds) for which the event dispatch thread sleeps when the SDK has no events to send to RudderStack. This value should be less than or equal to the value set using `withSleepCount`.  
  
**Default value** : `1 second`  
`withConfigRefreshInterval`| Integer| Time after which the SDK fetches the config from the dashboard.  
  
**Default value** : `2 hours`  
`withTrackLifecycleEvents`| Boolean| Determines if the SDK should automatically capture application lifecycle events using the activity lifecycle callbacks.  
  
**Default value** : `true`  
`withNewLifecycleEvents`| Boolean| Determines if the SDK should automatically capture application lifecycle events using AndroidX’s `LifecycleObserver` class. See Tracking events with AndroidX `LifecycleObserver` for more information.  
  
**Default value** : `false`  
`withTrackDeepLinks`| Boolean| Determines if the SDK should send the deep link-specific details as a `Deep Link Opened` event. See Tracking deep links for more information.  
  
**Default value** : `true`  
`withAutoSessionTracking`| Boolean| Determines if the SDK should automatically track the user sessions.  
  
**Default value** : `true`  
`withSessionTimeoutMillis`| Integer| Maximum inactivity period before the session expires.  
  
**Default value** : `300000 ms` (5 minutes)  
`withRecordScreenViews`| Boolean| Determines if the SDK should automatically capture the screen view events.  
  
**Default value** : `false`  
`withGzip`| Boolean| Gzips the event requests.  
  
**Default value** : `true`  
`withCollectDeviceId`| Boolean| Determines if the SDK should automatically collect the device ID. If set to `false`, it does not send `context.device.id` as a part of the event payload. See Disabling device ID collection for more information.  
  
**Default value** : `true`  
`withAutoCollectAdvertId`| Boolean| Determines if the SDK should automatically collect the advertisement ID.  
  
**Default value** : `false`  
`withDbEncryption`| `DbEncryption`| Specify whether to encrypt/decrypt the database using your desired key.  
`withFlushPeriodically`| Integer| [Periodically flushes events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/flushing-events-periodically/>) from the Android (Java) SDK to RudderStack irrespective of whether your app is open.  
  
**Default value** : `15 minutes`  
`withCustomFactories`| `List<RudderIntegration.Factory>`| Used for the customized extension of `RudderIntegration.Factory` while [adding your device mode destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#developing-a-device-mode-destination>).  
`withFactory`| `<RudderIntegration.Factory>`| Adds the available device mode destination. Refer to the destination-specific documentation for the usage details. For example, [Firebase](<https://www.rudderstack.com/docs/destinations/streaming-destinations/firebase/#adding-device-mode-integration>).  
`withFactories`| `List<RudderIntegration.Factory>`| Adds a list of factories for the available device mode destinations.  
`withFlushQueueSize`| Integer| Number of events in a batch request to the RudderStack server.  
  
**Default value** : `30`  
`withControlPlaneUrl`| String| Adds `/sourceConfig` along with this URL to fetch the source configuration. Change this parameter **only if** you are self-hosting the control plane.  
  
**Default value** : `https://api.rudderlabs.com`  
  
A sample code snippet to configure your client using `RudderConfig.Builder` is shown below:
    
    
    rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withSleepCount(1)
                .withLogLevel(RudderLogger.RudderLogLevel.VERBOSE)
                .build()
        )
    

#### DbEncryption

> ![info](/docs/images/info.svg)
> 
> This feature is available in the Android (Java) SDK v1.18.0. and later.

The Android (Java) SDK uses a SQLite database to store events before sending them to the RudderStack data plane.

You can use the `DbEncryption` object to encrypt/decrypt a new or existing database with your specified key.

##### Add dependencies

Since the Android (Java) SDK depends on the SQLite Cipher library, you need to add [`sqlcipher-android`](<https://github.com/sqlcipher/sqlcipher-android>) as a dependency:

  1. Add the RudderStack Android (Java) SDK as a dependency.
  2. Go to the module level `build.gradle` file an add the following under the `dependencies` section:


    
    
    dependencies {
       ...
        //sql-cipher
        implementation "net.zetetic:sqlcipher-android:4.5.6@aar"
        implementation "androidx.sqlite:sqlite:2.3.1"
        ...
    }
    

##### Set the encryption object

To encrypt/decrypt databases, create and set the `DbEncrpytion` object while initializing the Android (Java) SDK as follows:
    
    
    rudderClient = RudderClient.getInstance(
        this,
        WRITE_KEY,RudderConfig.Builder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withControlPlaneUrl(BuildConfig.CONTROL_PLANE_URL)
        .withLogLevel(RudderLogger.RudderLogLevel.ERROR)
        .withFactory(AmplitudeIntegrationFactory.FACTORY)
    	  ...
        .withDbEncryption(RudderConfig.DBEncryption(true, "<your-encryption-key>")) // Configure encryption key
        .build()
    )
    

The `withDbEncryption` method accepts a `DbEncryption` object with the following parameters:

Parameter| Data type| Description  
---|---|---  
`true`/`false`| Boolean| Specifies whether to encrypt an unencrypted database or decrypt an encrypted database.  
`key`| String| Key used to encrypt/decrypt the database.  
  
> ![warning](/docs/images/warning.svg)
> 
> After you encrypt the database:
> 
>   * If **no key** is provided, then the SDK deletes the current database with unsent events and creates a new unencrypted database instead.
>   * If a **wrong key** is provided, then the SDK deletes the current database with unsent events and creates a new encrypted database with the given key.
> 

> 
> The SDK does not store the key, so it cannot determine whether the entered key is right or wrong. Hence, if the key cannot decrypt the database, the SDK assumes it to be incorrect and deletes the old events and database.

#### Self-hosted control plane

If you are using a device mode destination like Adjust, Firebase, etc., the Android (Java) SDK needs to fetch the required configuration from the Control Plane. If you are using the [Control plane lite](<https://github.com/rudderlabs/config-generator#rudderstack-control-plane-lite>) utility to host your own Control Plane, then follow the steps in [this section](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#using-sdk-sources-set-up-in-self-hosted-control-plane>) and specify `controlPlaneUrl` in your`RudderConfig.Builder` that points to your hosted source configuration file.

> ![warning](/docs/images/warning.svg)
> 
> You shouldn’t pass the `controlPlaneUrl` parameter during SDK initialization if you are using the dashboard from [RudderStack Cloud Dashboard](<https://app.rudderstack.com>). This parameter is supported only if you are using our open-source [Control plane lite](<https://github.com/rudderlabs/config-generator#rudderstack-control-plane-lite>) to self-host your Control Plane.

## Gzipping requests

> ![success](/docs/images/tick.svg)
> 
> The Gzip feature is enabled by default in the Android (Java) SDK.

The Android (Java) SDK automatically gzip-compresses event requests. To disable this feature, set the `Gzip` parameter to `false` while initializing the SDK:
    
    
    RudderClient.getInstance(
        this,
        WRITE_KEY,
        RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .withGzip(false)
            .build()
    )
    
    
    
    RudderClient rudderClient = RudderClient.getInstance(
            this,
            WRITE_KEY,
            new RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withTrackLifecycleEvents(true)
                    .withGzip(false)
                    .withRecordScreenViews(true)
                    .build()
    );
    

> ![warning](/docs/images/warning.svg)
> 
> Gzip requires [rudder-server](<https://github.com/rudderlabs/rudder-server>) **v1.4 or higher**. Otherwise, your events might fail.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc. Once you identify the user, the SDK persists all the user information and passes it on to the subsequent `track` or `screen` calls. To reset the user identification, you can use the `reset` method.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * For older SDK versions (< v1.18.0), the Android (Java) SDK captures the device ID and uses that as `anonymousId` for identifying the user. This helps the SDK to track the users across the application installation.
>   * On Android devices, the `deviceId` is assigned during the first boot. It remains consistent across the applications and installs and changes only after factory reset.
>   * Starting from v1.18.0, the Android (Java) SDK uses a UUID as `anonymousId` instead of the device ID. If you are upgrading from a previous SDK version, see How RudderStack sets anonymous ID for more information on how the SDK collects and sets `anonymousId`.
> 


An sample `identify` event is as shown:
    
    
    val traits = RudderTraits()
    traits.putBirthday(Date())
    traits.putEmail("abc@123.com")
    traits.putFirstName("First")
    traits.putLastName("Last")
    traits.putGender("m")
    traits.putPhone("5555555555")
    val address = RudderTraits.Address()
    address.putCity("City")
    address.putCountry("USA")
    traits.putAddress(address)
    traits.put("boolean", Boolean.TRUE)
    traits.put("integer", 50)
    traits.put("float", 120.4f)
    traits.put("long", 1234L)
    traits.put("string", "hello")
    traits.put("date", Date(System.currentTimeMillis()))
    rudderClient.identify("test_user_id", traits, null)
    
    
    
    RudderTraits traits = new RudderTraits();
    traits.putBirthday(new Date());
    traits.putEmail("abc@123.com");
    traits.putFirstName("First");
    traits.putLastName("Last");
    traits.putGender("m");
    traits.putPhone("5555555555");
    RudderTraits.Address address = new RudderTraits.Address();
    address.putCity("City");
    address.putCountry("USA");
    traits.putAddress(address);
    traits.put("boolean", Boolean.TRUE);
    traits.put("integer", 50);
    traits.put("float", 120.4f);
    traits.put("long", 1234L);
    traits.put("string", "hello");
    traits.put("date", new Date(System.currentTimeMillis()));
    rudderClient.identify("test_user_id", traits, null);
    

Follow the method signatures below:

Name| Data Type| Required| Description  
---|---|---|---  
`traits`| `RudderTraits`| Yes| Traits information for the user  
`options`| `RudderOption`| No| Extra options for the `identify` event  
  
**OR**

Name| Data Type| Required| Description  
---|---|---|---  
`userId`| `String`| Yes| Developer identity for the user  
`traits`| `RudderTraits`| No| Traits information for user  
`option`| `RudderOption`| No| Extra options for the `identify` event  
  
### Overriding anonymous ID

You can use the following method to use your own `anonymousId` with the SDK.

An example of setting the `anonymousId` is shown below:
    
    
    RudderClient.putAnonymousId(<anonymousId>);
    

To retrieve the `anonymousId`, you can use the `anonymousId` instance property:
    
    
    RudderClient.getInstance()?.anonymousId
    

### Disabling device ID collection

Starting from v1.18.0, you can disable the collection of device ID by setting the `withCollectDeviceId` API of the `RudderConfigBuilder` class to `false`.

You will observe the following changes when this API is set to false:

  * The SDK does not send `context.device.id` as a part of the event payload.
  * The SDK replaces the existing `anonymousId` (if it is equal to the device ID) with a UUID.


> ![info](/docs/images/info.svg)
> 
> These changes are introduced to make the SDK more compliant with all policies around the device ID collection.
    
    
    RudderClient rudderClient = RudderClient.getInstance(
            this,
            WRITE_KEY,
            new RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withCollectDeviceId(false)
                    .build()
    );
    

> ![warning](/docs/images/warning.svg)
> 
> If you are upgrading to the latest SDK from a previous version (< v1.18.0) **and** disabling device ID collection using `withCollectDeviceId(false)`:
> 
>   * Make sure your user transformations are not dependent on `context.device.id` as the SDK will not send this value in the event payload.
>   * The `context.device.id` column in your warehouse destination will not be populated henceforth (it will still contain data populated by the previous SDK version).
> 


### How SDK sets anonymous ID

#### **For direct/fresh SDK installation**

For a fresh installation of the Android (Java) SDK v1.18.0 and later, RudderStack uses UUID as `anonymousId` regardless of whether `withCollectDeviceId` is set to `true` or `false`.

#### **For updating SDK from older version**

If you are updating your Android (Java)SDK from an older version (< v1.18.0), then:

  * RudderStack will continue to use the device ID as `anonymousId` \- it will not break the existing SDK behavior **until** you set `withCollectDeviceId` to `false`.
  * If you set `withCollectDeviceId` to `false`, the SDK checks if the existing `anonymousId` is a device ID. If yes, it sets a new UUID as the `anonymousId`.
  * If you have used the `putAnonymousId` method to set your own `anonymousId`, then the SDK will **not** modify it even if you set `withCollectDeviceId` to `false`.


### Setting a custom ID

You can pass a custom ID along with the standard `userId` in your `identify` calls. RudderStack adds this value under `context.externalId`.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports passing `externalId` only in the `identify` events. You must not pass this ID in other API calls like `track`, `page`, etc.

The following snippet shows how to add an `externalId` to your `identify` event:
    
    
    rudderClient.identify(
        "1hKOmRA4GRlm",
        RudderTraits().putFirstName("Alex"),
        RudderOption()
            .putExternalId("brazeExternalId", "some_external_id")
    )
    

## Track

You can record the users’ activity through the `track` method. Every user action is called an **event**.

A sample `track` event is as shown below:
    
    
    rudderClient.track(
        "Product Added",
        RudderProperty().putValue("product_id", "product_001")
    )
    
    
    
    rudderClient.track(
            "Product Added",
            new RudderProperty()
                    .putValue("product_id", "product_001")
    );
    

Follow the method signatures below:

Name| Data Type| Required| Description  
---|---|---|---  
`name`| `String`| Yes| Name of the event you want to track  
`property`| `RudderProperty` or `Map<String, Object>`| No| Extra data properties you want to send along with the event  
`options`| `RudderOption`| No| Extra event options  
  
## Screen

You can use the `screen` call to record whenever the user sees a screen on the mobile device. You can also send some extra properties along with this event.

An example of the `screen` event is as shown:
    
    
    rudderClient.screen(
        "MainActivity",
        "HomeScreen",
        RudderProperty().putValue("foo", "bar"),
        null
    )
    
    
    
    rudderClient.screen(
        "MainActivity",
        "HomeScreen",
        new RudderProperty().putValue("foo", "bar"),
        null
    );
    

Follow the method signatures below:

Name| Data Type| Required| Description  
---|---|---|---  
`screenName`| `String`| Yes| Name of the screen viewed.  
`category`| `String`| No| Category of the screen visited, such as `HomeScreen`, `LoginScreen`. Useful for tracking multiple `Fragment` views under a single `Activity`.  
`property`| `RudderProperty`| No| Extra property object that you want to pass along with the `screen` call.  
`option`| `RudderOption`| No| Extra options to be passed along with `screen` event.  
  
## Group

The `group` call associates a user to a specific organization. A sample `group` call for the API is below:
    
    
    rudderClient.group(
        "sample_group_id",
        RudderTraits().putAge("24")
            .putName("Test Group Name")
            .putPhone("1234567891")
    )
    
    
    
        rudderClient.group(
            "sample_group_id",
            new RudderTraits().putAge("24")
                .putName("Test Group Name")
                .putPhone("1234567891")
        );
    

Follow the method signatures below:

Name| Data Type| Required| Description  
---|---|---|---  
`groupId`| `String`| Yes| An ID of the organization with which you want to associate your user  
`traits`| `RudderTraits`| No| Any other property of the organization you want to pass along with the call  
`options`| `RudderOption`| No| Event level options  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack doesn’t persist the traits for the group across the sessions.

## Alias

The `alias` call lets you associate the user with a new identification.

> ![info](/docs/images/info.svg)
> 
> `alias` is an advanced API that lets you change the user identifier explicitly. It is useful when managing identities for some of the downstream destinations.

A sample `alias` call is shown:

RudderStack recommends using the default invocation in scenarios where you only want to replace the current `userId` with the new `userId`.

  * Specify only new user ID **without** previous user ID and event-level options:


    
    
    rudderClient?.alias("newId")
    
    
    
    rudderClient.alias("newId");
    

  * Specify new user ID and event-level options **without** previous user ID:


    
    
    rudderClient?.alias("newId", options)
    
    
    
    rudderClient.alias("newId", options);
    

In this case, the SDK automatically populates the `previousId` field with the previously-persisted `userId`/`anonymousId`.

RudderStack recommends using the following invocations in cases where you want to explicitly pass the previous user ID that may be required by some downstream destinations, for example, MoEngage.

  * Specify new user ID and previous user ID **with** event-level options:


    
    
    rudderClient?.alias("newId", "previousId", options)
    
    
    
    rudderClient.alias("Alias user Id", "Previous user Id", options);
    

  * Specify new user ID and previous user ID **without** event-level options:


    
    
    rudderClient?.alias("newId", "previousId")
    
    
    
    rudderClient.alias("newId", "previousId");
    

The following table highlights the supported `alias` API parameters:

Name| Data type| Description  
---|---|---  
`newId`  
Required| `String`| The new identifier (`userId`) to assign to the user.  
`previousId`| `String`| The old user identifier.  
  
Note that:

  * The Android (Java)SDK supports explicitly passing the `previousId` field from **v1.26.0** onwards.
  * If not provided explicitly, the SDK populates this field with the current `userId`/ `anonymousId`.

  
`options`| `RudderOption`| Event-level options.  
  
Once you make the `alias` call, RudderStack replaces the old `userId` with the new user identifier (`newId`) and persists that identification across the sessions.

## Reset

You can use the `reset` method to clear the persisted user traits. It also resets the `anonymousId` with a new UUID if you call it with `true` (for SDK v1.18.0 and later). To clear only user traits, call `reset` with `false`.

In [session tracking](<https://rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#:~:text=tracking%20is%20enabled%3A-,sessionId,-%28Number%29%3A%20The%20session>), calling the `reset` method clears the current `sessionId` and generates a new one.

A sample `reset` call is shown:
    
    
    rudderClient.reset(false)
    
    
    
    rudderClient.reset(false);
    

## Consent-driven user tracking (GDPR support)

RudderStack gives the users the ability to opt out of tracking any user activity until the user gives their consent. You can do this using the SDK’s `optOut` API.

The `optOut` API takes `true` or `false` as a Boolean value to enable or disable tracking user activities. This flag persists across device reboots.

The following snippet highlights the use of the `optOut` API to disable user tracking:
    
    
    rudderClient.optOut(true)
    
    
    
    rudderClient.optOut(true);
    

the user grants their consent, you can enable user tracking once again by using the `optOut` API with `false` as a parameter sent to it:
    
    
    rudderClient.optOut(false)
    
    
    
    rudderClient.optOut(false);
    

The `optOut` API is available in the Android (Java) SDK from v1.0.21 onwards.

## Setting the Android device token

You can set your `device-token` for push notification to be sent to the destinations that support Push Notification. We set the `token` under `context.device.token`.

Follow the code snippets below:
    
    
    RudderClient.putDeviceToken("your_device_token")
    
    
    
    RudderClient.putDeviceToken("your_device_token");
    

## Setting custom context

You can set custom contextual information in Android (Java) SDK by using either of the following ways:

### During SDK initialization

Set custom context during SDK initialization as follows:

> ![info](/docs/images/info.svg)
> 
> This feature is available in the Android (Java) SDK v1.22.0 and later.
    
    
    val rudderOption = RudderOption().putCustomContext(
            "tier", mutableMapOf(
                "category" to "premium",
                "type" to "gold"
            ) as Map<String, Any>
    )
    
    val rudderClient =
        RudderClient.getInstance(
                    this,
                    WRITE_KEY,
                    RudderConfig.Builder()
                        .withDataPlaneUrl(DATA_PLANE_URL)
                        .build(),
                    rudderOption
                )
    
    
    
    Map customContext = new HashMap<String, Object>();
    customContext.put("category", "premium");
    customContext.put("type", "gold");
    RudderOption rudderOption = new RudderOption();
    rudderOption.putCustomContext("tier", customContext);
    
    RudderClient rudderClient = RudderClient.getInstance(
            this,
            WRITE_KEY,
            new RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .build(),
            rudderOption
    );
    

Note that:

  * The Android (Java) SDK persists the contextual information set during SDK initialization for subsequent events but **not** across sessions.
  * Calling the `reset` method clears all the contextual information set during SDK initialization.
  * The contextual information passed at the event level gets precedence over the context set during SDK initialization.


### Using `putCustomContext` method

Use the `putCustomContext` method on an instance of `RudderOption` to set custom contextual information as a nested object within `context` while sending the events.

An example of setting custom context using an instance of `RudderOption` and passing it in a `track` call:
    
    
    RudderProperty properties = new RudderProperty();
    properties.put("paymentMethod", "credit card");
    Map customContext = new HashMap<String, Object>();
    customContext.put("category", "premium");
    customContext.put("type", "gold");
    RudderOption rudderOption = new RudderOption();
    rudderOption.putCustomContext("tier", customContext);
    RudderClient.with(this).track(
            "Subscription Purchased",
            properties,
            rudderOption
    );
    
    
    
    val properties = RudderProperty()
    properties.put("paymentMethod", "credit card")
    val rudderOption = RudderOption().putCustomContext(
            "tier", mutableMapOf(
                "category" to "premium",
                "type" to "gold"
            ) as Map<String, Any>
    )
    rudderClient.track(
            "Subscription Purchased",
            properties,
            rudderOption
    )
    

The `context` object in the created event payload looks like below:
    
    
    {
      "context": {
        "tier": {
          "category": "premium",
          "type": "gold",
        }
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> The SDK does not persist the contextual information set using `putCustomContext` for subsequent events. Hence, you must use this method every time you want to set custom context for an event.

## Setting the advertisement ID

By default, RudderStack collects the advertisement ID **only** if the following three conditions are met:

  * `withAutoCollectAdvertId` is set to `true` during the SDK initialization:


    
    
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withTrackLifecycleEvents(true)
                .withRecordScreenViews(true)
                .withAutoCollectAdvertId(true)
                .build()
        )
    

  * `com.google.android.gms.ads.identifier.AdvertisingIdClient` is present in your application’s class path.
  * `limitAdTracking`is not enabled for your device.


Use the `putAdvertisingId` method to set the advertisement ID:
    
    
    RudderClient.putAdvertisingId("sampleAdvertId")
    
    
    
    RudderClient.putAdvertisingId("advertId");
    

The `putAdvertisingId` method is static and can be called before or after the SDK initialization.

If `withAutoCollectAdvertId` is set to `true` and you set the advertisement ID value using `putAdvertisingId` method, RudderStack uses the value provided by the user instead of collecting it automatically.

Once you reset the advertisement ID using the `clearAdvertisingId` method, RudderStack starts auto-collecting the advertisement ID again.

To clear the advertisement ID, use the `clearAdvertisingId` method:
    
    
    rudderClient.clearAdvertisingId()
    ``
    
    
    
    RudderClient.with(this).clearAdvertisingId();
    

The `clearAdvertisingId` method is not static and hence can be called only after the SDK initialization.

RudderStack sets `gaid` under `context.device.advertisementId`.

## Filtering events

When sending events to a destination via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you can explicitly specify which events should be discarded or allowed to flow through - by allowlisting or denylisting them.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this feature.

## Enable/disable events for specific destinations

The RudderStack Android (Java) SDK allows you to enable or disable event flow to a specific destination or all destinations to which the source is connected. You can specify these destinations by creating a `RudderOption` object as shown:
    
    
    val option = RudderOption()
    //default value for `All` is true
    option.putIntegration("All", false)
    // specifying destination by its display name
    option.putIntegration("Google Analytics", true)
    option.putIntegration(<DESTINATION DISPLAY NAME>, <boolean>)
    // specifying destination by its Factory object
    option.putIntegration(AppcenterIntegrationFactory.FACTORY,true);
    option.putIntegration(<RudderIntegration.FACTORY>,<boolean>);
    
    
    
    RudderOption option = new RudderOption();
    // default value for `All` is true
    option.putIntegration("All", false);
    // specifying destination by its display name
    option.putIntegration("Google Analytics", true);
    option.putIntegration(<DESTINATION DISPLAY NAME>, <boolean>);
    // specifying destination by its Factory object
    option.putIntegration(AppcenterIntegrationFactory.FACTORY,true);
    option.putIntegration(<RudderIntegration.FACTORY>,<boolean>);
    

The keyword `All` in the above snippet represents all destinations the source is connected to. Its value is set to `true` by default.

> ![info](/docs/images/info.svg)
> 
> Make sure the `destination display name` that you pass while specifying the destinations should exactly match the destination name as shown [here](<https://app.rudderstack.com/directory>).

You can pass the destinations specified in the above snippet to the SDK in two ways:

#### 1\. While initializing the SDK

This is helpful when you want to enable/disable sending the events across all event calls made using the SDK to the specified destination(s).
    
    
    var rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .build(),
            // passing the rudderoption object containing
            // the list of destination(s) you specified
            option
        )
    
    
    
    RudderClient client = RudderClient.getInstance(
                    this,
                    <write_key>,
                    new RudderConfig.Builder()
                            .withEndPointUri(<end_point_url>)
                            .build(),
                    option // passing the rudderoption object containing the list of destination(s) you specified
            );
    

#### 2\. While sending events

This approach is helpful when you want to enable/disable sending only a particular event to the specified destination(s) or if you want to override the specified destinations passed with the SDK initialization for a particular event.
    
    
    rudderClient.track(
        "Product Added",
        RudderProperty().putValue("product_id", "product_001"),
        // passing the rudderoption object
        // containing the list of destination you specified
        option
    )
    
    
    
    rudderClient.track(
                    "Product Added",
                    new RudderProperty()
                            .putValue("product_id", "product_001"),
                    option // passing the rudderoption object containing the list of destination(s) you specified
            );
    

If you specify the destinations both while initializing the SDK as well as while making an event call, then the destinations specified at the event level only will be considered.

## Tracking user sessions

By default, the Android (Java) SDK automatically tracks the user sessions. This means that RudderStack automatically determines the start and end of a user session depending on the inactivity time configured in the SDK (default time is 5 minutes).

> ![warning](/docs/images/warning.svg)
> 
> To automatically track sessions in the Android (Java) SDK, `withTrackLifecycleEvents` should also be set to true. This is because RudderStack considers the [Application Opened](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>), [Application Installed](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>), or [Application Updated](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>) events as the start of a new session.
    
    
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                // Set to false to disable automatic session tracking
                .withAutoSessionTracking(true)
                .withSessionTimeoutMillis(5 * 60 * 1000)
                .build()
        )
    
    
    
    RudderClient rudderClient = RudderClient.getInstance(
        this,
        WRITE_KEY,
        new RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .withAutoSessionTracking(true) // Set to false to disable automatic session tracking
            .withSessionTimeoutMillis(5*60*1000)
            .build()
    );
    

To disable automatic session tracking, set `withAutoSessionTracking` to `false`.

For more information on the user sessions and how to track them using the Android (Java) SDK, see [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/>).

### Getting the session ID

To retrieve a session’s `sessionId`, use the `getSessionId()` method.

> ![info](/docs/images/info.svg)
> 
> `getsessionId()` is available in the Android (Java) SDK from v1.19.0 onwards.
    
    
    RudderClient.getInstance()?.sessionId
    

## Tracking lifecycle events

By default, RudderStack tracks the following **optional** [application lifecycle events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>):

  * [Application Installed](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>)
  * [Application Updated](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>)
  * [Application Opened](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>)
  * [Application Backgrounded](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-backgrounded>)


To disable tracking these events, set the `withTrackLifecycleEvents` method to `false` while initializing the SDK. However, it is highly recommended to keep them enabled.

#### Tracking events with AndroidX `LifecycleObserver`

Starting from version 1.14.0, the Android (Java) SDK supports a newer and more efficient way of tracking your application lifecycle events using the AndroidX [`LifecycleObserver`](<https://developer.android.com/reference/android/arch/lifecycle/LifecycleObserver>) class, as opposed to the standard method of tracking lifecycle events (using the [`ActivityLifecycleCallbacks`](<https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks>)).

To track lifecycle events with this method, add the following dependencies to your app:
    
    
    implementation 'androidx.lifecycle:lifecycle-process:2.6.1'
    implementation 'androidx.lifecycle:lifecycle-common:2.6.1'
    

Note that this method is **disabled** by default. Set `withNewLifecycleEvents` to `true` while initializing the Android (Java) SDK to use this method:
    
    
    val rudderClient = RudderClient.getInstance(
        this,
        WRITE_KEY,
        RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .withNewLifecycleEvents(true)
            .build()
    )
    
    
    
    RudderClient rudderClient = RudderClient.getInstance(
            this,
            WRITE_KEY,
            new RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withNewLifecycleEvents(true)
                    .build()
    );
    

If `withNewLifecycleEvents` is set to true but the required dependencies are missing in your app, the Android (Java) SDK will fall back to tracking lifecycle events using the default method `withTrackLifeCycleEvents` (if set to `true` while initializing the SDK).

The following table details the lifecycle event tracking matrix:

New way of tracking lifecycle events  
(`withNewLifecycleEvents`)| Standard way of tracking lifecycle events  
(`withTrackLifecycleEvents`)| Presence of AndroidX `LifecycleObserver` dependencies in app| Resultant way  
---|---|---|---  
Enabled| Enabled| Yes| New  
Enabled| Enabled| No| Standard  
Enabled| Disabled| No| Lifecycle events are not tracked.  
Enabled| Disabled| Yes| New  
Disabled| Enabled| NA| Standard  
Disabled| Disabled| NA| Lifecycle events are not tracked.  
  
## Tracking deep links

Starting from version 1.14.0, the Android (Java) SDK sends a `Deep Link Opened` event when you open any app from a [deep link](<https://developer.android.com/training/app-links/deep-linking>). It also sends all the deep link-related details as the event properties. In the previous versions, the SDK included these details as a part of the `Application Opened` event properties.

This feature is **turned on** by default. To turn it off, set `withTrackDeepLinks` to `false` while initializing the SDK - this causes the SDK to stop sending any additional `Deep Link Opened` events.

> ![info](/docs/images/info.svg)
> 
> After you set up the deep link in your Android app, you can trigger the deep linking as follows:
>     
>     
>     val url = "https://example.com/_app"
>     val intent = Intent(Intent.ACTION_VIEW)
>     intent.putExtra(Intent.EXTRA_REFERRER, Uri.parse("https://test.com/_app"))
>     intent.data = Uri.parse(url)
>     startActivity(intent)
>     

The `Deep Link Opened` event schema is shown below:

Property name| Data type| Description  
---|---|---  
`url`| String| Represents a Uniform Resource Locator used to identify a location on the network and a mechanism for retrieving it. URLs are used to open web pages, access APIs, and deep link into specific parts of the app.  
  
For example, `https://example.com/_app`.  
`referring_application`| String| Used to indicate the originating page or app when opening a URL.  
  
For example, `https://test.com/_app`.  
  
> ![info](/docs/images/info.svg)
> 
> The Android (Java) SDK also adds the query parameters as the deep link event properties.

## Debugging

If you run into any issues regarding the RudderStack Android (Java) SDK, you can turn on the `VERBOSE` or `DEBUG` logging to find out what the issue is. To turn on the logging, change your `RudderClient` initialization to the following:
    
    
    // initialize Rudder SDK
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            YOUR_WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withLogLevel(RudderLogger.RudderLogLevel.DEBUG)
                .build()
        )
    
    
    
    RudderClient rudderClient = RudderClient.getInstance(
        this,
        YOUR_WRITE_KEY,
        new RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .withLogLevel(RudderLogger.RudderLogLevel.DEBUG)
            .build()
    );
    

## Chromecast

[Google Chromecast](<https://store.google.com/in/product/chromecast?hl=en-GB>) is a device that plugs into your TV or monitor with an HDMI port, and can be used to stream content from your phone or computer.

RudderStack supports integrating the Android (Java) SDK with your Cast app. Follow [these instructions](<https://developers.google.com/cast/docs/android_sender>) to build your Android sender app. Then, add the Android (Java) SDK to it. Follow the [Google Cast developer guide](<https://developers.google.com/cast/docs/developers>) for more details.

## Developing a device mode destination

You can easily develop a device mode destination in case RudderStack doesn’t support it already, by following the steps listed in this section.

> ![info](/docs/images/info.svg)
> 
> More information on RudderStack device mode can be found in [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

  * Create a `CustomFactory` class by extending [`RudderIntegration.java`](<https://github.com/rudderlabs/rudder-sdk-android/blob/master/core/src/main/java/com/rudderstack/android/sdk/core/RudderIntegration.java>) :


    
    
    import androidx.annotation.NonNull;
    import androidx.annotation.Nullable;
    
    import com.rudderstack.android.sdk.core.RudderClient;
    import com.rudderstack.android.sdk.core.RudderConfig;
    import com.rudderstack.android.sdk.core.RudderIntegration;
    import com.rudderstack.android.sdk.core.RudderLogger;
    import com.rudderstack.android.sdk.core.RudderMessage;
    
    public class CustomFactory extends RudderIntegration<CustomFactory> {
        private static final String FACTORY_KEY = "Custom Factory";
    
        public static Factory FACTORY = new Factory() {
            @Override
            public RudderIntegration<?> create(Object settings, RudderClient client, RudderConfig rudderConfig) {
                return new CustomFactory(client,rudderConfig);
            }
    
            @Override
            public String key() {
                return FACTORY_KEY;
            }
        };
    
        private CustomFactory(@NonNull RudderClient client, RudderConfig config) {
    
        }
    
        private void processRudderEvent(RudderMessage element) {
            System.out.println("Processing RudderEvent of type "+element.getType());
    
        }
    
        @Override
        public void reset() {
            System.out.println("Reset is called");
        }
    
        @Override
        public void flush() {
            System.out.println("Flush is called");
        }
    
        @Override
        public void dump(@Nullable RudderMessage element) {
            try {
                if (element != null) {
                    processRudderEvent(element);
                }
            } catch (Exception e) {
                RudderLogger.logError(e);
            }
        }
    
        @Override
        public CustomFactory getUnderlyingInstance() {
            return this;
        }
    }
    

Some pointers to keep in mind:

  * You can use the constructor of the `CustomFactory` class to initialize the native SDK of the device mode destination you are working on.
  * RudderStack’s Android (Java) SDK dumps every event it receives to the `dump()` method of the `CustomFactory` class. From here, you can process the event and hand it over to the native SDK of the device mode destination.
  * The SDK also triggers the `reset()` method of the `CustomFactory` class on every `reset()` call made via the SDK. You can use this to handle the destination-specific reset.
  * RudderStack’s Android (Java) SDK also triggers the `flush()` method of the `CustomFactory` class on every `flush()` call made via the SDK which you can use to handle the destination-specific reset logic. You can make a `flush` call using the SDK as shown below:


    
    
    rudderClient.flush()
    
    
    
    rudderClient.flush();
    

Make sure you return a valid value from `getUnderlyingInstance()` as it is used by the Android (Java) SDK to validate `CustomFactory`.

  * Make sure you do not duplicate the value of `FACTORY_KEY` across multiple `CustomFactory` that you develop.
  * Register `CustomFactory` with the RudderStack Android (Java) SDK during its initialization:


    
    
    var rudderClient = RudderClient.getInstance(
                this,
                WRITE_KEY,
                RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withTrackLifecycleEvents(false)
                    .withRecordScreenViews(false)
                    .withCustomFactory(CustomFactory.FACTORY)
                    .build()
    )
    

That’s it! Your Device Mode destination is good to go.

## FAQ

#### What is the Android version required to set up the Android (Java) SDK?

RudderStack currently supports `API 14: Android 4.0 (IceCreamSandwich)` or higher.

#### I don’t have an `Application` class to initialize my RudderStack client. What do I do?

Follow our guide on [How to Add an Application Class to Your Android App](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/adding-an-application-class/>) to add an `Application` class.

#### How do I set the Android permissions?

See Setting the Android Permissions section above to do this.

#### Does the Android (Java) SDK support multi-process apps?

No, the RudderStack Android (Java) SDK does not support multi-process apps. Make sure to initialize the SDK from a single process to avoid any issues.

#### How do I use the Android (Java) SDK on applications with `minSDKVersion` less than 20?

By default, the Android (Java) SDK does not support applications with `minSDKVersion` less than `20`. You can add this support by following the steps below:

  1. Add the following dependency to the `build.gradle` file of your application:


    
    
    implementation 'com.google.android.gms:play-services-base:17.6.0'
    

  2. Add the function `tlsBackport()` in your `MainActivity` as shown:


    
    
    private fun tlsBackport() {
        try {
            ProviderInstaller.installIfNeeded(this)
            Log.e("Rudder", "Play present")
            val sslContext: SSLContext = SSLContext.getInstance("TLSv1.2")
            sslContext.init(null, null, null)
            sslContext.createSSLEngine()
        } catch (e: GooglePlayServicesRepairableException) {
            // Prompt the user to install/update/enable Google Play services.
            GoogleApiAvailability.getInstance()
                .showErrorNotification(this, e.connectionStatusCode)
            Log.e("Rudder", "Play install")
        } catch (e: GooglePlayServicesNotAvailableException) {
            // Indicates a non-recoverable error: let the user know.
            Log.e("SecurityException", "Google Play Services not available.")
            e.printStackTrace()
        }
    }
    

  3. Finally, call the `tlsBackport()` function at the very beginning of your `onCreate()` method in `MainActivity`.


    
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        if (Build.VERSION.SDK_INT <= Build.VERSION_CODES.KITKAT) {
            tlsBackport()
        }
    }
    

For more details, see [Android documentation](<https://developer.android.com/reference/javax/net/ssl/SSLSocket.html#protocols>).

#### Can I use the library with Maven?

Yes, you can use the library with `maven`.
    
    
    <dependency>
      <groupId>com.rudderstack.android.sdk</groupId>
      <artifactId>core</artifactId>
      <version>latest_version</version>
      <type>pom</type>
    </dependency>
    

#### How do I check whether a specific event is getting fired or not?

Using the following command in the Logcat tool once you set the `logLevel` to `VERBOSE`.
    
    
    adb logcat -s RudderSDK:V \
        -v tag -e "EventRepository: dump: message:"
    

#### How do I get the user `traits` after making the `identify` call?

You can get the user traits after making an `identify` call as shown in the following snippet:
    
    
    val traits = rudderClient!!.getRudderContext().getTraits()
    
    
    
        Map<string object=""> traitsObj = rudderClient.getRudderContext().getTraits();
    

#### Can I disable event tracking until the user gives their consent?

Yes, you can. RudderStack gives you the ability to disable tracking any user activity until the user gives their consent, by leveraging the `optOut` API. This is required in cases where your app is audience-dependent (e.g. minors) or where you’re using the app to track the user events (e.g. EU users) to meet the data protection and privacy regulations. The `optOut` API takes `true` or `false` as a Boolean value to enable or disable tracking user activities. So, to disable user tracking, you can use the `optOut` API as shown:
    
    
    rudderClient.optOut(true)
    

Once the user gives their consent, you can enable user tracking again:
    
    
    rudderClient.optOut(false)
    

For more information on the `optOut` API, refer to the [Enabling/Disabling User Tracking via optOut API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#enabling-tracking-via-optout>) section above.

> ![success](/docs/images/tick.svg)
> 
> You only need to call the `optOut` API with the required parameter once, as the information persists within the device even if you reboot it.

#### How does the SDK handle different client/server errors?

In case of client-side errors, e.g. if the source write key passed to the SDK is incorrect, RudderStack gives you a **400 Bad Request** response and aborts the operation immediately.

For other types of network errors (e.g. Invalid Data Plane URL), the SDK tries to flush the events to RudderStack in an incremental manner (every 1 second, 2 seconds, 3 seconds, and so on).

#### Can I apply encryption only on new databases?

Database encryption works on new and existing databases. Pass the `DbEncryption` object in `RudderConfig.Builder()` while initializing the Android (Java) SDK.

> ![info](/docs/images/info.svg)
> 
> You can use this object to convert an unencrypted database into an encrypted database and vice versa.

See Configuring your RudderStack client for more information on the configuration options.

#### Can I remove encryption from an encrypted database?

Yes, you can.

If the database is already encrypted, you can decrypt the database in the following way:
    
    
    RudderConfig.Builder()
    	  ...
        .withDbEncryption(RudderConfig.DBEncryption(false, "<your-encryption-key>")) // decrypt database
        .build()
    

> ![info](/docs/images/info.svg)
> 
> Make sure to set the `android-database-sqlcipher` dependency in your module level `build.gradle` file.
> 
> See DbEncryption for more information.

#### What happens if the supplied encryption key is different to the one the database is encrypted with?

After you encrypt the database:

  * If **no key** is provided, then the SDK deletes the current database with unsent events and creates a new unencrypted database instead.
  * If a **wrong key** is provided, then the SDK deletes the current database with unsent events and creates a new encrypted database with the given key.


#### How does the Android (Java) SDK handle events larger than 32KB?

The Android (Java) SDK drops any events greater than 32KB.