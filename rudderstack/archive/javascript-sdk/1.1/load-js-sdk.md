# Load JavaScript SDK

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# Load JavaScript SDK

Load the JavaScript SDK.

* * *

  * __11 minute read

  * 


You can load the JavaScript SDK using the `load` API method to track and send events from your website to RudderStack. It can be defined as:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, [loadOptions]);
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values in the snippets (wherever applicable) throughout this guide.

## Loading options

You can use **loadOptions** in the above `load` call to define various options while loading the SDK. It includes the following parameters:
    
    
    {
      logLevel: "DEBUG" | "INFO" | "WARN",
      integrations: IntegrationOpts,
      configUrl: string,  // defaults to https://api.rudderlabs.com
      getSourceConfig: function,
      queueOptions: QueueOpts,
      loadIntegration: boolean, // defaults to true.
      sessions: SessionOpts,
      secureCookie: boolean, // defaults to false.
      destSDKBaseURL: string, // defaults to https://cdn.rudderlabs.com/v1.1/js-integrations
      useBeacon: boolean, // defaults to false.
      beaconQueueOptions: BeaconQueueOpts,
      cookieConsentManager: cookieConsentManager,
      anonymousIdOptions: AnonymousIdOptions,
      setCookieDomain: string, // defaults to current domain.
      sameSiteCookie: "Strict" | "Lax" | "None", // defaults to Lax.
      lockIntegrationsVersion: boolean, // defaults to false.
      polyfillIfRequired: boolean, // defaults to true.
      onLoaded: callback function,
      uaChTrackLevel: "none" | "default" | "full", // defaults to None.
      sendAdblockPage: boolean,
      sendAdblockPageOptions: object,
      useGlobalIntegrationsConfigInEvents: boolean // defaults to false.
      sameDomainCookiesOnly: boolean // defaults to false.
    }
    

The detailed description of these parameters is as follows:

