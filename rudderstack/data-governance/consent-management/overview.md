# Consent Management Overview

Learn about RudderStack’s consent management feature.

* * *

  * __4 minute read

  * 


RudderStack’s robust consent management solution offers the following features:

  * Dedicated [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/>), [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>), and [iubenda](<https://www.rudderstack.com/docs/data-governance/consent-management/iubenda/>) consent management integrations.
  * Full support for [custom consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/>) integration.
  * Implement and run multiple consent integrations, that is, run OneTrust and a custom consent solution in the same environment.
  * Configurable blocking or delivery of events to each destination based on consent IDs and custom logic.
  * Configurable pre-consent user tracking for category IDs and cookies (JavaScript SDK only).


## Workflow

The following steps give a high-level overview of how to implement RudderStack’s consent management feature.

### Step 1: Configure consent settings for destination

You can configure each destination with custom logic to block or allow events based on the consent provider and the category IDs.

  1. Go to the destination’s **Configuration settings** > **Consent settings** to configure the consent settings for each source.
  2. Choose your consent management provider from the dropdown. You can also add multiple providers based on your requirements.
  3. In the RudderStack dashboard, enter the consent category IDs relevant for the destination in the **Enter consent category IDs** field. You can specify multiple consent category IDs by pressing the **Enter** key after each ID.

[![](/docs/images/data-governance/consent-management/onetrust-category-ids.webp)](</docs/images/data-governance/consent-management/onetrust-category-ids.webp>)

The settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/multiple-consent-ui.webp)](</docs/images/data-governance/consent-management/multiple-consent-ui.webp>)

Note that:

  * The consent category IDs are case-sensitive.
  * For **Custom** provider, you must also specify the consent logic to be applied on the category IDs while resolving them against user consent data. See [Custom Consent Management](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/#specify-consent-logic>) for more information.


#### Add multiple consent managers

RudderStack supports adding consent settings for multiple providers. However, note that only one of them will be used for filtering events to a destination, based on the provider specified in the client SDK’s load instrumentation or in the `context.consentManagement` object in the event payload.

You can add multiple consent management providers for **each source** while configuring the destination-specific consent settings:

  1. Specify the consent provider settings.
  2. Click **Add group condition**.
  3. Specify the consent settings for the other provider.

[![](/docs/images/data-governance/consent-management/multiple-consent-providers.webp)](</docs/images/data-governance/consent-management/multiple-consent-providers.webp>)

Note that the settings for specifying multiple consent managers vary slightly for some destinations. Click **Add more** after specifying the consent settings for each provider.

[![](/docs/images/data-governance/consent-management/multiple-consent-managers.webp)](</docs/images/data-governance/consent-management/multiple-consent-managers.webp>)

### Step 2: Instrument website to capture consent data

After specifying the consent settings in the RudderStack dashboard, you need to instrument your website to capture the consent IDs and add them to your event payloads.

> ![info](/docs/images/info.svg)
> 
> See the [Consent Management Support Matrix](<https://www.rudderstack.com/docs/data-governance/consent-management/support-matrix/>) for help in planning your implementation.

There are two ways to set up your instrumentation. If you are tracking consent across client and server-side SDKs, you will need to use both:

  1. **Automatically capture consent data through integrations** : The JavaScript SDK, iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. , and Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. support native integrations that automatically capture consent data from your consent provider, then append it to event payloads.
  2. **Add consent data directly to event payloads** : If you need to manage consent data coming from server-side SDKs and other sources, you need to add the `consentManagement` object to the context of the event payload. See [Add the Consent Object to Event Payloads](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) for more information.


## Pre-consent user tracking

RudderStack’s [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>) lets you configure user tracking [before](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#pre-consent-user-tracking>) the user provides consent.

### Sample implementation workflow

RudderStack’s pre-consent user tracking feature lets you configure a `preConsent` object that defines the JavaScript SDK’s cookie storage and event delivery behavior in pre-consent mode.

The following steps give a high-level implementation overview of the pre-consent user tracking feature:

  1. Configure the [storage options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) while loading the JavaScript SDK.
  2. In the loading snippet, set `preConsent.enabled` to `true`. You can also define the SDK’s [cookie storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#cookie-storage-strategy>) and [events delivery strategy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/#events-delivery-strategy>) **before** the user provides consent.


    
    
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
    

  3. Invoke the `consent` API **once the user provides consent**. You can also define the SDK’s post-consent [storage options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) here and determine if the SDK should discard the buffered pre-consent events, if any.


    
    
    rudderanalytics.consent({
      trackConsent: true,
      discardPreConsentEvents: true, // Optional; default value is false
      storage: {
        type: "localStorage" // Other available options are "cookieStorage", "sessionStorage", "memoryStorage", and "none".
      }
    });
    

See the following guides for more information on using this feature with the specific consent management platform:

  * [OneTrust (Web)](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/javascript/#pre-consent-user-tracking>)
  * [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/#pre-consent-user-tracking>)
  * [Custom provider](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#pre-consent-user-tracking>)