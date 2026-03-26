# Connect Reverse ETL Source to Zoho Beta

Configure a Reverse ETL source with your Zoho destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Zoho destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Zoho destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/setup-guide/#connection-settings>) for Zoho destination and click **Continue**.
  2. In the **Where do you want to sync data to?** section, select the **Object** from the dropdown.

[![](/docs/images/reverse-etl-destinations/zoho-object-type.webp)](</docs/images/reverse-etl-destinations/zoho-object-type.webp>)

  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Zoho.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific Zoho fields using the **Map fields** setting.

[![](/docs/images/reverse-etl-destinations/zoho-identifier-map-fields.webp)](</docs/images/reverse-etl-destinations/zoho-identifier-map-fields.webp>)

> ![info](/docs/images/info.svg)
> 
> Only the searchable fields of a module are visible under the **Destination fields**. Refer FAQ for more information on making the module fields searchable.

## Supported APIs

RudderStack uses the following Zoho APIs to sync data from your Reverse ETL sources:

  * [Upsert Records](<https://www.zoho.com/crm/developer/docs/api/v6/upsert-records.html>)
  * [Delete Records](<https://www.zoho.com/crm/developer/docs/api/v6/delete-records.html>)


## Next steps

  * [Configure advanced settings for Zoho destination](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/configuration-settings/>)


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.

#### Why am I getting an “INVALID_QUERY, the field is not available for search” error while deleting my records?

You can encounter this error if the [OAuth account used for authentication](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/setup-guide/#connection-settings>) does not have the required read-write permissions for the particular custom field you are trying to delete. To verify:

  1. Log in to your [Zoho CRM](<https://www.zoho.com/crm/login.html>) account.
  2. Click **Setup** > **Modules and fields**.[![](/docs/images/reverse-etl-destinations/zoho-settings.webp)](</docs/images/reverse-etl-destinations/zoho-settings.webp>)
  3. Select the required module and click the **Fields** tab.
  4. Click **Field permissions**.
  5. Choose **Read and Write** for that particular field and click **Save**.