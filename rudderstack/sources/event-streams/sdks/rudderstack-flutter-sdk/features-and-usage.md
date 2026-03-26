# Flutter SDK Features and Usage

Features and use cases that you can implement using the Flutter SDK.

* * *

  * __8 minute read

  * 


This guide walks you through the different Flutter SDK features and how to use them.

## Encrypting RudderStack databases

> ![info](/docs/images/info.svg)
> 
> This feature is available in the Flutter SDK from v2.6.0 onwards.

To use the database encryption feature in the Flutter SDK, follow these steps:

  1. Add the new `rudder_plugin_db_encryption` package to your app by adding the below line to your `pubspec.yml`:


    
    
    rudder_plugin_db_encryption: ^1.0.1
    

  2. Run the following command:


    
    
    flutter pub get
    

  3. Once the package is installed, import it by running the following command:


    
    
    import 'package:rudder_plugin_db_encryption/rudder_plugin_db_encryption.dart';
    

  4. Create a `RudderDBEncryption` object and pass it while initializing the SDK, as shown:


    
    
    RudderDBEncryption dbEncryption = RudderDBEncryption(true, "<encryption_key>");
        MobileConfig mc = MobileConfig(dbEncryption: dbEncryption);
        RudderConfigBuilder builder = RudderConfigBuilder();
        builder
          ..withDataPlaneUrl("DATA_PLANE_URL")
          ..withMobileConfig(mc);
        rudderClient.initialize("WRITE_KEY", config: builder.build());
    

The `RudderDBEncryption` class accepts the following parameters:

Parameter| Type| Description| Default value  
---|---|---|---  
`enable`| bool| Specifies whether to encrypt/decrypt the database.| `False`  
`encryption_key`| String| Key used to encrypt/decrypt the database.| -  
  
To remove encryption from a database, configure the `RudderDBEncryption` object with your encryption key and set `enable` to `false`.

**Instructions for iOS**

