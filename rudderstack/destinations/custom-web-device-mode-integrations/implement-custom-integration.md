# How to Implement Custom Web Device Mode Integrations

Learn how to implement custom web device mode integrations using the JavaScript SDK.

* * *

  * __4 minute read

  * 


This guide explains how to use the `addCustomIntegration` API to implement custom web device mode integrations using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

See [How to Create Custom Web Device Mode Integrations](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/>) for more information on setting up custom integrations in RudderStack.

## Basic syntax

The following snippet shows the basic syntax for registering a custom integration with the JavaScript SDK:
    
    
    rudderanalytics.addCustomIntegration('<destination_id>', {
      // Your integration implementation
    });
    

Replace `<destination_id>` with the destination ID of the **Custom device mode** destination [set up in the RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#1-dashboard-setup>).

## Integration structure

Your custom integration is an object that can include the following functions:
    
    
    rudderanalytics.addCustomIntegration('<destination_id>', {
      // OPTIONAL: Initialize your third-party SDK
      init: (destinationConfig, analytics, logger) => {
        logger.debug('Custom integration initializing');
        // Load and initialize your third-party SDK here
      },
    
      // REQUIRED: Check if integration is ready
      isReady: (analytics, logger) => {
        logger.debug('Checking integration readiness');
        // Return true when your SDK is ready to accept events
        return window.YourSDK && window.YourSDK.initialized;
      },
    
      // OPTIONAL: Handle track events
      track: (analytics, logger, rsEvent) => {
        logger.debug('Processing track event');
        // Transform and send track events to your third-party tool
        window.YourSDK.track(
          rsEvent.message.event, 
          rsEvent.message.properties
        );
      },
    
      // OPTIONAL: Handle page events
      page: (analytics, logger, rsEvent) => {
        logger.debug('Processing page event');
        // Transform and send page events to your third-party tool
        window.YourSDK.page(
          rsEvent.message.name, 
          rsEvent.message.properties
        );
      },
    
      // OPTIONAL: Handle identify events
      identify: (analytics, logger, rsEvent) => {
        logger.debug('Processing identify event');
        // Transform and send identify events to your third-party tool
        window.YourSDK.identify(
          rsEvent.message.userId, 
          rsEvent.message.context.traits
        );
      },
    
      // OPTIONAL: Handle group events
      group: (analytics, logger, rsEvent) => {
        logger.debug('Processing group event');
        // Transform and send group events to your third-party tool
        window.YourSDK.group(
          rsEvent.message.groupId, 
          rsEvent.message.traits
        );
      },
    
      // OPTIONAL: Handle alias events
      alias: (analytics, logger, rsEvent) => {
        logger.debug('Processing alias event');
        // Transform and send alias events to your third-party tool
        window.YourSDK.alias(
          rsEvent.message.userId, 
          rsEvent.message.previousId
        );
      }
    });
    

> ![info](/docs/images/info.svg)
> 
> See the [`addCustomIntegration` API Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/register-custom-integrations/>) guide for more information on the API details, supported function parameters, and event data structure.

## Load custom integration selectively

You can use the `integrations` object in the `load` API options to control when your custom integration loads:
    
    
    rudderanalytics.load('WRITE_KEY', 'DATA_PLANE_URL', {
      integrations: {
        'Custom Device Mode': true, // Loads the custom web device mode integration
        'Google Analytics': false    // Skips this standard integration
      }
    });
    

## Add multiple custom integrations

You can add multiple custom integrations by calling `addCustomIntegration` multiple times with different destination IDs:
    
    
    // Integration 1
    rudderanalytics.addCustomIntegration('<destination-id-1>', {
      // Implementation for first tool
    });
    
    // Integration 2
    rudderanalytics.addCustomIntegration('<destination-id-2>', {
      // Implementation for second tool
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Do not specify duplicate destination IDs as it will lead to a [validation error](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#validations>).

## Important considerations

This section covers some important considerations to keep in mind when building custom web device mode integrations.

### Validations

The JavaScript SDK logs errors to the console in the following cases:

  * If the `addCustomIntegration` API is invoked after the SDK has already reached the loaded or ready states.

  * If there are issues with the destination ID:

    * Incorrect or duplicate destination ID
    * Destination ID that does not correspond to a connected **Custom Device Mode** destination set up in the RudderStack dashboard
  * If there are issues with the integration instance.


### Error handling

RudderStack automatically catches and logs errors from your integration (arising due to network failures, invalid data, etc.). It then logs the error in the browser console for debugging and continues processing the other integrations, ensuring a faulty integration does not block the entire tracking system.

### Performance

Your custom integration runs in the browser alongside other integrations. Keep these performance tips in mind:

  * Make your `isReady` function returns quickly before the [11 second timeout](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#check-integration-readiness>), beyond which the integration is deemed to be a failure and dropped.


> ![info](/docs/images/info.svg)
> 
> Without this timeout, a custom integration that takes too long to initialize (reports that it is ready) can delay the entire system — this means all tracking events will be queued until the integration is ready.

  * Handle errors gracefully to avoid blocking other integrations.
  * Initialize your third-party SDK efficiently.
  * Use the logger for debugging instead of `console.log`.


## End-to-end example

An end-to-end example showing how to integrate with a hypothetical analytics tool is shown below:
    
    
    // Add custom integration before loading the SDK
    rudderanalytics.addCustomIntegration('your-destination-id', {
      init: (destinationConfig, analytics, logger) => {
        logger.debug('Initializing Custom Analytics SDK');
        
        // Load the third-party SDK
        const script = document.createElement('script');
        script.src = 'https://cdn.customanalytics.com/v1/analytics.js';
        script.onload = () => {
          window.CustomAnalytics.init({
            apiKey: destinationConfig.apiKey,
            trackPageViews: false // We'll handle this manually
          });
        };
        document.head.appendChild(script);
      },
    
      isReady: (analytics, logger) => {
        return window.CustomAnalytics && window.CustomAnalytics.ready;
      },
    
      track: (analytics, logger, rsEvent) => {
        const { event, properties } = rsEvent.message;
        window.CustomAnalytics.track(event, properties);
      },
    
      page: (analytics, logger, rsEvent) => {
        const { name, properties } = rsEvent.message;
        window.CustomAnalytics.page(name, properties);
      },
    
      identify: (analytics, logger, rsEvent) => {
        const { userId } = rsEvent.message;
        const traits = rsEvent.message.context.traits;
        window.CustomAnalytics.identify(userId, traits);
      }
    });
    
    // Load RudderStack SDK
    rudderanalytics.load('YOUR_WRITE_KEY', 'YOUR_DATA_PLANE_URL');