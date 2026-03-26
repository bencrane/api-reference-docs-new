# JavaScript SDK

> Version: Latest (v3)v1.1

# JavaScript SDK

Track event data and send it your specified destinations using the RudderStack JavaScript SDK.

* * *

  * __3 minute read

  * 


RudderStack’s [JavaScript SDK](<https://github.com/rudderlabs/rudder-sdk-js>) lets you track customer event data from your website and send it to your specified [destinations](<https://www.rudderstack.com/docs/destinations/overview/>). It is written in TypeScript and offers significant improvements in performance, size, and features compared to its [predecessor](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/>).

This documentation covers the latest **JavaScript SDK v3** ([`@rudderstack/analytics-js`](<https://www.npmjs.com/package/@rudderstack/analytics-js>) on npm).

[![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fregistry.npmjs.org%2F%40rudderstack%2Fanalytics-js&query=dist-tags.latest&label=npm)](<https://www.npmjs.com/package/@rudderstack/analytics-js>)  


## Key features

  * Fast, reliable, and less vulnerable to ad blockers.
  * Load specific SDK features on demand using [plugins](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#plugins>).
  * Lightweight [storage data footprint](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) with improved encryption.
  * Complete control over the persistent data storage strategy.
  * ITP (Intelligent Tracking Prevention) compliant as it implements server-side cookies.
  * Smaller SDK of around 25KB (size reduction of approximately 30% from the previous version).


## Get started

> ![info](/docs/images/info.svg)
> 
> **Migrating from older versions?**
> 
> If you are upgrading from a version prior to v3, review these guides before getting started:
> 
>   * [Migration guide](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/migration-guide/>): Step-by-step instructions for updating your SDK implementation.
>   * [Breaking changes](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/>): Understand the compatibility differences introduced in v3.
> 

> 
> Learn about the [benefits of upgrading to JavaScript SDK v3](<https://www.rudderstack.com/blog/feature-launch-javascript-sdk-v3-delivers-better-performance-and-more-control/>).

If you’re using `npm` module in your browser-side code, following code snippet will import the RudderStack JavaScript SDK and send its first `page` event.
    
    
    // Step 1: Install the SDK - `npm i @rudderstack/analytics-js`
    // Step 2: Initalize the SDK
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    const rudderAnalytics = new RudderAnalytics();
    rudderAnalytics.load(process.env.WRITE_KEY, process.env.DATA_PLANE_URL, {});
    // Q: How to generate your WRITE_KEY and DATA_PLANE_URL?
    // A: Create a new JavaScript source at https://app.rudderstack.com
    export { rudderAnalytics };
    // Step 3: Call event tracking methods such as `page`, `track`, `identify`, etc. as needed
    rudderAnalytics.page();
    // NOTICE: This code works only if you have set up your browser-side code to use `npm` modules. Follow the quickstart guide otherwise.
    // https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/
    

Follow the [JavaScript SDK Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/>) to quickly start using RudderStack JavaScript SDK with any of your preferred methods (Using CDN, npm (ESM or CJS), or for single-page applications).

## Core tasks

Find instructions for specific goals and common implementation tasks related to the JavaScript SDK:

Guide| Description  
---|---  
[Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/>)| Set up and use the JavaScript SDK on your website in no time.  
[Install the JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/>)| Install the JavaScript SDK via CDN or NPM.  
[Load the SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>)| Understand the different options for loading the SDK snippet.  
[Track event data](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/>)| Use the SDK’s API calls (`identify`, `track`, `page`, etc.) to send data.  
[Configure data persistence](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>)| Customize how the SDK stores user information and preferences.  
[Use server-side cookies](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/server-side-cookies/>)| Implement server-side cookies for improved tracking and ITP compliance.  
[Filter events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>)| Control which events are sent to specific destinations.  
[Implement consent management](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>)| Configure the various consent management options in JavaScript SDK.  
[Detect Ad-blocked pages](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>)| Identify when the SDK might be blocked by ad blockers.  
[Use the service worker SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/>)| Implement tracking in service worker environments.  
[Use JavaScript SDK in Chrome extensions](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/usage-in-chrome-extensions/>)| Integrate the SDK within a Chrome browser extension.  
[Harden JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/sdk-hardening/>)| Configure a hardened version of the JavaScript SDK for added security.  
  
## Understand concepts

  * [JavaScript SDK key features](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/new-features/>): Learn about the significant enhancements in SDK v3.
  * [Data persistence in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/>): Understand how and what data the SDK stores locally.


See [FAQs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/faq/>) for answers to the commonly-asked questions about the JavaScript SDK.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-amp-analytics/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/>)