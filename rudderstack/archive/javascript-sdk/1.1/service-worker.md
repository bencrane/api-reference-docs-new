# JavaScript SDK Service Worker

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# JavaScript SDK Service Worker

Use the JavaScript SDK service worker in browser extensions and serverless runtime.

* * *

  * __4 minute read

  * 


RudderStack’s JavaScript SDK provides a service worker that you can use in browser extensions and serverless runtimes. It exposes the same interface and features as the [RudderStack Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>).

[![NPM Badge](https://img.shields.io/npm/v/@rudderstack/analytics-js-service-worker)](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>)

## Install the package

To install the package, run the following command:
    
    
    npm install @rudderstack/analytics-js-service-worker --save
    

Then, run the following code snippet and use the exported object throughout your project:
    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics('<WRITE_KEY>', '<DATA_PLANE_URL>/v1/batch');
    

> ![warning](/docs/images/warning.svg)
> 
> This NPM module is meant to be used only for service worker usage. To integrate RudderStack with your Node.js apps, use the [Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) instead.

## Usage in Chrome extensions

You can use the JavaScript SDK in Chrome extensions with the manifest v3 - both as a content script (via the JavaScript SDK package) or as background script (via [service worker package](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>)).

For more information on usage in Chrome extensions, see the [JavaScript SDK GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/blob/main/examples/chrome-extension/USAGE.md>).

### Background script

You can use the RudderStack [service worker npm package](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>) as a background script. To do so, place it in your Chrome extension resources by following either of these approaches:

  * Copy the file from the node modules and place it as a part of the resources.
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
    

Then, follow the [Node.js SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) for further usage.

You can also react to events available in the background scripts using the [Chrome API](<https://developer.chrome.com/docs/extensions/reference/>).

The following example tracks any URL changes:
    
    
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
    

### Content script

To use the RudderStack `Analytics` JavaScript SDK as a content script, place it in your Chrome extension resources by following either of these approaches:

  * Download the file and place it as a part of the resources.
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
        ]
    }
    

Then, follow the [SDK documentation](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/>) for further usage.

You can also react to events available in both the content and background scripts by leveraging the [Chrome API](<https://developer.chrome.com/docs/extensions/reference/>).

The following sample scripts help you track any URL changes:
    
    
    # prepend the JS SDK file here
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
    

## Usage in serverless runtimes

You can use the JavaScript SDK in serverless runtimes like Cloudflare workers or Vercel Edge functions.

### Cloudflare worker

To use the JavaScript SDK service worker in Cloudflare workers, start with the [sample](<https://developers.cloudflare.com/workers/get-started/guide/>) and integrate the SDK in the `worker.js` file:
    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics(
      "<WRITE_KEY>",
      "<DATA_PLANE_URL>/v1/batch",
      {
        flushAt: 1
      }
    );
    

Then, use the JavaScript SDK within the `fetch` methods with promisified flush:
    
    
    const flush = () => new Promise((resolve) => rudderClient.flush(resolve));
    
    rudderClient.track({
      userId: '123456',
      event: 'test cloudflare worker',
      properties: {
        data: {
          url: 'test cloudflare worker',
        },
      },
    });
    
    await flush();
    

For more information, see this [sample implementation](<https://github.com/rudderlabs/rudder-sdk-js/tree/main/examples/serverless/cloudflare-worker>).

### Vercel Edge

To use the JavaScript SDK service worker in Vercel Edge functions, start with the [sample](<https://vercel.com/docs/functions/edge-functions/quickstart>) and integrate the SDK in the `app/api/edge-function-sample/route.ts` file:
    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics(
      "<WRITE_KEY>",
      "<DATA_PLANE_URL>/v1/batch",
      {
        flushAt: 1
      }
    );
    

Then, use the JavaScript SDK within the `fetch` methods as usual:
    
    
    rudderClient.track({
      userId: '123456',
      event: 'test vercel edge worker',
      properties: {
        data: {
          url: 'test vercel edge worker',
        },
      }
    });
    

For more information, see this [sample implementation](<https://github.com/rudderlabs/rudder-sdk-js/tree/main/examples/serverless/vercel-edge>).

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/javascript-sdk-enhancements/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/faq/>)