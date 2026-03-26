# OneTrust Consent Management for Web

Integrate the RudderStack JavaScript SDK with the OneTrust SDK.

* * *

  * __5 minute read

  * 


RudderStack’s [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) seamlessly integrates with the OneTrust SDK. It lets you map the OneTrust cookie consent categories to specific RudderStack destinations.

## How the integration works

  1. Whenever a user starts browsing a website, OneTrust pops up a modal to take consent from the user. This modal contains a list of cookie categories representing the consent categories that the user needs to decline or accept.
  2. The JavaScript SDK fetches the OneTrust consent data and the consent settings specified in the RudderStack dashboard.
  3. The SDK loads the [device mode destinations](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) based on the above data.
  4. The user must consent to **all** the consent categories corresponding to the category IDs specified in the dashboard settings for sending events to the destination (both in cloud and device mode).
  5. The SDK attaches the consent management data in the event payloads sent to the RudderStack backend (data plane) for performing the same consent-based filtering for [cloud mode destinations](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).


## Prerequisites

  * You must have a [OneTrust account](<https://my.onetrust.com/s/login/SelfRegister?language=en_US&startURL=%2Fs%2F%3Ft%3D1587743884774>) with a subscription to their [Cookie Consent](<https://www.onetrust.com/products/cookie-consent/>) product.


## Setup

The following sections highlight the steps to set up the JavaScript SDK integration with OneTrust.

### Step 1: Configure OneTrust

  1. Navigate to **Websites** > **Add Websites**.
  2. Enter your top-level website URL to scan and click **Start Scan**.
  3. Go to the **Categorizations** tab and define the new categories or modify the existing ones, as required.
  4. Go to the **Scripts** tab, select the domain to be published and click **Publish** to publish the script.
  5. Obtain the consent category IDs from the OneTrust dashboard by going to **Preference & Consent Management** > **Cookie Compliance** > **Categorizations** > **Categories**.


### Step 2: Specify OneTrust Cookie Category IDs

Specify the consent category IDs obtained above for **each** destination connected to your JavaScript source. You can specify multiple consent category IDs by pressing the **Enter** key after each ID.

> ![info](/docs/images/info.svg)
> 
> The OneTrust consent category IDs are case-sensitive.

[![OneTrust category ID in consent settings](/docs/images/data-governance/consent-management/onetrust-category-ids.webp)](</docs/images/data-governance/consent-management/onetrust-category-ids.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/multiple-consent-ui.webp)](</docs/images/data-governance/consent-management/multiple-consent-ui.webp>)

### Step 3: Set up your website

You can set up your website depending on the following use cases:

Use case| Description  
---|---  
Post-consent user tracking| Call the `load` API of the JavaScript SDK **only after** OneTrust confirms that the user has interacted with their consent banner. This is the most common implementation.  
Pre-consent user tracking| This approach is helpful in cases where you need to track some user activity and control the SDK and cookie behavior **before** and **after** the user provides their consent.  
  
#### Post-consent user tracking

Note that:

  * In this approach, you must load the JavaScript SDK **after** the OneTrust script.
  * If the user updates their consent preferences, you must refresh the web page for the changes to take effect in the SDK (for both cloud and device mode destinations).


  1. Load the OneTrust script that you published in Step 1:


    
    
    <script 
      src="https://cdn.cookielaw.org/scripttemplates/<sample>.js"
      type="text/javascript"
      charset="UTF-8"
      data-domain-script="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" >
    </script>
    

  2. Configure the RudderStack SDK `load` API options as follows:


    
    
    <script type="text/javascript">
      // Required OneTrust callback
      function OptanonWrapper() {
        if (window.OneTrust.IsAlertBoxClosed()) {
          // Insert the rest of the JS SDK loading snippet here
          rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
            consentManagement: {
              enabled: true,
              provider: "oneTrust"
            },
            // Other options
          }),
        }
      }
    </script>
    

> ![info](/docs/images/info.svg)
> 
> `OptanonWrapper` is a callback function supported by the OneTrust SDK. It is invoked when the user consent is available.

In the above instrumentation, the SDK is notified that consent management should be enabled, and the user has configured the OneTrust provider on their site. The SDK then fetches the user consents from OneTrust and filters the destinations and events accordingly.

#### Pre-consent user tracking

Note that:

  * In this mode, you can choose to track users as fully anonymous, track only their sessions, or track only with `anonymousId` as the user identifier. This minimizes any data loss related to attribution, acquisition, and the overall user journey.
  * Unlike post-consent user tracking, there is no restriction on the loading order of the JavaScript and OneTrust SDKs for this use case.
  * If the user updates their consent preferences, you must invoke the `consent` API again for the changes to take effect for the cloud mode destinations. For the device mode destinations tied to the consent preferences, reload the web page for the changes to take effect.


##### **Step 1: Configure the`preConsent` object**

Use the `preConsent` object while loading the JavaScript SDK to define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery behavior](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) in pre-consent mode.

The website instrumentation in this case looks as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: "oneTrust"
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
    

followed by the OneTrust script:
    
    
    <script 
      src="https://cdn.cookielaw.org/scripttemplates/<sample>.js"
      type="text/javascript"
      charset="UTF-8"
      data-domain-script="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" >
    </script>
    

In the above example, the JavaScript SDK is configured to load in the pre-consent mode. Note that:

  * The storage strategy is to persist only the session ID.
  * Any events instrumented to the SDK are buffered till the user provides consent.
  * The SDK does not load any device mode destination connected to the source.


##### **Step 2: Invoke`consent` API once user provides consent**

Once the user consent is available, invoke the JavaScript SDK’s [`consent`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#consent-api>) API. The SDK then comes out of the pre-consent mode and resumes normal functioning.
    
    
    rudderanalytics.consent({
      trackConsent: true,
      discardPreConsentEvents: true, // Optional; default value is false
      storage: {
        type: "localStorage"
      }
    });
    

In the above snippet, SDK does the following:

  * Loads device mode integrations based on the consent data.
  * Stores information like the user ID, anonymous user ID, user traits, etc. in the local storage henceforth.
  * Discards the buffered pre-consent events, if any.
  * Sends a `track` event named `Consent Management Interaction`, indicating the consent interaction has happened.