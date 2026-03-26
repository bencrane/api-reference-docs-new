# JavaScript SDK Migration Guide

> Version: Latest (v3)v1.1

# JavaScript SDK Migration Guide

Migrate your RudderStack JavaScript SDK from older versions to the latest version.

* * *

  * __3 minute read

  * 


This guide lists the steps to update your [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) from the older versions.

## Pre-migration checklist

  1. Go through the [Breaking Changes](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/>) in the JavaScript SDK v3 to understand potential impacts on your implementation.
  2. If you have implemented the JavaScript SDK in multiple sites sharing the same top-level domain and cookies and have different major SDK versions across these sites, then RudderStack recommends the following actions:


  * Consider upgrading **all** sites to the [latest v3 SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>) at once.
  * If that is not possible, then upgrade the older sites to the [latest version](<https://www.npmjs.com/package/rudder-sdk-js>) of SDK v1.1.
  * If any of the above actions are not possible, then set the [`storage.encryption.version`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) parameter to `legacy` for all the sites.


For example, if `shop.example.com` uses the latest JavaScript SDK (v3) and `docs.example.com` uses a legacy SDK version (v1.1 or below), then set the encryption version to `legacy` in the `shop.example.com` site to avoid corrupting the RudderStack storage data:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        encryption: {
          version: "legacy"
        }
      },
      // Other load options
    });
    

> ![info](/docs/images/info.svg)
> 
> RudderStack stores all its cookies in the top-level domain of your site by default unless you’ve configured to change the domain.

  3. Decide on storage migration. By default, the new SDK will migrate existing cookies to the new encryption technique. To prevent this, you can:


  * Set [`storage.migrate`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) load API option to `false`, or
  * Exclude the `StorageMigrator` plugin in the [`plugins`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#plugins>) load API option.


  4. If you directly access data from storage (not recommended by RudderStack), update your decryption logic to match the new encryption technique as the [data encryption technique has changed](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/#storage-and-encryption>).


See [Data Persistence in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/>) for more information on the storage and encryption features.

## CDN

Change the [SDK installation snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-cdn>). Then, replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values.

For more information, see the following guides:

  * [CDN installation method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>) for installing the SDK snippet.
  * [Setup for serving Javascript SDK](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/#step-3-serve-sdk>) if you are using your own domain to proxy the SDK or route the events.


## NPM

The NPM package based on the latest JavaScript SDK architecture is available [here](<https://www.npmjs.com/package/@rudderstack/analytics-js>).

> ![info](/docs/images/info.svg)
> 
> The latest SDK’s NPM package is published as `@rudderstack/analytics-js` instead of `rudder-sdk-js`.

You can use any of the following options to update the SDK using NPM:

  1. Install the SDK package using the below command:


    
    
    npm i @rudderstack/analytics-js
    

  2. Run`npm install`.


See the [NPM installation method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>) for more details on using the package.

  1. Manually modify the `package.json` file:


    
    
    "dependencies": {
      "@rudderstack/analytics-js": "^3.x.x"
    }
    

  2. Run`npm install`.


See the [NPM installation method](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>) for more details on using the package.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>)