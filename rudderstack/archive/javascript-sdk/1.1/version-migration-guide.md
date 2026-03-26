# JavaScript SDK Version Migration

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# JavaScript SDK Version Migration

Migrate the RudderStack JavaScript SDK from v1 to v1.1.

* * *

  * __4 minute read

  * 


The latest **JavaScript SDK (v1.1)** is the lightweight, efficient, and optimized version of the SDK with a size reduction of approximately 70%, thereby increasing its loading speed considerably.

Another significant improvement in the latest version (v1.1) is that the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destinations are published as individual plugins and loaded dynamically as per the dashboard configurations. In v1, device mode destinations were bundled with the core SDK.

## Migrating to JavaScript SDK v1.1

If you have installed the JavaScript SDK v1 from the RudderStack CDN, you can simply upgrade it to v1.1 by updating the script tag in your website:

From **v1** :
    
    
    <script src="https://cdn.rudderlabs.com/v1/rudder-analytics.min.js" />
    

To **v1.1** :
    
    
    <script src="https://cdn.rudderlabs.com/v1.1/rudder-analytics.min.js" />
    

## Other migration scenarios

This section covers the detailed steps on migrating to JavaScript SDK v1.1 depending on how you installed JavaScript SDK v1.

### Forwarded/proxied RudderStack CDN

> ![success](/docs/images/tick.svg)
> 
> Refer to the [Custom Domains](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/#setup-for-serving-the-sdk>) guide to use a custom domain to forward or proxy the JavaScript SDK hosted on the RudderStack CDN.

The following steps assume that you are using AWS CloudFront to forward or proxy the RudderStack CDN:

  1. Go to **Behaviors** and verify that the sub-path `/v1.1/*` is **not configured to be blocked** in any way. This is required to ensure that both the core SDK and destination SDKs are forwarded properly.
  2. Update the script tag in your website:


From **v1** :
    
    
    <script src="https://<subdomain>.<yourdomain>.com/v1/rudder-analytics.min.js" />
    

To **v1.1** :
    
    
    <script src="https://<subdomain>.<yourdomain>.com/v1.1/rudder-analytics.min.js" />
    

### Self-hosted JavaScript SDK

To migrate the self-hosted JavaScript SDK to v1.1, follow any of these options based on your folder structure.

See [Host your JavaScript SDK in CDN/Storage](<https://www.rudderstack.com/docs/user-guides/how-to-guides/self-hosting-js-sdk/>) for details.

#### Recommended structure

In this structure, the filename for the JavaScript SDK is `rudder-analytics.min.js` and device mode destination SDKs are located next to the core SDK file under the `js-integrations` directory.

[![Recommended structure for self-hosting RudderStack&rsquo;s CDN](/docs/images/js-sdk-recommended-folder-structure.webp)](</docs/images/js-sdk-recommended-folder-structure.webp>)

To migrate to v1.1 with this setup, update the script tag in your website:
    
    
    <script src="https://<subdomain>.<yourdomain>.com/<path-to-sdk-base-directory>/rudder-analytics.min.js"></script>
    

#### Destination SDKs are located elsewhere

If the filename of your self-hosted JavaScript SDK is `rudder-analytics.min.js` but the destination SDKs are **not** located next to the core SDK file under the `js-integrations` directory, update the script tag in your website:
    
    
    <script>
    // rudderanalytics object initialization
    // provide the location of the destination SDKs in the load options
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        destSDKBaseURL: "https://<subdomain>.<yourdomain>.com/<path-to-integration-sdks-directory>"
    });
    // ...
    </script>
    <script src="https://<subdomain>.<yourdomain>.com/<path-to-sdk-base-directory>rudder-analytics.min.js"></script>
    

#### Destination SDKs are located elsewhere, alternate filename for rudderanalytics

If your JavaScript SDK file name is **not** `rudder-analytics.min.js`, and the destination SDKs are **not** located under the `js-integrations` directory, update the script tag in your website as follows:
    
    
    <script> 
    // rudderanalytics object initialization
    // provide the location of the destination SDKs in the load options
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        destSDKBaseURL: "https://<subdomain>.<yourdomain>.com/<path-to-integration-sdks-directory>"
    });
    // ...
    </script>
    <script src="https://<subdomain>.<yourdomain>.com/<path-to-custom-sdk-file>/<custom-sdk-file-name.js>"></script>
    

### Using NPM

The latest NPM package is based on the JavaScript SDK v1.1 architecture and is released with the 2.x.x version.

To update the SDK package using NPM, use any of the following options:

  * Upgrade `rudder-sdk-js` package to v1.1 using the below command:


    
    
    npm install rudder-sdk-js@2.x.x
    

  * Manually modify the **package.json** file like below and run `npm install`:


    
    
    "dependencies": {
      "rudder-sdk-js": "^2.x.x"
    }
    

## Loading device mode destinations

Depending on the dashboard settings, all destination SDKs are loaded from <https://cdn.rudderlabs.com/v1.1/js-integrations/> by default. You can locate a specific destination SDK at <https://cdn.rudderlabs.com/v1.1/js-integrations/><destination_name>.min.js.

For example, the path for HubSpot is: <https://cdn.rudderlabs.com/v1.1/js-integrations/HubSpot.min.js>, and Google Analytics is: <https://cdn.rudderlabs.com/v1.1/js-integrations/GA.min.js>, etc.

However, if you are loading device mode destinations from a custom path using any of the below methods:

  * Forwarded/proxied RudderStack CDN
  * Self-hosted JavaScript SDK


Then, pass the custom path for the required device mode destination in the `destSDKBaseURL` option in the SDK’s `load()` call:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        destSDKBaseURL: "<custom-path-for-device-mode-destination>", // ex: "https://cdn.<yourdomain>.com/js-integrations"
        ...otherOptions
    });
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) in the snippet with their actual values.

## FAQ

#### How are the destination SDKs loaded in v1.1?

In v1.1, the core JavaScript SDK does not contain any destination-specific SDKs by default. It fetches them dynamically from the [hosted location](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/version-migration-guide/#loading-device-mode-destinations>), depending on the device mode destinations configured in your dashboard (control plane).

#### How does RudderStack determine the root location of the destination SDK?

RudderStack follows the below precedence order while determining the root location of the destination SDK:

  1. It refers to the `destSDKBaseURL` value in the `options` parameter of the `load` API call.
  2. If absent, it checks the `src` attribute of the `<script>` tag (that adds the core JavaScript SDK to your website) if `/js-integrations` is automatically appended to the root location.
  3. If none of the above options are applicable, it uses the default CDN URL: `https://cdn.rudderlabs.com/v1.1/js-integrations/`.


  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/filtering/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/detecting-adblocked-pages/>)