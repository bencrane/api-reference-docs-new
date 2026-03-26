# How to Allow or Block an Event for a Specific Destination

Learn how to allow or block an event for a specific destination in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide demonstrates how to use the [`integrations`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#the-integrations-field>) field of the `RudderOption` instance to implement event filtering, that is, allowing or blocking an event from being sent to a specific destination.

> ![success](/docs/images/tick.svg)
> 
> You can also use the `integrations` field to [send destination-specific data in event payload](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/send-destination-specific-data/>).

## Overview

By default, the `integrations` object is configured to send the event to **all** destinations which are present and initialized.
    
    
    {
      //.....
      "integrations": {
        "All": true
      },
      //.....
    }
    

You can override this behavior by tweaking the `integrations` object to allow or block an event from being sent to a specific destination in [cloud, device, or hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

> ![info](/docs/images/info.svg)
> 
> The Android (Kotlin) and iOS (Swift) SDKs do not persist the `integrations` field set for an event for subsequent events. Therefore, you must pass this parameter every time you want to allow or block an event for a specific destination.

## Allow event for a specific destination

To send an event only to a specific destination, configure the [`integrations` options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations-options>) so that:

  * The `All` parameter is set to `false`
  * The destination-specific parameter is set to `true`


> ![warning](/docs/images/warning.svg)
> 
> The destination name in the `integrations` object should match the name exactly as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). It should **not** be the name that you assigned to the destination while setting it up in RudderStack.
> 
> ![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)

An example of how to configure the `integrations` options to allow an event to be sent only to the **Firebase** destination is shown below:
    
    
    analytics.track(
        name = "Track Event",
        options = RudderOption(
            integrations = buildJsonObject {
                put("All", false) // Event blocked for all destinations
                put("Firebase", true) // Event allowed for Firebase destination
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Track Event";
    
    Map<String, Object> integrations = new LinkedHashMap<>();
    integrations.put("All", false);
    integrations.put("Firebase", true);
    
    RudderOption option = new RudderOptionBuilder()
                    .setIntegrations(integrations)
                    .build();
    
    analytics.track(name, option);
    
    
    
    analytics.track(
        name: "Track Example",
        options: RudderOption(
            integrations: [
                "All": false,
                "Firebase": true  // Event disabled for all destinations except Firebase
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    [optionBuilder setIntegrations:@{
        @"All": @NO,
        @"Firebase": @YES  // Event disabled for all except Firebase
    }];
    
    [analytics track:@"Track Example"
           options:[optionBuilder build]];
    

After making the above call, the `integrations` key at the root level of the event payload is shown below. RudderStack then sends this event only to the **Firebase** destination.
    
    
    {
      //.....
      "integrations": {
        "All": false,
        "Firebase": true
      },
      //.....
    }
    

## Block event for a specific destination

To block an event from being sent to a specific destination, configure the [`integrations` options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations-options>) so that:

  * The `All` parameter is set to `true`
  * The destination-specific parameter is set to `false`


> ![warning](/docs/images/warning.svg)
> 
> The destination name in the `integrations` object should match the name exactly as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). It should **not** be the name that you assigned to the destination while setting it up in RudderStack.
> 
> ![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)

An example of how to configure the `integrations` options to block an event from being sent to the **Firebase** destination is shown below:
    
    
    analytics.track(
        name = "Track Event",
        options = RudderOption(
            integrations = buildJsonObject {
                put("Firebase", false) // Event blocked for Firebase destination
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Track Event";
    
    Map<String, Object> integrations = new LinkedHashMap<>();
    integrations.put("Firebase", false);
    
    RudderOption option = new RudderOptionBuilder()
                    .setIntegrations(integrations)
                    .build();
    
    analytics.track(name, option);
    
    
    
    analytics.track(
        name: "Track Example",
        options: RudderOption(
            integrations: [
                "Firebase": false // Event disabled for Firebase destination
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    [optionBuilder setIntegrations:@{
        @"Firebase": @NO // event disabled for firebase
    }];
    
    [analytics track:@"Track Example"
           options:[optionBuilder build]];
    

After making the above call, the `integrations` key at the root level of the event payload is shown below. RudderStack then sends this event to all destinations except **Firebase**.
    
    
    {
      //.....
      "integrations": {
        "All": true,
        "Firebase": false
      },
      //.....
    }
    

## Block event for all destinations

To block an event from being sent to all destinations, configure the [`integrations` options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations-options>) so that:

  * The `All` parameter is set to `false`


An example of this use case is shown below:
    
    
    analytics.track(
        name = "Track Event",
        options = RudderOption(
            integrations = buildJsonObject {
                put("All", false) // Event blocked for all destinations
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Track Event";
    
    Map<String, Object> integrations = new LinkedHashMap<>();
    integrations.put("All", false);
    
    RudderOption option = new RudderOptionBuilder()
                    .setIntegrations(integrations)
                    .build();
    
    analytics.track(name, option);
    
    
    
    analytics.screen(
        screenName: "Some Screen",
        options: RudderOption(
            integrations: [
                "All": false  // All integrations blocked
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    [optionBuilder setIntegrations:@{
        @"All": @NO  // All integrations blocked
    }];
    
    [analytics screen:@"Some Screen"
            options:[optionBuilder build]];
    

After making the above call, the `integrations` key at the root level of the event payload is shown below. RudderStack then does not send this event to any destination.
    
    
    {
      //.....
      "integrations": {
        "All": false
      },
      //.....
    }
    

## See also

  * [How to send destination-specific configuration or data in event payload](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/send-destination-specific-data/>)