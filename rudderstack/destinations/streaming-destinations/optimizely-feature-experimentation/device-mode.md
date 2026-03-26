# Optimizely Feature Experimentation Device Mode Integration

Send events to Optimizely Feature Experimentation using RudderStack’s device mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send the experimentation data from your mobile apps to Optimizely Feature Experimentation via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

## Prerequisites

Unlike other destinations, Optimizely Feature Experimentation for the mobile integration works a little differently. You will have to implement some Optimizely functions natively to make sure the experiment logic runs correctly.

> ![info](/docs/images/info.svg)
> 
> RudderStack maps the `track` calls with Optimizely’s `track` calls. You need to implement all Optimizely’s decision-based methods like `activate` and `isFeatureEnabled` natively. For more details, refer to Optimizely’s [Easy Event Tracking](<https://blog.optimizely.com/2019/02/26/introducing-easy-event-tracking-the-easier-way-to-understand-and-optimize-the-customer-journey/>) blog and the [Optimizely SDK reference Guide](<https://docs.developers.optimizely.com/full-stack/docs/sdk-reference-guides#section-ios-and-tvos>).

## Adding Optimizely to your mobile project

Follow these steps to add Optimizely Feature Experimentation to your Android Project:

  1. Add the following `repository` to your `app/build.gradle` file.


    
    
    repositories {
        mavenCentral()
    }
    

  2. After that, add the following `dependency` in the same file:


    
    
    implementation 'com.rudderstack.android.integration:optimizely:0.1.1'
    implementation 'com.optimizely.ab:android-sdk:3.0.0'
    

  3. Initialize the Optimizely Manager:


> ![warning](/docs/images/warning.svg)
> 
> Optimizely recommends initializing their SDK as soon as possible. You need to initialize the Optimizely Manager before proceeding to the next step. Refer to the Optimizely [Initializing the SDK](<https://docs.developers.optimizely.com/full-stack/docs/initialize-sdk-android>) guide for more information.
    
    
    val optimizelyManager =  OptimizelyManager.builder()
                .withSDKKey(<YOUR OPTIMIZELY SDK KEY>)
                .build(this)
    

  4. Finally, change the initialization of your `RudderClient` in your `Application` class:


    
    
    val rudderClient = RudderClient.getInstance(
        this,
        <YOUT_WRITE_KEY>,
        RudderConfig.Builder()
            .withEndPointUri(<YOUR_DATA_PLANE_URL>)
            .withFactory(OptimizelyIntegrationFactory.FACTORY(optimizelyManager)
            .build()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure you pass the Optimizely manager instance you created in the previous step to the factory as shown in the above snippet above.

Follow these steps to add Optimizely Feature Experimentation to your iOS project:

  1. Go your `Podfile` and add the `Rudder-Optimizely` extension:


    
    
    pod 'Rudder-Optimizely'
    

  2. After adding the dependency followed by `pod install`, you can add the imports to your `AppDelegate.m` file as shown:


    
    
    #import "RudderOptimizelyFactory.h"
    

  3. Finally, change the initialization of your `RudderClient` as shown:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    // Setup optimizely logger.
    OPTLYLoggerDefault *optlyLogger = [[OPTLYLoggerDefault alloc] initWithLogLevel:OptimizelyLogLevelAll];
    // Create an Optimizely manager
     self.optlyManager = [[OPTLYManager alloc] initWithBuilder:[OPTLYManagerBuilder  builderWithBlock:^(OPTLYManagerBuilder * _Nullable builder) {
            builder.sdkKey = @<SDK KEY>;
            builder.logger = optlyLogger;
     }]];
    [builder withFactory:[RudderOptimizelyFactory instanceWithOptimizely:self.optlyManager]];
    [builder withLoglevel:RSLogLevelDebug];
    [RSClient getInstance:WRITE_KEY config:[builder build]];