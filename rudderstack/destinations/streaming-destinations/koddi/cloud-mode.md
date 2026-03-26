# Koddi Cloud Mode Integration Beta

Send events to Koddi using RudderStack cloud mode.

* * *

  * __3 minute read

  * 


After you have successfully instrumented Koddi as a destination in RudderStack, follow this guide to correctly send your events to Koddi in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/koddi>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track the impressions, clicks, and conversions on any ad by any user in Koddi.

### Ad impressions

You can track the impression activity in Koddi using the [Impressions API](<https://developers.koddi.com/reference/impressions-1>).

A sample track call for the `Impressions` event is as shown:
    
    
    rudderanalytics.track(
      "Impressions Event", {
        tracking_data: "your-tracking-data",
        rank: 1,
        beacon_issued: "2024-03-04T15:32:56.409Z"
      }, {
        integrations: {
          All: true,
          koddi: {
            eventType: "Impressions" // case-insensitive
          },
        }
      }
    );
    

#### Supported mappings

RudderStack maps the following `track` fields to the corresponding Koddi properties for `Impressions` event type:

RudderStack event/property| Koddi property| Data type  
---|---|---  
`properties.tracking_data`  
Required| `trackingData`| String  
`properties.rank`  
Required| `rank`| Integer  
`properties.beacon_issued`  
Required| `beaconIssued`| Date-Time  
`timestamp`  
`originalTimestamp`| `ts`| Date-Time  
  
### Ad clicks

You can track the click activity in Koddi using the [Click API](<https://developers.koddi.com/reference/clicks-1>).

A sample track call for the `Click` event is as shown:
    
    
    rudderanalytics.track(
      "Clicks Event", {
        tracking_data: "your-tracking-data",
        rank: 1,
        beacon_issued: "2024-03-04T15:32:56.409Z",
        test_version_override: "2",
        overrides: `{encrypted({"cpc": 1.5, "rank": 1})}`
      }, {
        "integrations": {
          "All": true,
          "koddi": {
            "eventType": "Clicks" // case-insensitive
          }
        },
      }
    );
    

#### Supported mappings

RudderStack maps the following `track` fields to the corresponding Koddi properties for `Clicks` event type:

RudderStack event/property| Koddi property| Data type  
---|---|---  
`properties.tracking_data`  
Required| `trackingData`| String  
`properties.rank`  
Required| `rank`| Integer  
`properties.beacon_issued`  
Required| `beaconIssued`| Date-Time  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `userGuid`| String  
`properties.test_version_override`| `testVersionOverride`| String  
`properties.destination_url`| `destinationUrl`| String  
`properties.overrides`| `overrides`| String  
  
### Ad conversions

You can track the conversions activity in Koddi using the [Conversions API](<https://developers.koddi.com/reference/conversions-1>).

A sample track call for the `Conversions` event is as shown:
    
    
    rudderanalytics.track(
      "Conversions Event", {
        currency: "USD",
        transaction_id: "123",
        bidders: [{
          "bidder": "bidder1", //required
          "alternate_bidder": "alternate1", // required if bidder is not present
          "count": 1, // required
          "base_price": 100, // required
          "total_price": 220
        }]
      }, {
        "integrations": {
          "All": true,
          "koddi": {
            "eventType": "Conversions" // case-insensitive
          }
        },
      }
    );
    

#### Supported mappings

RudderStack maps the following `track` fields to the corresponding Koddi properties for `Conversions` event type:

RudderStack event/property| Koddi property| Data type| Notes  
---|---|---|---  
`context.locale`  
Required| `culture`| String| -  
`properties.currency`  
Required| `currency`| String| -  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `user_guid`| String| -  
`properties.order_id`  
`properties.transaction_id`  
Required| `transaction_id`| String| -  
`properties.bidders`  
Required| `bidders`| []Object| See the below note for more information.  
`context.ip`  
`request_ip`| `user_ip`| String| -  
`context.userAgent`| `user_agent`| String| -  
`context.page.referring_domain`| `domain`| String| -  
`context.device.type`| `device_type`| String| -  
`properties.conversion_source`| `conversion_source`| String| -  
`timestamp`  
`originalTimestamp`| `unixtime`| Double| Rudderstack’s timestamp is in ISO 8601 date format which gets converted to `unixtime` during transformation.  
  
Note that the `properties.bidders` must contain an object’s array where all the objects must contain `bidder`/`alternate_bidder`, `count`, and `base_price` as the required fields. For example:
    
    
    "bidders": [
       {
          "bidder": "bidder1",  //required
          "alternate_bidder": "alternate1", // required if bidder is not present
          "count": 1, // required
          "base_price": 100, // required
          "total_price": 227
          "check_in": "2024-03-04T15:32:56.409Z"
          "check_out": "2024-03-04T15:32:56.409Z"
       }
    ]