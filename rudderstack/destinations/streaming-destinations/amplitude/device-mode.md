# Amplitude Device Mode Integration

Send events to Amplitude using RudderStack device mode.

* * *

  * __10 minute read

  * 


After you have successfully [set up Amplitude as a destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/>) in RudderStack, follow this guide to correctly send your events to Amplitude in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

## Add device mode integration

Follow these steps to add Amplitude to your project depending on your integration platform:

Follow the below steps to add Amplitude to your Flutter Project:

  1. Add the following dependency to the `dependencies` section of your `pubspec.yaml` file.


    
    
    rudder_integration_amplitude_flutter: ^1.0.1
    

  2. Run the below command to install the dependency added in the above step:


    
    
    flutter pub get
    

  3. Import the `RudderIntegrationAmplitudeFlutter` in your application where you are initializing the SDK.


    
    
    import 'package:rudder_integration_amplitude_flutter/rudder_integration_amplitude_flutter.dart';
    

  4. Finally, change the initialization of your `RudderClient` as shown:


    
    
    final RudderController rudderClient = RudderController.instance;
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder.withFactory(RudderIntegrationAmplitudeFlutter());
    rudderClient.initialize(<write_key>, config: builder.build(), options: null);
    

> ![info](/docs/images/info.svg)
> 
> For iOS platform, make sure that the minimum deployment target for your application’s target is at least 10.

To add Amplitude to your React Native project:

  1. Add the RudderStack-Amplitude module to your app using either of the following ways:


    
    
    npm install @rudderstack/rudder-integration-amplitude-react-native
    

OR  

    
    
    yarn add @rudderstack/rudder-integration-amplitude-react-native
    

  2. Import the module added above and add it to your SDK initialization code as shown:


    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native"
    import amplitude from "@rudderstack/rudder-integration-amplitude-react-native"
    const config = {
      dataPlaneUrl: DATA_PLANE_URL,
      trackAppLifecycleEvents: true,
      withFactories: [amplitude],
    }
    rudderClient.setup(WRITE_KEY, config)
    

Follow these steps to add Amplitude to your iOS project:

  1. In your `Podfile`, add the `Rudder-Amplitude` extension:


    
    
    pod 'Rudder-Amplitude'
    pod 'Amplitude', '~> 7.2.0'
    

  2. After adding the dependency followed by `pod install` , you can add the imports to your `AppDelegate.m` file as shown:


    
    
    #import <rudder>
    #import "RudderAmplitudeFactory.h"
    // for using IDFA as device id, location listening only
    #import <amplitude>
    

  3. Also add the initialization of your `RSClient` as shown:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderAmplitudeFactory instance]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    

  4. Add the below logic just after initializing `RudderClient` in `AppDelegate.m` if you would like to send `IDFA` of iOS device as `device id` to Amplitude


> ![warning](/docs/images/warning.svg)
> 
> Make sure to enable **Use IDFA for device ID** under the [iOS SDK settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ios>) in the RudderStack dashboard.
    
    
    // for using IDFA as device id only
    [Amplitude instance].adSupportBlock = ^{
        return [[ASIdentifierManager sharedManager] advertisingIdentifier];
    };
    

  5. Add the below logic to track location (latitude and longitude):


    
    
    [Amplitude instance].locationInfoBlock = ^{
            return @{
                    @"lat" : @37.7,
                    @"lng" : @122.4
                  };
    };
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Amplitude v8.8.0 and above.

Follow these steps to add Amplitude to your iOS project:

  1. Install `RudderAmplitude` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderAmplitude', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Then, import the SDK depending on your preferred platform:


    
    
    import RudderAmplitude
    

  

    
    
    @import RudderAmplitude;
    

  4. Next, add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderAmplitudeDestination())
    

  

    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderAmplitudeDestination alloc] init]];
    

To add Amplitude to your Android Project please follow these steps :

  1. Open your `app/build.gradle` (Module: app) file, and add the following under the `dependencies` section :


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.rudderstack.android.integration:amplitude:1.1.0'
    

  2. Initialize the RudderStack SDK in the `onCreate()` method of the `Application` class as following:


    
    
    // initializing Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(AmplitudeIntegrationFactory.FACTORY)
                .build()
        )
    

  3. To send `Google Advertising Id` of the device as `device id` to the Amplitude, add the below code in the `AndroidManifest.xml` of your app under `<application>` tag:


