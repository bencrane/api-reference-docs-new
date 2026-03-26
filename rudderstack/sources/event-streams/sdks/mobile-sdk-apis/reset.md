# Reset API in Mobile SDKs

Learn about the reset API call in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This guide explains how to use the `reset` API in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a `reset` API that lets you clear the persisted data, for example, user ID and traits.

The SDK also does the following once you call the `reset` API:

  * Generates a new `anonymousId` (default behavior)
  * If [session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/session-tracking/>) is enabled, clears the current `sessionId` and generates a new one.


> ![info](/docs/images/info.svg)
> 
> If a mobile device mode integration plugin is present, then calling the `reset` API also triggers the integration’s `reset` API — **provided it is supported**.

The `reset` API supports the following invocations:

  * Default behavior: Clears all persisted user data
  * Selective reset: Choose specific data points to reset while preserving others


## Default behavior

By default, calling the `reset` API clears all persisted user data including user ID and traits, refreshes session information, and generates a new anonymous ID.
    
    
    analytics.reset()
    

The corresponding Java snippet is shown below:
    
    
    analytics.reset();
    
    
    
    analytics.reset()
    

The corresponding Objective-C snippet is shown below:
    
    
    [analytics reset];
    

## Selective reset

You can also use the `reset` API to choose which specific data components to reset while preserving others. This way, you have granular control over each component — you can regenerate the anonymous ID, clear the user ID, clear traits, or refresh session information, or preserve any of these values as per your requirement.

To perform a selective reset, the SDKs provide a `options` parameter that accepts a `ResetOptions` object with the following structure:
    
    
    val options = ResetOptions(
      entries = ResetEntries(
        anonymousId = true,
        userId = true,
        traits = true,
        session = true
      )
    )
    analytics.reset(options)
    

The corresponding Java snippet is shown below:
    
    
    ResetEntriesBuilder entriesBuilder = new ResetEntriesBuilder()
      .setAnonymousId(true)
      .setUserId(true)
      .setTraits(true)
      .setSession(true);
    ResetOptionsBuilder optionsBuilder = new ResetOptionsBuilder()
      .setEntries(entriesBuilder.build());
    analytics.reset(optionsBuilder.build());
    
    
    
    analytics.reset(options: ResetOptions(
      entries: ResetEntries(
        anonymousId: true,
        userId: true,
        traits: true,
        session: true
      )
    ))
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSResetEntriesBuilder *entriesBuilder = [RSSResetEntriesBuilder new];
    [entriesBuilder setAnonymousIdResetEntry:YES];
    [entriesBuilder setUserIdResetEntry:YES];
    [entriesBuilder setTraitsResetEntry:YES];
    [entriesBuilder setSessionResetEntry:YES];
    
    RSSResetOptionsBuilder *optionsBuilder = [RSSResetOptionsBuilder new];
    [optionsBuilder setEntries:[entriesBuilder build]];
    
    [analytics resetWithOptions:[optionsBuilder build]];
    

### `entries` parameters

The following table describes the parameters accepted by the `entries` object of `ResetOptions`:

Parameter| Description| Default value  
---|---|---  
`anonymousId`| Resets the anonymous user ID.| `true`  
`userId`| Resets the persisted user ID.| `true`  
`traits`| Resets the persisted user traits.| `true`  
`session`| Resets the current session information.| `true`  
  
> ![info](/docs/images/info.svg)
> 
> All entries in the `ResetOptions.entries` object are **optional**. If you do not specify any entry, the SDK sets its default value as described in the above table.

## Examples

This section provides examples of how to perform a selective reset by using the `reset` API with different `entries` parameters.

#### Reset all data except session information
    
    
    analytics.reset(ResetOptions(
      entries = ResetEntries(
        anonymousId = true,
        userId = true,
        traits = true,
        session = false
      )
    ))
    

