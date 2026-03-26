# Multiple Instance Support in Android (Kotlin) and iOS (Swift) SDKs

Set up multiple Analytics instances in your Android (Kotlin) and iOS (Swift) apps by implementing separate configurations for different use cases.

* * *

  * __6 minute read

  * 


This guide explains the multiple instance support available in the Android (Kotlin) and iOS (Swift) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs support **multiple instances** within a single application. You can initialize and use **more than one Analytics instance** , each with its own configuration.

You can use this feature to leverage separate [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) to initialize instances for various use cases, allowing you to track events for different brands, user contexts, or modules - all within the same app.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support initializing multiple SDK instances within the application using the **same write key**. Doing so can lead to unexpected behavior like duplicate event delivery.

## Use cases

This section lists some of the use cases for which initializing multiple instances of the SDK is helpful.

### Multiple data planes

Different instances of the Android (Kotlin) and iOS (Swift) SDKs are helpful when your application needs to send events to **multiple different data planes**. Some examples are listed below:

  * Supporting **multiple brands** within a single app, wherein each brand has its own analytics configuration. For example, a super app that contains dedicated sections for different brands or companies.
  * Allowing **switching between users or organizations** , each requiring separate event tracking.


For such cases, you can instantiate two different instances of the SDK, each with its own write keys, as shown below:
    
    
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    
    // ........
    analyticsInstance1 = Analytics(
        configuration = Configuration(
            writeKey = "<WRITE_KEY_1>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    
    analyticsInstance2 = Analytics( 
        configuration = Configuration(
            writeKey = "<WRITE_KEY_2>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    // ........
    

The corresponding Java snippet is shown below:
    
    
    import com.rudderstack.sdk.kotlin.android.Configuration;
    import com.rudderstack.sdk.kotlin.android.javacompat.ConfigurationBuilder;
    import com.rudderstack.sdk.kotlin.android.javacompat.JavaAnalytics;
    
    // ........
    Configuration configuration1 = new ConfigurationBuilder(application, "<WRITE_KEY_1>", "<DATA_PLANE_URL_1>")
            .build();
    JavaAnalytics javaAnalytics1 = new JavaAnalytics(configuration);
    
    Configuration configuration2 = new ConfigurationBuilder(application, "<WRITE_KEY_2>", "<DATA_PLANE_URL_2>")
            .build();
    JavaAnalytics javaAnalytics2 = new JavaAnalytics(configuration);
    // ........
    
    
    
    import RudderStackAnalytics
    
    // ........
    
    let analyticsInstance1 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_1>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
        
    let analyticsInstance2 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_2>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
    
    // ........
    

The corresponding Objective-C snippet is shown below:
    
    
    @import RudderStackAnalytics;
    
    // ........
    
    RSSAnalytics *analyticsInstance1 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_1>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    RSSAnalytics *analyticsInstance2 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_2>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    // ........
    

### App library using the SDK internally

If your application uses a third-party library or SDK that internally uses the Android (Kotlin) or iOS (Swift) SDK, it may result in multiple instances getting initialized. Even if you send events to a single data plane, your application and the library will each use their own `Analytics` instance. No extra configuration is needed in this case — the SDK handles this safely under the hood.

## Important considerations

This section lists some important considerations when using multiple instances of the SDK.

### Device mode integrations

RudderStack **does not guarantee** compatibility of standard device mode integrations with multiple instances. Some integrations initialize singletons internally, which can lead to unexpected behavior when used across multiple `Analytics` instances.

#### Discouraged use cases

RudderStack **discourages** the use of multiple instances of the same integration in the following cases:

  1. Two different instances of the same integration are being used with two different SDK instances, as shown:


    
    
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    
    // ........
    analyticsInstance1 = Analytics(
        configuration = Configuration(
            writeKey = "<WRITE_KEY_1>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    
    analyticsInstance2 = Analytics( 
        configuration = Configuration(
            writeKey = "<WRITE_KEY_2>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    // ........
    
    val someStandardIntegration1 = ExampleStandardIntegration()
    val someStandardIntegration2 = ExampleStandardIntegration()
    
    analyticsInstance1.add(someStandardIntegration1)
    analyticsInstance2.add(someStandardIntegration2)
    

The corresponding Java snippet is shown below:
    
    
    import com.rudderstack.sdk.kotlin.android.Configuration;
    import com.rudderstack.sdk.kotlin.android.javacompat.ConfigurationBuilder;
    import com.rudderstack.sdk.kotlin.android.javacompat.JavaAnalytics;
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin;
    
    Configuration configuration1 = new ConfigurationBuilder(application, "<WRITE_KEY_1>", "<DATA_PLANE_URL_1>")
            .build();
    JavaAnalytics javaAnalytics1 = new JavaAnalytics(configuration);
    
    Configuration configuration2 = new ConfigurationBuilder(application, "<WRITE_KEY_2>", "<DATA_PLANE_URL_2>")
            .build();
    JavaAnalytics javaAnalytics2 = new JavaAnalytics(configuration);
    
    IntegrationPlugin someStandardIntegration1 = new ExampleStandardIntegration();
    IntegrationPlugin someStandardIntegration2 = new ExampleStandardIntegration();
    
    javaAnalytics1.add(someStandardIntegration1);
    javaAnalytics2.add(someStandardIntegration2);
    
    
    
    import RudderStackAnalytics
    
    // ........
    
    let analyticsInstance1 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_1>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
        
    let analyticsInstance2 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_2>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
    
    // ........
    
    let someStandardIntegration1 = ExampleStandardIntegration()
    let someStandardIntegration2 = ExampleStandardIntegration()
        
    analyticsInstance1.add(plugin: someStandardIntegration1)
    analyticsInstance2.add(plugin: someStandardIntegration2)
    

The corresponding Objective-C snippet is shown below:
    
    
    @import RudderStackAnalytics;
    
    // ........
    
    RSSAnalytics *analyticsInstance1 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_1>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    RSSAnalytics *analyticsInstance2 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_2>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    // ........
    
    ExampleStandardIntegration *someStandardIntegration1 = [[ExampleStandardIntegration alloc] init];
    ExampleStandardIntegration *someStandardIntegration2 = [[ExampleStandardIntegration alloc] init];
        
    [analyticsInstance1 addPlugin:someStandardIntegration1];
    [analyticsInstance2 addPlugin:someStandardIntegration2];
    

  2. Same instance of the integration used with two different SDK instances:


    
    
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    
    // ........
    analyticsInstance1 = Analytics(
        configuration = Configuration(
            writeKey = "<WRITE_KEY_1>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    
    analyticsInstance2 = Analytics( 
        configuration = Configuration(
            writeKey = "<WRITE_KEY_2>",
            application = application, // your application instance
            dataPlaneUrl = "<DATA_PLANE_URL>",
        )
    )
    // ........
    
    val someStandardIntegration = ExampleStandardIntegration()
    
    analyticsInstance1.add(someStandardIntegration)
    analyticsInstance2.add(someStandardIntegration)
    

The corresponding Java snippet is shown below:
    
    
    import com.rudderstack.sdk.kotlin.android.Configuration;
    import com.rudderstack.sdk.kotlin.android.javacompat.ConfigurationBuilder;
    import com.rudderstack.sdk.kotlin.android.javacompat.JavaAnalytics;
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin;
    
    Configuration configuration1 = new ConfigurationBuilder(application, "<WRITE_KEY_1>", "<DATA_PLANE_URL_1>")
            .build();
    JavaAnalytics javaAnalytics1 = new JavaAnalytics(configuration);
    
    Configuration configuration2 = new ConfigurationBuilder(application, "<WRITE_KEY_2>", "<DATA_PLANE_URL_2>")
            .build();
    JavaAnalytics javaAnalytics2 = new JavaAnalytics(configuration);
    
    IntegrationPlugin someStandardIntegration = new ExampleStandardIntegration();
    
    javaAnalytics1.add(someStandardIntegration);
    javaAnalytics2.add(someStandardIntegration);
    
    
    
    import RudderStackAnalytics
    
    // ........
    
    let analyticsInstance1 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_1>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
        
    let analyticsInstance2 = Analytics(
            configuration: Configuration(
                writeKey: "<WRITE_KEY_2>",
                dataPlaneUrl: "<DATA_PLANE_URL>"
            )
        )
    
    // ........
    
    let someStandardIntegration = ExampleStandardIntegration()
    
    analyticsInstance1.add(plugin: someStandardIntegration)
    analyticsInstance2.add(plugin: someStandardIntegration)
    

The corresponding Objective-C snippet is shown below:
    
    
    @import RudderStackAnalytics;
    
    // ........
    
    RSSAnalytics *analyticsInstance1 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_1>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    RSSAnalytics *analyticsInstance2 =
        [[RSSAnalytics alloc] initWithConfiguration:
            [[[RSSConfigurationBuilder alloc]
                initWithWriteKey:@"<WRITE_KEY_2>"
                   dataPlaneUrl:@"<DATA_PLANE_URL>"]
                build]];
    
    // ........
    
    ExampleStandardIntegration *someStandardIntegration = [[ExampleStandardIntegration alloc] init];
        
    [analyticsInstance1 addPlugin:someStandardIntegration];
    [analyticsInstance2 addPlugin:someStandardIntegration];
    

### Custom integrations

You can implement your own custom integration and use it across multiple SDK instances. However, make sure that the integration is implemented in a way that it supports:

  * Being instantiated multiple times safely.
  * Managing its internal state independently per instance.


## Logging behavior with multiple instances

The Android (Kotlin) and iOS (Swift) SDKs use a shared logging utility called `LoggerAnalytics`, which is implemented as a **singleton**. This means all the SDK instances within the same application share the same logger configuration.

Note the following:

  * **Global Effect** : If you set a custom `Logger` or `logLevel` via `LoggerAnalytics`, the changes apply globally to all the `Analytics` instances in the application.
  * **No instance distinction** : Currently, the log messages do not indicate which `Analytics` instance they are coming from — this can make it difficult to trace logs back to a specific instance when multiple SDK instances are active.