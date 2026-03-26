# JavaScript SDK Quickstart

> Version: Latest (v3)v1.1

# JavaScript SDK Quickstart

Your first steps with the RudderStack JavaScript SDK.

* * *

  * __5 minute read

  * 


In this tutorial, you’ll learn how to install RudderStack JavaScript SDK on your website and send your first `page`, `identify`, and `track` events.

## Prerequisites

  * Sign up for [RudderStack Cloud](<https://app.rudderstack.com/signup>).
  * [Set up a JavaScript source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the RudderStack dashboard. You’ll need the **Write Key** and **Data Plane URL** from the source settings page.


## Step 1: Install the JavaScript SDK

You can install the SDK using the simple CDN method (recommended for getting started quickly) or via NPM if you’re using a package manager in your project. Choose the method that best suits your setup.

> ![info](/docs/images/info.svg)
> 
> Most code snippets in this guide assume the SDK is available globally as `rudderanalytics`, which is the default when using the CDN installation method. If you use NPM, ensure you import or access your initialized `rudderAnalytics` object correctly in the subsequent steps.

**Option 1: Install using CDN (Recommended)**  


This is the simplest way to get started. The SDK will load asynchronously without blocking your page content.

  1. Go to the **Setup** tab of your JavaScript source in the [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Find the installation snippet. It already includes your unique **Write Key** and **Data Plane URL**.
  3. Click **Copy snippet** (using either the **Minified** or **Original** version).
  4. Paste the snippet into the `<head>` section of your website’s HTML.

![JavaScript SDK snippet from RudderStack dashboard](/docs/images/get-started/quickstart/js-sdk-snippet.webp)

The installation code snippet (seen above) contains both the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) by default.

The SDK will then automatically load and initialize — you can access it via the global `window.rudderanalytics` object.

See the [JavaScript SDK Installation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/>) guide for more details on advanced loading options (like loading synchronously or specific versions).

**Option 2: Using NPM**  


You can also use the [@rudderstack/analytics-js NPM module](<https://www.npmjs.com/package/@rudderstack/analytics-js>) for packaging RudderStack directly into your project.

> ![warning](/docs/images/warning.svg)
> 
> Use this NPM module only for browser applications. For Node.js server-side applications, use the [Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>).

  1. Install the package:


    
    
    npm install @rudderstack/analytics-js --save
    

  2. Import and initialize the SDK **once** in your project. Replace `YOUR_WRITE_KEY` and `YOUR_DATA_PLANE_URL` with the actual [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) values from your RudderStack source settings.

     * **For ECMAScript modules (ESM)** :
           
           import { RudderAnalytics } from '@rudderstack/analytics-js';
           
           const rudderAnalytics = new RudderAnalytics();
           
           // Load the SDK with your Write Key and Data Plane URL
           rudderAnalytics.load('YOUR_WRITE_KEY', 'YOUR_DATA_PLANE_URL', {});
           
           // Export for use in other parts of your app
           export { rudderAnalytics };
           

     * **For CommonJS (CJS) using`require`**:
           
           var RudderAnalytics = require("@rudderstack/analytics-js");
           
           const rudderAnalytics = new RudderAnalytics();
           
           // Load the SDK with your Write Key and Data Plane URL
           rudderAnalytics.load('YOUR_WRITE_KEY', 'YOUR_DATA_PLANE_URL', {});
           
           // Export for use in other parts of your app
           exports.rudderAnalytics = rudderAnalytics;
           

  3. Use the exported `rudderAnalytics` object consistently throughout your project for subsequent calls.


  


> ![success](/docs/images/tick.svg)
> 
> See the [RudderStack JavaScript SDK repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples>) for sample applications using different installation methods.

## Step 2: Track current page

To record which page the user is currently viewing, use the [`page`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#page>) call. You can add specific details about the page, although the SDK automatically captures information like the page URL and title.

> ![warning](/docs/images/warning.svg)
> 
> If you are migrating from an older version of the SDK (before v1.1), note that there is no automatic [`page`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#page>) call embedded in the loading scripts anymore. You will need to add the `page` call manually.
> 
> See the [Breaking Changes](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/breaking-changes/>) guide for more information.
    
    
    // Basic page call (SDK captures URL, path, title automatically)
    rudderanalytics.page();
    
    // Page call with custom name, category, and properties
    rudderanalytics.page(
      "Cart", // Category (optional)
      "Cart Viewed", // Name (optional)
      { // Properties (optional)
        path: "/best-seller/1",
        referrer: "https://www.google.com/",
        search: "estore bestseller",
        title: "EStore Best Sellers",
        url: "https://www.estore.com/best-seller/1"
      },
      () => { // Callback (optional)
        console.log("Page event successfully submitted.");
      }
    );
    

> ![info](/docs/images/info.svg)
> 
> The SDK automatically captures fields like `path`, `referrer`, `search`, `title`, and `url`. You only need to provide them in the `page` call if you want to override the automatically captured values.

Need to track views in a Single-Page Application (SPA)?

If your website is a Single-Page Application (built with frameworks like React, Angular, Vue, etc.), the page doesn’t fully reload when the user navigates between views.

You need to **manually call`rudderanalytics.page()`** every time the route changes within your application. How you do this depends on your specific framework’s router.

Check out [RudderStack-Next.js Integration](<https://www.rudderstack.com/docs/user-guides/how-to-guides/rudderstack-jamstack-integration/v3/nextjs/>) for inspiration.

## Step 3: Identify users

To associate events with a specific user, use the [`identify`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#identify>) call. Provide a unique `userId` and any traits you know about them, like name or email.
    
    
    rudderanalytics.identify(
      "user-12345", // Unique User ID
      { // User Traits (optional)
        firstName: "Alex",
        lastName: "Keener",
        email: "alex@example.com",
        phone: "+1-202-555-0146"
      },
      () => { // Callback (optional)
        console.log("Identify event successfully submitted.");
      }
    );
    

Calling `identify` links subsequent events to this user ID. If you don’t provide a `userId`, RudderStack automatically assigns an `anonymousId` to track the user before they are known. See [User Identification](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#identify>) for more details.

## Step 4: Track user actions

To record specific actions users take on your site, use the [`track`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#track>) call. Give the event a name and include any relevant properties.
    
    
    // Example: Tracking a completed order
    rudderanalytics.track(
      "Order Completed", // Event Name
      { // Event Properties (optional)
        revenue: 39.95,
        currency: "USD",
        productId: "product-xyz",
        quantity: 1
      },
      () => { // Callback (optional)
        console.log("Track event successfully submitted.");
      }
    );
    
    // Example: Tracking a button click
    rudderanalytics.track(
      "Signup Button Clicked",
      {
        location: "Homepage Hero"
      }
    );
    

> ![success](/docs/images/tick.svg)
> 
> You’ve now successfully installed the SDK and sent your first events! You can use the `track` method to record various user interactions important for your business, such as signups, purchases, form submissions, or video plays.

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/>)