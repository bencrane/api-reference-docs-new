# Add the Consent Object to Event Payloads

Pass the consent category IDs as contextual information in events for server-side SDKs and other sources.

* * *

  * __5 minute read

  * 


This guide explains how to add the consent data to event payloads to implement the consent-based filtering logic (allow or block) on downstream destinations.

## Overview

Irrespective of the source or destination, RudderStack honors the consent ID values included in the `consentManagement` object in the context of event payloads. [Several RudderStack SDKs](<https://www.rudderstack.com/docs/data-governance/consent-management/support-matrix/>) provide native integrations with popular consent management providers and **automatically** add this data for you.

You can also add the consent data to the event payloads manually to apply the filtering logic (allow or block) for downstream destinations. You can use this approach for:

  * [Server-side SDKs](<https://www.rudderstack.com/docs/sources/overview/#server>)
  * SDKs that do not integrate natively with the consent management providers, for example, using Ketch with iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. .


Note that RudderStack supports this approach **only** for [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) destinations.

## Prerequisites

  1. Set up the source in the RudderStack dashboard.
  2. Connect the source to the required destination.
  3. Specify the consent category IDs in the [consent settings](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/#step-1-configure-consent-settings-for-destination>) for that destination.
  4. For a **Custom** consent management provider, you must also select the consent logic to be applied on the category IDs while resolving them against user consent data:


  * **AND** : Allows the events to go through to the destination only if the end user consents to **all** the categories corresponding to the category IDs specified in the dashboard.
  * **OR** : Allows the events to go to the destination if the end user consents to **at least one** of the categories corresponding to the category IDs specified in the dashboard.


## Implementation

Pass the consent data in your event’s `context` object.

The following snippets highlight some sample instrumentations to send the consent management data to **OneTrust** via various RudderStack sources:
    
    
    curl --location '<DATA_PLANE_URL>/v1/track' \
    --header 'Content-Type: application/json' \
    --data '{
      "type": "track",
      "event": "Product Purchased",
      "properties": {
        "name": "Sweatshirt",
        "price": 14.99
      },
      "context": {
        "consentManagement": {
          "allowedConsentIds": ["<category_id_1>", "<category_id_2>"], // Required
          "deniedConsentIds": ["<category_id_3>", "<category_id_4>"], // Required
          "provider": "oneTrust",
          "resolutionStrategy": "and" // Required for "oneTrust" / "ketch" / "iubenda"; Not required for "custom"
        },
        "traits": {
          "email": "alex@example.com.com",
          "plan": "Free Tier"
        },
        "library": {
          "name": "http"
        },
      },
      "originalTimestamp": "2024-11-30T14:31:15.032Z",
      "messageId": "39342c15-e6aa-4dd6-8882-5a04befd796a",
      "userId": "4hs323dsh421ddb",
      "anonymousId": "32cc095e-5b8f-43d0-b69c-c4623d1be5c7",
      "integrations": {
        "All": true
      },
      "sentAt": "2024-11-30T14:31:16.998Z"
    }'
    

You can pass consent data to your [Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) by setting it as custom contextual information, as shown:
    
    
    import com.rudderstack.sdk.kotlin.core.internals.models.RudderOption
    import kotlinx.serialization.json.JsonPrimitive
    import kotlinx.serialization.json.buildJsonObject
    import kotlinx.serialization.json.put
    import kotlinx.serialization.json.putJsonArray
    import kotlinx.serialization.json.putJsonObject
    
    val options = RudderOption(
        customContext = buildJsonObject {
            putJsonObject("consentManagement") {
                putJsonArray("allowedConsentIds") {         // Required
                    add(JsonPrimitive("<category_id_1>"))
                    add(JsonPrimitive("<category_id_2>"))
                }
                putJsonArray("deniedConsentIds") {          // Required
                    add(JsonPrimitive("<category_id_3>"))
                    add(JsonPrimitive("<category_id_4>"))
                }
                put("provider", "oneTrust")
                put("resolutionStrategy", "and") // Required for oneTrust / ketch / iubenda; omit for custom
            }
        }
    )
    
    analytics.track("Track Event", options = options)
    

You can pass consent data to your [iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) by setting it as custom contextual information, as shown:
    
    
    import RudderStackAnalytics
    
    let options = RudderOption(
        customContext: [
            "consentManagement": [
                "allowedConsentIds": ["<category_id_1>", "<category_id_2>"],    // Required
                "deniedConsentIds": ["<category_id_3>", "<category_id_4>"],     // Required
                "provider": "oneTrust",
                "resolutionStrategy": "and" // Required for oneTrust / ketch / iubenda; omit for custom
            ]
        ]
    )
    
    analytics.track(name: "Track Event", options: options)
    
    
    
    client.track({
      userId: "1hKOmRA4GRlm",
      event: "Item Viewed",
      properties: {
        revenue: 19.95,
        shippingMethod: "Premium",
      },
      context: {
        "allowedConsentIds": ["<category_id_1>", "<category_id_2>"], // Required
        "deniedConsentIds": ["<category_id_3>", "<category_id_4>"], // Required 
        "provider": "oneTrust", 
        "resolutionStrategy": "and" // Required for "oneTrust" / "ketch" / "iubenda"; Not required for "custom"
      }
    })
    

You can pass consent data to your iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. by setting it as custom contextual information, as shown:
    
    
    RSOption* option = [[RSOption alloc] init];
    [option putCustomContext:@{
        @"allowedConsentIds": @[@"<category_id_1>", @"<category_id_2>"], // Required
        @"deniedConsentIds": @[@"<category_id_3>", @"<category_id_4>"], // Required
        @"provider": @"oneTrust",
        @"resolutionStrategy": @"and", // Required for "oneTrust" / "ketch" / "iubenda"; Not required for "custom"
    } withKey:@"consentManagement"];
    [[RSClient sharedInstance] track:@"Track Event" properties:properties options:option];
    

See the [iOS (Obj-C) SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#using-putcustomcontext-method>) for more information on setting the custom context.

You can pass consent data to Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. by setting it as custom contextual information, as shown:
    
    
    val options = RudderOption()
        .putCustomContext(
            "consentManagement",
            mapOf(
                "allowedConsentIds" to listOf("<category_id_1>", "<category_id_2>"), // Required
                "deniedConsentIds" to listOf("<category_id_3>", "<category_id_4>"), // Required
                "provider" to "oneTrust",
                "resolutionStrategy" to "and" // Required for "oneTrust" / "ketch" / "iubenda"; Not required for "custom"
            )
        )
    
    rudderClient.track("Track event", properties, options)
    

See the [Android (Java) SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#using-putcustomcontext-method>) for more information on setting the custom context.

Note that:

  * RudderStack **requires** the `allowedConsentIds` and `deniedConsentIds` fields to successfully filter events based on user’s consent.
  * You must first configure the consent categories in the consent manager’s platform, then provide the category IDs in the `allowedConsentIds` and `deniedConsentIds` fields.
  * The consent category IDs are case-sensitive.
  * The consent IDs specified in the `allowedConsentIds` and `deniedConsentIds` must be the **union** of all the [consent settings](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/#configure-consent-settings>) specified for the destination in the dashboard. Otherwise, the consent setup will not work and RudderStack may not filter your events as expected.
  * The `resolutionStrategy` parameter refers to the consent logic applied on the category IDs while resolving them against user-specified consent. It is a **required** field if you set `provider` to `oneTrust`, `ketch`, or `iubenda`. The below table highlights the `resolutionStrategy` value that you **must** set for the specific consent management providers:

Consent management provider| `resolutionStrategy` value  
---|---  
OneTrust| `and`  
Ketch| `or`  
iubenda| `or`  
  
> ![warning](/docs/images/warning.svg)
> 
> The event filtering will not work correctly if you set a different consent logic for these providers.

  * `resolutionStrategy` is **not required** if you set `provider` to `custom`. RudderStack fetches the value for this parameter directly from the [consent logic](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/#specify-consent-logic>) specified in the RudderStack dashboard.