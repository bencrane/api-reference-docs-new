# Visual Studio App Center

Send your event data from RudderStack to Visual Studio App Center.

* * *

  * __8 minute read

  * 


[App Center](<https://appcenter.ms/>) is Microsoft’s cross-platform build automation and management platform that lets you seamlessly manage your app’s lifecycle. With App Center, you can easily manage and automate your builds, effectively test your apps in the cloud, and monitor their real-time usage with the help of crash data and analytics.

RudderStack lets you send your event data to App Center via its native web SDKs.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , React Native , Cordova, Flutter
  * Refer to it as **App Center** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the platform supports sending events to App Center, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source and select **App Center** from the list of destinations.
  * Name your destination, and click **Next**. You should be able to see the following screen:

[![Connection settings for App Center destination](/docs/images/appcenter.webp)](</docs/images/appcenter.webp>)

  * Enter the relevant details and click **Next** to complete the setup. The **API Secret Key** can be found as **App Secret** on the **Getting Started** page or **Settings** page on the App Center portal.


## Adding device mode integration

Once you add App Center as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>), follow these steps to add it to your mobile project depending on your integration platform:

To add AppCenter to your React Native project, follow these steps:

  1. Add the RudderStack-App Center module to your app as shown:


    
    
    npm install @rudderstack/rudder-integration-appcenter-react-native
    ## OR ##
    yarn add @rudderstack/rudder-integration-appcenter-react-native
    

> ![info](/docs/images/info.svg)
> 
> Make sure the `minSdkVersion` of your `build.gradle` in the root of `android` directory is atleast `21`

2\. Run `pod install` inside the `ios` directory of your project adding `@rudderstack/rudder-integration-appcenter-react-native` to your project. 3\. Finally, import the module you added above and add it to your SDK initialization code:
    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native"
    import appcenter from "@rudderstack/rudder-integration-appcenter-react-native"
    
    const config = {
      dataPlaneUrl: DATA_PLANE_URL,
      trackAppLifecycleEvents: true,
      withFactories: [appcenter],
    }
    rudderClient.setup(WRITE_KEY, config)
    

Follow the below steps to add App Center to your Flutter Project:

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file.


    
    
    rudder_integration_appcenter_flutter: ^1.1.1
    

  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import the `RudderIntegrationAppcenterFlutter` in your application where you are initializing the SDK.


    
    
    import 'package:rudder_integration_appcenter_flutter/rudder_integration_appcenter_flutter.dart';
    

  4. Finally, change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationAppcenterFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

> ![info](/docs/images/info.svg)
> 
> For Android platform, make sure that the `android.defaultConfig.minSdkVersion` is set to atleast `21` by checking it in the `android/app/build.gradle` file.

> ![info](/docs/images/info.svg)
> 
> For iOS platform, you can link App Center as a framework instead of a library with your application by linking it statically as shown below:
>     
>     
>     use_frameworks! :linkage=> :static
>     

To add App Center to your Cordova project, follow these steps:

  1. Navigate to the root folder of your application and run the following command::


    
    
    cordova plugin add rudder-integration-appcenter-cordova
    

  2. Add the platforms that you want to target for your app:


    
    
    cordova platform add ios
    cordova platform add android
    

  3. Run the following command to build the project for all platforms:


    
    
    cordova build
    

  4. Add the following code in the `onDeviceReady()` function of your home page to initialize the SDK:


    
    
    RudderClient.initialize(WRITE_KEY , {
      dataPlaneUrl: DATA_PLANE_URL,
      factories: [RudderAppCenterFactory]
    })
    

> ![info](/docs/images/info.svg)
> 
> Make sure to use the `await` keyword with the `initialize` call.

Your Android project must be on **version 5.0 (API level 21) or higher** for RudderStack to be able to send events to App Center.  


Once confirmed, follow these steps to add App Center to your Android project:

  1. Add the following `dependencies` to your `app/build.gradle` file as shown:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.7+'
    implementation 'com.rudderstack.android.integration:appcenter:1.+'
    implementation 'com.google.code.gson:gson:2.8.6'
    

  2. Also add the App Center `analytics` depedencies to your `app/build.gradle` as shown below:


    
    
    def appCenterSdkVersion = '4.1.0'
    implementation "com.microsoft.appcenter:appcenter-analytics:${appCenterSdkVersion}"
    

  3. Make sure that the `minSdkVersion` in your `app/build.gradle` is atleast `21`.


    
    
    defaultConfig {
      minSdkVersion 21
    }
    

  4. Finally, change the initialization of your `RudderClient` in your `Application` class:


    
    
    // initializing Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(AppcenterIntegrationFactory.FACTORY)
                .build()
        )
    

