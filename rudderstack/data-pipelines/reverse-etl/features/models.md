# Models

Run custom SQL queries on your warehouse and send resulting data to the specified destinations.

* * *

  * __4 minute read

  * 


RudderStack’s **Models** feature lets you create models by defining custom SQL queries. You can then run these queries on your warehouse and send the resulting data to specific destinations. You can create as many models and reuse them with their corresponding [Reverse ETL sources](<https://www.rudderstack.com/docs/sources/reverse-etl/>).

With this feature, you can:

  * Build models with complex SQL queries using an intuitive UI.
  * Manage views of all models synced to different destinations in one place.
  * Reuse existing models in multiple connections.


## Create new model

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>).
  2. From the left navigation bar, go to **Activate** > **Models** and click **New model**.
  3. Configure the settings explained in the following sections:


### Select source

Select the warehouse source for which you want to create a model. RudderStack supports the Models feature for the following sources:

  * [Amazon Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/>)
  * [Google BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/>)
  * [PostgreSQL](<https://www.rudderstack.com/docs/sources/reverse-etl/postgresql/>)
  * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/>)
  * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/>)
  * [Trino](<https://www.rudderstack.com/docs/sources/reverse-etl/trino/>)


### Specify warehouse credentials

Specify the warehouse credentials to authenticate RudderStack. See the **Configure warehouse credentials** section of the [source-specific documentation](<https://www.rudderstack.com/docs/sources/reverse-etl/#supported-reverse-etl-sources>) (for example, [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#configuring-the-connection-credentials>)) for more details.

> ![info](/docs/images/info.svg)
> 
> Once you select or add your warehouse credentials and click **Next** , RudderStack will validate them before you can proceed with the setup. See FAQ for more information on these validations.

### Specify model name

  * Assign a name to uniquely identify the source in the RudderStack dashboard.
  * Select the source type to **Model** and click **Continue**.


### Configure model

  1. Enter an optional model description.
  2. Specify the custom SQL query in **Query** section.
  3. Click **Run Query** to fetch the data preview.
  4. Select the **Primary key** to use a column that uniquely identifies your warehouse records.


> ![warning](/docs/images/warning.svg)
> 
> You can set a primary key only after you run the SQL query successfully using the **Run Query** option.

[![Model configuration](/docs/images/data-pipelines/model-source-configuration.webp)](</docs/images/data-pipelines/model-source-configuration.webp>)

Note the following:

  * The **Preview** section displays the preview of the 50 resultant rows in a paginated format.
  * You can add single-line/multiline comments above the query. However, RudderStack supports only multiline comments at the end of the query. Support for single-line comments is coming soon.
  * You don’t need to add a semi-colon at the end of a query. RudderStack handles this automatically before running the query on the warehouse data.


### Review and complete setup

To make any changes to the warehouse credentials or audience configuration, click the edit icon present next to those sections.

[![Edit audience configuration](/docs/images/data-pipelines/edit-model-configuration.webp)](</docs/images/data-pipelines/edit-model-configuration.webp>)

Once you have reviewed your configuration, click **Create source** to complete the setup.

### Connect model to destination

To start using the newly-created source, you can connect it to:

  * A new [destination](<https://www.rudderstack.com/docs/destinations/overview/>), or
  * An existing destination that is **not already connected** to any other source.


To connect to a destination later, click **Done** on the top right:

[![Next steps](/docs/images/retl-sources/created-source.webp)](</docs/images/retl-sources/created-source.webp>)

You will then be redirected to the **Overview** page of the source where you will see the option of connecting it to a new or existing destination.

[![Add destination](/docs/images/retl-sources/add-destination.webp)](</docs/images/retl-sources/add-destination.webp>)

See [Set up Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) section for more information.

## Update model

  1. Go to the **Configuration** tab of the model source.
  2. To change the model description, click the edit icon in the **Configuration settings**.
  3. Click **Edit query** to change or update the model settings and primary key.


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You can set a primary key only after you run the updated SQL query successfully using the **Run Query** option.
>   * If you update the model’s query, you also need to check and update the relevant destination mappings in the **Schema** tab of the connection page.
>   * After updating the configuration, the next sync will be a full sync. To validate if the query is running fine, you can manually trigger a full sync.
> 


Go to the **Settings** tab to:

  * Get your source ID.
  * Change your warehouse credentials.
  * [Set up custom alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) for your Reverse ETL source.
  * Delete the source permanently.


> ![warning](/docs/images/warning.svg)
> 
> You cannot delete a source that is connected to any destination.

[![Edit source settings](/docs/images/retl-sources/source-settings.webp)](</docs/images/retl-sources/source-settings.webp>)

## FAQ

#### **What do the three validations under Verifying Credentials imply?**

Once you proceed after entering the connection credentials, you will see the following validations under the **Verifying Credentials** option:

[![Validating credentials](/docs/images/retl-sources/retl-credentials-validate.webp)](</docs/images/retl-sources/retl-credentials-validate.webp>)

These options are explained below:

  * **Verifying Connection** : Indicates that RudderStack is trying to connect to the warehouse with the information specified in the connection credentials.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, it means that one or more fields specified in the connection credentials are incorrect. Verify your credentials in this case.

  * **Able to List Schema** : Checks if RudderStack is able to fetch all schema details using the provided credentials.

  * **Able to Access RudderStack Schema** : Checks if RudderStack has the required access to the `_RUDDERSTACK` / `_rudderstack` schema (depending on your warehouse). To create the schema, run all commands listed in the **Permissions** section of the respective Reverse ETL source documentation:

    * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#granting-permissions>)
    * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/#granting-permissions>)
    * [PostgreSQL](<https://www.rudderstack.com/docs/sources/reverse-etl/postgresql/#granting-permissions>)
    * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#granting-permissions>)
    * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#granting-permissions>)
    * [Trino](<https://www.rudderstack.com/docs/sources/reverse-etl/trino/#granting-permissions>)


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, verify if you have successfully created the `_RUDDERSTACK` / `_rudderstack` schema and given RudderStack the required permissions to access it.