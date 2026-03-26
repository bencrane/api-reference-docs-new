# How to Dynamically Configure Device Mode Destinations

> Version: Latest (v3)v1.1

# How to Dynamically Configure Device Mode Destinations

Dynamically override destination configurations and toggle destination status at the instrumentation level using the RudderStack JavaScript SDK.

* * *

  * __3 minute read

  * 


This guide explains how to dynamically configure device mode destinations using the RudderStack JavaScript SDK.

## Overview

Managing destination configurations across thousands of websites can be challenging when relying solely on the [RudderStack dashboard](<https://app.rudderstack.com/>). The dynamic device mode destinations configuration feature lets you override destination-specific configuration values and toggle destination status directly at the instrumentation level when initializing the RudderStack JavaScript SDK.

> ![success](/docs/images/tick.svg)
> 
> This approach gives you granular, flexible control over your SDK behavior without needing to update configuration from the RudderStack dashboard for each website or application.

## Prerequisites

  * RudderStack JavaScript SDK v3.20.1 or later
  * Valid write key and data plane URL
  * Existing device mode destinations configured in your [RudderStack dashboard](<https://app.rudderstack.com/>)


## Override destination configuration

You can override specific configuration values for your destinations using the [`sourceConfigurationOverride` option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/configuration-override-options/>) in the SDK’s `load` API.

### Basic configuration override
    
    
    rudderanalytics.load(<WRITE_KEY>, <DATA_PLANE_URL>, {
      sourceConfigurationOverride: {
        destinations: [
          {
            id: "<destination-id>",  // Destination ID for the Facebook Pixel destination
            config: {
              pixel_id: "new_pixel_id_value",
              project_key: "updated_project_key"
            }
          },
          {
            id: "<destination-id-1>",  // Destination ID for the Google Analytics 4 destination
            config: {
              measurement_id: "G-XXXXXXXXXX"
            }
          }
        ]
      }
    });
    

See the [Configuration merging strategy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/configuration-override-options/#configuration-merging-strategy>) section for more information on how the SDK merges the configuration overrides with the source configuration from RudderStack.

#### Obtain the destination ID

In the [RudderStack dashboard](<https://app.rudderstack.com/>), go to the **Settings** of the destination page to find the destination ID.

[![Destination ID in the RudderStack dashboard](/docs/images/event-stream-destinations/destination-id.webp)](</docs/images/event-stream-destinations/destination-id.webp>)

#### Determine the configuration fields to override

To identify the exact configuration fields available for override, inspect the source configuration response from RudderStack:

  1. Open your browser’s developer tools.
  2. Navigate to the **Network** tab.
  3. Load your web page with the RudderStack SDK.
  4. Look for the source configuration request (typically to `sourceConfig` endpoint).
  5. Examine the response (`destinations[index].config`) to see the available configuration fields for each destination.

[![Source configuration response from the JavaScript SDK](/docs/images/event-stream-sources/source-config-response.webp)](</docs/images/event-stream-sources/source-config-response.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Configuration fields may change over time as destinations are updated. Always verify the current field names in the source configuration response before implementing the overrides.

## Verification

To verify your setup after implementing dynamic configuration:

  * Check the browser console for any warnings about invalid destination IDs.
  * Confirm that events are being sent to the correct destinations with updated configuration values.
  * Use your destination’s analytics interface to verify that data is flowing as expected.


## Best practices

  * Use overrides only when necessary to maintain clear and traceable configuration behavior.
  * Use exact property names as they appear in the source configuration response.
  * Validate destination IDs before using them in configuration overrides.
  * Do not override the required fields to `null` or `undefined`, otherwise you might encounter an error or unexpected behavior.
  * Test configuration changes in a development environment first.


## Troubleshooting

This section provides troubleshooting tips for common issues you may encounter when dynamically configuring device mode destinations.

### Invalid destination ID warnings

If you see console warnings about invalid destination IDs:

  * Verify that the destination ID in your override matches exactly with the destination ID present in the dashboard.
  * Ensure the destination is configured as a device mode destination in the RudderStack dashboard.
  * Verify that the destination corresponding to the destination ID is enabled.


### Configuration not taking effect

If your configuration overrides aren’t working:

  * Confirm you’re specifying the correct field names by inspecting the source configuration response.
  * Verify that the data types of your override values match the expected format.
  * Check that you’re only overriding the `config` field, as other fields are not supported.


### Events not reaching destinations

If events aren’t reaching your destinations after configuration:

  * Verify that **required** configuration fields (like measurement IDs or pixel IDs) are set correctly.
  * Check your destination’s debug or real-time view to confirm event delivery.


## Limitations

  * You can override the configuration for only the [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) destinations.
  * You can override only the `config` field per destination.


## See also

  * [`sourceConfigurationOverride` parameter reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#configure-device-mode-destinations-dynamically>)

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/dynamic-configuration/configuration-override-options/>)