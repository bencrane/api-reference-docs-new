# How to Create Custom Integrations

Create custom device mode integrations for unsupported destinations in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __9 minute read

  * 


This guide shows you how to create custom integration plugins to send events to third-party destinations that are not officially supported by RudderStack.

## Overview

Custom integrations let you wrap any third-party SDK and send event data directly to destinations that are not officially supported. You can extend RudderStack’s capabilities by integrating any third-party SDK into your mobile apps.

## Key differences from standard integrations

Aspect| Standard integrations| Custom integrations  
---|---|---  
Maintenance| Maintained by RudderStack| Maintained by you  
Configuration| Uses dashboard configuration| Uses hardcoded or custom configuration  
Source configuration| Receives destination configuration from the RudderStack dashboard| Receives an empty configuration object  
Updates| Automatic (via RudderStack releases)| Manual (updates made by the developer)  
  
## Implementation guide

The following example creates an integration plugin called `MyCustomIntegrationPlugin` that wraps a destination called `CustomDestinationSdk`. All APIs are implemented for demonstration purposes. Apart from the mandatory APIs (`key`, `create`, and `getDestinationInstance`), you can implement other APIs as needed.

### Android (Kotlin)

This section shows you how to create a custom integration plugin for Android (Kotlin).

#### 1\. Create the integration plugin
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin
    import com.rudderstack.sdk.kotlin.core.internals.logger.LoggerAnalytics
    import com.rudderstack.sdk.kotlin.core.internals.models.*
    import kotlinx.serialization.json.JsonObject
    
    /**
     * Custom integration plugin for CustomDestination
     */
    class MyCustomIntegrationPlugin : IntegrationPlugin() {
    
        /**
         * The instance of the destination SDK which is wrapped with this integration plugin.
         * Here, `CustomDestinationSdk` is a sample third party SDK class which you can wrap with an integration plugin.
         */
        private var destinationSdk: CustomDestinationSdk? = null
    
        // Unique identifier for your integration
        override val key: String = "CustomDestination"
    
        /**
         * Initialize your destination SDK
         * Note: destinationConfig will be empty for custom integrations
         */
        override fun create(destinationConfig: JsonObject) {
            // Initialize with your custom configuration
            val apiKey = "your-api-key"
            val serverUrl = "https://api.yourdestination.com"
            destinationSdk = CustomDestinationSdk.initialize(apiKey, serverUrl)
            LoggerAnalytics.debug("MyCustomDestination: SDK initialized")
        }
    
        /**
         * Return the destination SDK instance
         */
        override fun getDestinationInstance(): Any? {
            return destinationSdk
        }
    
        /**
         * Implement event methods to forward events to your destination SDK.
         * Call the appropriate methods on your destination SDK instance.
         */
        override fun track(payload: TrackEvent) {
            destinationSdk?.trackEvent(
                eventName = payload.event,
                properties = payload.properties.toMap()
            )
        }
    
        override fun identify(payload: IdentifyEvent) {
            destinationSdk?.identifyUser(
                userId = payload.userId,
                traits = payload.context["traits"]?.jsonObject?.toMap() ?: emptyMap()
            )
        }
    
        override fun screen(payload: ScreenEvent) {
            destinationSdk?.trackScreen(
                screenName = payload.screenName,
                properties = payload.properties.toMap()
            )
        }
    
        override fun group(payload: GroupEvent) {
            destinationSdk?.setGroup(
                groupId = payload.groupId,
                traits = payload.traits.toMap()
            )
        }
    
        override fun alias(payload: AliasEvent) {
            destinationSdk?.aliasUser(
                newUserId = payload.userId,
                previousUserId = payload.previousId
            )
        }
    
        /**
         * Optional: Implement flush method if supported by your destination SDK
         */
        override fun flush() {
            destinationSdk?.flush()
            LoggerAnalytics.debug("MyCustomDestination: Flushed events")
        }
    
        /**
         * Optional: Implement reset method if supported by your destination SDK
         */
        override fun reset() {
            destinationSdk?.reset()
            LoggerAnalytics.debug("MyCustomDestination: Reset user data")
        }
    }
    
    
    
    import androidx.annotation.NonNull;
    import androidx.annotation.Nullable;
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin;
    import com.rudderstack.sdk.kotlin.core.internals.logger.LoggerAnalytics;
    import com.rudderstack.sdk.kotlin.core.internals.models.*;
    
    import java.util.HashMap;
    import java.util.Map;
    
    import kotlinx.serialization.json.JsonObject;
    import kotlinx.serialization.json.JsonElement;
    
    /**
     * Custom integration plugin for CustomDestination
     */
    public class MyCustomIntegrationPlugin extends IntegrationPlugin {
    
        /**
         * The instance of the destination SDK which is wrapped with this integration plugin.
         * Here, `CustomDestinationSdk` is a sample third party SDK class which you can wrap with an integration plugin.
         */
        private CustomDestinationSdk destinationSdk;
    
        // Unique identifier for your integration
        private static final String KEY = "CustomDestination";
    
        @NonNull
        @Override
        public String getKey() {
            return KEY;
        }
    
        /**
         * Initialize your destination SDK
         * Note: destinationConfig will be empty for custom integrations
         */
        @Override
        public void create(@NonNull JsonObject destinationConfig) {
            // Initialize with your custom configuration
            String apiKey = "your-api-key";
            String serverUrl = "https://api.yourdestination.com";
            destinationSdk = CustomDestinationSdk.initialize(apiKey, serverUrl);
            LoggerAnalytics.INSTANCE.debug("MyCustomDestination: SDK initialized");
        }
    
        /**
         * Return the destination SDK instance
         */
        @Nullable
        @Override
        public Object getDestinationInstance() {
            return destinationSdk;
        }
    
        /**
         * Implement event methods to forward events to your destination SDK.
         * Call the appropriate methods on your destination SDK instance.
         */
        @Override
        public void track(@NonNull TrackEvent payload) {
            if (destinationSdk != null) {
                Map<String, Object> properties = convertJsonObjectToMap(payload.getProperties());
                destinationSdk.trackEvent(payload.getEvent(), properties);
            }
        }
    
        @Override
        public void identify(@NonNull IdentifyEvent payload) {
            if (destinationSdk != null) {
                Map<String, Object> traits = new HashMap<>();
                JsonElement traitsElement = payload.getContext().get("traits");
                if (traitsElement != null && traitsElement.isJsonObject()) {
                    traits = convertJsonObjectToMap(traitsElement.getAsJsonObject());
                }
                destinationSdk.identifyUser(payload.getUserId(), traits);
            }
        }
    
        @Override
        public void screen(@NonNull ScreenEvent payload) {
            if (destinationSdk != null) {
                Map<String, Object> properties = convertJsonObjectToMap(payload.getProperties());
                destinationSdk.trackScreen(payload.getScreenName(), properties);
            }
        }
    
        @Override
        public void group(@NonNull GroupEvent payload) {
            if (destinationSdk != null) {
                Map<String, Object> traits = payload.getTraits() != null 
                    ? convertJsonObjectToMap(payload.getTraits()) 
                    : new HashMap<>();
                destinationSdk.setGroup(payload.getGroupId(), traits);
            }
        }
    
        @Override
        public void alias(@NonNull AliasEvent payload) {
            if (destinationSdk != null) {
                destinationSdk.aliasUser(payload.getUserId(), payload.getPreviousId());
            }
        }
    
        /**
         * Optional: Implement flush method if supported by your destination SDK
         */
        @Override
        public void flush() {
            if (destinationSdk != null) {
                destinationSdk.flush();
                LoggerAnalytics.INSTANCE.debug("MyCustomDestination: Flushed events");
            }
        }
    
        /**
         * Optional: Implement reset method if supported by your destination SDK
         */
        @Override
        public void reset() {
            if (destinationSdk != null) {
                destinationSdk.reset();
                LoggerAnalytics.INSTANCE.debug("MyCustomDestination: Reset user data");
            }
        }
    
        /**
         * Utility method to convert JsonObject to Map for Java compatibility
         */
        private Map<String, Object> convertJsonObjectToMap(JsonObject jsonObject) {
            Map<String, Object> map = new HashMap<>();
            // Implementation depends on your JsonObject structure
            // This is a simplified example - you may need more robust conversion
            // You would typically iterate through the JsonObject and convert each element
            return map;
        }
    }
    

