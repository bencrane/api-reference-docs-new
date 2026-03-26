# Adobe Analytics Mobile Device Mode Integration

Send events to Adobe Analytics via the RudderStack mobile device mode.

* * *

  * __4 minute read

  * 


This document covers the necessary settings and configurations to send events to Adobe Analytics via your mobile device mode.

> ![info](/docs/images/info.svg)
> 
> Mobile [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) refers to using the Android (Java) or iOS (Obj-C) SDK to send your events directly to Adobe Analytics.

To configure Adobe Analytics via the mobile device mode, follow these steps:

  1. Click the **Manage Apps** option on the left nav bar on your Adobe Mobile Services dashboard.
  2. **Add** your app or click an existing app and configure the required settings under the **Manage App Settings** tab:

[![](/docs/images/event-stream-destinations/adobe-mobile-services-add-app.webp)](</docs/images/event-stream-destinations/adobe-mobile-services-add-app.webp>)

  3. Click the **Config File** option present at the bottom of the same page:

[![](/docs/images/event-stream-destinations/adobe-mobile-services-config-file.webp)](</docs/images/event-stream-destinations/adobe-mobile-services-config-file.webp>)

### Android (Java)

For Android (Java), place the `ADBMobileConfig.json` file inside your app under `src/main/assets/`.

Then, follow the instructions in the [Adobe documentation](<https://experienceleague.adobe.com/docs/mobile-services/android/getting-started-android/dev-qs.html?lang=en>) to create the report suite.

### iOS (Obj-C)

For iOS (Obj-C), drag and drop the `ADBMobileConfig.json` under the `Pods` section in the `Project Navigator`and verify the following:

  * The `Copy items if needed` checkbox is selected.
  * `Create groups` is selected.
  * None of the checkboxes in the `Add to targets` section is selected.


In **File Inspector** , add the JSON file to the `AdobeMobileSDK` target. Then, follow the instructions in the [Adobe documentation](<https://experienceleague.adobe.com/docs/media-analytics/using/sdk-implement/setup/set-up-ios.html?lang=en#>) to create the report suite.

## Adding device mode integration

Follow these steps to add Adobe Analytics to your iOS project:

  1. In your `Podfile`, add the `Rudder-Adobe` extension:


    
    
    pod 'Rudder-Adobe'
    

  2. After adding the dependency followed by `pod install` , add the imports to your `AppDelegate.m` file as shown:


    
    
    #import <rudder>
    #import <rudderadobefactory.h>
    

  3. Then, add the initialization of your `RSClient` as shown:


    
    
    RSConfigBuilder *configBuilder = [[RSConfigBuilder alloc] init];
    [configBuilder withDataPlaneUrl:DATA_PLANE_URL];
    [configBuilder withFactory:[RudderAdobeFactory instance]];
    [RSClient getInstance:<your_write_key> config:[configBuilder build]];
    

To add Adobe Analytics to your Android project, follow these steps :

  1. Open your `app/build.gradle` file and add the following under the `dependencies` section :


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.google.code.gson:gson:2.8.6'
    implementation 'com.rudderstack.android.integration:adobe:1.0.0'
    
    // Adobe Analytics
    implementation 'com.adobe.mobile:adobeMobileLibrary:4.18.2'
    

  2. Initialize the RudderStack SDK in the `Application` class’ `onCreate()` method as shown:


    
    
    // initializing Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(AdobeIntegrationFactory.FACTORY)
                .build()
        )
    

  3. For Android, make sure you add these permissions to your `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

## Dashboard settings to send events via mobile device mode:

Configure the following settings in the RudderStack dashboard to use the mobile device mode:

  * Set the **Heartbeat Tracking Server URL** and it should be in the format of `[your_namespace].hb.omtrdc.net`.
  * Toggle **Check for Heartbeat calls to be made over HTTPS** to enable or disable the SSL mode.
  * Enter **Prefix to add before all contextData property** to append a prefix before a custom property.
  * Select **Product Identifier** to look for `Product Id`. By default, it is set to `Product Name`.


## Sending events

Map all events defined in the Adobe Mobile Services dashboard in the **Map Rudder Events to Adobe Custom Events** dashboard setting.

## Sending custom properties

Map all properties defined at the Adobe Mobile Services dashboard in the **Map Rudder Context data to Adobe Context Data** dashboard setting.

> ![warning](/docs/images/warning.svg)
> 
> For mobile device mode, RudderStack currently does not support the [Initialize Heartbeat](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/adobe-analytics-heartbeat/#initialize-heartbeat>) and [Heartbeat Playhead Update](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/adobe-analytics-heartbeat/#heartbeat-playhead-update>) video events.

## Identify

When you make an `identify` call, RudderStack sets the Adobe `visitorId` to the value of the user’s RudderStack `userId`.

A sample `identify` call looks like the following:
    
    
    [[RSClient sharedInstance] identify:@"Adobe_iOS_user"];
    
    
    
    MainApplication.rudderClient.identify("AdobeUser");
    

## Track

When you make a `track` call, RudderStack sends an Adobe `trackAction` event and passes your event name and any associated properties mapped to Adobe as context data values.

A sample `track` call is as shown:
    
    
    [[RSClient sharedInstance] track:@"Order Completed" properties:@{
        @"orderId" : @2002,
        @"category" : @"Cloths",
        @"productId" : @"2200013",
        @"name": @"Shirt",
        @"price" : @10001,
        @"quantity" : @12
    }];
    
    
    
    MainApplication.rudderClient.track("Order Completed",
      RudderProperty()
        .putValue("orderId", "12345")
        .putValue("category", "category")
        .putValue("revenue", 99.9)
        .putValue("shipping", 13.99)
        .putValue("tax", 20.99)
        .putValue("promotion_id", "PROMO_1234")
      );
    

## Screen

When you make a `screen` call, RudderStack sends an Adobe `trackState` event and passes the screen name along with any associated properties mapped to Adobe as context data values.

A sample `screen` call looks like the following:
    
    
    [[RSClient sharedInstance] track:@"Home Screen"
      properties:@{
          @"Width" : @"13"
      }];
    
    
    
    MainApplication.rudderClient.screen("Home Screen",
          RudderProperty()
              .putValue("Width",12)
      )
    

## Reset

Calling the `reset` API sets the user’s Adobe `visitorId` to `null`.

> ![info](/docs/images/info.svg)
> 
> The default value of Adobe’s `visitorId` is `null` until you explicitly set it (by calling `identify`).

A sample `reset` call is as shown:
    
    
    [[RSClient sharedInstance] reset];
    
    
    
    MainApplication.rudderClient.reset()
    

## Flush

Calling the `flush` method immediately sends all locally queued events to Adobe.

A sample `flush` call is as follows:
    
    
    MainApplication.rudderClient.flush()
    

> ![info](/docs/images/info.svg)
> 
> RudderStack supports the `flush` call only in Android (Java) SDK.