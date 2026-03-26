# Load JavaScript SDK

> Version: Latest (v3)v1.1

# Load JavaScript SDK

Understand the different SDK load options.

* * *

  * __25 minute read

  * 


You can load the JavaScript SDK using the `load` API method to track and send events from your website to RudderStack.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, [loadOptions]);
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) with their actual values in the snippets (wherever applicable) throughout this guide.

## Loading options

You can use the `loadOptions` object in the above `load` call to define various options while loading the SDK. It includes the following **optional** parameters:

Parameter| Type| Description  
---|---|---  
`anonymousIdOptions`| Object| Automatically captures the anonymous ID from a source and sets it as RudderStack’s `anonymousId`.  
`autoTrack`| Object| Determines whether to enable or disable page tracking globally and at the page level, providing flexible control over tracking behaviors.  
  
See Autotrack page view metrics for more information.  
`beaconQueueOptions`| BeaconQueueOpts| Controls the behavior of the queue that buffers events before sending them through the Beacon utility in batches. The SDK lets you configure these batching options.  
`configUrl`| String| The [control plane](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#control-plane>) endpoint serving your destination configurations.  
  
**Default value** : `https://api.rudderstack.com`.  
Note that the SDK automatically appends `/sourceConfig` at the end if it is missing, for example, `<configURL>/sourceConfig`.  
`consentManagement`| Object| Lets you specify the consent management preferences. See Consent manager integration for more information.  
`destSDKBaseURL`| String| URL used by the SDK to load its integration SDKs.  
  
**Default value** : The CDN path or automatically determined based on core SDK URL.  
`destinationsQueueOptions`| Object| See `destinationsQueueOptions` for more information.  
`externalAnonymousIdCookieName`| String| Name of the cookie for the SDK to fetch the anonymous ID and use it as RudderStack’s `anonymousId`.  
  
See `externalAnonymousIdCookieName` for more information.  
`getSourceConfig`| Function| Returns custom configuration data to use instead of making a request to the control plane.  
`integrations`| IntegrationOpts| Sends event data to the [selective destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>).  
`loadIntegration`| Boolean| Determines whether to load the native destination SDKs. Supported for [Amplitude](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/>) and [Google Analytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-ga/>) destinations only. If set to `false`, the SDK assumes that the destination SDK is already loaded on your site and proceeds to initialize and forward data to it.  
  
**Default value** : `true`  
`logLevel`| String| Values include `LOG`, `INFO`, `DEBUG`, `WARN`, `ERROR`, and `NONE`.  
  
**Default value** : `ERROR`  
`onLoaded`| Function| Callback function that executes after the SDK loads and before the device mode destination SDKs are loaded.  
`plugins`| String array| List of plugins you want the SDK to load.  
  
See Plugins for more information.  
  
**Default value** : Array of all the plugins names.  
`pluginsSDKBaseURL`| String| Base URL path used by SDK to load the plugins.  
  
**Default value** : Standard CDN path or automatically determined from the core SDK location.  
`polyfillIfRequired`| Boolean| Loads the polyfills for unsupported features in older browsers.  
  
**Default value** : `true`.  
`polyfillURL`| String| URL to load polyfills from, not necessarily from the default polyfills service.  
  
**Default value** : `https://polyfill-fastly.io/v3/polyfill.min.js` with dynamic calculation of missing features from the browser.  
  
**Example** : Suppose your browser is missing the following features required by the SDK:

  * `Array.includes`
  * `String.startsWith`
  * `Promise`

Then the polyfill URL will look like this (not exactly):  
`https://polyfill-fastly.io/v3/polyfill.min.js?features=Array.prototype.includes%2CString.prototype.startsWith%2CPromise.`  
`queueOpts`| QueueOpts| Contains the options to control the behavior of the persistence queue that buffers the events before sending them to the data plane.  
`sameDomainCookiesOnly`| Boolean| Enables strict domain-level cookie scoping for the SDK cookies.  
  
**Default value** : `false` — the SDK stores cookies at the top-level domain (for example, `.example.com`), allowing them to be shared across all subdomains (for example, `app.example.com`, `blog.example.com`).  
  
When set to `true`, the SDK sets cookies only for the exact domain where the SDK is loaded. These cookies cannot be accessed by subdomains or the top-level domain.  
  


> ![info](/docs/images/info.svg)This parameter takes highest precedence over any other cookie domain configuration options, for example, `storage.cookie.domain`.

  
**Example** : If the SDK is loaded on `app.example.com` and `sameDomainCookiesOnly` is set to `true`, cookies are scoped only to `app.example.com` and are not accessible from `blog.example.com`, `example.com`, or `sub.app.example.com`.  
`sendAdblockPage`| Boolean| Enables the SDK to detect if the current page is ad-blocked and send an automatic page event. See [Detect Ad-blocked Pages](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>) for more information.  
  
**Default value** : `false`.  
`sendAdblockPageOptions`| Object| If `sendAdblockPage` is set to true, the SDK makes an implicit `page` call about the ad-blocked pages. You can then use this option to specify destinations to which you want to forward this `page` call. See [Detect Ad-blocked Pages](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>) for more information.  
`sessions`| SessionOpts| Captures the details specific to session tracking.  
`sourceConfigurationOverride`| Object| Lets you dynamically modify destination configurations and the destination status when initializing the RudderStack JavaScript SDK.  
  
See Configure device mode destinations dynamically for more information.  
`storage`| Object| Configures different storage-related features like, encryption, migration, etc.  
  
See Storage for more information.  
`timerScaleFactor`| Integer| Indicates how slow the event queue timers should run.  
  
See `timerScaleFactor` for more information.  
`uaChTrackLevel`| String| Configures the level of information captured in the `context` object. The SDK fetches this information using the [user-agent client hints API](<https://developer.mozilla.org/en-US/docs/Web/API/User-Agent_Client_Hints_API>).  
`useBeacon`| Boolean| Determines whether the SDK sends event payloads via the Beacon transport mechanism.  
  
**Default value** : `false`.  
`useGlobalIntegrationsConfigInEvents`| Boolean| Lets you automatically use the `integrations` object specified in the `load` API at the individual event level.  
  
**Default value** : `false`  
`lockIntegrationsVersion`  
Deprecated| Boolean| Determines if the SDK should use the same version of the integration SDKs from CDN as the core SDK. This is particularly useful for [NPM installations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#using-npm>) where a specific version of the core SDK is used.  
  
**Default value** : `true`  
`lockPluginsVersion`  
Deprecated| Boolean| Determines if the SDK should use the same version of the plugins from CDN as the core SDK. This is particularly useful for [NPM installations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#using-npm>) where a specific version of the core SDK is used.  
  
**Default value** : `true`  
  
> ![warning](/docs/images/warning.svg)
> 
> The following `load` API options are deprecated in the latest JavaScript SDK in favour of the `storage.cookie` option:
> 
>   * [`setCookieDomain`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#loading-options>)
>   * [`sameSiteCookie`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#loading-options>)
>   * [`secureCookie`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#loading-options>)
> 


The following snippet highlights some basic and commonly configured `load` options. Note that it **does not** include all the `load` options.
    
    
    {
      logLevel: 'DEBUG',
      integrations: {
        All: true,
        "Google Analytics 4": false
      },
      queueOptions: {
        maxItems: 200,
        maxAttempts: 15
      },
      useBeacon: true,
      beaconQueueOptions: {
        maxItems: 50,
        flushInterval: 60000 // 1 minute
      },
      autoTrack: {
        enabled: true,
        options: {}
        pageLifecycle: {
          enabled: true,
          options: {}
        }
      }
      consentManagement: {
        enabled: true,
        provider: 'oneTrust'
      },
      onLoaded: () => {
        console.log('RudderStack JavaScript SDK loaded successfully')
      },
      uaChTrackLevel: "full",
      sendAdblockPage: true
    }
    

The following sections contain the detailed definitions and usage of some of the above parameters:

### Integration options

You can use the `integrations` object to [filter events](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>) to selective [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destinations in the following scenarios:

  * While loading the JavaScript SDK via the `load` API.
  * Sending events to specific destinations at the event level.


> ![info](/docs/images/info.svg)
> 
> The `integrations` object in the `load` API only controls the loading of the device mode destinations. The data is **not** propagated to the individual event payloads automatically.
> 
> To use the globally-defined integration options at the event level, set the `useGlobalIntegrationsConfigInEvents` option of the `load` API to `true`.

The structure of the `integrations` object is shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: boolean, // default true
        <Destination1>: boolean, //or object
        <Destination2>: boolean // or object
        ...
      }
    });
    

The following table describes the above (optional) parameters in detail:

Parameter| Type| Description  
---|---|---  
`All`| Boolean| Global filtering status for all the destinations. The default value is `true`.  
  
If set to `false`, RudderStack filters all the destinations unless you override this setting with destination-specific parameters. For example:  
  

    
    
    {  
    All: false,   
    Amplitude: true  
    }

The above snippet causes the SDK to filter all destinations except Amplitude.  
`<Destination>`| Boolean / Object| Specific destination to filter. It overrides the `All` parameter value.  
  
If the type is object, the SDK automatically assumes this parameter as `true`. You can use this field for sending destination-specific custom configuration/data to the integration module in cloud and device modes.  
  
> ![warning](/docs/images/warning.svg)
> 
> The destination name in the `integrations` object should match the name exactly as displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). It should **not** be the name that you assigned to the destination while setting it up in RudderStack.
> 
> ![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)

The below sample snippet loads only the **Amplitude** and **Intercom** destinations:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: false,
        "Amplitude": true,
        "Intercom": true
      }
    });
    

The below snippet loads all the destinations except **Amplitude** :
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: true,
        "Amplitude": false
      }
    });
    