Follow these steps to add App Center to your iOS project:

  5. Go to your `Podfile` and add the `Rudder-AppCenter` extension


    
    
    pod 'Rudder-AppCenter'
    

  6. After adding the dependency followed by `pod install` , you can add the imports to your `AppDelegate.m` file:


    
    
    #import <rudderappcenterfactory.h>
    

  7. Finally, change the initialization of your `RudderClient` as shown:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:<your_data_plane_url>];
    [builder withFactory:[RudderAppCenterFactory instance]];
    [RSClient getInstance:<your_write_key> config:[builder build]];
    

> ![info](/docs/images/info.svg)
> 
> To use App Center, your iOS project must be set up in Xcode 11 or later on macOS version 10.14.4 or later. Also, you must be targeting devices running on iOS 9.0 or later.

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for App Center v4.4.1 and above.

Follow these steps to add App Center to your iOS project:

  1. Install `RudderAppCenter` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderAppCenter', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Next, import the SDK depending on your preferred platform:


    
    
    @import RudderAppCenter;
    
    
    
    import RudderAppCenter
    

  4. Next, add the imports to your `AppDelegate` file under `didFinishLaunchingWithOptions` method:


    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderAppCenterDestination alloc] init]];
    
    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderAppCenterDestination())
    

## Track

A `track` call lets you track custom events as they occur in your web application.

A sample `track` call looks like the following:
    
    
    [[RSClient sharedInstance] track:@"Product Clicked" properties:@{
        @"product_id" : @"pr01",
        @"name" : @"Cadbury"
    }];
    

> ![info](/docs/images/info.svg)
> 
> The above `track` call is directly passed on to App Center via its `trackEvent` api in both the RudderStack Android (Java) and iOS (Obj-C) SDKs.

The `eventProperties` object should only contain the values of type `String` and `Number`\- the other property types will be simply ignored, if sent.

For example, if `eventProperties` is set as:
    
    
    {
      "colours": [
        "red",
        "black"
      ],
      "city": "New Orleans",
      "state": "Louisiana"
    }
    

then RudderStack will send the data to App Center as:
    
    
    {
      "city": "New Orleans",
      "state": "Louisiana"
    }
    

## Screen

The `screen` method allows you to record whenever a user sees the mobile screen, along with any associated optional properties. This call is similar to the `page` call, but is exclusive to your mobile device.

A sample `screen` call using the RudderStack Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. looks like the following code snippet:
    
    
    [[RSClient sharedInstance] screen:@"Home" properties:@{
        @"category" : @"launcher"
    }];
    

In the above snippet, RudderStack captures the information related to the screen being viewed, such as screen’s name and category.

> ![info](/docs/images/info.svg)
> 
> The above `screen` call is directly passed on to App Center as a `track` event via its `trackEvent` API, with event name as `Viewed {screen name} screen` along with the its properties. The above example will be sent as a `track` event with name `Viewed MainActivity screen` along with its properties.

## Opting in/out of sending user data to App Center

Any users visting your app can express their consent over sending data to App Center. Based on this consent you can either opt in or out of sending that user’s data to App Center.

Refer to the section below for more details on how to use this feature.

Firstly import the `AppCenterIntegrationFactory` as shown below:
    
    
    import {
      enableAnalytics,
      disableAnalytics,
    } from '@rudderstack/rudder-integration-appcenter-react-native';
    

Then add the below script just after the initalization of the React Native SDK:

  * To enable App Center Analytics:


    
    
    await rudderClient.registerCallback("App Center", () => {
      enableAnalytics();
    });
    

  * To disable App Center Analytics:


    
    
    await rudderClient.registerCallback("App Center", () => {
      disableAnalytics();
    });
    

Firstly import Appcenter’s `Analytics` Module as shown below: `groovy import com.microsoft.appcenter.analytics.Analytics;`

Then add the below script just after the initialization of the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. :
    
    
    rudderClient.onIntegrationReady("App Center") {
        // have your own logic to get the user consent
        if (userConsent) {
            // enabling appcenter's analytics module
            Analytics.setEnabled(true)
        } else {
            // disabling appcenter's analytics module
            Analytics.setEnabled(false)
        }
    }
    

Firstly import the Appcenter’s `Analytics` Module as shown below:
    
    
    @import AppCenterAnalytics;
    

Then add the below script just after the initialization of the iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. :
    
    
    if(userConsent)
    {
        // enabling appcenter's analytics module
        [MSACAnalytics setEnabled:true];
    }
    else
    {
        // disabling appcenter's analytics module
        [MSACAnalytics setEnabled:false];
    }
    

## FAQ

#### How do I get the App Center API secret?

The **API Secret Key** can be found as **App Secret** on the **Getting Started** page or **Settings** page on your App Center portal.

#### What is transmission interval?

The App Center SDK uploads logs in a batch of 50. If the SDK doesn’t have 50 logs to send, it will still send logs after 3 seconds (set by default). There can be a maximum of 3 batches sent in parallel. In this case, this interval of 3 seconds is the **transmission interval**. Note that the value of this transmission interval must always be between 3 seconds and 86400 seconds (one day).