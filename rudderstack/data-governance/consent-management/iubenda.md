# iubenda Consent Management

Integrate RudderStack with the iubenda consent management platform.

* * *

  * __5 minute read

  * 


[iubenda](<https://www.iubenda.com/en/>) offers a comprehensive set of compliance solutions that help you deal with user privacy and make your website/app compliant with the regulatory laws across multiple countries and legislations.

RudderStack’s [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) seamlessly integrates with iubenda’s [Privacy Controls and Cookie Solution](<https://www.iubenda.com/en/cookie-solution?utm_source=rudderstack&utm_medium=web>).

## How the integration works

> ![info](/docs/images/info.svg)
> 
> RudderStack supports native iubenda integration only with the JavaScript SDK.
> 
> For the other SDKs, you can implement iubenda consent-based event filtering for **cloud mode** destinations, by adding the `consentManagement` object within the context of the event payload. See [Add the Consent Object to Event Payloads](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) for more information.

This section describes how the native iubenda consent management integration works with the JavaScript SDK:

  * You can map the iubenda cookies’ categorization to RudderStack’s consent management data.
  * RudderStack uses this consent information to enable/disable user tracking and sends the data to the relevant downstream destinations accordingly.


## Prerequisites

Obtain the iubenda embedding script by following these steps:

  1. Click the **Start generating** button on the top right of the [iubenda website](<https://www.iubenda.com/en/>) and follow the onboarding wizard.
  2. Follow the guided setup or go directly to **Solutions and embedding**.
  3. In the **Privacy Controls and Cookie Solution** tile, click **Generate now**.
  4. Follow the configuration steps.


Once completed, you will be redirected to the embedding section - copy the embedding snippet and use it to set up your website.

See the [iubenda documentation](<https://www.iubenda.com/en/help/3831-customize-cookie-banner?utm_source=rudderstack&utm_medium=web>) for more information on configuring the [Privacy Controls and Cookie Solution](<https://www.iubenda.com/en/cookie-solution?utm_source=rudderstack&utm_medium=web>) from scratch.

## Setup

The following sections highlight the steps to set up the JavaScript SDK integration with iubenda’s Privacy Controls and Cookie Solution.

### Step 1: Specify iubenda cookie categories

Specify the iubenda consent category IDs for each destination connected to your source in the RudderStack dashboard. You can specify multiple consent purpose IDs by pressing the **Enter** key after each ID.

> ![info](/docs/images/info.svg)
> 
> See the [full list](<https://www.iubenda.com/en/help/1229-manual-tagging-blocking-cookies?utm_source=rudderstack&utm_medium=web#per-category-consent>) of the supported iubenda consent categories.

[![iubenda consent settings](/docs/images/data-governance/consent-management/iubenda-category-ids.webp)](</docs/images/data-governance/consent-management/iubenda-category-ids.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/iubenda-multiple-consent.webp)](</docs/images/data-governance/consent-management/iubenda-multiple-consent.webp>)

### Step 2: Set up website

You can set up your website depending on the following use cases:

Use case| Description  
---|---  
Post-consent user tracking| Call the `load` API of the JavaScript SDK **only after** iubenda notifies that the user has interacted with their consent banner.  
Pre-consent user tracking| This approach is helpful in cases where you need to track some user activity and control the SDK and cookie behavior **before** and **after** the user provides their consent.  
  
#### Post-consent user tracking

Note that:

  * In this approach, you must load the JavaScript SDK **after** the iubenda script.
  * If the user updates their consent preferences, you must refresh the web page for the changes to take effect in the SDK (for both cloud and device mode destinations).


Place the scripts obtained in the Prerequisites section in your web page’s `<head>` section in the following sequence:

  1. Place the iubenda script as a first child of the `<head>` tag, as shown:


    
    
    <script type="text/javascript">
      var _iub = _iub || [];
      _iub.csConfiguration = {
      "siteId":XXXXXX,
      "cookiePolicyId":XXXXXX,
      "lang":"en"
      };
    </script>
    <script type="text/javascript" src="//cdn.iubenda.com/cs/iubenda_cs.js" charset="UTF-8" async></script>
    

  2. Load the JavaScript SDK using iubenda’s `onPreferenceExpressedOrNotNeeded` callback **after** the user provides their consent:


    
    
    {
    window._iub = window._iub || [];
    
    _iub.csConfiguration = {
         cookiePolicyId:xxxxxx,
         siteId: xxxxxx,
         lang: 'en'
         },
         callback: {
             onPreferenceExpressedOrNotNeeded: function () {
                 const loadOptions = {
                    consentManagement: {
                       enabled: true,
                       provider: 'iubenda',
                    },
                 };
                 rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, loadOptions);
             },
         }
    };
    

In the above instrumentation, the SDK is notified that consent management should be enabled, and the user has configured the iubenda script on their site. The SDK then fetches the user consents from iubenda and filters the destinations and events accordingly.

> ![info](/docs/images/info.svg)
> 
> You can also customize the SDK’s loading behavior by leveraging the other iubenda [callback methods](<https://www.iubenda.com/en/help/1205-how-to-configure-your-cookie-solution-advanced-guide#callbacks>).

#### Pre-consent user tracking

Note that:

  * In this mode, you can choose to track users as fully anonymous, track only their sessions, or track only with `anonymousId` as the user identifier. This minimizes any data loss related to attribution, acquisition, and the overall user journey.
  * If the user updates their consent preferences, you must invoke the `consent` API again for the changes to take effect for the cloud mode destinations. For the device mode destinations tied to the consent preferences, reload the web page for the changes to take effect.


##### **Step 1: Configure the`preConsent` object**

Use the `preConsent` object while loading the JavaScript SDK to define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery behavior](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) in pre-consent mode.

The website instrumentation in this case looks as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      consentManagement: {
        enabled: true,
        provider: "iubenda"
      },
      preConsent: {
        enabled: true,
        storage: { // Optional; defines SDK's cookie storage
          strategy: "session" // Optional; other accepted values are "none", "session"
        },
        events: { // Optional; defines SDK's events delivery behavior
          delivery: "buffer" // Optional; other accepted value is "immediate"
        },
      }
      // Other load options
    });
    

In the above example, the JavaScript SDK is configured to load in the pre-consent mode. Note that:

  * The storage strategy is to persist only the session ID.
  * Any events instrumented to the SDK are buffered till the user provides consent.
  * The SDK does not load any device mode destination connected to the source.


##### **Step 2: Invoke`consent` API once user provides consent**

Once the user consent is available, invoke the SDK’s [`consent`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#consent-api>) API. The SDK then comes out of the pre-consent mode and resumes normal functioning.

A sample instrumentation that loads the iubenda script and uses the `consent` API is shown:
    
    
    <script>
      window._iub = window._iub || [];
    
      _iub.csConfiguration = {
        lang: 'en',
        cookiePolicyId: xxxxxx, // Use the ID provided in the iubenda embedding code
        siteId: xxxxxx, // Use the ID provided in the iubenda embedding code
        banner: {
          position: 'float-center'
        },
        callback: {
          onPreferenceExpressedOrNotNeeded: function () {
            rudderanalytics.consent({
                trackConsent: true,
                discardPreConsentEvents: true, // Optional; default value is false
                storage: {
                  type: "localStorage"
                }
            });
          },
        }
      };
    </script>
    

In the above snippet, SDK does the following:

  * Loads device mode integrations based on the consent data.
  * Stores information like the user ID, anonymous user ID, user traits, etc. in the local storage henceforth.
  * Discards the buffered pre-consent events, if any.
  * Sends a `track` event named `Consent Management Interaction`, indicating the consent interaction has happened.


Note that the iubenda provides the below methods:

  * `getIubendaUserConsentedPurposes`: Returns the preferences IDs with consent granted by the user.
  * `getIubendaUserDeniedPurposes`: Returns the preferences IDs with consent denied by the user.