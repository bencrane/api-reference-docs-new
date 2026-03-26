# How to Create a Custom Plugin in Mobile SDKs

Create a custom plugin in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide lists the steps to create a sample custom plugin in the [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

[Custom plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) are user-defined plugins that provide flexibility in extending and modifying event processing within the SDK.

## Android (Kotlin)

This section lists the steps to create a custom plugin `EventFilteringPlugin` for filtering out specific `track` events in the [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) SDK.

Specifically, it filters out the `Application Opened` and `Application Backgrounded` events and prevents them from being tracked.

  1. Add the plugin logic:


    
    
    import com.rudderstack.sdk.kotlin.core.Analytics
    import com.rudderstack.sdk.kotlin.core.internals.logger.LoggerAnalytics
    import com.rudderstack.sdk.kotlin.core.internals.models.Event
    import com.rudderstack.sdk.kotlin.core.internals.models.TrackEvent
    import com.rudderstack.sdk.kotlin.core.internals.plugins.Plugin
    
    class EventFilteringPlugin : Plugin {
    
        override val pluginType: Plugin.PluginType = Plugin.PluginType.OnProcess
        override lateinit var analytics: Analytics
    
        private lateinit var listOfEventsToBeFiltered: List<String>
    
        override fun setup(analytics: Analytics) {
            super.setup(analytics)
            listOfEventsToBeFiltered = listOf("Application Opened", "Application Backgrounded")
        }
    
        override suspend fun intercept(event: Event): Event? {
            if (event is TrackEvent && listOfEventsToBeFiltered.contains(event.event)) {
                LoggerAnalytics.verbose("EventFilteringPlugin: Event ${event.event} is filtered out")
                return null
            }
            return event
        }
    
        override fun teardown() {
            listOfEventsToBeFiltered = emptyList()
        }
    }
    
    
    
    import androidx.annotation.NonNull;
    import androidx.annotation.Nullable;
    
    import com.rudderstack.sdk.kotlin.core.Analytics;
    import com.rudderstack.sdk.kotlin.core.internals.logger.LoggerAnalytics;
    import com.rudderstack.sdk.kotlin.core.internals.models.Event;
    import com.rudderstack.sdk.kotlin.core.internals.models.TrackEvent;
    import com.rudderstack.sdk.kotlin.core.internals.plugins.Plugin;
    
    import java.util.List;
    
    import kotlin.coroutines.Continuation;
    
    /**
     * A custom Java Plugin demonstrating how to perform event filtering in Java.
     */
    public class JavaEventFilteringPlugin implements Plugin {
        private Analytics analytics;
        private static final Plugin.PluginType pluginType = Plugin.PluginType.OnProcess;
    
        List<String> listOfEventsToBeFiltered;
    
        @Override
        public void setAnalytics(@NonNull Analytics analytics) {
            this.analytics = analytics;
        }
    
        @Override
        public void setup(@NonNull Analytics analytics) {
            this.analytics = analytics;
            listOfEventsToBeFiltered = List.of("Application Opened", "Application Backgrounded");
        }
    
        @Nullable
        @Override
        public Object intercept(@NonNull Event event, @NonNull Continuation<? super Event> $completion) {
            if (event instanceof TrackEvent && listOfEventsToBeFiltered.contains(((TrackEvent) event).getEvent())) {
                LoggerAnalytics.INSTANCE.verbose("EventFilteringPlugin: Event " + ((TrackEvent) event).getEvent() + " is filtered out");
                return null;
            }
    
            return event;
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
            listOfEventsToBeFiltered = null;
        }
    }
    

  2. Create an `EventFilteringPlugin` plugin:


    
    
    val eventFilteringPlugin = EventFilteringPlugin()
    
    
    
    JavaEventFilteringPlugin eventFilteringPlugin = new JavaEventFilteringPlugin();
    

  3. Add the plugin after initializing the SDK:


    
    
    analytics.add(eventFilteringPlugin)
    
    
    
    analytics.add(eventFilteringPlugin);
    

  4. To remove the plugin:


    
    
    analytics.remove(eventFilteringPlugin)
    
    
    
    analytics.remove(eventFilteringPlugin);
    

## iOS (Swift)

This section lists the steps to create a custom plugin `EventFilteringPlugin` for filtering out specific `track` events in the [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDK.

Specifically, it filters out the `Application Opened` and `Application Backgrounded` events and prevents them from being tracked.

  1. Add the plugin logic:


    
    
    import RudderStackAnalytics
    
    final class EventFilteringPlugin: Plugin {
        var pluginType: PluginType = .onProcess
        var analytics: Analytics?
        
        private var eventsToFilter = [String]()
        
        func setup(analytics: Analytics) {
            self.analytics = analytics
            self.eventsToFilter = ["Application Opened", "Application Backgrounded"]
        }
        
        func intercept(event: any Event) -> (any Event)? {
            if let trackEvent = event as? TrackEvent, self.eventsToFilter.contains(trackEvent.event) {
                LoggerAnalytics.verbose(log: "EventFilteringPlugin: Event \"\(trackEvent.event)\" is filtered out.")
                return nil
            }
            return event
        }
        
        func teardown() {
            self.eventsToFilter.removeAll()
            self.analytics = nil
        }
    }
    
    
    
    @interface EventFilteringPlugin()
    
    @property(nonatomic, retain) RSSAnalytics *client;
    @property(nonatomic, retain) NSMutableArray *eventsToFilter;
    
    @end
    
    @implementation EventFilteringPlugin
    @synthesize pluginType;
    
    - (instancetype)init {
        self = [super init];
        if (self) {
        }
        return self;
    }
    
    - (RSSPluginType)pluginType {
        return RSSPluginTypeOnProcess;
    }
    
    - (void)setup:(RSSAnalytics * _Nonnull)analytics {
        self.client = analytics;
        self.eventsToFilter = [NSMutableArray arrayWithArray: @[@"Application Opened", @"Application Backgrounded"]];
    }
    
    - (RSSEvent * _Nullable)intercept:(RSSEvent * _Nonnull)event {
        if ([event isKindOfClass:[RSSTrackEvent class]]) {
            RSSTrackEvent *trackEvent = (RSSTrackEvent *)event;
            if ([self shouldFilterEvent:trackEvent]) {
                [RSSLoggerAnalytics verbose:[NSString stringWithFormat:@"EventFilteringPlugin: Event \"%@\" is filtered out.", trackEvent.eventName]];
                return nil; // Filter out this event
            }
        }
        return event; // Allow event to pass through
    }
    
    - (BOOL)shouldFilterEvent:(RSSTrackEvent *)trackEvent {
        return [self.eventsToFilter containsObject:trackEvent.eventName];
    }
    
    - (void)teardown {
        [self.eventsToFilter removeAllObjects];
        self.eventsToFilter = nil;
        self.client = nil;
    }
    

  2. Create an `EventFilteringPlugin` plugin:


    
    
    let eventFilteringPlugin = EventFilteringPlugin()
    
    
    
    EventFilteringPlugin *eventFilteringPlugin = [[EventFilteringPlugin alloc] init];
    

  3. Add the plugin after initializing the SDK:


    
    
    analytics.add(plugin: eventFilteringPlugin)
    
    
    
    [self.analytics addPlugin: eventFilteringPlugin];
    

  4. To remove the plugin:


    
    
    analytics.remove(plugin: eventFilteringPlugin)
    
    
    
    [self.analytics removePlugin:eventFilteringPlugin];
    

> ![info](/docs/images/info.svg)
> 
> You can also use custom plugins with device mode integrations.
> 
> See [Add custom plugins to integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/#add-custom-plugins-to-integrations>) for more information.

## Workflow overview

In the above example, `EventFilteringPlugin` is a custom plugin that intercepts and filters the specified events before they are processed.

The high-level workflow is described below:

  * While initializing the plugin, you can specify a list of events to be filtered.
  * When an event is received, the plugin checks if it matches any of the events specified in the filter list.
  * If the event is present in the filter list, the plugin logs a message and discards it by returning `null`. Otherwise, it forwards the event for processing, as usual.
  * The `teardown` method clears the event list whenever you remove the plugin.