# Identify API in Mobile SDKs

Learn about the identify API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __5 minute read

  * 


This guide explains how to use the `identify` API in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) API that lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

> ![info](/docs/images/info.svg)
> 
> Once you make the identify call, the SDK persists the user information and passes it to the subsequent calls.

## Android (Kotlin)

The `identify` method definition in the Android (Kotlin) SDK is as follows:
    
    
    analytics.identify(
        userId = "<userId>",
        traits = buildJsonObject {
            put("key", "value")
        },
        options = RudderOption(),
    )
    

The corresponding Java snippet is shown below:
    
    
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("key", "value");
    
    analytics.identify("<userId>", traits, new RudderOption());
    
    
    
    // Identify event with userId
    analytics.identify(userId = "<userId>")
    
    // Identify event with traits
    analytics.identify(
        traits = buildJsonObject {
            put("key", "value")
        },
    )
    
    // Identify event with userId and traits
    analytics.identify(
        userId = "<userId>",
        traits = buildJsonObject {
            put("key", "value")
        },
    )
    
    // Identify event with userId and options
    analytics.identify(
        userId = "<userId>",
        options = RudderOption(
            customContext = buildJsonObject {
                put("key", "value")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("lookup", "field")
                })
            },
            externalIds = listOf(
                ExternalId(type = "<id_type>", id = "<value>"),
            ),
        ),
    )
    
    // Identify event with traits and options
    analytics.identify(
        traits = buildJsonObject {
            put("key", "value")
        },
        options = RudderOption(
            customContext = buildJsonObject {
                put("key", "value")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("lookup", "field")
                })
            },
            externalIds = listOf(
                ExternalId(type = "<id_type>", id = "<value>"),
            ),
        ),
    )
    

### Method signature

The below table describes the `identify` method signature in detail:

Field| Data type| Description  
---|---|---  
`userId`  
Required, if `traits` is not present| String| Unique user identifier. When provided, RudderStack prefers this field over `anonymousId` while sending data to the destinations.  
`traits`  
Required, if `userId` is not present| Traits| Contains the user traits or the properties associated with `userId` such as `email`, `address`, etc. See [Identify traits](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>) for more information.  
  
Note that:  
  


  * RudderStack stores the traits as `context.traits` in the final event object.
  * The `traits` type in Java is `Map<String, Object>`.

  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `identify` event sent from the Android (Kotlin) SDK is shown below:
    
    
    analytics.identify(
        userId = "1hKOmRA4GRlm",
        traits = buildJsonObject {
            put("city", "New Orleans")
        },
        options = RudderOption(
            customContext = buildJsonObject {
                put("key", "value")
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
    
    
    
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("city", "New Orleans");
    
    Map<String, Object> customContext = new HashMap<>();
    customContext.put("key", "value");
    
    Map<String, Object> nestedIntegrations = new HashMap<>();
    nestedIntegrations.put("lookup", "phone");
    Map<String, Object> integrations = new HashMap<>();
    integrations.put("Amplitude", true);
    integrations.put("INTERCOM", nestedIntegrations);
    
    List<ExternalId> externalIds = new ArrayList<>();
    externalIds.add(new ExternalId("brazeExternalId", "value1234"));
    
    RudderOption option = new RudderOptionBuilder()
            .setIntegrations(integrations)
            .setExternalId(externalIds)
            .setCustomContext(customContext)
            .build();
    
    analytics.identify("1hKOmRA4GRlm", traits, option);
    

## iOS (Swift)

The `identify` method definition in the iOS (Swift) SDK is as follows:
    
    
    analytics.identify(
        userId: "User 1",
        traits: [
            "key-1": "value-1"
        ],
        options: RudderOption()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include the `import RudderStackAnalytics` statement before making the call.

The corresponding Objective-C snippet is shown below:
    
    
    [analytics identify:@"User 1"
              traits:@{
                  @"key-1": @"value-1"
              }
              options:[[RSSOptionBuilder new] build]];
    

> ![info](/docs/images/info.svg)
> 
> `RSSOptionBuilder` is an Objective-C–only helper class. It uses the builder pattern to create an `RSSOption` instance and lets you set custom context, configure integrations, and attach external IDs in a structured way.
    
    
    // Identify event with userId
    analytics.identify(userId: "User 1")
    
    // Identify event with traits
    analytics.identify(
        traits: [
            "key-1": "value-1"
        ]
    )
    
    // Identify event with userId and traits
    analytics.identify(
        userId: "User 1",
        traits: [
            "key-1": "value-1"
        ]
    )
    
    // Identify event with userId and options
    analytics.identify(
        userId: "User 1",
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
    
    // Identify event with traits and options
    analytics.identify(
        traits: [
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
    
    
    // Identify event with userId
    [analytics identify:@"User 1"];
    
    // Identify event with traits
    [analytics identifyWithTraits:@{
                  @"key-1": @"value-1"
              }];
    
    // Identify event with userId and traits
    [analytics identify:@"User 1"
              traits:@{
                  @"key-1": @"value-1"
              }];
    
    // Identify event with userId and options
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
    
    [analytics identify:@"User 1"
              options:[optionBuilder build]];
    
    // Identify event with traits and options
    [analytics identifyWithTraits:@{
                  @"key-1": @"value-1"
              }
              options:[optionBuilder build]];
    

### Method signature

The below table describes the `identify` method signature in detail:

Field| Data type| Description  
---|---|---  
`userId`  
Required, if `traits` is not present| String| Unique user identifier. When provided, RudderStack prefers this field over `anonymousId` while sending data to the destinations.  
`traits`  
Required, if `userId` is not present| Properties| Contains the user traits or the properties associated with `userId` such as `email`, `address`, etc. See [Identify traits](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>) for more information.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `identify` event sent from the Swift SDK is shown below:
    
    
    analytics.identify(
        userId: "User 1",
        traits: [
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
    
    [analytics identify:@"User 1"
              traits:@{
                  @"key-1": @"value-1"
              }
              options:[optionBuilder build]];