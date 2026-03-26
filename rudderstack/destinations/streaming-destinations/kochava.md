# Kochava

Send your event data from RudderStack to Kochava.

* * *

  * __6 minute read

  * 


[Kochava](<https://www.kochava.com/>) is a leading mobile measurement and app analytics platform that offers unique dynamic deep linking, audience segmenting and data accessibility features for your business.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/kochava>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Kochava** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Kochava, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Kochava**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Kochava as a destination, you will need to configure the following settings:

  * **App GUID** : Kochava generates a unique ID for your application called the **App GUID**. You can find this ID by going to your Kochava account and navigating to **Apps & Assets** > **All Apps**. You can then select your app to the view the App GUID.


The following two settings are applicable for iOS device mode only:

  * **Enable AppTrackingTransparency (ATT)** : Enable this setting if you want to enable the `AppTrackingTransparency` feature provided by the Kochava iOS SDK.


> ![info](/docs/images/info.svg)
> 
> Make sure to include the key `NSUserTrackingUsageDescription` in your `info.plist` along with a string value explaining why you are requesting authorization to track.

  * **Enable skAdNetwork** : Enable this setting if you want to enable the `skAdNetwork` feature provided by the Kochava iOS SDK.


## Adding device mode integration

Follow the below steps to add Kochava to your Flutter Project:

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file:


    
    
    rudder_integration_kochava_flutter: ^1.0.1
    

  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import `RudderIntegrationKochavaFlutter` in your application where you are initializing the SDK:


    
    
    import 'package:rudder_integration_kochava_flutter/rudder_integration_kochava_flutter.dart';
    

  4. Finally, change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationKochavaFlutter())
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

To add Kochava to your Android project and enable functionalities like push notifications, follow these steps :

  1. Open your project level `build.gradle` file, and add the following:


    
    
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
    

  2. Also, add the following under the `dependencies` section:


    
    
    implementation 'com.rudderstack.android.integration:kochava:1.0.0'
    implementation 'com.google.code.gson:gson:2.8.6'
    

  3. Initialize the RudderStack SDK in the `Application` class’ `onCreate()` method as shown:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(kochavaIntegration.FACTORY)
                .build()
        )
    

To add Kochava to your iOS project:

  1. Go your `Podfile` and add the `Rudder-Kochava` extension as shown below:


    
    
    pod 'Rudder-Kochava'
    

  2. After adding the dependency followed by `pod install` , you can add the imports to your `AppDelegate.m` file as shown:


    
    
    #import "RudderKochavaFactory.h"
    

  3. Finally, change the initialization of your `RudderClient` as shown:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderKochavaFactory instance]];
    [RudderClient getInstance:WRITE_KEY config:[builder build]];
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

RudderStack transforms the following events to Kochava’s standard events:

RudderStack event| Kochava standard event  
---|---  
`Product Added`| `Add to Cart`  
`Product Added to Wishlist`| `Add to Wishlist`  
`Checkout Started`| `Checkout Start`  
`Order Completed`| `Purchase`  
`Product Reviewed`| `Rating`  
`Products Searched`| `Search`  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack sends the rest of the events to Kochava as custom events.
>   * You can send an event with the name same as that of a Kochava standard event. Kochava accepts it as a standard event.
> 


A sample `track` event sent to Kochava:
    
    
    [[RudderClient sharedInstance] track:@"Product Added" properties:@{
    @"price": @2.0,
    @"product_id": @"product_id_a",
    @"product_name": @"Product Name A"
    }];
    

RudderStack changes the `Product Added` event to `Add to Cart` before passing it to Kochava along with the associated properties.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `screen` event to Kochava as a custom event.

A sample `screen` call is shown below:
    
    
    MainApplication.rudderClient.screen(
        "Sample Screen Name",
        RudderProperty().putValue("prop_key", "prop_value")
    )
    

In the above snippet, RudderStack captures all information related to the viewed screen, along with any additional info associated with that event. In Kochava, the above `screen` call is shown as **“screen view`Sample Screen Name` “** along with the properties.

## Configuring push notifications

Follow these steps to configure push notifications for Kochava for the platform of your choice:

  1. Register push notifications for your Android device in the Kochava dashboard.
  2. Add the following dependency in your project level `build.gradle` file inside the `buildscript`:


    
    
    dependencies {
            classpath 'com.google.gms:google-services:4.3.5'
     }
    

  3. Next, add the following dependencies and plugin to your app level `build.gradle` file:


    
    
    dependencies {
    // for push notifications
        implementation 'com.google.firebase:firebase-messaging:21.1.0'
    }
    apply plugin: 'com.google.gms.google-services'
    

  4. Place the `google-services.json` downloaded from the `Firebase console` into the root folder of your `app`.
  5. Passing the new Push Token received from FCM to the Kochava SDK. For more information, look into the **sample-kotlin** app.


    
    
    // Extending FirebaseMessagingService class
    class MyFirebaseMessagingService : FirebaseMessagingService() {
        // The onNewToken callback fires whenever a new token is generated.
        override fun onNewToken(token: String) {
            super.onNewToken(token)
            // Method to pass the push token to the Kochava native sdk
            registeredForPushNotificationsWithFCMToken(token)
        }
    }
    

  1. Add push notifications as a capability by navigating to **Target** > **Signing & Capabilities** of your app when opened in Xcode.
  2. Enable **Background Modes/Remote notifications** by navigating to **Targets** > **Your App** > **Capabilities** > **Background Modes** and then check **Remote notifications**.
  3. Register the push notifications for the iOS devices in your Kochava dashboard.
  4. Add the following code in your app just after initializing iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. to register the push notifications.


    
    
    #import <usernotifications>
    // register for push notifications
        UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];
        center.delegate = self;
        [center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge)
                              completionHandler:^(BOOL granted, NSError * _Nullable error) {
            if (granted) {
                dispatch_async(dispatch_get_main_queue(), ^(void) {
                    [[UIApplication sharedApplication] registerForRemoteNotifications];
                });
            }
        }];
    

  5. Add the below handlers to handle the tokens and push notifications accordingly:


    
    
    #import <rudderkochavaintegration.h>
    
    - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken
    {
        [[RudderKochavaIntegration alloc] registeredForRemoteNotificationsWithDeviceToken:deviceToken];
    }
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler
    {
        completionHandler(UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
    }
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler
    {
        [[RudderKochavaIntegration alloc] receivedRemoteNotification:response.notification.request.content.userInfo withActionString:response.actionIdentifier];
    }
    

## FAQ

#### Where do I get the Kochava App GUID?

To get your Kochava app GUID, follow these steps:

  1. [Log in to Kochava](<https://go.kochava.com/session>). Then, go to your account and select the application for the specific campaign.
  2. Under **Apps & Assets**, select **All Apps**
  3. Click the desired app for which you want the procure the App GUID.
  4. You will be able to see the App GUID under the title of your application, within the details.


For more information, see the [Kochava support guide](<https://support.kochava.com/reference-information/locating-an-app-guid/>).