The below snippet highlights a case where an object is sent instead of a Boolean. In this case, RudderStack sends an `identify` event to [Mailjet](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailjet/>) to remove the user named `Alex Keener` from the list ID `13314el9Z`:
    
    
    rudderanalytics.identify('1hKOmRA4el9Z', {
          firstName: 'Alex',
          lastName: 'Keener',
          email: "alex@example.com"
        },
          externalId: [{
            type: "listId",
            id: "13314el9Z"
          }],
          integrations: {
            Mailjet: {
              Action: "remove"
            }
          }
        );
    

#### Use globally-defined integration options at event level

You can use the `useGlobalIntegrationsConfigInEvents` option to use the `integrations` object of the `load` API at the event level **if** it is not present in the event.

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

> ![info](/docs/images/info.svg)
> 
> The SDK gives precedence to the `integrations` object defined at the event level over the globally-defined `integrations` object.

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
    

In this case, the SDK uses the `integrations` option from the `load` API.

### Get source configuration

The `getSourceConfig` function returns a custom configuration that can be used in place of your [open source control plane’s](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) dashboard configuration:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      getSourceConfig: function() {
        return {
          // custom configuration
        };
      },
      // other load options
    });
    

### Queue options

The `queueOpts` object contains the options to control the behavior of the persistence queue that buffers the events before sending them to RudderStack. Its structure is defined as follows:
    
    
    {
      maxRetryDelay: 360000,
      minRetryDelay: 1000,
      backoffFactor: 2,
      backoffJitter: 0,
      maxAttempts: 10,
      maxItems: 100,
      batch: {
        enabled: true,
        maxItems: 100,
        maxSize: 512 * 1024, // 512 KB
        flushInterval: 60000 // In ms
      },
    }
    

