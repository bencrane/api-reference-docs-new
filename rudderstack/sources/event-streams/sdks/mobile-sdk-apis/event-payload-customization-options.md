# Event Payload Customization Options in Mobile SDKs

Complete reference for the available event payload customization options available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __6 minute read

  * 


This guide walks you through the event payload customization options available in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a `RudderOption` instance that lets you customize the payload for any event type. You can use this instance to pass the following parameters:

Field| Description  
---|---  
`integrations`| Used to specify the integrations for which the event should be sent or blocked. You can also use it to specify some specific actions to be performed for a particular integration.  
`externalId`| Used to set a custom user ID or specific IDs required by some integrations.  
`customContext`| Used to add custom contextual information to the event payload.  
  
> ![warning](/docs/images/warning.svg)
> 
> The SDK does not persist the information set using the `integrations`, `externalId`, and `customContext` fields across different events.
> 
> Therefore, you must pass these parameters every time you want to add the information to an event.

## Integration options (`integrations`)

You can use the `integrations` field of the `RudderOption` instance to define the integration options for an event. These options include:

  * Allowing or blocking an event from being sent to a particular destination (in [cloud, device, or hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>))
  * Passing specific configuration or data to a particular destination


### `integrations` options

The `integrations` field accepts the following parameters:

Parameter| Data type| Description  
---|---|---  
`All`| Boolean| Global filtering status for all destinations. If set to `false`, RudderStack blocks the event from being sent to all destinations unless you override it with destination-specific parameters.  
  
**Default value:** `true`  
`<Destination>`| Boolean / Object| Specific destination to filter. It overrides the `All` parameter.  
  
If the type is Object, then the SDK automatically assumes this parameter to be `true`. You can then use this field to send destination-specific configuration or data in cloud and device modes.  
  
### Default behavior

By default, the `integrations` object is configured to send the event to **all** destinations which are present and initialized.
    
    
    {
      //.....
      "integrations": {
        "All": true
      },
      //.....
    }
    

You can override this behavior by tweaking the `integrations` object to allow or block specific destinations, or send any destination-specific information, as per your use case.

See the following guides for more information:

  * [How to allow or block an event for a specific destination](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/allow-block-events/>)
  * [How to send destination-specific configuration or data](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/send-destination-specific-data/>)


## Custom user ID (`externalId`)

The `externalId` field of the `RudderOption` instance is used to set a custom user ID or specific IDs required by some integrations. RudderStack adds this value under the `context.externalId` field of the event payload.

