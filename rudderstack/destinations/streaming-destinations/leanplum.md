# Leanplum

Send your event data from RudderStack to Leanplum.

* * *

  * __6 minute read

  * 


[Leanplum](<https://www.leanplum.com/>) is a popular marketing and customer engagement platform. It boosts customer engagement and retention, leading to better conversion and increased business revenue.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/leanplum>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Leanplum**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Leanplum as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Application ID** : Enter your Leanplum application ID.
  * **Client Key** : Enter the associated client key.


> ![info](/docs/images/info.svg)
> 
> You can find your **Application ID** and **Client Key** by logging in to your [Leanplum dashboard](<https://www.leanplum.com/dashboard/login?continue=%2Fdashboard2>) and navigating to **Development** \- [App Settings](<https://leanplum.com/dashboard#/account/apps>). Under **Keys & Settings**, click **API Keys** to get the required credentials.
> 
> For more information, see [Leanplum documentation](<https://docs.leanplum.com/docs/use-the-right-api-keys>).

### Connection mode

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Leanplum** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
### Send events in hybrid mode

You can use [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) to send all events to Leanplum from your [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) and [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) sources.

Use the hybrid mode option (highlighted below) while connecting your iOS (Obj-C)/Android (Java) source to the Leanplum destination. Then, add the Leanplum integration to your project.

[![Leanplum hybrid mode connection setting](/docs/images/event-stream-destinations/braze-hybrid-mode.webp)](</docs/images/event-stream-destinations/braze-hybrid-mode.webp>)

#### Why use hybrid mode

Certain Leanplum functionalities like push notifications and A/B testing require you to load the Leanplum SDK.

When you choose hybrid mode to send events to Leanplum, RudderStack:

  * Initializes the Leanplum SDK.
  * Sends all the user-generated events (`identify`, `track`, `page`, `screen`, and `group`) to Leanplum only through [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) and blocks them from being sent via device mode.
  * Sends the auto-generated events (A/B testing, push notifications that require the Leanplum SDK) via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


With hybrid mode, you can send the auto-generated and user-generated events to Leanplum using a single connection.

### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Leanplum:

  * **Use in Development Environment** : If this setting is enabled, make sure to provide the **Client Key** corresponding to your development environment. Failure to do so will result in a faulty SDK initialization and your events will fail.
  * **Client-side event filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Leanplum. For more information, see [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Add Leanplum integration to your project

Depending on your platform of integration, follow these steps below to add Leanplum to your project:

  1. Add the following to the `dependencies` section of your `pubspec.yaml` file.


    
    
    rudder_integration_leanplum_flutter: ^1.0.1
    

  2. Install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import `RudderIntegrationLeanplumFlutter` in your application where you want to initialize the SDK.


    
    
    import 'package:rudder_integration_leanplum_flutter/rudder_integration_leanplum_flutter.dart';
    

  4. Finally, change the SDK initialization:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationLeanplumFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

> ![info](/docs/images/info.svg)
> 
> For iOS, Leanplum needs to be linked either as a dynamic or static framework with your application. You can do so by adding the following lines to your `Podfile`:
>     
>     
>     use_frameworks! :linkage=> :static // linking statically
>     
>     # OR
>     
>     use_frameworks! :linkage=> :dynamic // linking dynamically
>     

  1. Open your `app/build.gradle` (Module: app) file, and add the following.


    
    
    repositories {
        mavenCentral()
    }
    

  2. Add the following under `dependencies` section:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.rudderstack.android.integration:leanplum:1.+'
    implementation 'com.leanplum:leanplum-core:5+'
    

  3. Change the SDK initialization to the following:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(LeanPlumIntegrationFactory.FACTORY)
                .build()
        )
    

  1. Open the `Podfile` of your project and add the following:


    
    
    pod 'Rudder-Leanplum'
    

  2. Run the `pod install` command.
  3. Add the imports to your `AppDelegate.m` file:


    
    
    #import "RudderLeanplumFactory.h"
    

  3. Change the SDK initialization as shown:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withEndPointUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderLeanplumFactory instance]];
    [RudderClient getInstance:WRITE_KEY config:[builder build]];
    

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * The RudderStack SDKs store the user traits from the `identify` call in `SharedPreference` and `NSUserDefaults` for Android and iOS respectively.
>   * If RudderStack detects `userId` in the persisted traits information, it starts the native SDK along with it. If it is unable to find `userId`, RudderStack initializes the SDK without it. This is helpful in building a better session.
>   * For a persisted `userId`, the code for Android is `Leanplum.start(applicationContext, userId)`. If `userId` is absent, it is `Leanplum.start(applicationContext)`. RudderStack follows a similar pattern for iOS as well.
>   * While searching for the user identifier in the persisted traits, RudderStack looks for either `userId` or `id`.
> 


## Identify

RudderStack uses the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to populate and send user information to Leanplum.

Note that:

  * RudderStack uses the `setUserId` method of the Leanplum SDK to set the user’s identifier (`userId`).
  * It passes all the properties present in the event’s `context.traits` to the Leanplum SDK’s `setUserAttributes` method, which populates them in Leanplum.


The following snippet highlights a sample `identify` call:
    
    
    [[RudderClient sharedInstance] identify:@"developer_user_id"
                                     traits:@{@"email": @"bar@foo.com"}];
    

## Track

RudderStack forwards the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events to Leanplum without any modification to the payload, as long as the event name is not `null`.

The following snippet highlights a sample `track`call:
    
    
    [[RudderClient sharedInstance] track:@"Accepted Terms of Service"
                              properties:@{
                                      @"foo": @"bar",
                                  @"foo_int": @134
    }];
    

## Screen

Leanplum supports tracking the user states. RudderStack uses the [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) calls to advance the user’s states to LeanPlum. For every `screen` event, RudderStack calls the `advanceTo` method of the Leanplum SDK along with the screen name and the associated event properties.

RudderStack also sends the automatically tracked `screen` events to LeanPlum.

The following snippet highlights a sample `screen` call:
    
    
    [[RudderClient sharedInstance] screen:@"Main"];
    

## Reset

You can use the `reset` method to clear the user identification in Leanplum. RudderStack calls `clearUserContent` method of the Leanplum SDK to clear the persisted user data.

The following snippet highlights a sample `reset` call:
    
    
    [[RudderClient sharedInstance] reset];
    

## Debugging

RudderStack sets the verbose logging for development mode for the Leanplum Native SDK, based on the `logLevel` set during the SDK initialization.

If the `logLevel` is set as `DEBUG` or more, RudderStack enables logging using the `enableVerboseLoggingInDevelopmentMode` method of the Leanplum SDK.