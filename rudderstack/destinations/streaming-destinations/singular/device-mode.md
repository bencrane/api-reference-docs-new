# Singular Device Mode Integration

Send events from RudderStack to Singular via device mode.

* * *

  * __5 minute read

  * 


RudderStack lets you send your events to Singular via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the mobile SDKs.

## Add device mode integration

After you [set up Singular as a destination in RudderStack](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/setup-guide/>), follow these steps to add it to your project, depending on your platform of integration.

To add Singular to your React Native app, follow these steps:

  1. Add the RudderStack-Singular module to your app by running the following command:


    
    
    npm install @rudderstack/rudder-integration-singular-react-native
    // OR //
    yarn add @rudderstack/rudder-integration-singular-react-native
    

  


  2. Open your project-level `android/build.gradle` file and add the following snippet:


    
    
    repositories {
      maven {
        url "https://maven.singular.net/"
      }
    }
    

  


  3. Import the above module and add it to your SDK initialization:


    
    
    import rudderClient from "@rudderstack/rudder-sdk-react-native"
    import singular from "@rudderstack/rudder-integration-singular-react-native"
    const config = {
    	dataPlaneUrl: <data_plane_url>,
    	trackAppLifecycleEvents: true,
    	withFactories: [singular],
    }
    rudderClient.setup(<write_key>, config)
    

  


To add Singular to your Cordova app, follow these steps:

  1. Navigate to the root folder of your application and run the following command:


    
    
    cordova plugin add rudder-integration-singular-cordova
    

  


  2. Add the following code in the `onDeviceReady()` function of your app’s home page to initialize the SDK:


    
    
    RudderClient.initialize(<write_key>, {
      dataPlaneUrl: <data_plane_url>,
      factories: [RudderSingularFactory]
    })
    

  
Make sure to use the `await` keyword with the `initialize` call.

To add Singular to your iOS app, follow these steps:

  1. In your `Podfile`, add the following dependencies:


    
    
    pod 'Singular-SDK', '11.0.4'
    pod 'Rudder-Singular', '1.0.0'
    

  


  2. After adding the dependencies followed by `pod install` command, add the following imports to your `AppDelegate.m` file:


    
    
    #import <rudder>
    #import <ruddersingularfactory.h>
    

  


  3. Initialize your `RSClient`:


    
    
    RSConfigBuilder *configBuilder = [[RSConfigBuilder alloc] init];
    [configBuilder withDataPlaneUrl:<data_plane_url>];
    [configBuilder withFactory:[RudderSingularFactory instance]];
    RSClient *rudderClient = [RSClient getInstance:<write_key> config:[configBuilder build]];
    

  


