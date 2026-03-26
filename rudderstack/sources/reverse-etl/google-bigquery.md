# Google BigQuery Reverse ETL Source

Send data from Google BigQuery to your entire stack.

* * *

  * __8 minute read

  * 


[Google BigQuery](<https://cloud.google.com/bigquery>) is an industry-leading, fully-managed cloud data warehouse that lets you store and analyze petabytes of data in no time.

RudderStack supports Google BigQuery as a source from which you can ingest data and route it to your desired downstream destinations.

## Grant permissions

Before you set up BigQuery as a source, you must grant certain permissions on your BigQuery warehouse for RudderStack to access data from it.

Follow the steps below in the **exact order** to grant these permissions:

### Step 1: Create role and grant permissions

  1. Go to the [Roles](<https://console.cloud.google.com/iam-admin/roles>) section of Google Cloud Platform dashboard and click **CREATE ROLE**.

[![Google Cloud Platform dashboard create role](/docs/images/warehouse-actions-sources/GCP-create-role.webp)](</docs/images/warehouse-actions-sources/GCP-create-role.webp>)

  2. Fill in the details as shown:

[![GCP role details](/docs/images/warehouse-actions-sources/gcp-role-details.webp)](</docs/images/warehouse-actions-sources/gcp-role-details.webp>)

  3. Click **ADD PERMISSIONS** and add the following permissions individually:


**Read-only:**
    
    
    bigquery.datasets.get
    bigquery.jobs.list
    bigquery.tables.get
    bigquery.tables.getData
    bigquery.tables.list
    bigquery.routines.get
    bigquery.routines.list
    bigquery.tables.delete
    

**Read-write:**
    
    
    bigquery.jobs.create
    bigquery.tables.create
    bigquery.tables.update
    bigquery.tables.updateData
    bigquery.tables.delete
    

  4. Click **CREATE** after adding the permissions.

[![BigQuery role permissions](/docs/images/warehouse-actions-sources/gcp-role-permisssions.webp)](</docs/images/warehouse-actions-sources/gcp-role-permisssions.webp>)

### Step 2: Create service account and attach role

  1. Go to [Service Accounts](<https://console.cloud.google.com/iam-admin/serviceaccounts>) and select the project which has the dataset or the table that you want to use.
  2. Click **CREATE SERVICE ACCOUNT**.

[![Create service account in GCP](/docs/images/warehouse-actions-sources/gcp-create-service-account.webp)](</docs/images/warehouse-actions-sources/gcp-create-service-account.webp>)

  3. Fill in the **Service Account details** as shown below, and click **CREATE AND CONTINUE** :

[![Service account role details](/docs/images/warehouse-actions-sources/gcp-service-account-details.webp)](</docs/images/warehouse-actions-sources/gcp-service-account-details.webp>)

  4. Under **Grant this service account access to project** , select the role you created in Step 1: Creating a role and granting permissions section above.

[![Service account role connection](/docs/images/warehouse-actions-sources/gcp-service-account-connect-role.webp)](</docs/images/warehouse-actions-sources/gcp-service-account-connect-role.webp>)

  5. Click **DONE** to move to the list of service accounts.


> ![info](/docs/images/info.svg)
> 
> Note down the service account ID. You will need this ID while creating the RudderStack schema and granting the required permissions to it.
> 
> ![Service account ID](/docs/images/warehouse-actions-sources/gcp-service-account-id.webp)

### Step 3: Create and download JSON key

  1. Click the three dots icon under **Actions** in the service account that you just created and select **Manage keys** :

[![Managing keys in GCP](/docs/images/warehouse-actions-sources/manage-keys.webp)](</docs/images/warehouse-actions-sources/manage-keys.webp>)

  2. Click **ADD KEY** , followed by **Create new key** :

[![GCP Adding a new key](/docs/images/warehouse-actions-sources/gcp-add-key.webp)](</docs/images/warehouse-actions-sources/gcp-add-key.webp>)

  3. Select **JSON** and click **CREATE**.

[![Select Reverse ETL source in RudderStack](/docs/images/warehouse-actions-sources/create-new-key.webp)](</docs/images/warehouse-actions-sources/create-new-key.webp>)

A JSON file will be downloaded on your system. This file is required while setting up the BigQuery source in RudderStack.

### Step 4: Create RudderStack schema and granting permissions

  1. From your [BigQuery SQL workspace](<https://console.cloud.google.com/bigquery>), run the following command to create a dedicated schema `rudderstack_`.


> ![danger](/docs/images/danger.svg)
> 
> The `rudderstack_` schema is used by RudderStack for storing the state of each data sync. **Do not change this name**.
    
    
    create schema rudderstack_;
    

> ![warning](/docs/images/warning.svg)
> 
> The `rudderstack_` schema is created in the default region of your BigQuery instance.
> 
> If the GCP cloud storage bucket used as a staging bucket by RudderStack is in a different region, you will need to adjust the above SQL statement to match that region. For example, to create the schema in the [`europe-west-3`](<https://cloud.google.com/bigquery/docs/locations>) region, run the following statement:  
> 
>     
>     
>     create schema rudderstack_ OPTIONS (location = "europe-west3");
>     

  2. Grant full access to the `rudderstack_` schema for the RudderStack service account you created above. Replace `<SERVICE_ACCOUNT_ID>` with the service account ID you specified in Step 2: Creating a service account and attaching role to it.


> ![info](/docs/images/info.svg)
> 
> The `<SERVICE_ACCOUNT_ID>` takes the form of `name@your-gcp-project.iam.gserviceaccount.com`. You can also find it in the `client_email` key of the service account credentials JSON file downloaded in Step 3: Creating and downloading the JSON key.
    
    
    GRANT `roles/bigquery.dataOwner`
         ON SCHEMA rudderstack_
         TO "serviceAccount:<SERVICE_ACCOUNT_ID>";
    

## Set up BigQuery source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **BigQuery**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Credentials** : Add the contents of the GCP service account credentials JSON downloaded above.
  * **Project ID** : Specify your GCP project ID where your BigQuery database is located.
  * **Service account** : Specify your GCP service account in this field.


Click the **Verify** button on the top right. RudderStack will then verify and validate your credentials. Once verified, click **Continue** to proceed.

### Specify name and source type

Specify the source name and type in this step.

  * **Source name** : Assign a name to uniquely identify the source in the RudderStack dashboard.
  * **Select your source type** : RudderStack lets you set up a Reverse ETL source from a warehouse **Table** , **Model** , or **Audience**.

Source type| Description  
---|---  
Table| Use an existing warehouse table as a data source.  
  
See Use warehouse table as source for detailed setup.  
Model| Use custom SQL queries to fetch specific warehouse data and send them to your destinations.  
  
See Use model as source for detailed setup.  
Audience| Filter data in your warehouse tables to create target customer lists and send them to downstream destinations.  
  
See Use audience as source for detailed setup.  
  
#### **Use warehouse table as source**

Under **Select your source type** , choose **Table** and specify the below fields:

  * **Schema** : Select the warehouse schema from the dropdown.
  * **Table** : Choose the required table from which RudderStack syncs the data.
  * **Primary key** : Select the column from the above table that uniquely identifies your records in the warehouse.


> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` by creating a view on your warehouse table.

[![Use table as source](/docs/images/retl-sources/wh-table-source.webp)](</docs/images/retl-sources/wh-table-source.webp>)

Finally, review and complete your source setup.

#### **Use model as source**

Under **Select your source type** , choose **Model** and click **Continue**.

To configure a model as source:

  1. Enter an optional description and specify the custom SQL query in **Query** section.
  2. Click **Run Query** to fetch the data preview.
  3. Select the **Primary key** to use a column that uniquely identifies your warehouse records.


> ![warning](/docs/images/warning.svg)
> 
> You can set a primary key only after you run the SQL query successfully using the **Run Query** option.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` in SQL query of the model.

[![Model configuration](/docs/images/data-pipelines/model-source-configuration.webp)](</docs/images/data-pipelines/model-source-configuration.webp>)

Finally, review and complete your source setup.

#### **Use audience as source**

Under **Select your source type** , choose **Audience** and follow these steps:

  1. Configure your audience source by specifying the below fields:

     * **Schema** : Select the warehouse schema from the dropdown.
     * **Table** : Choose the required table from which RudderStack syncs the data.
     * **Primary key** : Select the column from the above table that uniquely identify your records in the warehouse.

[![Use audience as source](/docs/images/retl-sources/audience-source.webp)](</docs/images/retl-sources/audience-source.webp>)

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` by creating a view on your warehouse table.

  2. Set your [audience conditions](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/#set-your-conditions>).
  3. Click **Preview** to see the resulting data. Then, click **Continue** to proceed.

[![Audience configuration](/docs/images/retl-sources/audience-source-configuration.webp)](</docs/images/retl-sources/audience-source-configuration.webp>)

Finally, review and complete your source setup.

### Review and complete setup

To make any changes to the warehouse credentials or source configuration, click the edit icon present next to those sections.

[![Edit source configuration](/docs/images/retl-sources/edit-source-configuration.webp)](</docs/images/retl-sources/edit-source-configuration.webp>)

Review your configuration and click **Create source** to complete the setup.

## Connect destination

To start using the newly-created source, you can connect it to:

  * A new [destination](<https://www.rudderstack.com/docs/destinations/overview/>), or
  * An existing destination that is **not already connected** to any other source.


To connect to a destination later, click **Done** on the top right:

[![Next steps](/docs/images/retl-sources/created-source.webp)](</docs/images/retl-sources/created-source.webp>)

You will then be redirected to the **Overview** page of the source where you will see the option of connecting it to a new or existing destination.

[![Add destination](/docs/images/retl-sources/add-destination.webp)](</docs/images/retl-sources/add-destination.webp>)

See [Set up Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) section for more information.

## Update source configuration and settings

Go to the **Configuration** tab of your Reverse ETL source to update the configuration depending on your source type:

> ![warning](/docs/images/warning.svg)
> 
> You cannot change the source type on this page.

[![Update source configuration](/docs/images/retl-sources/update-source-configuration.webp)](</docs/images/retl-sources/update-source-configuration.webp>)

The below table lists the options you can update:

Source type| Configurable options  
---|---  
Table| Schema, Table, Primary key  
Model| 

  * Model settings
  * Primary key

**Note** : You can set the primary key only after the SQL query runs successfully.  
Audience| 

  * Schema, Table, Primary key
  * Audience conditions

  
  
> ![info](/docs/images/info.svg)
> 
> After updating the configuration, the next sync will be a full sync.

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

When setting up a Reverse ETL source, you will see the following three validations under the **Verifying Credentials** option once you proceed after entering the warehouse credentials:

[![Validating credentials](/docs/images/retl-sources/retl-credentials-validate.webp)](</docs/images/retl-sources/retl-credentials-validate.webp>)

These options are explained below:

  * **Verifying Connection** : This option indicates that RudderStack is trying to connect to the warehouse with the provided warehouse credentials.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, it means that one or more fields specified in the warehouse credentials are incorrect. Verify your credentials in this case.

  * **Able to List Schema** : This option checks if RudderStack is able to fetch all schema details by using the provided credentials.
  * **Able to Access RudderStack Schema** : This option implies that RudderStack is able to access the `_rudderstack` schema you have created by running all commands in the User Permissions section.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, verify if you have successfully created the `_rudderstack` schema and given RudderStack the required permissions to access it.

#### **What is the difference between the Table, Model, and Audience options when creating a Reverse ETL source?**

When creating a new Reverse ETL source, you are presented with the following options from which RudderStack syncs the data:

Source type| Description  
---|---  
Table| RudderStack uses an existing warehouse table as a data source.  
  
See Use warehouse table as source for detailed setup.  
Model| RudderStack uses custom SQL queries to fetch specific warehouse data and sends them to your destinations.  
  
See Use model as source for detailed setup.  
Audience| RudderStack filters data in your warehouse tables to create target customer lists and sends them to downstream destinations.  
  
See Use audience as source for detailed setup.