# Connect Reverse ETL Source to Facebook Custom Audience

Configure a Reverse ETL source with your Facebook Custom Audience destination.

* * *

  * __7 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Facebook Custom Audience destination. You can create a new custom audience or use an existing audience to sync the data.

The below steps assume that you have already [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and [configured the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/setup-guide/#connection-settings>) for the connected Facebook Custom Audience destination.

> ![success](/docs/images/tick.svg)
> 
> You can connect multiple Reverse ETL sources to the Facebook Custom Audience destination.

## Mapping settings

In the mapping window, you will see the below two options:

  * **Create a new Facebook Custom Audience** : Use this option to create a new custom audience in Facebook. You can specify the **Audience name** and **Audience description** of the new Facebook audience.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports the below two audience types:
> 
>   * [Custom Audiences](<https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences>)
>   * [Value-based lookalike audiences](<https://en-gb.facebook.com/business/help/917879191754763?id=401668390442328>) — see Create new value-based lookalike audiences section for more information.
> 


  * **Use an existing Facebook Custom Audience** : Use this option if you have an existing custom audience. Choose the audience (automatically prepopulated by RudderStack based on your specified [connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/setup-guide/#connection-settings>)) from the dropdown.


Then, specify the below settings:

Setting| Description  
---|---  
Sync mode| RudderStack supports only [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) for this integration.  
Enable hashing| Turn on the toggle to allow RudderStack to hash encode user data irrespective of the schema type chosen in the RudderStack dashboard.  
  
**Note** : Facebook expects the user data to be hash encoded using `SHA256`.  
Disable format| Turn on the toggle to **not** format the user data before sending it to the custom audience. Facebook has fixed data formats for all the allowed schema fields.  
  
See the Explicit formatting feature section for more information.  
Type| Specify the type of the audience from the dropdown.  
Sub-type| Specify the sub-type of the audience from the dropdown.  
  
> ![info](/docs/images/info.svg)
> 
> See the [Facebook documentation](<https://developers.facebook.com/docs/marketing-api/reference/custom-audience/#:~:text=the%20uploaded%20file-,data_source,-CustomAudienceDataSource>) for more information on the **Type** and **Sub-type** fields.

## Choose identifier mappings

Map your warehouse columns to specific Facebook Custom Audience fields:

[![](/docs/images/event-stream-destinations/fb-custom-audience-mappings.webp)](</docs/images/event-stream-destinations/fb-custom-audience-mappings.webp>)

If you have selected the **Create a new Facebook Custom Audience** option, RudderStack creates a new audience in Facebook with the same **Ad Account ID** configured in the [connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/setup-guide/#connection-settings>).

[![](/docs/images/event-stream-destinations/fb-custom-audience-connection-settings.webp)](</docs/images/event-stream-destinations/fb-custom-audience-connection-settings.webp>)

## Manage value-based lookalike audiences

This section describes the steps to map your warehouse data to a new or existing value-based lookalike audience.

### Create new audience

To create a new [value-based lookalike audience](<https://en-gb.facebook.com/business/help/917879191754763?id=401668390442328>), you need to map a relevant warehouse column to the **Lookalike Value** field in the Identifier mappings.

Follow these steps:

  1. In the mapping window, select **Create a new Facebook Custom Audience** and specify the below settings:

Setting| Description  
---|---  
Audience name| Specify the name of the audience.  
Audience description| Specify the description of the audience.  
  
  2. Configure the rest of the mapping settings.
  3. In the **Choose identifier mappings** window, map a relevant warehouse column to the **Lookalike Value** field.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack will not create a value-based lookalike audience if you do not include the **Lookalike Value** in your identifier mappings — it will create a [custom audience](<https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences>) instead.
>   * You can update the mapping for the **Lookalike Value** field after the audience is created.
> 


[![](/docs/images/event-stream-destinations/new-audience-lookalike-value.webp)](</docs/images/event-stream-destinations/new-audience-lookalike-value.webp>)

  4. Add the rest of the identifier mappings as per your requirement.
  5. Continue with the rest of the setup.


### Use an existing value-based lookalike audience

To use an existing value-based lookalike audience:

  1. Select the value-based lookalike audience from the dropdown.
  2. Configure the rest of the mapping settings.
  3. In the **Choose identifier mappings** window, map a relevant warehouse column to the **Lookalike Value** field.


> ![info](/docs/images/info.svg)
> 
> You can update the mapping for the **Lookalike Value** field after the audience is created.

[![](/docs/images/event-stream-destinations/existing-audience-lookalike-value.webp)](</docs/images/event-stream-destinations/existing-audience-lookalike-value.webp>)

  4. Add the rest of the identifier mappings as per your requirement.
  5. Continue with the rest of the setup.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the audience type from a value-based lookalike audience to a regular custom audience (and vice versa) after the audience is created.

## Schedule settings

RudderStack determines how and when to run a sync based on the [sync schedule](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) you set for your Reverse ETL connection.

Schedule type| Description  
---|---  
Basic| Run syncs at a given time interval and specified time (in UTC).  
CRON| Run syncs based on a specified CRON expression (in UTC).  
Manual| Run syncs manually.  
  
## Sync observability settings

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

The Facebook Custom Audience destination supports only `record` events.

A sample `record` event that RudderStack sends to Facebook is shown:
    
    
    {
      "action": "insert",
      "channel": "sources",
      "context": {
        "sources": {
          "job_id": "2o9EffQ0mAIrGAgRxcLuwxhiXM0",
          "job_run_id": "cskrt1kme831eq0jrafg",
          "task_run_id": "cskrt1sme831eq0jrag0",
          "version": "v1.57.0-rc.1"
        }
      },
      "fields": {},
      "identifiers": {
        "EMAIL": "alex@example.com"
      },
      "messageId": "997b78eb-d06a-4123-b4d6-d3b87b62c3a9",
      "receivedAt": "2024-11-05T06:43:27.176Z",
      "recordId": "1",
      "request_ip": "10.1.17.46",
      "rudderId": "853ae90f-0351-424b-973e-a615e6487517",
      "type": "record"
    }
    

Parameter| Description  
---|---  
`context`| Used for internal metrics for a sync task run.  
`recordId`| Ordering ID that RudderStack adds when delivering the events from the warehouse.  
`messageId`| UUID generated by RudderStack.  
`rudderId`| UUID generated by RudderStack.  
  
### Schema fields mapping

The following table details the schema fields mappings specified in the RudderStack dashboard:

Dashboard field name| Marketing API schema field (RudderStack-supported field name)| Guidelines  
---|---|---  
`EMAIL`| `EMAIL`| Trim any leading or trailing whitespaces and convert all the characters to lower case.  
`PHONE`| `PHONE`| Remove symbols, letters, and any leading zeroes. The country code is needed as a prefix, if the `COUNTRY` field is not specified in the dashboard.  
`GENDER`| `GEN`| Use these values: `m` or `male` for male and `f` or `female` for female.  
`MADID`| `MADID`| Use lowercase and keep the hyphens. This information will not be hashed.  
`EXTERN_ID`| `EXTERN_ID`| This information will not be hashed.  
`DOB YEAR (YYYY)`| `DOBY`| Use the YYYY format from `1900` to the current year.  
`DOB MONTH (MM)`| `DOBM`| Use the MM format from `01` to `12`.  
`DOB DATE (DD)`| `DOBD`| Use the DD format from `01` to `31`.  
`LAST NAME`| `LN`| Use a-z only. Lower case only, no punctuation. Use special characters in the UTF-8 format.  
`FIRST NAME`| `FN`| Use a-z only. Lower case only, no punctuation. Use special characters in the UTF-8 format.  
`FIRST NAME INITIAL`| `FI`| Use a-z only. Lower case only. Use special characters in the UTF-8 format.  
`CITY`| `CT`| Use a-z only. Lower case only, with no punctuation, no special characters, and no whitespace.  
`US STATES`| `ST`| Use the 2-character ANSI abbreviation code in lower case. Normalize the states outside the US in lowercase, with no punctuation, no special characters, and no white space.  
`ZIP`| `ZIP`| Use lower case and no white space. For US, use only the first 5 digits. For UK, use the Area/District/Sector format.  
`COUNTRY`| `COUNTRY`| Use lower case, 2-letter ISO 3166-1 alpha-2 country codes.  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack modifies the schema names visible in the dashboard to ensure better readability. However, during the event call, the field names **must be exactly the same as** the schema names specified by Facebook Marketing API, as mentioned in the table above.

### Explicit formatting feature

By default, RudderStack formats the data as prescribed by Facebook before sending it to the destination, as shown in the below table:

Schema field name| Example input| Formatted output (before hashing)  
---|---|---  
`EMAIL`| `ABC@gmail.com`| `abc@gmail.com`  
`PHONE`| `0@96346895`| `96346895`  
`GEN`| `FEMALE`| `f`  
`DOBD`| `2`| `02`  
`DOBM`| `1`| `01`  
`LN & FN`| `Abc,@`| `abc@`  
`FI`| `Mr.`| `mr.`  
`CT`| `HN#`| `hn`  
`ST`| `? AL ?`| `al`  
`ZIP`| `11502 @bc`| `11502@bc`  
`COUNTRY`| `IN`| `in`  
  
If you turn on the Disable Format toggle in the RudderStack dashboard, RudderStack **does not** format the user data in the format prescribed by the Facebook Marketing API.

## FAQ

#### Where can I find the Custom Audience ID?

  1. To get your Custom Audience ID, go to the Facebook Ads Manager account. On the left navigation bar, select **Audiences** and choose the Ad account you have created the custom audience for.

[![Customer audience ID](/docs/images/event-stream-destinations/fb-custom-audience-id-1.webp)](</docs/images/event-stream-destinations/fb-custom-audience-id-1.webp>)

  2. Click **All Audiences** and select the specific custom audience from the list.
  3. Finally, click the **History** tab. Here, you will find the audience ID under the **Item Changed** column:

[![Customer audience ID](/docs/images/event-stream-destinations/fb-custom-audience-id-2.webp)](</docs/images/event-stream-destinations/fb-custom-audience-id-2.webp>)