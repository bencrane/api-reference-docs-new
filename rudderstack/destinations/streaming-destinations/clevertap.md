# CleverTap

Send your event data from RudderStack to CleverTap.

* * *

  * __13 minute read

  * 


[CleverTap](<https://clevertap.com/>) is a popular customer engagement and retention platform. Its in-app analytics and marketing capabilities allow you to get real-time insights into your customers and build valuable, long-term relationships with them.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/clevertap>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **CleverTap** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the CleverTap native SDK from the`https://d2r1yp2w7bby2u.cloudfront.net` domain.
> 
> Based on your website’s content security policy, you may need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the CleverTap SDK.

## Get started

Once you have confirmed that the source platform supports sending events to CleverTap, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **CleverTap**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully set up CleverTap as a destination, you will need to configure the following settings:

  * **Account ID** : Your account ID is a unique ID generated for your account. It can be found in your account **Settings** as your **Project ID**.
  * **Passcode** : Your account passcode is a unique code generated for your account. It can be found in your CleverTap dashboard by going to **Settings** > **Passcode**.
  * **Enable track for anonymous user** : Enable this option to track anonymous users in CleverTap.
  * **Use CleverTap ObjectId for Mapping** : Enable this option to use both CleverTap `objectId` along with `identity` for mapping events from RudderStack to CleverTap.
  * **Region** : Select your CleverTap region.
  * **Client-side Events Filtering** : Specify which events should be blocked or allowed to flow through to CleverTap. For more information on this setting, see the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.
  * **Use device mode to send events** : Enable this option to send events in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


> ![info](/docs/images/info.svg)
> 
> All server-side destination requests require either an `anonymousId` or a `userId` in the payload.

## Adding device mode integration

To add CleverTap to your React Native project:

  1. Add the RudderStack-CleverTap module to your app using:


    
    
    npm install @rudderstack/rudder-integration-clevertap-react-native
    ## OR ##
    yarn add @rudderstack/rudder-integration-clevertap-react-native
    

  2. Run `pod install` inside the `ios` directory of your project adding `@rudderstack/rudder-integration-clevertap-react-native` to your project.

  3. Import the module you added above and add it to your SDK initialization code as shown below:


    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native"
    import clevertap from "@rudderstack/rudder-integration-clevertap-react-native"
    
    const config = {
      dataPlaneUrl: DATA_PLANE_URL,
      trackAppLifecycleEvents: true,
      withFactories: [clevertap],
    }
    rudderClient.setup(WRITE_KEY, config)
    

To add CleverTap to your Android project and enable functionalities like push notifications, follow these steps:

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
    

  2. Ensure that `android.useAndroidX` is set to `true` in your `gradle.properties` file. Add the following under the `dependencies` section:


    
    
    // ruddder core sdk
    implementation 'com.rudderstack.android.sdk:core:1.+'
    // rudder-clevertap integration
    implementation 'com.rudderstack.android.integration:clevertap:1.+'
    // clevertap native sdk
    implementation 'com.clevertap.android:clevertap-android-sdk:4.+'
    // if you don't have Gson included already
    implementation 'com.google.code.gson:gson:2.8.6'
    

  3. Initialize the RudderStack SDK in the `Application` class’s `onCreate()` method as shown:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(CleverTapIntegrationFactory.FACTORY)
                .build()
        )
    

Follow these steps to add CleverTap to your iOS project:

  1. Go your `Podfile` and add the `Rudder-CleverTap` extension as shown below:


    
    
    pod 'Rudder-CleverTap'
    

  2. After adding the dependency followed by `pod install` , you can add the imports to your `AppDelegate.m` file:


    
    
    #import "RudderCleverTapFactory.h"
    

  3. Change the initialization of your `RudderClient` as shown:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderCleverTapFactory instance]];
    [RudderClient getInstance:WRITE_KEY config:[builder build]];
    

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you associate a user with their actions and capture relevant traits about them. This information includes `userId` and other user information like `name`, `email`, etc.

> ![info](/docs/images/info.svg)
> 
> RudderStack requires either `userId` or `email` to send `identify` events to CleverTap.

RudderStack maps the following user traits to the CleverTap attributes:

**RudderStack**| **CleverTap**  
---|---  
`name`| `Name`  
`birthday`| `DOB`  
`avatar`| `Photo`  
`gender`| `Gender`  
`phone`| `Phone`  
`email`| `Email`  
`employed`| `Employed`  
`education`| `Education`  
`married`| `Married`  
`customerType`| `Customer Type`  
  
RudderStack sends all other traits to CleverTap as custom attributes.

