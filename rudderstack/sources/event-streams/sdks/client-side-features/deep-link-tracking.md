# Deep Link Tracking in Mobile SDKs

Learn about the deep link tracking feature available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide walks you through the deep link tracking feature available in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

Deep links are URLs that navigate users directly to specific content within your app, bypassing the home screen. The RudderStack mobile SDKs support tracking deep link opens, allowing you to:

  * Capture which deep links bring users into your app
  * Track query parameters for attribution and analytics
  * Understand user acquisition sources and campaign performance


> ![info](/docs/images/info.svg)
> 
> The Android (Kotlin) SDK provides automatic deep link tracking, while the iOS (Swift) SDK requires manual API calls to track deep links.

## Event structure

When a deep link is tracked, the SDK sends a `track` event with the event name `Deep Link Opened`. The event properties include:

Property| Type| Description  
---|---|---  
`url`| String| The complete URL string  
Query parameters| String| Each query parameter is extracted and added as a separate property  
  
For example, the SDK sends the below event for the deep link `https://test.com/_app?id=123&ref=campaign`:
    
    
    {
      "event": "Deep Link Opened",
      "properties": {
        "url": "https://test.com/_app?id=123&ref=campaign",
        "id": "123",
        "ref": "campaign"
      }
    }
    

## iOS (Swift)

The RudderStack iOS (Swift) SDK provides a manual API to track when users open your app via deep links. You can use the `open(url:options:)` method to track deep link events:
    
    
    analytics.open(url: url, options: ["source": "email_campaign"])
    
    // Without options
    analytics.open(url: url)
    
    
    
    [analytics openURL:url options:@{@"source": @"email_campaign"}];
    
    // Without options
    [analytics openURL:url];
    

### Custom properties

The iOS (Swift) SDK supports custom options that are merged into the event properties. Any additional options you pass to the `open(url:options:)` method are included in the event payload.

### Universal links

For universal links, implement the appropriate delegate method in your app:
    
    
    func scene(_ scene: UIScene, continue userActivity: NSUserActivity) {
        guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
              let url = userActivity.webpageURL else { return }
    
        analytics.open(url: url, options: ["type": "universal_link"])
    }
    
    
    
    func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
        guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
              let url = userActivity.webpageURL else { return false }
    
        analytics.open(url: url, options: ["type": "universal_link"])
        return true
    }
    

## Android (Kotlin)

The RudderStack Android (Kotlin) SDK provides automatic deep link tracking, meaning it automatically tracks deep link events when your app is opened via a deep link, without requiring manual API calls.

> ![info](/docs/images/info.svg)
> 
> Deep link tracking is enabled by default in the Android (Kotlin) SDK.

### Manage automatic deep link tracking

To enable or disable automatic deep link tracking, set the `trackDeepLinks` parameter in the `Configuration` object during SDK initialization:
    
    
    val configuration = Configuration(
        application = application,
        writeKey = "YOUR_WRITE_KEY",
        dataPlaneUrl = "YOUR_DATA_PLANE_URL",
        trackDeepLinks = false  // Set to true to enable automatic deep link tracking
    )
    val analytics = Analytics(configuration)
    
    
    
    Configuration configuration = new ConfigurationBuilder(application, "YOUR_WRITE_KEY")
        .dataPlaneUrl("YOUR_DATA_PLANE_URL")
        .trackDeepLinks(false)  // Set to true to enable automatic deep link tracking
        .build();
    Analytics analytics = new Analytics(configuration);
    

### Additional properties

The Android SDK captures additional referrer information:

Property| Type| Description  
---|---|---  
`referring_application`| String| The URI of the app that opened the deep link (if available)  
  
A sample event payload with referrer information is shown below:
    
    
    {
      "event": "Deep Link Opened",
      "properties": {
        "url": "https://test.com/_app?id=123&ref=campaign",
        "referring_application": "android-app://com.example.referringapp",
        "id": "123",
        "ref": "campaign"
      }
    }
    

### Trigger deep links with referrer

To open a deep link from another Android app with proper referrer attribution:
    
    
    val url = "https://test.com/_app?id=123&ref=campaign"
    val intent = Intent(Intent.ACTION_VIEW).apply {
        data = Uri.parse(url)
        putExtra(Intent.EXTRA_REFERRER, Uri.parse("android-app://${context.packageName}"))
    }
    context.startActivity(intent)
    
    
    
    String url = "https://test.com/_app?id=123&ref=campaign";
    Intent intent = new Intent(Intent.ACTION_VIEW);
    intent.setData(Uri.parse(url));
    intent.putExtra(Intent.EXTRA_REFERRER, Uri.parse("android-app://" + context.getPackageName()));
    context.startActivity(intent);
    

## FAQ

#### Do the mobile SDKs support deferred deep linking?

No — deferred deep linking is not supported in either the iOS (Swift) or Android (Kotlin) SDKs.

Deferred deep linking requires a backend service to capture and store the deep link URL when a user clicks it (before the app is installed), then match and deliver that data after installation. This server-side infrastructure is beyond the scope of a client-side SDK.