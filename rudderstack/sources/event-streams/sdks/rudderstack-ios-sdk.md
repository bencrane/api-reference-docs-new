# RudderStack iOS (Obj-C) SDK

Use the RudderStack iOS (Obj-C) SDK to send events from your iOS apps to various destinations.

* * *

  * __38 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **iOS (Obj-C) SDK is legacy and will be deprecated soon.**
> 
>   * For new implementations, RudderStack recommends using the [iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) instead.
>   * If you are planning to migrate your existing implementation from the iOS (Obj-C) SDK to the iOS (Swift) SDK, see the [Breaking Changes in iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/breaking-changes/>) first.
> 


With RudderStack’s iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. , you can track events from your iOS applications and send them to your specified destinations.

See the [iOS (Obj-C) SDK GitHub codebase](<https://github.com/rudderlabs/rudder-sdk-ios>) for the implementation details.

[![](https://img.shields.io/badge/dynamic/json?color=blue&label=pod&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Frudderlabs%2Frudder-sdk-ios%2Fdevelop%2Fpackage.json)](<https://github.com/rudderlabs/rudder-sdk-ios/tree/master>)

## Prerequisites

  * A Mac with the latest version of [Xcode](<https://developer.apple.com/xcode/>).
  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up an iOS (Obj-C) source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> In the dashboard, the **Setup** tab for the source has an SDK installation snippet containing both the write key and the data plane URL. You can use it to integrate the iOS (Obj-C) SDK into your project.

## Install SDK

You can install the iOS (Obj-C) SDK through [Cocoapods](<https://cocoapods.org/pods/Rudder>) and [Carthage](<https://github.com/Carthage/Carthage>). The recommended and easiest way to add the SDK to your project is through `Podfile`. To do so, follow these steps:

  1. Add the RudderStack SDK to your `Podfile`:


    
    
    pod 'Rudder'
    

  2. Then, run the following command:


    
    
    pod install
    

  1. Add the RudderStack SDK to your `Cartfile`:


    
    
    github "rudderlabs/rudder-sdk-ios"
    

  2. Run the following command:


    
    
    carthage update
    

> ![warning](/docs/images/warning.svg)
> 
> Remember to include the following code in all `.m` and `.h` files or your `.swift` files where you want to refer to or use RudderStack SDK classes.
    
    
    #import <Rudder/Rudder.h>
    
    
    
    import Rudder
    

> ![danger](/docs/images/danger.svg)
> 
> RudderStack uses [SQLite](<https://sqlite.org/index.html>) to store events locally before sending them to the RudderStack data plane. Making calls like `SQLite.shutdown()` which is not thread-safe might lead to unexpected crash.

### Using Swift Package Manager (SPM)

You can also install the iOS (Obj-C) SDK through Swift Package Manager (SPM) via one of the following methods:

To add the RudderStack package in Xcode:

  1. Go to **File** > **Add Package**.
  2. In the search bar, enter the package repository: `https://github.com/rudderlabs/rudder-sdk-ios.git`.
  3. In **Dependency Rule** , select **Up to Next Major Version** and enter the value as **1.8.0** as shown:

![SPM dependency rule](/docs/images/event-stream-sources/spm-dependency-rule.webp)

  4. Select the project to which you want to add the package and click **Add Package**.


To leverage the RudderStack Swift package, include the following snippet in your project:
    
    
    // swift-tools-version:5.5
    // The swift-tools-version declares the minimum version of Swift required to build this package.
    
    import PackageDescription
    
    let package = Package(
        name: "RudderStack",
        products: [
            // Products define the executables and libraries a package produces, and make them visible to other packages.
            .library(
                name: "RudderStack",
                targets: ["RudderStack"]),
        ],
        dependencies: [
            // Dependencies declare other packages that this package depends on.
            .package(url: "git@github.com:rudderlabs/rudder-sdk-ios.git", from: "1.8.0")
        ],
        targets: [
            // Targets are the basic building blocks of a package. A target can define a module or a test suite.
            // Targets can depend on other targets in this package, and on products in packages this package depends on.
            .target(
                name: "RudderStack",
                dependencies: [
                    .product(name: "Rudder", package: "rudder-sdk-ios")
                ]),
            .testTarget(
                name: "RudderStackTests",
                dependencies: ["RudderStack"]),
        ]
    )
    

## Initialize SDK

Put the following code in your `AppDelegate.m` file under the method `didFinishLaunchingWithOptions`:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    

A shared instance of `RSClient` is accessible after the initialization by `[RSClient sharedInstance]`.
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

A shared instance of `RSClient` is accesible after the initialization by `RSClient.sharedInstance()`.

RudderStack automatically tracks the following [application lifecycle events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>):

  * [`Application Installed`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>)
  * [`Application Updated`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>)
  * [`Application Opened`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>)
  * [`Application Backgrounded`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-backgrounded>)


You can disable these events using the `withTrackLifecycleEvents` method of `RSConfigBuilder` and passing `false`. However, it is highly recommended to keep them enabled.

RudderStack supports all major API calls across all iOS devices via the SDK. These include the `track`, `identify`, and `screen` calls.

#### OneTrust consent

The iOS (Obj-C) SDK natively integrates with the OneTrust consent manager and lets you specify the user’s consent during initialization.

See [OneTrust Consent Management for iOS](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/ios/>) for more information.

## Configure SDK options

You can configure the RudderStack client based on the following parameters using `RSConfigBuilder`:

Parameter| Type| Description| Default value  
---|---|---|---  
`logLevel`| `int`| Controls the level of log details you see from the SDK.| `RSLogLevelNone`  
`dataPlaneUrl`| `string`| Your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>)| -  
`flushQueueSize`| `int`| Number of events in a batch request sent to the server.| `30`  
`dbThresholdCount`| `int`| Number of events to be saved in the `SQLite` database. Once the limit is reached, the SDK deletes the older events from the database.| `10000`  
`sleepTimeout`| `int`| Minimum waiting time to flush the events to the server.| `10 seconds`  
`configRefreshInterval`| `int`| Fetches the configuration from the dashboard after the specified time.| `2 hours`  
`trackLifecycleEvents`| `boolean`| Determines if the SDK should capture the application life cycle events automatically.| `true`  
`collectDeviceId`| `boolean`| Determines if the SDK should automatically collect the device ID. If set to `NO`, it does not send `context.device.id` as a part of the event payload. See Disabling device ID collection for more information.| `true`  
`autoSessionTracking`| `boolean`| Determines if the SDK should automatically track the user sessions. See Track user sessions for more information.| `true`  
`sessionTimeout`| `int`| Maximum inactivity period before the session expires.| `300000 ms` (5 minutes)  
`recordScreenViews`| `boolean`| Determines if the SDK should automatically capture the screen view events. See Automatically capture screen views for more details.| `false`  
`enableBackgroundMode`| `boolean`| Determines if the SDK should send the events for some time when the app is moved to the background. Currently, this feature is available only for `iOS` & `tvOS`.| `false`  
`gzip`| `boolean`| Gzips the event requests.| `true`  
`dbEncryption`| `object`| Determines if the SDK should encrypt/decrypt the database using the specified key. See Encrypt RudderStack databases for more information.| -  
`controlPlaneUrl`| `string`| Change this parameter **only** if you are self-hosting the control plane or using a custom domain to serve the SDK. The iOS (Obj-C) SDK automatically adds `/sourceConfig` along with this URL to fetch the required configuration.| `https://api.rudderlabs.com`  
  
### Specify source configuration

> ![info](/docs/images/info.svg)
> 
> The information in this section is applicable for the following scenarios:
> 
>   * If you are self-hosting the control plane.
>   * If you are using a custom domain to serve the SDK.
> 


The iOS (Obj-C) SDK generally fetches the required source configuration from the [RudderStack dashboard](<https://app.rudderstack.com>) (control plane) in case of device mode destinations.

However, if you are self-hosting the control plane using [Control plane lite](<https://github.com/rudderlabs/config-generator#rudderstack-control-plane-lite>) or serving the SDK over a custom domain, then:

  1. Follow the steps in [this guide](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#using-sdk-sources-set-up-in-self-hosted-control-plane>) to host the source configuration.
  2. Specify the `controlPlaneUrl` parameter (without `/sourceConfig`, as the SDK automatically appends this to the URL) in `RSConfigBuilder` that points to your hosted source configuration file.


> ![warning](/docs/images/warning.svg)
> 
> Do not pass the `controlPlaneUrl` parameter during the SDK initialization if you have set up the iOS (Obj-C) source in the [RudderStack dashboard](<https://app.rudderstack.com>).

## Gzip requests

> ![info](/docs/images/info.svg)
> 
> This feature requires [rudder-server](<https://github.com/rudderlabs/rudder-server>) **v1.4 or higher**. Otherwise, your events might fail.

The iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. automatically gzips event requests. To turn off this feature, set the `Gzip` parameter to `NO` while initializing the SDK:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withGzip:NO];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withGzip(false)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc. Once you identify the user, the SDK persists all the user information and passes it on to the subsequent `track` or `screen` calls. To reset the user identification, you can use the `reset` method.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * For older SDK versions (< v1.19.0), the iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
>   
>  For new implementations, use the iOS (Swift) SDK instead. captures the device ID and uses that as `anonymousId` for identifying the user. This helps the SDK to track the users across the application installation.
>   * According to the Apple [documentation](<https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor>), if the device has multiple apps from the same vendors, all those apps will be assigned the same device ID. If all applications from a vendor are uninstalled, then on next install the app will be assigned a new device ID.
>   * Starting from v1.19.0, the SDK uses a UUID as `anonymousId` instead of the device ID. If you are upgrading from a previous SDK version, see How RudderStack sets anonymous ID for more information on how the SDK collects and sets `anonymousId`.
> 


An example `identify` event is as shown:
    
    
    [[RSClient sharedInstance] identify:@"test_user_id"
    traits:@{@"foo": @"bar",
            @"foo1": @"bar1",
            @"email": @"test@gmail.com",
            @"key_1" : @"value_1",
            @"key_2" : @"value_2"
    }
    ];
    
    
    
    RSClient.sharedInstance()?.identify("test_user_id", traits: [
        "key_1": "value_1",
        "key_2": "value_2",
        "email": "test@gmail.com"
    ])
    

The `identify` method accepts the following parameters:

Name| Data type| Description  
---|---|---  
`userId`  
Required| `NSString`| Unique identifier for the user.  
`traits`| `NSDictionary`| User traits. Use the `dict` method of `RudderTraits` to convert to `NSDictionary` easily.  
`options`| `RudderOption`| Event-level options.  
  
### Set custom anonymous ID

RudderStack use the `deviceId` as `anonymousId` by default. You can use the following method to override and use your own `anonymousId` with the SDK.

An example of setting the `anonymousId` is shown below:
    
    
    [RSClient putAnonymousId:<ANONYMOUS_ID>];
    
    
    
    RSClient.putAnonymousId("<ANONYMOUS_ID>")
    

To retrieve `anonymousId`, use the `anonymousId` instance property:
    
    
    [RSClient getInstance].anonymousId;
    

### Turn off device ID collection

Starting from v1.19.0, you can disable the collection of device ID by setting the `withCollectDeviceId` API of the `RSConfigBuilder` class to `NO`.

You will observe the following changes when this API is set to false:

  * The SDK does not send `context.device.id` as a part of the event payload.
  * The SDK replaces the existing `anonymousId` (if it is equal to the device ID) with a UUID.


> ![info](/docs/images/info.svg)
> 
> These changes are introduced to make the SDK more compliant with all policies around the device ID collection.
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withCollectDeviceId:NO];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withCollectDeviceId(false)
        .withDataPlaneUrl(DATA_PLANE_URL)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

> ![warning](/docs/images/warning.svg)
> 
> If you are upgrading to the latest SDK from a previous version (< v1.19.0) **and** disabling device ID collection using `withCollectDeviceId:NO`:
> 
>   * Make sure your user transformations are not dependent on `context.device.id` as the SDK will not send this value in the event payload.
>   * The `context.device.id` column in your warehouse destination will not be populated henceforth (it will still contain data populated by the previous SDK version).
> 


### How SDK sets anonymous ID

#### Case 1. Fresh SDK installation

For a fresh installation of the iOS (Obj-C) SDK v1.19.0 and later, RudderStack uses UUID as `anonymousId` regardless of whether `withCollectDeviceId` is set to `YES` or `NO`.

#### Case 2. Updating SDK from older version

If you are updating your iOS (Obj-C) SDK from an older version (< v1.19.0), then:

  * RudderStack will continue to use the device ID as `anonymousId` \- it will not break the existing SDK behavior **until** you set `withCollectDeviceId` to `NO`.
  * If you set `withCollectDeviceId` to `NO`, the SDK checks if the existing `anonymousId` is a device ID. If yes, it sets a new UUID as the `anonymousId`.
  * If you have used the `putAnonymousId` method to set your own `anonymousId`, then the SDK will **not** modify it even if you set `withCollectDeviceId` to `NO`.


### Set custom user ID

You can pass a custom ID along with the standard `userId` in your `identify` calls. RudderStack adds this value under `context.externalId`.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports passing `externalId` only in the `identify` events. You must not pass this ID in other API calls like `track`, `page`, etc.

The following snippet shows how to add an `externalId` to your `identify` event:
    
    
    RSOption *identifyOptions = [[RSOption alloc] init];
    [identifyOptions putExternalId:@"brazeExternalId" withId:@"some_external_id_1"];
    [[RSClient sharedInstance] identify:@"1hKOmRA4GRlm"
                                 traits:@{@"firstname": @"Alex"}
                                options:identifyOptions];
    
    
    
    let identifyOptions = RSOption()
    identifyOptions.putExternalId("brazeExternalId", withId: "some_external_id_1")
    RSClient.sharedInstance()?.identify("1hKOmRA4GRlm", traits: ["firstname": "Alex"], options: identifyOptions)
    

## Track

You can record the users’ activity through the `track` method. Every user action is called as an **event**.

A sample `track` event is as shown:
    
    
    [[RSClient sharedInstance] track:@"simple_track_with_props" properties:@{
        @"key_1" : @"value_1",
        @"key_2" : @"value_2"
    }];
    
    
    
    RSClient.sharedInstance()?.track("test_user_id", properties: [
        "key_1": "value_1",
        "key_2": "value_2"
    ])
    

The `track` method accepts the following parameters:

Name| Data type| Description  
---|---|---  
`eventName`  
Required| `NSString`| Event name.  
`properties`| `NSDictionary`| Properties associated with the `track` event.  
`options`| `RudderOption`| Event-level options.  
  
## Screen

You can use the `screen` call to record whenever the user sees a screen on the mobile device. You can also send some extra properties along with this event.

An example of the `screen` event is as shown:
    
    
    [[RSClient sharedInstance] screen:@"ViewController"];
    
    
    
    RSClient.sharedInstance()?.screen("ViewController")
    

The `screen` method accepts the following parameters:

Name| Data type| Description  
---|---|---  
`screenName`  
Required| `NSString`| Screen name.  
`properties`| `NSDictionary`| Properties associated with the `screen` event.  
`options`| `RudderOption`| Event-level options.  
  
#### Automatically capture screen views

To automatically capture the screen views, you can enable the `recordScreenViews` parameter while initializing the SDK:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withRecordScreenViews:YES];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withRecordScreenViews(true)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

Note that if automatic screen recording is enabled, RudderStack removes every instance of `ViewController` in the `screen` event.

For example, if automatic screen recording is enabled and you set the `ViewController` class name to `HomeViewController`, then the SDK sets the screen event name to `Home`.

For more details related to this implementation, refer to the [iOS (Obj-C) SDK repository](<https://github.com/rudderlabs/rudder-sdk-ios/blob/791f71c94b323d20d59dacc8aa8bb8626ad62245/Sources/Classes/UIViewController%2BRSScreen.m#L53>).

## Group

The `group` call associates a user to a specific organization. A sample `group` call for the API is below:
    
    
    [[RSClient sharedInstance] group:@"sample_group_id"
      traits:@{@"foo": @"bar",
                @"foo1": @"bar1",
                @"email": @"ruchira@gmail.com"}
    ];
    
    
    
    RSClient.sharedInstance()?.group("test_group_id", traits: [
        "key_1": "value_1",
        "key_2": "value_2"
    ])
    

Alternatively, you can use the following method signature

Name| Data type| Description  
---|---|---  
`groupId`  
Required| `String`| Identifier associated with the group.  
`traits`| `NSDictionary`| Group traits.  
  
**Note** : The SDK **does not** persist the `group` traits across the sessions.  
`options`| `RudderOption`| Event-level options.  
  
## Alias

The `alias` call lets you associate the user with a new identification.

> ![info](/docs/images/info.svg)
> 
> `alias` is an advanced API that lets you change the user identifier explicitly. It is useful when managing identities for some of the downstream destinations.

A sample `alias` call is shown:

RudderStack recommends using the default invocation in scenarios where you only want to replace the current `userId` with the new `userId`.

  * Specify only new user ID **without** previous user ID and event-level options:


    
    
    [[RSClient sharedInstance] alias:@"newId"];
    
    
    
    RSClient.sharedInstance()?.alias("newId")
    

  * Specify new user ID and event-level options **without** previous user ID:


    
    
    [[RSClient sharedInstance] alias:@"newId" options:options];
    
    
    
    RSClient.getInstance().alias("newId", options: options)
    

In this case, the SDK automatically populates the `previousId` field with the previously-persisted `userId`/`anonymousId`.

RudderStack recommends using the following invocations in cases where you want to explicitly pass the previous user ID that may be required by some downstream destinations, for example, MoEngage.

  * Specify new user ID and previous user ID **with** event-level options:


    
    
    [[RSClient sharedInstance] alias:@"newId" previousId:@"previousId" options:options];
    
    
    
    RSClient.getInstance().alias("newId", previousId: "previousId", options: options)
    

  * Specify new user ID and previous user ID **without** event-level options:


    
    
    [[RSClient sharedInstance] alias:@"newId" previousId:@"previousId"];
    
    
    
    RSClient.getInstance().alias("newId", previousId: "previousId")
    

The following table highlights the supported `alias` API parameters:

Name| Data type| Description  
---|---|---  
`newId`  
Required| `String`| The new identifier (`userId`) to assign to the user.  
`previousId`| `String`| The old (current) user identifier.  
  
Note that:

  * The iOS (Obj-C) SDK supports explicitly passing the `previousId` field from **v1.31.0** onwards.
  * If not provided explicitly, the SDK populates this field with the current `userId`/ `anonymousId`.

  
`options`| `RudderOption`| Event-level options.  
  
Once you make the `alias` call, RudderStack replaces the old `userId` with the new user identifier (`newId`) and persists that identification across the sessions.

## Reset

You can use the `reset` method to clear the persisted user traits. It also resets the `anonymousId` with a new UUID if you call it with `YES` (for SDK v1.19.0 and later). To clear only user traits, call `reset` with `NO`.

In [session tracking](<https://rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#:~:text=tracking%20is%20enabled%3A-,sessionId,-%28Number%29%3A%20The%20session>), calling the `reset` method clears the current `sessionId` and generates a new one.

A sample `reset` call is shown:
    
    
    [[RSClient sharedInstance] reset:NO];
    
    
    
    RSClient.sharedInstance()?.reset(false)
    

## Encrypt RudderStack databases

> ![info](/docs/images/info.svg)
> 
> This feature is available in the iOS (Obj-C) SDK v1.20.0 and later.

The iOS (Obj-C) SDK uses a [SQLite](<https://sqlite.org/index.html>) database to store events before sending them to the RudderStack backend (data plane).

By default, SQLite databases created by RudderStack are not encrypted but they are still protected by iOS - similar to data in any iOS application. To add an extra level of security, you can use the [SQLCipher](<https://www.zetetic.net/sqlcipher/>) extension to encrypt the database content and SQLite metadata.

#### Using CocoaPods

> ![info](/docs/images/info.svg)
> 
> This feature is supported for SQLCipher v4.0 and later.

**Step 1: Integrate SDK with SQLCipher**

  1. `RudderDatabaseEncryption` is available through [CocoaPods](<https://cocoapods.org/>). To install it, add the following line to your `Podfile`:


    
    
    pod 'RudderDatabaseEncryption', '~> 1.0.0'
    

  2. Run the `pod install` command.


**Step 2: Import the iOS (Obj-C) SDK**
    
    
     @import RudderDatabaseEncryption;
    
    
    
    import RudderDatabaseEncryption
    

**Step 3: Initialize the SDK**

Place the following snippet in your app’s `AppDelegate` under `didFinishLaunchingWithOptions` method:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withDBEncryption:[[RSDBEncryption alloc] initWithKey:@"<password>" enable:YES databaseProvider:[RSEncryptedDatabaseProvider new]]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withDBEncryption(RSDBEncryption(key: "<password>", enable: true, databaseProvider: RSEncryptedDatabaseProvider()))
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

#### Using Swift Package Manager (SPM)

**Register an RSDatabaseProvider implementation**

The standard SQLite library does not support encryption out of the box. Hence, you need to integrate a third-party option into your codebase. `RSDatabaseProvider` acts as a bridge between this third-party code and RudderStack, and uses SQLCipher for the implementation.

> ![info](/docs/images/info.svg)
> 
> To integrate SQLCipher with your application, see the instructions for the [community](<https://www.zetetic.net/sqlcipher/ios-tutorial/>) or [commercial](<https://www.zetetic.net/sqlcipher/sqlcipher-ios/>) editions.

Once SQLCipher is correctly set up, add the below implementation of the `RSDatabaseProvider` protocol in your project.

> ![warning](/docs/images/warning.svg)
> 
> Copy-paste the code exactly as given below and change the class names as per your requirement.
    
    
    @interface RSEncryptedDatabase : NSObject <RSDatabase>
    
    @end
    
    @implementation RSEncryptedDatabase {
        sqlite3 *db;
    }
    
    - (int)open_v2:(const char *)filename flags:(int)flags zVfs:(const char *)zVfs {
        return sqlite3_open_v2(filename, &db, flags, zVfs);
    }
    
    - (int)exec:(const char *)zSql xCallback:(callback)xCallback pArg:(void *)pArg pzErrMsg:(char * _Nullable *)pzErrMsg {
        return sqlite3_exec(db, zSql, xCallback, pArg, pzErrMsg);
    }
    
    - (int)close {
        return sqlite3_close(db);
    }
    
    - (int)step:(void *)pStmt {
        return sqlite3_step(pStmt);
    }
    
    - (int)finalize:(void *)pStmt {
        return sqlite3_finalize(pStmt);
    }
    
    - (int)prepare_v2:(const char *)zSql nBytes:(int)nBytes ppStmt:(void **)ppStmt pzTail:(const char **)pzTail {
        return sqlite3_prepare_v2(db, zSql, nBytes, (sqlite3_stmt **)(ppStmt), pzTail);
    }
    
    - (int)column_int:(void *)pStmt i:(int)i {
        return sqlite3_column_int(pStmt, i);
    }
    
    - (const unsigned char *)column_text:(void *)pStmt i:(int)i {
        return sqlite3_column_text(pStmt, i);
    }
    
    - (int)key:(const void *)pKey nKey:(int)nKey {
        return sqlite3_key(db, pKey, nKey);
    }
    
    - (int)last_insert_rowid {
        int64_t lastRowId = sqlite3_last_insert_rowid(db);
        return (int)lastRowId;
    }
    
    @end
    
    @interface EncryptedDatabaseProvider : NSObject<RSDatabaseProvider>
    
    @end
    
    @implementation EncryptedDatabaseProvider
    
    - (id<RSDatabase>)getDatabase {
        return [RSEncryptedDatabase new];
    }
    
    @end
    
    
    
    class EncryptedDatabase: RSDatabase {
        
        private var db: OpaquePointer?
        
        func open_v2(_ filename: UnsafePointer<CChar>?, flags: Int32, zVfs: UnsafePointer<CChar>?) -> Int32 {
            return sqlite3_open_v2(filename, &db, flags, zVfs)
        }
        
        func exec(_ zSql: UnsafePointer<CChar>?, xCallback: callback?, pArg: UnsafeMutableRawPointer?, pzErrMsg: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>?) -> Int32 {
            return sqlite3_exec(db, zSql, xCallback, pArg, pzErrMsg)
        }
            
        func prepare_v2(_ zSql: UnsafePointer<CChar>?, nBytes: Int32, ppStmt: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, pzTail: UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Int32 {
            return sqlite3_prepare_v2(db, zSql, nBytes, UnsafeMutablePointer(OpaquePointer(ppStmt)), pzTail)
        }
        
        func close() -> Int32 {
            return sqlite3_close(db)
        }
        
        func step(_ pStmt: UnsafeMutableRawPointer?) -> Int32 {
            return sqlite3_step(OpaquePointer(pStmt))
        }
        
        func finalize(_ pStmt: UnsafeMutableRawPointer?) -> Int32 {
            return sqlite3_finalize(OpaquePointer(pStmt))
        }
        
        func column_int(_ pStmt: UnsafeMutableRawPointer?, i: Int32) -> Int32 {
            return sqlite3_column_int(OpaquePointer(pStmt), i)
        }
        
        func column_text(_ pStmt: UnsafeMutableRawPointer?, i: Int32) -> UnsafePointer<UInt8> {
            return sqlite3_column_text(OpaquePointer(pStmt), i)
        }
        
        func key(_ pKey: UnsafeRawPointer?, nKey: Int32) -> Int32 {
            return sqlite3_key(db, pKey, nKey)
        }
    
        func last_insert_rowid() -> Int32 {
            return Int32(sqlite3_last_insert_rowid(db))
        }
    }
    
    class EncryptedDatabaseProvider: RSDatabaseProvider {
        func getDatabase() -> RSDatabase {
            return EncryptedDatabase()
        }
    }
    

  2. Register your database provider with the RudderStack iOS (Obj-C) SDK. The following setup code is recommended:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withDBEncryption:[[RSDBEncryption alloc] initWithKey:@"<password>" enable:YES databaseProvider:[EncryptedDatabaseProvider new]]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withDBEncryption(RSDBEncryption(key: "<password>", enable: true, databaseProvider: EncryptedDatabaseProvider()))
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

The iOS (Obj-C) SDK is now configured to support database encryption.

> ![warning](/docs/images/warning.svg)
> 
> After you encrypt the database:
> 
>   * If **no key** is provided, then the SDK deletes the current database with unsent events and creates a new unencrypted database instead.
>   * If a **wrong key** is provided, then the SDK deletes the current database with unsent events and creates a new encrypted database with the given key.
> 

> 
> The SDK does not store the key, so it cannot determine whether the entered key is right or wrong. Hence, if the key cannot decrypt the database, the SDK assumes it to be incorrect and deletes the old events and database.

#### Instructions for linking issues

The Cocoapod `RudderDatabaseEncryption` uses the [SQLCipher](<https://github.com/sqlcipher/sqlcipher>) Cocoapod under the hood to perform encryption. This Cocoapod requires the removal of any references to the standard SQLite system library for it to function as expected.

If you set up a project to inadvertently include a linking reference against the standard SQLite library before SQLCipher, it is possible that the application builds and runs correctly but does not use SQLCipher for encryption. This is not a problem for most projects but there are certain cases where unintentional SQLite linking can occur.

One such example is when using CocoaPods or some other sub-project that declares a dependency on the SQLite3 library. In this case, adding a pod to a project can **silently** modify the project settings in such a way that SQLCipher is not properly linked.

You can identify and fix the above linking issue during the development stage by looking for the below error log from the SDK:
    
    
    RSDBPersistentManager: createDB: Cannot encrypt the Database as SQLCipher wasn't linked correctly.
    

To fix the linking issue, add a linker flag to your project settings to ensure that the Xcode links SQLCipher before SQLite. Follow these steps:

  1. Open the project-level build settings. These are the global project settings, not for the individual application target.
  2. Locate the **Other Linker Flags** setting and add one of the following commands depending on how you are integrating SQLCipher into the app.


> ![warning](/docs/images/warning.svg)
> 
> If you are not adding `SQLCipher` into the app on your own and only using `RudderDatabaseEncryption`, then see only the points 3 and 4 in the below table - depending on whether you are using `use_frameworks!` in your app’s `ios/Podfile`.

Scenario| Command| Notes  
---|---|---  
When using SQLCipher commercial edition static libraries| `$(PROJECT_DIR)/sqlcipher-static-ios/ios-libs/libsqlcipher-ios.a`| Adjust according to the path to the `libsqlcipher-ios.a` you received as a part of the package.  
When using the `sqlcipher.xcodeproj` included in the SQLCipher Git repository| `$(BUILT_PRODUCTS_DIR)/libsqlcipher.a`| -  
When using the SQLCipher CocoaPod with the `use_frameworks` Podfile setting enabled| `-framework SQLCipher`| -  
When using the SQLCipher CocoaPod without the `use_frameworks` Podfile setting enabled| `-lSQLCipher`| -  
  
Once the linker flag is added to the project-level build settings, you should see something like the below image:

[![Project-level build settings](/docs/images/event-stream-sources/flutter-sdk-project-build-settings.webp)](</docs/images/event-stream-sources/flutter-sdk-project-build-settings.webp>)

After adding the linker flag to your project-level build settings, check the target-level build settings to ensure SQLCipher is shown first, as seen below:

[![Target-level build settings](/docs/images/event-stream-sources/flutter-sdk-target-build-settings.webp)](</docs/images/event-stream-sources/flutter-sdk-target-build-settings.webp>)

## Manage user tracking via `optOut` API (GDPR)

RudderStack gives users (e.g., an EU user) the ability to opt out of tracking any user activity until the user gives their consent. You can do this by leveraging RudderStack’s `optOut` API.

The `optOut` API takes `YES` or `NO` as a Boolean value to enable or disable tracking user activities. This flag persists across device reboots.

The following snippet highlights the use of the `optOut` API to disable user tracking:
    
    
    [[RSClient sharedInstance] optOut:YES];
    
    
    
    RSClient.sharedInstance()?.optOut(true)
    

the user grants their consent, you can enable user tracking once again by using the `optOut` API with `NO` or `false` as a parameter sent to it:
    
    
    [[RSClient sharedInstance] optOut:NO];
    
    
    
    RSClient.sharedInstance()?.optOut(false)
    

The `optOut` API is available in iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. starting from version `1.0.24`.

## Set custom context

You can set custom contextual information in the iOS (Obj-C) SDK by using either of the following ways:

### During SDK initialization

You can set custom context during SDK initialization as follows:

> ![info](/docs/images/info.svg)
> 
> This feature is available in the iOS (Obj-C) SDK v1.26.0 and later.
    
    
    RSOption* option = [[RSOption alloc] init];
    [option putCustomContext:@{
            @"category": @"premium",
            @"type": @"gold"
     } withKey:@"tier"];
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [RSClient getInstance:WRITE_KEY config:[builder build] options: option];
    
    
    
    let option = RSOption()
    option.putCustomContext(["category": "premium", "type": "gold"], withKey: "tier")
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
    RSClient.getInstance(WRITE_KEY, config: builder.build(), options: option)
    

Note that:

  * The iOS (Obj-C) SDK persists the contextual information set during SDK initialization for subsequent events but **not** across sessions.
  * Calling the `reset` method clears all the contextual information set during SDK initialization.
  * The contextual information passed at the event level gets precedence over the context set during SDK initialization.


### Using `putCustomContext` method

You can use the `putCustomContext` method on an instance of `RSOption` to set custom contextual information as a nested object within `context` while sending the events.

An example of setting custom context using an instance of `RSOption` and passing it in a `track` call:
    
    
    RSOption* option = [[RSOption alloc] init];
    [option putCustomContext:@{
            @"category": @"premium",
            @"type": @"gold"
     } withKey:@"tier"];
    [[RSClient sharedInstance] track:@"Subscription Purchased" properties:@{
            @"paymentMethod": @"credit card"
    } options:option];
    
    
    
    let option = RSOption()
    option.putCustomContext(["category": "premium", "type": "gold"], withKey: "tier")
    RSClient.getInstance().track(
      "Subscription Purchased", properties: ["paymentMethod": "credit card"], options: option)
    

The `context` object in the created event payload looks like below:
    
    
    {
      "context": {
        "tier": {
          "category": "premium",
          "type": "gold",
        }
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> The SDK does not persist the contextual information set using `putCustomContext` for subsequent events. Hence, you must use this method every time you want to set custom context for an event.

## Set device token

You can pass your `device-token` for Push Notifications to be passed to the destinations which support Push Notification. We set the `token` under `context.device.token`.

Follow the instructions below:
    
    
    [RSClient putDeviceToken:@"your_device_token"];
    
    
    
    RSClient.putDeviceToken("your_device_token")
    

## Set advertisement ID

To set the advertisement ID, you can use the static method `putAdvertisingId` and call it before or after the SDK initialization:
    
    
    [RSClient putAdvertisingId:@"sampleAdvertId"];
    
    
    
    RSClient.putAdvertisingId("advertId")
    

Once set, the advertisement ID persists and gets attached to all the events until it is cleared using the `clearAdvertisingId` method.

To clear the advertisement ID, use the `clearAdvertisingId` method:
    
    
    [[RSClient sharedInstance] clearAdvertisingId];
    
    
    
    RSClient.sharedInstance()?.clearAdvertisingId()
    

The `clearAdvertisingId` method is not static and hence can be called only after the SDK initialization.

## Pass authorization consent (`ATTrackingManager` )

You can pass the [ATTrackingManager.trackingAuthorizationStatus](<https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547038-trackingauthorizationstatus>) to RudderStack. RudderStack then sends it to the relevant destinations as required.

For example, AppsFlyer accepts this parameter for the attribution to work in their [server-to-server mode](<https://support.appsflyer.com/hc/en-us/articles/207034486-Server-to-server-events-API-for-mobile-S2S-mobile-#att-3>).
    
    
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
    {
        // Override point for customization after application launch.
        RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
        [builder withDataPlaneUrl:DATA_PLANE_URL];
        [RSClient getInstance:WRITE_KEY config:[builder build]];
    
        [[[RSClient sharedInstance] context] putAppTrackingConsent:RSATTAuthorize];
    
        return YES;
    }
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    RSClient.sharedInstance()?.context.putAppTrackingConsent(RSATTAuthorize)
    

You can pass the following options to the `putAppTrackingConsent` method:

  * `RSATTNotDetermined`
  * `RSATTRestricted`
  * `RSATTDenied`
  * `RSATTAuthorize`


## Filter events

When sending events to a destination via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you can explicitly specify which events should be discarded or allowed to flow through - by allowlisting or denylisting them.

Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this feature.

## Filter events for specific destinations

The iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. allows you to enable or disable event flow to a specific destination or all destinations to which the source is connected. You can specify these destinations by creating a `RSOption` object as shown:
    
    
    RSOption *option = [[RSOption alloc]init];
    //default value for `All` is true
    [option putIntegration:@"All" isEnabled:YES];
    // specifying destination by its display name
    [option putIntegration:@"Amplitude" isEnabled:YES];
    [option putIntegration:@"<destination display name>" isEnabled:<BOOL>];
    // specifying destination by its Factory instance
    [option putIntegrationWithFactory:[RudderMoengageFactory instance] isEnabled:NO];
    [option putIntegrationWithFactory:[<RudderIntegrationFactory> instance] isEnabled:<BOOL>];
    
    
    
    let option:RSOption = RSOption();
    //default value for `All` is true
    option.putIntegration("All", isEnabled:true)
    // specifying destination by its display name
    option.putIntegration("Amplitude", isEnabled:true)
    option.putIntegration(<DESTINATION DISPLAY NAME>, isEnabled:<BOOL>)
    // specifying destination by its Factory instance
    option.putIntegration(with: RudderMoengageFactory.instance(), isEnabled: true);
    option.putIntegration(with: <RudderIntegrationFactory>.instance(), isEnabled:<BOOL>);
    

The keyword `All` in the above snippet represents all destinations the source is connected to. Its value is set to `true` by default.

> ![info](/docs/images/info.svg)
> 
> Make sure the `destination display name` you pass while specifying the custom destinations should exactly match the destination name as shown [here](<https://app.rudderstack.com/directory>).

You can pass the destination(s) specified in the above snippet to the SDK in two ways:

#### 1\. Passing destinations while initializing SDK

This is helpful when you want to enable/disable sending the events across all event calls made using the SDK to the specified destinations.
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withLoglevel:RSLogLevelDebug];
    [builder withTrackLifecycleEvens:YES];
    [builder withRecordScreenViews:YES;
    [RSClient getInstance:WRITE_KEY config:[builder build] options:option]; // passing the rudderoption object containing the list of destinations you specified
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
                .withLoglevel(RSLogLevelDebug)
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withTrackLifecycleEvens(true)
                .withRecordScreenViews(true)
    RSClient.getInstance(WRITE_KEY, config: builder.build(),options: option)// passing the rudderoption object containing the list of destination(s) you specified
    

#### 2\. Passing destinations while making event calls

This approach is helpful when you want to enable/disable sending only a particular event to the specified destination(s) or if you want to override the specified destinations passed with the SDK initialization for a particular event.
    
    
    [[RSClient sharedInstance] track:@"simple_track_with_props" properties:@{
            @"key_1" : @"value_1",
            @"key_2" : @"value_2"
        } options:option]; // passing the rudderoption object containing the list of destination(s) you specified
    
    
    
    let rudder: RSClient? = RSClient.sharedInstance()
    rudder?.track("track_with_props", properties: [
                "key_1": "value_1",
                "key_2": "value_2",
            ],options:option) // passing the rudderoption object containing the list of destination(s) you specified
    

If you specify the destinations both while initializing the SDK as well as making an event call, then the destinations specified at the event level only will be considered.

## Track user sessions

> ![info](/docs/images/info.svg)
> 
> The iOS (Obj-C) SDK supports session tracking starting v1.7.0.

By default, iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. automatically tracks the user sessions. This means that RudderStack automatically determines the start and end of a user session depending on the inactivity time configured in the SDK (default time is 5 minutes).

> ![warning](/docs/images/warning.svg)
> 
> To automatically track sessions in the iOS (Obj-C) SDK, `withTrackLifecycleEvents` should also be set to true. This is because RudderStack considers the [Application Opened](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>), [Application Installed](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>), or [Application Updated](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>) events as the start of a new session.
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withAutoSessionTracking:YES];  // Set to No to disable automatic session tracking
    [builder withSessionTimeoutMillis:(5*60*1000)];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withAutoSessionTracking(true)  // Set to false to disable automatic session tracking
                .withSessionTimeoutMillis(5*60*1000)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

To disable automatic session tracking, set `withAutoSessionTracking` to `false`.

> ![info](/docs/images/info.svg)
> 
> For more information on the user sessions and how to track them using the iOS (Obj-C) SDK, see the [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/>) guide.

## Track deep links

Starting from version 1.27.0, iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. supports tracking deep links. Deep links provide direct access to specific content and features within your app. See the [Apple documentation](<https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app#>) for more information on configuring deep links in your iOS app.

After completing the setup, call the SDK’s deep link API from either your `AppDelegate` or `SceneDelegate` depending on the below scenarios:

  * When you only have a URL to pass:


    
    
    [[RSClient sharedInstance] openURL:url];
    
    
    
    RSClient.sharedInstance()?.open(url)
    

  * When you have URL and custom properties to pass along with the deep link event:


    
    
    [[RSClient sharedInstance] openURL:url options:options];
    
    
    
    RSClient.sharedInstance()?.open(url, options: options)
    

The deep link method accepts the below parameters:

Name| Data type| Description  
---|---|---  
`url`  
Required| `NSURL`| Represents a Uniform Resource Locator used to identify a location on the network and a mechanism for retrieving it. URLs are used to open web pages, access APIs, and deep link into specific parts of the app.  
  
For example, `com.ruddertestappswift://`.  
`options`| `NSDictionary`| Additional data properties to send along with the deep link event.  
  
The `Deep Link Opened` event schema is shown below:

Property name| Data type| Description  
---|---|---  
`url`| String| The `url` parameter described above. It is a string of characters used to identify a location on the network and a mechanism for retrieving it.  
  
For example, `com.ruddertestappswift://`.  
  
> ![info](/docs/images/info.svg)
> 
> The iOS (Obj-C) SDK also adds the query parameters as the deep link event properties.

## Callback support for mobile device mode integrations

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * This feature is supported in the iOS (Obj-C) SDK v1.24.0 and later.
>   * Currently, the callback support is only available for the [Braze mobile device mode integration](<https://github.com/rudderlabs/rudder-integration-braze-ios>). It will be implemented for other integrations over time.
> 


iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. supports a `onIntegrationReady` callback functionality that returns the instance of the mobile device mode integration after the destination SDK is initialized.

You can use this feature to obtain the Braze SDK instance and use it for registering to Braze’s [in-app messaging feature](<>).
    
    
    id<RSIntegrationFactory> brazeFactoryInstance = [RudderBrazeFactory instance];
    [[RSClient getInstance] onIntegrationReady:brazeFactoryInstance withCallback:^(NSObject *brazeInstance) {
        if (brazeInstance && [brazeInstance isKindOfClass:[Braze class]]) {
            braze = (Braze *)brazeInstance;
        } else {
            NSLog(@"Error getting Braze instance.");
        }
    }];
    
    
    
    let brazeFactoryInstance = RudderBrazeFactory()
    RSClient.getInstance().onIntegrationReady(brazeFactoryInstance) { brazeInstance in
        if let brazeInstance = brazeInstance as? Braze {
            AppDelegate.braze = brazeInstance
        } else {
            print("Error getting Braze instance.")
        }
    }
    

## Send device model information

Starting from iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. v1.25.0, you can send the `context.device.model` in a more detailed format to your downstream destinations. The SDK sends the device model information in the standard Apple format like `iPhone 13,1` instead of the earlier format `iPhone`. Here, `iPhone 13,1` corresponds to the human-readable format `iPhone 12 Mini`.

While most destinations are able to recognize the standard Apple format, there might some cases where the destination is unable to comprehend it. For such cases, you can use the **Localize Apple Device Model** transformation to convert the standard Apple device model into a human-readable format.

[![Apple device model enrichment](/docs/images/event-stream-sources/apple-device-model-enrichment.webp)](</docs/images/event-stream-sources/apple-device-model-enrichment.webp>)

The transformation code is as follows:
    
    
    import { getLocalizedDeviceModel } from "@rs/localizeAppleDeviceModel/v1";
    
     export function transformEvent(event, metadata) {
     const localizedDeviceModel = getLocalizedDeviceModel(event);
      if(localizedDeviceModel && event?.context?.device?.model) {
        event.context.device.model = localizedDeviceModel;
      }
      return event;
    }
    

See the [Localize Apple Device Model](<https://www.rudderstack.com/docs/transformations/templates/#localize-apple-device-model>) transformation template for more information.

## Develop device mode destination

You can easily develop a [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destination if RudderStack doesn’t support it already. Follow these steps:

  1. Create a `CustomIntegration` class by extending [`RSIntegration`](<https://github.com/rudderlabs/rudder-sdk-ios/blob/master/Sources/Classes/Headers/Public/RSIntegration.h>).


    
    
    #import <Rudder/Rudder.h>
    @interface CustomIntegration : NSObject<RSIntegration>
    
    @property (nonatomic, strong) NSDictionary *config;
    @property (nonatomic, strong) RSClient *client;
    
    - (instancetype)initWithConfig:(NSDictionary *)config withAnalytics:(RSClient *)client;
    
    @end
    
    @implementation CustomIntegration
    
    - (instancetype) initWithConfig:(NSDictionary *)config withAnalytics:(RSClient *)client {
        if (self == [super init]) {
        }
        return self;
    }
    
    - (void) processRuderEvent:(nonnull RSMessage *)message {
        NSString *type = message.type;
        if ([type isEqualToString:@"identify"]) {
    //        Do something
        } else if ([type isEqualToString:@"track"]) {
    //        Do something
        } else if ([type isEqualToString:@"screen"]) {
    //        Do something
        } else {
            [RSLogger logWarn:@"MessageType is not supported"];
        }
    }
    
    - (void) dump:(nonnull RSMessage *)message {
        [self processRuderEvent:message];
    }
    
    - (void) reset {
    }
    
    - (void) flush {
    }
    
    @end
    
    
    
    class CustomIntegration: NSObject, RSIntegration {
        
        let config: [AnyHashable: Any]
        let analytics: RSClient
        
        init(config: [AnyHashable: Any], analytics: RSClient) {
            self.config = config
            self.analytics = analytics
        }
        
        func dump(_ message: RSMessage) {
            processRudderEvent(message)
        }
        
        func processRudderEvent(_ message: RSMessage) {
            let type = message.type
            switch type {
            case "identify":
                //Do something
                break
            case "track":
                //Do something
                break
            case "screen":
                //Do something
                break
            default:
                    RSLogger.logWarn("MessageType is not supported")
            }
        }
        
        func reset() {
            
        }
        
        func flush() {
            
        }
    }
    

  2. Create a `CustomFactory` class by extending [`RSIntegrationFactory`](<https://github.com/rudderlabs/rudder-sdk-ios/blob/master/Sources/Classes/Headers/Public/RSIntegrationFactory.h>):


    
    
    #import <Rudder/Rudder.h>
    
    @interface CustomFactory : NSObject<RSIntegrationFactory>
    
    + (instancetype) instance;
    
    @end
    
    @implementation CustomFactory
    
    + (instancetype)instance {
        static CustomFactory *sharedInstance;
        static dispatch_once_t onceToken;
        dispatch_once(&onceToken, ^{
            sharedInstance = [[self alloc] init];
        });
        return sharedInstance;
    }
    
    - (instancetype)init
    {
        self = [super init];
        return self;
    }
    
    - (nonnull NSString *)key {
        return @"Custom Factory";
    }
    
    - (nonnull id<RSIntegration>)initiate:(NSDictionary *)config client:(nonnull RSClient *)client rudderConfig:(nonnull RSConfig *)rudderConfig {
        return [[CustomIntegration alloc] initWithConfig:config withAnalytics:client];
    }
    @end
    
    
    
    class CustomFactory: RSIntegrationFactory {
        static func instance() -> CustomFactory {
            return CustomFactory()
        }
        
        func key() -> String {
            return "Custom Factory"
        }
        
        func initiate(_ config: [AnyHashable: Any], client: RSClient, rudderConfig: RSConfig) -> RSIntegration {
            return CustomIntegration(config: config, analytics: client)
        }
    }
    

  3. Register `CustomFactory` with the iOS (Obj-C) SDK during its initialization:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withCustomFactory:[CustomFactory instance]];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withCustomFactory(CustomFactory.instance())
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

Some pointers to keep in mind:

  * iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. dumps every event it receives to the `dump()` method of the `CustomFIntegration` class. From here, you can process the event and hand it over to the native SDK of the device mode destination.
  * The SDK also triggers the `reset()` method of the `CustomFactory` class on every `reset()` call made via the SDK. You can use this to handle the destination-specific reset logic.
  * Make sure you do not duplicate the value of `KEY` present inside `CustomFactory`, across multiple `CustomFactory` that you develop.


## Flush events via `flush` API

iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. supports the `flush()` API. RudderStack retrieves all messages present in the database, divides them into individual batches based on the specified queue size, and flushes them to the RudderStack server/backend.

For example, if the `flushQueueSize` is 30 and there are 180 events in the database when the `flush()` API is called, the SDK will retrieve all those events and divide them into batches of 30 messages each, that is, into 6 batches.

If a batch fails for some reason, RudderStack drops the remaining batches to maintain the sequence of the messages. A batch is considered as failed if it isn’t sent to the RudderStack server after 3 retries.

In device mode, the `flush()` API also calls the destination SDK’s `flush()` API (if applicable).

For every `flush()` call made via the iOS (Obj-C) SDK, the `flush()` method of the `CustomFactory` class is also triggered, which can be used to handle the destination-specific reset logic. You can make a `flush` call using the SDK as shown:
    
    
    [[RSClient sharedInstance] flush];
    
    
    
    RSClient.sharedInstance()?.flush()
    

## Debugging

If you run into any issues while using iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. , turn on the `VERBOSE` or `DEBUG` logging to find out what the issue is. To turn on the logging, change your `RudderClient` initialization to the following:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withLoglevel:RudderLogLevelDebug];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
    builder.withDataPlaneUrl(<DATA_PLANE_URL>)
    builder.withLoglevel(RudderLogLevelDebug)
    RSClient.getInstance(<WRITE_KEY>, config: builder.build())
    

## Other SDK integrations

### Chromecast

RudderStack supports integrating iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. with [Google Chromecast](<https://store.google.com/in/product/chromecast?hl=en-GB>).

Follow [these instructions](<https://developers.google.com/cast/docs/ios_sender>) to build your iOS sender app. Then, add the iOS (Obj-C) SDK to it.

See the [Google Cast developer guide](<https://developers.google.com/cast/docs/developers>) for more details.

## tvOS and watchOS

> ![info](/docs/images/info.svg)
> 
> The iOS (Obj-C) SDK supports tvOS tracking in **v1.1.0 and above** and watchOS tracking in **v1.3.1 and above**.

You can integrate iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. with your tvOS and watchOS apps and seamlessly track user events without any additional configuration.

## Privacy manifest

Your apps and third-party SDKs (usually distributed as Swift packages, XCFrameworks, or framework bundles) contain a privacy manifest file named `PrivacyInfo.xcprivacy`. It records the data collected by your app/third-party SDK and the associated [required reason API](<https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api>).

You need to record the reasons in your privacy manifest for each data type your app/SDK collects along with the category of required reasons API that it uses.

See the [Apple developer documentation](<https://developer.apple.com/documentation/bundleresources/privacy_manifest_files#4284009>) for more information on creating a privacy manifest.

> ![info](/docs/images/info.svg)
> 
> Starting Spring 2024, you are required to include an approved reason in your app’s privacy manifest that accurately reflects how your app uses the API.
> 
> This is a mandatory requirement to upload a new app/app update to the App Store Connect. For more information, see this [Apple update](<https://developer.apple.com/news/?id=z6fu1dcu>).

#### Privacy Accessed API Types

`NSPrivacyAccessedAPITypes` is an array of dictionaries describing the API types your app/third-party SDK accesses that have been designated as APIs that require reasons to access.

The RudderStack iOS (Obj-C) SDK only uses the `userDefaults` API to store user and context information and it is declared in the privacy manifest in the [iOS (Obj-C) SDK repository](<https://github.com/rudderlabs/rudder-sdk-ios/tree/develop/Sources/Resources>).

#### Privacy tracking domains

`NSPrivacyTrackingDomains` is an array of strings listing the internet domains that your app/third-party SDK connects to for tracking purposes. If the user has not granted the tracking permissions through the App Tracking Transparency framework, the network requests to these domains fail and you get an error on your app.

If your application utilizes data for tracking users as [outlined by Apple](<https://developer.apple.com/app-store/user-privacy-and-data-use/>), it is important to seek the user’s consent first. Also, make sure to include the following domain in your app’s privacy manifest under the purpose `NSPrivacyTrackingDomains`:

  * `rudderstack.com/`


#### Privacy Nutrition Label Types

`NSPrivacyCollectedDataTypes` is an array of dictionaries that describe the data types your app/third-party SDK collects.

The RudderStack iOS (Obj-C) SDK includes an array of [Privacy Nutrition Label Types](<https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4250555>) for the following automatically-collected fields:

Data| Linked to user| Used for tracking| Collection purpose  
---|---|---|---  
App version| No| No| 

  * **Developer advertising or marketing**
  * **Analytics**

  
App name| No| No| 

  * **Developer advertising or marketing**
  * **Analytics**

  
Crash data| No| No| **App functionality**  
Device ID| No| No| 

  * **Developer advertising or marketing**
  * **Analytics**
  * **Third-party advertising**

  
Product interaction| No| No| **App functionality**  
Other data types| No| No| **App functionality**  
  
See the [Apple developer documentation](<https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4250556>) for more information on the above collection purposes.

## FAQ

#### I’m facing issues building with Carthage on XCode 12. What should I do?

If you’re facing an issue with Carthage and XCode 12, you can follow [this workaround](<https://github.com/Carthage/Carthage/blob/master/Documentation/Xcode12Workaround.md>) suggested by the Carthage team.

#### How do I migrate from v1.0.2?

Update the usage of the following classes as per the table below:

Previous Name| Updated Name  
---|---  
`RudderClient`| `RSClient`  
`RudderConfig`| `RSConfig`  
`RudderConfigBuilder`| `RSConfigBuilder`  
`RudderLogLevelDebug`| `RSLogLevelDebug`  
Other `LogLevel`s follow the same nomenclature.  
  
#### How do I ensure the events tracked just before closing/backgrounding the app are sent immediately and not on the next app launch?

To ensure that the events tracked just before closing/backgrounding the app are sent to RudderStack immediately, you can set `withEnableBackgroundMode` to `YES` while creating the `RSConfigBuilder` object as shown below:

> ![info](/docs/images/info.svg)
> 
> Currently, this feature is available only for `iOS` & `tvOS` platforms.
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withEnableBackgroundMode:YES];
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withEnableBackgroundMode(true)
    RSClient.getInstance(WRITE_KEY, config: builder.build())
    

By doing so, your app requests iOS for some additional background run time to run the app, which in turn allows the SDK to immediately send the events tracked just before the app is closed/backgrounded, instead of waiting till the next app launch.

This SDK feature relies on the background mode capability offered by the iOS platform. There is no set number on the background run time the apps get, as it is completely abstracted by iOS. For more information, refer to [this guide](<https://www.raywenderlich.com/5817-background-modes-tutorial-getting-started#toc-anchor-008>).

#### How can I get the user `traits` after making the `identify` call?

You can get the user traits after making an `identify` call in the following way:
    
    
    NSDictionary *traits = [[[RSClient sharedInstance] context] traits];
    
    
    
    let traits = RSClient.sharedInstance()?.context.traits
    

#### How does the SDK handle different client/server errors?

In case of client-side errors, e.g. if the source write key passed to the SDK is incorrect, RudderStack gives you a **400 Bad Request** response and aborts the operation immediately. For other types of network errors (e.g. Invalid Data Plane URL), the SDK tries to flush the events to RudderStack in an incremental manner (every 1 second, 2 seconds, 3 seconds, and so on).

#### Why is there a larger difference between `timestamp` and `received_at` for iOS events vs. Android events?

This scenario is most likely caused by the default behavior of iOS apps staying open in the background for a shorter period of time after a user closes them.

When a user closes an iOS or Android app, events will still continue to be sent from the queue until the app closes in the background as well. Any events still in the queue will remain there until the user reopens the app. Due to this lag, there are some scenarios where there can be significant differences between `timestamp` (when the event was created) and `received_at` (when RudderStack actually receives the events).

For Android apps, events can be sent from the background after apps close for a longer period of time than iOS apps, therefore, more of the events coming from the Android (Java) SDK have closer `timestamp` and `received_at` times.

#### Does RudderStack integrate with SKAdNetwork?

RudderStack does not integrate with SKAdNetwork. However, SKAdNetwork can be directly integrated into an iOS application alongside RudderStack.

#### Can I disable event tracking until the user gives their consent?

Yes, you can.

RudderStack gives you the ability to disable tracking any user activity until the user gives their consent, by leveraging the `optOut` API. This is required in cases where your app is audience-dependent (e.g. minors) or where you’re using the app to track the user events (e.g. EU users) to meet the data protection and privacy regulations.

The `optOut` API takes `true` / `false` (in case of Swift) or `YES` / `NO` (in case of Objective-C) as a value to enable or disable tracking user activities. So, to disable user tracking, you can use the `optOut` API as shown:
    
    
    [[RSClient sharedInstance] optOut:YES];
    
    
    
    RSClient.sharedInstance()?.optOut(true)
    

the user gives their consent, you can enable user tracking again:
    
    
    [[RSClient sharedInstance] optOut:NO];
    
    
    
    RSClient.sharedInstance()?.optOut(false)
    

For more information on the `optOut` API, refer to the Enabling/Disabling User Tracking via optOut API (GDPR Support) section.

> ![success](/docs/images/tick.svg)
> 
> You only need to call the `optOut` API with the required parameter only once, as the information persists within the device even if you reboot it.

#### Can I apply encryption only on new databases?

Database encryption works on new or existing databases. You can pass the RSDBEncryption object in `RSConfigBuilder` while initializing the iOS (Obj-C) SDK.

See Configuring the RudderStack client for more information on the configuration options.

#### Can I remove encryption from an encrypted database?

Yes, you can. When passing the `RSDBEncryption` object, configure the object with the encryption key and set `enable` to false. It will remove the encryption from the encrypted database.

See Creating an encryption object for more information.

#### How does the iOS (Obj-C) SDK handle events larger than 32KB?

The iOS (Obj-C) SDK drops any events greater than 32KB.

#### How long does the iOS (Obj-C) SDK retain the events in the database? Do the events expire and get removed after a certain period?

The iOS (Obj-C) SDK stores all the events in the database before flushing them to the RudderStack backend. The SDK never deletes events based on the time period, that is, how long the events are in the database.

However, note that the SDK removes the older events once the database threshold (`dbThresholdCount`, 10000 events by default) is reached.

#### Why am I getting a warning in `Points of Interest` instruments?

You may get a warning in your `Points of Interest` instrument if `rudderstack.com/` is not listed in your app’s `NSPrivacyTrackingDomain` key in any privacy manifest. It may be following users across multiple apps and websites to create user profiles for apps that contact this domain.

To resolve this issue, make sure to:

  * Seek user consent, especially if your app utilizes data for tracking users as [outlined by Apple](<https://developer.apple.com/app-store/user-privacy-and-data-use/>).
  * Include the `rudderstack.com/` domain in your app’s privacy manifest under the purpose `NSPrivacyTrackingDomains`.


See Privacy tracking domains for more information.