> ![info](/docs/images/info.svg)
> 
> **Phone number format requirement**
> 
> CleverTap requires phone numbers to be formatted as `+[country code][phone number]` (for example, `+14155551234` for a U.S. phone number).
> 
> RudderStack **does not modify** the phone format in its integration logic — hence, ensure your phone numbers are properly formatted before sending them through RudderStack.
> 
> See the [CleverTap Upload User Profiles API documentation](<https://developer.clevertap.com/docs/upload-user-profiles-api#body-parameters>) for more information.

A sample `identify` call looks like the following:
    
    
    rudderanalytics.identify("userid", {
      name: "Name Surname",
      email: "name@website.com",
      phone: "+14155551234",
      birthday: "birthday",
      gender: "M",
      avatar: "link to image",
      title: "Owner",
      organization: "Company",
      city: "Tokyo",
      region: "ABC",
      country: "JP",
      zip: "100-0001",
      Flagged: false,
      Residence: "Shibuya",
      MSG-email: false
    });
    

In the above snippet, RudderStack captures relevant information about the user such as the `email` and `phone`, along with the associated user traits.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If a user already exists, the new values will be updated for that user. RudderStack automatically maps the `userId` (or `anoymousId`) to CleverTap’s `identity` attribute.
>   * The profile properties `MSG-email`, `MSG-push`, `MSG-sms` and `MSG-whatsapp` are used to set the Do Not Disturb (DND) status for the user. They are always `true` by default, unless you explicitly set them to `false`. For example, to disable push notifications for a user, set `MSG-push` to `false`.
> 


### Privacy options

When loading the RudderStack SDK, you can set the following options in the `CLEVERTAP` integrations object:

Option| Data type| Notes  
---|---|---  
`optOut`| Boolean| Defaults to `false`. Set to `true` if the user opts out of sharing their data.  
`useIP`| Boolean| Defaults to `false`. Set to `true` if the user agrees to share their IP data.  
      
    
    rudderanalytics.load(
      "WRITE_KEY",
      "DATAPLANE_URL", {
        configUrl: "https://api.rudderlabs.com",
        logLevel: "DEBUG",
        integrations: {
          CleverTap: {
            optOut: true,
            useIP: true,
          }
        }
      }
    );
    

CleverTap does a reverse lookup on the IP of the incoming request in the back end to map the user’s location. Under GDPR laws, user consent is required to initiate this lookup. Use the `useIP` flag in the web SDK to provide that consent.

If `useIP` is set to `true`, the city/country information will populate on the Profile page of the CleverTap dashboard. If set to `false`, then this data won’t be populated, and the city/country information will be shown as `Unknown, Unknown`.

See the [CleverTap documentation](<https://developer.clevertap.com/docs/sdk-changes-for-gdpr-compliance>) for more information.

### Delete a user

You can delete a user in CleverTap using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![warning](/docs/images/warning.svg)
> 
> While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with CleverTap if the request is fulfilled.

To delete a user, specify their `userId` in the event. Additionally, you can specify a custom identifier (optional) in the event.

A sample regulation request body for deleting a user in CleverTap is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
        "userId": "1hKOmRA4GRlm",
        "<customKey>": "<customValue>"
      }]
    }
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them. The user is associated with `userId` or `anonymousId` by default.

A sample `track` call looks like the following:
    
    
    rudderanalytics.track("Checked Out", {
      Clicked_Rush_delivery_Button: true,
      total_value: 2000,
      revenue: 2000,
    })
    

In the above snippet, RudderStack captures the information related to the `Checked Out` event, along with any additional info about that event.

> ![info](/docs/images/info.svg)
> 
> CleverTap does not support nested objects or arrays for custom attributes in the `track` events. Hence, RudderStack converts the nested objects or arrays into strings before sending them to CleverTap.

### Order Completed

When you track an event with the name `Order Completed` using the using the RudderStack [Ecommerce Events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) tracking, RudderStack maps it to CleverTap’s [Charged](<https://developer.clevertap.com/docs/events#recording-customer-purchases>) event.

A number of RudderStack’s specific fields map to CleverTap’s standard `Charged` event fields

**RudderStack**| **CleverTap**  
---|---  
`checkout_id`| `Charged ID`  
`revenue`| `Amount`  
`products`| `Items`  
  
A sample `Order Completed` event looks like the following:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "12345",
      order_id: "1234",
      affiliation: "Apple Store",
      "Payment mode": "Credit Card",
      total: 20,
      revenue: 15.0,
      shipping: 22,
      tax: 1,
      discount: 1.5,
      coupon: "Games",
      currency: "USD",
      products: [
        {
          product_id: "123",
          sku: "G-32",
          name: "Monopoly",
          price: 14,
          quantity: 1,
          category: "Games",
          url: "https://www.website.com/product/path",
          image_url: "https://www.website.com/product/path.jpg",
        },
        {
          product_id: "345",
          sku: "F-32",
          name: "UNO",
          price: 3.45,
          quantity: 2,
          category: "Games",
        },
        {
          product_id: "125",
          sku: "S-32",
          name: "Ludo",
          price: 14,
          quantity: 7,
          category: "Games",
          brand: "Ludo King",
        },
      ],
    })
    

