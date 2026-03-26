# Custom Web Device Mode Integrations

Leverage custom web device mode integrations for third-party tools and services that RudderStack does not support out of the box.

* * *

  * __2 minute read

  * 


This guide will help you build custom web device mode integrations that let you connect RudderStack to any tool or platform, even when there is no pre-built integration available.

## Overview

Custom web device mode integrations run client-side in your users’ browsers ([device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)), giving you direct control over how events are transformed and sent to your chosen tools.

This approach is helpful when you need to:

  * **Connect to niche or proprietary tools** that aren’t part of RudderStack’s standard integration catalog.
  * **Implement custom business logic** for event transformation that goes beyond what configuration settings allow.
  * **Maintain real-time, client-side connections** to tools that require immediate data processing.
  * **Bridge legacy systems** that need specific data formats or authentication methods.


## How custom integrations work

A custom web device mode integration creates a bridge between RudderStack’s event tracking and your tool’s SDK or API. RudderStack handles the event collection, consent management, and filtering, while your custom code handles the specific requirements of your chosen tool.

The integration runs alongside RudderStack’s other device mode integrations, automatically receiving filtered and transformed events based on your destination configuration. This means your custom integration benefits from all of RudderStack’s built-in features while giving you complete control over the final data delivery.

## Supported features

All custom device mode integrations support the same features as standard RudderStack device mode integrations:

  * [**Device Mode Transformations**](<https://www.rudderstack.com/docs/transformations/usage/#device-mode>): If you have connected a device mode transformation to your custom web device mode destination, RudderStack automatically applies the transformation before sending events to the integration.
  * [**Consent management**](<https://www.rudderstack.com/docs/data-governance/consent-management/>): Your custom integration respects the [consent management settings](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#1-dashboard-setup>) configured in your destination. Events are forwarded **only when** the consent requirements are met.
  * [**Event filtering**](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>): You can configure [client-side event filtering](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#1-dashboard-setup>) in your destination settings to control which events reach your custom integration.


## Next steps

  * [Set up the custom device mode destination in RudderStack](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#1-dashboard-setup>)
  * [Register the custom integration with the JavaScript SDK](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#2-add-your-custom-integration-to-the-javascript-sdk>)
  * [Implement the custom integration functions](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#3-implement-the-custom-integration-functions>)