The following table describes the above `integer` type (optional) parameters in detail:

Parameter| Description| Default value  
---|---|---  
`maxRetryDelay`| Upper limit on the maximum delay (in ms) between each retries of an event.| 360000  
`minRetryDelay`| Minimum wait time (in ms) between each retries of an event.| 1000  
`backoffFactor`| Exponential base.| 2  
`backoffJitter`| Jitter to be applied to the delay.| 0  
`maxAttempts`| Maximum number of attempts to send the event to the RudderStack backend (data plane).| 10  
`maxItems`| Maximum number of events buffered in the persistent storage for processing.| 100  
`batch`| Options for batched requests.| `BatchOpts`  
  
### Batch request options

Parameter| Description| Default value  
---|---|---  
`enabled`| Determines whether to enable batching.| `false`  
`maxItems`| Maximum number of events in a batch.| 100  
`maxSize`| Maximum batch payload size (in bytes).| 512 KB (Also the maximum configurable value)  
`flushInterval`| Minimum interval (in ms) between two batch requests.| 60000  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `queueOptions.batch` is an optional object, meaning batching is disabled by default.
>   * The SDK makes a batch request when either of the following criteria is met:
>     * `maxItems` in a batch is reached.
>     * `maxSize` of the batch is reached.
>     * Time period of `flushInterval` ms has elapsed since the last batch request.
> 


