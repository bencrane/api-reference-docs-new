# Session Tracking FAQ

Answers to the generally asked questions related to RudderStack’s session tracking feature.

* * *

  * __3 minute read

  * 


This section answers the commonly asked questions related to RudderStack’s session tracking feature.

## General

#### Do RudderStack’s server-side SDKs support automatic session tracking?

No, the server-side SDKs do not support automatic session tracking.

#### How does RudderStack determine the session ID?

RudderStack sets the session ID (`sessionId`) as the current time in Unix epoch timestamp format.

#### Does RudderStack attach any user information to the `sessionId`?

RudderStack **does not** attach any user information to the `sessionId`. This is so that a user cannot be traced back or identified only with the `sessionId`.

#### How do I correctly count the number of sessions for a given user?

To correctly count the number of sessions, you can pair `sessionId` with the user’s anonymous ID (`anonymousId`) or user ID (`userId`) for identified users.

#### What happens to the existing session if I call the `reset()` API?

If you call the [`reset()`API](<https://www.rudderstack.com/docs/event-spec/standard-events/>), RudderStack ends the existing session and generates a new one.

#### Which RudderStack APIs contribute to a session’s activeness?

The following RudderStack APIs contribute to a session’s activeness:

  * `identify`
  * `track`
  * `page`
  * `group`
  * `screen`
  * `alias`


#### What happens if I manually trigger a new session during an active session?

If you call the `startSession()` API while automatic session tracking is enabled, RudderStack ends the existing session and starts a new manual session.

## JavaScript SDK

#### What happens if I set `timeout` to 0 or less than 10 seconds?

If you set the session’s `timeout` to 0, RudderStack disables automatic session tracking. This is because upon setting the `timeout` to 0, RudderStack creates a new session for each event. As such, enabling automatic session tracking serves no purpose.

If your session `timeout` is less than 10 seconds, RudderStack gives a caution but proceeds with the session tracking.

#### What happens I close a website tab and reopen it after some time?

If the time between the last event API invocation or SDK initialization before closing a browser tab and reopening a new one is less than the session timeout (default is 30 minutes), then RudderStack continues the same session. Otherwise, it starts a new session.

#### Does the existing session end if an `identify` call is made with a different `userId`?

If you identify a user with a new `userId` in an existing session, RudderStack triggers a `reset()` call. This ends the existing session and generates a new one.

> ![info](/docs/images/info.svg)
> 
> This functionality is applicable for both automatic and manual session tracking.

## Mobile SDKs

#### What is the scope of persistence in case of automatic session tracking?

When an application is closed completely and launched from scratch, RudderStack checks if the inactivity timeout of the previous automatically tracked session has elapsed. If yes, RudderStack creates a new session, otherwise, it continues the previous session.

#### What is the scope of persistence in case of manual session tracking?

The scope of manual session tracking depends on whether the automatic session tracking feature is enabled.

  * If automatic session tracking is **enabled** : On the next app launch (from scratch), RudderStack clears the manual session even if [`endSession()`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/manual-session-tracking/>) is not called and generates a new **automatic** session.
  * If automatic session tracking is **disabled** : On the next app launch, the manual session will still be active and cleared only when the user ends the session using `endSession()`.


#### Where does RudderStack store the session tracking information?

For mobile SDKs,RudderStack stores the session tracking information in the following locations:

Platform| Class  
---|---  
Android| [`SharedPreferences`](<https://developer.android.com/reference/android/content/SharedPreferences>)  
iOS| [`UserDefaults`](<https://developer.apple.com/documentation/foundation/userdefaults>)