# Ketch Consent Management

Integrate RudderStack with the Ketch consent management platform.

* * *

  * __6 minute read

  * 


[Ketch](<https://www.ketch.com/platform/consent-management>) provides a robust consent management system with customizable no-code consent policy templates that adhere to all major privacy laws. It also provides comprehensive cookie categorization and identity resolution across devices, channels, and platforms.

## How the integration works

> ![info](/docs/images/info.svg)
> 
> RudderStack supports native Ketch integration only with the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).
> 
> For the other SDKs, you can implement Ketch consent-based event filtering **cloud mode** destinations, by adding the `consentManagement` object within the context of the event payload. See [Add the Consent Object to Event Payloads](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) for more information.

This section describes how the native Ketch consent management integration works with the JavaScript SDK:

  1. Websites with the [Ketch Smart Tag](<https://developers.ketch.com/docs/ketch-smart-tag-overview>) present a consent experience for users to decide the consent purposes based on the applicable regulatory framework.
  2. User consent is stored in the Ketch backend and cached in the user’s browser.
  3. The JavaScript SDK fetches the Ketch consent data and the consent settings specified in the RudderStack dashboard.
  4. The SDK loads the [device mode destinations](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) based on the above data.
  5. The user must consent to at least one of the consent purposes corresponding to the category IDs specified in the dashboard settings for sending events to the destination (both in cloud and device mode).
  6. The SDK attaches the consent management data in the event payloads sent to the RudderStack backend (data plane) for performing the same consent-based filtering for [cloud mode destinations](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).


## Prerequisites

You must have an active [Ketch account](<https://www.ketch.com/>).

## Setup

The following sections highlight the JavaScript SDK integration with Ketch Smart Tag:

### Step 1: Configure Ketch Smart Tag

  1. Log in to your [Ketch account](<https://www.ketch.com/>) and go to the dashboard.
  2. By default, the Ketch smart tag for the website will be deployed and ready to use. You can access it from the **Consent & Rights** > **Properties** section of the Ketch dashboard.

[![Configure Ketch smart tag](/docs/images/data-governance/consent-management/configure-ketch-tag-1.webp)](</docs/images/data-governance/consent-management/configure-ketch-tag-1.webp>)

  3. Access the Ketch purposes from the **Privacy Program** section. A few of those purposes will already be listed by default — edit those to fit your business requirement, or create a new one.

[![Configure Privacy Program](/docs/images/data-governance/consent-management/configure-ketch-tag-2.webp)](</docs/images/data-governance/consent-management/configure-ketch-tag-2.webp>)

### Step 2: Specify Ketch consent purposes

Specify the Ketch consent purposes defined in Step 1 for each destination connected to your source in the RudderStack dashboard. You can specify multiple consent purpose IDs by pressing the **Enter** key after each ID.

[![Ketch purpose IDs in dashboard settings](/docs/images/data-governance/consent-management/ketch-purpose-ids.webp)](</docs/images/data-governance/consent-management/ketch-purpose-ids.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/ketch-multiple-consents.webp)](</docs/images/data-governance/consent-management/ketch-multiple-consents.webp>)

### Step 3: Set up website

You can set up your website depending on the following use cases:

Use case| Description  
---|---  
Post-consent user tracking| Call the `load` API of the JavaScript SDK **only after** Ketch notifies that the user has interacted with their consent banner.  
Pre-consent user tracking| This approach is helpful in cases where you need to track some user activity and control the SDK and cookie behavior **before** and **after** the user provides their consent.  
  
#### Post-consent user tracking

Note that:

  * In this approach, you must load the JavaScript SDK **after** the Ketch script.
  * If the user updates their consent preferences, you must refresh the web page for the changes to take effect in the SDK (for both cloud and device mode destinations).


Place the scripts in your web page’s `<head>` section in the following sequence:

  1. Place the Ketch script. You can get the script by going to your Ketch dashboard and navigating to **Consent & Rights** > **Properties**. Select your Ketch Smart Tag and click **Export Code** to get the script. For more information, see [Ketch documentation](<https://docs.ketch.com/ketch/docs/web-implementation>).


The following snippet highlights a sample script:
    
    
    <script>
      !function () { window.semaphore = window.semaphore || [], window.ketch = function () { window.semaphore.push(arguments) }; var e = new URLSearchParams(document.location.search), n = document.createElement("script"); n.type = "text/javascript", n.src = "https://global.ketchcdn.com/web/v3/config/<organisation>/<ketch-tag>/boot.js", n.defer = n.async = !0, document.getElementsByTagName("head")[0].appendChild(n) }();
    </script>
    

  2. Call the SDK `load` API, as shown:


    
    
    function getCookie(key) {
      return window.document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=')
        return parts[0] === key ? decodeURIComponent(parts[1]) : r
      }, '')
    }
    
    if (getCookie('_ketch_consent_v1_')) {
      rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
          consentManagement: {
            enabled: true,
            provider: "ketch"
          }
        });
        // Other options
      }
    else {
      // Waiting for consent
      ketch('once', 'userConsentUpdated', () => {
        rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
          consentManagement: {
            enabled: true,
            provider: "ketch"
          },
          // Other options
        });
      });
    }
    