> ![info](/docs/images/info.svg)
> 
> `Order Completed` is a free-flowing event. If you set extra fields like `discount`, `coupon`, `currency`, etc., RudderStack automatically maps them to the `Charged` event properties.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack sends a `page` event to CleverTap as a `Web Page Viewed <Page_Name>` event.

An example of a `page` call is shown below:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in",
    })
    

> ![info](/docs/images/info.svg)
> 
> CleverTap does not support nested objects or arrays for custom attributes in the `page` events. Hence, RudderStack converts the nested objects or arrays into strings before sending them to CleverTap.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method lets you record whenever your user views their mobile screen, with any additional relevant information about the screen.

A sample `screen` call is shown:
    
    
    [[RSClient sharedInstance] screen:@"Sample Screen Name"
            properties:@{@"prop_key" : @"prop_value"}];
    

In the above snippet, RudderStack captures all information related to the screen being viewed, along with any additional info associated with that screen view event. In CleverTap, the above `screen` call will be shown as - `Screen Viewed: <screen_name>` along with the properties.

> ![info](/docs/images/info.svg)
> 
> CleverTap does not support nested objects or arrays for custom attributes in the `screen` events. Hence, RudderStack converts the nested objects or arrays into strings before sending them to CleverTap.

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user.

A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("newUserId","userId");
    

## Configuring push notifications and in-app messages