#### 2\. Add the plugin to Analytics
    
    
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    
    class MyApp : Application() {
        
        lateinit var analytics: Analytics
        
        override fun onCreate() {
            super.onCreate()
            
            // Initialize Analytics
            analytics = Analytics(
                configuration = Configuration(
                    writeKey = "your-write-key",
                    application = this,
                    dataPlaneUrl = "your-data-plane-url"
                )
            )
            
            // Create and add your custom integration
            val customIntegration = MyCustomIntegrationPlugin()
            
            // Add the integration to analytics
            analytics.add(customIntegration)
        }
    }
    
    
    
    import android.app.Application;
    
    import com.rudderstack.sdk.kotlin.android.Configuration;
    import com.rudderstack.sdk.kotlin.android.javacompat.ConfigurationBuilder;
    import com.rudderstack.sdk.kotlin.android.javacompat.JavaAnalytics;
    
    public class MyApp extends Application {
        
        private JavaAnalytics analytics;
        
        @Override
        public void onCreate() {
            super.onCreate();
            
            // Initialize Analytics
            Configuration config = new ConfigurationBuilder(this, "your-write-key", "your-data-plane-url")
                    .build();
            analytics = new JavaAnalytics(config);
            
            // Create and add your custom integration
            MyCustomIntegrationPlugin customIntegration = new MyCustomIntegrationPlugin();
            
            // Add the integration to analytics
            analytics.add(customIntegration);
        }
    }
    

