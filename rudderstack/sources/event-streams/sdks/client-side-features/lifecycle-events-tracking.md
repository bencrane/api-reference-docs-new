# Application Lifecycle Tracking in Mobile SDKs

Learn about the application lifecycle events tracking in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __2 minute read

  * 


The RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs automatically track the following lifecycle events when you use the lifecycle tracking feature in your app:

  * `Application Installed`
  * `Application Updated`
  * `Application Opened`
  * `Application Backgrounded`


> ![success](/docs/images/tick.svg)
> 
> With the application lifecycle tracking feature, you can automatically capture user’s app usage behavior and get insights into their behaviour and app engagement patterns.

## Manage lifecycle tracking

Note that the lifecycle tracking feature is enabled in the mobile SDKs by default. To turn it off, set `trackApplicationLifecycleEvents` to `false` / `NO` (in case of Objective-C) in the `Configuration` object during the SDK initialization, as shown:
    
    
    analytics = Analytics(
        configuration = Configuration(
            trackApplicationLifecycleEvents = false,
            writeKey = BuildConfig.WRITE_KEY,
            application = application,
            dataPlaneUrl = BuildConfig.DATA_PLANE_URL,
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    Configuration configuration = new ConfigurationBuilder(this, "WRITE_KEY", "DATA_PLANE_URL")
            .setTrackApplicationLifecycleEvents(true)
            .build();
    
    analytics = new JavaAnalytics(configuration);
    
    
    
    analytics = Analytics(
        configuration: Configuration(
            writeKey: "WRITE_KEY",
            dataPlaneUrl: "DATA_PLANE_URL",
            trackApplicationLifecycleEvents: false
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSConfigurationBuilder *builder = [[RSSConfigurationBuilder alloc] 
    		initWithWriteKey:@"WRITE_KEY"
    		dataPlaneUrl:@"DATA_PLANE_URL"];
    
    [builder setTrackApplicationLifecycleEvents:NO];
    
    analytics = [[RSSAnalytics alloc] initWithConfiguration:[builder build]];
    

## Lifecycle events

This section covers the different application lifecycle events tracked by the SDK.

### Application Installed

The `Application Installed` event is triggered when the user opens the app for the first time after installation.

The SDK also captures the following properties while tracking this event:

Property| Data type| Description  
---|---|---  
`version`| String| App’s version name.  
`build`| Long| App’s build number.  
  
### Application Updated

The `Application Updated` event is triggered when the user opens the app for the first time **after** updating it.

The SDK also captures the following properties while tracking this event:

Property| Data type| Description  
---|---|---  
`version`| String| App’s version name.  
`build`| Long| App’s build number.  
`previous_version`| String| App’s version name before the update.  
`build`| Long| App’s build number before the update.  
  
### Application Opened

The `Application Opened` event is triggered when the user opens the app, either as a fresh launch or from the background.

The SDK also captures the following properties while tracking this event:

Property| Data type| Description  
---|---|---  
`version`| String| App’s current version name.  
  
**Note** : This property is tracked only for a fresh app launch.  
`from_background`| Boolean| Set to `true` if the app was opened from the background, set to `false` otherwise.  
  
### Application Backgrounded

The `Application Backgrounded` event is triggered whenever the app is backgrounded. Note that this event **does not** contain any additional properties.