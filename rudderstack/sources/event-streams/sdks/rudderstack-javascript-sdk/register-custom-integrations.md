# addCustomIntegration API Reference

> Version: Latest (v3)v1.1

# addCustomIntegration API Reference

Complete reference for the addCustomIntegration API used for registering custom web device mode integrations with the JavaScript SDK.

* * *

  * __4 minute read

  * 


This guide provides a complete reference for the `addCustomIntegration` API used to register [Custom Web Device Mode Integrations](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/>) with the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).

## Prerequisites

  * [Custom web device mode destination](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/>) set up in the RudderStack dashboard


## Basic syntax

The following snippet shows the basic syntax for registering a custom integration:
    
    
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
    

## API details

The below table lists the APIs present in the above integration structure:

API| Description| Notes  
---|---|---  
`init`| The third-party SDK load/initialization code — you can use it to load third-party SDK script tags or initialize them.| Implement this API when you want to initialize or load the custom integration along with standard integrations.  
`isReady`  
Required| Returns `true` if the integration is ready to accept events for processing. The SDK will continuously invoke this API to retrieve the status until it is `true` but will give up after a timeout of 11 seconds.| No events are forwarded to the custom integration if the SDK cannot determine if the integration is ready.  
  
Typically, third-party SDKs have some mechanism to indicate when they are ready — so, this should be implemented accordingly.  
`track`| Processes `track` events.| -  
`page`| Processes `page` events.| -  
`identify`| Processes `identify` events.| -  
`group`| Processes `group` events.| -  
`alias`| Processes `alias` events.| -  
  
## Function parameters

Each integration function receives these parameters:

Parameter| Description| Available in  
---|---|---  
`destinationConfig`| Configuration object from your **Custom Device Mode** destination  
  


> ![info](/docs/images/info.svg)Currently, this object contains the consent management and client-side filtering settings for the **Custom Device Mode** destination [set up in the RudderStack dashboard](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/setup/#1-dashboard-setup>).

| `init` only  
`analytics`| RudderStack SDK instance for accessing user data and methods  
  
See [`analytics` instance](<>) for more information.| All functions  
`logger`| Logging system for debugging (`log`, `info`, `debug`, `warn`, `error`)| All functions  
`rsEvent`| Complete event data in RudderStack’s standard format  
  
See the following sections for more information:  
  


  * Event data structure
  * [JavaScript SDK GitHub Repository](<https://github.com/rudderlabs/rudder-sdk-js/blob/381b913609da5b23dde5e84747927a65e1f5d5de/packages/analytics-js-common/src/types/Event.ts#L65>)

| Event handlers only  
  
### `analytics` instance

The `analytics` object supports the following APIs:

  * `track`
  * `page`
  * `identify`
  * `group`
  * `alias`
  * `getAnonymousId`
  * `getUserId`
  * `getUserTraits`
  * `getGroupId`
  * `getGroupTraits`
  * `getSessionId`


See [this example](<https://github.com/rudderlabs/rudder-sdk-js/blob/381b913609da5b23dde5e84747927a65e1f5d5de/packages/analytics-js/public/index.html#L199>) for more information on how to use the `analytics` instance:

> ![warning](/docs/images/warning.svg)
> 
> RudderStack recommends not using the `GET` APIs like `getUserId`, `getUserTraits`, etc., in the event handling APIs as the event payload itself contains the data — and it is the most appropriate to use.

### `logger` parameter

The logger also has `setMinLogLevel` API which you can invoke in any of the APIs. The log level value is the same as the value configured in the [`load` API options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>).

Note that:

  * The default log level is set in the `load` API options but you can override it for the custom integration using the `logger` parameter.
  * The log level set in one API is persistent across all other API invocations. RudderStack recommends setting it in the `init` API.
  * All the log messages from the SDK have the `RS SDK` prefix. However, the log messages from custom integrations have the `RS SDK - Custom Device Mode` prefix for easy identification.


## Event data structure

The `rsEvent` parameter contains the event data in the below format:
    
    
    {
      "message": {
        // Standard RudderStack event object
        // Same schema as HTTP API payload
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The event object schema is the same the [HTTP API](<https://www.rudderstack.com/docs/api/http-api/>) payload schema.
>   * User traits are present in `rsEvent.message.context.traits`, while the group traits are available at `rsEvent.message.traits`.
> 


## See also

  * [How to Create Custom Web Device Mode Integrations](<https://www.rudderstack.com/docs/destinations/custom-web-device-mode-integrations/>)

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/configuration-override-options/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/detecting-adblocked-pages/>)