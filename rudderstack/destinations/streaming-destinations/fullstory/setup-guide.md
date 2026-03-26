# Setup Guide Beta

Send your event data from RudderStack to FullStory.

* * *

  * __5 minute read

  * 


This guide will help you set up FullStory as a destination in RudderStack.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **FullStory**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up FullStory as a destination in RudderStack:

  * **Name** : Specify a unique name to identify the destination in RudderStack.
  * **API Key** : Enter your FullStory API key required to send events to FullStory in **cloud mode**.


> ![warning](/docs/images/warning.svg)
> 
> Make sure your API key has **Admin** or **Architect** permissions to view and delete data.
> 
> See [FullStory documentation](<https://developer.fullstory.com/server/authentication/>) for more information on creating and managing your API keys.

  * **FS Org** : Enter the `fs_org` value from your data capture snippet in your FullStory dashboard. For more information on getting this value, see FAQ.


> ![info](/docs/images/info.svg)
> 
> This field is required for sending events to FullStory in **web device mode**.

### Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Fullstory** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the FullStory native SDK from the `https://edge.fullstory.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the FullStory SDK successfully.

### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in FullStory:

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to FullStory. See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Web SDK settings

The following settings are applicable when sending events to FullStory in web device mode, that is, using their native web SDK:

  * **FullStory Host** : If you have a custom FullStory host, enter the host name to initialize the FullStory SDK with it. The default value is `fullstory.com`.
  * **FS debug mode** : This setting is enabled by default and lets you use the FullStory debugging feature.


### Add mobile device mode integration

Once you add FullStory as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>), follow these steps to add it to your mobile project depending on your integration platform:

  1. Add the following dependencies in your `Podfile`:


    
    
    pod 'FullStory', :http => 'https://ios-releases.fullstory.com/fullstory-1.18.0-xcframework.tar.gz'
    pod 'Rudder-FullStory', :git => 'https://github.com/rudderlabs/rudder-integration-fullstory-ios.git', :tag => 'v1.0.0'
    

  2. Run the `pod install` command.
  3. Add the following imports to your `AppDelegate.m` file:


    
    
    #import <Rudder/Rudder.h>
    #import <RudderFullStoryFactory.h>
    

  4. Initialize your iOS (Obj-C) SDK:


    
    
    RSConfigBuilder *configBuilder = [[RSConfigBuilder alloc] init];
    [configBuilder withDataPlaneUrl:dataPlaneUrl];
    [configBuilder withFactory:[RudderFullStoryFactory instance]];
    RSClient *rudderClient = [RSClient getInstance:writeKey config:[configBuilder build]];
    

To complete the FullStory integration, you need to specify which FullStory organization to record. Follow these steps:

  1. Open your app’s `Info.plist`.
  2. From the menu, choose **Editor** > **Add Item**. Set the key name to `FullStory` and type to `Dictionary`.
  3. Right-click the FullStory row and choose **Add Row**. Set the key name to `OrgId` and type to `String`. For the value, paste your assigned organization ID.


When configured correctly, the `Info.plist` entry should look as follows:

![Final entry](/docs/images/event-stream-destinations/fullstory-devicemode-ios.webp)

For more information, see [FullStory iOS documentation](<https://help.fullstory.com/hc/en-us/articles/360042772333-Getting-Started-with-iOS-Recording>).

  1. Open your `app/build.gradle` (Module: app) file and add the following under the `dependencies` section:


    
    
    implementation 'com.rudderstack.android.sdk:core:1.0.22'
    implementation 'com.rudderstack.android.integration:fullstory:1.0.0'
    implementation 'com.google.code.gson:gson:2.8.6'
    // FullStory
    repositories {
      maven { url "https://maven.fullstory.com" }
    }
    implementation 'com.fullstory:instrumentation-full:1.18.0@aar'
    

  2. Add the FullStory Maven plugin to your build script. To do so, add the following snippet into the `Gradle Scripts` section of your root `build.gradle`:


    
    
    buildscript {
      repositories {
        google()
        jcenter()
        maven { url "https://maven.fullstory.com" }
      }
      dependencies {
        classpath 'com.fullstory:gradle-plugin-local:PLUGIN_VERSION'
        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
      }
    }
    
    allprojects {
        repositories {
            google()
            mavenCentral()
        }
    }
    

  3. Replace `PLUGIN_VERSION` with the correct version of the FullStory Android plugin. You can find the latest release notes [here](<https://help.fullstory.com/hc/en-us/articles/4412766845591>).
  4. To apply the FullStory plugin, add the following snippet into your app-specific `build.gradle` (if your Gradle file adds plugins via plugin ID):


    
    
    plugins {
      id 'com.android.application'
      id 'fullstory'
    }
    fullstory {
      org 'YOUR_ORG_ID_HERE'
    }
    

  5. If your Gradle file applies plugins, use the following snippet instead:


    
    
    apply plugin: 'com.android.application'
    apply plugin: 'fullstory'
    fullstory {
      org 'YOUR_ORG_ID_HERE' // Replace with your organization ID.
    }
    

  6. To apply FullStory to all variants, including those used at debug time, add the following line below `org`:


    
    
    org 'YOUR_ORG_ID_HERE'
    enabledVariants 'all'
    

  7. Add the following permissions, if not present already, to your `AndroidManifest.xml`:


    
    
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    

  8. Initialize the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. in your `Application` class’ `onCreate()` method as shown:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(FullStoryIntegrationFactory.FACTORY)
                .build()
        )
    

For more information, see [FullStory Android documentation](<https://help.fullstory.com/hc/en-us/articles/360040596093-Getting-Started-with-Android-Recording>).

## FAQ

#### How do I obtain **FS ORG** value?

  1. Log in to your [FullStory dashboard](<https://app.fullstory.com/login/>).
  2. Click your **Profile** > **Settings**.
  3. Click **FullStory Setup** to get your data capture snippet and copy the value present under `window['_fs_org']`:

[![Fullstory org](/docs/images/event-stream-destinations/fullstory-org.webp)](</docs/images/event-stream-destinations/fullstory-org.webp>)