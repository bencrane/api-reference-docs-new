# How to Create Custom Web Device Mode Integrations

Create custom web device mode integrations in RudderStack.

* * *

  * __4 minute read

  * 


This guide lists the steps to set up a custom web device mode destination in RudderStack and the necessary SDK configuration required to send events correctly.

## Prerequisites

Before you start creating custom device mode integrations, make sure you have:

  * A [JavaScript source](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) set up in your RudderStack workspace and integrated with your website
  * Access to your third-party tool’s API, documentation, and SDK


## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Custom Device Mode** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## 1\. Dashboard setup

Create a custom device mode destination in your RudderStack dashboard by following these steps:

  1. Navigate to the JavaScript source set up in your RudderStack dashboard.
  2. In the **Overview** tab, click **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Custom Device Mode** from the list of destinations and click **Continue**.
  4. Configure the following settings:

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
Connection mode| Device mode is selected by default, as this is a web device mode-only integration.  
  
  5. Configure the other **optional** settings as per your requirements:

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
Client-side Events Filtering| This setting lets you specify which `track` events should be blocked or allowed to flow through to the custom integration.  
  
See [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) for more information.  
  
  6. Save your destination and note the **Destination ID** — you will need this for the JavaScript SDK integration.

[![Destination ID for Custom Device Mode destination](/docs/images/event-stream-destinations/custom-integrations/destination-id.webp)](</docs/images/event-stream-destinations/custom-integrations/destination-id.webp>)

## 2\. Add your custom integration to the JavaScript SDK

Use the [`addCustomIntegration` API](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/>) to register your custom integration with the RudderStack JavaScript SDK.

> ![info](/docs/images/info.svg)
> 
> The `addCustomIntegration` API connects your custom code to the **Custom Device Mode** destination set up in the RudderStack dashboard.

### Basic syntax
    
    
    rudderanalytics.addCustomIntegration('<destination_id>', {
      // Your integration implementation
    });
    

See the detailed [`addCustomIntegration`](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/>) API reference for more information on the following:

  * [Integration structure](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/#integration-structure>)
  * [Function parameters](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/#function-parameters>)
  * [Event data structure](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/#event-data-structure>)


## 3\. Implement the integration functions

This section covers the functions you need to implement to correctly create your custom web device mode integration.

> ![info](/docs/images/info.svg)
> 
> Your implementation determines the supported event types and how the integration handles them.

### Initialize the third-party SDK

Use the [`init` function](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/#integration-structure>) to load and configure your third-party SDK:
    
    
    init: (destinationConfig, analytics, logger) => {
      logger.debug('Loading third-party SDK');
      
      // Dynamically load the SDK script
      const script = document.createElement('script');
      script.src = 'https://cdn.your-sdk.com/sdk.js';
      script.onload = () => {
        // Initialize the SDK once loaded
        window.YourSDK.init({
          apiKey: destinationConfig.apiKey,
          // Add other configuration options
        });
      };
      document.head.appendChild(script);
    }
    

### Check integration readiness

Note that [`isReady`](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/#integration-structure>) is the only required function — it tells RudderStack when your integration is ready to receive events:
    
    
    isReady: (analytics, logger) => {
      // Check if your third-party SDK is loaded and initialized
      return window.YourSDK && window.YourSDK.initialized === true;
    }
    

> ![warning](/docs/images/warning.svg)
> 
> If `isReady` doesn’t return `true` within 11 seconds, RudderStack will time out and skip your integration.

### Handle events

Make sure to implement only the event types your integration supports:
    
    
    track: (analytics, logger, rsEvent) => {
      try {
        // Extract event data
        const eventName = rsEvent.message.event;
        const properties = rsEvent.message.properties;
        
        // Send to your third-party tool
        window.YourSDK.track(eventName, properties);
        
        logger.debug('Track event sent successfully');
      } catch (error) {
        logger.error('Failed to send track event:', error);
      }
    }
    

## 4\. Test the integration

After implementing your custom integration, verify it works correctly by following these steps:

  1. Open your browser’s developer console.
  2. Look for any debug messages (after configuring the required log levels in the JavaScript SDK) from your integration.
  3. Check that events are being sent to your tool.
  4. Test different event types (`track`, `page`, `identify`) to ensure they’re handled properly.


## Troubleshooting

Issue| Solution  
---|---  
Integration not initializing| Make sure to call `addCustomIntegration()` before `rudderanalytics.load()`.  
Events not being sent| Check that `isReady` returns `true`.  
Third-party SDK not loading| Verify the script URL and check for console errors.  
Configuration not available| Ensure your destination is properly configured in the RudderStack dashboard.  
  
## See more

  * [How to Implement Custom Web Device Mode Integrations](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/implement-custom-integration/>)
  * [JavaScript SDK Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
  * [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>)
  * [Consent Management](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>)