> ![info](/docs/images/info.svg)
> 
> Make sure to enable **Use Advertising ID for device ID** under the [Android SDK settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#android>) in the RudderStack dashboard.
    
    
    <meta-data android:name="com.google.android.gms.ads.AD_MANAGER_APP" android:value="true"></meta-data>
    

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to associate a user with their actions and capture all relevant traits about them. This includes a unique `userId` and other optional information like name, email address, etc.

> ![info](/docs/images/info.svg)
> 
> In device mode, RudderStack automatically captures and sends the device-specific identifiers like `deviceId` to Amplitude. These identifiers are used by Amplitude to track unique devices and sessions.

A sample `identify` call looks like the following:
    
    
    rudderanalytics.identify(
      "userId", {
        email: "name@surname.com",
        name: "John Doe",
        profession: "Student",
      })
    

### Opt out of identify calls

> ![warning](/docs/images/warning.svg)
> 
> This feature is available only for the mobile platforms.

You can opt out of an `identify` call in a current session by passing a `optOutOfSession` trait and setting it to `true`. If there is no active session, passing `optOutOfSession: true` does not start a new session.

### Unset user properties

To unset the user traits in device mode, specify them in the `integrations.Amplitude.fieldsToUnset` object.

When you unset fields using `fieldsToUnset`, RudderStack notifies Amplitude to delete the fields along with their schema (if they exist).

See the [Amplitude documentation](<https://www.docs.developers.amplitude.com/analytics/apis/http-v2-api/#keys-for-the-event-argument:~:text=exceed%2040%20layers.-,user_properties,-Optional.%20Object.%20A>) for more information on this feature.

#### Example

To unset `firstName` and `lastName` in the following `identify` event:
    
    
    rudderanalytics.identify("userId", {
      "firstName": "Alex",
      "outerObject": {
        "innerObject": {
          "lastName": "Keener"
        }
      }
    });
    

Set the `integrations` object in your `identify` event as shown:
    
    
    rudderanalytics.identify("userId", {}, {
      integrations: {
        Amplitude: {
          "fieldsToUnset": ["firstName", "outerObject.innerObject.lastName"]
        }
      }
    })
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call allows you to record your website’s page views, with the additional relevant information about the viewed page. RudderStack recommends calling this method at least once per page load.

In device mode, page views are automatically tracked as events in Amplitude with the event type as `[RudderStack] Page`.

A sample `page` call looks like the following:
    
    
    rudderanalytics.page({
      category: "Category",
      name: "Sample",
    })
    

In the above example, RudderStack captures information related to the page being viewed such as the category of the page (`Category`) and the page name (`Sample`).

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record screen views with any additional information about the viewed screen.

In device mode, screen views are automatically tracked as events in Amplitude with the event type as `[RudderStack] Screen`.

A sample `screen` call looks like the following code snippet:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                    properties:@{@"prop_key" : @"prop_value"}];
    

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) event to link an identified user with a group, like a company, organization, or an account.

Note that RudderStack does not support associating a user to more than one group per `group` call sent to Amplitude.