### Session options

The `SessionOpts` object contains the options related to the SDK’s automatic session tracking behavior. Its structure is defined as follows:

Parameter| Description| Default value  
---|---|---  
`autoTrack`| Determines if the SDK should automatically track the user sessions.| `true`  
`cutOff`| Provides an additional layer of session management by automatically resetting user sessions when they exceed a configured maximum duration  
  
See [Configure Session Cutoff in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/configure-session-cutoff/>) for more information on using this parameter.| -  
`timeout`| The maximum inactivity period before the session expires.| `1800000 ms` (30 minutes)  
  
See [Automatic Session Tracking in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#automatic-session-tracking>) guide for more information.

### Consent management options

You can implement consent management for the downstream destinations in JavaScript SDK depending on your [use case](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#overview>).

A sample `consentManagement` object that specifies the consent management provider while loading the SDK is shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: "oneTrust" / "ketch" / "custom",
        allowedConsentIds: ["<category_id_1>", "<category_id_2>"], // Required for Custom provider
        deniedConsentIds: ["<category_id_3>", "<category_id_4>"] // Required for Custom provider
      },
      // Other load options
    });
    

The `consentManagement` object parameters are explained below:

Parameter| Data type| Description  
---|---|---  
`enabled`| Boolean| Determines if the SDK should enable the consent management functionality.  
`provider`| String| Name of the consent management provider. RudderStack accepts these values currently: `oneTrust`, `ketch`, and `custom`.  
`allowedConsentIds`| Array| [Category IDs](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/#step-1-configure-consent-settings-for-destination>) for which the SDK allows the events to flow through to the destination.  
`deniedConsentIds`| Array| [Category IDs](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/#step-1-configure-consent-settings-for-destination>) for which the SDK blocks the events from going to the destination.  
  
> ![info](/docs/images/info.svg)
> 
> The SDK requires the `allowedConsentIds` and `deniedConsentIds` fields in the `consentManagement` object of the `load` API **only** for [Post-consent user tracking](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#post-consent-user-tracking>) in case of a [Custom consent provider](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#post-consent-user-tracking>).
> 
> The SDK automatically captures these fields in case of the [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>), [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>), and [iubenda](<https://www.rudderstack.com/docs/data-governance/consent-management/iubenda/>) integrations, so you do not need to specify them explicitly.

### Anonymous ID options

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
`source`| String| Determines the external source of anonymous ID. The only allowed value is `segment`.  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If the RudderStack `anonymousId` is already set in your browser, `anonymousIdOptions` will not take effect.
>   * You can call the **reset** API to clear the persisted anonymous ID and force the SDK to generate a new ID when the next tracking API is called (irrespective of whether `anonymousIdOptions` is enabled or disabled). However, if the `anonymousIdOptions` object is enabled and the SDK is loaded again (as a result of webpage reload, navigate to a different webpage, etc.), the `setAnonymousId` call will trigger automatically and the anonymous ID for the specific source will be set again as the RudderStack `anonymousId`.
> 


### Configure information present in context

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
    

### The `onLoaded` callback function

The `onLoaded` callback function takes the `rudderanalytics` instance as an argument and executes after the JavaScript SDK loads and before the native device-mode destination SDKs are loaded.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      onLoaded: function(rudderanalytics) {
        console.log("All set!");
      }
    });
    

Use the `onLoaded` callback for the below purposes:

  * To determine if the SDK has loaded (not ready) successfully
  * To retrieve information from the SDK like using the `GET` APIs (`getAnonymousId`, `getUserId`, etc.)
  * To ensure the SDK persists all the queued events reliably before processing them.


> ![success](/docs/images/tick.svg)
> 
> You can start instrumenting events to the SDK after the initialization snippet for CDN installation and once the SDK instance is created in case of NPM installations.
> 
> The loading snippet and SDK has mechanisms to buffer events and process them for delivering it to the RudderStack backend (data plane) and device mode destinations appropriately.

#### `onLoaded` vs. `ready` callback

Note that the `onLoaded` callback is different from the [`ready` callback](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#ready-api>) which fires **only when** the SDK has initialized itself along with the other third-party destination SDKs.

### Destination queue options

The `destinationsQueueOptions` object controls the behavior of the in-memory queue that buffers events before sending them to the device mode destinations. Its structure is defined as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      destinationsQueueOptions: {
        maxItems: 100
      }
    });
    

Parameter| Type| Description  
---|---|---  
`maxItems`| Integer| Maximum number of events the device mode destinations (in-memory) queue can store while the destinations are still loading.  
  
**Default value** : 100  
  
### Set external anonymous ID cookie name

You can use this option to specify the cookie name in cases where the user has set a cookie for the SDK to fetch the external anonymous ID and use it further as the RudderStack’s `anonymousId`.

If you provide a cookie name that does not exist, the SDK either uses the existing `anonymousId` or generates a new one.

Note that the external `anonymousId` is fetched only once while loading the SDK and any changes to the `anonymousId` cookie mid-session is not reflected in the events. To modify the `anonymousId` stored by RudderStack in such cases, use the [`setAnonymousId`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#overriding-anonymous-id>) method.

### Optimize timers behavior

The JavaScript SDK internally uses timers to continuously interact with the local storage. These timers acknowledge the local storage status and reclaim any stale event queues. They run at a set frequency optimizing their performance.

Generally, these timers do not impact your webpage. However, if you still feel that your webpage’s performance is degraded by any CPU or memory spikes, you can configure the value of `timerScaleFactor` parameter. It is an integer with the minimum and maximum values as 1 (default value) and 10 respectively. The higher the value, the slower the timers run - reducing their impact on the page, if any.

## Plugins

> ![info](/docs/images/info.svg)
> 
> Plugins are JavaScript SDK features that you can load **optionally** , based on your requirements.

Name| Description  
---|---  
`BeaconQueue`| Uses the browser’s Beacon utility to send a batch of events to the data plane instead of a single event per request.  
  
See Sending events using Beacon for more information.  
`DeviceModeDestinations`| Loads the device mode destinations supported by RudderStack.  
`DeviceModeTransformation`| Transforms events before sending them to the connected device mode destinations.  
  


> ![info](/docs/images/info.svg)The SDK loads this plugin by default if there is at least one device mode destination connected to the transformation.  
>   
> However, if you are explicitly specifying the plugins list while loading the SDK, make sure to include this plugin in the list. Otherwise, device mode transformations will not work correctly.  
  
`ExternalAnonymousId`| Lets you migrate the external anonymous user IDs to RudderStack’s `anonymousId`.  
  
See [`anonymousIdOptions`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#anonymousidoptions>) for more information.  
`GoogleLinker`| Provides `anonymousId` from Google AMP Linker URL query parameters.  
`NativeDestinationQueue`| Stores incoming events in a queue and sends them to the device mode destinations.  
`StorageEncryptionLegacy`| Existing (SDK version v1.1 or below) approach to encrypt/decrypt data before storing the data.  
`StorageEncryption`| Lightweight alternative to encrypt/decrypt data before storing the data.  
`StorageMigrator`| Assists the SDK in migrating the legacy encrypted persisted data.  
`XhrQueue`| Stores incoming events in a local storage retry queue and sends them to the data plane via XMLHttpRequest.  
`OneTrustConsentManager`| Integrates the OneTrust consent manager.  
  
See [OneTrust consent management for web](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>) for more information.  
`KetchConsentManager`| Integrates the Ketch consent manager.  
  
See [Ketch consent management for web](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>) for more information.  
`ErrorReporting`  
Deprecated \- now a part of the core SDK functionality| Reports SDK errors to RudderStack.  
`Bugsnag`  
Deprecated \- now a part of the core SDK functionality| Integrates Bugsnag as an error reporting provider.  
  
If you wish to use only a subset of the SDK features, you can explicitly specify the plugins in the `plugins` option while loading the SDK.

For example, if you **do not want** the external anonymous ID, Google Linker and error reporting features, you can provide an array of plugin names excluding those plugins. A sample snippet highlighting how to set the `plugins` load option in this scenario:
    
    
    plugins: ["BeaconQueue", 
              "DeviceModeDestinations", 
              "NativeDestinationQueue",
              "StorageEncryptionLegacy",
              "StorageEncryption",
              "StorageMigrator",
              "XhrQueue",
              "OneTrustConsentManager",
              "KetchConsentManager"
             ]
    

> ![warning](/docs/images/warning.svg)
> 
> If you set the `plugins` option and exclude certain plugins from the list (for example, `OneTrustConsentManager`), setting the associated options while loading the SDK (for example, `consentManagement.provider` to `oneTrust`) will have no effect.

If you **do not specify** the `plugins` option while loading the JavaScript SDK, then RudderStack considers **all** plugins mentioned in the above table by default.

> ![info](/docs/images/info.svg)
> 
> **Once the list of plugins is determined, the SDK automatically loads a subset of them based on your load options, browser capabilities, and source configuration**.
> 
> For example, if you set `consentManagement.provider` to `ketch`, then the SDK will not load `OneTrustConsentManager` plugin by default.

### Lazyloading plugins

For older browsers and users intentionally using the legacy Javascript SDK, RudderStack bundles the plugins with the core SDK. However, for modern browsers, the SDK lazy loads the plugins as multiple small chunks. These chunks are very small in size and loaded with the website parallelly.

The SDK’s bundling tool uses a package that supports Module Federation to bundle each feature into separate code chunks that can have interdependency among themselves. These chunks act as containers and can expose and consume code between them, creating a single, unified application. These chunks or plugins are then uploaded into CDN.

Depending on the load options, browser capabilities, and source configuration, RudderStack fetches these plugins from the remote location at runtime when the SDK loads.

## Storage

You can use the `storage` load option to configure different storage-specific features like encryption and migration.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        encryption: {
          version: "v3" / "legacy"
        },
        type: "cookieStorage", // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
        entries: {
          userId: {
            type: "cookieStorage" // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
          },
          userTraits: {
            type: "cookieStorage" // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
          },
          sessionInfo: {
            type: "cookieStorage" // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
          }
        },
        migrate: true / false,
        cookie: {
          maxage: 31536000 * 1000, // 1 year
          path: "/",
          domain: "example.com",
          samesite: "Lax",
          secure: true / false
        }
      }
    });
    

