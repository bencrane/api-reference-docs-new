# Automatic Session Tracking in JavaScript SDK

Learn about the automatic session tracking feature in the JavaScript SDK.

* * *

  * __5 minute read

  * 


This guide explains the automatic session tracking feature in the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

## Overview

The JavaScript SDK supports automatic session tracking with the following capabilities:

  * The SDK automatically tracks user sessions by default and considers the [SDK initialization](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) as the start of a user session.

  * By default, each session remains active for 30 minutes of inactivity. However, you can customize the session timeout period and disable automatic tracking, if needed.

  * The SDK generates a unique `sessionId` for each session. You can retrieve the current session ID using the `getSessionId()` API.

  * The SDK automatically resets the session in following cases:

    * After the timeout duration has elapsed without any activity
    * When you call the `reset()` API
    * When you identify a user with a new `userId`
  * The SDK includes a `sessionStart: true` parameter in the context for the first event of each session.


See the Session tracking flow section for a visual workflow of automatic session tracking in the JavaScript SDK.

## Manage automatic session tracking

By default, the JavaScript SDK automatically tracks user sessions and assigns a unique session ID (`sessionId`).

> ![info](/docs/images/info.svg)
> 
> RudderStack sets the session ID as the current time in Unix epoch timestamp format. So, it is not universally unique.
> 
> To uniquely identify events of a user in a session, use a combination of session ID and user ID (`userId`) / anonymous user ID (`anonymousId`).

RudderStack considers the [SDK initialization](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) as the start of a user session.

You can disable automatic session tracking by setting the `sessions.autoTrack` load option to `false`, as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sessions: {
        autoTrack: false,  // Disables automatic session tracking
      },
      ...<otherLoadOptions>
    });
    

### When does a session become inactive?

By default, a session is active until **30 minutes of inactivity** have elapsed since the last received event.

> ![info](/docs/images/info.svg)
> 
> **What constitutes inactivity?**
> 
> The SDK treats the following as activity:
> 
>   * Tracking API calls for events
>   * `load` (when the SDK is initialized) and `reset` API calls
> 

> 
> The SDK **does not** treat the following as activity:
> 
>   * Other API calls like `getUserId`, `setAnonymousId`, etc.
>   * Page scrolls or click events on the web page
> 


Whenever RudderStack receives a new event, it checks if the inactivity period has elapsed. If yes, it starts a new session with a new `sessionId`. Otherwise, it continues the previous session.

Every time a new event is generated (`track`, `page`, `identify`, etc.), the SDK resets the session expiration time by adding the configured `timeout` (default 30 minutes) to the last received event’s [`timestamp`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#clock-skew-considerations>).

You can also adjust the inactivity period using the `timeout` load option. The following snippet highlights the use of the `timeout` option to set a custom session timeout of 10 minutes:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sessions: {
        autoTrack: true,
        timeout: 10 * 60 * 1000,  // 10 min in milliseconds
      },
      ...<otherLoadOptions>
    });
    

### When does a session reset?

The JavaScript SDK resets and starts a new session in the following cases:

  * When RudderStack receives a new event after the session inactivity period has elapsed, as explained above.
  * When you call the Reset API.
  * If you identify a user with a new `userId` in an existing session. RudderStack triggers a `reset()` call that ends the existing session and generates a new one with a different `sessionId`.


## Retrieve the session ID

The JavaScript SDK provides a `getSessionId` method to fetch the current session’s ID. Note that this method returns a `null` value if the session ID is unavailable or the session is inactive.

The following snippet highlights the use of the `getSessionId` method to fetch the current session ID:
    
    
    rudderanalytics.getSessionId();
    

## Configure session cutoff

The JavaScript SDK provides a [Session Cutoff](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/configure-session-cutoff/>) feature that provides an additional layer of session management by automatically resetting user sessions when they exceed a configured maximum duration. This feature works alongside the standard session timeout mechanism to enforce stricter session boundaries.

When enabled, the session cutoff feature forcibly resets a user session if it exceeds the configured cutoff duration, **even if** the session hasn’t timed out due to inactivity. This helps ensure that sessions don’t persist indefinitely and provides better control over user session lifecycles.

> ![info](/docs/images/info.svg)
> 
> The cutoff duration is independent of session timeout settings (configurable by the `timeout` option). While session timeout resets sessions due to inactivity, session cutoff resets sessions based on total elapsed time since the session began.

A sample configuration for a 12 hour session cutoff duration is as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sessions: {
        autoTrack: true,
        cutOff: {
          enabled: true, // Optional; set to true to enable the feature
          duration: 12 * 60 * 60 * 1000 // Optional; 12 hours in milliseconds (default)
        }
      },
      ...
      // Other load options
    
    });
    

See [Configure Session Cutoff in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/configure-session-cutoff/>) for more information on using this feature.

## Session tracking flow

The automatic session tracking flow (when enabled) in the JavaScript SDK is as follows:

  1. During the initialization, the SDK checks for an existing user session. If no valid session exists, it creates a new session. Otherwise, the SDK proceeds with the existing session.
  2. Upon receiving an event, the SDK fetches the `sessionId`. If no valid `sessionId` is found, it creates a new session and returns the `sessionId`. If this is the first event of the session, the SDK also sends another parameter in the context called `sessionStart: true`.


> ![info](/docs/images/info.svg)
> 
> See the [Session Tracking FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/faq/#how-does-rudderstack-determine-the-session-id>) guide for more information on how RudderStack calculates `sessionId`.

  3. The SDK records the user events and the session is active until the `timeout` (default 30 minutes of inactivity) period has elapsed since the last received event. If yes, it starts a new session with a new `sessionId`.
  4. Otherwise, the SDK updates the session expiration time by adding the last current timestamp to the `timeout` period (default 30 minutes).

[![Session tracking in JavaScript SDK](/docs/images/event-stream-sources/session-tracking-web-new.webp)](</docs/images/event-stream-sources/session-tracking-web-new.webp>)

## FAQ

See the [Session Tracking FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/faq/#javascript-sdk>) guide for answers to some commonly-asked questions on session tracking in the JavaScript SDK.