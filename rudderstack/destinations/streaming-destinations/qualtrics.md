# Qualtrics

Send your event data from RudderStack to Qualtrics.

* * *

  * __7 minute read

  * 


[Qualtrics](<https://www.qualtrics.com/au/core-xm/survey-software/>) is a popular survey software that lets you create intelligent, real-time user surveys. It lets you get cutting-edge insights into your customers and use them to boost your brand value.

RudderStack lets you configure Qualtrics as a destination to which you can send your event data directly.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift)
  * Refer to it as **Qualtrics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Android (Java)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Qualtrics native SDK from the`http://qualtrics.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Qualtrics SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Qualtrics, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source and select **Qualtrics** from the list of destinations.
  2. Assign a name to the destination and click **Continue**.


### Configuration Settings

To successfully configure Qualtrics as a destination, you will need to configure the following settings:

  * **Project ID:** Enter your Qualtrics Project ID here.
  * **Brand ID:** Enter your Qualtrics Brand ID here.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section below for steps on obtaining your Qualtrics Project ID and Brand ID.

  * **Enable Generic Page Title:** If this field is enabled, RudderStack sends every `page` call with the name `Viewed a Page`.


> ![info](/docs/images/info.svg)
> 
> This field is useful only when using the `page` call.

> ![info](/docs/images/info.svg)
> 
> If this option is disabled, RudderStack will search for the category and name of the `page` call and send the event as `Viewed <category_field> <name_field> Page`. If any of the two fields is absent, RudderStack sends the `page` call as `Viewed <category_field> / <name_field> Page`.

## Adding device mode integration

To add Qualtrics to your iOS project, follow these steps:

  1. In your `Podfile`, add the `Rudder-Qualtrics` extension as shown:


    
    
    pod 'Rudder-Qualtrics'
    

  2. After adding the dependency followed by a `pod install` command, add the following imports to your `AppDelegate.m` file:


    
    
    #import <rudder>
    #import <rudderqualtricsfactory.h>
    @import Qualtrics;
    

  3. Then, add the initialization of your `RSClient` as shown:


    
    
    RSConfigBuilder *configBuilder = [[RSConfigBuilder alloc] init];
        [configBuilder withDataPlaneUrl:DATA_PLANE_URL];
        [configBuilder withFactory:[RudderQualtricsFactory instance]];
        [RSClient getInstance:<source_write_key> config:[configBuilder build]];
    

  4. Next, add the following snippet to display the qualified intercept on your `ViewController`:


    
    
    [Qualtrics.shared evaluateProjectWithCompletion:^(NSDictionary<nsstring>* targetingResults){
        for (NSString* interceptID in targetingResults) {
          TargetingResult *result = targetingResults[interceptID];
              if ([result passed]) {
                [[Qualtrics shared] displayWithViewController:self];
              }
        }
    }];
    

For more information, refer to the [Qualtrics iOS documentation](<https://api.qualtrics.com/2241421657525-getting-started-with-the-mobile-app-sdk-on-i-os>).

> ![info](/docs/images/info.svg)
> 
> Your Android project must be on **version 5.0 (API level 21) or higher** for RudderStack to be able to send events to Qualtrics.

Once confirmed, follow these steps to add Qualtrics to your Android project:

  1. Open your `app/build.gradle` (Module: app) file and add the following under the `dependencies` section :


    
    
    implementation 'com.rudderstack.android.sdk:core:1.+'
    implementation 'com.rudderstack.android.integration:qualtrics:1.0.0'
    implementation 'com.google.code.gson:gson:2.8.6'
    
    // Qualtrics
    implementation 'com.qualtrics:digital:2.0.0'
    

  2. Add a new Maven repository for the App Feedback package. Your `allprojects` section should appear as shown:


    
    
    allprojects {
        repositories {
            google()
            jcenter()
            maven {
                url "https://s3-us-west-2.amazonaws.com/si-mobile-sdks/android/"
            }
        }
    }
    

  3. Open the `AndroidManifest.xml` file from the `src/main` folder in the project root and add the following XML snippet after the existing activity:


    
    
    <activity android:name="com.qualtrics.digital.QualtricsSurveyActivity"></activity>
    <activity android:name="com.qualtrics.digital.QualtricsPopOverActivity" android:theme="@style/Qualtrics.Theme.Transparent"></activity>
    

  4. Initialize the RudderStack SDK in your `Application` class’ `onCreate()` method as shown:


    
    
    // initialize Rudder SDK
    val rudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(QualtricsIntegrationFactory.FACTORY)
                .build()
        )
    

  5. Add a `MyCallback` subclass. You need to implement a callback for the Qualtrics APIs. This will be used to call the `displayIntercept()` method based on the `evaluateIntercept()` result. A good place to add this callback is before the last closing brace (`}`) in your `MainActivity.Java` class. Add the following code:


    
    
    private class MyCallback implements IQualtricsProjectEvaluationCallback {
       @Override
       public void run(Map<string targetingresult=""> targetingResults) {
           for (Map.Entry<string> result: targetingResults.entrySet())
               if (result.getValue().passed()) {
                   Qualtrics.instance().displayIntercept(MainActivity.this, result.getKey());
               }
       }
    }
    

  6. Add the following snippet to display the qualified intercept in your activity class:


    
    
    Qualtrics.instance().evaluateProject(new MyCallback());
    

> ![info](/docs/images/info.svg)
> 
> For more information, refer to the [Qualtrics Android documentation](<https://api.qualtrics.com/2241421657525-getting-started-with-the-mobile-app-sdk-on-i-os>).

> ![info](/docs/images/info.svg)
> 
> In the iOS device mode implementation, even if the user qualifies for multiple intercepts, only one will be shown. Whereas in Android, all intercepts for the user will be shown.

## Page

The `page` call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack passes any tracked events as embedded data to the Qualtrics [intercept](<https://www.qualtrics.com/support/website-app-feedback/getting-started-with-website-app-feedback/step-4-setting-up-your-intercept/>) target. After the `page` call, the Qualtrics survey is loaded.

> ![success](/docs/images/tick.svg)
> 
> You can set the intercepts when a user creates the project or after they have created the project.

A sample `page` call is as shown:
    
    
    rudderanalytics.page("category", "name", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
      testDimension: "true"
    });
    

For the above example, The event will be sent as `Viewed category name Page`, if the **Generic Page Title** option is disabled in the RudderStack dashboard. If this option is enabled, the event will be sent as `Viewed a Page`.

If the category field is not mentioned in the `page` call but specified inside the properties, RudderStack still includes the field while sending the event. For example, refer to the following snippet:
    
    
    rudderanalytics.page("name", {
      category: "category",
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
      testDimension: "true"
    });
    

For the above example, the event will be sent as `Viewed category name Page`, if the **Generic Page Title** option is disabled in the RudderStack dashboard. If it is enabled, the event will be sent as `Viewed a Page`.

If `category` is not specified in the event at all, RudderStack sends the event with only the page name, as shown below:
    
    
    rudderanalytics.page("name", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
      testDimension: "true"
    });
    

For the above example, The event will be sent as `Viewed name Page`, if the **Generic Page Title** option is disabled in the RudderStack dashboard. If enabled, the event will be sent as `Viewed a Page`.

> ![warning](/docs/images/warning.svg)
> 
> If both the name and category fields are absent in the `page` call and the **Generic Page Title** option is disabled, RudderStack will not send the event to Qualtrics.

## Track

The `track` call lets you track how many times a user performs certain actions. RudderStack passes any tracked events as embedded data to the Qualtrics [intercept](<https://www.qualtrics.com/support/website-app-feedback/getting-started-with-website-app-feedback/step-4-setting-up-your-intercept/>) target. After the `track` call, the Qualtrics survey is loaded.

> ![info](/docs/images/info.svg)
> 
> In Qualtrics, both `page` and `track` calls have the same functionality.

> ![success](/docs/images/tick.svg)
> 
> You can set the intercepts either during or after creating the project.

In this case, the value of event field of the `track` call will be used as the event name while sending it to Qualtrics.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Test Event");
    

In the above example, the event will be sent to Qualtrics as `Test Event`.

## Identify

> ![info](/docs/images/info.svg)
> 
> The `identify` call is supported only in the mobile (Android (Java) and iOS (Obj-C)) device mode integration.

When you make an `identify` call, RudderStack sets the user traits using:

  * The Qualtrics `Properties` class, `setString`, and `setNumber` API in case of Android, and
  * The `setStringWithString` and `setNumberWithNumber` API in case of iOS


These user traits can be used as custom properties while setting the [Target Logic](<https://www.qualtrics.com/support/website-app-feedback/common-use-cases/optimizing-intercept-targeting-logic/>) or [Embedded Data](<https://api.qualtrics.com/sdks/ZG9jOjgwNTgzNjE-getting-started-with-mobile-app-sdk-on-android#using-embedded-data>) for any intercept in your Qualtrics dashboard.
    
    
    [[RSClient sharedInstance] identify:@"test_user_id"
            traits: @{ @"property_key": @"property_value" }];
    
    
    
    MainApplication.rudderClient.identify(
        RudderTraits().put("property_key", "property_value")
    )
    

## FAQ

#### How do I get my Qualtrics project ID and brand ID?

  1. Log into your [Qualtrics account](<https://login.qualtrics.com/login?lang=au>).
  2. Click the project you will be using.
  3. Click **Settings** tab, followed by **Manage Project** option (the right-most dropdown menu in the dashboard).

[![Qualtrics IDs](/docs/images/event-stream-destinations/qualtrics-ids.webp)](</docs/images/event-stream-destinations/qualtrics-ids.webp>)

  4. Click **Project IDs**. Here you will find both your Project ID and Brand ID:

[![Qualtrics IDs](/docs/images/event-stream-destinations/qualtrics-ids-2.webp)](</docs/images/event-stream-destinations/qualtrics-ids-2.webp>)

#### How do I know if the RudderStack SDK has loaded successfully?

Once RudderStack loads the web SDK successfully, you will be able to see the survey options chosen in the Qualtrics dashboard, for example, a survey button, survey form, etc.

[![Qualtrics success](/docs/images/event-stream-destinations/qualtrics-success.webp)](</docs/images/event-stream-destinations/qualtrics-success.webp>)

#### Is it possible to manually set the logic in the mobile device mode integration?

Yes, you can manually set the logic using Qualtrics `Properties` class `setString` and `setNumber` API on Android and `setStringWithString` and `setNumberWithNumber` API on iOS. For more information, refer to the [iOS documentation](<https://api.qualtrics.com/2241421657525-getting-started-with-the-mobile-app-sdk-on-i-os>) or the [Android documentation](<https://api.qualtrics.com/sdks/ZG9jOjgwNTgzNjE-getting-started-with-mobile-app-sdk-on-android>), depending on your implementation.