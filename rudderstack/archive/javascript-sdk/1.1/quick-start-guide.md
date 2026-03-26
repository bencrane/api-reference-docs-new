# Quickstart

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# Quickstart

Install and use the RudderStack JavaScript SDK on your website.

* * *

  * __6 minute read

  * 


This guide lists the steps to quickly install and use the JavaScript SDK to identify your website users and track their actions.

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values in the snippets (wherever applicable) throughout this guide.

## Prerequisites

To set up and use the RudderStack JavaScript SDK, the following prerequisites must be met:

  * Set up a [RudderStack account](<https://app.rudderstack.com/signup>).
  * [Set up a JavaScript source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the RudderStack dashboard.


## Step 1: Install JavaScript SDK

### Using a CDN

To integrate the SDK with your website and load it **asynchronously** :

  1. Go to the **Setup** tab of your JavaScript source in the dashboard.
  2. Copy the following snippet by clicking on **Copy Snippet** and paste it in your website’s `<head>` section:

[![JavaScript source write key](/docs/images/event-stream-sources/javascript-setup-new.webp)](</docs/images/event-stream-sources/javascript-setup-new.webp>)

> ![success](/docs/images/tick.svg)
> 
> The SDK installation snippet (seen above) contains both the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) by default.

Alternatively, you can copy and use the below snippet:
    
    
    <script type="text/javascript">
    !function(){var e=window.rudderanalytics=window.rudderanalytics||[];e.methods=["load","page","track","identify","alias","group","ready","reset","getAnonymousId","setAnonymousId","getUserId","getUserTraits","getGroupId","getGroupTraits","startSession","endSession","getSessionId"],e.factory=function(t){return function(){e.push([t].concat(Array.prototype.slice.call(arguments)))}};for(var t=0;t<e.methods.length;t++){var r=e.methods[t];e[r]=e.factory(r)}e.loadJS=function(e,t){var r=document.createElement("script");r.type="text/javascript",r.async=!0,r.src="https://cdn.rudderlabs.com/v1.1/rudder-analytics.min.js";var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(r,a)},e.loadJS(),
    e.load(WRITE_KEY,DATA_PLANE_URL),
    e.page()}();
    </script>
    

To integrate the SDK with your website and load it **synchronously** , add any of the following scripts in your website’s `<head>` section.

**Minified code**
    
    
     <script>
    rudderanalytics=window.rudderanalytics=[];for(var methods=["load","page","track","identify","alias","group","ready","reset","getAnonymousId","setAnonymousId","getUserId","getUserTraits","getGroupId","getGroupTraits","startSession","endSession","getSessionId"],i=0;i<methods.length;i++){var method=methods[i];rudderanalytics[method]=function(a){return function(){rudderanalytics.push([a].concat(Array.prototype.slice.call(arguments)))}}(method)}rudderanalytics.load(WRITE_KEY,DATA_PLANE_URL),rudderanalytics.page();
    </script>
    
    <script src="https://cdn.rudderlabs.com/v1.1/rudder-analytics.min.js"></script>
    

**Non-minified code**
    
    
     <script>
      rudderanalytics = window.rudderanalytics = [];
      var methods = [
        "load",
        "page",
        "track",
        "identify",
        "alias",
        "group",
        "ready",
        "reset",
        "getAnonymousId",
        "setAnonymousId",
        "getUserId",
        "getUserTraits",
        "getGroupId",
        "getGroupTraits",
        "startSession",
        "endSession",
        "getSessionId"
      ];
      for (var i = 0; i < methods.length; i++) {
        var method = methods[i];
        rudderanalytics[method] = (function (methodName) {
          return function () {
            rudderanalytics.push(
              [methodName].concat(Array.prototype.slice.call(arguments))
            );
          };
        })(method);
      }
    
      rudderanalytics.load(WRITE_KEY,DATA_PLANE_URL);
      rudderanalytics.page();
    </script>
    
    <script src="https://cdn.rudderlabs.com/v1.1/rudder-analytics.min.js"></script>
    

> ![info](/docs/images/info.svg)
> 
> There is an explicit `page` call at the end in all above snippets. This is to ensure that a `page` call is sent whenever the SDK loads on a page. You can remove this call or modify it with any extra `page` properties. You can also add `page` calls in your application in places not tied directly to page load, for example, virtual page views and page renders on route change, such as in single-page applications.

### Using NPM

While it is recommended to use the above method to integrate the JavaScript SDK with your website, you can alternatively use the [NPM module](<https://www.npmjs.com/package/rudder-sdk-js>) for packaging RudderStack directly into your project.

To install the JavaScript SDK via NPM, run the following command:
    
    
    npm install rudder-sdk-js --save
    

> ![warning](/docs/images/warning.svg)
> 
> Use this NPM module only for browser installation. To integrate RudderStack with your Node.js apps, refer to the [RudderStack Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>) documentation.

Since the NPM module exports the related APIs on an already-defined object combined with the Node.js module caching, you should run the following code snippet **once** and use the exported object throughout your project:
    
    
    import * as rudderanalytics from "rudder-sdk-js";
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL);
    rudderanalytics.ready(() => {
      console.log("We are all set!!!");
    });
    export { rudderanalytics };
    

Alternatively, you can do this with **ES5** using the `require` method:
    
    
    var rudderanalytics = require("rudder-sdk-js");
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL);
    rudderanalytics.ready(() => {
      console.log("We are all set!!!");
    });
    exports.rudderanalytics = rudderanalytics;
    

