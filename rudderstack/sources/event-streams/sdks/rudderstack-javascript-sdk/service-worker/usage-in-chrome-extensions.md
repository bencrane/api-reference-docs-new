# Use JavaScript Service Worker SDK in Chrome Extensions

> Version: Latest (v3)v1.1

# Use JavaScript Service Worker SDK in Chrome Extensions

* * *

  *  __3 minute read

  * 


You can use the JavaScript SDK in Chrome extensions with the manifest v3 as:

  * Content script (via the JavaScript SDK package), OR
  * Background script (via [JavaScript service worker SDK](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>)).


See the [JavaScript SDK GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/blob/main/examples/chrome-extension/USAGE.md>) for more information.

## Background script

You can use the RudderStack [service worker NPM package](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>) as a background script.

To do so, place it in your Chrome extension resources by following either of these approaches:

  * Copy the file from `node_modules` and place it as a part of resources.
  * Use a JS bundler and bundle it as a part of your service worker script.


> ![warning](/docs/images/warning.svg)
> 
> You need to enable relevant permissions in the manifest file according to the required capabilities and allowed connections.
> 
> Also, setting the background script `type` as a `module` is recommended, as it allows to import the script as ESM.
    
    
    "permissions": ["storage", "tabs"],
    "host_permissions": [
        "https://*.dataplane.rudderstack.com/*",
        "https://*.rudderlabs.com/*",
        "*://*/*"
    ],
    "externally_connectable": {
        "matches": [
            "https://*.dataplane.rudderstack.com/*",
            "https://*.rudderlabs.com/*"
        ]
    },
    "background": {
        "service_worker": "service-worker.js",
        "type": "module"
    },
    

Then, follow the [Node.js SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) for further usage as the API is identical to it.
    
    
    // If file is copied from node_modules/@rudderstack/analytics-js-service-worker/npm/esm/index.js in extension resources folder
    
    import { Analytics } from "./rudderAnalytics.js";
    
    // If the package is imported directly as umd and then bundled in the background script
    
    import { Analytics } from "@rudderstack/analytics-js-service-worker/umd/index.js";
    
    // If the package is imported directly as es-module and then bundled in the background script
    
    import { Analytics } from "@rudderstack/analytics-js-service-worker";
    
    
    
    const rudderClient = new Analytics("<WRITE_KEY>","<DATA_PLANE_URL>/v1/batch");
    
    chrome.tabs.onUpdated.addListener((tabId, tab) => {
        if (tab.url) {
            rudderClient.track({
                userId: "123456",
                event: "Event Name",
                properties: {
                    data: { url: tab.url },
                }
            });
        }
    });
    

See the [sample application](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/chrome-extension/background-script>) for more information on using the service worker NPM package as a background script.

## Content script

To use the JavaScript SDK as a content script, place it in your Chrome extension resources by following either of these approaches:

  * Copy the `index.js` file from the `node_modules` folder after installing the package (`node_modules/@rudderstack/analytics-js/dist/npm/modern/cjs/index.js`) and place it as a part of the resources.


> ![info](/docs/images/info.svg)
> 
> You can use the `cjs` bundle from `legacy` folder (`node_modules/@rudderstack/analytics-js/dist/npm/legacy/cjs/index.js`) as well, depending on your requirement.
> 
> Note that the `modern` folder is targeted for browsers that support the modern JavaScript syntax, especially dynamic imports, whereas the `legacy` folder is meant for the rest of the browsers.

  * Use a JS bundler and bundle it as part of your content script.


> ![warning](/docs/images/warning.svg)
> 
> You need to enable relevant permissions in the manifest file according to the required capabilities and allowed connections.
    
    
    "permissions": ["storage", "tabs"],
    "host_permissions": [
      "https://*.dataplane.rudderstack.com/*",
      "https://*.rudderlabs.com/*",
      "*://*/*"
    ],
    "externally_connectable": {
      "matches": [
        "https://*.dataplane.rudderstack.com/*",
        "https://*.rudderlabs.com/*"
    ]},
    "content_scripts": [{
      "js": ["foreground.js"],
      "matches": ["https://github.com/*"]
    }]
    

Then, follow the [SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) for further usage.

You can also react to events available in both the content and background scripts by leveraging the [Chrome API](<https://developer.chrome.com/docs/extensions/reference/>).

The following sample scripts help you track any URL changes:
    
    
    // Prepend the JavaScript SDK file here
    rudderanalytics.load("<WRITE_KEY>", "<DATA_PLANE_URL>");
    
    chrome.runtime.onMessage.addListener((obj, sender, response) => {
        const { type, value } = obj;
    
        if (type === "trackURL") {
            rudderanalytics.track("URL change", { url: value });
        }
    });
    
    
    
    chrome.tabs.onUpdated.addListener((tabId, tab) => {
        if (tab.url) {
            chrome.tabs.sendMessage(tabId, {
                type: "trackURL",
                value: {
                    url: tab.url
                },
            });
        }
    });
    

See the [sample application](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/chrome-extension/content-script-v3>) for more information on using the SDK as a content script.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/faq/>)