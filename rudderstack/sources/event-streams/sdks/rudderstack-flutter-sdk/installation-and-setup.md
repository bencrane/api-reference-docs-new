# Flutter SDK Installation and Setup

Install and set up the Flutter SDK.

* * *

  * __6 minute read

  * 


This guide walks you through the SDK installation and initialization steps in detail.

## Prerequisites

  * Set up the [Flutter development environment](<https://flutter.dev/docs/get-started/install>) in your system.
  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up a Flutter source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in your [RudderStack Cloud dashboard](<https://app.rudderstack.com/>). Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


## Installing the SDK

> ![info](/docs/images/info.svg)
> 
> Starting from v1.0.2, the RudderStack Flutter SDK is migrated to [Null Safety](<https://dart.dev/null-safety>).

Follow these steps to add the Flutter SDK through [`pub`](<https://pub.dev/packages/rudder_sdk_flutter>):

  1. Open `pubspec.yaml` and add `rudder_sdk_flutter` under `dependencies` section:


    
    
    dependencies:
      rudder_sdk_flutter: ^2.0.1
    

  2. Navigate to your application’s root folder and install all the required dependencies with the following command:


    
    
    flutter pub get
    

If you are using Proguard full mode to optimize your app, add the lines specified in the FAQ to your Android ProGuard rules.

### Installing Flutter SDK for web

> ![info](/docs/images/info.svg)
> 
> Starting from v3.2.0, the Flutter Web SDK supports [WebAssembly (WASM)](<https://docs.flutter.dev/platform-integration/web/wasm>).

  1. Install the Flutter SDK.
  2. Create a [Flutter source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the RudderStack dashboard.
  3. Copy the installation snippet from the **Web (Minified)** or **Web (Original)** tab as per your requirement.

[![Flutter JavaScript snippet](/docs/images/event-stream-sources/flutter-js-snippet.webp)](</docs/images/event-stream-sources/flutter-js-snippet.webp>)

  4. Paste the snippet in the `<head>` section of your web page.


> ![warning](/docs/images/warning.svg)
> 
> The Flutter Web SDK **does not support** the following features:
> 
>   * [Manage user tracking (GDPR support)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#enablingdisabling-user-tracking-gdpr-support>)
>   * [Setting the device token](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#setting-the-device-token>)
>   * [Setting the advertisement ID](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#setting-the-advertisement-id>)
> 


## Initializing the SDK

  1. Import the SDK using the following snippet:


    
    
    import 'package:rudder_sdk_flutter_platform_interface/platform.dart';
    import 'package:rudder_sdk_flutter/RudderController.dart';
    

  2. Add the following code in your application:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderLogger.init(RudderLogger.VERBOSE);
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withDataPlaneUrl(<DATA_PLANE_URL>);
    builder.withTrackLifecycleEvents(true);
    rudderClient.initialize(<WRITE_KEY>,config: builder.build());
    

> ![warning](/docs/images/warning.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values.

The `initialize` method has the following signature:

Name| Type| Description  
---|---|---  
`writeKey`  
Required| String| Flutter source’s write key.  
`config`| `RudderConfig`| RudderStack client configuration.  
  
## SDK initialization options

You can configure the SDK behavior using the `RudderConfig` object passed to the `rudderClient.initialize()` call during initialization.

You can create the object of `RudderConfig` class by either:

  * Directly calling its constructor using the parameters documented below, or
  * Using the `RudderConfigBuilder` class APIs as per your requirement

`RudderConfig` constructor parameter| `RudderConfigBuilder` class API| Type| Description| Default value  
---|---|---|---|---  
`dataPlaneUrl`| `withDataPlaneUrl()`| String| Your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>)|   
`flushQueueSize`| `withFlushQueueSize()`| int| Number of events in a batch request to the server.| `30`  
`isDebug`| `withDebug()`| bool| When enabled, sets the log level as `debug`. For more information, refer to the [Debugging](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#debugging>) section.| `false`  
`logLevel`| `withLogLevel()`| int| Controls the logs you want to see from the Flutter SDK.| `RudderLogger.RudderLogLevel.NONE`  
`mobileConfig`| `withMobileConfig()`| MobileConfig| Refer to the `mobileConfig` parameters section below.| -  
`webConfig`| `withWebConfig()`| WebConfig| Refer to the `webConfig` parameters section below.| -  
`controlPlaneUrl`| `withControlPlaneUrl()`| String| This parameter should be changed **only if** you are self-hosting the control plane. Refer to the Self-hosted control plane section for more information. The SDK will add `/sourceConfig` along with this URL to fetch the configuration.| `https://api.rudderlabs.com`  
  
### mobileConfig parameters

The `mobileConfig` object contains the mobile-specific configuration parameters for the Flutter SDK.

Parameter| Type| Description| Default value  
---|---|---|---  
`dbCountThreshold`| int| Number of events to be saved in the SQLite database. Once this limit is reached, the older events are deleted from the database.| `10000`  
`sleepTimeOut`| int| Minimum waiting time to flush the events to the server.| `10 seconds`  
`configRefreshInterval`| int| Fetches the config from the dashboard after this specified time.| `2`  
`trackLifecycleEvents`| bool| Determines if the SDK will capture application life cycle events automatically.| `true`  
`autoCollectAdvertId`| bool| Determines if the SDK will collect the advertisement ID.| `false`  
`recordScreenViews`| bool| When enabled, the SDK automatically records the screens viewed by the user.| `false`  
`dbEncryption`| `RudderDBEncryption`| Specify whether to encrypt/decrypt the database using the specified key. See [Encrypting RudderStack databases](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#encrypting-rudderstack-databases>) for more information.| -  
  
### webConfig parameters

The `webConfig` object contains the configuration parameters for using the SDK in the Flutter web applications.

Note the following:

  * The `webConfig` object of the Flutter SDK supports all the [load options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) currently supported by the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) except the following:

    * `logLevel`
    * `integrations`
    * `configUrl`
    * `getSourceConfig`


> ![warning](/docs/images/warning.svg)
> 
> The `webConfig` object **does not support** the following parameters anymore from the Flutter SDK v3.0.0:
> 
>   * `maxRetryDelay`, `minRetryDelay`
>   * `backoffFactor`
>   * `maxAttempts`, `maxItems`
>   * `maxBeaconItems`
>   * `beaconFlushQueueInterval`
>   * `autoSessionTracking`
>   * `sessionTimeoutInMillis`
>   * `cookieConsentManagers`
> 


  * You can [enable or disable events for specific destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/features-and-usage/#enablingdisabling-events-for-specific-destinations>) while initializing the Flutter SDK.


## Self-hosted control plane

If you are self-hosting RudderStack and using the [Control plane lite](<https://github.com/rudderlabs/config-generator#rudderstack-control-plane-lite>) utility to host your own control plane, then follow the steps in [this section](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#using-sdk-sources-set-up-in-self-hosted-control-plane>) and specify the `controlPlaneUrl` parameter in your `RudderConfigBuilder` that points to the hosted configuration file.

> ![danger](/docs/images/danger.svg)
> 
> You should not pass the `controlPlaneUrl` parameter during SDK initialization if you are using [RudderStack Cloud](<https://app.rudderstack.com>). This parameter is supported **only** if you are using the open source [Control plane lite](<https://github.com/rudderlabs/config-generator#rudderstack-control-plane-lite>) utility to set up your own control plane.

## FAQ

#### Do I need to add anything to my Android ProGuard rules?

Add the following lines to your Android ProGuard rules if you are using Proguard full mode to optimize your app:

> ![info](/docs/images/info.svg)
> 
> Add the below rules if you are using the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
>   
>  For new implementations, use the Android (Kotlin) SDK instead. older than v1.20.0.
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