Parameter| Type| Description  
---|---|---  
`logLevel`| String| Values include `DEBUG`, `INFO`, and `WARN`.  
`integrations`| IntegrationOpts| Sends event data to the [selective destinations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/filtering/>).  
`configUrl`| String| The [Control Plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) endpoint serving your destination configurations. Default value is `https://api.rudderlabs.com`. Note that `sourceConfig` is automatically appended to this endpoint in the format `https://api.rudderlabs.com/<source_config_url>/sourceConfig`  
`getSourceConfig`| Function| Returns a custom configuration which can be used in place of the [control plane’s dashboard](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) configuration.  
`queueOpts`| QueueOpts| Contains the options to control the behavior of the persistence queue that buffers the events before sending them to the data plane.  
`loadIntegration`| Boolean| Determines whether the destination SDKs are fetched by the SDK. Default value is `true`. Supported for **Amplitude** and **Google Analytics** only.  
`sessions`| SessionOpts| Captures the details specific to session tracking.  
`secureCookie`| Boolean| Determines whether the SDK sends the cookie to the storage backend via HTTPS. Default value is `false`.  
`destSDKBaseURL`| String| Path used by the SDK to load the integrations. Default value is `https://cdn.rudderlabs.com/v1.1/js-integrations`. [Reference](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/version-migration-guide/#case-3-self-hosting-rudderstacks-cdn>).  
`useBeacon`| Boolean| Determines whether the SDK [sends event payloads via Beacon](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/javascript-sdk-enhancements/#sending-events-using-beacon>). Default value is `false`.  
`beaconQueueOptions`| [BeaconQueueOpts](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/javascript-sdk-enhancements/#sending-events-using-beacon>)| Internal queue to hold the data and send it through the Beacon utility in batches.  
`cookieConsentManager`| Object| See the Consent manager integration section.  
`anonymousIdOptions`| Object| Automatically captures the anonymous ID from a source and sets it as RudderStack’s `anonymousId`.  
`setCookieDomain`| String| Sets the cookie domain. SDK captures and uses the current domain as the default value. Refer to the [Data Storage](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/data-storage-cookies/>) guide for more information.  
`sameSiteCookie`| String| Sets the `SameSite` attribute of a cookie. Default value is `Lax`.  
`lockIntegrationsVersion`| Boolean| Determines if the JavaScript SDK should use the version of the native destination SDKs as used by the core SDK. This is particularly useful for [NPM installations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/quick-start-guide/#using-npm>) where a specific version of the core SDK is used. The default value is `false`, meaning the latest versions of the destination SDKs are used in case of both CDN and NPM installations. Note that if `destSDKBaseURL` is set to a specific path, it gets the highest priority.  
`polyfillIfRequired`| Boolean| Loads the polyfills for unsupported features in older browsers. Default value is `true`.  
`onLoaded`| Function| Callback function that executes after the JavaScript SDK loads and before the native device-mode destination SDKs load.  
`uaChTrackLevel`| String| Configures the information a user should get in the `context` object regarding the [client hints](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints>). The JavaScript SDK fetches this information using the [user-agent client hints API](<https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API>).  
`sendAdblockPage`| Boolean| Enables the JavaScript SDK to load the [Google AdSense](<https://adsense.google.com/start/>) library. If RudderStack fails to load this library, it concludes that an adblocker is enabled on the page. [Reference](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/detecting-adblocked-pages/>).  
`sendAdblockPageOptions`| Object| If the `sendAdblockPage` option is set to true, the JavaScript SDK makes an implicit `page` call about the ad-blocked pages. You can use the `sendAdblockPageOptions` option (containing the [`IntegrationOpts`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#integrationopts>) object) to specify the destinations to which you want to forward this `page` call. [Reference](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/detecting-adblocked-pages/>).  
`useGlobalIntegrationsConfigInEvents`| Boolean| Lets you use the `integrations` object of the `load` method at the event level when it is not present at the event level. Default value is `false`.  
`sameDomainCookiesOnly`| Boolean| If set to true, the SDK reads cookies from the exact domain it is set at. Default value is `false`.  
  
For example, if this load option is set to true then the cookies set from the site’s top-level domain are not accessible by the sub-domains and vice versa.  
  
The following sections contain the detailed definitions and usage of some of the above parameters:

#### `IntegrationOpts`

You can use this parameter to send the event data only to the [selective destinations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/filtering/#filtering-destinations>). Its structure is defined as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: boolean, // default true
        <Destination1>: boolean, // or object.
        <Destination2>: boolean, // or object.
        ...
      }
    });
    

The following table describes the above (optional) parameters in detail:

**Parameter**| **Type**| **Description**  
---|---|---  
`All`| Boolean| All destinations to which the event data must be sent. The default value is `true`. If set to `false`, RudderStack will not send the event data to any destination.  
`<Destination>`| Boolean| Specific destination to which the event data must be sent/not, depending on its Boolean value.  
  
You **must** specify the actual destination name (as listed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>)) in the `<Destination>` parameter and **not** the name you have assigned to the destination. For example, the below sample snippet sends the event data only to **Amplitude** and **Intercom** destinations:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        integrations: {
            All: false,
            "Amplitude": true,
            "Intercom": true
        }
    });
    

#### `getSourceConfig`

The `getSourceConfig` function returns the custom configuration which can be used in place of [control plane’s dashboard](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) configuration:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      getSourceConfig: function() {
        return {
          // custom configuration
        };
      },
      // other load options
    });
    

#### `QueueOpts`

The `queueOpts` object contains the options to control the behavior of the persistence queue that buffers the events before sending them to RudderStack. Its structure is defined as follows:
    
    
    {
      maxRetryDelay: 360000,
      minRetryDelay: 1000,
      backoffFactor: 2,
      maxAttempts: 10,
      maxItems: 100,
    }
    

The following table describes the above `integer` type (optional) parameters in detail:

