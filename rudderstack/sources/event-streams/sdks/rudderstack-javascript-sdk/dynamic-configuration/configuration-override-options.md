# sourceConfigurationOverride Parameter Reference

> Version: Latest (v3)v1.1

# sourceConfigurationOverride Parameter Reference

Reference for the `sourceConfigurationOverride` parameter used for dynamically configuring device mode destinations in the RudderStack JavaScript SDK.

* * *

  * __2 minute read

  * 


This guide provides a detailed reference for the `sourceConfigurationOverride` parameter used for dynamically configuring device mode destinations in the RudderStack JavaScript SDK.

## Overview

The `sourceConfigurationOverride` option of the JavaScript SDK’s [`load` API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) lets you dynamically modify destination configurations when initializing the RudderStack JavaScript SDK. This parameter provides programmatic control over device mode destinations without requiring dashboard configuration changes.

See [How to Dynamically Configure Device Mode Destinations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/>) for more information on using this parameter.

## `sourceConfigurationOverride` structure
    
    
    {
      sourceConfigurationOverride: {
        destinations: [
          {
            id: string,           // Required
            config: object        // Optional
          }
        ]
      }
    }
    

### The `destinations` array

The `destinations` array contains objects that specify which destinations to override and how to modify them. Each object in the array contains the following properties:

Parameter| Type| Description  
---|---|---  
`id`  
Required| String| The unique identifier of the destination configured in your RudderStack dashboard  
`config`| Object| Configuration properties to override for the destination.  
  
### The `config` object

The `config` object contains destination-specific configuration properties that override the corresponding values from the RudderStack dashboard configuration.

Note that different destinations support different configuration properties. Some examples are listed in the below table:

Destination| Configuration properties| Example values  
---|---|---  
Google Analytics 4| `measurement_id`| `G-XXXXXXXXXX`  
Facebook Pixel| `pixel_id`| `1234567890123456`  
  
> ![info](/docs/images/info.svg)
> 
> The configuration fields may change over time as destinations are updated. [Verify the current field names](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/#determine-the-configuration-fields-to-override>) in the source configuration response before implementing the overrides.

## Configuration merging strategy

The SDK merges the configuration overrides specified in the `sourceConfigurationOverride` parameter with the source configuration from RudderStack using the following rules:

  * Only explicitly overridden fields are changed — all other configuration values are inherited from the dashboard configuration.
  * Override values can change the data type of a property (for example, string to object).
  * Setting a field to `null` or `undefined` removes it from the final configuration. RudderStack does not perform any further validation.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/register-custom-integrations/>)