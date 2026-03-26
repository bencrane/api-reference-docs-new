# Connect Reverse ETL Source to Google Ads Remarketing Lists

Configure a Reverse ETL source with your Google Ads Remarketing Lists destination.

* * *

  * __4 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Google Ads Remarketing Lists destination. You can create a new audience or use an existing audience to sync the data.

The below steps assume that you have already [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and [configured the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/setup-guide/#connection-settings>) for the connected Google Ads Remarketing Lists destination.

> ![success](/docs/images/tick.svg)
> 
> You can connect multiple Reverse ETL sources to the Google Ads Remarketing Lists destination.

## List settings

Setting| Description  
---|---  
Choose whether to create a new Google Ads Remarketing List| Specify whether you want to sync data to a new or existing Google Ads list.  
  


  * If you select **Create a new Remarketing List** , then specify the name and description (optional) for the new list.
  * Select **Use an existing Remarketing List** if you have an existing list in Google Ads. Then, choose the list automatically prepopulated by RudderStack based on your specified [connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/setup-guide/#connection-settings>).

  
Sync mode| RudderStack supports only [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) for this integration.  
Type of list| Select the type of list where you want to sync the data. RudderStack provides three options:

  * **General** : You can send email, phone number, and address information in this list. RudderStack hashes this data and sends it to Google Ads Remarketing Lists depending on the **Enable Hashing** setting (described below) is toggled on.
  * **User ID** : You can send third party user IDs in this list.
  * **Mobile Device ID** : You can send mobile device IDs in this list.

  
Enable Hashing| This setting is turned on by default and causes RudderStack to hash the `email`, `phone`, `firstName`, and `lastName` fields in the SHA-256 format.  
User Data Consent| Specify the consent type for the uploaded users for using their data in Google Ads. RudderStack provides four options for this setting:  
  


  * **Unspecified**
  * **Unknown**
  * **Granted**
  * **Denied**

Note that if you do not set this field, RudderStack sets it to **Unspecified** , by default.  
Personalization Consent| Specify consent for uploaded users for personalizing ads. RudderStack provides four options for this setting:  
  


  * **Unspecified**
  * **Unknown**
  * **Granted**
  * **Denied**

Note that if you do not set this field, RudderStack sets it to **Unspecified** by default.  
  
### Mapping settings

Use this section to map your warehouse columns to specific Google Ads fields:

[![GARL mapping settings](/docs/images/reverse-etl-destinations/google-ads-list-identifier-mappings.webp)](</docs/images/reverse-etl-destinations/google-ads-list-identifier-mappings.webp>)

### Schedule settings

RudderStack determines how and when to run a sync based on the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) you set for your Reverse ETL connection.

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time (in UTC).  
CRON| Run syncs based on a specified CRON expression (in UTC).  
Manual| Run syncs manually.  
  
### Sync observability settings

Setting| Description  
---|---  
Retain sync logs| This setting is toggled on by default and instructs RudderStack to store the sync logs in your warehouse. You can also configure the below settings:  
  
| Setting| Description  
---|---  
Sync log retention| Specify the retention period of the [sync logs](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#sync-logs>) in your warehouse.  
  
If you set it to 1, then RudderStack deletes any sync log older than a day (in UTC time).  
Snapshot table retention| Specify the number of [snapshot tables](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#snapshot-table-schema>) to retain.  
Retry failed records| This setting is toggled on by default and causes RudderStack to continually [retry sending the failed records](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#retry-failed-records>).  
  
> ![warning](/docs/images/warning.svg)
> 
> Storing sync logs and snapshot tables may incur additional warehouse costs.

## `record` event structure

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The Google Ads Remarketing Lists destination supports only `record` events. You can send up to 100000 user records in one event.
>   * RudderStack supports both additions and deletions to a user list.
> 


The following code snippet shows a sample `record` event that adds a new record to the user list:
    
    
    {
      "action": "insert",
      "context": {
        "ip": "1.2.3.4",
        "library": {
          "name": "http",
        },
      },
      "recordId": "2",
      "rudderId": "2",
      "fields": {
        "email": "alex@example.com",
        "firstName": "Alex",
        "lastName": "Keener",
        "country": "US",
        "postalCode": "50001",
      },
      "type": "record",
    }
    

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.