The corresponding Java snippet is shown below:
    
    
    ResetEntriesBuilder entriesBuilder = new ResetEntriesBuilder()
      .setAnonymousId(true)
      .setUserId(true)
      .setTraits(true)
      .setSession(false);
    ResetOptionsBuilder optionsBuilder = new ResetOptionsBuilder()
      .setEntries(entriesBuilder.build());
    analytics.reset(optionsBuilder.build());
    
    
    
    analytics.reset(options: ResetOptions(
      entries: ResetEntries(
        anonymousId: true,
        userId: true,
        traits: true,
        session: false
      )
    ))
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSResetEntriesBuilder *entriesBuilder = [RSSResetEntriesBuilder new];
    [entriesBuilder setAnonymousIdResetEntry:YES];
    [entriesBuilder setUserIdResetEntry:YES];
    [entriesBuilder setTraitsResetEntry:YES];
    [entriesBuilder setSessionResetEntry:NO];
    
    RSSResetOptionsBuilder *optionsBuilder = [RSSResetOptionsBuilder new];
    [optionsBuilder setEntries:[entriesBuilder build]];
    
    [analytics resetWithOptions:[optionsBuilder build]];
    

#### Reset only session information
    
    
    analytics.reset(ResetOptions(
      entries = ResetEntries(
        anonymousId = false,
        userId = false,
        traits = false,
        session = true
      )
    ))
    

The corresponding Java snippet is shown below:
    
    
    ResetEntriesBuilder entriesBuilder = new ResetEntriesBuilder()
      .setAnonymousId(false)
      .setUserId(false)
      .setTraits(false)
      .setSession(true);
    ResetOptionsBuilder optionsBuilder = new ResetOptionsBuilder()
      .setEntries(entriesBuilder.build());
    analytics.reset(optionsBuilder.build());
    
    
    
    analytics.reset(options: ResetOptions(
      entries: ResetEntries(
        anonymousId: false,
        userId: false,
        traits: false,
        session: true
      )
    ))
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSResetEntriesBuilder *entriesBuilder = [RSSResetEntriesBuilder new];
    [entriesBuilder setAnonymousIdResetEntry:NO];
    [entriesBuilder setUserIdResetEntry:NO];
    [entriesBuilder setTraitsResetEntry:NO];
    [entriesBuilder setSessionResetEntry:YES];
    
    RSSResetOptionsBuilder *optionsBuilder = [RSSResetOptionsBuilder new];
    [optionsBuilder setEntries:[entriesBuilder build]];
    
    [analytics resetWithOptions:[optionsBuilder build]];
    

#### Reset only user ID and traits
    
    
    analytics.reset(ResetOptions(
      entries = ResetEntries(
        anonymousId = false,
        userId = true,
        traits = true,
        session = false
      )
    ))
    

The corresponding Java snippet is shown below:
    
    
    ResetEntriesBuilder entriesBuilder = new ResetEntriesBuilder()
      .setAnonymousId(false)
      .setUserId(true)
      .setTraits(true)
      .setSession(false);
    ResetOptionsBuilder optionsBuilder = new ResetOptionsBuilder()
      .setEntries(entriesBuilder.build());
    analytics.reset(optionsBuilder.build());
    
    
    
    analytics.reset(options: ResetOptions(
      entries: ResetEntries(
        anonymousId: false,
        userId: true,
        traits: true,
        session: false
      )
    ))
    

The corresponding Objective-C snippet is shown below:
    
    
    RSSResetEntriesBuilder *entriesBuilder = [RSSResetEntriesBuilder new];
    [entriesBuilder setAnonymousIdResetEntry:NO];
    [entriesBuilder setUserIdResetEntry:YES];
    [entriesBuilder setTraitsResetEntry:YES];
    [entriesBuilder setSessionResetEntry:NO];
    
    RSSResetOptionsBuilder *optionsBuilder = [RSSResetOptionsBuilder new];
    [optionsBuilder setEntries:[entriesBuilder build]];
    
    [analytics resetWithOptions:[optionsBuilder build]];