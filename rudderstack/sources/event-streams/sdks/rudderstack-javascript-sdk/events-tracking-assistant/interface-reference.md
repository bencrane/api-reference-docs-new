# Events Tracking Assistant Interface Reference

> Version: Latest (v3)v1.1

# Events Tracking Assistant Interface Reference

Complete reference guide to all tabs and features in Events Tracking Assistant.

* * *

  * __7 minute read

  * 


This guide provides a reference to all tabs and features in the Events Tracking Assistant.

> ![info](/docs/images/info.svg)
> 
> If no SDK is detected on the page, you will see the SDK injection interface instead of the below tabs.

## Home tab

The **Home** tab provides a quick overview of your RudderStack implementation health. Use it to quickly identify if there are any issues with your implementation.

[![Home Tab](/docs/images/event-stream-sources/javascript/home-tab.webp)](</docs/images/event-stream-sources/javascript/home-tab.webp>)

### Health status

At-a-glance view of your SDK setup with visual indicators showing:

  * SDK detection status
  * Overall configuration health
  * Quick access to key information


### Destinations

Shows the number of:

  * Successfully loaded device-mode destinations
  * Failed destinations
  * Filtered destinations


### Plugins summary

Displays the status of:

  * Successfully loaded plugins
  * Failed plugins


### Recent events

Shows the last 10 events captured with:

  * Event type (`identify`, `track`, `page`, `group`, `alias`)
  * Event names
  * Timestamps
  * Quick access to event payloads
  * The option to preserve event logs


## Overview tab

The **Overview** tab provides detailed information about your SDK setup, organized into sections.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Look for the ⓘ icon next to field names for additional context and explanations.

[![Overview Tab](/docs/images/event-stream-sources/javascript/overview-tab.webp)](</docs/images/event-stream-sources/javascript/overview-tab.webp>)

### Setup

View essential SDK configuration details:

Detail| Description  
---|---  
SDK Version| The version of RudderStack JavaScript SDK in use  
Write Key| JavaScript source write key used in the web page integration  
Data Plane URL| The data plane URL  
Installation Type| CDN or NPM installation method  
Plugins Bundled| Whether plugins are bundled with the SDK  
Source| RudderStack source name, source ID, and workspace details  
  
### Persisted Data

Inspect data stored by the SDK in browser storage. This section helps you verify that user and session data is being captured correctly.

