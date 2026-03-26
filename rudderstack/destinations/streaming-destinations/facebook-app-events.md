# Facebook App Events

Send your event data from RudderStack to Facebook App Events.

* * *

  * __13 minute read

  * 


[Facebook App Events](<https://developers.facebook.com/docs/app-events/>) is Facebook’s event tracking functionality which lets you track events via your app or web page, including user activities such as app installation, purchases, etc.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/fb>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Facebook App Events** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Facebook App Events, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Facebook App Events**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Facebook App Events as a destination, you will need to configure the following settings:

**APP ID** : Enter your Facebook App ID. See FAQ for more information on getting your Facebook App ID.

The following settings are applicable **only if** you are sending events to Facebook using [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>):

**Limited Data Use** : Enable this setting to send the end user’s country and state information. Facebook processes the user data according to the data regulations set for that region. See Limited Data Use for more information on this setting.

> ![info](/docs/images/info.svg)
> 
> You can allow Facebook to detect your country and state automatically by choosing the **Use Facebook to detect Automatically** option.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Facebook App Events. See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Add device mode integration

Depending on your platform of integration, follow the below steps to integrate App Events with your app.

Follow the steps in this section to add Facebook App Events to your Kotlin project.

[![Github Badge](https://img.shields.io/maven-central/v/com.rudderstack.integration.kotlin/facebook?style=flat)](<https://central.sonatype.com/artifact/com.rudderstack.integration.kotlin/facebook>)

#### 1\. Add dependencies

In your module (app-level) Gradle file (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the following dependencies for the RudderStack-Facebook integration:
    
    
    dependencies {
      // ...
      
      // Add Rudder Kotlin and Facebook integration SDKs:
      implementation("com.rudderstack.sdk.kotlin:android:<latest-version>")
      implementation("com.rudderstack.integration.kotlin:facebook:<latest-version>")
    }
    

#### 2\. Update manifest

Add your [App ID](<https://developers.facebook.com/docs/android/getting-started#app-id>) and [client token](<https://developers.facebook.com/docs/android/getting-started#client-token>) to the project’s string file and update the manifest file:

  1. Open `/app/res/values/strings.xml` in your app project.
  2. Add `string` elements with the names `facebook_app_id` and `facebook_client_token`, and set their values to your App ID and client token. For example, if your app ID is `1234` and your client token is `56789`, then your code should look as follows:


    
    
    <string name="facebook_app_id">1234</string>
    <string name="facebook_client_token">56789</string>
    

  3. Open `/app/src/main/AndroidManifest.xml` in your app project.
  4. Add `meta-data` elements to the `application` element for your App ID and client token:


    
    
    <application android:label="@string/app_name" ...>
        ...
        <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"/>
        <meta-data android:name="com.facebook.sdk.ClientToken" android:value="@string/facebook_client_token"/>
        ...
    </application>
    

#### 3\. Initialize the SDK and integration

Add the SDK initialization and the `Rudder-Facebook` integration in your `Application` class:
    
    
    import android.app.Application
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    import com.rudderstack.integration.kotlin.facebook.FacebookIntegration
    
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
            
            analytics.add(FacebookIntegration())
        }
    }
    

[![Github Badge](https://img.shields.io/github/v/tag/rudderlabs/integration-swift-facebook?label=Swift Package Manager)](<https://github.com/rudderlabs/integration-swift-facebook/>)

Follow these steps to add the Facebook App Events integration to your Swift project using Swift Package Manager:

  1. In Xcode, select **File > Add Package Dependencies…**.

![](/docs/images/event-stream-sources/swift/add-package-dependencies.webp)

  2. Enter the below package repository URL in the search bar:


    
    
    https://github.com/rudderlabs/integration-swift-facebook/
    

  3. Select the latest version and the target to which you want to add the package.
  4. Click **Add Package**.


Alternatively, you can add the dependency to your `Package.swift` file, as shown:
    
    
    dependencies: [
        .package(url: "<https://github.com/rudderlabs/integration-swift-facebook.git>", from: "<latest_integration_version>")
    ]
    

#### Usage

  1. Import the Facebook SDK:


    
    
    import FacebookCore
    

  2. Initialize the Facebook App Events iOS SDK **just before** initializing the RudderStack iOS (Swift) SDK:


    
    
    ApplicationDelegate.shared.application(
        UIApplication.shared,
        didFinishLaunchingWithOptions: [:]
    )
    

  3. Send the user’s consent to Facebook App Events, as shown:


    
    
    // Set AdvertiserTrackingEnabled to true if a user provides consent
    Settings.setAdvertiserTrackingEnabled(true)
    
    // Set AdvertiserTrackingEnabled to false if a user does not provide consent
    Settings.setAdvertiserTrackingEnabled(false)
    

  4. Configure your project by adding the following lines to `<dict>...</dict>` in your `Info.plist` file.


    
    
    <key>CFBundleURLTypes</key>
    <array>
    <dict>
    <key>CFBundleURLSchemes</key>
    <array>
    <string>fbAPP-ID</string>
    </array>
    </dict>
    </array>
    <key>FacebookAppID</key>
    <string>APP-ID</string>
    <key>FacebookClientToken</key>
    <string>CLIENT-TOKEN</string>
    <key>FacebookDisplayName</key>
    <string>APP-NAME</string>
    

> ![info](/docs/images/info.svg)
> 
> Make sure to replace `fbAPP-ID`, `APP-ID`, `CLIENT-TOKEN`, `APP-NAME` with the app-specific details from the [Facebook for Developers platform](<https://developers.facebook.com/>).

  5. Import the SDK and integration:


    
    
    import RudderStackAnalytics
    import RudderIntegrationFacebook
    

  6. Add `FacebookIntegration` to your `analytics` instance:


    
    
    // Initialize RudderStack Analytics
    let analytics = Analytics(
        configuration: Configuration(
            writeKey: "<WRITE_KEY>",
            dataPlaneUrl: "<DATA_PLANE_URL>"
        )
    )
    
    // Add Facebook Integration
    analytics.add(plugin: FacebookIntegration())
    

### Configure React Native Android app

  1. Open the `/app/res/values/strings.xml` file and add the following lines. Make sure to replace `APP_ID` and `CLIENT_TOKEN` with the appropriate values:


    
    
    <!-- Refer to the Facebook doc: https://developers.facebook.com/docs/android/getting-started-->
    <string name="facebook_app_id">APP_ID</string>
    <string name="facebook_client_token">CLIENT_TOKEN</string>
    

  2. In the `app/AndroidManifest.xml` file, add a `meta-data` element to the `application` element. See the [Facebook developer documentation](<https://developers.facebook.com/docs/app-events/getting-started-app-events-android>) for more details.


    
    
    <!-- Refer to the Facebook doc: https://developers.facebook.com/docs/android/getting-started-->
    <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"/>
    <meta-data android:name="com.facebook.sdk.ClientToken" android:value="@string/facebook_client_token"/>
    

### Configure React Native iOS app

  1. Import the Facebook app into the `AppDeletegate.swift` file:


    
    
    import FBSDKCoreKit
    

  2. Initialize the Facebook App Events iOS SDK by adding the below snippet to the `application` method in `AppDelegate.swift`:


    
    
    ApplicationDelegate.shared.application(application, didFinishLaunchingWithOptions: launchOptions)
    

  3. Configure the `Info.plist` file with the below XML snippet containing the data about your app. See the [Facebook developer documentation](<https://developers.facebook.com/docs/app-events/getting-started-app-events-ios>) for more details.


    
    
    <key>CFBundleURLTypes</key>
    <array>
      <dict>
      <key>CFBundleURLSchemes</key>
      <array>
        <string>fbAPP-ID</string>
      </array>
      </dict>
    </array>
    <key>FacebookAppID</key>
    <string>APP-ID</string>
    <key>FacebookClientToken</key>
    <string>CLIENT-TOKEN</string>
    <key>FacebookDisplayName</key>
    <string>APP-NAME</string>
    

### Add RudderStack-Facebook module

Add the React Native integration to your app using either of the below ways:
    
    
    npm install @rudderstack/rudder-integration-facebook-react-native
    

OR
    
    
    yarn add @rudderstack/rudder-integration-facebook-react-native
    

### Import module and initialize SDK

Import the module you added to the app and include it in your React Native SDK initialization, as shown:
    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native"
    import facebook from '@rudderstack/rudder-integration-facebook-react-native';
    
    const config = {
      dataPlaneUrl: DATA_PLANE_URL,
      withFactories: [facebook],
    }
    rudderClient.setup(WRITE_KEY, config)
    

  1. Add the repository:


    
    
    repositories {
        mavenCentral()
    }
    

  2. Add the following lines to your`app/build.gradle` file under the`dependencies` section:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.rudderstack.android.integration:facebook:1.0.0'
    implementation 'com.facebook.android:facebook-android-sdk:11.1.0'
    

  


  3. Open your`/app/res/values/strings.xml` file and add the following lines. **Replace`[APP_ID` with your actual app ID**.


    
    
    <string name="facebook_app_id">[APP_ID]</string>
    <string name="fb_login_protocol_scheme">fb[APP_ID]</string>
    

  


  4. In the`app/manifests/AndroidManifest.xml`file, add a`meta-data` element to the`application` element:


    
    
    <application ...="" android:label="@string/app_name">
      ...
      <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"></meta-data>
      ...
    </application>
    

  5. Change the initialization of your`RudderClient` in your`Application` class:


    
    
    val rudderClient = RudderClient.getInstance(
        this,
        WRITE_KEY,
        RudderConfig.Builder()
            .withDataPlaneUrl(DATA_PLANE_URL)
            .withFactory(FacebookIntegrationFactory.FACTORY)
            .build()
    )
    

  1. Add the following line to your [CocoaPods](<https://cocoapods.org>)`Podfile`:


    
    
    pod 'Rudder-Facebook'
    

  


  2. Initialize the Facebook App Events iOS SDK just before intializing the RudderStack iOS (Obj-C) SDK:


    
    
    [[FBSDKApplicationDelegate sharedInstance] application:application
                                 didFinishLaunchingWithOptions:launchOptions];
    

  


  3. Send the user’s consent to App Events as shown below:


For **Objective-C** :
    
    
    // Set AdvertiserTrackingEnabled to YES if a user provides consent
    [FBSDKSettings setAdvertiserTrackingEnabled:YES];
    // Set AdvertiserTrackingEnabled to NO if a user does not provide consent
    [FBSDKSettings setAdvertiserTrackingEnabled:NO];
    

  


For **Swift** :
    
    
    // Set AdvertiserTrackingEnabled to true if a user provides consent
    Settings.setAdvertiserTrackingEnabled(true)
    // Set AdvertiserTrackingEnabled to false if a user does not provide consent
    Settings.setAdvertiserTrackingEnabled(false)
    

  


  4. Configure your project by adding the following lines to`(<dict>...</dict>)` in your`Info.plist` :


    
    
    <key>CFBundleURLTypes</key>
    <array>
    <dict>
    <key>CFBundleURLSchemes</key>
    <array>
    <string>fbAPP-ID</string>
    </array>
    </dict>
    </array>
    <key>FacebookAppID</key>
    <string>APP-ID</string>
    <key>FacebookClientToken</key>
    <string>CLIENT-TOKEN</string>
    <key>FacebookDisplayName</key>
    <string>APP-NAME</string>
    

  


> ![info](/docs/images/info.svg)
> 
> Make sure you replace`fbAPP-ID` ,`APP-ID`,`CLIENT-TOKEN`,`APP-NAME` with the app-specific details from the [Facebook for Developers platform](<https://developers.facebook.com/>).

  5. After adding the dependency, register the`RudderFacebookFactory` with your`RudderClient` initialization as a`factory` of`RudderConfig`. To do this, run the following command to import the`RudderFacebookFactory.h` file in your`AppDelegate.m` file:


    
    
    #import <rudder-facebook>
    

  


  6. Add the RudderStack iOS (Obj-C) SDK initialization:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderFacebookFactory instance]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Facebook App Events 13.0.0 and above.

  1. Install`RudderFacebookAppEvents` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your`Podfile`:


    
    
    pod 'RudderFacebookAppEvents', '~>; 1.0.0'
    

  


  2. Run the`pod install` command.
  3. Import the SDK depending on your preferred platform:


    
    
    import RudderFacebookAppEvents
    

  

    
    
    @import RudderFacebookAppEvents;
    

  


  4. Add the imports to your`AppDelegate` file under the`didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
            
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderFacebookAppEventsDestination())
    

  

    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderFacebookAppEventsDestination alloc] init]];
    

## Identify

> ![warning](/docs/images/warning.svg)
> 
> For Facebook App Events, RudderStack supports the`identify` calls only in mobile device mode.

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to set the `userId` through the `setUserID` method from `AppEventsLogger`.

RudderStack sets the following properties (if available) using the `setUserData` method.

RudderStack property| Data type| App Events property  
---|---|---  
`traits.email`  
`context.traits.email`| String| `em`  
`traits.firstName`  
`context.traits.firstName`| String| `fn`  
`traits.lastName`  
`context.traits.lastName`| String| `ln`  
`traits.phone`  
`context.traits.phone`| String| `ph`  
`traits.gender`  
`context.traits.gender`| String| `ge`  
`traits.birthday`  
`context.traits.birthday`| String| `db`  
`traits.city`  
`context.traits.city`| String| `ct`  
`traits.state`  
`context.traits.state`| String| `st`  
`traits.zip`  
`context.traits.zip`| String| `zp`  
`traits.country`  
`context.traits.country`| String| `cn`  
  
> ![warning](/docs/images/warning.svg)
> 
> Make sure you pass the above properties in their specific format. Otherwise, RudderStack will ignore them and not map to any Facebook properties.

A sample `identify` call for an iOS application is shown below:
    
    
    [[RSClient sharedInstance] identify:@"developer_user_id"
                                     traits:@{@"email": @"bar@foo.com"}];
    

## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

RudderStack logs the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to Facebook using the `logEvent` method of the `AppEventsLogger` class. It uses the same `eventName` as you have passed in the `track` call along with all `properties`, after converting them into the accepted format.

A sample `track` call for an iOS application is as shown:.
    
    
    [[RSClient sharedInstance] track:@"Accepted Terms of Service"
                          properties:@{
                              @"foo": @"bar",
                              @"foo_int": @134
                          }];
    

> ![info](/docs/images/info.svg)
> 
> When`revenue` and`currency` are present in the event properties of any`track` call, RudderStack makes a`Purchase` call to Facebook using its`logPurchase` API along with the normal`track` call using the`logEvent` API.
> 
> If`currency` is absent in the event properties, RudderStack sets the default value to`USD`.

#### **Supported mappings for iOS v2**

This section lists some `track` event and property mappings which are **applicable only** when sending events via the [iOS SDK v2](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/ios-v2/>) device mode.

The following table lists the `track` event properties mappings between RudderStack and Facebook App Events:

RudderStack property| Facebook App Events property  
---|---  
`product_id`| ContentID  
`rating`| MaxRatingValue  
`name`| AdType  
`order_id`| OrderID  
`currency`| Currency  
`query`| Query  
`description`| Description  
  
The following table lists the ecommerce events mappings between RudderStack and Facebook App Events:

RudderStack event| Facebook App Events event  
---|---  
Products Searched| Search  
Products Viewed| View Content  
Product Added| Add to Cart  
Product Added To Wishlist| Add to Wishlist  
Payment Info Entered| Add Payment Info  
Checkout Started| Initiate Checkout  
Order Completed| Purchase  
Promotion Clicked| In-App Ad Click  
Promotion Viewed| In-App Ad Impression  
Product Reviewed| Rate  
Spend Credits| Spent Credits  
  
RudderStack also supports the following Lifecycle events and maps them as it is before sending them to Facebook App Events:

  * Complete Registration
  * Achieve Level
  * Complete Tutorial
  * Unlock Achievement
  * Subscribe
  * Start Trial


## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) method lets you record your website’s page views with any additional relevant information about the viewed page. You need not pass the event name as RudderStack automatically sets it to `Viewed Page`.

A sample `page` call made using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) is show below:
    
    
    rudderanalytics.page();
    

> ![info](/docs/images/info.svg)
> 
> The`page` call is directly passed on to Facebook as a`track` event via its`logEvent` API, with the event name as`Viewed Page` along with the the associated properties.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen.

A sample `screen` call using the iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. is as shown:
    
    
    [[RSClient sharedInstance] screen:@"Home" properties:@{
        @"category" : @"launcher"
    }];
    

In the above snippet, RudderStack captures the `name` and `category` of the viewed screen and sends this information to Facebook as a `track` event `Viewed Home screen` by leveraging Facebook’s `logEvent` API.

## Limited Data Use

In July 2020, Facebook released a [Limited Data Use](<https://developers.facebook.com/docs/marketing-apis/data-processing-options>) feature to give businesses better control over how their data is used in their **California Consumer Privacy Act (CCPA)** compliance efforts.

Using this, you can send the **Limited Data Use** data processing parameters to Facebook for each event via RudderStack, so that Facebook can appropriately apply the user’s data choice.

To use this feature, enable the **Limited Data Use** setting in the RudderStack dashboard and control its behavior via the following data processing parameters:

**Parameter**| **Default Value**| **Description**  
---|---|---  
Data Processing Options State| `0`| Use Facebook’s geolocation to determine the end-user’s state.  
Data Processing Options Country| `0`| Use Facebook’s geolocation to determine the end-user’s country.  
  
> ![success](/docs/images/tick.svg)
> 
> Learn more about the different [data processing options](<https://developers.facebook.com/docs/marketing-apis/data-processing-options>) accepted by Facebook.

## Configure App Events SDK based on user consent

This section highlights the different consent-based options for configuring the App Events SDK.

### Disable automatically logged events

To disable automatic event logging, open the application’s`.plist` as code in Xcode and add the following XML to the property dictionary:
    
    
    <key>FacebookAutoLogAppEventsEnabled</key>
    <false></false>
    

In some cases, you can delay the collection of automatically logged events to obtain user consent or fulfill legal obligations instead of disabling it entirely. To do so, call the`setAutoLogAppEventsEnabled` method of the`FBSDKSettings` class to re-enable auto-logging after the end-user provides the required consent.

In **Objective-C** :
    
    
    [FBSDKSettings setAutoLogAppEventsEnabled:YES];
    

  


In **Swift** :
    
    
    FBSDKSettings.setAutoLogAppEventsEnabled(true)
    

  


To suspend event collection for any reason, set the`setAutoLogAppEventsEnabled` method to`NO` for iOS or`false` for Swift:

In **Objective-C** :
    
    
    [FBSDKSettings setAutoLogAppEventsEnabled:NO];
    

  


In **Swift** :
    
    
    FBSDKSettings.setAutoLogAppEventsEnabled(false)
    

  


To disable automatically logged events, add the following to your`AndroidManifest.xml` file:
    
    
    <application>
      ...
      <meta-data android:name="com.facebook.sdk.AutoLogAppEventsEnabled" android:value="false"></meta-data>
      ...
    </application>
    

  


In some cases, you can delay the collection of automatically logged events to obtain user consent or fulfill legal obligations instead of disabling it entirely. To do so, call the`setAutoLogAppEventsEnabled()` method of the`FacebookSDK` class and set it to`true` . This re-enables event logging after the end-user has provided the required consent.
    
    
    setAutoLogAppEventsEnabled(true);
    

To suspend event logging again for any reason, set the`setAutoLogAppEventsEnabled()` method to`false`:
    
    
    setAutoLogAppEventsEnabled(false);
    

### Disable collection of advertiser IDs

To disable the collection of advertiser ID, open the application’s`.plist` as code in Xcode and add the following XML to the property dictionary:
    
    
    <key>FacebookAdvertiserIDCollectionEnabled</key>
    <false></false>
    

  


In some cases, you can delay the collection of`advertiser_id` to obtain the user consent or fulfill any legal obligations instead of disabling it entirely. To do so, call the`setAdvertiserIDCollectionEnabled` method of the`FBSDKSettings` class and set it to`YES` for iOS, or`true` for Swift after the end-user provides consent:

In **Objective-C** :
    
    
    [FBSDKSettings setAdvertiserIDCollectionEnabled:@YES];
    

  


In **Swift** :
    
    
    FBSDKSettings.setAdvertiserIDCollectionEnabled(true);
    

  


To suspend collection for any reason, set the`setAdvertiserIDCollectionEnabled` method to`NO` for iOS or`false` for Swift.

In **Objective-C** :
    
    
    [FBSDKSettings setAdvertiserIDCollectionEnabled:@NO];
    

  


In **Swift** :
    
    
    FBSDKSettings.setAdvertiserIDCollectionEnabled(false)
    

  


To disable collection of`advertiser-id`, add the following code to your`AndroidManifest.xml` file:
    
    
    <application>
      ...
      <meta-data android:name="com.facebook.sdk.AdvertiserIDCollectionEnabled" android:value="false"></meta-data>
      ...
    </application>
    

In some cases, you can delay the collection of`advertiser_id` to obtain user consent or fulfill any legal obligations instead of disabling it entirely. To do so, call the`setAdvertiserIDCollectionEnabled()` method of the`FacebookSDK` class and set it to`true` . This re-enables the collection of`advertiser_id` after the end-user provides the required consent:
    
    
    setAdvertiserIDCollectionEnabled(true);
    

To suspend collection for any reason, set the`setAdvertiserIDCollectionEnabled()` method to`false`:
    
    
    setAdvertiserIDCollectionEnabled(false)
    

### Disable automatic SDK initialization

To disable automatic SDK initialization in case of Android, add the following to your`AndroidManifest.xml` file:
    
    
    <application>
      ...
      <meta-data androidname="com.facebook.sdk.AutoInitEnabled" androidvalue="false"></meta-data>
      ...
    </application>
    

In some cases, you can delay the SDK initialization to obtain user consent or fulfill any legal obligations instead of disabling it entirely. To do so, call the class method`setAutoInitEnabled` and set it to`true` to manually initialize the SDK after the end-user provides the required consent.
    
    
    FacebookSdk.setAutoInitEnabled(true)
    FacebookSdk.fullyInitialize()
    

Starting from iOS version 14.5, you need to get the device consent to share data with Facebook by setting the `isAdvertiserTrackingEnabled` property. Refer to Facebook’s [Get device consent](<https://developers.facebook.com/docs/app-events/getting-started-app-events-ios#get-device-consent>) documentation for more information.

## FAQ

#### Where do I get the Facebook App ID?

You can find the **Facebook App ID** by logging into your [Facebook Developer account](<https://developers.facebook.com/>), and navigating to the **Home** page of your application’s dashboard:

[![](/docs/images/event-stream-destinations/fb-app-events-app-id.webp)](</docs/images/event-stream-destinations/fb-app-events-app-id.webp>)

#### Where do I get the Facebook Client Token?

You can find the **Facebook Client Token** by logging into your [Facebook Developer account](<https://developers.facebook.com/>) and navigating to **Settings** > **Advanced** > **Security** section in the application’s dashboard:

[![](/docs/images/event-stream-destinations/fb-app-events-client-token.webp)](</docs/images/event-stream-destinations/fb-app-events-client-token.webp>)