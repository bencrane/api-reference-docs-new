# Connect Reverse ETL Source to Bing Ads Audience Beta

Configure a Reverse ETL source with your Bing Ads Audience destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Bing Ads Audience destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Bing Ads destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bing-ads-audience/setup-guide/#connection-settings>) for Bing Ads Audience and click **Continue**.
  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select the **Object** in the **Where do you want to sync data to?** section.
  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Bing Ads.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific Bing Ads fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/bingads-identifier-map-fields.webp)](</docs/images/event-stream-destinations/bingads-identifier-map-fields.webp>)

## `audienceList` event structure

You can add or remove users from an audience by sending the `audienceList` call to Bing Ads.
    
    
    {
      "anonymousId": "2234232hK4el9Z",
      "channel": "sources",
      "properties": {
        "listData": {
          "add": [{
              "email": "alex@example.com"
            },
            {
              "email": "julie@example.com"
            },
            {
              "email": "peter@example.com"
            },
            {
              "email": "russell@example.com"
            },
            {
              "email": "john@example.com"
            }
          ],
        }
      },
      "type": "audienceList",
      "userId": "1hKOmRA4el9Z"
    }
    

RudderStack maps the following properties to Bing Ads properties:

RudderStack property| Data type| Bing Ads property  
---|---|---  
`properties.listData.add[i].email`  
Required| String| `email`  
`properties.listData.remove[i].email`  
Required| String| `email`  
  
## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.