To send more than one group per user, you must call the `group` API multiple times with the relevant group information specified in the [group settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#group-trait-settings>).

### Use Amplitude Groups

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * This feature is only available for web (JavaScript) device mode.
>   * [Groups](<https://developers.amplitude.com/docs/group-identify-api>) are an enterprise-only feature in Amplitude. You need to purchase the [Accounts](<https://help.amplitude.com/hc/en-us/articles/115001765532>) add-on to use this feature.
> 


To use the Amplitude Groups feature with RudderStack:

  1. Configure the **Group name trait** and **Group value trait** fields in the [**Group trait settings**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#group-trait-settings>).
  2. In device mode, RudderStack triggers a `group` call for a `groupId` by mentioning `groupType` as `'[RudderStack] Group'` and `value` as `groupId`.


Even if you don’t have an enterprise account or the Groups add-on, RudderStack adds `groups` as a user property in the user’s profile with **Group Name Trait** as its type and **Group Value Trait** as its value.

For example, if you define the **Group Name Trait** as `RS` and **Group Value Trait** as `RudderStack` and make the `group` call, the user would then be associated with the group name as `RS` and the group value as `RudderStack`.

Note that in device mode:

  * Group properties are limited to scalar values and arrays.
  * Nested objects in group properties are not supported.
  * Group property values cannot exceed 1000 characters.


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user’s actions along with any properties associated with them.

In device mode, events are processed and sent immediately to Amplitude. The SDK also supports offline event caching and automatic retries when the device is back online.

A sample `track` call looks like the following:
    
    
    rudderanalytics.track("Track me")
    

### Opt out of track calls

> ![warning](/docs/images/warning.svg)
> 
> This feature is available only for the mobile platforms.

If you set a property with the name `optOutOfSession` with value set to `true`, then this `track` call will be opted out of the current session if it exists. If there is no active session, passing `optOutOfSession: true` does not start a new session.

### Track revenue events

> ![info](/docs/images/info.svg)
> 
> Revenue events are available only in web device mode.
> 
> To track revenue events, RudderStack uses Amplitude’s `logRevenueV2()` API which expects `revenue` as a top level attribute.

To track a revenue event, you must include a `revenue` key in the event, as shown:
    
    
    rudderanalytics.track("Item Purchased", {
      revenue: 30,
      revenue_type: "add-on purchase",
    })
    

RudderStack processes revenue events in the following ways:

  * If you include `price` and `quantity` fields in your event, then RudderStack calculates the revenue as `price * quantity`.
  * If the `revenue` field is present in your event but `price` is not, then RudderStack uses `revenue` as the `price` with `quantity` set to 1.


> ![info](/docs/images/info.svg)
> 
> The `revenue` field **does not override** the `price * quantity` calculation, if both are present.

Note that:

  * Each product must have either `price` or `revenue` fields for tracking.
  * The `logRevenueV2` API uses both `price` and `quantity` to calculate revenue.
  * If `quantity` is not specified, it defaults to `1`.


#### Track revenue at event or product level

For events with a `products` array, you can track revenue at event level or product level based on your dashboard configuration:

Dashboard setting| Action  
---|---  
[Track revenue per product](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) is enabled| Revenue is tracked separately for each product.  
[Track revenue per product](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) is disabled| Revenue is tracked as an aggregate at the event level.  
  
### Track completed orders

> ![info](/docs/images/info.svg)
> 
> This feature is available only in web device mode.

In device mode, revenue tracking for orders is handled by the Amplitude SDK’s `logRevenueV2` API, which ensures accurate revenue attribution even in offline scenarios.

While tracking completed orders with multiple products, RudderStack generates events as follows:

**When[Track products as a single event](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) setting is toggled off**:

  * One main `Order Completed` event with the overall order details
  * Separate `Product Purchased` events for each product in the `products` array
  * Revenue tracking based on your revenue tracking configuration


**When[Track products as a single event](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) setting is toggled on**:

  * One single event with the original event name (`Order Completed`)

  * All products are included as properties in this single event

  * Revenue tracking based on your revenue tracking configuration:

    * If [Track revenue per product](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) setting is enabled: Each product is tracked individually with its own revenue calculation, regardless of the total order revenue.
    * If [Track revenue per product](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#ecommerce-settings>) setting is disabled: The total revenue specified at the order level is used.


> ![info](/docs/images/info.svg)
> 
> In both the cases, any discrepancy between the sum of product revenues and the order-level revenue is ignored.

A sample `Order Completed` event is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      checkoutId: "ABCD1234",
      orderId: "order1234",
      revenue: 50,
      products: [
        {
          productId: "product1",
          sku: "45790-32",
          name: "Monopoly: 3rd Edition",
          price: 20,
          quantity: 1,
          category: "Games",
        },
        {
          productId: "product2",
          sku: "46493-32",
          name: "Uno Card Game",
          price: 15,
          quantity: 2,
          category: "Games",
        },
      ],
    })
    

## Advanced features

This section covers some advanced features that you can use to enhance your Amplitude device mode integration with RudderStack.

### Reset

> ![info](/docs/images/info.svg)
> 
> This feature is currently available only for the mobile platforms.

You can use the `reset` method to reset the previously identified user and related information. This is particularly useful in scenarios like user logout.
    
    
    [[RSClient sharedInstance] reset];
    
    
    
    rudderClient.reset()
    

### Send `event_id`

RudderStack supports sending `event_id` to Amplitude in device mode. You can include it under the `integrations` object and it is supported for all API calls (`identify`, `track`, `page`, `screen`, and `group`).

> ![info](/docs/images/info.svg)
> 
> If you don’t specify an `event_id`, the SDK automatically generates one to ensure event uniqueness.

A sample `identify` call with `event_id` is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        name: "Alex Keener"
      }, {
        integrations: {
          Amplitude: {
            event_id: 1234
          }
        }
      }
    );
    

### Skip user properties sync

When you send an event to Amplitude via RudderStack, Amplitude updates the existing user properties and appends any new ones. You can change this behavior by setting the `skip_user_properties_sync` property to `true` in the `integrations` object.

This ensures that the event in Amplitude:

  * Includes only the user properties sent with it
  * Does not modify the user properties table
  * Does not include any pre-existing user properties


See [Amplitude documentation](<https://www.docs.developers.amplitude.com/analytics/data-backfill-guide/#skip-user-properties-sync>) for more information on this feature.

A sample `integrations` object with the `skip_user_properties_sync` property is shown below:
    
    
    "integrations": {
            ...
            ...
            "Amplitude": {
                "skipUserPropertiesSync": true
            }
            ...
            ...
        }
    

## FAQ

#### Can I send more than one group per user to Amplitude?

RudderStack does not support associating a user to more than one group per `group` call sent to Amplitude. To send more than one group per user, you need to call the `group` API multiple times with the relevant group information specified in the [group settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/setup-guide/#group-trait-settings>).