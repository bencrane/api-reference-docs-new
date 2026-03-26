# Use the JavaScript Service Worker SDK

> Version: Latest (v3)v1.1

# Use the JavaScript Service Worker SDK

Use the JavaScript service worker SDK in your browser extensions and serverless runtime.

* * *

  * __3 minute read

  * 


This guide explains how to use the JavaScript [service worker SDK](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>) in browser extensions and serverless runtimes.

[![](https://img.shields.io/npm/v/@rudderstack/analytics-js-service-worker)](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>)

## Overview

The JavaScript service worker SDK brings RudderStack’s analytics capabilities to environments where the standard browser JavaScript SDK cannot operate. This specialized SDK targets non-browser contexts that require background processing and offline functionality.

> ![info](/docs/images/info.svg)
> 
> This SDK exposes the same interface and applicable features as RudderStack’s [Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>).

Some key features of the service worker SDK are:

  * **Browser extension compatibility** : You can integrate analytics into Chrome extensions using manifest v3, supporting both content scripts and background scripts.
  * **Serverless runtime support** : The SDK works seamlessly in serverless environments like Cloudflare Workers and Vercel Edge functions.
  * **Background processing** : Service workers run independently of web pages, enabling reliable data collection even when users navigate away, and features like offline support and push notifications.


## Install the service worker package

  1. Run the following command to install the service worker package:


    
    
    npm install @rudderstack/analytics-js-service-worker --save
    

  2. Run the following snippet and use the exported object throughout your project:


    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics('<WRITE_KEY>', '<DATA_PLANE_URL>/v1/batch');
    

> ![warning](/docs/images/warning.svg)
> 
> This NPM module is meant to be used only in non-browser environments. To integrate RudderStack with your Node.js apps, RudderStack recommends using the [Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) instead.
> 
> Note that the APIs are the same in both the cases.

## Usage in Chrome extensions

You can use the JavaScript SDK in Chrome extensions with the manifest v3 as:

  * [Content script](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/#content-script>) (via the JavaScript SDK package), OR
  * [Background script](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/#background-script>) (via [JavaScript service worker SDK](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>)).


See the [Usage in Chrome Extensions](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/>) for more information.

## Usage in serverless runtimes

You can use the JavaScript service worker SDK in serverless runtimes like Cloudflare workers or Vercel Edge functions.

### Cloudflare worker

To use the JavaScript SDK service worker in Cloudflare workers:

  1. Start with the [Cloudflare worker sample](<https://developers.cloudflare.com/workers/get-started/guide/>).
  2. Integrate the SDK in the `worker.js` file:


    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics(
      "<WRITE_KEY>",
      "<DATA_PLANE_URL>/v1/batch",
      {
        flushAt: 1
      }
    );
    

  3. Use the JavaScript SDK within the `fetch` methods with promisified flush:


    
    
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
    

For more information, see this [sample implementation](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/serverless/cloudflare-worker>).

### Vercel Edge

To use the JavaScript SDK service worker in Vercel Edge functions:

  1. Start with the [Vercel Edge function sample](<https://vercel.com/docs/functions/edge-functions/quickstart>).
  2. Integrate the SDK in the `app/api/edge-function-sample/route.ts` file:


    
    
    import { Analytics } from '@rudderstack/analytics-js-service-worker';
    
    const rudderClient = new Analytics(
      "<WRITE_KEY>",
      "<DATA_PLANE_URL>/v1/batch",
      {
        flushAt: 1
      }
    );
    

  3. Use the JavaScript SDK within the `fetch` methods as usual:


    
    
    rudderClient.track({
      userId: '123456',
      event: 'test vercel edge worker',
      properties: {
        data: {
          url: 'test vercel edge worker',
        },
      }
    });
    

For more information, see this [sample implementation](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/serverless/vercel-edge>).

  


##### [Use JavaScript Service Worker SDK in Chrome Extensions](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/>)

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/>)