# Track API in Mobile SDKs

Learn about the track API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide explains how to use the `track` API in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) API that lets you record the user’s actions along with any properties associated with them.

## Android (Kotlin)

The `track` method definition in the Android (Kotlin) SDK is as follows:
    
    
    analytics.track(
        name = "Product Added",
        properties = buildJsonObject {
            put("key", "value")
        },
        options = RudderOption()
    )
    

The corresponding Java snippet is shown below:
    
    
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("key", "value");
    
    analytics.track("Product Added", properties, new RudderOption());
    
    
    
    // Track event with event name
    analytics.track(name = "Product Added")
    
    // Track event with event name and properties
    analytics.track(
        name = "Product Added",
        properties = buildJsonObject {
            put("key-1", "value-1")
        },
    )
    
    // Track event with event name and options
    analytics.track(
        name = "Product Added",
        options = RudderOption(
            customContext = buildJsonObject {
                put("key-1", "value-1")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("lookup", "phone")
                })
            },
            externalIds = listOf(
                ExternalId(type = "brazeExternalId", id = "value1234"),
            ),
        ),
    )
    

### Method signature

The below table describes the `track` method signature in detail:

Field| Data type| Description  
---|---|---  
`name`| String| Name of the event.  
`properties`| Properties| Additional properties describing the event that you want to send.  
  
**Note** : The `properties` type in Java is `Map<String, Object>`.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `track` event sent from the Android (Kotlin) SDK is shown below:
    
    
    analytics.track(
        name = "Product Added",
        options = RudderOption(
            customContext = buildJsonObject {
                put("currency", "USD")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("lookup", "phone")
                })
            },
            externalIds = listOf(
                ExternalId(type = "brazeExternalId", id = "1hKOmRA4GRlm"),
            ),
        ),
    )
    
    
    
    Map<String, Object> customContext = new HashMap<>();
    customContext.put("key", "value");
    
    Map<String, Object> nestedIntegrations = new HashMap<>();
    nestedIntegrations.put("lookup", "phone");
    Map<String, Object> integrations = new HashMap<>();
    integrations.put("Amplitude", true);
    integrations.put("INTERCOM", nestedIntegrations);
    
    List<ExternalId> externalIds = new ArrayList<>();
    externalIds.add(new ExternalId("brazeExternalId", "1hKOmRA4GRlm"));
    
    RudderOption option = new RudderOptionBuilder()
            .setIntegrations(integrations)
            .setExternalId(externalIds)
            .setCustomContext(customContext)
            .build();
            
    analytics.track("Product Added", option);
    

## iOS (Swift)

The `track` method definition in the iOS (Swift) SDK is as follows:
    
    
    analytics.track(
        name: "Product Added",
        properties: [
            "key-1": "value-1"
        ],
        options: RudderOption()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include the `import RudderStackAnalytics` statement before making the call.

The corresponding Objective-C snippet is shown below:
    
    
    [analytics track:@"Product Added"
          properties:@{
              @"key-1": @"value-1"
          }
          options:[[RSSOptionBuilder new] build]];
    

> ![info](/docs/images/info.svg)
> 
> `RSSOptionBuilder` is an Objective-C–only helper class. It uses the builder pattern to create an `RSSOption` instance and lets you set custom context, configure integrations, and attach external IDs in a structured way.
    
    
    // Track event with event name
    analytics.track(name: "Product Added")
    
    // Track event with event name and properties
    analytics.track(
        name: "Product Added",
        properties: [
            "key-1": "value-1"
        ]
    )
    
    // Track event with event name and options
    analytics.track(
        name: "Product Added",
        properties: [
            "key-1": "value-1"
        ],
        options: RudderOption(
            integrations: [
                "Amplitude": true,
                "INTERCOM": [
                    "lookup": "phone"
                ]
            ],
            customContext: [
                "key-1": "value-1"
            ],
            externalIds: [
                ExternalId(type: "brazeExternalId", id: "value1234")
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    // Track event with event name
    [analytics track:@"Product Added"];
    
    // Track event with event name and properties
    [analytics track:@"Product Added"
        properties:@{
            @"key-1": @"value-1"
        }];
    
    // Track event with event name and options
    RSSOptionBuilder *optionBuilder = [[RSSOptionBuilder alloc] init];
    
    [optionBuilder setCustomContext:@{
        @"key-1": @"value-1"
    }];
    
    [optionBuilder setIntegrations:@{
        @"Amplitude": @YES,
        @"INTERCOM": @{
            @"lookup": @"phone"
        }
    }];
    
    [optionBuilder setExternalIds:@[
        [[RSSExternalId alloc] initWithType:@"brazeExternalId" id:@"value1234"]
    ]];
    
    [analytics track:@"Product Added"
          properties:@{
              @"key-1": @"value-1"
          }
          options:[optionBuilder build]];
    

### Method signature

The below table describes the `track` method signature in detail:

Field| Data type| Description  
---|---|---  
`name`| String| Name of the event.  
`properties`| Properties| Additional properties describing the event that you want to send.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `track` event sent from the iOS (Swift) SDK is shown below:
    
    
    analytics.track(
        name: "Track at \(Date())",
        properties: [
            "key-1": "value-1"
        ],
        options: RudderOption(
            integrations: [
                "Amplitude": true,
                "INTERCOM": [
                    "lookup": "phone"
                ]
            ],
            customContext: [
                "key-1": "value-1"
            ],
            externalIds: [
                ExternalId(type: "brazeExternalId", id: "value1234")
            ]
        )
    )
    
    
    
    RSSOptionBuilder *optionBuilder = [[RSSOptionBuilder alloc] init];
    
    [optionBuilder setCustomContext:@{
        @"key-1": @"value-1"
    }];
    
    [optionBuilder setIntegrations:@{
        @"Amplitude": @YES,
        @"INTERCOM": @{
            @"lookup": @"phone"
        }
    }];
    
    [optionBuilder setExternalIds:@[
        [[RSSExternalId alloc] initWithType:@"brazeExternalId" id:@"value1234"]
    ]];
    
    [analytics track:[NSString stringWithFormat:@"Track at %@", [NSDate date]]
          properties:@{
              @"key-1": @"value-1"
          }
          options:[optionBuilder build]];