The following snippet demonstrates how to add a custom `externalId` to your `identify` event before sending it to the **Braze** destination:
    
    
    analytics.identify(
        userId = "1hKOmRA4GRlm",
        options = RudderOption(
            externalIds = listOf(
                ExternalId(type = "brazeExternalId", id = "Brz1hGXsD")
            )
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    List<ExternalId> externalIds = new ArrayList<>();
    externalIds.add(new ExternalId("brazeExternalId", "Brz1hGXsD"));
    
    Map<String, Object> traits = new HashMap<>(); // Define empty traits map
    
    RudderOption option = new RudderOptionBuilder()
            .setExternalId(externalIds)
            .build();
    
    analytics.identify("1hKOmRA4GRlm", traits, option);
    
    
    
    analytics.identify(
        userId: "User123",
        options: RudderOption(
            externalIds: [
                ExternalId(type: "brazeExternalId", id: "Brz1hGXsD")
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    
    [optionBuilder setExternalIds:@[
        [[RSSExternalId alloc] initWithType:@"brazeExternalId" id:@"Brz1hGXsD"]
    ]];
    
    [analytics identify:@"User123"
              options:[optionBuilder build]];
    

After making the above call, the custom ID will be added to the `context.externalId` field of the event payload, as shown:
    
    
    {
      //.....
      "context": {
        //......
        "externalId": [{
          "id": "Brz1hGXsD",
          "type": "brazeExternalId"
        }],
        //......
      }
      //.....
    }
    

## Custom context (`customContext`)

The `customContext` field of the `RudderOption` instance is used to add custom contextual information to the event payload. This field is a JSON object that can contain any key-value pairs.

The following snippet demonstrates how to add custom context to your `track` event:
    
    
    analytics.track(
        name = "Track Event",
        properties = Properties(emptyMap()),
        options = RudderOption(
            customContext = buildJsonObject {
                put("Plan", "Enterprise")
                put("Product", buildJsonObject {
                    put("Type", "Accessories")
                })
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Track Event";
    
    Map<String, Object> context = new HashMap<>();
    context.put("Plan", "Enterprise");
    context.put("Product", Map.of("Type", "Accessories"));
    
    RudderOption option = new RudderOptionBuilder()
            .setCustomContext(context)
            .build();
    
    analytics.track(name, option);
    
    
    
    analytics.track(
        name: "Track Event",
        options: RudderOption(
            customContext: [
                "Plan": "Enterprise",
                "Product": [
                    "Type": "Accessories"
                ]
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    
    [optionBuilder setCustomContext:@{
        @"Plan": @"Enterprise",
        @"Product": @{
            @"Type": @"Accessories"
        }
    }];
    
    [analytics track:@"Track Event"
           options:[optionBuilder build]];
    

After making the above call, the custom context will be added to the `context` field of the event payload, as shown:
    
    
    {
      //.....
      "context": {
        //.....
        "Plan": "Enterprise",
        "Product": {
          "Type": "Accessories"
        },
        //....
      }
      //.....
    }
    

Note that you **cannot** use the `customContext` field to override the default contextual fields set by the SDK. For example, if you set the `device` field in the `customContext` object, the SDK ignores it and uses the default device information instead. An example is shown below:
    
    
    analytics.track(
        name = "Track Event",
        properties = Properties(emptyMap()),
        options = RudderOption(
            customContext = buildJsonObject {
                put("Plan", "Enterprise") // This will reflect in the final event payload
                put("device", buildJsonObject {  // This won't reflect in the final event payload
                    put("id", "my-device-id")
                    put("name", "My Android Device") 
                })
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String name = "Track Event";
    
    Map<String, Object> context = new HashMap<>();
    context.put("Plan", "Enterprise");
    context.put("device", Map.of("id", "my-device-id", "name", "My Android Device"));
    
    RudderOption option = new RudderOptionBuilder()
            .setCustomContext(context)
            .build();
    
    analytics.track(name, option);
    
    
    
    analytics.track(
        name: "Track Event",
        options: RudderOption(
            customContext: [
                "Plan": "Enterprise", // Present in the final event payload
                "device": [ // Absent in the final event payload
                    "id": "my-device-id",
                    "name": "My Android Device"
                ]
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    
    [optionBuilder setCustomContext:@{
        @"Plan": @"Enterprise",
        @"device": @{
            @"id": @"my-device-id",
            @"name": @"My Android Device"
        }
    }];
    
    [analytics track:@"Track Event"
           options:[optionBuilder build]];
    

After making the above call, the `context` field of the event payload will contain the following:
    
    
    {
    	//.....
    	"context": {
          //.....
          "Plan": "Enterprise",
          "device": { // The default device info captured by the SDK
              "id": "d190f76ea636bc44",
              "manufacturer": "Google",
              "model": "sdk_gphone64_arm64",
              "name": "emu64a",
              "type": "Android"
          },
          //.....
      }
      //.....
    }
    

> ![warning](/docs/images/warning.svg)
> 
> **Overriding default contextual fields**
> 
> RudderStack does not recommend overriding the default contextual fields set by the SDK as it can lead to unexpected issues.
> 
> However, if you wish to do so, you can use a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>) to override the default contextual fields.

## Example

The following snippet demonstrates how to use the `RudderOption` instance to customize the event payload:
    
    
    analytics.identify(
        userId = "1hKOmRA4GRlm",
        options = RudderOption(
            integrations = buildJsonObject {
                put("Firebase", false) // Event disabled for Firebase
            },
            externalIds = listOf(
                ExternalId(type = "brazeExternalId", id = "Brz1hGXsD")
            ),
            customContext = buildJsonObject {
                put("Plan", "Enterprise")
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String userId = "1hKOmRA4GRlm";
    
    Map<String, Object> context = new HashMap<>();
    context.put("Plan", "Enterprise");
    
    ExternalId externalId = new ExternalId("brazeExternalId", "Brz1hGXsD");
    List<ExternalId> externalIds = Arrays.asList(externalId);
    
    Map<String, Object> integrations = new LinkedHashMap<>();
    integrations.put("Firebase", false);
    
    RudderOption option = new RudderOptionBuilder()
            .setIntegrations(integrations)
            .setExternalId(externalIds)
            .setCustomContext(context)
            .build();
    
    analytics.identify(userId, option);
    
    
    
    analytics.identify(
        userId: "1hKOmRA4GRlm",
        options: RudderOption(
            integrations: [
                "Firebase": false // event disabled for Firebase
            ],
            customContext: [
                "Plan": "Enterprise"
            ],
            externalIds: [
                ExternalId(type: "brazeExternalId", id: "Brz1hGXsD")
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    
    [optionBuilder setIntegrations:@{
        @"Firebase": @NO
    }];
    
    [optionBuilder setCustomContext:@{
        @"Plan": @"Enterprise"
    }];
    
    [optionBuilder setExternalIds:@[
        [[RSSExternalId alloc] initWithType:@"brazeExternalId" id:@"Brz1hGXsD"]
    ]];
    
    [analytics identify:@"1hKOmRA4GRlm"
              options:[optionBuilder build]];
    

The above snippet:

  * Disables the `identify` event for the **Firebase** integration through the `integrations` parameter
  * Sets a custom user ID for the Braze integration through the `externalId` parameter
  * Adds custom contextual information (`Plan: Enterprise`) to the event payload through the `customContext` parameter