# Consent Management Support Matrix

Details on the availability of RudderStack’s consent management feature across different sources.

* * *

  * __less than a minute

  * 


This guide details RudderStack’s consent management integration support across different SDKs and sources.

## Pre-consent user tracking

Pre-consent user tracking is only available in the [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

## Integrations support

Irrespective of the source or destination, RudderStack honors the consent ID values included in the `consentManagement` object in the context of event payloads. Several RudderStack SDKs provide native integrations with popular consent management providers and **automatically** add this data for you.

You can also add the consent data to the event payloads [manually](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) to apply the filtering logic (allow or block) on downstream destinations (this is required for some SDKs). Note that RudderStack supports this approach **only** for [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) destinations.

The following table lists the SDKs and integrations that automatically append consent data to your events:

## Support matrix

Source| OneTrust| Ketch| iubenda| Custom  
---|---|---|---|---  
[JavaScript SDK (v3)](<https://rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)| __| __| __| __  
[JavaScript SDK](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/>)  
  
(older versions)| __| __| Through[event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)  
Deprecated|  __| Through[event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)  
Deprecated|  __| Through[event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>)| Through [event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[iOS (Swift) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>)| Through [event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[Server-side SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/#server>)| Through [event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)  
[HTTP Source](<https://www.rudderstack.com/docs/sources/event-streams/http/>)| Through [event context](<https://rudderstack.com/docs/data-governance/consent-management/passing-consent/>)