# Self-host JavaScript SDK in Your CDN

Steps on self-hosting and setting up the JavaScript SDK in your CDN.

* * *

  * __4 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends serving the JavaScript SDK on your [own domain](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/>) over self-hosting it, especially to defend against the adblockers.
> 
> Self-hosting the SDK is only recommended in cases where you want to create a zero-gap architecture and ensure no data goes out to any external service.

This guide walks you through the steps for self-hosting the RudderStack JavaScript SDK.

## Prerequisites: Directory structure

For self-hosting the JavaScript SDK, RudderStack **recommends** following the below directory structure (as present in RudderStack’s CDN) to place the SDK and the associated files:

[![Recommended directory structure for self-hosting RudderStack JavaScript SDK v3](/docs/images/event-stream-sources/sdk-directory-structure.webp)](</docs/images/event-stream-sources/sdk-directory-structure.webp>)

In this structure, there are two directories - **v3** and **3.x.y** (denoting the specific [SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>)) - within the base directory.

Folder name| Description  
---|---  
v3| Contains the core SDK files - `rsa.min.js` and `rsa.min.js.map`.  
3.x.y| Contains the device mode integrations and plugins.  
  
Each of the above folders folders has two subdirectories - **modern** and **legacy**.

> ![info](/docs/images/info.svg)
> 
> The SDK bundle in the **modern** directory is built for ES2015, while the **legacy** bundle is for ES5, with all the plugins bundled into the core SDK.

The **modern** folder within **3.x.y** further contains the following subdirectories:

Folder name| Description  
---|---  
js-integrations| Directory for storing the device mode destination SDKs.  
plugins| Directory for storing the plugins.  
  
## Setup

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends downloading and hosting **all** the device mode destination SDKs, plugins, and source map files to help with troubleshooting.

### 1\. Download core SDK files

Download the [JavaScript SDK](<https://cdn.rudderlabs.com/v3/modern/rsa.min.js>) and save it as `rsa.min.js`. Also, download the [corresponding source map file](<https://cdn.rudderlabs.com/v3/modern/rsa.min.js.map>), and save it as `rsa.min.js.map`.

> ![warning](/docs/images/warning.svg)
> 
> Note that the above URLs point to the latest version of the SDK (v3).
> 
> To download the latest SDK version, replace `v3` in the URL with the required [SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>).
> 
> For example, the URLs for fetching the `rsa.min.js` and `rsa.min.js.map` files for the SDK v3.15.1 would be as follows:
>     
>     
>     https://cdn.rudderlabs.com/3.15.1/modern/rsa.min.js
>     https://cdn.rudderlabs.com/3.15.1/modern/rsa.min.js.map
>     

Then, place these files in the **v3** > **modern** / **legacy** folder within your base directory, as applicable.

### 2\. Download device mode integrations

Download the required device mode destination SDK files along with the corresponding source map file from the RudderStack CDN (`https://cdn.rudderlabs.com/`) using the below URL:
    
    
    https://cdn.rudderlabs.com/3.x.y/<bundle>/js-integrations/list.html
    

In the above URL, make sure to replace:

  * `3.x.y` with the required [SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>).
  * `<bundle>` with the desired SDK bundle (`modern` or `legacy`).


For example, the URL to download the device mode integrations for the modern bundle for SDK v3.15.1 would be as follows:
    
    
    https://cdn.rudderlabs.com/3.15.1/modern/js-integrations/list.html
    

Then, place the downloaded files in the **3.x.y** > **modern** / **legacy** > **js-integrations** folder, as applicable.

### 3\. Download plugins

> ![info](/docs/images/info.svg)
> 
> This section is applicable only for the **modern** bundle.

Download the required plugin files along with the corresponding map files from the RudderStack CDN using the below URL:
    
    
    https://cdn.rudderlabs.com/3.x.y/modern/plugins/list.html
    

In the above URL, make sure to replace `3.x.y` with the required [SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>).

For example, the URL to download the plugins for the SDK v3.15.1 would be as follows:
    
    
    https://cdn.rudderlabs.com/3.15.1/modern/plugins/list.html
    

Then, place the downloaded files in the **3.x.y** > **modern** > **plugins** folder.

### 4\. Update SDK loading snippet

  * Update `sdkBaseUrl` in the [SDK loading snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#asynchronous-loading>) to:


    
    
    var sdkBaseUrl = "https://<subdomain>.<yourdomain>.com/<base-directory-path>";
    

Note that the SDK loading snippet automatically appends `/v3/` to the `sdkBaseUrl` path in accordance with the recommended directory structure.

If you have placed the core SDK files in a structure that is different to the recommended directory structure, make sure to update the `sdkVersion` variable in the snippet accordingly.

For example, if your **modern** folder is placed within a subdirectory called **custom-version-id** instead of **v3** , then your updated SDK loading snippet should look like:
    
    
    var sdkBaseUrl = "https://<subdomain>.<yourdomain>.com/<base-directory-path>";
    var sdkVersion = "custom-version-id";
    

  * If your JavaScript SDK file name is **not** `rsa.min.js`, then update `sdkFileName` in the loading snippet to:


    
    
    var sdkFileName = "<custom-file-name>.min.js";
    

[![Updating sdkBaseURL](/docs/images/event-stream-sources/sdkbaseurl-update.webp)](</docs/images/event-stream-sources/sdkbaseurl-update.webp>)

#### Example

  * Base directory: **rs-js-sdk-artifacts**
  * Subdirectory: **custom-version-id** (instead of the recommended **v3**)
  * SDK file name: `customsdk.min.js`


Then, update the [SDK loading snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#asynchronous-loading>) as follows:
    
    
    var sdkBaseUrl = "https://<subdomain>.<yourdomain>.com/rs-js-sdk-artifacts";
    var sdkVersion = "custom-version-id";
    var sdkFileName = "customsdk.min.js";
    

Then, the final URL would be:
    
    
    https://<subdomain>.<yourdomain>.com/rs-js-sdk-artifacts/custom-version-id/customsdk.min.js
    

## Load device mode destinations and plugins

If you’ve installed the SDK via CDN and have retained the recommended directory and file structure, the SDK automatically determines the location of the device mode destinations and plugins.

Otherwise, provide location of the destination SDKs via the `destSDKBaseURL` [`load` API option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>):
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      destSDKBaseURL: "https://<subdomain>.<yourdomain>.com/<integration-sdks-directory-path>"
    });
    

Similarly, you can provide the location of the plugins via the `pluginsSDKBaseURL` [`load` API option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>):
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      pluginsSDKBaseURL: "https://<subdomain>.<yourdomain>.com/<plugins-directory-path>"
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to replace `WRITE_KEY` and `DATA_PLANE_URL` with their actual values.