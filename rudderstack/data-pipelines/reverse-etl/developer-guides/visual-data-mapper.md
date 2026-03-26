# Data Mapping with Visual Data Mapper (VDM)

Map your warehouse columns to destination tables with RudderStack’s Visual Data Mapper functionality.

* * *

  * __4 minute read

  * 


The **Visual Data Mapper** (VDM) offers an intuitive UI to map your warehouse columns to specific destination fields. This is useful especially when mapping your warehouse data to custom fields defined in your destination.

> ![success](/docs/images/tick.svg)
> 
> To use this feature, set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and then connect it to a destination that supports VDM.

## Supported destinations

RudderStack supports the Visual Data Mapper for the following destinations:

[![Amplitude logo](/docs/images/logos/destinations/amplitude.svg)Amplitude](</docs/destinations/streaming-destinations/amplitude/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Amazon Audience logo](/docs/images/logos/destinations/amazon.svg)Amazon Audience](</docs/destinations/reverse-etl-destinations/amazon-audience/>)[![Bing Ads Audience logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Audience](</docs/destinations/reverse-etl-destinations/bing-ads-audience/>)[![Bing Ads Offline Conversions logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Offline Conversions](</docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Braze logo](/docs/images/logos/destinations/braze.svg)Braze](</docs/destinations/streaming-destinations/braze/>)[![Criteo Audience logo](/docs/images/logos/destinations/criteo.svg)Criteo Audience](</docs/destinations/reverse-etl-destinations/criteo-audience/>)[![Customer.io logo](/docs/images/logos/destinations/customerio.svg)Customer.io](</docs/destinations/streaming-destinations/customer.io/>)[![Customer.io Audience logo](/docs/images/logos/destinations/customerio.svg)Customer.io Audience](</docs/destinations/reverse-etl-destinations/customerio-audience/>)[![Eloqua logo](/docs/images/logos/destinations/eloqua.svg)Eloqua](</docs/destinations/reverse-etl-destinations/eloqua/>)[![Facebook Custom Audience logo](/docs/images/logos/destinations/facebook.svg)Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)[![Google Ads Remarketing Lists \(Customer Match\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)[![HubSpot logo](/docs/images/logos/destinations/hubspot.svg)HubSpot](</docs/destinations/streaming-destinations/hubspot/>)[![Intercom logo](/docs/images/logos/destinations/intercom.svg)Intercom](</docs/destinations/streaming-destinations/intercom/>)[![Iterable logo](/docs/images/logos/destinations/iterable.svg)Iterable](</docs/destinations/streaming-destinations/iterable/>)[![Klaviyo logo](/docs/images/logos/destinations/klaviyo.svg)Klaviyo](</docs/destinations/streaming-destinations/klaviyo/>)[![Klaviyo Bulk upload logo](/docs/images/logos/destinations/klaviyo.svg)Klaviyo Bulk upload](</docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/>)[![LaunchDarkly Segments logo](/docs/images/logos/destinations/launchdarkly.svg)LaunchDarkly Segments](</docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)[![Linkedin Audience logo](/docs/images/logos/destinations/linkedin.svg)Linkedin Audience](</docs/destinations/reverse-etl-destinations/linkedin-audience/>)[![Mailchimp logo](/docs/images/logos/destinations/mailchimp.svg)Mailchimp](</docs/destinations/streaming-destinations/mailchimp/>)[![Marketo logo](/docs/images/logos/destinations/marketo.svg)Marketo](</docs/destinations/streaming-destinations/marketo/>)[![Marketo Static Lists logo](/docs/images/logos/destinations/marketo.svg)Marketo Static Lists](</docs/destinations/reverse-etl-destinations/marketo-static-lists/>)[![Salesforce logo](/docs/images/logos/destinations/salesforce.svg)Salesforce](</docs/destinations/streaming-destinations/salesforce/>)[![Salesforce Marketing Cloud logo](/docs/images/logos/destinations/salesforce.svg)Salesforce Marketing Cloud](</docs/destinations/streaming-destinations/sfmc/>)[![SFTP logo](/docs/images/logos/destinations/sftp.svg)SFTP](</docs/destinations/reverse-etl-destinations/sftp/>)[![Snapchat Custom Audience logo](/docs/images/logos/destinations/snapchat.svg)Snapchat Custom Audience](</docs/destinations/reverse-etl-destinations/snapchat-custom-audience/>)[![The Trade Desk Audience logo](/docs/images/logos/destinations/the-trade-desk.svg)The Trade Desk Audience](</docs/destinations/reverse-etl-destinations/trade-desk-audience/>)[![TikTok Audiences logo](/docs/images/logos/destinations/tiktok-ads.svg)TikTok Audiences](</docs/destinations/reverse-etl-destinations/tiktok-audiences/>)[![Yandex.Metrica Offline Events logo](/docs/images/logos/destinations/yandex-metrica.svg)Yandex.Metrica Offline Events](</docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/>)[![X Audience logo](/docs/images/logos/destinations/twitter.svg)X Audience](</docs/destinations/reverse-etl-destinations/x-audience/>)

  


## Use Visual Data Mapper

> ![info](/docs/images/info.svg)
> 
> By default, Visual Data Mapping is enabled for all the supported destinations. Click the **Map with JSON** button to [configure the data mappings via JSON](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>).

  1. Select the destination **Object** where you want to sync the data.


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * RudderStack automatically loads all the relevant destination objects. If you have added a new destination object during this configuration process, click **Reload objects** to get all the latest objects.
>   * RudderStack **does not** support objects that do not have any fields or a unique user identifier.
> 


[![Select object](/docs/images/data-pipelines/vdm-mapping-1.webp)](</docs/images/data-pipelines/vdm-mapping-1.webp>)

  2. Select the [sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) that RudderStack uses to sync your data.


### Choose identifier

In the **Choose Identifier** section, choose a warehouse column and destination field to map your records from the source to the destination. You can choose any column from the dropdown that acts as a unique identifier.

[![Choose idenfier](/docs/images/data-pipelines/vdm-mapping-2.webp)](</docs/images/data-pipelines/vdm-mapping-2.webp>)

> ![warning](/docs/images/warning.svg)
> 
> The **Choose identifier** field must have unique values in order to successfully sync the data to the destination. The records containing duplicate identifier values will **not** sync.
> 
> For example, if you have chosen `name` as the identifier and it contains more than one values like `Alex`, the duplicate records will fail to sync.

### Map fields

In this section, you can configure the specific source-destination field mappings.

  1. Click the **Map another field** option. Select the **Destination field** from the dropdown. Then, select the **Warehouse column** you want to map to this field.

[![Map objects](/docs/images/data-pipelines/vdm-mapping-3.webp)](</docs/images/data-pipelines/vdm-mapping-3.webp>)

> ![success](/docs/images/tick.svg)
> 
> RudderStack gives you full visibility into the name and type of the fields that you are mapping along with a sample preview.

#### **Mandatory mappings**

There are some required fields you need to map when sending events to some destination objects. These fields cannot be removed from the mappings.

For example, in the Salesforce **Account** object, **Account Name** is a required field, as seen in the following image:

[![Map another field](/docs/images/warehouse-actions-sources/vdm-5.webp)](</docs/images/warehouse-actions-sources/vdm-5.webp>)

#### **Map fields of different type/format**

If you are mapping fields with different data types or formats, you can use the [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature to do the type conversion before sending the data.

[![Map another field](/docs/images/warehouse-actions-sources/vdm-6.webp)](</docs/images/warehouse-actions-sources/vdm-6.webp>)

In the above example, RudderStack lets you map the warehouse column `PHONE` of string type to a destination field `Associated Company ID` of float data type. You can then add a transformation at the destination end to do this type conversion to ensure there is no data type mismatch.

### Create custom destination fields

RudderStack lets you create a custom destination field and map it to a warehouse column.

  1. Click the **Map another field** option.
  2. Enter the name of the custom destination field you want to create.
  3. Click **Create**.


> ![info](/docs/images/info.svg)
> 
> In some cases, you must create or define the custom fields in the destination **before** creating them in the RudderStack dashboard.

[![Create custom fields](/docs/images/data-pipelines/vdm-mapping-4.webp)](</docs/images/data-pipelines/vdm-mapping-4.webp>)

#### **Sync data to custom Salesforce objects**

RudderStack **does not support** creating new custom fields for the [Salesforce](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce/>) destination using the above steps. However, you can still use the Visual Data Mapper to sync your data to custom Salesforce objects by following these steps:

  1. Log in to your [Salesforce dashboard](<https://login.salesforce.com/?locale=in>).
  2. In the top navigation bar, click the **Setup** icon and go to **Object Manager**.

[![Salesforce custom object](/docs/images/warehouse-actions-sources/salesforce-custom-object.webp)](</docs/images/warehouse-actions-sources/salesforce-custom-object.webp>)

  3. Go to **Create** > **Custom Object**.
  4. Enter the relevant details and click **Save** to finish the configuration.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to select the **Allow Search** setting under the **Search Status** section, as seen below. Otherwise, the custom object will **not** be visible in the RudderStack dashboard.
> 
> ![Salesforce custom object](/docs/images/warehouse-actions-sources/salesforce-custom-object-1.webp)

  5. In your RudderStack dashboard, click **Reload objects** under the **Object** field. Your newly created custom object should now be visible in this list. Select the object and map the relevant fields to sync your data.

[![Create custom Salesforce fields](/docs/images/data-pipelines/salesforce-custom-object.webp)](</docs/images/data-pipelines/salesforce-custom-object.webp>)

## Update mapping configuration

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * You can update your mapping configuration irrespective of whether the connection is turned on or off.
>   * While updating the mapping configuration, you **cannot** change the **Object** , **Sync mode** , and **Choose identifier** fields. You will have to delete the destination and connect a new destination from scratch to do so.
> 


  1. Go to the **Schema** tab of your Reverse ETL connection page.
  2. Update the mappings as required.
  3. Click **Save** to update the configuration.

[![Update JSON mappings](/docs/images/retl-sources/update-vdm-mapping.webp)](</docs/images/retl-sources/update-vdm-mapping.webp>)