In the above instrumentation:

  * The SDK is notified that consent management should be enabled and the user has configured the Ketch tag on their site.
  * If consent is already present, then the SDK loads immediately. Otherwise, it waits for user consent.
  * The Ketch JavaScript function is used to trigger the `load` API once the user gives consent.


#### Pre-consent user tracking

Note that:

  * In this mode, you can choose to track users as fully anonymous, track only their sessions, or track only with `anonymousId` as the user identifier. This minimizes any data loss related to attribution, acquisition, and the overall user journey.
  * Unlike post-consent user tracking, there is no restriction on the loading order of the JavaScript and Ketch SDKs for this use case.
  * If the user updates their consent preferences, you must invoke the `consent` API again for the changes to take effect for the cloud mode destinations. For the device mode destinations tied to the consent preferences, reload the web page for the changes to take effect.


##### **Step 1: Configure the`preConsent` object**

Use the `preConsent` object while loading the JavaScript SDK to define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery behavior](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) in pre-consent mode.

The website instrumentation in this case looks as follows:
    
    
    function getCookie(key) {
      return window.document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=')
        return parts[0] === key ? decodeURIComponent(parts[1]) : r
      }, '')
    }
    
    var loadOptions = {
      consentManagement: {
        enabled: true,
        provider: "ketch"
      }
    };
    if (!getCookie('_ketch_consent_v1_')) {
      // If consent is not present, add pre-consent option
      loadOptions.preConsent = {
        enabled: true,
        storage: { // Optional; Defines SDK's cookie storage strategy
          strategy: "session" // Optional; Other accepted values are "none", "session"
        },
        events: { // Optional; Defines SDK's events delivery behavior
          delivery: "buffer" // Optional; Other accepted value is "immediate"
        },
      }
    }
    
    // When consent is not present, add the pre-consent option
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, loadOptions);
    

followed by the Ketch script:
    
    
    <script>
      !function () { window.semaphore = window.semaphore || [], window.ketch = function () { window.semaphore.push(arguments) }; var e = new URLSearchParams(document.location.search), n = document.createElement("script"); n.type = "text/javascript", n.src = "https://global.ketchcdn.com/web/v3/config/<organisation>/<ketch-tag>/boot.js", n.defer = n.async = !0, document.getElementsByTagName("head")[0].appendChild(n) }();
    </script>
    

In the above example, the JavaScript SDK is configured to load in the pre-consent mode. Note that:

  * The storage strategy is to persist only the session ID.
  * Any events instrumented to the SDK are buffered till the user provides consent.
  * The SDK does not load any device mode destination connected to the source.
  * If consent is already present, then the SDK loads without the `preConsent` option.


##### **Step 2: Invoke`consent` API once user provides consent**

Once the user consent is available, invoke the SDK’s [`consent`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#consent-api>) API. The SDK then comes out of the pre-consent mode and resumes normal functioning.
    
    
    // Waiting for consent
    ketch('on', 'userConsentUpdated', () => {
      rudderanalytics.consent({
        trackConsent: true,
        discardPreConsentEvents: true, // Optional; Default value is false
        storage: {
          type: "localStorage"
        }
      });
    });
    

In the above snippet, SDK does the following:

  * Loads device mode integrations based on the consent data.
  * Stores information like the user ID, anonymous user ID, user traits, etc. in the local storage henceforth.
  * Discards the buffered pre-consent events, if any.
  * Sends a `track` event named `Consent Management Interaction`, indicating the consent interaction has happened.
  * The SDK is subscribed to the `userConsentUpdated` (Ketch JavaScript function). This triggers the `consent` API when there is a change in the user’s consent. See the [Ketch documentation](<https://docs.ketch.com/ketch/docs/ketch-smart-tag-plugins>) for more information.