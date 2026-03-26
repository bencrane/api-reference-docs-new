# Events Tracking Assistant Quickstart

> Version: Latest (v3)v1.1

# Events Tracking Assistant Quickstart

Get started with Events Tracking Assistant in less than 5 minutes.

* * *

  * __3 minute read

  * 


This guide walks you through installation and your first use of the Events Tracking Assistant.

## Prerequisites

  * A web page with RudderStack JavaScript SDK installed
  * A JavaScript source [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) from your RudderStack dashboard


## Step 1: Install the extension

This section walks you through the process of installing the extension in your preferred browser.

#### Chrome

  1. Go to the extension’s page in the [Chrome Web Store](<https://chromewebstore.google.com/detail/rudderstack-assistant/mldkpbdooncodocccgjjkjojkneohnif>).
  2. Click **Add to Chrome**.
  3. Confirm the installation when prompted.


#### Firefox

  1. Go to the extension’s page in the [Firefox Add-ons](<https://addons.mozilla.org/en-GB/firefox/addon/rudderstack-assistant/>).
  2. Click **Add to Firefox**.
  3. Confirm the installation when prompted.


## Step 2: Open a page with RudderStack

Navigate to any web page that has RudderStack JavaScript SDK installed.

## Step 3: Open the extension

You can access the extension in two ways:

#### Option 1: Developer tools (Recommended)

> ![success](/docs/images/tick.svg)
> 
> Prefer this option as the extension stays open as you navigate between pages and tabs.

  1. Open your browser’s **Developer Tools** (press **F12** or right-click > **Inspect**)
  2. Click the **»** menu.
  3. Select **RudderStack Assistant**.

[![Developer Tools](/docs/images/event-stream-sources/javascript/dev-tools.webp)](</docs/images/event-stream-sources/javascript/dev-tools.webp>)

#### Option 2: Browser toolbar

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Make sure to pin the **Events Tracking Assistant** extension in your browser’s toolbar first.

Click the **Events Tracking Assistant** extension icon in your browser’s toolbar. Note that the popup will close automatically when you switch tabs or navigate to a different page.

[![Browser Extension](/docs/images/event-stream-sources/javascript/browser-extension.webp)](</docs/images/event-stream-sources/javascript/browser-extension.webp>)

## Step 4: View your SDK status

The extension automatically detects your SDK and displays:

  * SDK version in the top right corner
  * Configuration status
  * Loaded destinations
  * Real-time events

[![Home Tab](/docs/images/event-stream-sources/javascript/home-tab.webp)](</docs/images/event-stream-sources/javascript/home-tab.webp>)

If no SDK is detected, you can manually inject the SDK for testing. Enter your write key and data plane URL, then click **Inject SDK**.

> ![warning](/docs/images/warning.svg)
> 
> Not all sites support SDK injection due to strict Content Security Policy (CSP) headers. The extension indicates if injection is not supported.

[![Inject SDK](/docs/images/event-stream-sources/javascript/inject-sdk.webp)](</docs/images/event-stream-sources/javascript/inject-sdk.webp>)

## Step 5: Trigger events

> ![warning](/docs/images/warning.svg)
> 
> Open the extension **before** triggering events. The extension can only capture events sent **after** it is opened.

  1. Navigate to the **Events** tab of the extension
  2. Interact with your web page to trigger events.
  3. Watch events appear in real-time with their payloads and HTTP status codes.


#### Tabs overview

Tab| What it does| When to use  
---|---|---  
**Home**|  Quick health overview| First place to check for issues  
**Overview**|  Detailed SDK configuration| Verify setup, check destinations/plugins  
**Events**|  Real-time event monitoring| Debug event tracking  
**Advanced**|  Deep debugging tools| Troubleshoot complex issues  
  
See the [Interface Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>) guide for more details on these tabs.

## See also

  * [Events Tracking Assistant Overview](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/>): Learn about the Events Tracking Assistant extension and its features
  * [Interface Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>): Learn about the different tabs available in the extension
  * [Troubleshooting](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/troubleshooting/>): Solutions to common issues while using the extension


## FAQ

#### Which browsers does this extension support?

The extension supports [Chrome](<https://chromewebstore.google.com/detail/rudderstack-assistant/mldkpbdooncodocccgjjkjojkneohnif>) and [Firefox](<https://addons.mozilla.org/en-GB/firefox/addon/rudderstack-assistant/>).

#### Does this extension work with cloud-mode destinations?

Yes. The extension monitors all events sent from the SDK, regardless of destination mode. However, the **Destinations** section in **Overview** only shows device-mode destinations since those load directly in the browser.

#### Is my data sent to external servers?

No. All data stays local in your browser. The extension only monitors RudderStack SDK activity and does not send any data to external servers.

#### Can I use this extension in production?

Yes. The extension is safe to use in production for debugging purposes. It only observes SDK activity without interfering with your website’s functionality or performance.

#### Will this extension slow down my website?

No. The extension runs separately from your website and does not affect your website’s performance.

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>)