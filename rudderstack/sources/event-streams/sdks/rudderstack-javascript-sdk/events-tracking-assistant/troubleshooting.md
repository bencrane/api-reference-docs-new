# Troubleshooting Events Tracking Assistant

> Version: Latest (v3)v1.1

# Troubleshooting Events Tracking Assistant

Solutions for when Events Tracking Assistant isn’t working as expected.

* * *

  * __3 minute read

  * 


This guide contains solutions for common issues you may encounter while using the Events Tracking Assistant.

> ![info](/docs/images/info.svg)
> 
> This guide covers troubleshooting the extension itself.
> 
> If you’re looking to debug your RudderStack SDK implementation, use the different tabs (**Overview** , **Events** , **Advanced**) described in the [Interface Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>).

## Extension issues

Issue| Solution  
---|---  
Extension blank or not loading| 

  * Right-click the extension icon > **Inspect popup** and check for errors.
  * Reload the extension (Chrome: `chrome://extensions/`, Firefox: `about:addons`).
  * If issues persist, temporarily disable other extensions or reinstall the extension.

  
Extension taking too long to load| 

  * Refresh the web page and wait for it to fully load before opening the extension.
  * Check browser console for errors.

  
Extension icon not visible in toolbar| 

  * Chrome: Click the puzzle piece icon (Extensions) and pin the extension.
  * Firefox: Right-click the toolbar > **Customize Toolbar** and drag the extension icon to the toolbar.

  
Extension shows stale data| Close and reopen the extension. The extension shows data for the currently active browser tab.  
Extension not in Developer Tools| Close and reopen Developer Tools. The **RudderStack Assistant** tab should appear in the **»** menu.  
  
## SDK detection issues

Issue| Solution  
---|---  
SDK not detected| 

  * Refresh the web page with the extension open and wait 2-3 seconds.
  * Verify the SDK is installed by checking `window.rudderanalytics` in the browser console.
  * If undefined, the SDK is not installed on this page.

  
SDK injection not working| 

  * Some websites have strict Content Security Policy (CSP) headers that prevent script injection. The extension indicates if injection is not supported.
  * For production use, install the JavaScript SDK on the website instead.

  
  
## Events and data issues

Issue| Solution  
---|---  
Events not appearing in **Events** tab| 

  * Open the extension **before** triggering events. The extension can only capture events sent after it is opened.
  * To capture page load events, open the extension and refresh the page.

  
Events count differs from dashboard| 

  * This is normal behavior. The extension shows events sent from the browser, while the dashboard shows events received by RudderStack.
  * The count can differ due to processing delays, failed events, filtering, or different time ranges.

  
**Overview** tab shows empty data| 

  * Wait for the SDK to fully initialize. Verify the SDK is detected (check for SDK version in the header).
  * Some data may be empty if no user ID is set or no destinations are configured.

  
  
## Destination issues

Issue| Solution  
---|---  
Destination not loading or showing as failed| Check **Overview** > **Destinations** for error details. Common causes include:

  * Ad blocker interference: Disable ad blockers temporarily or configure custom domains/proxies
  * Incorrect base URL: Verify destination configuration in the RudderStack dashboard and check **Advanced** > **Custom Domains
  * Slow CDN response: Check network connectivity and browser console for network errors
  * Incorrect configuration: Verify the destination is enabled in the RudderStack dashboard and device-mode is enabled

  
Destination showing as filtered| 

  * Destinations can be filtered due to consent requirements, SDK loaded in pre-consent mode, destination not enabled in the dashboard, or explicitly disabled via integrations object in load options.
  * Check your RudderStack dashboard and SDK configuration.

  
  
## Feature issues

Issue| Solution  
---|---  
Copy to clipboard not working| 

  * Check browser clipboard permissions in extension settings. Try downloading as a file instead, or manually select and copy text.

  
Export not working| 

  * Check if popup blockers are enabled. Try **Copy to Clipboard** instead.
  * Ensure the SDK is detected and fully initialized before exporting.

  
  
## Get help

If you’ve tried the above solutions and still have problems, report the issue on the [GitHub repository](<https://github.com/rudderlabs/events-tracking-assistant/issues>). Include:

  * Browser and version
  * Extension version
  * Steps to reproduce the problem
  * Screenshots (if applicable)
  * Browser console errors


> ![warning](/docs/images/warning.svg)
> 
> Do not include write keys, credentials, or personal user data in public reports. Share these privately with support if needed.

## See also

  * [Events Tracking Assistant Overview](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/>): Learn about the Events Tracking Assistant extension and its features
  * [Interface Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>): Learn about the different tabs available in the extension
  * [Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/quickstart/>): Installation and basic usage of the Events Tracking Assistant extension


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/interface-reference/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/>)