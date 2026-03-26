# Configure Session Cutoff in JavaScript SDK

Learn how to use the session cutoff feature in the JavaScript SDK.

* * *

  * __3 minute read

  * 


This guide explains how to configure the session cutoff feature in the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

## Overview

The JavaScript SDK provides a **session cutoff** feature that provides an additional layer of session management by automatically resetting user sessions when they exceed a configured maximum duration. This feature works alongside the standard session timeout mechanism (configurable by the [`timeout` option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/#when-does-a-session-become-inactive>)) to enforce stricter session boundaries.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The session cutoff feature only works when [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/>) is enabled.
>   * If enabled, this feature forcibly resets a user session if it exceeds the configured cutoff duration, **even if** the session timeout duration (configurable by the [`timeout` option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/#when-does-a-session-become-inactive>)) has not elapsed.
> 


## Compatibility

  * **SDK version requirements** : The session cutoff feature requires JavaScript SDK v3.18.0 or later. Make sure all instances of the SDK across your application are using compatible versions.

  * **Cookie compatibility** : The session cutoff feature adds new information to the `rl_session` cookie. This creates important compatibility considerations:

    * **Do not mix SDK versions** : Do not use the compatible SDK version alongside older versions (v1.1 or earlier v3 builds) on websites that share cookies.
    * **Older SDK behavior** : Older SDK versions do not recognize the new session cutoff data and will overwrite or remove it, leading to inconsistent session cutoff behavior.
    * **Cross-domain considerations** : If your application spans multiple domains that share cookies, make sure all domains use compatible SDK versions.


> ![success](/docs/images/tick.svg)
> 
> **Migration strategy**
> 
> If you need to upgrade your SDK version to use the session cutoff feature, RudderStack recommends updating all SDK instances simultaneously rather than implementing a gradual rollout across different parts of your application.

## Configure session cutoff

You can configure session cutoff during the [SDK initialization](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) using the `cutOff` option under the `sessions` object.

A sample configuration for a 12 hour cutoff duration is as follows:
    
    
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
    

Note that the session cutoff feature is active only if:

  * `sessions.autoTrack` is `true`, that is, automatic session tracking is enabled.
  * `sessions.cutOff.enabled` is `true`.


### Configuration options

The following table highlights the configuration options for the `cutOff` parameter:

Option| Type| Description  
---|---|---  
`enabled`| Boolean| Determines whether to enable the session cutoff feature.  
  
**Default value:** `false`  
`duration`| Number| The duration (in milliseconds) after which a session is forcibly reset, **even if** the session hasn’t timed out. If not specified, the SDK logs a console warning and uses the default value.  
  


> ![warning](/docs/images/warning.svg)The cutoff duration must be greater than or equal to the [session timeout](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/#when-does-a-session-become-inactive>) (defaults to 30 minutes). Otherwise, the SDK automatically disables the session cutoff feature and logs a warning.

  
**Default value:** `12 * 60 * 60 * 1000` (12 hours)  
  
## Considerations

Consider the following important points before implementing the session cutoff feature:

  * **Default behavior** : This feature is disabled by default. You must explicitly enable it by setting `sessions.cutOff.enabled` to `true` in your configuration.
  * **Session tracking dependency** : Session cutoff only works when [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/>) is enabled.
  * **Session duration requirements** : The cutoff duration must be longer than your configured [session timeout](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/#when-does-a-session-become-inactive>). If you set a cutoff duration that’s shorter than the session timeout (defaults to 30 minutes), then the SDK automatically disables the session cutoff feature and logs a warning.
  * **Data storage** : Cutoff data is stored as part of the existing `rl_session` cookie, so it follows the same storage and privacy considerations as your current session management.
  * **Reset behavior** : When you call the `reset()` API, all session-related information is cleared, including cutoff data.