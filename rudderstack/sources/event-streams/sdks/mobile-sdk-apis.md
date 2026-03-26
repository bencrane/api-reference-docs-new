# Mobile SDK APIs

Send events by leveraging the Android (Kotlin) and iOS (Swift) SDK APIs.

* * *

  * __less than a minute

  * 


This section walks you through the different APIs provided by the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs:

## Event APIs

The [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs support the following standard event APIs in accordance with the [RudderStack Event Spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>):

API| Description  
---|---  
[Track](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/track/>)| Tracks user actions along with their associated properties.  
[Identify](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/identify/>)| Identifies a user and associate them to their actions.  
[Screen](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/screen/>)| Records whenever user views their mobile screen and captures any relevant information about the screen.  
[Group](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/group/>)| Links an identified user with a group and record any traits associated with that group.  
[Alias](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/alias/>)| Merges different identities of a known user.  
[Reset](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/reset/>)| Clears the user ID and traits.  
  
## Other APIs

In addition to the standard event APIs, the Android (Kotlin) and iOS (Swift) SDKs also support the below APIs for specific use cases:

API| Description  
---|---  
[Device Mode Integration APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/integration-apis/>)| Access destination instances and register callbacks for device mode integrations.  
[User Identity APIs](<>)| Retrieves the user ID, anonymous ID, and user traits persisted by the SDK.  
[Flush API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/flush-api/>)| Manually flushes any events stored in the SDK.  
[Logging APIs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/logging-apis/>)| Lets you monitor and debug the SDK’s behavior with fine-grained control.  
[Shutdown API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/shutdown/>)| Stops all the operations associated with the SDK and frees up resources.