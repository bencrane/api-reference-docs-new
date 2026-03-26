# Group API in Mobile SDKs

Learn about the group API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide explains how to use the `group` API in the [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) API that lets you link an identified user with a group like a company, organization, or an account. You can also record any custom traits associated with that group like the company name, number of employees, etc.

> ![info](/docs/images/info.svg)
> 
> You can link an identified user to multiple groups.

## Android (Kotlin)

The `group` method definition in the Android (Kotlin) SDK is as follows:
    
    
    analytics.group(
        groupId = "<groupId>",
        traits = buildJsonObject {
            put("key", "value")
        },
        options = RudderOption(),
    )
    

The corresponding Java snippet is shown below:
    
    
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("key", "value");
    
    analytics.group("<groupId>", traits, new RudderOption());
    
    
    
    // Group event with groupId
    analytics.group(
        groupId = "<groupId>"
    )
    
    // Group event with groupId and traits
    analytics.group(
        groupId = "<groupId>",
        traits = buildJsonObject {
            put("key", "value")
        }
    )
    
    // Group event with groupId, traits and options
    analytics.group(
        groupId = "<groupId>",
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
                    put("field", "value")
                })
            },
            externalIds = listOf(
                ExternalId(type = "<id_type>", id = "<value>")
            )
        )
    )
    

### Method signature

The below table describes the `group` method signature in detail:

Field| Data type| Description  
---|---|---  
`groupId`| String| The group’s unique identifier in your database.  
`traits`| Traits| Contains traits associated with the group. They are added in the root level of the event.  
  
Note that:  
  


  * RudderStack does not store any group traits.
  * The `traits` type in Java is `Map<String, Object>`.

  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `group` event sent from the Android (Kotlin) SDK is shown below:
    
    
    analytics.group(
        groupId = "5e8a78ba9d32d3b1898a6247",
        traits = buildJsonObject {
            put("name", "RudderStack")
        },
        options = RudderOption(
            customContext = buildJsonObject {
                put("plan", "Basic")
            },
            integrations = buildJsonObject {
                put("Amplitude", true)
                put("INTERCOM", buildJsonObject {
                    put("lookup", "phone")
                })
            },
            externalIds = listOf(
                ExternalId(type = "brazeExternalId", id = "value1234")
            )
        )
    )
    
    
    
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("name", "RudderStack");
    
    Map<String, Object> customContext = new HashMap<>();
    customContext.put("plan", "Basic");
    
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
    
    analytics.group("5e8a78ba9d32d3b1898a6247", traits, option);
    

## iOS (Swift)

The `group` method definition in the iOS (Swift) SDK is as follows:
    
    
    analytics.group(
        groupId: "<groupId>",
        traits: [
            "key": "value"
        ],
        options: RudderOption()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include the `import RudderStackAnalytics` statement before making the call.

The corresponding Objective-C snippet is shown below:
    
    
    [analytics group:@"<groupId>" traits:@{@"key": @"value"} options:[[RSSOptionBuilder new] build]];
    

> ![info](/docs/images/info.svg)
> 
> `RSSOptionBuilder` is an Objective-C–only helper class. It uses the builder pattern to create an `RSSOption` instance and lets you set custom context, configure integrations, and attach external IDs in a structured way.
    
    
    // Group event with groupId
    analytics.group(groupId: "some_group_id")
    
    // Group event with groupId and traits
    analytics.group(
        groupId: "group_id",
        traits: [
            "key-1": "value-1"
        ]
    )
    
    // Group event with groupId, traits and options
    analytics.group(
        groupId: "some_group_id",
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
    
    
    // Group event with groupId
    [analytics group:@"some_group_id"];
    
    // Group event with groupId and traits
    [analytics group:@"some_group_id"
             traits:@{
                 @"key-1": @"value-1"
             }];
    
    // Group event with groupId, traits and options
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
    
    [analytics group:@"some_group_id"
             traits:@{
                 @"key-1": @"value-1"
             }
            options:[optionBuilder build]];
    

### Method signature

The below table describes the `group` method signature in detail:

Field| Data type| Description  
---|---|---  
`groupId`| String| The group’s unique identifier in your database.  
`traits`| Traits| Contains traits associated with the group. They are added in the root level of the event.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `group` event sent from the iOS (Swift) SDK is shown below:
    
    
    analytics.group(
        groupId: "some_group_id",
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
    
    [analytics group:@"some_group_id"
             traits:@{
                 @"key-1": @"value-1"
             }
            options:[optionBuilder build]];