> ![info](/docs/images/info.svg)
> 
> For more information, refer to the [Singular iOS documentation](<https://support.singular.net/hc/en-us/articles/12054824479387>).

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Singular v11.0.4 and above.

Follow these steps to add Singular to your iOS project:

  1. Install `RudderSingular` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderSingular', '~> 1.0.0'
    

  


  2. Run the `pod install` command.

  3. Import the SDK depending on your preferred platform:


    
    
    import RudderSingular
    

  

    
    
    @import RudderSingular;
    

  


  4. Add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    let rudderSingularConfig = RudderSingularConfig()
                .skAdNetworkEnabled(true)
                .manualSkanConversionManagement(true)
                .conversionValueUpdatedCallback({ value in
                    print("Your SKAN handler \(value)")
                })
                .waitForTrackingAuthorizationWithTimeoutInterval(0)
    RSClient.sharedInstance().addDestination(RudderSingularDestination(rudderSingularConfig: rudderSingularConfig))
    

  

    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    RudderSingularConfig *rudderSingularConfig = [[RudderSingularConfig alloc] init];
    [rudderSingularConfig skAdNetworkEnabled:YES];
    [rudderSingularConfig manualSkanConversionManagement:YES];
    [rudderSingularConfig conversionValueUpdatedCallback:^(NSInteger value) {
        printf("Your SKAN handler %ld", value);
    }];
    [rudderSingularConfig waitForTrackingAuthorizationWithTimeoutInterval:0];
    [[RSClient sharedInstance] addDestination:[[RudderSingularDestination alloc] initWithRudderSingularConfig:rudderSingularConfig]];
    

To add Singular to your Android app, follow these steps:

1.Open your `app/build.gradle` (Module: `app`) file, and add the following under the `dependencies` section :
    
    
    implementation 'com.rudderstack.android.sdk:core:[1.0,2.0)'
    implementation 'com.rudderstack.android.integration:singular:1.0.0'
    implementation 'com.google.code.gson:gson:2.8.6'
    

  


  2. Add the Singular Maven plugin to your build script. To do this, add the following snippet into the `Gradle Scripts` section of your root `build.gradle`:


    
    
    buildscript {
        repositories {
            google()
            mavenCentral()
            maven {
              url 'https://maven.singular.net/'
            }
        }
        dependencies {
            classpath 'com.android.tools.build:gradle:7.1.2'
            classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:1.6.10'
        }
    }
    allprojects {
        repositories {
            google()
            mavenCentral()
            maven {
              url 'https://maven.singular.net/'
            }
        }
    }
    

  


  3. Add the following permissions(if not present already) to your `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
    

  


  4. Finally, initialize the RudderStack SDK in your `Application` class’ `onCreate()` method:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(SingularIntegrationFactory.FACTORY)
                .build()
        )
    

  


> ![info](/docs/images/info.svg)
> 
> For more information, refer to the [Singular Android documentation](<https://support.singular.net/hc/en-us/articles/360037581952-Android-SDK-Basic-Integration?navigation_side_bar=true>).

## Identify

For device mode integrations, the Singular SDK uses RudderStack’s [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method to map the user ID to their custom user ID. RudderStack uses Singular’s [`setCustomUserId`](<https://support.singular.net/hc/en-us/articles/360037581952-Android-SDK-Basic-Integration#Optional_Setting_the_User_ID>) API to forward the identified user ID to Singular.

A sample `identify` call for both the Android (Java) and iOS (Obj-C) SDKs is shown below:
    
    
    [[RSClient getInstance] identify:@"1hKOmRA4el9Zt1WSfVJIVo4GRlm"];
    
    
    
    RudderClient.getInstance()?.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm")
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture any user actions and the properties associated with them. Each user action is considered to be an event.

### Tracking custom events

A custom `track` call lets you track custom events as they occur in your apps. RudderStack sends these calls to Singular where they are processed as custom post-install events and are made available in the relevant reports.

A sample custom `track` call for both the Android (Java) and iOS SDKs is shown below:
    
    
    [[RSClient getInstance] track:@"Product Reviewed" properties:@{
            @"product_id" : @"345676543",
            @"review_id" : @"123454387"
        }];
    
    
    
    RudderClient.getInstance()
        ?.track(
            "Product Reviewed",
            RudderProperty()
                .putValue("product_id", "345676543")
                .putValue("review_id", "123454387")
        )
    

### Tracking revenue

Singular supports tracking revenue events. It implements revenue tracking whenever an event containing the `revenue` property is sent(including a zero value). Optionally, you can also pass the `currency` field as an [ISO code](<https://www.iso.org/iso-4217-currency-codes.html>).

> ![info](/docs/images/info.svg)
> 
> The default currency is set to `USD`.

A sample `revenue` track call is shown below:
    
    
    [[RSClient getInstance] track:@"Order Completed" properties:@{
            @"revenue" : @1251,
            @"currency" : @"INR"
        }];
    
    
    
    RudderClient.getInstance()
        ?.track(
            "Order Completed",
            RudderProperty().putValue("revenue", 1251).putValue("currency", "INR")
        )
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method allows you to record whenever a user sees the mobile screen, along with any associated optional properties. This call is similar to the `page` call for the web applications but exclusive to your mobile device.

A sample `screen` call for both the Android (Java) and iOS (Obj-C) SDKs is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Home" properties:@{
        @"category" : @"launcher"
    }];
    
    
    
    RudderClient.getInstance()
        ?.screen(
            "Home",
            RudderProperty().putValue("category", "launcher")
        )
    

e above snippet, RudderStack captures all information related to the viewed screen, along with any additional info about the screen.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `screen` event to Singular as a custom event.

## Reset

The `reset` method resets the current user’s identity and creates a new anonymous session. It should be called when a user logs out.

RudderStack calls Singular’s [`unsetCustomUserId`](<https://support.singular.net/hc/en-us/articles/360037581952-Android-SDK-Basic-Integration#Optional_Setting_the_User_ID>) method to reset a user’s identity.

A sample `reset` call for both the Android (Java) and iOS (Obj-C) SDKs is shown below:
    
    
    [[RSClient getInstance] reset];
    
    
    
    RudderClient.getInstance()?.reset();
    

## Implementing SKAdNetwork (SKAN) support

Add the following code before the initialization of the iOS SDK to give the control to Singular for your SKAdNetwork integration:
    
    
    [RudderSingularIntegration setSKANOptions:YES
            isManualSkanConversionManagementMode:YES
    withWaitForTrackingAuthorizationWithTimeoutInterval:@0
            withConversionValueUpdatedHandler:^(NSInteger conversionValue){
        // Receive a callback whenever the Conversion Value is updated
        NSLog(@"SKAN handler %ld",conversionValue);
    }];
    

> ![info](/docs/images/info.svg)
> 
> For more details, refer to the [iOS SDK: Adding SKAdNetwork Support](<https://support.singular.net/hc/en-us/articles/12054824479387#23_Customizing_SKAdNetwork_Options>) section of the Singular documentation.