Follow these steps to configure CleverTap push notifications for your desired platform.

  1. Open the `android` folder of your React Native app and follow the steps listed in the **Android** tab of this section.
  2. Open the `ios` folder of your React Native app and follow the steps listed in the **iOS** tab of this section.


  1. Register push notifications for Android devices on your CleverTap dashboard either by uploading your [FCM credentials](<https://developer.clevertap.com/docs/android-push#find-fcm-credentials>) or any other supported credentials by navigating to **Settings** > **Channels** > **Mobile Push** > **Android**. Add the following dependency in your project level `build.gradle` file inside the `buildscript`:


    
    
    dependencies {
      classpath 'com.google.gms:google-services:4.3.5'
    }
    

  2. Add the following dependencies and plugin to your app level `build.gradle` file:


    
    
    dependencies {
      // for push notifications
      implementation 'com.clevertap.android:clevertap-android-sdk:4.0.0'
      implementation 'com.google.firebase:firebase-messaging:20.2.4'
    }
    apply plugin: 'com.google.gms.google-services'
    

  3. Place the `google-services.json` downloaded from the `Firebase console` into the root folder of your `app`. Add your `CLEVERTAP_ACCOUNT_ID` , `CLEVERTAP_TOKEN` & `FcmMessageListenerService` to the `application` tag of your app’s `AndroidManifest.xml`:


    
    
    <meta-data android:name="CLEVERTAP_ACCOUNT_ID" android:value="XXX-XXX-XXXX"></meta-data>
    <meta-data android:name="CLEVERTAP_TOKEN" android:value="XXX-XXX"></meta-data>
    <service android:name="com.clevertap.android.sdk.pushnotification.fcm.FcmMessageListenerService">
    <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT"></action>
    </intent-filter>
    </service>
    

  4. Create a notification channel anywhere in your application using the following block of code. You can then use this `channel Id` while creating any campaign in your CleverTap dashboard.


    
    
    CleverTapAPI.createNotificationChannel(
        getApplicationContext(),
        "yourChannelId",
        "Your Channel Name",
        "Your Channel Description",
        NotificationManager.IMPORTANCE_MAX,
        true
    )
    

> ![info](/docs/images/info.svg)
> 
> For push notifications and In-app messages to function correctly, CleverTap needs to know the `Application` status as early as possible. You can either set `android:name` in your `AndroidManifest.xml` tag to `com.clevertap.android.sdk.Application`. If you have a custom `Application` class, call `ActivityLifecycleCallback.register(this);` before `super.onCreate()`.
> 
> To learn more about push notifications in CleverTap, see the [CleverTap documentation](<https://github.com/CleverTap/clevertap-android-sdk#setup-the-lifecycle-callback---important>).

  1. Navigate to **Target** > **Signing & Capabilities** in Xcode.
  2. Enable **Background Modes/Remote notifications** by navigating to **Targets** > **Your App** > **Capabilities** > **Background Modes** and checking **Remote notifications**.
  3. Navigate to **Settings** > **Channels** > **Mobile Push** > **iOS**.
  4. Register push notifications for the iOS devices on your CleverTap dashboard either by uploading your Auth Key or APNS push certificate.
  5. Add the following code in your app just after initializing iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. to register push notifications.


    
    
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
    

  6. Add these handlers for the tokens and push notifications:


    
    
    #import "RudderCleverTapIntegration.h"
    
    - (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      [[RudderCleverTapIntegration alloc] registeredForRemoteNotificationsWithDeviceToken:deviceToken];
    }
    
    - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
      [[RudderCleverTapIntegration alloc] receivedRemoteNotification:userInfo];
      completionHandler(UIBackgroundFetchResultNoData);
    }
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center willPresentNotification:(UNNotification *)notification withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler {
      completionHandler(UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
    }
    
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center didReceiveNotificationResponse:(UNNotificationResponse *)response withCompletionHandler:(void (^)(void))completionHandler {
      [[RudderCleverTapIntegration alloc] receivedRemoteNotification:response.notification.request.content.userInfo];
    }
    

## Using CleverTap objectId and identity for mapping

> ![info](/docs/images/info.svg)
> 
> This section is applicable when sending events in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

CleverTap uniquely identifies each user with two main identifiers, namely `objectId` and `identity`. When you enable the **Use CleverTap ObjectId for Mapping** option in the dashboard, RudderStack uses both `objectId` and `identity` and expects the following mapping:

  * For `identify` events:

**RudderStack**| **RudderStack**| **CleverTap**| **CleverTap**  
---|---|---|---  
**`anonymousId` present?**| **`userId` present?**| **`objectId`**| **`identity`**  
Yes| Yes| `anonymousId`| `userId`  
Yes| No| `anonymousId`| -  
No| Yes| CleverTap-generated UUID| `userId`  
  
  * For `track` events:

**RudderStack**| **RudderStack**| **CleverTap**| **CleverTap**  
---|---|---|---  
**`anonymousId` present?**| **`userId` present?**| **Tracking with**| **Value**  
Yes| Yes| `objectId`| `anonymousId`  
Yes| No| `objectId`| `anonymousId`  
No| Yes| `identity`| `userId`  
  
If **Use CleverTap ObjectId for Mapping** setting is disabled in the dashboard, RudderStack expects the following mapping for identifying users and tracking events (`track`/`page`/`screen`):

**RudderStack**| **CleverTap**  
---|---  
`userId` or `anonymousId`| `identity`  
  
> ![info](/docs/images/info.svg)
> 
> **Why use CleverTap`objectId` for mapping?**
> 
> When you track an unidentified user in CleverTap, a user profile is created with minimal details along with the user activity details. When the same user is then identified with a `userId` without the **Use CleverTap ObjectId for Mapping** option enabled, RudderStack creates another profile for the user with the `userId` identifier (in case of RudderStack) which maps to CleverTap’s `identity` attribute.
> 
> One way to solve this problem is to track users only in cases where a `userId` is present. To do so, disable the **Enable tracking for anonymous users** option in the RudderStack dashboard. Alternatively, you can turn on the **Use CleverTap ObjectId for Mapping** option in the dashboard which allows you to track the anonymous users and when they are later identified, merge their `anonymousId` with their `userId`.

## Upload device token in cloud mode

> ![info](/docs/images/info.svg)
> 
> This section is applicable for the Android (Java) and iOS (Obj-C) sources when sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

When the device token is present in `context.device.token` in `identify` calls, RudderStack uses CleverTap’s [Upload Device Tokens API](<https://developer.clevertap.com/docs/upload-device-tokens-api>) to upload the device token for the identified user. For Android, RudderStack sets the token type as `fcm`. For iOS, it is set as `apns`.

To use this feature, enable the **Use CleverTap ObjectId for Mapping** option in the dashboard as RudderStack needs the `objectId` to upload the device token.

You can also define the token type irrespective of your operating system by sending your choice of device token via the event’s `integrations` object. The supported token types are listed below:

  * `chrome`
  * `fcm`
  * `gcm`
  * `apns`
  * `wns`
  * `mpns`


A sample `integrations` object is shown below:
    
    
    integrations: {
      All: true,
      CleverTap: {
        deviceTokenType: 'apns',
      },
    }
    

For the `chrome` device token type, you can also send the `chromeKeys` object within the `integrations` object, as shown:
    
    
     integrations: {
       All: true,
       CleverTap: {
         deviceTokenType: 'chrome',
         chromeKeys: {
           p256dh: '<value>',
           auth: '<value>'
         },
       },
     },
    

See the CleverTap documentation on [uploading device tokens](<https://developer.clevertap.com/docs/upload-device-tokens-api>) for more details.