Detail| Description  
---|---  
User| Anonymous ID, User ID, User Traits  
User Group| Group ID, Group Traits  
Session| Session ID, [session tracking mode](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#session-tracking-types>), timeout, expiration time  
Page| Initial Referrer, Initial Referring Domain  
  
> ![info](/docs/images/info.svg)
> 
> Each field shows the [storage type](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>) used by the SDK to store the data (local storage, session storage, cookies, or memory)

### Page

View current page information. This section helps you verify that page context is being captured correctly for your events.

Detail| Description  
---|---  
Page URL| Current page URL  
Canonical URL| Canonical URL (if specified)  
Page Title| Page title  
Referrer| Referring page URL  
  
### Destinations

Monitor device-mode destination loading status. This section helps you troubleshoot why specific destinations aren’t loading or receiving data.

Detail| Description  
---|---  
Successfully loaded destinations| Destinations that loaded correctly  
Failed destinations| Destinations that failed to load with error details  
Filtered destinations| Destinations filtered due to consent, configuration, or other reasons  
Device-mode transformations| Shows whether device-mode transformations are enabled and their loading status.  
  


> ![info](/docs/images/info.svg)[Device-mode transformations](<https://www.rudderstack.com/docs/transformations/usage/#device-mode-transformations>) let you transform event data before it is sent to device-mode destinations, enabling custom data mapping and enrichment directly in the browser.  
  
Some common reasons for destination failures include:

  * Destination not configured correctly
  * Integration SDK blocked by ad blockers
  * Incorrect base URL configuration
  * Slow CDN response


### Plugins

Track plugin loading status. This section helps you troubleshoot why specific plugins aren’t loading or receiving data.

Detail| Description  
---|---  
Successfully loaded plugins| Plugins that loaded correctly  
Failed plugins| Plugins that failed to load with error details  
  
## Events tab

The **Events** tab provides real-time monitoring of all events sent through RudderStack.

[![Events Tab](/docs/images/event-stream-sources/javascript/events-tab.webp)](</docs/images/event-stream-sources/javascript/events-tab.webp>)

### Event list

View all captured events in chronological order with:

Detail| Description  
---|---  
Event type| Color-coded icons for `identify`, `track`, `page`, `group`, and `alias` events  
Event name| Name of the event (for track events) or event type  
HTTP status code| Status codes for successful or failed requests  
Beacon indicator| Shows “Beacon” for events sent via the Beacon API — these don’t return HTTP status codes  
Timestamp| Time when each event was sent (in UTC)  
  
> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use the search and filter options to quickly find specific events (by name or type) from the events list.

### Event details

Click on any event in the events list to view:

Detail| Description  
---|---  
Complete event payload| Formatted JSON showing all event data  
Request URL| The endpoint URL where the event was sent  
HTTP method| `GET` or `POST`  
HTTP status| Response status code  
Timestamp| Time when the event was sent (in UTC)  
Transport method| XHR or Beacon API  
  
> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Keep the extension open before triggering events. The extension can only capture events sent after it is opened on the page.

### Preserve logs

Lets you keep your event history across page navigations. This setting is helpful when you want to:

  * Track event flow across multi-page user journeys
  * Debug checkout or signup flows that span multiple pages
  * Analyze events before and after navigation
  * Retain event history when testing page transitions

Detail| Description  
---|---  
Preserve logs| Enable to retain events when navigating to new pages  
Clear| Clears all events in the log  
  
This feature works on a per-tab basis and remembers your preference. When enabled:

  * Events are marked as inactive (with reduced opacity) after page navigation
  * You will see page boundaries that show the URL where the navigation occurred
  * Events persist until you manually clear the log or close the tab

[![Preserve Logs](/docs/images/event-stream-sources/javascript/preserve-logs.webp)](</docs/images/event-stream-sources/javascript/preserve-logs.webp>)

### Export events

Detail| Description  
---|---  
Export all events| Download all captured events as a JSON file  
  
## Advanced tab

The **Advanced** tab contains tools for deeper debugging and configuration verification.

[![Advanced Tab](/docs/images/event-stream-sources/javascript/advanced-tab.webp)](</docs/images/event-stream-sources/javascript/advanced-tab.webp>)

### Custom Domains

Check if you’re using [custom domains](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/>). This section helps you verify proxy configuration and troubleshoot CORS or loading issues.

Detail| Description  
---|---  
Source Configuration URL| Custom domain for loading source configuration  
Data Plane URL| Custom domain for sending events to the data plane  
Integrations Base URL| Custom domain for loading device-mode destination SDKs  
Plugins Base URL| Custom domain for loading SDK plugins  
  
> ![info](/docs/images/info.svg)
> 
> Each field shows either **Standard Domain** or **Custom Domain** to indicate whether you’re using a proxy.

### Storage

View detailed information about browser storage usage. This section helps you debug storage-related issues and verify storage configuration.

Detail| Description  
---|---  
Encryption Version| The version used to encrypt the data persisted in the browser storage  
Data Migration Enabled| Determines if the persisted data encrypted using the legacy encryption technique is migrated to the latest format  
Truly Anonymous Tracking| Determines if the [cookieless tracking](<https://www.rudderstack.com/docs/data-governance/cookieless-tracking/>) feature is enabled. With this feature, you can track users without storing any user data — each event has a unique anonymous ID.  
Server-side Cookies Configured| Determines if [server-side cookies](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/server-side-cookies/>) are configured. If configured, the SDK makes requests to the analytics data server to set cookies via the response headers.  
Storage Type| Storage type for each data category (user, group, session, page, etc.)  
  
### Capabilities

Check browser and SDK capabilities. This section helps you understand browser limitations that might affect SDK functionality.

Detail| Description  
---|---  
Online Status| Determines if the browser is online or offline  
Storage support| Determines if the browser supports local storage, session storage, and cookies  
Beacon API support| Determines if the browser supports the Beacon API  
Legacy Browser| Determines if the browser is a legacy DOM  
UA Client Hints| Determines if the browser supports User-Agent Client Hints  
Ad-Blockers Detected| Determines if an ad-blocker is detected on the page  
  
### Export Debug Data

Click **Export** to export comprehensive SDK debug information including:

  * Complete SDK state
  * Configuration details
  * Source information
  * Session data
  * Loaded destinations and plugins
  * **Optional** : Include captured events


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Export debug data when contacting support or for detailed analysis. Include events if you need to share event payloads.

You can either copy the debug data to clipboard or download it as a JSON file.

## SDK injection (when no SDK is detected)

> ![warning](/docs/images/warning.svg)
> 
> Not all sites support injecting scripts due to strict Content Security Policy (CSP) headers. The extension indicates if injection is not supported. Use SDK injection for testing purposes only. For production use, install the JavaScript SDK on the website.

If no RudderStack JavaScript SDK is found on the page, the extension offers manual injection:

  1. Enter your **Write Key**.
  2. Enter your **Data Plane URL**.
  3. Click **Inject SDK**.

[![Inject SDK](/docs/images/event-stream-sources/javascript/inject-sdk.webp)](</docs/images/event-stream-sources/javascript/inject-sdk.webp>)

## See also

  * [Events Tracking Assistant Overview](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/>): Learn about the Events Tracking Assistant extension and its features
  * [Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>): Installation and basic usage of the Events Tracking Assistant extension
  * [Troubleshooting](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/troubleshooting/>): Solutions to common issues while using the Events Tracking Assistant extension


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/troubleshooting/>)