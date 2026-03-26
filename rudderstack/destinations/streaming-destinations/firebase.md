# Firebase

Send your event data from RudderStack to Firebase.

* * *

  * __12 minute read

  * 


[Firebase](<https://firebase.google.com/>) is a popular mobile platform powered by Google. It helps you to quickly develop high-quality, enterprise-grade applications and grow your business.

RudderStack supports Firebase as a [mobile device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) to which you can seamlessly send your customer data for analytics.

> ![warning](/docs/images/warning.svg)
> 
> Firebase device mode support is not available for the [Cordova](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-cordova-sdk/>) SDK.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, React Native , Flutter
  * Refer to it as **Firebase** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Android (Java)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Firebase, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Firebase**.
  2. Assign a name to the destination and click **Next**.


### Connection settings

Connect this destination to your Android (Java)/iOS (Obj-C)/Unity/React Native source. You should then see the following screen:

[![Firebase connection settings](/docs/images/event-stream-destinations/firebase-connection-settings.webp)](</docs/images/event-stream-destinations/firebase-connection-settings.webp>)

  * **Client-side Events Filtering** : Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this setting.


As this is a device mode-only integration, click **Next** to complete the destination setup.

### Add device mode integration

Depending on your platform of integration, follow the steps below to add Firebase to your project:

Follow the steps in this section to add Firebase to your Kotlin project.

[![Github Badge](https://img.shields.io/maven-central/v/com.rudderstack.integration.kotlin/firebase?style=flat)](<https://central.sonatype.com/artifact/com.rudderstack.integration.kotlin/firebase>)

#### 1\. Project setup

> ![info](/docs/images/info.svg)
> 
> See the [Firebase documentation](<https://firebase.google.com/docs/android/setup>) for more information on setting up your project.

  1. Register your mobile app in the [Firebase console](<https://console.firebase.google.com/>).
  2. Once you have successfully created the app in the Firebase console, you will be prompted to download the `google-services.json` file.
  3. Copy this file in the `app` folder of your project. It contains all necessary information about the project and the integration.
  4. To make the values in your `google-services.json` config file accessible to the Firebase SDK, you will need the [Google services Gradle plugin](<https://developers.google.com/android/guides/google-services-plugin>) (`google-services`).


  * In your root-level (project-level) Gradle file (`<project>/build.gradle.kts` or `<project>/build.gradle`), add the Google services plugin as a dependency:


**Kotlin DSL (`build.gradle.kts`)**
    
    
    plugins {
      // Add the dependency for the Google services Gradle plugin
      id("com.google.gms.google-services") version "4.4.2" apply false
    }
    

**Groovy DSL (`build.gradle`)**
    
    
    plugins {
      // Add the dependency for the Google services Gradle plugin
      id 'com.google.gms.google-services' version '4.4.2' apply false
    }
    

  * In your module (app-level) Gradle file (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the Google services plugin:


**Kotlin DSL (`build.gradle.kts`)**
    
    
    plugins {
      // Add the Google services Gradle plugin
      id("com.google.gms.google-services")
    }
    

**Groovy DSL (`build.gradle`)**
    
    
    plugins {
      // Add the Google services Gradle plugin
      id 'com.google.gms.google-services'
    }
    

#### 2\. Add dependencies

In your module (app-level) Gradle file (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependencies for the RudderStack Firebase integration:
    
    
    dependencies {
      // ...
      
      // Add Rudder Kotlin and Firebase integration:
      implementation("com.rudderstack.sdk.kotlin:android:<latest-version>")
      implementation("com.rudderstack.integration.kotlin:firebase:<latest-version>")
    
      // Add Firebase dependencies:
      // Import the Firebase BoM
      implementation(platform("com.google.firebase:firebase-bom:33.7.0"))
    
      // When using the BoM, you don't specify versions in Firebase library dependencies
    
      // Add the dependency for the Firebase SDK for Google Analytics
      implementation("com.google.firebase:firebase-analytics")
    }
    

#### 3\. Initialize the SDK and integration

Add the SDK initialization and the `Rudder-Firebase` integration in your `Application` class:
    
    
    import android.app.Application
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration
    
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
            
            analytics.add(FirebaseIntegration())
        }
    }
    

[![Github Badge](https://img.shields.io/github/v/tag/rudderlabs/integration-swift-firebase?label=Swift Package Manager)](<https://github.com/rudderlabs/integration-swift-firebase/>)

#### Add Firebase to your iOS project

  1. Register your app in the [Firebase console](<https://console.firebase.google.com/>). It will then prompt you to download the `GoogleServices-Info.plist` file.

  2. Add the `GoogleServices-Info.plist` file to the root of your XCode project.


#### Integrate the Firebase SDK with your project

  1. In Xcode, select **File > Add Package Dependencies…**.

![](/docs/images/event-stream-sources/swift/add-package-dependencies.webp)

  2. Enter the below package repository URL in the search bar:


    
    
    https://github.com/rudderlabs/integration-swift-firebase/
    

  3. Select the latest version and the target to which you want to add the package.
  4. Click **Add Package**.


Alternatively, you can add the dependency to your `Package.swift` file, as shown:
    
    
    dependencies: [
        .package(url: "<https://github.com/rudderlabs/integration-swift-firebase.git>", from: "<latest_integration_version>")
    ]
    

#### Usage

  1. Import the SDK and integration:


    
    
    import RudderStackAnalytics
    import RudderIntegrationFirebase
    

  2. Add `FirebaseIntegration` to your `analytics` instance:


    
    
    // Initialize RudderStack Analytics
    let analytics = Analytics(
        configuration: Configuration(
            writeKey: "<WRITE_KEY>",
            dataPlaneUrl: "<DATA_PLANE_URL>"
        )
    )
    
    // Add Firebase Integration
    analytics.add(plugin: FirebaseIntegration())
    

Follow these steps to add Firebase to your Unity project:

  1. Register your project in the [Firebase Console](<https://console.firebase.google.com>). Currently, RudderStack supports only Android and iOS platforms for Unity.
  2. After adding the project, Firebase will prompt you to download the `google-services.json` for Android and `GoogleServices-Info.plist` for iOS.
  3. Add those two files to your project’s `Assets` folder.
  4. Integrate the RudderStack core SDK with your project. For more information, refer to the [Unity SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-unity-sdk/>).
  5. Download and import the Firebase Unity SDK and follow the [instructions](<https://firebase.google.com/docs/unity/setup>) to add the Firebase SDK (specifically, `FirebaseAnalytics.unitypackage`) to your project.
  6. Download the [RudderStack Firebase Extension](<https://github.com/rudderlabs/rudder-sdk-unity/raw/master/Integrations/Firebase/rudder-integration-firebase-unity.unitypackage>) from the GitHub page and import it in your project.
  7. Attach the `RudderPreferbs.prefab` file from `Rudder` to your main `GameObject`
  8. Finally, change the SDK initialization using the following code snippet:


    
    
    // Build your config
    RudderConfigBuilder configBuilder = new RudderConfigBuilder()
        .WithEndPointUrl(<data_plane_url>)
        .WithFactory(RudderFirebaseIntegrationFactory.GetFactory());
    
    // get instance for RudderClient
    RudderClient rudderClient = RudderClient.GetInstance(
        <source_write_key>,
        configBuilder.Build()
    );
    

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * Starting with v3.0.0, the React Native SDK [supports the new React Native architecture](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/#enable-new-react-native-architecture-support>).
>   * RudderStack recommends using the [latest version](<https://www.npmjs.com/package/@rudderstack/rudder-integration-firebase-react-native>) of the Firebase React Native device mode to get the latest updates and performance enhancements.
> 


  1. Register your Android and iOS applications in the [Firebase console](<https://console.firebase.google.com/>).
  2. Once you have successfully created the applications in the Firebase console, you will be prompted to download the `google-services.json` and `GoogleServices-Info.plist` files.
  3. Add the RudderStack React Native SDK to your app by referring to the [React Native SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>).
  4. Add the RudderStack-Firebase React Native module to your app using the following command:


    
    
    npm install @rudderstack/rudder-integration-firebase-react-native
    // OR //
    yarn add @rudderstack/rudder-integration-firebase-react-native
    

  5. Next, import the module you added above and add it to your SDK initialization code as shown:


    
    
    import rudderClient from '@rudderstack/rudder-sdk-react-native';
    import firebase from "@rudderstack/rudder-integration-firebase-react-native";
    
    const config = {
        dataPlaneUrl: <data_plane_url>,
        trackAppLifecycleEvents: true,
        withFactories: [firebase]
    };
    
    rudderClient.setup(<source_write_key>, config);
    

  6. Navigate to your app’s `android` folder and follow the steps below:


  * Copy the `google-services.json` file in the `app` folder of your Android project. This file contains all necessary information about the project and the integration.
  * Add the `classpath` under `dependencies` to your project level `build.gradle` file:


    
    
    buildscript {
      repositories {
        google()
      }
      dependencies {
        // add this line
        classpath 'com.google.gms:google-services:4.3.3'
      }
    }
    

  * Once you have completed the steps above, you can add the plugins and dependencies to your `app/build.gradle` file:


    
    
    apply plugin: 'com.android.application'
    apply plugin: 'com.google.gms.google-services'
    

  * Then, add the necessary permissions under `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

  7. For React-Native Firebase version 1.0.16 and above, if you encounter any static libraries issue while installing the Rudder-Firebase pods, add the below lines in your iOS app’s `Podfile`:


    
    
    pod 'FirebaseCore', :modular_headers => true
    pod 'GoogleUtilities', :modular_headers => true
    

  8. Finally, navigate to your app’s `iOS` folder and follow these steps:


  * Install all required pods using the `pod install` command.
  * Add the `GoogleServices-Info.plist` file to the root of your XCode project.


Follow the below steps to add Firebase to your Flutter Project:

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file.


    
    
    rudder_integration_firebase_flutter: ^1.0.1
    

  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import the `RudderIntegrationFirebaseFlutter` in your application where you are initializing the SDK.


    
    
    import 'package:rudder_integration_firebase_flutter/rudder_integration_firebase_flutter.dart';
    

  4. Change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationFirebaseFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

  5. Navigate to your app’s `android` folder and follow the below steps:


  * Copy the `google-services.json` file in the `app` folder of your Android project. This file contains all necessary information about the project and the integration.
  * Add the `classpath` under `dependencies` to your project level `build.gradle` file:


    
    
    buildscript {
      repositories {
        google()
      }
      dependencies {
        // add this line
        classpath 'com.google.gms:google-services:4.3.3'
      }
    }
    

  * Add `mavenCentral()` as a repository under `buildscript.repositories` and `allprojects.repositories` to your project level `build.gradle` file:


    
    
    buildscript {
      repositories {
        google()
        // should be added
        mavenCentral()
      }
      dependencies {
        classpath 'com.google.gms:google-services:4.3.3'
      }
    }
    allprojects {
      repositories {
          google()
          // should be added
          mavenCentral()
      }
    }
    

  * Next, add the plugins and dependencies to your `app/build.gradle` file:


    
    
    apply plugin: 'com.android.application'
    apply plugin: 'com.google.gms.google-services'
    

  * Add the necessary permissions under `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

  6. Finally, navigate to your app’s `iOS` folder and add the `GoogleServices-Info.plist` file to the root of your XCode project.


> ![info](/docs/images/info.svg)
> 
> Use the [latest version](<https://search.maven.org/artifact/com.rudderstack.android.integration/firebase>) of the Firebase Android device mode to get the latest updates, bug fixes, and performance enhancements.

Follow these steps to add Firebase to your Android project:

  1. Register your mobile app in the [Firebase console](<https://console.firebase.google.com/>).
  2. Once you have successfully created the app in the Firebase console, you will be prompted to download the `google-services.json` file.
  3. Copy this file in the `app` folder of your project. It contains all necessary information about the project and the integration.
  4. Add the `classpath` under `dependencies` to your project level `build.gradle`:


    
    
    buildscript {
      repositories {
        google()
      }
      dependencies {
        // add this line
        classpath 'com.google.gms:google-services:4.3.3'
      }
    }
    

  5. Now, you can add the `plugins` and `dependencies` to your `app/build.gradle` file:


    
    
    apply plugin: 'com.android.application'
    apply plugin: 'com.google.gms.google-services'
    

  6. Then, add the `mavenCentral` repository:


    
    
    repositories {
      mavenCentral()
    }
    

  7. Add the RudderStack-Firebase SDK extension along with the `core` SDK under `dependencies`:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.rudderstack.android.integration:firebase:2.+'
    
    //Firebase
    implementation platform('com.google.firebase:firebase-bom:28.4.2')
    implementation 'com.google.firebase:firebase-analytics'
    

  8. Next, add the necessary `permissions` under `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

  9. Finally, change the SDK initialization in your `Application` class:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(FirebaseIntegrationFactory.FACTORY)
                .build()
        )
    

> ![info](/docs/images/info.svg)
> 
> If you’re using the Firebase iOS device mode v1.0.2, update to the [latest version](<https://cocoapods.org/pods/Rudder-Firebase>) to get the latest updates, bug fixes, and performance enhancements.

Follow these steps to add Firebase to your iOS project:

  1. Register your app in the [Firebase console](<https://console.firebase.google.com>). It will then prompt you to download the `GoogleServices-Info.plist` file.
  2. Add the file to the root of your XCode project.
  3. Go to your `Podfile` and add the `Rudder-Firebase` extension along with the core SDK using the following code:


    
    
    pod 'Rudder-Firebase', '~> 2.0.5'
    

> ![info](/docs/images/info.svg)
> 
> `Rudder-Firebase` version `2.0.5` is tested and fully compatible with `Firebase/Analytics` version `8.15.0`.

4\. After adding the dependency followed by the `pod install` command, you can add the imports to your `AppDelegate.m` file:
    
    
    #import "RudderFirebaseFactory.h"
    

  5. Finally, change the SDK initialization, as shown in the following snippet:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:<data_plane_url>];
    [builder withFactory:[RudderFirebaseFactory instance]];
    [builder withLoglevel:RSLogLevelDebug];
    [RSClient getInstance:<write_key> config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Firebase v8.15.0 and above.

Follow these steps to add Firebase to your iOS project:

  1. Add Firebase as a destination in the [RudderStack dashboard](<https://app.rudderstack.com>).
  2. Register your app in the [Firebase console](<https://console.firebase.google.com>). It will then prompt you to download the `GoogleServices-Info.plist` file.
  3. Download and place this file in your project.
  4. Install `RudderFirebase` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderFirebase', '~> 1.0.0'
    

  5. Run the `pod install` command.
  6. Then, import the SDK depending on your preferred platform:


    
    
    import RudderFirebase
    
    
    
    @import RudderFirebase;
    

  7. Next, add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderFirebaseDestination alloc] init]];
    
    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderFirebaseDestination())
    

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call sets the `userId` through the `setUserId` method from `FirebaseAnalytics`. RudderStack sets the other user properties from `RudderTraits` to Firebase using the `setUserProperty` method.

> ![info](/docs/images/info.svg)
> 
> RudderStack ignores `age`, `gender`, and `interest`, as these properties are reserved by Google.
    
    
    [[RSClient sharedInstance] identify:@"test_user_id"
                                 traits:@{@"foo": @"bar",
                                          @"foo1": @"bar1",
                                          @"email": @"test@gmail.com",
                                          @"key_1" : @"value_1",
                                          @"key_2" : @"value_2"
                                 }
    ];
    

## Track

RudderStack’s [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events are mapped to the standard Firebase events wherever possible.

### Event mapping

RudderStack maps the following events to the standard Firebase events:

RudderStack Event| Firebase Event  
---|---  
`Payment Info Entered`| `add_payment_info`  
`Product Added`| `add_to_cart`  
`Product Added to Wishlist`| `add_to_wishlist`  
`Application Opened`| `app_open`  
`Checkout Started`| `begin_checkout`  
`Order Completed`| `purchase`  
`Order Refunded`| `refund`  
`Products Searched`| `search`  
`Cart Shared`| `share`  
`Product Shared`| `share`  
`Product Viewed`| `view_item`  
`Product List Viewed`| `view_item_list`  
`Product Removed`| `remove_from_cart`  
`Product Clicked`| `select_content`  
`Promotion Viewed`| `view_promotion`  
`Promotion Clicked`| `select_promotion`  
`Cart Viewed`| `view_cart`  
  
The following Firebase events are **not** mapped to any RudderStack event:

  * `number_of_nights`
  * `number_of_rooms`
  * `number_of_passengers`
  * `origin`
  * `destination`
  * `start_date`
  * `end_date`
  * `travel_class`
  * `item_list_name`
  * `creative_slot`
  * `location_id`
  * `transaction_id`
  * `screen_class`


> ![info](/docs/images/info.svg)
> 
> RudderStack passes all event-related properties to Firebase. The nested values in the properties are converted to JSON using [GSON](<https://github.com/google/gson>).

### Property mapping

RudderStack maps the following event properties to the standard Firebase properties:

RudderStack property| Firebase property  
---|---  
`category`| `item_category`  
`cart_id`,`product_id`| `item_id`  
`share_via`| `method`  
`query`| `search_term`  
`revenue`, `value`, `total`| `value`  
`currency`| `currency`  
`tax`| `tax`  
`shipping`| `shipping`  
`coupon`| `coupon`  
`name`| `name`, `promotion_name`  
`quantity`| `quantity`  
`price`| `price`  
`payment_method`| `payment_type`  
`list_id`| `item_list_id`  
`promotion_id`| `promotion_id`  
`creative`| `creative_name`  
`affiliation`| `affiliation`  
  
Along with mapping the above list of the standard property names, RudderStack exhibits the following behavior:

  * Converts the event names to the lower case.
  * Trims the whitespaces at the start and the end.
  * Replaces a space with an underscore.


> ![info](/docs/images/info.svg)
> 
> Firebase enforces a [strict event name length limit](<https://firebase.google.com/docs/reference/cpp/group/event-names#summary>) of 40 characters. RudderStack takes a substring of 40 characters (from the beginning) if the event names exceed this permitted value.

A sample `track` call sent from the iOS (Obj-C) SDK is shown below:
    
    
    [[RSClient sharedInstance] track:@"simple_track_with_props" properties:@{
        @"key_1" : @"value_1",
        @"key_2" : @"value_2"
    }];
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method lets you record whenever a user sees their mobile screen along with any optional properties about the viewed screen.

A sample `screen` call is as shown:
    
    
    [[RSClient sharedInstance] screen:@"Home Screen"
                                  properties:@{
                                      @"Width" : @"13"
                                  }];
    

## Reset

The `reset` method resets the user identification.

A sample `reset` call is shown below:
    
    
    [[RSClient getInstance] reset];
    
    
    
    RudderClient.getInstance()?.reset()
    

## Debugging

You can check the events and their properties in the [Firebase DebugView](<https://firebase.google.com/docs/analytics/debugview>). To enable it for Android, run the following command from your terminal:
    
    
    $ adb shell setprop debug.firebase.analytics.app <your_package_name>
    

For iOS, specify the following in your command line argument in XCode:
    
    
    -FIRAnalyticsDebugEnabled
    

## FAQ

#### How do I disable automatic screen tracking while using the RudderStack SDKs?

  * For Android, nest the following setting within the `<application>` tag of your `AndroidManifest.xml` file:


    
    
    <meta-data android:name="google_analytics_automatic_screen_reporting_enabled" android:value="false" />
    

  * For iOS, set `FirebaseAutomaticScreenReportingEnabled` to `NO` (Boolean) in your `Info.plist`.


For more information, refer to the [Firebase documentation](<https://firebase.google.com/docs/analytics/screenviews#automatically_track_screens>).