Parameter| Type| Description  
---|---|---  
`encryption`| Object| Configures the encryption type for persisted user data. It consists of a `version` parameter that accepts two values - `v3` and `legacy`.  
  
The SDK uses Base64 encryption if you set `version` to `v3` and AES encryption for `legacy`.  
  
**Default value** : `v3`  
`type`| String| Specifies the storage for the persisted data.  
  
Acceptable values are: `cookieStorage`, `localStorage`, `sessionStorage`, `memoryStorage`, and `none`.  
  
See [Configure Persistent Data Storage in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>) for more information on this parameter.  
`entries`| Object| Lets you define the storage for specific type of persisted user data.  
  
See [Configure Persistent Data Storage in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/##set-storage-for-specific-information-type>) for more information on this parameter.  
`migrate`| Boolean| Migrates persisted legacy encrypted data if set to `true`.  
  
**Default value** : `true`  
`cookie`| Object| Contains the configurable options for the cookie.  
  
See Cookie settings for more information.  
  
> ![warning](/docs/images/warning.svg)
> 
> If you set `version` to `legacy`, then you must also load the `StorageEncryptionLegacy` plugin. For `v3`, you must load the `StorageEncryption` plugin.
> 
> Similarly, if you do not set `migrate` to `false`, then you must also load the `StorageMigrator` plugin.

Note that:

  * If you access the SDK persisted data directly from the cookie or local storage, you must update the custom decryption logic.
  * All sites under the same top-level domain must use the same encryption version. For example, if `xyz.test.com` uses the latest JavaScript SDK and `abc.test.com` uses a legacy SDK version (v1.1 or below), then you should set the `storage` load option as follows:


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        encryption: {
          version: "legacy"
        }
      },
      // other load options
    });
    

  * Migrating all your subdomain sites to use SDK v3 is recommended.


