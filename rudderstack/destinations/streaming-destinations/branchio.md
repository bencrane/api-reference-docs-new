# Branch

Send your event data from RudderStack to Branch.

* * *

  * __6 minute read

  * 


[Branch.io](<https://branch.io>) is an industry leader in cross-platform attribution, mobile app measurement, and deep linking. Many top-ranking apps use Branch to increase their performance and revenue through better performance and engagement.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/branch>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Branch Metrics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Branch, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Branch Metrics**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up Branch as a destination, you will need to configure the following settings:

  * **Branch key** : Enter your Branch key from the **Settings** section in the [Branch dashboard](<https://dashboard.branch.io/#/settings>). For more information on obtaining this key, see FAQ.
  * **Map Your Events To Branch Events** : Use this setting to map your RudderStack events to specific Branch events from the dropdown.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * This setting is currently available in cloud mode only.
>   * The mappings specified using this setting override the default event mappings configured by RudderStack internally.
> 


[![Branch event mapping setting](/docs/images/event-stream-destinations/branch-event-mapping-ui.webp)](</docs/images/event-stream-destinations/branch-event-mapping-ui.webp>)

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Branch. For more information on this setting, see the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Adding device mode integration

Depending on your platform of integration, follow the below steps below to integrate Branch with your app.

  1. Open the `Podfile` of your project and add the following line:


    
    
    pod 'Rudder-Branch', '2.0.0'
    

  2. Run the `pod install` command.
  3. Change the SDK initialization to the following:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:<data_plane_url>];
    [builder withFactory:[RudderBranchFactory instance]];
    [builder withLoglevel:RudderLogLevelDebug];
    [RudderClient getInstance:<write_key> config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Branch v1.41.0 and above.

Follow these steps to add Branch to your iOS project:

  1. Install `RudderBranch` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderBranch', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Then, import the SDK depending on your preferred platform:


    
    
    import RudderBranch
    
    
    
    @import RudderBranch;
    

  4. Next, add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderBranchDestination())
    
    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderBranchDestination alloc] init]];
    

Your Android project must be on **version 5.0 (API level 21) or higher** for RudderStack to be able to send events to Branch.

Once confirmed, follow these steps to add Branch to your Android project:

  1. Open your `app/build.gradle` (Module: app) file, add the following


    
    
    repositories {
        mavenCentral()
    }
    

  2. Add the following under `dependencies` section:


    
    
    implementation 'com.rudderstack.android.sdk:core:[1.20.1, 2.0.0)'
    implementation 'com.rudderstack.android.integration:branch:2.0.0'
    

  3. If needed, add the following **optional** dependencies required by Branch in the `dependencies` section:


    
    
    // required if your app is in the Google Play Store (tip: avoid using bundled play services libs)
    implementation 'com.google.android.gms:play-services-ads-identifier:17.1.0+'
    // alternatively, use the following lib for getting the AAID
    // implementation 'com.google.android.gms:play-services-ads:17.2.0'
    // optional
    // Chrome Tab matching (enables 100% guaranteed matching based on cookies)
    implementation 'androidx.browser:browser:1.0.0'
    // Replace above with the line below if you do not support androidx
    // implementation 'com.android.support:customtabs:28.0.0'
    

  4. Change the initialization of the SDK with the following:


    
    
    // initialize Rudder SDK
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withLogLevel(RudderLogger.RudderLogLevel.DEBUG)
                .withFactory(BranchIntegrationFactory.FACTORY)
                .build()
        )
    

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call associates a user to their actions and also captures the traits associated with that user.

A sample `identify` call captured from the RudderStack iOS (Obj-C) SDK is as shown:
    
    
    [[RudderClient sharedInstance] identify:@"developer_user_id"];
    

> ![info](/docs/images/info.svg)
> 
> You can call `identify` when the user registers to the app for the first time, logs into the app, or updates their information.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the customer events along with any properties associated with them.

A sample `track` call is shown below:
    
    
    [[RudderClient sharedInstance] track:@"test_event"
                              properties:@{@"key":@"value", @"foo": @"bar"}]
    

