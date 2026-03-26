# Autotrack Page View Metrics using JavaScript SDK

> Version: Latest (v3)v1.1

# Autotrack Page View Metrics using JavaScript SDK

Use the JavaScript SDK to autotrack page view metrics like time spent by user on a page.

* * *

  * __3 minute read

  * 


This guide explains the autotracking feature of the JavaScript SDK that helps you get visibility into various page view metrics, including the time spent by the user on a web page.

## Overview

When you enable the autotracking feature, the JavaScript SDK provides two main capabilities:

  1. **Page view ID tracking** : `context.autoTrack.page.pageViewId` is automatically added to all events (including `track`, `page`, `identify`, and `group` events) sent from the page. This allows you to tie all events to a single page visit using the unique page view ID. This works regardless of whether Beacon is enabled.

  2. **Page Unloaded event** : If Beacon is enabled, the JavaScript SDK automatically fires a `track` event called `Page Unloaded` whenever a page unloads, that is, when the browser or tab is closed, the page is reloaded, or the user navigates to a different tab.


Each `Page Unloaded` event contains:

  * A property indicating the page view with a unique `pageViewId`
  * The time spent on that page (`properties.timeOnPage`) calculated by the SDK


## Enable autotracking

The autotracking feature is controlled by the `autoTrack` parameter in the SDK’s [`load` API options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>). By default, it is set to `false`.
    
    
    "autoTrack" : {
      "enabled": true, // Default false
      "options": {} // Optional track API options to pass custom context
      "pageLifecycle": {
        "enabled": true, // Default false; overrides the global value (autoTrack.enabled)
        "options": {} // Optional, overrides the global value (autoTrack.options)
      }
    }
    

Note the following:

  * When autotracking is enabled, `context.autoTrack.page.pageViewId` is available in all events (including `track`, `page`, `identify`, and `group` events) sent from the page, **regardless** of whether the Beacon feature is enabled, allowing you to tie all events to a single page visit using the unique page view ID.
  * The nested `pageLifecycle` object provides granular and precise tracking configuration at the page level and **overrides** the global tracking settings.


### `autoTrack` configuration options

The following table lists the various `autoTrack` configuration options in detail:

Option| Data type| Description| Default value  
---|---|---|---  
`enabled`| Boolean| Enables or disables the autotracking feature.| `false`  
`options`| Object| Optional custom metadata to the `track` API.| -  
`pageLifecycle.enabled`| Boolean| Overrides the global `autoTrack.enabled` setting for tracking lifecycle of a specific page.| `false`  
`pageLifecycle.options`| Object| Optional custom metadata to the `track` API specified at the page level.| -  
  
## Workflow

When you set `autoTrack.pageLifecycle.enabled` or `autoTrack.enabled` (when `autoTrack.pageLifecycle.enabled` is **not** set) to `true`:

  1. `context.autoTrack.page.pageViewId` becomes available in all events (including `track`, `page`, `identify`, and `group` events) sent from the page. Note that the `pageViewId` is a UUID. **This works regardless of whether Beacon is enabled.**
  2. If Beacon is enabled, RudderStack fires a `track` event called `Page Unloaded` with the property `context.autoTrack.page.pageViewId` when the current page unloads.
  3. The `Page Unloaded` event also includes the time spent on the page in milliseconds in the `properties.timeOnPage` field.


## Important considerations

  * To reliably deliver the `Page Unloaded` event, you **must** enable the [Beacon transport mechanism](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#send-events-using-beacon>) by setting `useBeacon` to `true` in the [SDK load API options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>).
  * `context.autoTrack.page.pageViewId` is available in all events when autotracking is enabled, **regardless** of whether Beacon is enabled.


## Example payload

A sample payload for the `Page Unloaded` event containing the `timeOnPage` and `pageViewId` fields is shown:
    
    
    {
      "properties": {
        "timeOnPage": 25257
      },
      "event": "Page Unloaded",
      "type": "track",
      "channel": "web",
      "context": {
        "traits": {
          ...
        },
        "sessionId": 1747113325887,
        ...
    
        "autoTrack": {
          "page": {
            "pageViewId": "2d9abedf-a703-4c42-8e83-db6965fc1249"
          }
        }
      },
      ...
    
      "integrations": {
        "Google Analytics 4 (GA4)": {
          ...
          "sessionNumber": 131
        },
        "All": true
      },
      "sentAt": "2025-05-13T05:19:04.714Z"
    }
    

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/kotlin-sdk/>)