# Bugsnag

Send your app event data from RudderStack to Bugsnag.

* * *

  * __4 minute read

  * 


[Bugsnag](<https://www.bugsnag.com/>) provides error reporting libraries for [major software platforms](<https://docs.bugsnag.com/platforms/>) which automatically detect and report errors in your applications, and capture diagnostic data required to help you reproduce and fix each error.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web
  * Refer to it as **Bugsnag** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Bugsnag native SDK from the `https://d2wy8f7a9ursnm.cloudfront.net/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Bugsnag SDK successfully.

## Get started

Once you have confirmed that the platform supports sending events to Bugsnag, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Bugsnag**.
  2. Assign a name to the destination and click **Next**.


### Connection settings

To successfully set up Bugsnag as a destination, you will need to configure the following settings:

  * **Bugsnag API Key** : Enter your BugSnag API key. You can find the API key in your Bugsnag dashboard under **Settings** > **Project Settings**.
  * **Use device-mode to send events** : As this is a device mode-only destination, this setting is turned on by default and cannot be toggled off.
  * **Release Stage** : Use this setting to specify the release stage of your app:
    * Toggle it on for `Development` stage.
    * Keep it toggled off for `Production` stage.
  * **SSL** : This option is turned on by default and causes RudderStack to use SSL while sending data to Bugsnag.


## Adding Bugsnag to mobile project

Once you add Bugsnag as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>), follow these steps to add it to your mobile project depending on your integration platform:

Follow these steps to add Bugsnag to your Android Project:

  1. Add the following `repository` to your `app/build.gradle` file.


    
    
    repositories {
        mavenCentral()
    }
    

  2. Add the following `dependencies` in the same file:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.0.1-beta.1'
    implementation 'com.rudderstack.android.integration:bugsnag:0.1.0-beta.1'
    

  3. Change the initialization of your `RudderClient` in your `Application` class:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(BugsnagIntegrationFactory.FACTORY)
                .build()
        )
    

Follow these steps to add Bugsnag to your iOS project:

  1. Go to `Podfile` and add the `Rudder-Bugsnag` extension:


    
    
    pod 'Rudder-Bugsnag', '0.1.0-beta.1'
    

  2. After adding the dependency followed by `pod install` , you can add the imports to your `AppDelegate.m` file as shown:


    
    
    #import "RudderBugsnagFactory.h"
    

  3. Change the initialization of your `RudderClient` as shown:


    
    
    RudderConfigBuilder *builder = [[RudderConfigBuilder alloc] init];
    [builder withDataPlaneUrl:<your_data_plane_url>];
    [builder withFactory:[RudderBugsnagFactory instance]];
    [RudderClient getInstance:<your_write_key> config:[builder build]];
    

> ![warning](/docs/images/warning.svg)
> 
> This device mode integration is supported for Bugsnag v6.16.4 and above.

Follow these steps to add Bugsnag to your iOS project:

  1. Install `RudderBugsnag` (available through [CocoaPods](<https://cocoapods.org>)) by adding the following line to your `Podfile`:


    
    
    pod 'RudderBugsnag', '~> 1.0.0'
    

  2. Run the `pod install` command.
  3. Import the SDK depending on your preferred platform:


    
    
    import RudderBugsnag
    
    
    
    @import RudderBugsnag;
    

  4. Add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method:


    
    
    let config: RSConfig = RSConfig(writeKey: WRITE_KEY)
                .dataPlaneURL(DATA_PLANE_URL)
    
    RSClient.sharedInstance().configure(with: config)
    RSClient.sharedInstance().addDestination(RudderBugsnagDestination())
    
    
    
    RSConfig *config = [[RSConfig alloc] initWithWriteKey:WRITE_KEY];
    [config dataPlaneURL:DATA_PLANE_URL];
    
    [[RSClient sharedInstance] configureWith:config];
    [[RSClient sharedInstance] addDestination:[[RudderBugsnagDestination alloc] init]];
    

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    });
    

Bugsnag will show the `userId` and `traits` in the **Users** tab of each error.

## Error reporting

Along with user-specific information, you can also use Bugsnag to track handled exceptions data to your dashboard using Bugsnag’s native methods. See the [Bugsnag documentation](<https://docs.bugsnag.com/platforms/browsers/#reporting-handled-exceptions>) for more information on these functions.

## FAQ

#### **Where can I find the Bugsnag API Key?**

  1. Log in to your [Bugsnag dashboard](<https://app.bugsnag.com/>).
  2. Click **Settings** at the top right corner.
  3. Click **Project Settings** to find the API key as shown:

[![](/docs/images/event-stream-destinations/bugsnag-api-key.webp)](</docs/images/event-stream-destinations/bugsnag-api-key.webp>)

#### **What is meant by release stage?**

You can distinguish errors that happen in different stages of your app’s release process, for example, `production`, `development`, etc.

#### **Do I need to use SSL to send the event data to Bugsnag?**

RudderStack recommends using SSL to send data to Bugsnag in web device mode.