**Parameter**| **Description**| **Default value**  
---|---|---  
`maxRetryDelay`| Upper limit on the maximum delay for an event (in ms).| 360000  
`minRetryDelay`| Minimum delay expected before sending an event (in ms).| 1000  
`backoffFactor`| Exponential base.| 2  
`maxAttempts`| Maximum number of attempts to send the event to the destination.| 10  
`maxItems`| Maximum number of events kept in the storage.| 100  
  
#### `SessionOpts`

The `SessionOpts` object contains the options related to the SDK’s automatic session tracking behavior. Refer to the [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#automatic-session-tracking>) guide for more information. Its structure is defined as follows:

**Parameter**| **Description**| **Default value**  
---|---|---  
`autoTrack`| Determines if the SDK should automatically track the user sessions.| `true`  
`timeout`| The maximum inactivity period before the session expires.| `1800000 ms` (30 minutes)  
  
#### `cookieConsentManager`

Once a user provides the consent, you can load the JavaScript SDK and enable the [OneTrust integration](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>) via the `cookieConsentManager` object:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      cookieConsentManager: {
        oneTrust: {
          enabled: true
        }
      }
    });
    

#### `anonymousIdOptions`

You can use the `anonymousIdOptions` object to automatically capture the anonymous ID from a source and set it as RudderStack’s `anonymousId`.

For example, if you are migrating from a particular source and want to retain its anonymous ID, you can enable the `anonymousIdOptions` to set the source’s anonymous ID as the `anonymousId` in RudderStack.

The structure of `anonymousIdOptions` is defined as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      anonymousIdOptions: {
        autoCapture: {
          enabled: true,
          source: "segment"
        }
      }
    });
    

The following table describes the above (required) parameters in detail:

Parameter| Type| Description  
---|---|---  
`enabled`| Boolean| Determines if the anonymous ID should be auto-captured.  
`source`| String| Determines the external source of anonymous ID.  
  
> ![info](/docs/images/info.svg)
> 
> If the RudderStack `anonymousId` is already set in your browser, `anonymousIdOptions` will not take effect.

> ![info](/docs/images/info.svg)
> 
> You can call the **reset** API to clear the persisted anonymous ID and force the SDK to generate a new ID when the next tracking API is called (irrespective of whether `anonymousIdOptions` is enabled or disabled). However, if the `anonymousIdOptions` object is enabled and the SDK is loaded again (as a result of webpage reload, navigate to a different webpage, etc.), the `setAnonymousId` call will trigger automatically and the specified source’s anonymous ID will again be set as the RudderStack `anonymousId`.

#### `uaChTrackLevel`

You can use the `uaChTrackLevel` option to configure the information a user should get in the `context` object regarding the [client hints](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints>). The JavaScript SDK fetches this information using the [user-agent client hints API](<https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API>). It can take the below values:

  * `none`: Specifies that `uaChTrackLevel` field is absent in the `context` object.
  * `default`: Specifies that `uaChTrackLevel` field is present in the `context` object and contains an object similar to the one below:


    
    
    {
      "brands": [{
        "brand": "Chromium",
        "version": "110"
      }, {
        "brand": "Not A(Brand",
        "version": "24"
      }, {
        "brand": "Google Chrome",
        "version": "110"
      }],
      "mobile": false,
      "platform": "macOS"
    }
    

  * `full`: Specifies that `uaChTrackLevel` field is present in the `context` object and contains an object similar to the one below:


    
    
    {
      "architecture": "arm",
      "bitness": "64",
      "brands": [{
        "brand": "Chromium",
        "version": "110"
      }, {
        "brand": "Not A(Brand",
        "version": "24"
      }, {
        "brand": "Google Chrome",
        "version": "110"
      }],
      "fullVersionList": [{
        "brand": "Chromium",
        "version": "110.0.5481.77"
      }, {
        "brand": "Not A(Brand",
        "version": "24.0.0.0"
      }, {
        "brand": "Google Chrome",
        "version": "110.0.5481.77"
      }],
      "mobile": false,
      "model": "",
      "platform": "macOS",
      "platformVersion": "13.1.0",
      "uaFullVersion": "110.0.5481.77",
      "wow64": false
    }
    

