# RudderStack Events Tracking Assistant

> Version: Latest (v3)v1.1

# RudderStack Events Tracking Assistant

Learn about Events Tracking Assistant and how it helps you debug and monitor events tracked using the JavaScript SDK.

* * *

  * __2 minute read

  * 


The RudderStack **Events Tracking Assistant** is a browser extension for [Google Chrome](<https://chromewebstore.google.com/detail/rudderstack-assistant/mldkpbdooncodocccgjjkjojkneohnif>) and [Mozilla Firefox](<https://addons.mozilla.org/en-GB/firefox/addon/rudderstack-assistant/>) that helps you monitor, debug, and validate your RudderStack JavaScript SDK implementations directly within your browser.

> ![success](/docs/images/tick.svg)
> 
> Whether you’re implementing event tracking for the first time or troubleshooting issues in production, the **Events Tracking Assistant** extension provides real-time insights into your SDK configuration and event flow.

## Key features

Events Tracking Assistant automatically detects the RudderStack JavaScript SDK on web pages and provides the following capabilities:

  * **Real-time event monitoring** : Monitor all events sent through RudderStack in real-time without waiting for the events to reflect in the RudderStack dashboard
  * **SDK configuration visibility** : View the source write key, data plane URL, SDK version, and installation details
  * **Destination status** : Monitor device-mode destination loading status (loaded, failed, or filtered)
  * **Plugin tracking** : Track plugin loading status and identify failures
  * **Debug data export** : Export comprehensive SDK state and events for sharing with support
  * **SDK injection** : Test RudderStack on any webpage without modifying code
  * **Independent troubleshooting** : Identify and fix issues independently without external support
  * **Immediate feedback** : Get immediate feedback during implementation and testing
  * **Production debugging** : Debug issues in production without code changes or special builds


## Use cases

Target user| Use case| Pain points solved  
---|---|---  
  
  * Frontend Developer
  * Implementation Engineer

| Implementing and maintaining RudderStack JavaScript SDK| 

  * No visibility into events, SDK config, or destinations
  * Delayed feedback

  
  
  * Product Manager
  * Analyst

| Verifying tracking implementation meets requirements| 

  * Requires technical knowledge
  * Depends on developers for verification and issue communication

  
Support Engineer| Helping customers debug RudderStack implementations| 

  * Cannot debug independently
  * Rely on developers for information gathering

  
  
## Get started

  1. Install the extension from the [Chrome Web Store](<https://chromewebstore.google.com/detail/rudderstack-assistant/mldkpbdooncodocccgjjkjojkneohnif>) or [Firefox Add-ons](<https://addons.mozilla.org/en-GB/firefox/addon/rudderstack-assistant/>).
  2. Open a web page with the RudderStack JavaScript SDK installed.
  3. Open the extension from Developer Tools (**F12** > **»** > **RudderStack Assistant**) or click the pinned extension in your browser toolbar.


See the [Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>) guide for detailed instructions.

## Privacy and security

The extension only monitors RudderStack SDK activity on pages you visit. All data stays locally in your browser — **no data is sent to external servers**.

## In this section

Guide| Description  
---|---  
[Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>)| Get started with the **Events Tracking Assistant** extension in under 5 minutes  
[Interface reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>)| Complete reference to all tabs present in the Events Tracking Assistant and their features  
[Troubleshooting](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/troubleshooting/>)| Solutions to common issues while using the Events Tracking Assistant  
  
  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/sdk-hardening/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>)