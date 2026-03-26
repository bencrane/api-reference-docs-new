# Reddit Destination v3 Migration Guide

Migrate your Reddit destination integration from Reddit’s API v2 to the new API v3.

* * *

  * __2 minute read

  * 


This guide walks you through migrating your Reddit destination integration from API v2 to API v3.

> ![success](/docs/images/tick.svg)
> 
> The Reddit API v3 introduces updated event mapping and new capabilities while maintaining compatibility with your existing setup.

## API v3 overview

The new Reddit API v3 introduces the following changes:

  * Support for `test_id` in event properties for testing events in the Reddit dashboard
  * The deprecated `properties.optOut` is replaced with `properties.modes` for data processing options


> ![info](/docs/images/info.svg)
> 
> **API v2 is deprecated but not sunset yet.**.
> 
> RudderStack recommends migrating to API v3 to take advantage of the latest features and ensure continued support.

### New features

The new Reddit API v3 supports the `test_id` property in event properties, which you can use to test events on the Reddit dashboard without affecting your production data.

Example event with `test_id`:
    
    
    {
      "type": "track",
      "event": "Order Completed",
      "userId": "test_user",
      "timestamp": "2025-01-22T13:00:00Z",
      "properties": {
        "test_id": "test_campaign_001",
        "revenue": 99.99,
        "currency": "USD"
      }
    }
    

## Migration steps

Follow these steps to migrate your Reddit destination integration from API v2 to API v3:

### Update API version in dashboard

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), navigate to your Reddit destination.
  2. Go to the **Configuration** tab in the destination page.
  3. Under **Connection Settings** , go to the [**API Version**](<https://www.rudderstack.com/docs/destinations/streaming-destinations/reddit/#connection-settings>) dropdown and select **v3**.
  4. Save your changes.


### Update event properties

  * Review and use the event and [property mappings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/reddit/#supported-mappings>) for API v3, as listed in the Reddit destination documentation.
  * If you are currently using the `optOut` property in your event properties, update your events to use the new `modes` property with the value `["LDU"]` instead.


> ![info](/docs/images/info.svg)
> 
> The `properties.optOut` property is deprecated in v3.
    
    
    {
      "type": "track",
      "event": "Order Completed",
      "userId": "test_user",
      "timestamp": "2025-01-22T13:00:00Z",
      "properties": {
        "optOut": "true",
        "revenue": 99.99,
        "currency": "USD"
      }
    }
    
    
    
    {
      "type": "track",
      "event": "Order Completed",
      "userId": "test_user",
      "timestamp": "2025-01-22T13:00:00Z",
      "properties": {
        "modes": ["LDU"],
        "revenue": 99.99,
        "currency": "USD"
      }
    }
    

## Verify your migration

After migrating to API v3, send some events to verify that they are being processed correctly in the Reddit dashboard. If you are including the `test_id` property in your events, verify that test events appear separately.

## See more

  * [Reddit Destination Setup Guide](<https://www.rudderstack.com/docs/destinations/streaming-destinations/reddit/>)
  * [Reddit Conversions API documentation](<https://business.reddithelp.com/s/article/Conversions-API>)