# Consent Management in JavaScript SDK

> Version: Latest (v3)v1.1

# Consent Management in JavaScript SDK

Understand the consent management functionality in the JavaScript SDK.

* * *

  * __7 minute read

  * 


This guide explains the consent management functionality and the various consent tracking approaches supported by the JavaScript SDK.

## Overview

The JavaScript SDK supports RudderStack’s [consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/>) functionality and lets you manage data sent to downstream destinations based on user consent. This feature is crucial for respecting user privacy preferences and complying with data protection regulations.

With this functionality, you can:

  * Seamlessly integrate with popular consent management providers like [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/>), [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>), and [iubenda](<https://www.rudderstack.com/docs/data-governance/consent-management/iubenda/>). You can also set up a [custom consent management provider](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/>).
  * Configure consent settings for multiple providers for your web source.
  * Unlock advanced use cases like pre-consent user tracking where you can track user activity and control the SDK’s behavior before and after the user provides their consent.


## Consent management approaches

There are two primary approaches to implementing consent management with the RudderStack JavaScript SDK:

### Post-consent user tracking

Post-consent user tracking is the most common implementation where you load the JavaScript SDK only after the user has provided consent. This approach is straightforward but has limitations:

  * It ensures that no tracking occurs before consent is given
  * You cannot control SDK behavior before consent is provided
  * It may result in loss of some initial user activity data


See the [OneTrust post-consent user tracking setup](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/#post-consent-user-tracking>) for a sample implementation.

### Pre-consent user tracking

Pre-consent user tracking allows you to track some user activity and control SDK behavior both before and after the user provides consent. This approach offers more flexibility because of the following reasons:

  * It minimizes data loss related to attribution, acquisition, and the overall user journey
  * You can choose to track users as fully anonymous, track only their sessions, or track only with `anonymousId` identifier
  * It allows for a more nuanced approach to data collection based on consent status
  * There is no particular restriction on the loading order of the SDKs


See the [OneTrust pre-consent user tracking setup](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/#pre-consent-user-tracking>) for a sample implementation.

> ![info](/docs/images/info.svg)
> 
> The presence of consent management object in the event’s context (`context.consentManagement`) helps you differentiate between the pre- and post-consent events.
> 
> RudderStack does not add any other extra property to differentiate these events.

## Key components of pre-consent user tracking

This section explains the key components of pre-consent user tracking in the JavaScript SDK.

### The `preConsent` object

You can use the `preConsent` object while loading the JavaScript SDK to define the SDK’s cookie storage and events delivery behavior in pre-consent mode.

  1. Pass the consent management platform’s information in the `consentManagement` object as a `load` API option.
  2. Add the `preConsent` object, as shown:


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: "oneTrust" / "ketch" / "custom"
      },
      preConsent: {
        enabled: true // false by default"
        storage: { // Optional
          strategy: "none" / "session" / "anonymousId", // Default is "none"
        },
        events: { // Optional
          delivery: "immediate" / "buffer", // Default is "immediate"
        },
      },
      ...
      // Other load options
    });
    

> ![info](/docs/images/info.svg)
> 
> If you set `preConsent.enabled` to `true`, the JavaScript SDK does **not** load the device mode integrations.

#### Cookie storage strategy

The SDK stores information in the pre-consent mode based on the following cookie storage strategies:

Value| Description  
---|---  
`none`| Fully anonymous tracking where RudderStack does not store any cookies.  
  