### Cookie settings

The `cookie` object contains the configurable options for your cookie. All parameters in this object are **optional**.

> ![warning](/docs/images/warning.svg)
> 
> The configuration provided in these cookie options overrides any other cookie settings.

Parameter| Type| Description  
---|---|---  
`maxage`| Number| Maximum duration (in ms) that the cookie lives.  
  
**Default value** : 1 year  
`path`| String| Path of the page where the cookie is accessible.  
  
**Default value** : `/`  
`domain`| String| Sets the cookie domain unless overridden by the `sameDomainCookiesOnly` parameter.  
  
**Default value** : The SDK captures and uses the current domain as the default value.  
`samesite`| String| Sets the `SameSite` attribute of the cookie.  
  
**Default value** : `Lax`  
`secure`| Boolean| Determines if the SDK should send the cookie to the storage backend via HTTPS.  
  
**Default value** : `false`  
  
## Configure persistent data storage

While loading the JavaScript SDK, you can specify the information to store (`userId`, `anonymousId`, session information, etc.) and whether to store it in your browser’s cookies, local storage, in-memory storage, or not store it at all (fully anonymous tracking).

See [Configure Persistent Data Storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>) guide for more information.

## Load SDK for self-hosted control plane

If you are self-hosting the control plane using the [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#using-sdk-sources-set-up-in-self-hosted-control-plane>) utility, the `load` call should be made as below:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      configUrl: CONTROL_PLANE_URL,
    });
    