The `rudder_plugin_db_encryption` uses the [SQLCipher](<https://github.com/sqlcipher/sqlcipher>) Cocoapod under the hood to perform encryption. This Cocoapod requires the removal of any references to the standard SQLite system library for it to function as expected.

If you set up a project to inadvertently include a linking reference against the standard SQLite library before SQLCipher, it is possible that the application builds and runs correctly but does not use SQLCipher for encryption. This is not a problem for most projects but there are certain cases where unintentional SQLite linking can occur.

One such example is when using CocoaPods or some other sub-project that declares a dependency on the SQLite3 library. In this case, adding a pod to a project can **silently** modify the project settings in such a way that SQLCipher is not properly linked.

You can identify and fix the above linking issue during the development stage by looking for the below error log from the SDK:
    
    
    RSDBPersistentManager: createDB: Cannot encrypt the Database as SQLCipher wasn't linked correctly.
    

To fix the linking issue, add a linker flag to your project settings to ensure that the Xcode links SQLCipher before SQLite. Follow these steps:

  1. Open the project-level build settings. These are the global project settings, not for the individual application target.
  2. Locate the **Other Linker Flags** setting and add one of the following commands depending on how you are integrating SQLCipher into the app.


> ![warning](/docs/images/warning.svg)
> 
> If you are not adding `SQLCipher` into the app on your own and only using `rudder_plugin_db_encryption`, then see only the points 3 and 4 in the below table - depending on whether you are using `use_frameworks!` in your app’s `ios/Podfile`.

Scenario| Command| Notes  
---|---|---  
When using SQLCipher commercial edition static libraries| `$(PROJECT_DIR)/sqlcipher-static-ios/ios-libs/libsqlcipher-ios.a`| Adjust according to the path to the `libsqlcipher-ios.a` you received as a part of the package.  
When using the `sqlcipher.xcodeproj` included in the SQLCipher Git repository| `$(BUILT_PRODUCTS_DIR)/libsqlcipher.a`| -  
When using the SQLCipher CocoaPod with the `use_frameworks` Podfile setting enabled| `-framework SQLCipher`| -  
When using the SQLCipher CocoaPod without the `use_frameworks` Podfile setting enabled| `-lSQLCipher`| -  
  
Once the linker flag is added to the project-level build settings, you should see something like the below image:

[![Project-level build settings](/docs/images/event-stream-sources/flutter-sdk-project-build-settings.webp)](</docs/images/event-stream-sources/flutter-sdk-project-build-settings.webp>)

After adding the linker flag to your project-level build settings, check the target-level build settings to ensure SQLCipher is shown first, as seen below:

[![Target-level build settings](/docs/images/event-stream-sources/flutter-sdk-target-build-settings.webp)](</docs/images/event-stream-sources/flutter-sdk-target-build-settings.webp>)

## Gzipping requests

> ![info](/docs/images/info.svg)
> 
> This feature is supported only for the mobile platforms.

The Flutter SDK automatically gzips event requests before sending it to the RudderStack backend (data plane) for processing. However, you can disable this by setting the `gzip` parameter to false while initializing the SDK:
    
    
    MobileConfig mc = MobileConfig(gzip: false);
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder
        ..withDataPlaneUrl("DATA_PLANE_URL")
        ..withMobileConfig(mc);
    rudderClient.initialize("WRITE_KEY", config: builder.build(), options: null);
    

## Enabling/disabling user tracking (GDPR support)

> ![warning](/docs/images/warning.svg)
> 
> This functionality is not available for the [web](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/installation-and-setup/#installing-flutter-sdk-for-web>).

RudderStack lets you opt out of tracking any user activity until the user gives their consent. You can do this using the SDK’s `optOut` API.

> ![info](/docs/images/info.svg)
> 
> The `optOut` API is available in the Flutter SDK starting from version `1.0.6`.

The `optOut` API takes a Boolean value to enable or disable tracking user activities. **This flag persists across device reboots**.

The following snippet highlights the use of the `optOut` API to disable user tracking:
    
    
    rudderClient.optOut(true);
    

Once the user grants their consent, you can enable user tracking by passing `false` to the `optOut` API:
    
    
    rudderClient.optOut(false);
    

## Filtering events

When sending events to a destination via the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you can explicitly specify the events to be sent or discarded by allowlisting or denylisting them.

Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this feature.

## Enabling/disabling events for specific destinations

The Flutter SDK lets you enable or disable sending events to a specific destination or all destinations connected to a source. You can specify these destinations by creating an object shown in the following snippet:
    
    
    RudderOption options = new RudderOption();
    // represents all destinations connected to the source, the default value is true.
    options.putIntegration("All", false);
    // specifying destination by its display name
    options.putIntegration("Mixpanel", false);
    // specifying destination by its Factory object
    options.putIntegrationWithFactory(Appcenter(), true);
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure the destination names that you pass while specifying the destinations **match exactly** with the names listed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>).

You can pass the destinations to the SDK in the following two ways:

#### Method 1. Passing destinations while initializing the SDK

This is helpful when you want to enable or disable sending the events to the destinations across all the API calls made using the SDK.
    
    
    rudderClient.initialize(WRITE_KEY,
                        config: builder.build(),options: options);
    

#### Method 2. Passing destinations while making event calls

This approach is helpful when you want to:

  * Enable or disable sending a particular event to the destination, or
  * If you want to override the destinations passed while initializing the SDK, for a particular event.


    
    
    RudderProperty property = RudderProperty();
    property.put("test_key_1", "test_key_1");
    rudderClient.track("test_track_event", properties: property, options: options);
    

> ![info](/docs/images/info.svg)
> 
> If you specify the destinations while initializing the SDK and in the event, then the SDK considers only the destinations specified at the event level.

### Setting custom objects for destinations

Starting from v2.4.0, you can also use the `putIntegration` method on the `RudderOption` object to set custom objects used by the device mode destinations.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * This feature is applicable **only** for the web platform.
>   * For mobile platforms, the `putIntegration` method accepts the custom objects but **does not** set them for the destination. Instead, it only enables sending events to that destination (equivalent to `options.putIntegration("<destination>", true);`).
> 


An example of setting a custom object to Google Analytics 4 via a `track` call:
    
    
    RudderProperty property = RudderProperty();
    property.put("manufacturer", "Ford");
    property.put("model", "Explorer");
    RudderOption options = RudderOption();
    options.putIntegration("Mixpanel", false);
    options.putIntegration("Google Analytics 4", {
       "sendUserID": false
     });
    rudderClient.track("Purchased Car", properties: property, options: options);
    

## Setting custom context

Starting from v2.4.0, you can use the `putCustomContext` method on the `RudderOption` object to pass custom contextual information in all the [events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/supported-api/>).

An example of setting custom context and passing it in a `track` call:
    
    
    RudderProperty property = RudderProperty();
    property.put("manufacturer", "Ford");
    property.put("model", "Explorer");
    RudderOption options = RudderOption();
    options.putCustomContext("address", {
          "city": "New Orleans",
          "pin": "70032",
          "state": {"name": "Louisiana", "code": "LO"},
          "country": {"name": "USA", "code": "US"},
          "zone": 12,
          "lat": 22.5726,
    });
    rudderClient.track("Purchased Car", properties: property, options: options);
    

## Setting the advertisement ID

> ![warning](/docs/images/warning.svg)
> 
> This functionality is not available for the [web](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/installation-and-setup/#installing-flutter-sdk-for-web>).

RudderStack automatically collects the advertisement ID **only** if `autoCollectAdvertId` is set to `true` during the [SDK initialization](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/installation-and-setup/#initializing-the-sdk>):
    
    
    final RudderController rudderClient = RudderController.instance;
    MobileConfig mobileConfig = MobileConfig(autoCollectAdvertId: true);
    RudderLogger.init(RudderLogger.VERBOSE);
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withDataPlaneUrl(DATA_PLANE_URL);
    builder.withTrackLifecycleEvents(true);
    rudderClient.initialize(WRITE_KEY,config: builder.build());
    

To explicitly pass your Android AAID or iOS IDFA, you can use the SDK’s `putAdvertisingId` method.

The `putAdvertisingId` method accepts a string argument `<ADVERTISING_ID>` which corresponds to your Android `advertisingId`(AAID) or iOS `advertisingId` (IDFA).

An example of how to use `putAdvertisingId` is shown below:
    
    
    rudderClient.putAdvertisingId(<ADVERTISING_ID>);
    

## Setting the device token

> ![warning](/docs/images/warning.svg)
> 
> This functionality is not available for the [web](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/installation-and-setup/#installing-flutter-sdk-for-web>).

You can use your device token to pass push notifications to the destinations that support them. RudderStack sets this token under `context.device.token`. To set a custom device token, the SDK supports the `putDeviceToken` method.

An example of setting a custom device token is shown below:
    
    
    rudderClient.putDeviceToken(<DEVICE_TOKEN>);
    

## Sending events to web device mode destinations

RudderStack does not support sending events from the Flutter SDK to your destinations in [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) due to some limitations. If you are deploying a Flutter app to the web, you can send events to these destinations in cloud mode only.

As a workaround, you can create a separate [JavaScript source](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) in RudderStack and use its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for the web build of your Flutter apps to send events to these destinations in web device mode.

## Debugging

If you run into any issues when using the Flutter SDK, you can enable the SDK’s logging feature to determine the issue. To do so, follow these steps:

  1. Import `RudderLogger` by running the following command:


    
    
    import 'package:rudder_sdk_flutter/RudderLogger.dart';
    

  2. Enable the logging by changing your SDK initialization:


    
    
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withDataPlaneUrl(DATA_PLANE_URL);
    builder.withLogLevel(RudderLogger.VERBOSE);
    rudderClient.initialize(WRITE_KEY,
                              config: builder.build());
    

  3. Set the log level to one of the following values:


  * `NONE`
  * `ERROR`
  * `WARN`
  * `INFO`
  * `DEBUG`
  * `VERBOSE`


> ![info](/docs/images/info.svg)
> 
> For detailed logs, set the log level to `DEBUG` or `VERBOSE`.

## FAQ

#### Can I apply encryption only on new databases?

Database encryption works on new and existing databases. Pass the `RudderDBEncryption` object while initializing the Flutter SDK.

#### Can I remove encryption from an encrypted database?

Yes, you can. If the database is already encrypted, you can decrypt the database by configuring the `RudderDBEncryption` object with your encryption key and setting `enable` to `false`.

#### What happens if the supplied encryption key is different to the one the database is encrypted with?

After you encrypt the database:

  * If **no key** is provided, then the SDK deletes the current database with unsent events and creates a new unencrypted database instead.
  * If a **wrong key** is provided, then the SDK deletes the current database with unsent events and creates a new encrypted database with the given key.


#### Does the Flutter SDK support impression events?

No, the SDK does not support [Flutter Impression](<https://pub.dev/packages/impression>) currently.