# Mobile Application Lifecycle Events Spec

Learn the app lifecyle events tracked out of the box by RudderStack SDKs.

* * *

  * __4 minute read

  * 


RudderStack lets you track various application lifecycle events across the mobile SDKs and get insights into app-related metrics like installs, opens, etc. This guide provides the details and semantic definitions of these events and the associated properties.

> ![info](/docs/images/info.svg)
> 
> To track application lifecycle events in Android apps using the Unity SDK, you need to perform some additional steps — refer to [Tracking application lifecycle events on the Android platform](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-unity-sdk/v1/#tracking-application-lifecycle-events-on-the-android-platform>) for more information.

## Supported lifecycle events

RudderStack **automatically tracks** the following application lifecycle events:

  * Application Installed
  * Application Opened
  * Application Updated
  * Application Backgrounded


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** To disable the auto-tracking of these events, set the `withTrackLifecycleEvents` parameter to `false` while initializing the [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) / [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) SDK.

## Application Installed

The `Application Installed` event is triggered when a user opens an application for the first time after installation.

Note that:

  * RudderStack does not collect this event if you not open the app after installation.
  * This event fires only on a fresh install — if you reinstall the app without uninstalling it first (and the build number increases), RudderStack triggers the Application Updated event instead.
  * If you uninstall the app and then reinstall it, the `Application Installed` event fires again once you open the app.


This event supports the following properties:

Property| Type| Description  
---|---|---  
`version`| String| Application version  
`build`| Number| Application build number  
  
A sample payload for the `Application Installed` event is shown below:
    
    
    {
      "type": "track",
      "event": "Application Installed",
      "properties": {
        "version": "11.1.7",
        "build": 12
      }
    }
    

## Application Opened

The `Application Opened` event is triggered each time a user launches the application.

This event supports the following properties:

Property| Type| Description  
---|---|---  
`from_background`| Boolean| Determines if the app was backgrounded initially  
`version`| String| Application version  
  


> ![info](/docs/images/info.svg)This property is included only on the first `Application Opened` event after app launch. It is omitted when the event fires on subsequent returns from the background.  
  
`url`*| String| Deep linking URL  
`referring_application`*| String| External application that referred the user to the app  
  
Note the following regarding the above properties marked with an asterisk (*):

  * These properties are supported only in the [React Native iOS](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>), [Flutter iOS](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>), and iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .
  * They require the legacy `AppDelegate` architecture and work by default in iOS 12 or iOS 13+ (with `SceneDelegate` disabled, by removing `UIApplicationSceneManifest` from the `Info.plist` file). They are not supported in the iOS 13+ apps using `SceneDelegate`.
  * These properties are not supported in the new [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>), [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>), and Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. .


A sample payload for the `Application Opened` event is shown below:
    
    
    {
      "userId": "1hKOmRA4el9Z",
      "type": "track",
      "event": "Application Opened",
      "properties": {
        "from_background": false,
        "version": "11.1.7"
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> `userId` is present only if the user is logged into the application, that is, an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call was previously made for the user.

## Application Updated

The `Application Updated` event is triggered when a user updates their application.

This event supports the following properties:

Property| Type| Description  
---|---|---  
`previous_version`| String| Application version before update  
`version`| String| Application version after update  
`build`| Number| Application build number after update  
`previous_build`| Number| Application build number before update  
  
A sample payload for the `Application Updated` event is shown below:
    
    
    {
      "userId": "1hKOmRA4el9Z",
      "type": "track",
      "event": "Application Updated",
      "properties": {
        "build": 13,
        "previous_build": 12,
        "previous_version": "11.1.7",
        "version": "12.0.1"
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> For the Unity SDK, you need to perform some [additional steps](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-unity-sdk/v1/#triggering-application-updated-lifecycle-event>) for Android and iOS platforms to trigger the **Application Updated** lifecycle event.

## Application Backgrounded

The `Application Backgrounded` event is triggered when the user backgrounds the application.

A sample payload for the `Application Backgrounded` event is shown below:
    
    
    {
      "userId": "1hKOmRA4el9Z",
      "type": "track",
      "event": "Application Backgrounded"
    }
    

> ![info](/docs/images/info.svg)
> 
> RudderStack does not track any properties for this event.

## FAQ

#### What is the format of application lifecycle events follow the standard timestamps?

The lifecycle events timestamp format is the same as [Common Fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>).

#### Do application lifecycle events include user traits or context objects?

Application lifecycle events include `context` objects. Note that `userId` will only be present if the user is logged into the application, i.e., an [identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call was previously triggered.

#### Does the `Application Installed` event fire only on a fresh install?

Yes, the `Application Installed` event fires only on a fresh install.

If you reinstall the app without uninstalling it first (and the build number increases), RudderStack triggers the Application Updated event instead.

However, if you uninstall the app and then reinstall it, the `Application Installed` event will fire again once you open the app.