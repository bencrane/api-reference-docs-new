# How to Use Device Mode Integrations

Add and use device mode integrations in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __9 minute read

  * 


This guide shows you how to add device mode integrations in your Android (Kotlin) and iOS (Swift) apps to send events directly to third-party destinations. It covers how to:

  * Add standard device mode integrations using the integration APIs
  * Add custom plugins to integrations


## Add a standard device mode integration

To add a standard integration, instantiate the integration plugin and add it to your `Analytics` instance.

### Android (Kotlin)
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration
    
    // Get reference to your integration plugin
    val integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    
    // Add integration plugin to your analytics instance
    analytics.add(integrationPlugin)
    
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin;
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration;
    
    // Get reference to your integration plugin
    IntegrationPlugin integrationPlugin = new FirebaseIntegration();
    
    // Add integration plugin to your analytics instance
    analytics.add(integrationPlugin);
    

### iOS (Swift)
    
    
    import RudderStackAnalytics
    import RudderIntegrationFirebase
    
    // Get reference to your integration plugin
    let integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    
    // Add integration plugin to your analytics instance
    analytics.add(integrationPlugin)
    
    
    
    @import RudderStackAnalytics;
    @import RudderIntegrationFirebase;
    
    // Get reference to your integration plugin
    RSSFirebaseIntegration *integration = [RSSFirebaseIntegration new];
    
    // Add integration plugin to your analytics instance
    [self.analytics addPlugin: integration];
    

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Always add the `integrationPlugin` to the `Analytics` instance before invoking any APIs on the `integrationPlugin`. Calling them earlier may lead to unexpected behavior.

## Access destination instances

Device mode integrations provide the following APIs to interact with destination instances:

  * `onDestinationReady()`: Register a callback for destination initialization
  * `getDestinationInstance()`: Access the destination instance directly


See the [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>) guide for the complete API specification.

### `onDestinationReady()`

`onDestinationReady()` lets you perform actions only after the destination is successfully initialized. This is useful for fetching IDs or initializing resources that depend on the destination being ready.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use the `onDestinationReady()` API for critical startup logic that requires the destination to be ready before proceeding.

#### Android (Kotlin)
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin
    import com.rudderstack.sdk.kotlin.core.internals.utils.Result
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration
    
    val integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    analytics.add(integrationPlugin)
    
    integrationPlugin.onDestinationReady { instance, result ->
        if (result is Result.Success) {
            // Destination is ready
            println("Destination is ready: $instance")
        } else {
            // Handle initialization failure
            println("Destination initialization failed: ${(result as Result.Failure).exception.message}")
        }
    }
    
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin;
    import com.rudderstack.sdk.kotlin.core.internals.utils.Result;
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration;
    
    IntegrationPlugin integrationPlugin = new FirebaseIntegration();
    analytics.add(integrationPlugin);
    
    integrationPlugin.onDestinationReady((instance, result) -> {
        if (result instanceof Result.Success) {
            // Destination is ready
            System.out.println("Destination is ready: " + instance);
        } else if (result instanceof Result.Failure) {
            // Handle initialization failure
            Exception exception = ((Result.Failure) result).getException();
            System.out.println("Destination initialization failed: " + exception.getMessage());
        }
    });
    

