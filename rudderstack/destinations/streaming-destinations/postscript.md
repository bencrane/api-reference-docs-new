# PostScript Destination Beta

Send your event data from RudderStack to PostScript.

* * *

  * __less than a minute

  * 


[PostScript](<https://www.postscript.io/>) is an SMS marketing platform that enables e-commerce brands to create personalized text messaging campaigns and automated flows. It supports subscriber management, custom event tracking, and automated SMS flows based on customer behavior.

## Key features

The PostScript destination integration supports the following features:

Feature| Available| Description  
---|---|---  
Connection modes| Cloud, Warehouse| PostScript supports only cloud mode (Event Stream) and Reverse ETL for event delivery  
Message types| Yes| Supports `identify` and `track` events  
Event batching| Yes| Batch processing for all message types  
Rate limits| Yes| 15 requests per second per token  
User deletion| No| PostScript does not support user deletion functionality  
OAuth| No| Uses API key authentication only  
  
## Links

This documentation is split into the following sections:

  * [Set up PostScript destination in RudderStack](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript/setup-guide/>)
  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript/cloud-mode/>)
  * [Connect Reverse ETL source to PostScript](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript/connect-retl-source/>)


See [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>) to learn more about sending events in these modes.