For this value, note that:  
  


  * Each event contains a new `anonymousId`.
  * If [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#automatic-session-tracking>) is enabled, each event will contain a new `sessionId`.
  * The SDK does not persist any data from the previous API calls, that is, `userId`, `groupId`, `traits`, etc. are not included in the future events.

  
`session`| Fully anonymous tracking where RudderStack stores only the session tracking cookie ([manual](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/manual-session-tracking/>) or [automatic](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#automatic-session-tracking>)), if it is active.  
  
For this value, note that:  
  


  * Each event contains a new `anonymousId`.
  * The SDK does not persist any data from the previous API calls, that is, `userId`, `groupId`, `traits`, etc. are not included in the future events.

  
`anonymousId`| RudderStack persists only the anonymous ID (`anonymousId`).  
  
For this value, note that:  
  


  * If [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#automatic-session-tracking>) is enabled, each event will contain a new `sessionId`.
  * The SDK does not persist any data from the previous API calls, that is, `userId`, `groupId`, `traits`, etc. are not included in the future events.

  
  
#### Events delivery strategy

> ![info](/docs/images/info.svg)
> 
> As the SDK does not load any device mode destinations in pre-consent mode, you can control the events delivery strategy for the cloud mode destinations only.

The SDK delivers events in the pre-consent mode based on the following values:

Value| Description  
---|---  
`immediate`| RudderStack sends the events to the RudderStack backend (data plane) immediately as they occur.  
`buffer`| This option is applicable only if the cookie storage strategy is set to `none` or `session`. The SDK buffers the events in the local storage. You can use the `consent` API to decide what to do with these buffered events.  
  
The SDK decides the delivery for preload events (events instrumented to the SDK before it is loaded), [ad-blocked page view](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>) events, and [Query string API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#query-string-api>) events, based on the above options (`immediate`/`buffer`) set in the pre-consent mode.

### The `consent` API

You can invoke the JavaScript SDK’s [`consent` API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#consent-api>) once the user consent is available. The SDK then comes out of the pre-consent mode and resumes normal functioning.

A sample implementation for a [custom provider](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/>) is shown below:
    
    
    <script type = "text/javascript">
      // consent provider callback
      function ConsentManagerWrapper() { /// Pseudo name
        if (window.isConsented()) { // Pseudo name
    
          // Pass the allowed and denied category IDs for custom setup
          rudderanalytics.consent({
            options: {
              trackConsent: true / false, // Optional; default is false
              consentManagement: {
                allowedConsentIds: ['<category_id_1>','<category_id_2>',.....], // Required for Custom provider
                deniedConsentIds: ['<category_id_3>','<category_id_4>',.....]
              }, // Required for Custom provider
              storage: {
                type: "cookieStorage", // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
                entries: {
                  userId: {
                    type: "localStorage" // Other supported values are "cookieStorage","sessionStorage", "memoryStorage", and "none"
                  },
                  userTraits: {
                    type: "cookieStorage" // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
                  },
                  sessionInfo: {
                    type: "cookieStorage" // Other supported values are "localStorage","sessionStorage", "memoryStorage", and "none"
                  }
                }
              }, // Optional
              integrations: IntegrationOpts, // Optional
              discardPreConsentEvents: true / false, // Optional; default is false
              sendPageEvent: true / false // Optional, default is false
            }
          });
        }
      } 
    </script>
    

The `consent` API options are listed below:

Parameter| Type| Description  
---|---|---  
`trackConsent`| Boolean| Determines if the SDK should send a `track` event with the name `Consent Management Interaction`.  
  
**Default value** : `false`  
`consentManagement`| Object| Lets you pass the user consent data in case of a [custom consent management provider](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/>). The SDK **requires** the `allowedConsentIds` and `deniedConsentIds` fields in case of a **Custom** consent provider.  
`storage`| Object| Lets you configure the different storage-specific options like:  
  


  * [`storage.type`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>): Specify where the persisted data should be stored.
  * [`storage.entries`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/##set-storage-for-specific-information-type>): Lets you define storage for specific type of persisted user data.

  
`integrations`| Object| Instructs the SDK to filter the integrations before the consent filtering takes effect.  
`discardPreConsentEvents`| Boolean| Determines if the SDK should discard all the pre-consent events buffered previously.  
  
**Default value** : `false`  
`sendPageEvent`| Boolean| Determines if the SDK should send a `page` event.  
  
**Default value** : `false`  
  
The SDK does the following once you invoke the `consent` API:

  * Loads the device mode integrations based on consent.
  * Fetches the consent information from the consent manager.
  * Stores persistent user information like `userId`, `anonymousId`, `traits`, etc. according to the specified [`storage`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>) option.
  * Discards or replays the buffered pre-consent events to the destinations based on the `discardPreconsentEvents` parameter.


The SDK also sends any events received after the user gives consent to the destinations immediately.

## Set different pre-consent and post-consent storage options

You can configure different [storage options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) for pre-consent and post-consent user tracking that let you:

  * Ensure data is stored appropriately based on the consent status and reduce unnecessary data collection.
  * Maintain seamless user experience while respecting users’ privacy preferences.


Follow these steps to set different storage options for pre-consent and post-consent user tracking:

  1. Configure the [storage options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) while loading the JavaScript SDK.
  2. Set `preConsent.enabled` to `true`. You can also define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery strategy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) here.


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
        storage: {
            encryption: {
                version: "v3" / "legacy"
            },
            type: "cookieStorage", // Other available options are "localStorage", "sessionStorage", "memoryStorage", and "none".
            
            // Other storage options
        }
      consentManagement: {
        enabled: true,
        provider: "oneTrust" / "ketch" / "custom" // Specify your consent management provider
      },
      preConsent: {
        enabled: true,
        storage: { // Optional; defines SDK's cookie storage strategy
          strategy: "session" // Optional; other accepted values are "none", "session"
        },
        events: { // Optional; defines SDK's events delivery behavior
          delivery: "buffer" // Optional; other accepted value is "immediate"
        },
      }
      // Other load options
    });
    

  3. Invoke the `consent` API **after** the user provides consent. You can also define the SDK’s post-consent [storage options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) here.


    
    
    rudderanalytics.consent({
      trackConsent: true,
      discardPreConsentEvents: true, // Optional; default value is false
      storage: {
        type: "localStorage" // Other available options are "cookieStorage", "sessionStorage", "memoryStorage", and "none".
      }
    });
    

## Integration with consent management platforms

RudderStack’s JavaScript SDK integrates with various consent management platforms:

  * [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/#set-up-website>)
  * [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>)
  * [iubenda](<https://www.rudderstack.com/docs/data-governance/consent-management/iubenda/>)
  * [Custom providers](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#setup>)


These integrations enable:

  * Flexibility to use the consent management tool that best fits your needs
  * Seamless coordination between consent decisions and data collection
  * Compliance with privacy regulations across different jurisdictions

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/server-side-cookies/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/service-worker/>)