#### `onLoaded`

The `onLoaded` callback function takes the `rudderanalytics` instance as an argument and executes after the JavaScript SDK loads and before the native device-mode destination SDKs are loaded.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      onLoaded: function(rudderanalytics) {
        console.log("All set!");
      }
    });
    

#### `useGlobalIntegrationsConfigInEvents`

You can use this option to use the `integrations` object of the `load` method at the event level when it is not present at the event level.

For example, if the `integrations` object is defined in the `load` method and the `useGlobalIntegrationsConfigInEvents` option is set to `true`:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: true,
        "Google Analytics": false,
        ...
      },
      useGlobalIntegrationsConfigInEvents: true,
      // other load options
    });
    

**Case 1** : `integrations` option is present at the event level:
    
    
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345
      }, {
        integrations: {
          All: true,
          Amplitude: false
        },
      },
      () => {
        console.log("track call");
      }
    );
    

In this case, the JavaScript SDK uses the `integrations` option from the `track` event.

**Case 2** : `integrations` option is not present at the event level:
    
    
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345
      }, {},
      () => {
        console.log("track call");
      }
    );
    

In this case, the SDK uses the `integrations` option from the `load` method.

## Loading SDK for self-hosted control plane

If you are self-hosting the control plane using the [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#using-sdk-sources-set-up-in-self-hosted-control-plane>) utility, the `load` call should be made as below:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      configUrl: < CONTROL_PLANE_URL > ,
    });
    

## Verifying if the SDK has loaded correctly

You can verify if the JavaScript SDK has loaded correctly by opening the JavaScript console in your browser:

  * **Safari** : `Ctrl+Alt+I` (Windows) or `Command+Option+I` (Mac) and go to the `Console` tab.
  * **Chrome** : `Ctrl+Shift+J` (Windows) or `Command+Option+J` (Mac).
  * **Firefox** : `Ctrl+Shift+K` (Windows) or `Command+Option+K` (Mac) and select the `Console` tab.
  * **Internet Explorer** : Press `F12` and go to the `Console` tab.


Run the `rudderanalytics` command in the console. If it returns the following code snippet, it means that the `analytics.js` file has loaded successfully:
    
    
    {Integrations: Object, _integrations: Object, _readied: true, _timeout: 300, _user: n_}
    

If it gives an `undefined` error, you need to verify the SDK installation.

## Allowlist destination domain

While using the JavaScript SDK with destinations supporting the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you might need to allowlist the domain from where the destination SDK will load in your content security policy (CSP).

> ![info](/docs/images/info.svg)
> 
> A content security policy adds an extra layer of protection from any type of cross-site scripting, clickjacking, and data injection attacks.

See the specific [destination’s documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) to obtain the domain to be allowlisted. For example, [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#connection-mode>).

RudderStack expects the following (minimum) CSP header configuration to load the JavaScript SDK without any errors:
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

If you don’t want to allow unsafe inline and use the CDN package with its loading snippet, use `nonce` attribute to the script tag for the loading snippet:
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'nonce-rAnd0m' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

In case you use the npm package, no inline loading snippet is required:
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

## Tracking user sessions

By default, the JavaScript SDK automatically tracks the user sessions. This means that RudderStack automatically determines the start and end of a user session depending on the inactivity time configured in the SDK (default time is 30 minutes).
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sessions: {
        autoTrack: true,
        timeout: 10 * 60 * 1000,  // 10 min in milliseconds
      },
      ...<otherLoadOptions>
    });
    

To disable automatic session tracking, you can set the load option `autoTrack` to `false`.

For more information on the user sessions and how to track them using the JavaScript SDK, refer to the [Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/>) guide.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/quick-start-guide/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/supported-api/>)