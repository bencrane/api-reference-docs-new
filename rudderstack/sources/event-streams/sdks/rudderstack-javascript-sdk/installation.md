# How to Install the JavaScript SDK

> Version: Latest (v3)v1.1

# How to Install the JavaScript SDK

Learn how to install the RudderStack JavaScript SDK on your website.

* * *

  * __5 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> If you are migrating from an older version, see the [Migration Guide](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/migration-guide/>) for details.

The JavaScript SDK lets you track user events, identify users, and send this data to various analytics platforms and marketing tools. By integrating this SDK with your website, you can gain valuable insights into user behavior, optimize your marketing efforts, and make data-driven decisions to drive growth.

This guide will help you install the RudderStack JavaScript SDK on your website via CDN or using NPM.

> ![success](/docs/images/tick.svg)
> 
> See the [RudderStack JavaScript SDK repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples>) for sample applications using different installation methods.

## Using CDN

Follow these steps to get the JavaScript SDK installation snippet and integrate it in your website.

  1. Go to the **Setup** tab of your JavaScript source in the [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Click the **Minified** or **Original** tab followed by **Copy snippet**.

[![JavaScript SDK snippet](/docs/images/get-started/quickstart/js-sdk-snippet.webp)](</docs/images/get-started/quickstart/js-sdk-snippet.webp>)

To integrate the SDK with your website and load it **synchronously** , set `scriptLoadingMode` (highlighted below) to `""`.
    
    
    var scriptLoadingMode = "";
    

[![JavaScript SDK synchronous installation](/docs/images/event-stream-sources/js-sdk-installation-snippet-unminified.webp)](</docs/images/event-stream-sources/js-sdk-installation-snippet-unminified.webp>)

To defer the script loading to the end, set `scriptLoadingMode` to `defer`, as shown:
    
    
    var scriptLoadingMode = "defer";
    

  4. Paste the modified script in your website’s `<head>` section.


Note the following:

  * The SDK installation snippet contains both the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) by default.
  * The implicit `page` call at the end of the snippet (present in the previous JavaScript SDK versions) is removed in the [latest SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/#installation>). If required, you need to make a `page` call explicitly, as shown:


    
    
    rudderanalytics.page();
    

  * Depending on the browser, the SDK loads either the legacy or modern JavaScript SDK bundle. The legacy bundle is built for ES5 while the modern bundle (with Module Federation) is built for ES6.
  * You can also pass your `loadOptions` as a third argument in the `rudderanalytics.load` method. See [Load JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) for more information.


### Installation workflow

The installation code snippets listed above perform the following actions:

  1. Based on browser capabilities, load either the `legacy` or `modern` bundle.
  2. Load the necessary polyfills for the SDK to load.
  3. Create an array to store the events until the SDK is ready.
  4. Store the method invocations in the below table to replay them when the SDK is ready.
  5. Load the SDK with the specified write key.

Method| Description  
---|---  
[`load`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>)| Loads the SDK with the specified [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).  
[`identify`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#identify>)| Identifies the users, records their traits, and associates them with their actions.  
[`page`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#page>)| Records your website’s page views along with any other information about the viewed page.  
[`track`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#track>)| Tracks user events along with the associated properties.  
[`alias`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#alias>)| Maps new user ID with an old ID.  
[`group`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#group>)| Links an identified user with a group like a company, organization, or an account.  
[`reset`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#reset>)| Resets information related to the previously identified user.  
[`ready`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#ready-api>)| Fired when the SDK has initialized itself and the other third-party native SDK destinations.  
[`setAnonymousId`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#overriding-anonymous-id>)| Sets the anonymous user ID.  
[`startSession`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/manual-session-tracking/>)| Starts a new session.  
[`endSession`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/manual-session-tracking/>)| Resets the current session.  
  
## Using NPM

While using the above snippets to integrate the JavaScript SDK with your website is recommended, you can alternatively use the [NPM module](<https://www.npmjs.com/package/@rudderstack/analytics-js>) for packaging RudderStack directly into your project.

To install the JavaScript SDK via NPM, run the following command:
    
    
    npm install @rudderstack/analytics-js --save
    

> ![warning](/docs/images/warning.svg)
> 
> **Use this NPM module only for browser installation.**
> 
> To integrate RudderStack with your Node.js apps, see [Node.js SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>)

Since the NPM module exports the related APIs on an already-defined object combined with the Node.js module caching, run the following code snippet **once** and use the exported `rudderAnalytics` object throughout your project:

  * **For ECMAScript modules (ESM)** :


    
    
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    
    const rudderAnalytics = new RudderAnalytics();
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {});
      
    export { rudderAnalytics };
    

  * **For CJS using the`require` method**:


    
    
    var RudderAnalytics = require("@rudderstack/analytics-js");
    
    const rudderAnalytics = new RudderAnalytics();
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {});
    
    exports.rudderAnalytics = rudderAnalytics;
    

#### SDK imports for bundling tools that process dynamic imports

If you are using a tool to bundle your application and it is attempting to process the dynamic runtime imports of the dependencies, update your SDK imports from `@rudderstack/analytics-js` to `@rudderstack/analytics-js/bundled` to avoid any issues with dynamic imports failing to find plugin modules.

Most common toolchains like the ones based on webpack, rollup, and vite should not face any issues. If your particular setup/toolchain is affected, contact [RudderStack Support](<mailto:support@rudderstack.com>).

##### **Usage in Chrome extension**

To use the JavaScript SDK within a Chrome extension, import the content-script as shown:
    
    
    import { RudderAnalytics } from '@rudderstack/analytics-js/content-script';
    

See the [Usage in Chrome Extensions](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/#content-script>) guide for more details, along with a [sample application](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/chrome-extension/content-script-v3>).

##### **Preload events with NPM package**

If you are using a single-page application (SPA) or frameworks that load the JavaScript SDK in an async manner (lazy loading), you will need an array buffer to store the events before the SDK is loaded.

You can use this [sample snippet](<https://github.com/rudderlabs/rudder-sdk-js/blob/develop/examples/nextjs/hooks/sample-app/src/app/layout.tsx#L17>) to achieve this use case.

## Supported browsers

The JavaScript SDK supports the following browsers and their corresponding versions:

Browser| Supported Versions  
---|---  
Safari| v10 and above  
IE| v11 and above  
Edge| v80 and above  
Mozilla Firefox| v47 and above  
Chrome| v54 and above  
Opera| v43 and above  
  
> ![info](/docs/images/info.svg)
> 
> For unsupported browser versions, try adding browser [polyfills](<https://developer.mozilla.org/en-US/docs/Glossary/Polyfill>) to your application for the SDK to work correctly.

## Integration with Chromecast

RudderStack supports integrating the JavaScript SDK with [Google Chromecast](<https://store.google.com/in/product/chromecast?hl=en-GB>). You can build the web sender app by following [these instructions](<https://developers.google.com/cast/docs/web_sender>) and adding the JavaScript SDK.

See [Google Cast developer guide](<https://developers.google.com/cast/docs/developers>) for more details.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/migration-guide/>)