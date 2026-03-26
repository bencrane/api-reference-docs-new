# Adjust Device Mode Integration

Send events to Adjust in RudderStack device mode.

* * *

  * __10 minute read

  * 


After you have [successfully instrumented](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/>) Adjust as a destination in RudderStack, follow this guide to correctly send your events to Adjust in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

See the following GitHub repositories for more information on the implementation:

  * [Android (Java) — Legacy](<https://github.com/rudderlabs/rudder-integration-adjust-android>)
  * [iOS (Obj-C) — Legacy](<https://github.com/rudderlabs/rudder-integration-adjust-ios>)


## Add device mode integration

Follow these steps to add Adjust to your project depending on your integration platform:

Follow the steps in this section to add Adjust to your Kotlin project.

[![Github Badge](https://img.shields.io/maven-central/v/com.rudderstack.integration.kotlin/adjust?style=flat)](<https://central.sonatype.com/artifact/com.rudderstack.integration.kotlin/adjust>)

  1. In your module (app-level) Gradle file (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the following dependencies for the RudderStack-Adjust integration:


    
    
    dependencies {
      // ...
      
      // Add Rudder Kotlin and Adjust integration SDKs:
      implementation("com.rudderstack.sdk.kotlin:android:<latest-version>")
      implementation("com.rudderstack.integration.kotlin:adjust:<latest-version>")
    }
    

  2. For further steps like adding the Google Play Services dependency, required AndroidManifest permissions, and ProGuard rules, refer to the [Adjust documentation](<https://dev.adjust.com/en/sdk/android/>).
  3. Add the SDK initialization and the `Rudder-Adjust` integration in your `Application` class:


    
    
    import android.app.Application
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    import com.rudderstack.integration.kotlin.adjust.AdjustIntegration
    
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
            
            analytics.add(AdjustIntegration())
        }
    }
    

[![Github Badge](https://img.shields.io/github/v/tag/rudderlabs/integration-swift-adjust?label=Swift Package Manager)](<https://github.com/rudderlabs/integration-swift-adjust/>)

Follow these steps to add the Adjust integration to your Swift project using Swift Package Manager:

  1. In Xcode, select **File > Add Package Dependencies…**.

![](/docs/images/event-stream-sources/swift/add-package-dependencies.webp)

  2. Enter the below package repository URL in the search bar:


    
    
    https://github.com/rudderlabs/integration-swift-adjust/
    

  3. Select the latest version and the target to which you want to add the package.
  4. Click **Add Package**.


Alternatively, you can add the dependency to your `Package.swift` file, as shown:
    
    
    dependencies: [
        .package(url: "<https://github.com/rudderlabs/integration-swift-adjust.git>", from: "<latest_integration_version>")
    ]
    

#### Usage

  1. Import the SDK and the integration:


    
    
    import RudderStackAnalytics
    import RudderIntegrationAdjust
    

  2. Add `AdjustIntegration` to your `analytics` instance:


    
    
    // Initialize RudderStack Analytics
    let analytics = Analytics(
        configuration: Configuration(
            writeKey: "<WRITE_KEY>",
            dataPlaneUrl: "<DATA_PLANE_URL>"
        )
    )
    
    // Add Adjust Integration
    analytics.add(plugin: AdjustIntegration())
    

To add Adjust to your Unity app, follow these steps:

  1. Add the [RudderStack Unity SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-unity-sdk/>) to your project.

  2. Download the [Adjust SDK extension](<https://github.com/rudderlabs/rudder-sdk-unity/tree/master/Integrations/Adjust/RudderAdjust>) package and import it in your project.


The package comes with Adjust Unity SDK embedded in it along with the required `jar` files for Android Install Referrer. **It is strongly recommended to not add the Adjust SDK separately**.

  3. After importing the `rudder-unity-extension-adjust.unitypackage` to your project, attach the `RudderPrefabs.prefab` file from `RudderUnityPlugin` to your main `GameObject`.
  4. Finally, change the SDK initialization:


    
    
    // Build your config
    RudderConfigBuilder configBuilder = new RudderConfigBuilder()
        .WithEndPointUrl(DATA_PLANE_URL)
        .WithFactory(RudderAdjustIntegrationFactory.GetFactory());
    
    // Get instance for RudderClient
    RudderClient rudderClient = RudderClient.GetInstance(
        WRITE_KEY,
        configBuilder.Build()
    );
    

Follow the below steps to add Adjust to your Flutter Project:

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file.


    
    
    rudder_integration_adjust_flutter: ^1.0.1
    

  


  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  


  3. Import the `RudderIntegrationAdjustFlutter` in your application where you are initializing the SDK.


    
    
    import 'package:rudder_integration_adjust_flutter/rudder_integration_adjust_flutter.dart';
    

  


  4. Finally, change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationAdjustFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

To add Adjust to your Android project, follow these steps:

  1. Add `mavenCentral()` to the `repositories` section of your `build.gradle` file:


    
    
    repositories {
      mavenCentral()
    }
    

  2. Next, add the following permissions to your `AndroidManifest.xml` file:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    // If you are not targeting the Google Play Store, you need to add the following permission:
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"></uses-permission>
    // If you are targeting Android 13 and above (API level 33), you need to add the com.google.android.gms.AD_ID permission to read the device's advertising ID.
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"></uses-permission>
    

  3. Finally, add the following lines in your `build.gradle` file under `dependencies`:


    
    
    // RudderStack Android-SDK
    implementation 'com.rudderstack.android.sdk:core:[1.0,2.0)'
    // RudderStack Adjust-SDK
    implementation 'com.rudderstack.android.integration:adjust:1.0.1'
    // Add Google Play Services library to enable the Google Advertising ID for Adjust SDK
    implementation 'com.google.android.gms:play-services-ads-identifier:17.0.1'
    // To support the Google Play Referrer API, make sure you have the following in your build.gradle file:
    implementation 'com.android.installreferrer:installreferrer:2.2'
    

> ![info](/docs/images/info.svg)
> 
> For more information on implementing `com.google.android.gms:play-services-ads-identifier:17.0.1`, refer to the [Adjust documentation](<https://help.adjust.com/en/article/get-started-android-sdk#add-google-play-services>).

  4. After adding the dependency, register the `RudderAdjustFactory` with your `RudderClient` initialization as a `factory` of `RudderConfig`. Add the following line in your `Application` class:


    
    
    import com.rudderstack.android.integration.adjust.AdjustIntegrationFactory;
    

  5. Finally, change the SDK initialization to the following:


    
    
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(AdjustIntegrationFactory.FACTORY)
                .build()
        )
    

To add Adjust to your iOS project, follow these steps:

  1. Add the following line to your [CocoaPods](<https://cocoapods.org>) `Podfile`:


    
    
    pod 'Rudder-Adjust'
    

  2. After adding the dependency, register the `RudderAdjustFactory` with your `RudderClient` initialization as a `factory` of `RudderConfig`. Run the following command to import `RudderAdjustFactory.h` file in your `AppDelegate.m` file:


    
    
    #import <Rudder-Adjust/RudderAdjustFactory.h>

  3. Then, change the SDK initialization to the following:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderAdjustFactory instance]];
    [RudderClient getInstance:WRITE_KEY config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Adjust v4.29.7 and above.

To add Adjust to your iOS project, follow these steps:

  1. Install `RudderAdjust` (available through [CocoaPods](<https://cocoapods.org>) by adding the following line to your `Podfile`):


    
    
    pod 'RudderAdjust', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Next, import the SDK depending on your preferred platform:


    
    
    import RudderAdjust
    

  

    
    
    @import RudderAdjust;
    

  4. Add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderAdjustDestination())
    

  

    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderAdjustDestination alloc] init]];
    

## Supported events

In device mode, RudderStack supports sending the following events to Adjust:

  * [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>)
  * [Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>)


## Identify

RudderStack’s [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions.

RudderStack sends the user information in the `identify` call to Adjust’s `addSessionPartnerParameter` method to set the `userId` (or `anonymousId`, in case `userId` is absent), so that the user information is passed to the subsequent calls.

A sample `identify` call is shown below:
    
    
    [[RudderClient sharedInstance] identify:@"developer_user_id"
                                     traits:@{@"foo": @"bar", @"foo1": @"bar1"}];
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them.

When you make a `track` call, RudderStack maps the event name with the corresponding Adjust custom event in the dashboard using Adjust’s [`trackEvent` method](<https://dev.adjust.com/en/sdk/ios/features/events>).

> ![warning](/docs/images/warning.svg)
> 
> Make sure to define the event mapping in the [**Map events to Adjust Event Tokens**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) dashboard setting. Adjust will reject any events apart from these mappings.
> 
> You must [create the event token in the Adjust dashboard](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#how-can-i-create-a-new-event-token-in-adjust>) before specifying the mappings.

### Callback parameters

RudderStack sends all custom properties in your `track` calls as [callback parameters](<https://dev.adjust.com/en/sdk/ios/v4/features/session-parameters/>).

A sample `track` call is shown below:
    
    
    [[RudderClient sharedInstance] track:@"test_event"
                              properties:@{@"key":@"value", @"foo": @"bar"}];
    

### Partner parameters

You can also send custom properties in your `track` calls as [partner parameters](<https://dev.adjust.com/en/sdk/adobe-extension/ios/global-parameters/>) to Adjust. Adjust then sends those parameters to the external partners you have set up in your Adjust dashboard. See the [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/#how-can-i-set-up-new-partners-in-adjust>) for more information on adding a partner in Adjust.

RudderStack uses the property mappings specified in the [**RudderStack Parameters to Partner Parameters**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) dashboard setting to check if a key is present in the `track` event properties and maps it to the corresponding Adjust partner parameter object.

> ![warning](/docs/images/warning.svg)
> 
>   * Adjust will reject any properties apart from mappings specified in the **RudderStack Parameters to Partner Parameters** dashboard setting.
>   * The partner parameters only accept the String data type.
> 


Suppose you set the following mappings in the RudderStack dashboard:

RudderStack property| Adjust partner parameter  
---|---  
`revenue`| `price`  
`quantity`| `quantity`  
  
A sample `track` call with the above properties is shown below:
    
    
    [[RudderClient sharedInstance] track:@"purchase"
                              properties:@{@"revenue":@20.99,
                              @"currency": @"USD",
                              @"quantity": @10}];
    

### Revenue tracking

To send [revenue tracking](<https://help.adjust.com/en/article/record-events-ios-sdk#record-event-revenue>) events to Adjust, add `revenue` and `currency` to your event properties:
    
    
    [[RudderClient sharedInstance] track:@"purchase"
                              properties:@{@"revenue":@2.99, @"currency": @"USD"}];
    

## App install attribution

RudderStack’s Adjust mobile integration (iOS and Android) automatically triggers an `Install Attributed` event if you have enabled **Install Attribution tracking** in the [dashboard settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).

> ![info](/docs/images/info.svg)
> 
> The enhanced attribution support is available from:
> 
>   * Rudder-Adjust Android v2.1.0 and above
>   * Rudder-Adjust iOS v2.2.0 and above
> 


### Usage

Follow these steps to use the enhanced attribution tracking feature:

#### 1\. Configure token mapping in the Adjust dashboard

  1. In your Adjust dashboard, create a new event token specifically for the `Install Attributed` event — you can also use an existing event token in case you have one.
  2. Copy the generated event token.
  3. Use this token in the Adjust destination configuration (explained below).


#### 2\. Adjust destination configuration in RudderStack

  1. In your RudderStack dashboard, add Adjust as a mobile device mode destination.
  2. Specify your Adjust [**App Token**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).
  3. In the **Map events to Adjust event tokens** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>), map the `Install Attributed` event to the event token obtained above.
  4. Save the mapping.


#### 3\. Enable automatic attribution tracking

Toggle on the **Enable Install Attribution** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) to automatically track the `Install Attributed` event when the app is installed for the first time.

### How attribution tracking works

By leveraging Adjust’s attribution callback on iOS and Android, the integration listens for an attribution change from Adjust’s SDK and triggers the event with the following Adjust attribution parameters:

Key| Value| Description  
---|---|---  
`provider`| `Adjust`| Hardcoded value  
`trackerToken`| `attribution.trackerToken`| Token of the link to which the device is currently attributed  
`trackerName`| `attribution.trackerName`| Name of the link to which the device is currently attributed  
`campaign.source`| `attribution.network`| Name of the network to which the device is currently attributed  
`campaign.name`| `attribution.campaign`| Name of the campaign to which the device is currently attributed  
`campaign.content`| `attribution.clickLabel`| The [click label](<https://help.adjust.com/en/article/user-rewards>) tagged with the install  
`campaign.adCreative`| `attribution.creative`| Name of the creative to which the device is currently attributed  
`campaign.adGroup`| `attribution.adGroup`| Name of the ad group to which the device is currently attributed  
  
An example of the attribution data automatically captured by the `Install Attributed` event is shown below:
    
    
    {
      "event": "Install Attributed",
      "properties": {
        "provider": "Adjust",
        "trackerToken": "abc123",
        "trackerName": "Campaign Name",
        "campaign": {
          "source": "google",
          "name": "summer_campaign",
          "content": "click_label",
          "adCreative": "banner_ad",
          "adGroup": "mobile_users"
        }
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> If any of the above values are unavailable, they are defaulted to `null`. This event is then sent to all the connected device mode and cloud destinations.

See the following FAQs for troubleshooting tips:

  * [Why are the `Install Attributed` events not appearing in my Adjust dashboard?](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/#install-attributed-events-not-appearing>)
  * [Why is the `Install Attributed` event not triggering?](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/#install-attributed-event-not-triggering>)


## Environment dependency on log level

RudderStack sends data to the Adjust environment depending on the `Logger.LogLevel` parameter (Android (Kotlin)) or `LoggerAnalytics.LogLevel` (iOS (Swift)) set in the SDK, as listed in the table below:

`LogLevel`| Adjust environment  
---|---  
`VERBOSE` / `DEBUG` / `INFO` / `WARN` / `ERROR`| Sandbox  
`NONE`| Production  
  
RudderStack sends data to the Adjust environment depending on the `RudderLogLevel` set in the SDK, as listed in the table below:

`RudderLogLevel`| Adjust environment| Adjust SDK `LogLevel`  
---|---|---  
`DEBUG` / `VERBOSE`| Sandbox| `VERBOSE`  
`NONE` / `ERROR` / `WARN` / `INFO`| Production| `ERROR`  
  
For more information on `RudderLogLevel`, see the following SDK documentation:

  * [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#configuring-your-rudderstack-client>)
  * [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#configuring-the-rudderstack-client>)


## Property mapping

RudderStack’s device mode integration automatically handles device information through the native Adjust SDK. The following table shows how RudderStack events map to Adjust’s native methods:

RudderStack event/method| Adjust SDK method| Description  
---|---|---  
`identify()`| `addSessionPartnerParameter()`| Sets user ID for session attribution  
`track()`  
Required| `trackEvent()`| Sends custom events to Adjust  
`reset()`| `resetSessionCallbackParameters()`| Resets user session data  
`properties.revenue`| Revenue tracking| Revenue amount for purchase events  
`properties.currency`| Revenue tracking| Currency code for revenue  
`properties.*`| Callback parameters| All properties as callback parameters  
`properties.*` (mapped)| Partner parameters| Mapped properties as partner parameters  
  
> ![info](/docs/images/info.svg)
> 
> Device mode automatically handles device identification through the native Adjust SDK, so you don’t need to manually provide `context.device` information like in cloud mode.

## Troubleshooting

Issue| Resolution  
---|---  
Events not appearing in Adjust dashboard| 

  * Verify that your event is mapped to an Adjust event token in the [dashboard settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).
  * Check that the event token exists in your Adjust dashboard.
  * Ensure your **App Token** is correctly configured.

  
Install attribution not working| 

  * Ensure the **Enable Install Attribution** setting is enabled in your [dashboard configuration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).
  * Verify that the `Install Attributed` event is properly mapped to an Adjust event token.
  * Check that you’re not using the native Adjust SDK alongside RudderStack’s integration.
  * See the [Install attribution troubleshooting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/faq/#install-attributed-events-not-appearing>) section for device unregistration steps.

  
Partner parameters not working| 

  * Verify that property mappings are configured in the **RudderStack Parameters to Partner Parameters** setting.
  * Check that only String values are being sent (RudderStack converts numeric values automatically).
  * Ensure the partner is set up in your Adjust dashboard.

  
SDK integration issues| 

  * **iOS (Obj-C)** : Ensure you’re using the correct version of `RudderAdjust` (v1.0.0+ for **iOS SDK v2**).
  * **Android (Java)** : Verify that all required permissions are added to your `AndroidManifest.xml`.
  * **Unity** : Make sure you’re not adding the native Adjust SDK separately.
  * **Flutter** : Ensure the dependency version is compatible with your Flutter version.

  
Environment configuration issues| Check the [Adjust environment dependency on log level](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/device-mode/#adjust-environment-dependency-on-log-level>) section to understand how your SDK log level affects the Adjust environment.