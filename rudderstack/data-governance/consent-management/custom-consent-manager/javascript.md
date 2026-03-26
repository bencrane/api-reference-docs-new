# Custom Consent Management for Web

* * *

  *  __4 minute read

  * 


The JavaScript SDK seamlessly integrates with your custom consent management provider and lets you map the user’s consent categories to specific RudderStack destinations.

RudderStack fetches the [consent settings](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/#configure-consent-settings>) specified in the RudderStack dashboard and processes the destinations and events accordingly.

## Setup

The following sections highlight the steps to set up the JavaScript SDK integration with a custom consent management provider.

### Step 1: Configure consent categories

Configure the consent categories in your consent manager’s dashboard.

### Step 2: Specify consent category IDs

Specify the consent category IDs defined above for **each** destination connected to your JavaScript source. You can specify multiple consent purpose IDs by pressing the **Enter** key after each ID.

> ![info](/docs/images/info.svg)
> 
> The consent category IDs are case-sensitive.

[![Custom category ID in consent settings](/docs/images/data-governance/consent-management/custom-category-ids.webp)](</docs/images/data-governance/consent-management/custom-category-ids.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/custom-multiple-consent.webp)](</docs/images/data-governance/consent-management/custom-multiple-consent.webp>)

### Step 3: Set up your website

You can set up your website depending on the following use cases:

Use case| Description  
---|---  
Post-consent user tracking| Call the `load` API of the JavaScript SDK **only after** the user has provided consent.  
Pre-consent user tracking| This approach is helpful in cases where you need to track some user activity and control the SDK and cookie behavior **before** and **after** the user provides their consent.  
  
#### Post-consent user tracking

Note that:

  * In this approach, you must load the JavaScript SDK **after** the user has provided consent.
  * If the user updates their consent preferences, you must refresh the web page for the changes to take effect in the SDK (for both cloud and device mode destinations).


Use the `consentManagement` object in the `load` API, as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: "custom",
    
        // Provide the consent IDs obtained from your consent provider.
        allowedConsentIds: ['<category_id_1>', '<category_id_2>', .....], // Required
        deniedConsentIds: ['<category_id_3>', '<category_id_4>', .....] // Required
      },
      // Other options
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * RudderStack **requires** the `allowedConsentIds` and `deniedConsentIds` fields to successfully filter events based on user’s consent.
>   * The consent IDs specified in the `allowedConsentIds` and `deniedConsentIds` must be the **union** of all the consent category IDs specified in the consent settings for the destination. Otherwise, the consent setup will not work as expected.
> 


#### Pre-consent user tracking

Note that:

  * With this approach, you can choose to track users as fully anonymous, track only their sessions, or track only with `anonymousId` as the user identifier. This minimizes any data loss related to attribution, acquisition, and the overall user journey.
  * Unlike post-consent user tracking, there is no restriction on the loading order of the JavaScript SDK for this use case.
  * If the user updates their consent preferences, you must invoke the `consent` API again for the changes to take effect for the cloud mode destinations. For the device mode destinations tied to the consent preferences, reload the web page for the changes to take effect.


##### **Step 1: Configure the`preConsent` object**

Use the `preConsent` object while loading the JavaScript SDK to define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery behavior](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) in pre-consent mode.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: { // Optional
        enabled: true,
        provider: "custom"
      },
      preConsent: { // Optional
        enabled: true, // Optional; false by default
        storage: { // Optional
          strategy: "session", // Optional; other accepted values are "none", "session"
        },
        events: { // Optional
          delivery: "buffer", // Optional; other accepted value is "immediate"
        },
      },
      ...
      // Other load options
    });
    

In the above example, the JavaScript SDK is configured to load in the pre-consent mode. Note that:

  * The storage strategy is to persist only the session ID.
  * Any events instrumented to the SDK are buffered till the user provides consent.
  * The SDK does not load any device mode destination connected to the source.


##### **Step 2: Invoke`consent` API once user provides consent**

Once the user consent is available, invoke the SDK’s [`consent`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#consent-api>) API with the consent data obtained from your provider. The SDK then comes out of the pre-consent mode and resumes normal functioning.
    
    
    rudderanalytics.consent({
      consentManagement: {
        // Provide the consent IDs obtained from your consent provider.
        allowedConsentIds: ["<category_id_1>", "<category_id_2>"], // Required for custom provider
        deniedConsentIds: ["<category_id_3>", "<category_id_4>"], // Required for custom provider
      },
      trackConsent: true,
      discardPreConsentEvents: true, // Optional; default value is false
      storage: {
        type: "localStorage"
      }
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * RudderStack **requires** the `allowedConsentIds` and `deniedConsentIds` fields to successfully filter events based on user’s consent.
>   * The consent IDs specified in the `allowedConsentIds` and `deniedConsentIds` must be the **union** of all the consent category IDs specified in the consent settings for the destination. Otherwise, the consent setup will not work as expected.
> 


In the above snippet, SDK does the following:

  * Loads device mode integrations based on the consent data.
  * Stores information like the user ID, anonymous user ID, user traits, etc. in the local storage henceforth.
  * Discards the buffered pre-consent events, if any.
  * Sends a `track` event named `Consent Management Interaction`, indicating the consent interaction has happened.