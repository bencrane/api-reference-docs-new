# Custom Consent Management Beta

Integrate a custom consent management provider with RudderStack.

* * *

  * __2 minute read

  * 


This guide walks you through the steps to integrate a custom consent management provider (other than OneTrust, Ketch, and iubenda) with RudderStack.

## Prerequisites

Configure the consent information in your consent manager’s platform and note their unique IDs. Note that these consent category IDs are case-sensitive.

## Configure consent settings

While setting up a destination in the RudderStack dashboard, use the **Consent settings** section to configure the consent management provider settings for **each source** that you connect to a destination.

[![](/docs/images/data-governance/consent-mgmt.gif)](</docs/images/data-governance/consent-mgmt.gif>)

  1. Choose **Custom** provider from the dropdown.
  2. Enter enter the consent category IDs relevant for the destination in the **Enter consent category IDs** field. You can specify multiple consent purpose IDs by pressing the **Enter** key after each ID.


Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/custom-multiple-consent.webp)](</docs/images/data-governance/consent-management/custom-multiple-consent.webp>)

### Specify consent logic

For **Custom** consent management provider, you must also select the consent logic to be applied on the category IDs while resolving them against user consent data:

  * **AND** : Allows the events to go through to the destination **only if** the end user consents to all the categories corresponding to the category IDs specified in the dashboard.
  * **OR** : Allows the events to go to the destination if the end user consents to **at least one** of the categories corresponding to the category IDs specified in the dashboard.


## Filter events based on consent

### JavaScript SDK

You can set up your website depending on the following use cases:

Use case| Description  
---|---  
[Post-consent user tracking](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#post-consent-user-tracking>)| Call the `load` API of the JavaScript SDK **only after** the user has provided consent.  
[Pre-consent user tracking](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#pre-consent-user-tracking>)| This approach is helpful in cases where you need to track some user activity and control the SDK and cookie behavior **before** and **after** the user provides their consent.  
  
See [Custom Consent Management for Web](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/javascript/#pre-consent-user-tracking>) for the implementation details.

### Other SDKs

For the other SDKs, RudderStack supports consent-based event filtering for a custom provider only in **cloud mode**. See the [Consent Management Support Matrix](<https://www.rudderstack.com/docs/data-governance/consent-management/support-matrix/>) for more information.

To filter events to your cloud mode destinations based on the user’s consent, you need to add the `consentManagement` object within the context of the event payload. See [Add the Consent Object to Event Payloads](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) for more information.