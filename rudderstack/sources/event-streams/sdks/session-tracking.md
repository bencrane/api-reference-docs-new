# Session Tracking in RudderStack SDKs

Track user sessions from RudderStack web and mobile sources.

* * *

  * __3 minute read

  * 


This guide explains the session tracking feature in RudderStack.

## Overview

RudderStack provides a **session tracking** feature that helps you track user sessions and gather event tracking metrics. You can use this feature to:

  * Combine events with session metadata to better understand the user’s product journey and analyze their behavior.
  * Use the insights to identify problems and optimization opportunities in your product workflow.


#### What is a session?

A session is a group of user interactions with your website or mobile app within a given time frame. It is usually triggered when a user opens a mobile app or a website in their browser and ends after a particular period of inactivity.

> ![info](/docs/images/info.svg)
> 
> A single session can contain multiple page views or screen views, events, social interactions, and ecommerce transactions.

## Session tracking in RudderStack SDKs

The following RudderStack SDKs support the session tracking feature:

RudderStack SDK| Minimum supported version  
---|---  
[JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)| 

  * v1: **1.16.0** (CDN)
  * v1.1: **2.15.0** (CDN & NPM)

  
[Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)| **v1.7.0**  
[iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)| 

  * [v1](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>): **v1.7.0**
  * [v2](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/ios-v2/>): **v2.3.0**

  
[React Native](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>)| **v1.8.0**  
[Flutter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)| **v2.7.0**  
  
You can expect the following properties in your event’s [context object](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) object when session tracking is enabled:

Property| Type| Description  
---|---|---  
`sessionId`| Number| The session ID.  
  
See the [FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/faq/#how-does-rudderstack-determine-the-session-id>) guide for more information on how RudderStack calculates `sessionId` .  
`sessionStart`| Boolean| Present in the first event, indicating the start of the session.  
  
> ![warning](/docs/images/warning.svg)
> 
> Note the following:
> 
>   * RudderStack’s [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/>) feature overrides any `sessionId` present in the event’s `context` object.
>   * Make sure to send any other session-related information within the event’s `traits` or `properties` object.
> 


## Session tracking types

The RudderStack SDKs mentioned above support two types of session tracking:

Type| Description  
---|---  
[Automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/>)| RudderStack automatically determines the start and end of a session based on the inactivity time configured in the SDK.  
[Manual session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/manual-session-tracking/>)| You can manually start and end a session using the SDK methods.  
  
## Supported downstream tools

The RudderStack SDKs support sending the `sessionId` and `sessionStart` fields to all [cloud](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) and [warehouse](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) destinations, **within the event’s`context`**.

It is important to note the following:

  * RudderStack passes the `sessionId` to the subsequent events in the `context.sessionId` field.
  * RudderStack sets the `context.sessionStart` field to `true` in the first event to indicate the start of the session.


RudderStack maps `sessionId` to specific fields **only** in case of the following two destinations:

Destination| Notes  
---|---  
[Amplitude](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/>)| RudderStack maps `sessionId` to Amplitue’s `session_id` field. For more information, see the [Amplitude documentation](<https://www.docs.developers.amplitude.com/analytics/apis/http-v2-api/#keys-for-the-event-argument:~:text=to%20occur%20simultaneously.-,session_id,-Optional.%20Long.%20The%22>).  
[Mixpanel](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/>)| 
* RudderStack passes the `$session_id` under the event properties.
  

* Mixpanel doesn’t have a specific field for `$session_id` but you can use this field in the reports.  
  
## FAQ

See the [Session Tracking FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/faq/>) guide for answers to some commonly-asked questions on session tracking.