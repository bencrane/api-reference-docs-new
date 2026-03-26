# Consent Management

Integrate RudderStack with popular consent management platforms or use a custom setup.

* * *

  * __2 minute read

  * 


Consent management is the process of capturing users’ consent preferences, syncing preferences across every tool in the stack, and blocking user data from being sent to destinations where the user has not provided consent.

RudderStack makes it simple for data teams and developers to capture consent data centrally and maintain compliance with GDPR, CCPA, and other privacy regulations.

## How it works

RudderStack gives you the ability to configure consent logic for each destination in your stack.

For example, you may want to send data to a marketing tool only if a user has opted in to advertising and marketing tracking. In this case, you would configure your marketing destination to require `allowedconsentId`s for both analytics and marketing. If event payloads do not include these consent IDs, RudderStack will drop them, ensuring you don’t send non-compliant user data.

To apply consent logic, consent ID values need to be present in the `consentManagement` object in the `context` of event payloads. Several of RudderStack’s SDKs and integrations can automatically populate the `consentManagement` object, but you can also [manually add](<https://www.rudderstack.com/docs/data-governance/consent-management/passing-consent/>) consent data as part of your instrumentation.

> ![info](/docs/images/info.svg)
> 
> **See the support matrix to plan your implementation**
> 
>   * The implementation of RudderStack’s consent management functionality varies across RudderStack SDKs. See the [Consent Management Support Matrix](<https://www.rudderstack.com/docs/data-governance/consent-management/support-matrix/>) for details.
>   * RudderStack recommends starting with the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>), which has the most comprehensive feature support.
> 


## Key features

  * **Configure pre-consent user tracking (JavaScript SDK only)** : Decide how to track users and manage cookies before they provide consent.
  * **Add user consent to event payloads** : Use intuitive features in our SDKs to add consent IDs to event payloads for each unique user.
  * **Block or allow data delivery to destinations** : Apply logic to each destination using consent IDs to ensure only compliant user data is delivered to every system.


## Integrations

RudderStack supports full integration with multiple popular consent management vendors as well as custom consent management systems.

#### Native integrations

  * [OneTrust](<https://www.rudderstack.com/docs/data-governance/consent-management/onetrust/>)
  * [Ketch](<https://www.rudderstack.com/docs/data-governance/consent-management/ketch/>)
  * [iubenda](<https://www.rudderstack.com/docs/data-governance/consent-management/iubenda/>)


#### Support for custom systems

Use our [Custom Consent Management feature](<https://www.rudderstack.com/docs/data-governance/consent-management/custom-consent-manager/>) to easily integrate your custom-built consent solution across your entire stack.

## Feature walkthrough