## Allowlist RudderStack domain

If you are using RudderStack’s CDN for the SDK content, add the following (minimum) content security policy (CSP) header configuration to load the JavaScript SDK without any errors:

> ![info](/docs/images/info.svg)
> 
> A content security policy (CSP) adds an extra layer of protection from any type of cross-site scripting, clickjacking, and data injection attacks.
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-inline' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

If you don’t want to allow unsafe inline and use the CDN package with its loading snippet, use `nonce` attribute to the script tag for the loading snippet:
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'nonce-rAnd0m' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

If you use the NPM package, no inline loading snippet is required:
    
    
    <meta http-equiv="Content-Security-Policy" content="script-src 'self' https: //cdn.rudderlabs.com/ https://cdn.rudderstack.com/;">
    

### For device mode destinations

While using the JavaScript SDK with destinations that support [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you might need to allowlist the domain from where the destination SDK loads in your content security policy (CSP).

See the specific [destination’s documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) to obtain the domain to be allowlisted. For example, [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#connection-mode>).

## Track user sessions

By default, the JavaScript SDK automatically tracks the user sessions. This means that RudderStack automatically determines the start and end of a user session depending on the inactivity time configured in the SDK (default time is 30 minutes).
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sessions: {
        autoTrack: true,
        cutOff: {
          enabled: true, // Optional; set to true to enable the feature
          duration: 12 * 60 * 60 * 1000 // Optional; 12 hours in milliseconds (default)
        },
        timeout: 10 * 60 * 1000,  // 10 min in milliseconds; Default is 30 minutes
      },
      ...<otherLoadOptions>
    });
    