#### iOS (Swift)
    
    
    import RudderStackAnalytics
    import RudderIntegrationFirebase
    
    let integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    analytics.add(integrationPlugin)
    
    integrationPlugin.onDestinationReady { instance, result in
        switch result {
        case .success:
            // Destination is ready, safe to send events
            print("Destination is ready: \(String(describing: instance))")
        case .failure(let error):
            // Handle initialization failure
            print("Destination initialization failed: \(error.localizedDescription)")
        }
    }
    
    
    
    @import RudderStackAnalytics;
    @import RudderIntegrationFirebase;
    
    RSSFirebaseIntegration *integration = [RSSFirebaseIntegration new];
    [self.analytics addPlugin: integration];
    
    [self.analytics onDestinationReadyForKey:integration.key :^(id _Nullable destination, NSError * _Nullable error) {
        if (error == nil) {
            // Destination is ready, safe to send events
            [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination is ready: %@", destination]];
        } else {
            // Handle initialization failure
            [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination initialization failed: %@", [error localizedDescription]]];
        }
    }];
    

#### Example: Fetch Firebase app instance ID
    
    
    import com.google.firebase.analytics.FirebaseAnalytics
    
    integrationPlugin.onDestinationReady { instance, result ->
        if (result is Result.Success && instance is FirebaseAnalytics) {
            instance.appInstanceId.addOnSuccessListener { appInstanceId ->
                appInstanceId?.let {
                    // Send to your backend for analytics correlation
                    sendToBackend(it)
                }
            }
        }
    }
    
    
    
    import FirebaseAnalytics
    
    integrationPlugin.onDestinationReady { instance, result in
        switch result {
        case .success:
            if let firebaseAnalytics = instance as? Analytics {
                firebaseAnalytics.appInstanceID { appInstanceID in
                    if let appInstanceID = appInstanceID {
                        // Send to your backend for analytics correlation
                        sendToBackend(appInstanceID)
                    }
                }
            }
        case .failure(_):
            break
        }
    }
    

### `getDestinationInstance()`

`getDestinationInstance()` lets you directly access the destination SDK instance for advanced use cases like interacting with destination-specific APIs or features.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use the `getDestinationInstance()` API for on-demand access later in the app lifecycle when you need to interact with the destination instance immediately.

#### Android (Kotlin)
    
    
    val destination = integrationPlugin.getDestinationInstance()
    if (destination != null) {
        // Interact with the destination SDK
        println("Destination instance: $destination")
        // Cast to specific destination type if needed
        // val firebaseDestination = destination as? FirebaseAnalytics
    }
    
    
    
    Object destination = integrationPlugin.getDestinationInstance();
    if (destination != null) {
        // Interact with the destination SDK
        System.out.println("Destination instance: " + destination);
        // Cast to specific destination type if needed
        // FirebaseAnalytics firebaseDestination = (FirebaseAnalytics) destination;
    }
    

#### iOS (Swift)
    
    
    if let destination = integrationPlugin.getDestinationInstance() {
        // Interact with the destination SDK
        print("Destination instance: \(destination)")
        // Cast to specific destination type if needed
        // let firebaseDestination = destination as? Analytics
    }
    
    
    
    id destination = [integration getDestinationInstance];
    if (destination != nil) {
        // Interact with the destination SDK
        [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination instance: %@", destination]];
        // Cast to specific destination type if needed
        // Analytics *firebaseDestination = [integration getDestinationInstance];
    }
    

#### Example 1: Set default event parameters for Firebase
    
    
    import android.os.Bundle
    import com.google.firebase.analytics.FirebaseAnalytics
    
    val firebaseAnalytics = firebaseIntegration.getDestinationInstance() as? FirebaseAnalytics
    
    firebaseAnalytics?.let {
        val parameters = Bundle().apply {
            putString("app_variant", "premium")
            putString("global_source", "mobile_app")
        }
        // This ensures these parameters are included in every subsequent Firebase event
        it.setDefaultEventParameters(parameters)
    }
    
    
    
    import FirebaseAnalytics
    
    if let firebaseAnalytics = firebaseIntegration.getDestinationInstance() as? Analytics {
        // Set the global parameters
        let parameters: [String: Any] = [
            "app_variant": "premium",
            "global_source": "mobile_app"
        ]
        
        // This ensures these parameters are included in every subsequent Firebase event
        Analytics.setDefaultEventParameters(parameters)
    }
    

#### Example 2: Use Braze content cards
    
    
    import com.braze.Braze
    
    val braze = brazeIntegration.getDestinationInstance() as? Braze
    
    braze?.let {
        // Manually request a refresh of Content Cards
        it.requestContentCardsRefresh()
        
        // Access current content cards for custom UI rendering
        val unreadCount = it.getContentCardCount()
        println("User has $unreadCount unread Content Cards.")
    } ?: run {
        println("Braze integration is not yet ready or is disabled.")
    }
    
    
    
    import RudderIntegrationBraze
    import BrazeKit
    
    if let braze = brazeIntegration.getDestinationInstance() as? Braze {
        // Manually request a refresh of Content Cards
        braze.contentCards.requestRefresh()
        
        // Access current content cards for custom UI rendering
        let unreadCount = braze.contentCards.cards.filter { !$0.viewed }.count
        print("User has \(unreadCount) unread Content Cards.")
    } else {
        print("Braze integration is not yet ready or is disabled.")
    }
    

## Add custom plugins to integrations

Device mode integrations support adding custom plugins to modify or enhance event data before sending it to a specific destination. This enables filtering, transformation, or enrichment of events for specific destinations.

With this feature, you can:

  * Add different plugins to different device mode integrations (for example, Firebase, Amplitude, Braze)
  * Apply unique transformations, filtering, or enrichment logic for each destination
  * Handle destination-specific requirements without affecting other integrations


See the [Plugin Architecture](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) guide for more information on custom plugins.

### Android (Kotlin)
    
    
    import com.rudderstack.sdk.kotlin.android.plugins.devicemode.IntegrationPlugin
    import com.rudderstack.sdk.kotlin.core.internals.plugins.Plugin
    import com.rudderstack.sdk.kotlin.core.internals.plugins.EventPlugin
    import com.rudderstack.sdk.kotlin.core.internals.models.Event
    import com.rudderstack.sdk.kotlin.core.internals.models.TrackEvent
    import com.rudderstack.integration.kotlin.firebase.FirebaseIntegration
    
    // Step 1: Create a custom plugin
    class MyCustomPlugin : EventPlugin {
        override val pluginType = Plugin.PluginType.PreProcess
        
        override suspend fun intercept(event: Event): Event? {
            // Filter out debug events
            return if (event is TrackEvent && event.event.startsWith("Debug_")) {
                null // This will drop the event
            } else {
                event // Pass through all other events
            }
        }
    }
    
    // Step 2: Add integration to analytics
    val integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    analytics.add(integrationPlugin)
    
    // Step 3: Add custom plugin to integration
    val customPlugin = MyCustomPlugin()
    integrationPlugin.add(customPlugin)
    
    
    
    import androidx.annotation.NonNull;
    import androidx.annotation.Nullable;
    import com.rudderstack.sdk.kotlin.core.Analytics;
    import com.rudderstack.sdk.kotlin.core.internals.models.Event;
    import com.rudderstack.sdk.kotlin.core.internals.models.TrackEvent;
    import com.rudderstack.sdk.kotlin.core.internals.plugins.Plugin;
    import kotlin.coroutines.Continuation;
    
    // Step 1: Create a custom plugin
    public class MyCustomPlugin implements Plugin {
        private Analytics analytics;
        private static final Plugin.PluginType pluginType = Plugin.PluginType.PreProcess;
    
        @Override
        public void setAnalytics(@NonNull Analytics analytics) {
            this.analytics = analytics;
        }
    
        @Override
        public void setup(@NonNull Analytics analytics) {
            this.analytics = analytics;
        }
    
        @Nullable
        @Override
        public Object intercept(@NonNull Event event, @NonNull Continuation<? super Event> $completion) {
            // Filter out debug events
            if (event instanceof TrackEvent && ((TrackEvent) event).getEvent().startsWith("Debug_")) {
                return null; // This will drop the event
            }
            return event; // Pass through all other events
        }
    
        @NonNull
        @Override
        public Analytics getAnalytics() {
            return this.analytics;
        }
    
        @NonNull
        @Override
        public Plugin.PluginType getPluginType() {
            return pluginType;
        }
    
        @Override
        public void teardown() {
            // Clean up resources if needed
        }
    }
    
    // Step 2: Add integration to analytics
    IntegrationPlugin integrationPlugin = new FirebaseIntegration();
    analytics.add(integrationPlugin);
    
    // Step 3: Add custom plugin to integration
    MyCustomPlugin customPlugin = new MyCustomPlugin();
    integrationPlugin.add(customPlugin);
    

### iOS (Swift)
    
    
    import RudderStackAnalytics
    import RudderIntegrationFirebase
    
    // Step 1: Create a custom plugin
    class MyCustomPlugin: EventPlugin {
        var pluginType: PluginType = .preProcess
        var analytics: Analytics?
        
        func intercept(event: any Event) -> (any Event)? {
            // Filter out debug events
            if let trackEvent = event as? TrackEvent,
               let eventName = trackEvent.event,
               eventName.hasPrefix("Debug_") {
                return nil // This will drop the event
            }
            return event // Pass through all other events
        }
    }
    
    // Step 2: Add integration to analytics
    let integrationPlugin: IntegrationPlugin = FirebaseIntegration()
    analytics.add(plugin: integrationPlugin)
    
    // Step 3: Add custom plugin to integration
    let customPlugin = MyCustomPlugin()
    integrationPlugin.add(plugin: customPlugin)
    
    
    
    // Step 1: Create custom plugin
    
    // MyCustomPlugin.h
    #import <Foundation/Foundation.h>
    @import RudderStackAnalytics;
    
    @interface MyCustomPlugin : NSObject <RSSEventPlugin>
    
    @end
    
    // MyCustomPlugin.m
    @implementation MyCustomPlugin
    @synthesize pluginType;
    
    - (instancetype)init {
        self = [super init];
        if (self) {
        }
        return self;
    }
    
    - (enum RSSPluginType)pluginType {
        return RSSPluginTypeTerminal;
    }
    
    - (RSSEvent *)intercept:(RSSEvent *)event {
        if ([event isKindOfClass:[RSSTrackEvent class]]) {
            RSSTrackEvent *trackEvent = (RSSTrackEvent *)event;
            NSString *eventName = trackEvent.eventName;
            if ([eventName hasPrefix:@"Debug_"]) {
                return nil; // This will drop the event
            }
        }
        return event; // Pass through all other events
    }
    
    @end
    
    // Step 2: Add integration to analytics:
    
    // Import Firebase integration at the top of the file
    @import RudderIntegrationFirebase;
    
    // Adding firebase integration to analytics instance
    RSSFirebaseIntegration *integrationPlugin = [RSSFirebaseIntegration new];
    [self.analytics addPlugin: integrationPlugin];
    
    // Step 3: Add custom plugin to integration:
    
    MyCustomPlugin *customPlugin = [MyCustomPlugin new];
    [self.analytics addPlugin:customPlugin destinationKey:integrationPlugin.key];
    

## Troubleshooting

Issue| Solution  
---|---  
Integration not initializing| 

  * Ensure you have added the integration plugin to the `Analytics` instance before calling any integration APIs
  * Check that the destination is enabled in your RudderStack dashboard
  * Verify that required dependencies are properly installed

  
Destination instance is null| 

  * The destination may not be initialized yet. Use `onDestinationReady()` to wait for initialization
  * Check if the integration failed to initialize by handling the failure case in `onDestinationReady()`
  * Ensure the integration is properly configured in your RudderStack dashboard

  
Events not reaching destination| 

  * Verify the integration is added to your `Analytics` instance
  * Check that events are being tracked using the standard RudderStack APIs (`track`, `identify`, etc.)
  * Review destination-specific requirements in the destination’s documentation

  
  
## See more

  * [Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>): Complete API reference for device mode integration APIs
  * [How to Build Custom Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/custom-integrations/>): Create custom integrations for unsupported destinations
  * [Plugin Architecture](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/>): Learn about the plugin system available in the mobile SDKs