All the events tracked by RudderStack are divided into three major Branch event categories:

  * [Commerce events](<https://help.branch.io/developers-hub/docs/tracking-commerce-content-lifecycle-and-custom-events#track-commerce-events>)
  * [Content events](<https://help.branch.io/developers-hub/docs/tracking-commerce-content-lifecycle-and-custom-events#track-content-events>)
  * [Lifecycle events](<https://help.branch.io/developers-hub/docs/tracking-commerce-content-lifecycle-and-custom-events#track-lifecycle-events>)


### Ecommerce event mapping

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The following table lists the mapping between the [RudderStack ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) and the Branch [commerce events](<https://help.branch.io/developers-hub/docs/tracking-commerce-content-lifecycle-and-custom-events#available-events>):

RudderStack event| Branch event  
---|---  
`Product Added`| `ADD_TO_CART`  
`Product Added to Wishlist`| `ADD_TO_WISHLIST`  
`Cart Viewed`| `VIEW_CART`  
`Checkout Started`| `INITIATE_PURCHASE`  
`Payment Info Entered`| `ADD_PAYMENT_INFO`  
`Order Completed`| `ADD_PAYMENT_INFO`  
`Spend Credits`| `SPEND_CREDITS`  
`Promotion Viewed`| `VIEW_AD`  
`Promotion Clicked`| `CLICK_AD`  
`Checkout Started`| `PURCHASE`  
`Order Completed`| `PURCHASE`  
`Reserve`| `RESERVE`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack also maps the `Spend Credits` event to Branch’s `SPEND_CREDITS`, although it is not directly a part of the ecommerce events.
> 
> However, note that the Android device mode integration **does not** support this mapping.

### Content event mapping

The following table lists the mapping between the RudderStack events and the Branch Content events:

RudderStack event| Branch event  
---|---  
`Products Searched`| `SEARCH`  
`Product Viewed`| `VIEW_ITEM`  
`Product List Viewed`| `VIEW_ITEMS`  
`Product Reviewed`| `RATE`  
`Product Shared`| `SHARE`  
`Initiate Stream`| `INITIATE_STREAM`  
`Complete Stream`| `COMPLETE_STREAM`  
  
> ![info](/docs/images/info.svg)
> 
> The above mentioned events are a part of the RudderStack ecommerce events but are mapped to Branch’s Content events.

### Lifecycle event mapping

RudderStack supports mapping the following Branch lifecycle events:

RudderStack event| Branch event  
---|---  
`Complete Registration`| `COMPLETE_REGISTRATION`  
`Complete Tutorial`| `COMPLETE_TUTORIAL`  
`Achieve Level`| `ACHIEVE_LEVEL`  
`Unlock Achievement`| `UNLOCK_ACHIEVEMENT`  
`Invite`| `INVITE`  
`Login`| `LOGIN`  
`Start Trial`| `START_TRIAL`  
`Subscribe`| `SUBSCRIBE`  
  
## Reset

The `reset` method resets the previously identified user and related information.

A sample `reset` call is shown:
    
    
    [[RSClient getInstance] reset];
    

## Property mappings

The following table lists the mapping of the accepted RudderStack properties common to all events:

RudderStack property| Branch property  
---|---  
`title`| `$og_title`  
`description`| `$og_description`  
`image_url`| `$og_image_url`  
`canonical_identifier`| `$canonical_identifier`  
`publicly_indexable`| `$publicly_indexable`  
`price`| `$price`  
`locally_indexable`| `$locally_indexable`  
`quantity`| `$quantity`  
`sku`| `$sku`  
`name`| `$product_name`  
`brand`| `$product_brand`  
`category`| `$product_category`  
`variant`| `$product_variant`  
`rating_average`| `$rating_average`  
`rating_count`| `$rating_count`  
`rating_max`| `$rating_max`  
`creating_timestamp`| `$creation_timestamp`  
`exp_date`| `$exp_date`  
`keywords`| `$keywords`  
`address_street`| `$address_street`  
`address_city`| `$address_city`  
`address_region`| `$address_region`  
`address_country`| `$address_country`  
`address_postal_code`| `$address_postal_code`  
`latitude`| `$latitude`  
`longitude`| `$longitude`  
`image_captions`| `$image_captions`  
`condition`| `$condition`  
  
## FAQ

#### Where can I find the Branch key?

To retrieve your Branch key, follow these steps:

  1. Log into your [Branch dashboard](<https://dashboard.branch.io>).
  2. Go to **Account Settings** > **Profile**.
  3. You can find the Branch Key under **Branch Key and Secret** section:

[![Branch key](/docs/images/event-stream-destinations/branchio-key.webp)](</docs/images/event-stream-destinations/branchio-key.webp>)