### iOS (Swift)

This section shows you how to create a custom integration plugin for iOS (Swift).

#### 1\. Create the integration plugin
    
    
    import Foundation
    import RudderStackAnalytics
    
    /**
     * Custom integration plugin for MyCustomDestination
     */
    class MyCustomIntegrationPlugin: IntegrationPlugin {
        var pluginType: PluginType = .terminal
        var analytics: Analytics?
        var key: String = "MyCustomDestination"
        
        /**
         * The instance of the destination SDK which is wrapped with this integration plugin.
         * Here, `CustomDestinationSdk` is a sample third party SDK class which you can wrap with an integration plugin.
         */
        private var destinationSdk: MyCustomDestinationSdk?
        
        func getDestinationInstance() -> Any? {
            return destinationSdk
        }
        
        /**
         * Initialize your destination SDK
         * Note: destinationConfig will be empty for custom integrations
         */
        func create(destinationConfig: [String: Any]) throws {
            // Initialize with your custom configuration
            let apiKey = "your-api-key"
            let serverUrl = "https://api.yourdestination.com"
            destinationSdk = MyCustomDestinationSdk.initialize(apiKey: apiKey, serverUrl: serverUrl)
            print("MyCustomDestination: SDK initialized")
        }
        
        /**
         * Implement event methods to forward events to your destination SDK.
         * Call the appropriate methods on your destination SDK instance.
         */
        func identify(payload: IdentifyEvent) {
            destinationSdk?.identifyUser(
                userId: payload.userId ?? "",
                traits: payload.traits ?? [:]
            )
        }
        
        func track(payload: TrackEvent) {
            destinationSdk?.trackEvent(
                eventName: payload.event ?? "",
                properties: payload.properties ?? [:]
            )
        }
        
        func screen(payload: ScreenEvent) {
            destinationSdk?.trackScreen(
                screenName: payload.name ?? "",
                properties: payload.properties ?? [:]
            )
        }
        
        func group(payload: GroupEvent) {
            destinationSdk?.setGroup(
                groupId: payload.groupId ?? "",
                traits: payload.traits ?? [:]
            )
        }
        
        func alias(payload: AliasEvent) {
            destinationSdk?.aliasUser(
                newUserId: payload.userId ?? "",
                previousUserId: payload.previousId ?? ""
            )
        }
        
        /**
         * Optional: Implement flush method if supported by your destination SDK
         */
        func flush() {
            destinationSdk?.flush()
            print("MyCustomDestination: Flushed events")
        }
        
        /**
         * Optional: Implement reset method if supported by your destination SDK
         */
        func reset() {
            destinationSdk?.reset()
            print("MyCustomDestination: Reset user data")
        }
    }
    
    
    
    #import <Foundation/Foundation.h>
    @import RudderStackAnalytics;
    
    // MyCustomIntegrationPlugin.h
    @interface MyCustomIntegrationPlugin : NSObject<RSSIntegrationPlugin>
    @end
    
    // MyCustomIntegrationPlugin.m
    @interface MyCustomIntegrationPlugin()
    @property SampleDestination *destination;
    @end
    
    @implementation MyCustomIntegrationPlugin
    
    @synthesize pluginType;
    @synthesize key;
    
    - (NSString*)key {
        return @"MyCustomDestination";
    }
    
    - (RSSPluginType)pluginType {
        return RSSPluginTypeTerminal;
    }
    
    /**
     * The instance of the destination SDK which is wrapped with this integration plugin.
     */
    - (id _Nullable)getDestinationInstance { 
        return self.destination;
    }
    
    /**
     * Initialize your destination SDK
     * Note: destinationConfig will be empty for custom integrations
     */
    - (BOOL)createWithDestinationConfig:(NSDictionary<NSString *,id> * _Nonnull)destinationConfig error:(NSError * _Nullable __autoreleasing * _Nullable)error {
        if (_destination == nil) {
            _destination = [SampleDestination createWithApiKey:@"MyCustomDeviceDestination"];
        }
        return YES;
    }
    
    /**
     * Implement event methods to forward events to your destination SDK.
     * Call the appropriate methods on your destination SDK instance.
     */
    - (void)identify:(RSSIdentifyEvent *)payload {
        [_destination identifyUser:payload.userId ?: @"" traits:payload.traits ?: @{}];
    }
         
    - (void)track:(RSSTrackEvent *)payload {
        [_destination trackEvent:payload.eventName properties:payload.properties ?: @{}];
    }
    
    - (void)screen:(RSSScreenEvent *)payload {
        [_destination screen:payload.screenName properties:payload.properties ?: @{}];
    }
    
    - (void)group:(RSSGroupEvent *)payload {
        [_destination group:payload.groupId traits:payload.traits ?: @{}];
    }
    
    - (void)alias:(RSSAliasEvent *)payload {
        [_destination aliasUser:payload.userId ?: @"" previousId:payload.previousId];
    }
    
    /**
     * Optional: Implement flush method if supported by your destination SDK
     */
    - (void)flush {
        [_destination flush];
    }
    
    /**
     * Optional: Implement reset method if supported by your destination SDK
     */
    - (void)reset {
        [_destination reset];
    }
    
    @end
    

