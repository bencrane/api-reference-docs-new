# Google Ads Offline Conversions Destination Beta

Send your event data from RudderStack to Google Ads Offline Conversions.

* * *

  * __less than a minute

  * 


[Google Ads Offline Conversions](<https://support.google.com/google-ads/answer/2998031?hl=en&ref_topic=7280668>) helps you track the offline sales which occur when your ads lead to a click or call to your business. It lets you measure your sale conversions in the offline mode after a user clicks your ad online but does not directly proceed to sale in the online mode.

## Key features

The Google Ads Offline Conversions destination integration supports the following features:

Feature| Available| Description  
---|---|---  
Connection modes| Cloud| Google Ads Offline Conversions supports only cloud mode (Event Stream) for event delivery  
Message types| Yes| Supports `track` events for conversion tracking  
Conversion types| Yes| Supports click, call, and store sales conversions  
Custom event mapping| Yes| Map RudderStack events to Google Ads conversion types  
User identification| Yes| Supports email and phone number identification with SHA-256 hashing  
Consent management| Yes| Supports user consent specification for ad data and personalization  
Batching support| No| Google Ads Offline Conversions does not support event batching  
User deletion| No| Google Ads Offline Conversions does not support user deletion  
  
## Links

This documentation is split into the following sections:

  * [Set up Google Ads Offline Conversions destination in RudderStack](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads-offline-conversions/setup-guide/>)
  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads-offline-conversions/cloud-mode/>)


See [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>) to learn more about sending events in these modes.