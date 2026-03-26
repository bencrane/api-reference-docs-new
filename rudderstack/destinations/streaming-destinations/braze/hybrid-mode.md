# Braze Hybrid Mode Integration

Send events to Braze in RudderStack hybrid mode.

* * *

  * __3 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Hybrid mode is not recommended** due to potential race conditions that can create split user profiles in Braze.
> 
> Consider using [device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/>) or [cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/cloud-mode/>) instead.

This guide explains how to send events to Braze in [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>).

## Overview

You can use RudderStack’s [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) to send events from the following sources to Braze:

  * [JavaScript (web)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
  * [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)
  * [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>)
  * [Android (Java) — Legacy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)


## Race condition limitations

When cloud mode events reach Braze earlier than the `setAlias` call via the Braze SDK (and no `identify` calls are made), it can lead to split profiles for a single user.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * This race condition is particularly problematic when hybrid mode is used without an `identify` call at the beginning of the user session.
>   * RudderStack tries to flush the Braze `setAlias` calls as soon as possible — however, this approach **does not** eliminate the possibility of split user profiles entirely.
> 


**Click here to read the technical details**  
This race condition occurs because:  
  


  * **Cloud events create an alias-only profile** : RudderStack sends events through the cloud mode, creating a profile with the `rudder_id:<rudder_anonymous_id>` alias.
  * **Braze SDK creates a separate anonymous profile** : The Braze SDK creates a Braze-anonymous profile when the session opens.
  * **Alias setting fails** : The Braze SDK attempts to set the `rudder_id:<rudder_anonymous_id>` alias, but since an alias-only-profile with the same alias already exists, Braze skips the `setAlias` call entirely.
  * **Result** : Two separate profiles exist for the same user, leading to data fragmentation and inaccurate analytics.


### Recommended alternatives

Instead of using hybrid mode, consider these alternatives:

  * **Use device mode** if you need features like push notifications
  * **Use cloud mode** if you do not need device-specific features, for better reliability and data governance capabilities.


## When to use hybrid mode

> ![warning](/docs/images/warning.svg)
> 
> Use hybrid mode only in specific scenarios where you can tolerate potential profile splitting issues.

Consider using hybrid mode when you:

  * Need device mode features like push notifications and in-app messaging that require the Braze SDK.
  * Can tolerate inflated user profiles as a trade-off for accessing both cloud and device mode features.
  * Want to leverage RudderStack features available in cloud mode like [Data Governance](<https://www.rudderstack.com/docs/data-governance/>) and [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>).


> ![info](/docs/images/info.svg)
> 
> In hybrid mode, RudderStack sends all the user-generated events to Braze through their REST API and **does not process** them on the client-side.

### Workflow

When you select hybrid mode to send events to Braze, RudderStack:

  * Initializes the Braze SDK.
  * Sends all the user-generated events (`identify`, `track`, `page`, `screen`, `group`, and `alias`) to Braze through [cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/>) and blocks them from being sent via device mode.
  * Sends the auto-generated events (in-app messages, push notifications that require the Braze SDK) by leveraging [device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/>).


## Mobile source setup

  1. Select the hybrid mode option while connecting your mobile source to the Braze destination.

[![Braze hybrid mode connection setting](/docs/images/event-stream-destinations/braze-hybrid-mode.webp)](</docs/images/event-stream-destinations/braze-hybrid-mode.webp>)

  2. [Add the Braze integration to your project](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/device-mode/#add-braze-integration>).


## Web source setup

  1. Select the hybrid mode option while connecting your web source to the Braze destination.

[![Braze hybrid mode connection setting for web](/docs/images/event-stream-destinations/braze-hybrid-mode-web.webp)](</docs/images/event-stream-destinations/braze-hybrid-mode-web.webp>)

  2. Configure the [Web SDK settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#web-sdk-settings>) to receive data in Braze correctly.