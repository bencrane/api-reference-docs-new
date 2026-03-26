# OneTrust Consent Management

Integrate RudderStack with the OneTrust consent management platform.

* * *

  * __less than a minute

  * 


[OneTrust](<https://www.onetrust.com/>) is a popular consent management platform that provides data governance, privacy management, and security solutions to thousands of businesses worldwide.

This section will help you integrate OneTrust consent management with RudderStack.

## How the integration works

RudderStack supports native OneTrust integration with the web ([JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)) and the mobile ([Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) and [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)) SDKs.

See the below guides for the implementation details:

  * [OneTrust Consent Management for Web](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>)
  * [OneTrust Consent Management for Android](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/android/>)
  * [OneTrust Consent Management for iOS](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/ios/>)


> ![info](/docs/images/info.svg)
> 
> For the other SDKs, you can implement OneTrust consent-based event filtering for **cloud mode** destinations, by adding the `consentManagement` object within the context of the event payload.
> 
> See [Add the Consent Object to Event Payloads](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) for more information.