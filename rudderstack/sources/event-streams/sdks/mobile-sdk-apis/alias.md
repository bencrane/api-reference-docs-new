# Alias API in Mobile SDKs

Learn about the alias API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide explains how to use the `alias` API in the [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide an [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) API that lets you merge different identities of a known user.

Note that:

  * You can use the `alias` event only for merging user identities. It **does not** update the user’s traits or other common properties.
  * RudderStack supports sending `alias` events only to certain downstream destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.


## Android (Kotlin)

The `alias` method definition in the Android (Kotlin) SDK is as follows:
    
    
    analytics.alias(
        newId = "<newId>",
        previousId = "<previousId>",
        options = RudderOption()
    )
    

The corresponding Java snippet is shown below:
    
    
    analytics.alias("<newId>", "<previousId>", new RudderOption());
    
    
    
    // Alias event with newId
    analytics.alias(newId = "<newId>")
    
    // Alias event with newId and previousId
    analytics.alias(
        newId = "<newId>",
        previousId = "<previousId>"
    )
    
    // Alias event with newId and options
    analytics.alias(
        newId = "<newId>",
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
                ExternalId(type = "<id_type>", id = "<value>")
            )
        )
    )
    

### Method signature

The below table describes the `alias` method signature in detail:

Field| Data type| Description  
---|---|---  
`newId`| String| New user identifier (`userId`) associated with the user.  
`previousId`| String| The old user identifier.  
  
**Note** : If not provided explicitly, the SDK automatically populates this field with the current `userId` or `anonymousId`.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `alias` event sent from the Android (Kotlin) SDK is shown below:
    
    
    analytics.alias(
        newId = "1hKOmRA4GRlm",
        previousId = "156K7m214GR2X",
        options = RudderOption()
    )
    
    
    
    analytics.alias("1hKOmRA4GRlm", "156K7m214GR2X", new RudderOption());
    

## iOS (Swift)

The `alias` method definition in the iOS (Swift) SDK is as follows:
    
    
    analytics.alias(
        newId: "<newId>",
        previousId: "<previousId>",
        options: RudderOption()
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to include the `import RudderStackAnalytics` statement before making the call.

The corresponding Objective-C snippet is shown below:
    
    
    [analytics alias:@"<newId>" previousId:@"<previousId>" options:[[RSSOptionBuilder new] build]];
    

> ![info](/docs/images/info.svg)
> 
> `RSSOptionBuilder` is an Objective-C–only helper class. It uses the builder pattern to create an `RSSOption` instance and lets you set custom context, configure integrations, and attach external IDs in a structured way.
    
    
    // Alias event with newId
    analytics.alias(newId: "Alias ID 1")
    
    // Alias event with newId and previousId
    analytics.alias(
        newId: "Alias ID 1",
        previousId: "Explicit Previous User ID 1"
    )
    
    // Alias event with newId and options
    analytics.alias(
        newId: "Alias ID 1",
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
    
    
    // Alias event with newId
    [analytics alias:@"Alias ID 1"];
    
    // Alias event with newId and previousId
    [analytics alias:@"Alias ID 1" previousId:@"Explicit Previous User ID 1"];
    
    // Alias event with newId and options
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
    
    [analytics alias:@"Alias ID 1" options:[optionBuilder build]];
    

### Method signature

The below table describes the `alias` method signature in detail:

Field| Data type| Description  
---|---|---  
`newId`| String| New user identifier (`userId`) associated with the user.  
`previousId`| String| The old user identifier.  
  
**Note** : If not provided explicitly, the SDK automatically populates this field with the current `userId` or `anonymousId`.  
`options`| RudderOption| Additional event options.  
  
### Example

A sample `alias` event sent from the iOS (Swift) SDK is shown below:
    
    
    analytics.alias(
        newId: "Alias ID 1",
        previousId: "Explicit Previous User ID 1",
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
    
    [analytics alias:@"Alias ID 1"
             previousId:@"Explicit Previous User ID 1"
                options:[optionBuilder build]];