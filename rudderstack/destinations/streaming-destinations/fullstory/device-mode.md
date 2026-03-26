# FullStory Device Mode Integration Beta

Send events to FullStory using RudderStack device mode.

* * *

  * __4 minute read

  * 


This guide will help you send events to FullStory in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using their native web/mobile SDK.

> ![warning](/docs/images/warning.svg)
> 
> Before sending events, follow the instructions in the [Setup guide](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fullstory/setup-guide/>) to set up the FullStory device mode integration depending on your platform.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method to uniquely identify a user in FullStory.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      displayName: "Alex",
      email: "alex@example.com",
      country: "US",
    });
    

RudderStack translates the above call to FullStory’s `identify` call as follows:

  * Sends `userId` as `uid`.
  * Passes the remaining traits as is.


> ![info](/docs/images/info.svg)
> 
> In web device mode, RudderStack sends the `anonymousId` of the user as `uid` if you do not provide the `userId`.

`displayName` and `email` are **optional** traits and FullStory handles them differently. Once specified in the `identify` call, they show up automatically the next time you browse your user list in FullStory.

See [FullStory documentation](<https://help.fullstory.com/hc/en-us/articles/360020828113#displayname>) for more information.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you track custom events as they occur in your web application.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      orderId: "1234567",
      price: "567",
      currency: "USD",
    });
    

RudderStack passes a `track` call with all its associated event properties to FullStory via its [FS.event](<https://help.fullstory.com/hc/en-us/articles/360020623274-FS-event-API-Sending-custom-event-data-into-FullStory>) method.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views, with any additional relevant information about the viewed page. By default, RudderStack sends all `page` calls to FullStory as events.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("homepage");
    

The above call sends a `Viewed a Page` event to FullStory along with the following properties:

  * `name` (`homepage` in the above example)
  * `path`
  * `referrer`
  * `search`
  * `title`
  * `url`


RudderStack also passes any additional properties in the `page` call to FullStory.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It lets you record the screen views on your mobile app along with other relevant information about the screen.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `screen` call to FullStory as a custom event.

A sample `screen` call is shown below:
    
    
    MainApplication.rudderClient.screen(
        "Sample Screen Name",
        RudderProperty().putValue("prop_key", "prop_value")
    )
    

In the above snippet, RudderStack captures all the information related to the viewed screen, along with any additional info associated with that event. In FullStory, the above `screen` call is shown as `Screen Viewed`, along with the associated properties.

## Reset

The `reset` method resets the previously identified user and any related information. See [FullStory Reset API](<https://developer.fullstory.com/anonymize?lang=ObjectiveC>) for more information.

A sample `reset` call for iOS is shown below:
    
    
    [[RSClient sharedInstance] reset];
    

A sample `reset` call for Android is shown below:
    
    
    MainApplication.rudderClient.reset()
    

## FAQ

#### **How do I prevent FullStory from automatically recording on startup?**

By default, FullStory automatically requests a session and starts recording on the app’s startup.

To start recording the app only when certain conditions are met, you can use FullStory’s `RecordOnStart` feature. Configuring FullStory to disable `RecordOnStart` prevents any recording until you explicitly invoke `FS.restart`.

Follow these steps:

**For iOS**

In your iOS app’s `Info.plist` FullStory dictionary, add a `RecordOnStart` key of type `Boolean` with a value of `NO`.

See [FullStory iOS documentation](<https://help.fullstory.com/hc/en-us/articles/360042772333-Getting-Started-with-iOS-Recording#01ER0FEDVJS9RJ843477QPRYS6>) for more information.

**For Android**

Go to your FullStory plugin configuration (where you set the organiation ID) and set the following:
    
    
    fullstory {
    org 'YOUR_ORG_ID_HERE'
    recordOnStart false
    }
    

See [FullStory Android documentation](<https://help.fullstory.com/hc/en-us/articles/360040596093-Getting-Started-with-Android-Recording#01F5E7XY5HJYV5ZWCCSYNQ8TXC>) for more information.

#### **How do I subclass from an application in Android?**

FullStory requires that you enable MultiDex. If your minSdkVersion is set to 21 or higher, Multidex is enabled by default. In this case, you will need to extend `android.app.Application`, otherwise there will be a build error. If your minSdkVersion is lower than 21, you will need to subclass from `androidx.multidex.MultiDexApplication` instead.

If you’re using Java and if you do not have an application class, you will need to create one. In your `App.java`, add the following:
    
    
    import android.app.Application;
    public class App extends Application {
    ...
    }
    

If you’re using Kotlin and if you do not have an application class, you will need to create one and add the following in your `App.kt`:
    
    
    import android.app.Application
    
    class App: Application() {
    ...
    }
    

Then, set `android:name="App"` in your `AndroidManifest.xml` under the `<application>` tag as shown:
    
    
    <application
    android:name="App" ….
    

#### **Build was configured to prefer settings repositories over project repositories but repository ‘Google’ was added by build file ‘build.gradle’. What do I do?**

Go to your `settings.gradle` file located in the root, and then comment or remove this line: `repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)` as shown in the following snippet:
    
    
    dependencyResolutionManagement {
        // repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            jcenter() // Warning: this repository is going to shut down soon
        }
    }
    rootProject.name = "FullStory_Sample_App"
    include ':app'
    

For more information, see [FullStory documentation](<https://help.fullstory.com/hc/en-us/articles/360040596093-Getting-Started-with-Android-Recording#01F5E7X1NYJY51ME0PEWSM0KBJ>).