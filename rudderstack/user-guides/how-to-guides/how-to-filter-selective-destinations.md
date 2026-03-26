# Filter Selective Destinations while Sending Events

Filter selective destinations while sending your event data via RudderStack.

* * *

  * __4 minute read

  * 


This guide covers how to filter events to specific destinations while sending them via RudderStack.

## Overview

RudderStack lets you send your event data only to specific destination or a set of destinations by filtering out the rest. You can do this by passing an `integrations` object in the `options` parameter of your event method.

See the following guides for the SDK-specific documentation and examples:

  * [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>)
  * [Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/allow-block-events/>)
  * [iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/allow-block-events/>)
  * [Android (Java) — Legacy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#enabledisable-events-for-specific-destinations>)
  * [iOS (Obj-C) — Legacy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#filter-events-for-specific-destinations>)


## Filter events to specific destinations

The following example demonstrates how to send an event **only** to HubSpot and Intercom using the JavaScript SDK:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        email: "alex@example.com",
        name: "Alex Keener",
      }, {
        integrations: {
          All: false,
          "HubSpot": true,
          "Intercom": true,
        },
      }
    )
    

Note that:

  * `All` is always set to `true` unless explicitly set to `false` — this means RudderStack sends the event to all destinations by default.
  * `All: false` instructs RudderStack to not send the event to all destinations.


## Disable events for specific destinations

You can also disable sending event data to specific destinations. In this case, RudderStack sends the event data to **all other destinations** except the specified ones.
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        email: "alex@example.com",
        name: "Alex Keener",
      }, {
        integrations: {
          "HubSpot": false,
          "Intercom": false,
        },
      }
    )
    

In the above code snippet, RudderStack will send the event data to all destinations **except** HubSpot and Intercom.

## Destination naming convention

To filter events to specific destinations, you must specify the exact destination names. Go to the destination’s page in the RudderStack dashboard to get the name.

> ![warning](/docs/images/warning.svg)
> 
> The destination name in the `integrations` object is case sensitive — it should match the name exactly as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). It should **not** be the name that you assigned to the destination while setting it up in RudderStack.
> 
> ![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)

## Examples

This section lists some sample events sent from a different SDKs to the specified destinations.
    
    
    rudderanalytics.track(
      "Product Added", {
        product_id: "product_001",
        email: "alex@example.com",
        name: "Alex Keener"
      }, {
        integrations: {
          All: false,
          "Amplitude": true,
          "Intercom": true
        }
      }
    )
    
    
    
    analytics.track(
        name = "Product Added",
        options = RudderOption(
            integrations = buildJsonObject {
                put("All", false) // Event blocked for all destinations
                put("Amplitude", true) // Event allowed for Amplitude destination
                put("Intercom", true) // Event allowed for Intercom destination
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Product Added";
    
    Map<String, Object> integrations = new LinkedHashMap<>();
    integrations.put("All", false);
    integrations.put("Amplitude", true);
    integrations.put("Intercom", true);
    
    RudderOption option = new RudderOptionBuilder()
                    .setIntegrations(integrations)
                    .build();
    
    analytics.track(name, option);
    
    
    
    analytics.track(
        name: "Product Added",
        options: RudderOption(
            integrations: [
                "All": false,
                "Amplitude": true, // Event disabled for all destinations except Amplitude
                "Intercom": true, // Event disabled for all destinations except Intercom
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    [optionBuilder setIntegrations:@{
        @"All": @NO,
        @"Amplitude": @YES, // Event disabled for all destinations except Amplitude
        @"Intercom": @YES, // Event disabled for all destinations except Intercom
    }];
    
    [analytics track:@"Product Added"
           options:[optionBuilder build]];
    
    
    
    rudder_analytics.track(
      "Product Added", {
        "product_id": "product_001",
        "email": "alex@example.com",
        "name": "Alex Keener"
      },
      integrations={
        "All": False,
        "Amplitude": True,
        "Intercom": True
      }
    )
    
    
    
    // Create the RudderOption object
    val option = RudderOption()
    option.putIntegration("All", false)
    option.putIntegration("Amplitude", true)
    option.putIntegration("Intercom", true)
    
    rudderClient.track(
      "Product Added",
      RudderProperty()
        .putValue("product_id", "product_001")
        .putValue("email", "alex@example.com")
        .putValue("name", "Alex Keener"),
      option
    )
    

The corresponding Java snippet is shown below:
    
    
    // Create the RudderOption object
    RudderOption option = new RudderOption();
    option.putIntegration("All", false);
    option.putIntegration("Amplitude", true);
    option.putIntegration("Intercom", true);
    
    rudderClient.track(
      "Product Added",
      new RudderProperty()
        .putValue("product_id", "product_001")
        .putValue("email", "alex@example.com")
        .putValue("name", "Alex Keener"),
      option
    );
    
    
    
    // Create the RudderOption object
    RSOption *option = [[RSOption alloc] init];
    [option putIntegration:@"All" isEnabled:NO];
    [option putIntegration:@"Amplitude" isEnabled:YES];
    [option putIntegration:@"Intercom" isEnabled:YES];
    
    [[RSClient sharedInstance] track:@"Product Added" properties:@{
      @"product_id": @"product_001",
      @"email": @"alex@example.com",
      @"name": @"Alex Keener"
    } options:option];
    

The corresponding Swift snippet is shown below:
    
    
    // Create the RudderOption object
    let option = RSOption()
    option.putIntegration("All", isEnabled: false)
    option.putIntegration("Amplitude", isEnabled: true)
    option.putIntegration("Intercom", isEnabled: true)
    
    let rudder: RSClient? = RSClient.sharedInstance()
    rudder?.track("Product Added", properties: [
      "product_id": "product_001",
      "email": "alex@example.com",
      "name": "Alex Keener"
    ], options: option)
    

In the above examples, RudderStack SDKs send the `track` events only to the Amplitude and Intercom destinations.