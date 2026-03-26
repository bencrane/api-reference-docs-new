# Connect Reverse ETL Source to X Audience Beta

Configure a Reverse ETL source with your X Audience destination.

* * *

  * __4 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the X Audience destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your X Audience destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/x-audience/setup-guide/#connection-settings>) for X Audience destination and click **Continue**.

  2. In the **Where do you want to sync data to?** section:

     * Select **Create New audience** if you want to create a new data segment in X Audience. Specify the name and description of the data segment in the respective fields.
     * Select **Use Existing Audience** if you have an existing audience segment in X Audience and specify the **Audience ID**.
  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to X Audience.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently supports syncing data to X Audience via mirror mode only.

  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific X Audience fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/x-audience-identifier-map-fields.webp)](</docs/images/event-stream-destinations/x-audience-identifier-map-fields.webp>)

## Schedule settings

RudderStack determines how and when to run a sync based on the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) you set for your Reverse ETL connection.

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time (in UTC).  
CRON| Run syncs based on a specified CRON expression (in UTC).  
Manual| Run syncs manually.  
  
See [Sync Schedule Settings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) guide for more information.

## Sync settings

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

See [Sync Observability Settings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/>) guide for more information.

## VDM mappings

RudderStack maps the below fields to the **optional** X Audience fields:

RudderStack property| X Audience property| Comments  
---|---|---  
`email`| `email`| String with comma-separated emails.  
`phone_number`| `phone_number`| String with comma-separated phone numbers.  
`device_id`| `device_id`| String with comma-separated device IDs (IDFA/AdID/Android ID of the user’s device).  
`twitter_id`| `twitter_id`| String with comma-separated Twitter IDs.  
`partner_user_id`| `partner_user_id`| String with comma-separated user IDs present in the partners’ system.  
`handle`| `handle`| String with comma-separated handles (@s) belonging to the user.  
`effective_at`| `effective_at`| UTC time (in string format) at which the custom audience association takes effect. It should be present in the ISO 8601 timestamp format.  
  
**Note** : By default, RudderStack sets it to the current date and time.  
`expires_at`| `expires_at`| UTC time (in string format) at which the custom audience association expires. It should be present in the ISO 8601 timestamp format.  
  
**Note** : The specified time must be later than the value of `effective_at`. By default, RudderStack sets it to 13 months from the request timestamp.  
User parameters (see below)| `users`| List of objects.  
  
## `record` event structure

RudderStack supports both updates and deletions to a user list sent to X.

The following code snippet shows a sample `record` event that RudderStack sends to X Audience:
    
    
    POST https://ads-api.x.com/12/accounts/<account_id>/custom_audiences/1nmth/users
    [
      {
        "operation_type": "Update",
        "params": {
          "effective_at": "2018-05-15T00:00:00Z",
          "expires_at": "2019-01-01T07:00:00Z",
          "users": [
            {
              "email": [
                "4798b8bbdcf6f2a52e527f46a3d7a7c9aefb541afda03af79c74809ecc6376f3"
              ],
              "handle": [
                "7352f353c460e74c7ae226952d04f8aa307b12329c5512ec8cb6f1a0f8f9b2cb",
                "49e0be2aeccfb51a8dee4c945c8a70a9ac500cf6f5cb08112575f74db9b1470d"
              ]
            },
            {
              "email": [
                "5bf13d5ad4200407c5bc8b9bb578e425d05ef936fd488e3799a9d0806669223c"
              ],
              "twitter_id": [
                "34d56c7159a7eea941f359653029410f813f65a1d2d13ecc5ccbdd5a8cb755cf",
                "00e7b76c9739dec57f4c4a20ec021a20ffcf26bd00f519b17ea00f0ed6048f85"
              ]
            }
          ]
        }
      },
      {
        "operation_type": "Delete",
        "params": {
          "effective_at": "2018-05-15T00:00:00Z",
          "expires_at": "2019-01-01T07:00:00Z",
          "users": [
            {
              "device_id": [
                "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
              ],
              "email": [
                "4798b8bbdcf6f2a52e527f46a3d7a7c9aefb541afda03af79c74809ecc6376f3"
              ],
              "handle": [
                "461222f5dd690a20651c3d19848015cb0369db3f8e937571ffb775de70750847"
              ],
              "twitter_id": [
                "c623c7e163984493b46c547088542e95d0aaa529bc52bbecce3ff91eb6b7843b"
              ]
            },
            {
              "email": [
                "5bf13d5ad4200407c5bc8b9bb578e425d05ef936fd488e3799a9d0806669223c"
              ],
              "twitter_id": [
                "858cdc7f313f84a3f3c48e9a6323307c1ef1bb7439b8e3623e140454b0fd8fa5",
                "bb074e154657b91d99bd1bb3757409149670e8ae7a0fe9136fae29a26a7881c8"
              ]
            }
          ]
        }
      }
    ]
    
    
    
    {
      "request": {
        "params": {
          "account_id": "<account_id>",
          "custom_audience_id": "1nmth"
        }
      },
      "data": {
        "success_count": 4,
        "total_count": 4
      }
    }
    

## FAQ

#### Where can I find the X Audience ID?

  1. In your X Audience Manager, go to **Tools** > **Audiences**.
  2. Click **Edit** next to the audience for which you want the Audience ID.

[![](/docs/images/event-stream-destinations/x-audience-id-1.webp)](</docs/images/event-stream-destinations/x-audience-id-1.webp>)

  3. Note the **Audience ID** displayed in the URL (`/audience/<AUDIENCE_ID>/edit`)

[![](/docs/images/event-stream-destinations/x-audience-id-2.webp)](</docs/images/event-stream-destinations/x-audience-id-2.webp>)

Once you obtain the **Audience ID** , specify it in the **Use Existing Audience** setting under the **Where do you want to sync data to?** section of the X Audience destination configuration.

[![](/docs/images/event-stream-destinations/x-audience-id.webp)](</docs/images/event-stream-destinations/x-audience-id.webp>)

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.