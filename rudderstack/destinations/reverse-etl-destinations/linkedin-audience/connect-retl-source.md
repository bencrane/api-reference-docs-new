# Connect Reverse ETL Source to LinkedIn Audience Beta

Configure a Reverse ETL source with your LinkedIn Audience destination.

* * *

  * __5 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the LinkedIn Audience destination. You can create a new audience or use an existing audience to sync the data.

The below steps assume that you have already [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and [configured the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/linkedin-audience/setup-guide/#connection-settings>) for the connected LinkedIn Audience destination.

> ![success](/docs/images/tick.svg)
> 
> You can connect multiple Reverse ETL sources to the LinkedIn Audience destination.

## Audience settings

Setting| Description  
---|---  
Which LinkedIn account would you like to sync to?| Select your LinkedIn Ads account from the dropdown that RudderStack automatically fetches based on your specified [connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/linkedin-audience/setup-guide/#connection-settings>).  
Which type of audience you want to sync data to?| Select the audience type from the dropdown. RudderStack supports two types - **User** and **Company**.  
Sync to new or existing LinkedIn audience| Specify whether you want to sync data to a new or existing LinkedIn audience.  
  


  * If you select **Create a new LinkedIn Audience** , then specify the name and description (optional) for the new audience.
  * Select **Use an existing LinkedIn Audience** if you have an existing audience in LinkedIn. Then, choose the audience automatically prepopulated by RudderStack based on your specified [connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/linkedin-audience/setup-guide/#connection-settings>) and the audience type (user or company) configured above.

  
Sync mode| RudderStack supports only [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) for this integration.  
  
### Mapping settings

> ![info](/docs/images/info.svg)
> 
> RudderStack does not typecast any data while syncing it to LinkedIn - it expects the data to be present in your warehouse in the correct format.
> 
> You can [connect a transformation](<https://www.rudderstack.com/docs/transformations/usage/#from-destination>) to the destination to update the data in the required format.

Use this section to map your warehouse columns to specific LinkedIn Audience fields:

[![LinkedIn Audience mapping settings](/docs/images/reverse-etl-destinations/linkedin-mappings.webp)](</docs/images/reverse-etl-destinations/linkedin-mappings.webp>)

#### Identifier mappings

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports specifying multiple identifiers for both the **User** and **Company** audience types.

For the **User** audience type, RudderStack supports the below LinkedIn identifiers to which you can map your warehouse columns:

Identifier| Description  
---|---  
Email (SHA256)| User’s email in a hex-encoded string format with a maximum length of 64 characters.  
Email (SHA512)| User’s email in a hex-encoded string format with a maximum length of 128 characters.  
[Google Advertising ID](<https://support.google.com/googleplay/android-developer/answer/6048248?hl=en>)| Plain text string (in lower case) with a maximum length of 32 characters.  
  
For the **Company** audience type, RudderStack supports the below identifiers:

Identifier| Description  
---|---  
Company Name| The company name.  
Company Email Domain| Company’s email domain string in a URL format, for example, `linkedin.com`.  
Company Website Domain| Company’s website domain string in a URL format, for example, `www.linkedin.com`.  
Company Page URL| The LinkedIn company page URL with a maximum length of 100 characters, for example, `linkedin.com/company/acmecorp`.  
Organization URN| The LinkedIn company page URN, for example, `urn:li:organizationUrn:123`.  
  
#### Other settings

Apart from the identifier mappings, the **User** audience type also supports the below field mappings:

Field| Description  
---|---  
First Name| User’s first name with a maximum length of 35 characters, for example, `Alex`.  
Last Name| User’s last name with a maximum length of 35 characters, for example, `Keener`.  
Title| User’s title in the company with a maximum length of 50 characters, for example, `Engineer`.  
Company| User’s company name with a maximum length of 50 characters, for example, `Acme Corp`.  
Country| ISO standard two letter country code, for example, `US`.  
  
For the **Company** audience type, RudderStack supports the below field mappings:

Field| Description  
---|---  
Stock Symbol| Stock symbol of the company with a maximum length of 5 letters, for example, `ACME`.  
Industries| Three industry names for the company with a maximum length of 50 characters, for example, `Technology`, `Software`.  
City| City of the company with a maximum length of 50 characters, for example, `New York`.  
State| State or province of the company with a maximum length of 50 characters, for example, `Louisiana`.  
Country| ISO standard two letter country code, for example, `US`.  
Postal Code| Postal code of the company with a maximum length of 20 characters, for example, `560001`.  
  
### User data hashing

Setting| Description  
---|---  
Enable hashing| This setting is toggled on by default and causes RudderStack to send hash-encrypted data to LinkedIn.  
  
**Note that** :

  * This setting is applicable only for the **User** audience type.
  * Toggle off this setting if you are syncing already-hashed data from your warehouse to LinkedIn.

  
  
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

The LinkedIn Audience destination supports only `record` events.

A sample `record` event that RudderStack sends to LinkedIn depending on the audience type is shown:
    
    
    {
      "type": "record",
      "action": "insert",
      "fields": {
        "title": "Mr.",
        "lastName": "Keener",
        "firstName": "Alex"
      },
      "channel": "sources",
      "context": {
        "sources": {
          "job_id": "<job_id>",
          "version": "<version>",
          "job_run_id": "<job_run_id>",
          "task_run_id": "<task_run_id>"
        }
      },
      "recordId": "4",
      "rudderId": "853ae90f-0351-424b-973e-a615e6487517",
      "messageId": "7416cf4a-e5bd-4a3b-b2ff-805e7f39f5a0",
      "receivedAt": "2024-11-18T14:01:09.737Z",
      "request_ip": "1.2.3.4",
      "identifiers": {
        "sha256Email": "alex@example.com",
        "sha512Email": "alex@example.com"
      }
    }
    
    
    
    {
      "type": "record",
      "action": "insert",
      "fields": {
        "city": "New York",
        "industries": "Information Technology",
        "country": "USA"
      },
      "channel": "sources",
      "context": {
        "sources": {
          "job_id": "<job_id>",
          "version": "<version>",
          "job_run_id": "<job_run_id>",
          "task_run_id": "<task_run_id>"
        }
      },
      "recordId": "5",
      "rudderId": "853ae90f-0351-424b-973e-a615e6487517",
      "messageId": "8dbf3a72-8f4d-4499-b1fd-72b1f930dc3a",
      "receivedAt": "2024-11-18T14:16:55.481Z",
      "request_ip": "<ip>",
      "identifiers": {
        "companyName": "Acme Inc.",
        "organizationUrn": "urn:isbn:<org_id>",
        "companyWebsiteDomain": "example.com",
        "companyEmailDomain": "example.com"
      }
    }