# Screen API in Mobile SDKs

Learn about the screen API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide explains how to use the `screen` API in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) API that lets you record whenever your user views their mobile screen, along with any additional relevant information about the screen.

## Android (Kotlin)

The `screen` method definition in the Android (Kotlin) SDK is as follows:
    
    
    analytics.screen(
        screenName = "<name>",
        category = "<category>",
        properties = buildJsonObject {
            put("key", "value")
        },
        options = RudderOption(),
    )
    

The corresponding Java snippet is shown below:
    
    
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("key", "value");
    
    analytics.screen("<name>", "<category>", properties, new RudderOption());
    
    
    
    // Screen event with screen name
    analytics.screen(screenName = "Main Screen")
    
    // Screen event with screen name and category
    analytics.screen(screenName = "Main Screen", category = "Main")
    
    // Screen event with screen name, category and properties
    analytics.screen(
        screenName = "Main Screen",
        category = "Main",
        properties = buildJsonObject {
            put("key-1", "value")
        }
    )
    
    // Screen event with screen name and properties
    analytics.screen(
        screenName = "Main Screen",
        properties = buildJsonObject {
            put("key-1", "value")
        }
    )
    
    // Screen event with screen name, category, and options
    analytics.screen(
        screenName = "Main Screen",
        category = "Main",
        options = RudderOption(
            customContext = buildJsonObject {
                put("key-1", "value")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("field", "value")
                })
            },
            externalIds = listOf(
                ExternalId(type = "<id_type>", id = "<value>"),
            ),
        )
    )
    

### Method signature

The below table describes the `screen` method signature in detail:

Field| Data type| Description  
---|---|---  
`screenName`| String| Name of the screen viewed by the user.  
`category`| String| Screen category.  
`properties`| Properties| Additional properties describing the screen to be sent along with the event.  
  
**Note** : The `properties` type in Java is `Map<String, Object>`.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `screen` event sent from the Android (Kotlin) SDK is shown below:
    
    
    analytics.screen(
        screenName = "Main Screen",
        category = "Main",
        properties = buildJsonObject {
            put("type", "application")
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
    
    
    
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("type", "application");
    
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
    
    analytics.screen("Main Screen", "Main", properties, option);
    

## iOS (Swift)

The `screen` method definition in the iOS (Swift) SDK is as follows:
    
    
    analytics.screen(
        screenName: "<name>",
        category: "<category>",
        properties: [
            "key": "value"
        ],
        options: RudderOption()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include the `import RudderStackAnalytics` statement before making the call.

The corresponding Objective-C snippet is shown below:
    
    
    [analytics screen:@"<name>" category:@"<category>" properties:@{@"key": @"value"} options:[[RSSOptionBuilder new] build]];
    

> ![info](/docs/images/info.svg)
> 
> `RSSOptionBuilder` is an Objective-C–only helper class. It uses the builder pattern to create an `RSSOption` instance and lets you set custom context, configure integrations, and attach external IDs in a structured way.
    
    
    // Screen event with screen name
    analytics.screen(screenName: "Main Screen")
    
    // Screen event with screen name and category
    analytics.screen(screenName: "Main Screen", category: "Main")
    
    // Screen event with screen name, category and properties
    analytics.screen(
        screenName: "Main Screen",
        category: "Main",
        properties: [
            "key-1": "value-1"
        ]
    )
    
    // Screen event with screen name and properties
    analytics.screen(
        screenName: "Main Screen",
        properties: [
            "key-1": "value-1"
        ]
    )
    
    // Screen event with screen name, category, and options
    analytics.screen(
        screenName: "Main Screen",
        category: "Main",
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
    
    
    // Screen event with screen name
    [analytics screen:@"Main Screen"];
    
    // Screen event with screen name and category
    [analytics screen:@"Main Screen" category:@"Main"];
    
    // Screen event with screen name, category and properties
    [analytics screen:@"Main Screen"
             category:@"Main"
           properties:@{
               @"key-1": @"value-1"
           }];
    
    // Screen event with screen name and properties
    [analytics screen:@"Main Screen"
           properties:@{
               @"key-1": @"value-1"
           }];
    
    // Screen event with screen name, category, and options
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
    
    [analytics screen:@"Main Screen"
             category:@"Main"
           properties:@{
               @"key-1": @"value-1"
           }
             options:[optionBuilder build]];
    

### Method signature

The below table describes the `screen` method signature in detail:

Field| Data type| Description  
---|---|---  
`screenName`| String| Name of the screen viewed by the user.  
`category`| String| Screen category.  
`properties`| Properties| Additional properties describing the screen to be sent along with the event.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `screen` event sent from the iOS (Swift) SDK is shown below:
    
    
    analytics.screen(
        screenName: "Main Screen",
        category: "Main",
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
    
    [analytics screen:@"Main Screen"
             category:@"Main"
           properties:@{
               @"key-1": @"value-1"
           }
             options:[optionBuilder build]];