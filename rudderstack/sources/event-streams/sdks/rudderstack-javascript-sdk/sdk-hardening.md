# Harden JavaScript SDK

> Version: Latest (v3)v1.1

# Harden JavaScript SDK

Steps to configure a hardened version of the JavaScript SDK.

* * *

  * __2 minute read

  * 


This guide walks you through the steps of setting up and configuring a hardened version of your JavaScript SDK. These steps focus on minimizing the SDK’s reliance on external resources that could be used as an attack surface to disrupt events flow or compromise the app, thereby enhancing security.

## SDK hardening steps

  1. Use a named export that bundles plugins while [packaging RudderStack directly in your project](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>) using NPM. By using the NPM package export that bundles the plugins code, the SDK **does not** make any request to dynamically download the plugins.


> ![info](/docs/images/info.svg)
> 
> You can also:
> 
>   * [Self-host the plugin files and integration SDKs](<https://www.rudderstack.com/docs/user-guides/how-to-guides/self-hosting-js-sdk/>) and serve them over your domain.
>   * Proxy the RudderStack domains and [use your own domain](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/>) to serve the JavaScript SDK.
> 

    
    
    import { RudderAnalytics } from '@rudderstack/analytics-js/bundled';
    
    
    
    var RudderAnalytics = require("@rudderstack/analytics-js/bundled");
    

  2. Override/mock source configuration data. By mocking the source configuration response to the SDK, RudderStack **does not** make any source configuration request again.


    
    
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      polyfillIfRequired: false,
      getSourceConfig: () => ({
        updatedAt: new Date().toISOString(),
        source: {
          // Use relevant valid values from the RudderStack dashboard
          name: SOURCE_NAME,
          id: SOURCE_ID,
          workspaceId: WORKSPACE_ID,
          writeKey: WRITE_KEY,
          updatedAt: new Date().toISOString(),
          config: {
            statsCollection: {
              errors: {
                enabled: false
              },
              metrics: {
                enabled: false
              }
            }
          },
          enabled: true,
          destinations: []
        }
      })
    });
    

  3. Disable the loading of polyfills by setting `polyfillIfRequired` to `false`. By disabling polyfills, the SDK **does not** dynamically add a polyfills script from a third-party domain.


    
    
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      polyfillIfRequired: false
    });
    

RudderStack also recommends using only the cloud mode destinations to avoid loading any other third-party SDKs on the website.

## Final instrumentation
    
    
    import { RudderAnalytics } from '@rudderstack/analytics-js/bundled';
    
    const rudderAnalytics = new RudderAnalytics();
    
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      polyfillIfRequired: false,
      getSourceConfig: () => ({
        updatedAt: new Date().toISOString(),
        source: {
          // Use relevant valid values from the RudderStack dashboard
          name: SOURCE_NAME,
          id: SOURCE_ID,
          workspaceId: WORKSPACE_ID,
          writeKey: WRITE_KEY,
          updatedAt: new Date().toISOString(),
          config: {
            statsCollection: {
              errors: {
                enabled: false
              },
              metrics: {
                enabled: false
              }
            }
          },
          enabled: true,
          destinations: []
        }
      })
    });
    
    export { rudderAnalytics };
    
    
    
    var RudderAnalytics = require("@rudderstack/analytics-js/bundled");
    
    const rudderAnalytics = new RudderAnalytics();
    
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      polyfillIfRequired: false,
      getSourceConfig: () => ({
        updatedAt: new Date().toISOString(),
        source: {
          // Use relevant valid values from the RudderStack dashboard
          name: SOURCE_NAME,
          id: SOURCE_ID,
          workspaceId: WORKSPACE_ID,
          writeKey: WRITE_KEY,
          updatedAt: new Date().toISOString(),
          config: {
            statsCollection: {
              errors: {
                enabled: false
              },
              metrics: {
                enabled: false
              }
            }
          },
          enabled: true,
          destinations: []
        }
      })
    });
    
    exports.rudderAnalytics = rudderAnalytics;
    

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/new-features/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/>)