Note that:

  * To disable automatic session tracking, set the load option `autoTrack` to `false`.
  * You can enforce stricter session boundaries using the `cutOff` object to reset user sessions when they exceed a configured maximum duration. This feature works alongside the standard session timeout (`timeout`) mechanism.


See [Automatic Session Tracking in JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/>) for more information on this feature.

## Autotrack page view metrics

You can use the `autoTrack` option of the `load` API to get visibility into page view metrics. When autotracking is enabled:

  * `context.autoTrack.page.pageViewId` is automatically added to **all** events sent from the page, allowing you to tie events to a single page visit. This works **regardless** of whether the Beacon transport mechanism is enabled.
  * If Beacon is enabled, the SDK automatically fires a `Page Unloaded` event when a page unloads, including the time spent on the page.


> ![info](/docs/images/info.svg)
> 
> To reliably deliver the `Page Unloaded` event, enable the Beacon transport mechanism by setting `useBeacon` to `true` in the SDK load API options.

See [Autotrack Page View Metrics using JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/autotrack-page-metrics/>) for more information on this feature.

## Send events using Beacon

The JavaScript SDK lets you send the event payloads using the **XHR** (XMLHttpRequest) API (default) or [Beacon](<https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon>) browser utility.

There are two advantages of using the [Beacon](<https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon>) utility to send your event payload:

  * The events delivery request is executed even when the page unloads, leading to no loss of data.
  * The Beacon requests are optimized so that the browser waits until the CPU load is lower or until the network is free before making the actual requests, leading to better website performance.


> ![info](/docs/images/info.svg)
> 
> The Beacon queue maintained by the browsers limits the total size of the elements present in the queue at any point and **peaks at 64 KB**.

See Event delivery and retry mechanism to help you decide whether to use Beacon to send your events.

### Workflow

The **Beacon** browser utility asynchronously sends a small amount of data over HTTP to the RudderStack server. To send the SDK events using this utility, set the `useBeacon` field in the `load()` call options to `true`.

The SDK internally uses a queue (`BeaconQueueOpts`) to buffer the events and send it through the Beacon utility in batches. The queue options can be configured as shown below:
    
    
    {
      maxItems: 10, 
      flushQueueInterval: 600000 // In ms
    }
    

The following table describes the above `integer` type parameters in detail:

Parameter| Description| Default Value  
---|---|---  
`maxItems`| The SDK flushes the events queue when the event count meets this limit.| 10  
`flushQueueInterval`| The SDK flushes the events queue periodically at this interval (ms).| 600000  
  
> ![info](/docs/images/info.svg)
> 
> The JavaScript SDK flushes the Beacon events queue if the total size of the payload exceeds 64 KB before even reaching the `maxItems` or `flushQueueInterval` criteria.

### Event delivery and retry mechanism

This section highlights some important points which will help you choose whether to use Beacon for sending your event payloads:

  * The requests sent from the SDK using the Beacon utility only push the events to the browser’s Beacon queue. Further, it depends on the browser’s engine to send these events from the queue. Hence, RudderStack **cannot guarantee** if any events get discarded due to any 5xx or other network-related errors (request timed out, end resource unavailable, etc.).


> ![warning](/docs/images/warning.svg)
> 
> If event delivery and retry is an important requirement for your website, using the XHR API of the JavaScript SDK is highly recommended. RudderStack retries event delivery based on the status codes and other errors.

  * The Beacon queue maintained by the browsers limits the total size of the elements present in the queue at any point and **peaks at 64 KB**. Therefore, you cannot send high-frequency hits from the main thread in one go, as the Beacon queue cannot take up cycles to dequeue itself.


## Configure device mode destinations dynamically

> ![info](/docs/images/info.svg)
> 
> This feature is available in the JavaScript SDK v3.20.1 and later.

You can use the `sourceConfigurationOverride` parameter to dynamically modify device mode destination configurations when initializing the RudderStack JavaScript SDK without requiring any dashboard configuration changes.

See [How to Dynamically Configure Device Mode Destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/>) for more information on using this parameter.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/migration-guide/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/>)