#### 2\. Add the plugin to Analytics
    
    
    import UIKit
    import RudderStackAnalytics
    
    class AppDelegate: UIResponder, UIApplicationDelegate {
        
        var analytics: Analytics!
        
        func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
            
            // Initialize Analytics
            let config = Configuration(
                writeKey: "your-write-key",
                dataPlaneUrl: "your-data-plane-url"
            )
            
            analytics = Analytics(configuration: config)
            
            // Create and add your custom integration
            let customIntegration = MyCustomIntegrationPlugin()
            
            // Add the integration to analytics
            analytics.add(plugin: customIntegration)
    
            return true
        }
    }
    
    
    
    #import <UIKit/UIKit.h>
    @import RudderStackAnalytics;
    
    // AppDelegate.m
    @interface AppDelegate ()
    @property RSSAnalytics *analytics;
    @end
    
    @implementation AppDelegate
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
        // Initialize Analytics
        NSString *writeKey = @"your-write-key";
        NSString *dataPlaneUrl = @"your-data-plane-url";
        
        RSSConfigurationBuilder *builder = [[RSSConfigurationBuilder alloc] initWithWriteKey:writeKey dataPlaneUrl:dataPlaneUrl];
        self.analytics = [[RSSAnalytics alloc] initWithConfiguration:[builder build]];
        
        // Create and add your custom integration
        MyCustomIntegrationPlugin *customIntegration = [MyCustomIntegrationPlugin new];
        // Add the integration to analytics
        [self.analytics addPlugin:customIntegration];
        
        return YES;
    }
    
    @end
    

> ![info](/docs/images/info.svg)
> 
> **Important consideration**
> 
> The `pluginType` for a custom integration plugin in iOS (Swift) SDK should always be `.terminal`.

## Required and optional methods

This section lists the required and optional methods for custom integration plugins.

#### Required methods

Method| Description  
---|---  
`key`| Unique identifier for your integration  
`create(destinationConfig)`| Initializes your destination SDK  
`getDestinationInstance()`| Returns the destination SDK instance  
  
#### Optional methods

Method| Description  
---|---  
`track(payload)`| Forwards `track` events to your destination SDK  
`identify(payload)`| Forwards `identify` events to your destination SDK  
`screen(payload)`| Forwards `screen` events to your destination SDK  
`group(payload)`| Forwards `group` events to your destination SDK  
`alias(payload)`| Forwards `alias` events to your destination SDK  
`flush()`| Flushes events to your destination SDK (if supported)  
`reset()`| Resets user data to your destination SDK (if supported)  
  
## Custom integration APIs

Custom integrations support the following [device mode integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>):

  * `onDestinationReady()`: Register a callback for when the destination is ready
  * `getDestinationInstance()`: Access the destination instance directly


## See more

  * [How to Use Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/>): Learn how to add and use standard integrations
  * [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>): Complete API reference for device mode integration APIs