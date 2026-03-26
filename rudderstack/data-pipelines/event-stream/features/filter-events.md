# Event Filtering Techniques

Filter event data before sending it to your destinations.

* * *

  * __less than a minute

  * 


RudderStack provides different techniques to filter your events before sending them to your specified destinations:

Technique| Description| Connection mode| Applicable to  
---|---|---|---  
[User Transformations](<https://www.rudderstack.com/docs/transformations/overview/>)| Create transformations to filter events by name, type, or any other specific fields.| Cloud mode| 

  * [Cloud Apps](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/>)
  * [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>)

  
[Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>)| Allowlist or denylist events while setting up the destination in the RudderStack dashboard.| Device mode| [All SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>)  
[Sending events to selective destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>)| Send events only to selective destinations by excluding other device mode integrations.| Device mode| [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)  
[Filtering selective destinations](<https://www.rudderstack.com/docs/user-guides/how-to-guides/how-to-filter-selective-destinations/>)| Instruct RudderStack to block or send events to selective destinations.| Cloud mode and device mode| 

  * [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>)
  * [Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#enablingdisabling-events-for-specific-destinations>)
  * [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#enablingdisabling-events-for-specific-destinations>)