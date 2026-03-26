# Braze Device Mode Integration

Send events to Braze in RudderStack device mode.

* * *

  * __12 minute read

  * 


After you have successfully instrumented Braze as a destination in RudderStack, follow this guide to correctly send your events to Braze in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

## Add Braze integration

> ![warning](/docs/images/warning.svg)
> 
> Make sure to add the Braze integration to your project before sending events to Braze in device mode.

Depending on your integration platform, follow these steps:

> ![warning](/docs/images/warning.svg)
> 
> The Braze integration v1.0.0 and above requires minimum SDK version (`minSdk`) of 25.

Follow the steps in this section to add Braze to your Kotlin project.

[![Github Badge](https://img.shields.io/maven-central/v/com.rudderstack.integration.kotlin/braze?style=flat)](<https://central.sonatype.com/artifact/com.rudderstack.integration.kotlin/braze>)

  1. In your module (app-level) Gradle file (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the following dependencies for the RudderStack-Braze integration:


    
    
    dependencies {
      // ...
      
      // Add Rudder Kotlin and Braze integration SDKs:
      implementation("com.rudderstack.sdk.kotlin:android:<latest-version>")
      implementation("com.rudderstack.integration.kotlin:braze:<latest-version>")
    }
    

  2. For further steps on permissions and other optional configurations, see the [Braze documentation](<https://www.braze.com/docs/developer_guide/sdk_integration>).
  3. Add the SDK initialization and the `Rudder-Braze` integration in your `Application` class:


    
    
    import android.app.Application
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    import com.rudderstack.integration.kotlin.braze.BrazeIntegration
    
    class MyApplication : Application() {
        lateinit var analytics: Analytics
    
        override fun onCreate() {
            super.onCreate()
            analytics = Analytics(
                configuration = Configuration(
                    writeKey = "WRITE_KEY",
                    application = this,
                    dataPlaneUrl = "DATA_PLANE_URL",
                )
            )
            
            analytics.add(BrazeIntegration())
        }
    }
    

[![Github Badge](https://img.shields.io/github/v/tag/rudderlabs/integration-swift-braze?label=Swift Package Manager)](<https://github.com/rudderlabs/integration-swift-braze/>)

Follow these steps to add the Braze integration to your Swift project using Swift Package Manager:

  1. In Xcode, select **File > Add Package Dependencies…**.

![](/docs/images/event-stream-sources/swift/add-package-dependencies.webp)

  2. Enter the below package repository URL in the search bar:


    
    
    https://github.com/rudderlabs/integration-swift-braze/
    

  3. Select the latest version and the target to which you want to add the package.
  4. Click **Add Package**.


Alternatively, you can add the dependency to your `Package.swift` file, as shown:
    
    
    dependencies: [
        .package(url: "<https://github.com/rudderlabs/integration-swift-braze.git>", from: "<latest_integration_version>")
    ]
    

#### Usage

  1. Import the SDK and the integration:


    
    
    import RudderStackAnalytics
    import RudderIntegrationBraze
    

  2. Add `BrazeIntegration` to your `analytics` instance:


    
    
    // Initialize RudderStack Analytics
    let analytics = Analytics(
        configuration: Configuration(
            writeKey: "<WRITE_KEY>",
            dataPlaneUrl: "<DATA_PLANE_URL>"
        )
    )
    
    // Add Braze Integration
    analytics.add(plugin: BrazeIntegration())
    

> ![warning](/docs/images/warning.svg)
> 
> **Important**
> 
> The React Native-Braze integration has a known limitation.
> 
> See the Limitations for React Native and Flutter sources section for more details and workaround on this limitation.

  1. Add the RudderStack-Braze module to your app by running the following command:


    
    
    npm install @rudderstack/rudder-integration-braze-react-native
    
    
    
    yarn add @rudderstack/rudder-integration-braze-react-native
    

  2. Import the module you added above and add it to your SDK initialization code:


    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native";
    import braze from "@rudderstack/rudder-integration-braze-react-native";
    const config = {
      dataPlaneUrl: DATA_PLANE_URL,
      trackAppLifecycleEvents: true,
      withFactories: [braze]
    };
    rudderClient.setup(WRITE_KEY, config);
    

> ![warning](/docs/images/warning.svg)
> 
> **Important**
> 
> The Flutter-Braze integration has a known limitation.
> 
> See the Limitations for React Native and Flutter sources section for more details and workaround on this limitation.

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file:


    
    
    rudder_integration_braze_flutter: ^1.0.1
    

  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import the `RudderIntegrationBrazeFlutter` in your application where you are initializing the SDK:


    
    
    import 'package:rudder_integration_braze_flutter/rudder_integration_braze_flutter.dart';
    

  4. Change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationBrazeFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

  1. Add the following under `dependencies` section:


    
    
    implementation 'com.rudderstack.android.sdk:core:[1.0,2.0)'
    implementation 'com.rudderstack.android.integration:braze:[1.3.0,)'
    

> ![warning](/docs/images/warning.svg)
> 
> The [Braze-RudderStack Android SDK integration](<https://github.com/rudderlabs/rudder-integration-braze-android>) v2.0.0 and above requires a minimum SDK version (`minSdkVersion`) of 25.

  2. Add the following permissions to the `AndroidManifest.xml` file:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

  3. Change the SDK initialization to the following:


    
    
    // initialize Rudder SDK
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withLogLevel(RudderLogger.RudderLogLevel.DEBUG)
                .withFactory(BrazeIntegrationFactory.FACTORY)
                .build()
        )
    

  1. Open the `Podfile` of your project and add the following:


    
    
    pod 'Rudder-Braze'
    

  2. Run the `pod install` command.
  3. Change the SDK initialization to the following snippet:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:<data_plane_url>];
    [builder withFactory:[RudderBrazeFactory instance]];
    [RudderClient getInstance:<write_key>; config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports this device mode integration for Braze v4.4.4 and above.

  1. Install `RudderBraze` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following to your `Podfile`:


    
    
    pod 'RudderBraze', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Import the SDK depending on your preferred platform:


    
    
    import RudderBraze
    
    
    
    @import RudderBraze;
    

  4. Add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderBrazeDestination())
    
    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderBrazeDestination alloc] init]];
    

> ![info](/docs/images/info.svg)
> 
> To send push notification events, see Send push notifications.

## Limitations for React Native and Flutter sources

Braze requires different App Keys for Android and iOS platforms. Currently, there is no way to provide App Keys per platform when using the [React Native](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>) or [Flutter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>) SDKs with the Braze integration. **This is a known limitation** — the RudderStack team has a planned item to fix it in the near future.

You can work around this limitation by creating separate integrations and sources for Android (Java) and iOS (Obj-C). See the below sections for detailed steps.

#### Step 1: Create separate integrations

[Create two Braze destination integrations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/>) in the RudderStack dashboard:

  * **Braze Android** : Configure this integration with your Android App Key.
  * **Braze iOS** : Configure this integration with your iOS App Key.


#### Step 2: Create separate sources

Create two sources in the RudderStack dashboard:

  * **Flutter / React Native Android (Java)**
  * **Flutter / React Native iOS (Obj-C)**


#### Step 3: Connect sources to destinations

  1. Connect the **Flutter Android (Java)** source to the **Braze Android (Java)** destination.
  2. Connect the **Flutter iOS (Obj-C)** source to the **Braze iOS (Obj-C)** destination.


#### Step 4: Platform-specific SDK initialization

During SDK initialization, use platform checks to conditionally initialize the appropriate RudderStack SDK.

The example code snippets for Flutter and React Native are shown below:
    
    
    import 'dart:io';
    import 'package:rudder_sdk_flutter_platform_interface/platform.dart';
    import 'package:rudder_sdk_flutter/RudderController.dart';
    import 'package:rudder_integration_braze_flutter/rudder_integration_braze_flutter.dart';
    
    void initializeRudderSDK() {
        String writeKey = "";
        if (Platform.isAndroid) {
          writeKey = "<FLUTTER_ANDROID_WRITE_KEY>";
        } else if (Platform.isIOS) {
          writeKey = "<FLUTTER_IOS_WRITE_KEY>";
        }
    
        final RudderController rudderClient = RudderController.instance;
        RudderConfigBuilder builder = RudderConfigBuilder();
        builder
          ..withFactory(RudderIntegrationBrazeFlutter())
          ..withDataPlaneUrl(<DATA_PLANE_URL>)
        rudderClient.initialize(writeKey, config: builder.build());
    }
    

> ![info](/docs/images/info.svg)
> 
> Replace `FLUTTER_ANDROID_WRITE_KEY` and `FLUTTER_IOS_WRITE_KEY` with the actual write keys from your respective Flutter sources (for Android (Java) and iOS (Obj-C)) created in Step 2.
    
    
    import { Platform } from 'react-native';
    import rudderClient from "@rudderstack/rudder-sdk-react-native";
    import braze from "@rudderstack/rudder-integration-braze-react-native";
    
    const rudderInitialise = async () => {
      let writeKey = '';
      if (Platform.OS === 'android') {
        writeKey = '<REACT_NATIVE_ANDROID_WRITE_KEY>';
      } else if (Platform.OS === 'ios') {
        writeKey = '<REACT_NATIVE_IOS_WRITE_KEY>';
      }
    
      await rudderClient.setup(writeKey, {
        dataPlaneUrl: DATA_PLANE_URL,
        withFactories: [braze]
      });
    };
    
    rudderInitialise().catch(console.error);
    

> ![info](/docs/images/info.svg)
> 
> Replace `REACT_NATIVE_ANDROID_WRITE_KEY` and `REACT_NATIVE_IOS_WRITE_KEY` with the actual write keys from your respective React Native sources (for Android (Java) and iOS) created in Step 2.

### Use platform-specific Braze App Identifier keys

> ![announcement](/docs/images/announcement.svg)
> 
> This feature is currently in **Beta** and behind a feature flag. It is expected to be generally available by March 31, 2026.
> 
> Contact [RudderStack Support](<mailto:support@rudderstack.com>) to enable this feature for your account.

For device mode connections, you can configure platform-specific (Android, iOS, and web) Braze App Identifier keys while [setting up your Braze destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>). This is useful especially when connecting cross-platform SDK sources like React Native and Flutter, while also allowing Android and iOS sources to be configured to the same Braze destination.

To use this feature:

  1. Enable the **Enable Platform-specific App Identifier Keys** setting in the [Connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>).
  2. Configure the relevant App Identifier keys based on your connected sources.


#### How App Identifier key selection works

The Braze device mode integration looks for platform-specific App Identifier keys first. If unavailable, it uses the [Default App Identifier Key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>) instead.

Note that:

  * An older version of the device mode integration will continue to work with the default App Identifier key.
  * If you remove the default App Identifier key and configure platform-specific App Identifier keys, **you must upgrade** to the latest version of the device mode integration highlighted below:

SDK| Minimum supported integration version  
---|---  
Android (Kotlin)| [1.1.1](<https://github.com/rudderlabs/rudder-sdk-kotlin/releases/tag/com.rudderstack.integration.kotlin.braze%401.1.1>)  
iOS (Swift)| [1.0.1](<https://github.com/rudderlabs/integration-swift-braze/releases/tag/1.0.1>)  
React Native| [2.1.0](<https://github.com/rudderlabs/rudder-sdk-react-native/releases/tag/rudder-integration-braze-react-native%402.1.0>)  
Flutter| [2.5.0](<https://github.com/rudderlabs/rudder-sdk-flutter/releases/tag/rudder_integration_braze_flutter-v2.5.0>)  
Android (Java) — Legacy| [2.1.1](<https://github.com/rudderlabs/rudder-integration-braze-android/releases/tag/v2.1.1>)  
iOS (Obj-C) — Legacy| [4.2.1](<https://github.com/rudderlabs/rudder-integration-braze-ios/releases/tag/v4.2.1>)  
  
#### Migration example

**Scenario**

Suppose you have three sources connected to three separate Braze destinations in your current setup:

  * Android source (A) → Braze destination (B1)
  * iOS source (B) → Braze destination (B2)
  * JavaScript source (C) → Braze destination (B3)


Each destination is configured with platform-specific keys.

**What you want to achieve**

You want to consolidate these connections to a single Braze destination (B3, for example) that supports all the platform-specific App Identifier keys, simplifying your overall setup.

**Steps**

  1. **Upgrade your SDK integrations** : Upgrade your Android and iOS SDK integrations to the minimum versions that support platform-specific App Identifier keys. See the supported versions table above for details.

  2. **Enable platform-specific keys** : In your existing Braze destination B3 (previously connected only to the JavaScript source), enable the **Enable Platform-specific App Identifier Keys** toggle in the [Connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>) and specify the platform-specific key for the JavaScript source.

  3. **Connect additional sources** : Connect your Android (A) and iOS (B) sources to the Braze destination.

  4. **Add platform-specific keys** : Configure the Android and iOS App Identifier keys in the destination settings.

  5. **Remove old destinations** : Delete the older separate Braze destinations (B1 and B2) that are no longer needed.


After completing these steps, all three sources (Android, iOS, and JavaScript) send events to a single Braze destination configured with platform-specific App Identifier keys.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in Braze in any of the below cases:

  * When the user registers to the app for the first time.
  * When they log into their app.
  * When they update their information.


A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com",
      name: "Alex Keener"
    });
    

### Set custom user ID (`externalId`)

In mobile device mode, that is, when using Android (Java), iOS (Obj-C), React Native, or Flutter as source, you need to pass `externalId` in your `identify` events. Otherwise, Braze uses `userId` to identify the user.

> ![info](/docs/images/info.svg)
> 
> Braze gives first preference to the `externalId` field in the `identify` event to identify the user. If `externalId` is absent, it falls back to the `userId` field.

The following code snippet shows how to add an `externalId` to your `identify` event using the [React Native SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/#setting-custom-id>):
    
    
    const options = {
      externalIds: [
        {
          id: "<your_external_id>",
          type: "brazeExternalId",
        },
      ],
    }
    rudderClient.identify(
      "1hKOmRA4GRlm",
      {
        email: "alex@example.com",
        gender: "male",
      },
      options
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to send the `identify` event containing the `externalId` before sending any subsequent `track` events. That way, RudderStack is able to successfully persist the `externalId` information in all the future events.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event lets you record the customer events along with any associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added", {
      numberOfRatings: "12",
      name: "item 1"
    });
    

### Order Completed

When you use the `track` call for an `Order Completed` event, RudderStack sends the product information present in the event to Braze as `purchases`.

A sample `Order Completed` event is shown:
    
    
    rudderanalytics.track("Order Completed", {
      userId: "1hKOmRA4GRlm",
      currency: "USD",
      products: [
        {
          product_id: "123454387",
          name: "Game",
          price: 15.99
        }
      ]
    });
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event lets you record your website’s page views, with the additional relevant information about the viewed page.

A sample `page` call is as shown:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in"
    });
    

## Delta management for `identify` and `track` calls

If you are sending events to Braze in device mode, you can save costs by deduplicating your `identify` calls. To do so, enable the [Deduplicate Traits](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#deduplication-settings>) dashboard setting. RudderStack then sends only the changed or modified attributes (traits) to Braze.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends reviewing Braze’s [data points policy](<https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points/>) to fully understand how this functionality can help you avoid data overages.

## Advanced features

This section covers some advanced Braze operations that you can perform using RudderStack.

### Send push notification events

Depending on your iOS (Obj-C) SDK version, follow these steps to send push notification events to Braze:

  1. Follow the [Braze documentation](<https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/integration#push-notification-certificate>) to generate a push notification certificate.
  2. Add the following code to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    [[UIApplication sharedApplication] registerForRemoteNotifications];
    
    UNUserNotificationCenter *center = UNUserNotificationCenter.currentNotificationCenter;
    [center setNotificationCategories:BRZNotifications.categories];
    center.delegate = self;
    UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
    if (@available(iOS 12.0, *)) {
        options = options | UNAuthorizationOptionProvisional;
    }
    [center requestAuthorizationWithOptions:options
                          completionHandler:^(BOOL granted, NSError *_Nullable error) {
        NSLog(@"Notification authorization, granted: %d, "
              @"error: %@)",
              granted, error);
    }];
    

> ![warning](/docs/images/warning.svg)
> 
> You must assign the delegate object using `center.delegate = self` synchronously before your app finishes launching - preferably in `application:didFinishLaunchingWithOptions`.
> 
> Otherwise, your app may miss any incoming push notificaitons. See [Apple’s `UNUserNotificationCenterDelegate` documentation](<https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate>) for more information.

  3. Register push tokens with Braze:


    
    
    // - Register the device token with Braze
    - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
        if ([RudderBrazeFactory instance].integration) {
            [[RudderBrazeFactory instance].integration didRegisterForRemoteNotificationsWithDeviceToken:deviceToken];
        }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure that `RudderBrazeFactory` is initialized before making calls to this push API.
> 
> Since the Braze push API is designed as an instance method, it relies on the SDK that is correctly initialized beforehand. To do this, you can utilize the [`dispatch_after`](<https://developer.apple.com/documentation/dispatch/1452876-dispatch_after>) API.

  4. Enable push handling:


    
    
    // - Add support for silent notification
    
    - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler: (void (^)(UIBackgroundFetchResult))completionHandler {
        if ([RudderBrazeFactory instance].integration) {
            [[RudderBrazeFactory instance].integration didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
        }
    }
    
    // - Add support for push notifications
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler {
        if ([RudderBrazeFactory instance].integration) {
            [[RudderBrazeFactory instance].integration didReceiveNotificationResponse:response withCompletionHandler:completionHandler];
        }
    }
    
    // - Add support for displaying push notification when the app is currently running in the foreground
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler: (void (^)(UNNotificationPresentationOptions))completionHandler {
        if (@available(iOS 14, *)) {
            completionHandler(UNNotificationPresentationOptionList |
                              UNNotificationPresentationOptionBanner);
        } else {
            completionHandler(UNNotificationPresentationOptionAlert);
        }
    }
    

> ![info](/docs/images/info.svg)
> 
> Braze recommends invoking the [push integration code](<https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-3-enable-push-handling>) within the application’s main thread.

Add the following code to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:
    
    
    if #available(iOS 10, *) {
        let center = UNUserNotificationCenter.current()
        center.delegate = self
        var options: UNAuthorizationOptions = [.alert, .sound, .badge]
        if #available(iOS 12.0, *) {
            options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
            }
            center.requestAuthorization(options: options) { (granted, error) in
                RSClient.sharedInstance().pushAuthorizationFromUserNotificationCenter(granted)
        }
        UIApplication.shared.registerForRemoteNotifications()
    } else {
        let types: UIUserNotificationType = [.alert, .badge, .sound]
        let setting: UIUserNotificationSettings = UIUserNotificationSettings(types: types, categories: nil)
        UIApplication.shared.registerUserNotificationSettings(setting)
        UIApplication.shared.registerForRemoteNotifications()
    }
    
    
    
    if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_9_x_Max) {
      UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
      center.delegate = self;
      UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
      if (@available(iOS 12.0, *)) {
      options = options | UNAuthorizationOptionProvisional;
      }
      [center requestAuthorizationWithOptions:options
                            completionHandler:^(BOOL granted, NSError * _Nullable error) {
          [[RSClient sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
      }];
      [[UIApplication sharedApplication] registerForRemoteNotifications];
    } else {
      UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:(UIUserNotificationTypeBadge | UIUserNotificationTypeAlert | UIUserNotificationTypeSound) categories:nil];
      [[UIApplication sharedApplication] registerForRemoteNotifications];
      [[UIApplication sharedApplication] registerUserNotificationSettings:settings];
    }
    

### Send in-app message events

> ![info](/docs/images/info.svg)
> 
> This feature is available in the [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) [device mode integration](<https://github.com/rudderlabs/rudder-integration-braze-ios>) starting from version 1.4.0.

  1. Add the following line to your `Podfile` for Braze IAM support:


    
    
    pod 'BrazeUI'
    

  2. Navigate to your Xcode app project directory and run `pod install`.
  3. Import the BrazeUI SDK in your `AppDelegate.m` file:


    
    
    @import BrazeUI;
    

  4. Add a static variable to your `AppDelegate.m` file to keep a reference to the Braze instance throughout your app’s lifetime:


    
    
    static Braze *braze;
    

  5. Add the following code in your `AppDelegate.m` file just after the RudderStack iOS (Obj-C) SDK initialization snippet:


    
    
    id<RSIntegrationFactory> brazeFactoryInstance = [RudderBrazeFactory instance];
    // RudderStack SDK initialization
    [[RSClient getInstance] onIntegrationReady:brazeFactoryInstance withCallback:^(NSObject *brazeInstance) {
        if (brazeInstance && [brazeInstance isKindOfClass:[Braze class]]) {
            braze = (Braze *)brazeInstance;
            [self configureIAM];
        } else {
            NSLog(@"Error getting Braze instance.");
        }
    }];
    
    
    
    let brazeFactoryInstance = RudderBrazeFactory()
    // RudderStack SDK initialization
    RSClient.getInstance().onIntegrationReady(brazeFactoryInstance) { brazeInstance in
        if let brazeInstance = brazeInstance as? Braze {
            AppDelegate.braze = brazeInstance
            self.configureIAM()
        } else {
            print("Error getting Braze instance.")
        }
    }
    

  6. Add the `configureIAM` method in the `AppDelegate.m` file:


    
    
    -(void) configureIAM {
        // Refer here: https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/#setting-the-in-app-message-delegate
        BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
        braze.inAppMessagePresenter = inAppMessageUI;
    }
    
    
    
    func configureIAM() {
        // Refer here: https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/#setting-the-in-app-message-delegate
        let inAppMessageUI: BrazeInAppMessageUI = BrazeInAppMessageUI()
        AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
    }