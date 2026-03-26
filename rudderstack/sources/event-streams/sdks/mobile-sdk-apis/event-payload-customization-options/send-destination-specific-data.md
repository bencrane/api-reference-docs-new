# How to Send Destination-specific Data in Event Payload

Learn how to use the `integrations` object to send destination-specific configuration or data in the event payload.

* * *

  * __2 minute read

  * 


This guide demonstrates how to use the [`integrations`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#the-integrations-field>) field of the `RudderOption` instance to send destination-specific configuration or data in the event payload.

## Overview

You can set the [`<Destination>`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations-options>) parameter of the `integrations` field to an object — and use this object to send any specific configuration or data that you want to send to that destination in both [cloud and device modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * When you set the `<Destination>` parameter to an object, the SDKs (Android (Kotlin) and iOS (Swift)) automatically assumes this parameter to be `true`.
>   * The SDKs do not persist the information set using the `integrations` field across different events. Therefore, you must pass this parameter every time you want to send destination-specific data within an event payload.
> 


## Send destination-specific configuration or data

In the following example, the `integrations` object is used to specify a **Mailjet** configuration that removes the user from a Mailjet list (with the ID `13314el9Z`).
    
    
    analytics.identify(
        userId = "1hKOmRA4GRlm",
        traits = buildJsonObject {
            put("firstName", "Alex")
            put("lastName", "Keener")
        },
        options = RudderOption(
            externalIds = listOf(
                ExternalId(type = "listId", id = "13314el9Z")
            ),
            integrations = buildJsonObject {
                put("Mailjet", buildJsonObject {
                    put("Action", "remove")
                })
            }
        )
    )
    

The corresponding Java snippet is shown below:
    
    
    String userId = "1hKOmRA4GRlm";
    
    Map<String, Object> traits = new HashMap<>();
    traits.put("firstName", "Alex");
    traits.put("lastName", "Keener");
    
    List<ExternalId> externalIds = new ArrayList<>();
    externalIds.add(new ExternalId("listId", "13314el9Z"));
    
    Map<String, Object> mailjetConfig = new HashMap<>();
    mailjetConfig.put("Action", "remove");
    Map<String, Object> integrations = new HashMap<>();
    integrations.put("Mailjet", mailjetConfig);
    
    RudderOption option = new RudderOptionBuilder()
            .setIntegrations(integrations)
            .setExternalId(externalIds)
            .build();
    
    analytics.identify(userId, traits, option);
    
    
    
    analytics.identify(
        userId: "User123",
        traits: [
            "firstName": "Alex",
            "lastName": "Keener"
        ],
        options: RudderOption(
            integrations: [
                "Mailjet": [
                    "Action": "remove"
                ]
            ],
            externalIds: [
                ExternalId(type: "listId", id: "13314el9Z")
            ]
        )
    )
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSOptionBuilder *optionBuilder = [RSSOptionBuilder new];
    
    [optionBuilder setIntegrations:@{
        @"Mailjet": @{@"Action": @"remove"}
    }];
    
    [optionBuilder setExternalIds:@[
        [[RSSExternalId alloc] initWithType:@"listId" id:@"13314el9Z"]
    ]];
    
    [analytics identify:@"User123"
               traits:@{
                   @"firstName": @"Alex",
                   @"lastName": @"Keener"
               }
              options:[optionBuilder build]];
    

After making the above call, the external ID information gets attached to the `context.externalId` field and `integrations` information gets attached to the `integrations` key at the root level. The final payload will look as follows:
    
    
    {
      //.....
      "context": {
        //......
        "externalId": [{
          "id": "13314el9Z",
          "type": "listId"
        }],
        //......
      }
      //.....
      "integrations": {
        "All": false,
        "Mailjet": true
      },
      //.....
    }