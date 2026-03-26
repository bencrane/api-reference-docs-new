# Amazon Redshift Reverse ETL Source

Send data from Amazon Redshift to your entire stack.

* * *

  * __9 minute read

  * 


[Amazon Redshift](<https://aws.amazon.com/redshift/>) is one of the fastest cloud data warehouse services. It lets you handle large analytical workloads with best-in-class performance, speed, and efficiency.

RudderStack supports Amazon Redshift as a data source from which you can ingest data and route it to your desired downstream destinations.

## Grant permissions

Before you set up Redshift as a source, you must grant certain permissions on your Redshift warehouse for RudderStack to access data from it.

Run the queries listed in the following sections in the **exact order** to grant the required permissions:

### Step 1: Create new user in Redshift

  1. Create a new user `rudder` with a password `<strong_unique_password>`.


    
    
    CREATE USER rudder WITH PASSWORD '<strong_unique_password>'
    

The password set in the above command must meet the following conditions:

  * It should be **8-64** characters in length.
  * It must contain at least one upper case, one lower case, and one number.
  * It can contain any ASCII characters with the ASCII codes 33-126, with the exception of `'` (single quotation mark), `"` (double quotation mark), `\`, `/`, and `@`.


See the [Amazon Redshift documentation](<https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html#r_CREATE_USER-parameters>) for more information on the password rules.

### Step 2: Create RudderStack schema and grant permissions

  1. Create a dedicated schema `_rudderstack`.


    
    
    CREATE SCHEMA "_rudderstack";
    

> ![warning](/docs/images/warning.svg)
> 
> The `_rudderstack` schema is used by RudderStack for storing the state of each data sync. **Do not change this name**.

  2. Grant full access to schema `_rudderstack` for the user `rudder`.


    
    
    GRANT ALL ON SCHEMA "_rudderstack" TO rudder;
    

  3. Grant full access to the user `rudder` over all `_rudderstack` schema objects.


    
    
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "_rudderstack" TO rudder;
    

### Step 3: Grant permissions on schema and table

  1. Grant access to the user `rudder` to look up the objects within your schema:


    
    
    GRANT USAGE ON SCHEMA "<YOUR_SCHEMA>" TO rudder;
    

  2. Grant access to the user `rudder` to read data from the required table/view:


    
    
    GRANT SELECT ON TABLE "<YOUR_SCHEMA>"."<YOUR_TABLE>" TO rudder;
    

Replace `<YOUR_SCHEMA>` and `<YOUR_TABLE>` with the exact names of your Redshift schema and table respectively.

#### **Optional commands**

  * The following command grants access to the user `rudder` to view and read data from **all** the tables present in the schema `<YOUR_SCHEMA>`:


    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "<YOUR_SCHEMA>" TO rudder;
    

> ![warning](/docs/images/warning.svg)
> 
> Run this command only if you’re okay with RudderStack being able to access the data in all tables residing within your specified schema.

  * The following command grants access to the user `rudder` to read data from all future tables created by the user `creator` in your schema:


    
    
    ALTER DEFAULT PRIVILEGES for user creator IN SCHEMA "<YOUR_SCHEMA>" GRANT SELECT ON TABLES TO rudder;
    

> ![warning](/docs/images/warning.svg)
> 
> Run this command only if you’re okay with RudderStack being able to access the data in all future tables residing within your specified schema.

Replace `<YOUR_SCHEMA>` with the exact name of your Redshift schema.

## Set up Redshift source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **Redshift**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Host** : Enter the host name of your Redshift service.
  * **Port** : Enter the port number associated with the Redshift database instance.
  * **Database** : Enter the database name of your Redshift instance from where RudderStack ingests the data.
  * **User** : Enter the name of the Redshift user created while granting permissions.
  * **Authentication Type** : Select the authentication mechanism from the dropdown. RudderStack provides the below authentication mechanisms:
    * **IAM** (recommended): Lets you use the RudderStack IAM role for authentication. For more information on creating a RudderStack IAM role for Redshift, see [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/redshift-iam-role/>).
    * **Username Password Authentication** : Lets you use the username and password for authenticating to Redshift.


You will see the following settings depending on the authentication type you select:

  * **Cluster identifier** : Enter your AWS cluster ID.
  * **Cluster region** : Enter your AWS cluster region.


  * **Password** : Enter the password for the user specified in the **User** field above.


Then, continue with the setup by specifying the below setting:

  * **SSL Mode** : Select the SSL mode as **disable** or **require** depending on how RudderStack should connect to your Redshift instance.


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

#### What are the SSL mode options when setting up the Redshift source in RudderStack?

When setting up a Redshift source, RudderStack provides the following two SSL options:

  * **disable** : SSL mode is disabled when you select this option. Use it in cases where security is not an issue and you don’t want any encryption overhead.
  * **require** : When you select this option, your data is encrypted and sent to RudderStack. Use it in cases where security is important and you can deal with the resulting encryption overhead.


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