The related APIs exported by the module are `load`, `ready`, `identify`, `alias`, `page`, `track`, `group`, `reset`, `getAnonymousId`, `setAnonymousId`, `getUserId`, `getUserTraits`, `getGroupId`, and `getGroupTraits`.

> ![info](/docs/images/info.svg)
> 
> Refer to the sample [Angular](<https://github.com/rudderlabs/rudder-analytics-angular>) and [React](<https://github.com/rudderlabs/rudder-analytics-react>) projects for a detailed walkthrough of the above steps.

The installation code snippets discussed above perform the following actions:

  * Creates an array to store the events until the `analytics` object is ready.
  * Stores the following methods to replay them when the `analytics` object is ready:

Method| Description  
---|---  
[`load()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/>)| Loads `analytics.js` with the specified write key.  
[`track()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#track>)| Tracks user events along with the associated properties.  
[`identify()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#identify>)| Identifies the users, records their traits, and associates them with their actions.  
[`alias()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#alias>)| Maps a new user ID with an old ID.  
[`group()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#group>)| Links an identified user with a group such as a company, organization, or an account.  
[`ready()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/quick-start-guide/#step-2-check-ready-state>)| Fired when the SDK has initialized itself and the other third-party native SDK destinations.  
[`reset()`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#reset>)| Resets the information related to the previously identified user.  
`getAnonymousId`| Fetches the current `anonymousId`.  
`setAnonymousId`| Sets the `anonymousId`.  
`getUserId`| Fetches the current `userId`.  
`getUserTraits`| Fetches the current user traits.  
`getGroupId`| Fetches the current `groupId`.  
`getGroupTraits`| Fetches the current group traits.  
`startSession`| Starts a new session.  
`endSession`| Clears the `sessionId` and ends the current session.  
`getSessionId`| Fetches the session ID of the current session. Returns `null` if the session ID is not available.  
  
  * Loads the analytics object with the specified write key.
  * Makes a `page()`call to track the page views. It captures the whole URL including the UTM parameters as part of the `page` call payload, such as `path`, `referrer`, `search`, `title`, and `URL`. Refer to the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/#properties>) method to override these properties.


## Step 2: Check ready state

The JavaScript SDK provides the `ready` API with a `callback` parameter that triggers when the SDK is done initializing itself and the other third-party native SDK destinations.

An example is shown below:
    
    
    rudderanalytics.ready(() => {
        console.log("All set!");
    });
    

## Step 3: Identify users

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them with their actions. It also enables you to record any traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
        "1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
            firstName: "Alex",
            lastName: "Keener",
            email: "alex@example.com",
            phone: "+1-202-555-0146"
        }, {
            page: {
                path: "/best-seller/1",
                referrer: "https://www.google.com/search?q=estore+bestseller",
                search: "estore bestseller",
                title: "The best sellers offered by EStore",
                url: "https://www.estore.com/best-seller/1"
            }
        },
        () => {
            console.log("identify call");
        }
    );
    

The JavaScript SDK captures the `userId`, `email` and the [contextual information](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) from the above snippet.

> ![info](/docs/images/info.svg)
> 
> The anonymous visitors are automatically assigned an `anonymousId`. Refer to the [Anonymous ID](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#anonymous-id>) section for more information.

## Step 4: Track user actions

The [](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
        "Order Completed", {
            revenue: 77.6,
            currency: "USD",
        },
        () => {
            console.log("track call");
        }
    );
    

The JavaScript SDK captures the `Order Completed` event along with `revenue`, `currency`, and `anonymousId` from the above snippet.

> ![success](/docs/images/tick.svg)
> 
> You can use the `track` method to track various success metrics for your website like user signups, item purchases, article bookmarks, and more.

## Supported browsers

The JavaScript SDK supports the following browsers and their corresponding versions:

Browser| Supported Versions  
---|---  
Safari| v7 or later  
IE| v10 or later  
Edge| v80 or later  
Mozilla Firefox| v47 or later  
Chrome| v54 or later  
Opera| v43 or later  
  
> ![info](/docs/images/info.svg)
> 
> You can try adding the browser [polyfills](<https://developer.mozilla.org/en-US/docs/Glossary/Polyfill>) to your application if the SDK does not work on your browser.

## Single-page application

The JavaScript SDK makes a `page` call after its initialization (explicitly called at the end of the installation script). However, in the case of a single-page application (SPA) where a route change does not reload the page, you need to make the `page` call explicitly after the route change on the frontend. For more information, refer to the [RudderStack-Next.js Integration](<https://www.rudderstack.com/docs/user-guides/how-to-guides/rudderstack-jamstack-integration/v1.1/nextjs/#method-2-installing-and-configuring-the-javascript-sdk-using-npm-package-in-your-nextjs-app>) guide.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/load-js-sdk/>)