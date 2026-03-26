# Amazon Audience Configuration Settings

Advanced configuration settings for Amazon Audience destination.

* * *

  * __less than a minute

  * 


This guide lists the advanced configuration settings to receive the data correctly in Amazon Audience.

### Schedule Settings

Set the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) to define how your syncs run.

### Sync Settings

Set the [sync settings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#sync-settings>) to specify if RudderStack should retain the sync logs and retry sending the failed records.

### Configuration settings

Setting| Description  
---|---  
Enable user data hashing| Turn on this setting to hash all the user data before sending it to Amazon Audience. You can keep it disabled if you are already passing the hashed data.  
Type External Audience Id to use while creating Audience| Enter the `external_audience_id` you want to assign to your audience.  
Time To Live| Use this setting to allow batch uploads to refresh your audience on a regular cadence without first removing the previously synchronized records.  
Data Source Countries| Enter the countries from where the data is coming.