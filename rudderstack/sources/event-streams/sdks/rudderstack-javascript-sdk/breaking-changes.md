# Breaking Changes in JavaScript SDK v3

> Version: Latest (v3)v1.1

# Breaking Changes in JavaScript SDK v3

Understand the breaking changes introduced in RudderStack JavaScript SDK v3.

* * *

  * __4 minute read

  * 


This guide lists the breaking changes introduced in JavaScript SDK v3.

## Storage and encryption

This section covers the new changes introduced in the JavaScript SDK’s storage and encryption features.

### Storage prefix changes

The local storage entries prefix has been updated from `rudder` to `rudder_<write-key>`, where `<write-key>` is your JavaScript source [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).

### Encryption updates

  * Storage data encryption now uses Base64 by default.
  * Existing persisted data is automatically migrated to the latest version unless specified otherwise.
  * New load API options for encryption configuration are introduced:


    
    
    storage: {
      migrate: true,
      encryption: {
        version: 'v3',
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> **Important storage encryption considerations**
> 
> If you have implemented the JavaScript SDK in multiple sites sharing the same top-level domain and cookies and have different major SDK versions across these sites, then RudderStack recommends the following actions:
> 
>   * Consider upgrading **all** sites to the [latest v3 SDK version](<https://www.npmjs.com/package/@rudderstack/analytics-js?activeTab=versions>) at once.
>   * If that is not possible, then upgrade the older sites to the [latest version](<https://www.npmjs.com/package/rudder-sdk-js>) of SDK v1.1.
>   * If any of the above actions are not possible, then set the [`storage.encryption.version`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) parameter to `legacy` for all the sites.
> 

> 
> See the [JavaScript SDK Migration Guide](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/migration-guide/#pre-migration-checklist>) for more information.

## Installation related changes

  * The [SDK loading snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/>) is updated in v3.
  * The SDK file name is changed from `rudder-analytics.min.js` to `rsa.min.js`.
  * NPM package is changed from [`rudder-sdk-js`](<https://www.npmjs.com/package/rudder-sdk-js>) to [`@rudderstack/analytics-js`](<https://www.npmjs.com/package/@rudderstack/analytics-js>) to [`@rudderstack/analytics-js`](<https://www.npmjs.com/package/@rudderstack/analytics-js>).
  * All `GET` type methods from the loading snippet (`getAnonymousId`, `getGroupTraits`, etc.) are removed. These methods were not functional before the SDK loaded, making them unnecessary. However, these APIs are available in the SDK instance once it is loaded.


## Default `page` call removed

The default `page` call is removed from the loading snippet. You must now explicitly make a `page` call, if required.

## Source configuration changes

The default source configuration host has changed from `rudderlabs.com` to `rudderstack.com`. If you’re using a proxy for the source configuration host, update it to forward `https://api.rudderstack.com` instead of `https://api.rudderlabs.com`.

## Consent management updates

The consent management configuration structure is updated in v3:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      cookieConsentManager: {
        oneTrust: {
          enabled: true
        }
      }
    });
    
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: 'oneTrust'
      }
    });
    

## Client-side events filtering changes

For [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>):

  * Empty and non-string event names are not allowlisted anymore.
  * Event name comparison is now case-sensitive.


## Changes in `integrations` options

The destination names in the [`integrations`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#integrationopts>) object must exactly match the names displayed in the [RudderStack dashboard](<https://app.rudderstack.com/directory>). Custom names assigned during destination setup are no longer supported.

> ![warning](/docs/images/warning.svg)
> 
> The SDK will ignore any destination names that don’t match exactly as shown in the dashboard.

[![](/docs/images/dashboard-guides/amplitude-destination-name-webapp.webp)](</docs/images/dashboard-guides/amplitude-destination-name-webapp.webp>)

The following examples highlight the correct and incorrect declaration of the destination names within the `integrations` object:

The below sample snippet loads the SDK with the **Amplitude** , **Intercom** , and **ActiveCampaign** destinations only:
    
    
    // Correct usage
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: false,
        "Amplitude": true,
        "Intercom": true,
        "ActiveCampaign": true
      }
    });
    

Declaring the destination names in the `integrations` object in the following manner will **not** work anymore:
    
    
    // Incorrect usage
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        All: false,
        "AM": true,
        "INTERCOM": true,
        "ACTIVE_CAMPAIGN": true
      }
    });
    

The following snippet highlights a sample `track` event sent to only the **Amplitude** destination:
    
    
    // Correct usage
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345
      }, {
        integrations: {
          All: false,
          "Amplitude": true
        }
      }
    );
    

Declaring the destination name in the `integrations` object in the following manner will **not** work anymore:
    
    
    // Incorrect usage - will not work
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345
      }, {
        integrations: {
          All: false,
          "AM": true
        }
      }
    );
    

## Ad blocker detection changes

  * The ad blocker detection logic is updated.
  * Dependency on the Google AdSense script is removed.


## Service worker

Service worker is now available as a separate package. It is published at [@rudderstack/analytics-js-service-worker](<https://www.npmjs.com/package/@rudderstack/analytics-js-service-worker>).

## Removed features

[Sync pixel callback](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#callbacks-to-common-methods>) feature has been removed.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/new-features/>)