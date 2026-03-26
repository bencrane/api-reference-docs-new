# Databricks Delta Lake

Sync data from RudderStack to Databricks Delta Lake.

* * *

  * __16 minute read

  * 


[Delta Lake](<https://databricks.com/product/delta-lake-on-databricks>) is a popular data lake used for both streaming and batch operations. It lets you store structured, unstructured, and semi-structured data securely and reliably.

> ![success](/docs/images/tick.svg)
> 
> You can now use [Databricks Partner Connect](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/partner-connect/>) to set up your Databricks Delta Lake destination in RudderStack without following the setup instructions.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/deltalake>).

## Configuring Delta Lake destination in RudderStack

> ![warning](/docs/images/warning.svg)
> 
> Before configuring Delta Lake as a destination in RudderStack, it is highly recommended to go through the following sections to obtain the necessary configuration settings. These sections also contain the steps to grant RudderStack and Databricks the necessary permissions to your preferred storage bucket.
> 
>   * Granting RudderStack access to your storage bucket
>   * Granting Databricks access to your storage bucket
>   * Creating a new Databricks cluster
>   * Generating the Databricks access token
>   * Obtaining the JDBC/ODBC configuration
> 


To send event data to Delta Lake, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to Delta Lake via RudderStack.

To configure Delta Lake as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **Databricks Delta Lake** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **Host** : Enter your server hostname from the Databricks dashboard.
  * **Port** : Enter the port number.
  * **HTTP Path** : Enter the cluster’s HTTP path.


See Obtaining the JDBC/ODBC configuration for more information on obtaining the server hostname, port, and the cluster’s HTTP path.

  * **Use M2M OAuth** : Toggle on this setting to use [OAuth M2M](<https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m>) for authorizing access to Databricks resources. Then, provide the following credentials:

    * **Client ID** : The client ID for the service principal.
    * **Client Secret** : The corresponding client secret.


See the [Databricks documentation](<https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m#step-2-create-an-oauth-secret-for-a-service-principal>) for detailed steps on obtaining the **Client ID** and **Client Secret** fields.

  * **Personal Access Token** : You will see this field only if the **Use M2M OAuth** setting is toggled off. Use it to enter your Databricks access token. See Generating the Databricks access token for more information on generating the access token.


> ![warning](/docs/images/warning.svg)
> 
> Databricks [strongly recommends](<https://docs.databricks.com/aws/en/dev-tools/auth/#what-authorization-option-should-i-choose>) using OAuth over Personal Access Tokens for authorization.
> 
> OAuth tokens are automatically refreshed by default and do not require you to directly manage the access token, thereby improving your security against token hijacking and unauthorized access.

  * **Enable delta tables creation in an external location** : Enable this setting to specify the external location to create the delta tables. You can specify the external location in the **External delta table location** setting. When disabled, RudderStack creates the delta tables at a default storage location for the non-external Apache Hive tables.


> ![info](/docs/images/info.svg)
> 
> If you **have not** configured a [Unity catalog](<https://docs.databricks.com/data-governance/unity-catalog/index.html>), you can access the delta tables at `{path_to_table}/{schema}/{table}`.
> 
>   
> 
> 
> If you **have** configured a Unity catalog, follow these steps:
> 
>   1. Create an external location by following this [Databricks documentation](<https://docs.databricks.com/data-governance/unity-catalog/manage-external-locations-and-credentials.html#manage-external-locations>). Your location will look something like `s3://{bucket_path}/{external_location}`.
>   2. Specify the absolute location in the **External delta table location** setting. It will look something like `s3://{bucket_path}/{external_location}/{path_to_table}/{schema}/{table}`.
> 


  * **Catalog** : If you have configured a [Unity catalog](<https://docs.databricks.com/data-governance/unity-catalog/index.html>), enter the catalog name where your data assets are organized. For more information on creating a Unity Catalog, refer to the [Databricks documentation](<https://docs.databricks.com/data-governance/unity-catalog/create-catalogs.html>).


> ![info](/docs/images/info.svg)
> 
> If you do not specify the catalog name, RudderStack uses the default catalog configured for your workspace.

  * **Namespace** : Enter the the name of the schema where RudderStack will create the tables. If you don’t specify a namespace in the dashboard settings, RudderStack will set it to the source name, by default.

  * **Sync Frequency** : Specify how often RudderStack should sync the data to your Delta Lake instance.

  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the Delta Lake instance.

  * **Exclude Window** : This optional setting lets you specify the time window (in UTC) when RudderStack will **skip** the data sync.

  * **Object Storage Configuration** : Use this setting to specify your object storage.

    * **Use RudderStack managed object storage** : Enable this setting to use RudderStack-managed buckets for object storage. Note that this option is applicable only for RudderStack-hosted data planes. For self-hosted data planes, you need to specify your own object storage configuration settings.

    * **Choose your storage provider** : If **Use RudderStack managed object storage** is disabled, you can select any one of the following platforms for storing your staging files:

      * [Amazon S3 bucket storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#connection-settings>)
      * [Azure Blob Storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/#setting-up-azure-blob-storage>)
      * [Google Cloud Storage bucket settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/#setting-up-google-cloud-storage>)


See [How RudderStack stores data in an object storage platform](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/#how-does-rudderstack-store-data-in-an-object-storage-platform>) for more information.

> ![info](/docs/images/info.svg)
> 
> If you select S3 as your storage provider, RudderStack provides the option to specify your IAM role ARN or the AWS access key ID/secret access key by enabling the **Use STS Tokens to copy staging files** setting. For more information, refer to the Amazon S3 storage bucket settings section below.

  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.


### Advanced settings

  * **Warehouse Append** : This setting is turned on by default - RudderStack appends your incoming Event Stream data to the existing data in your warehouse. Turning it off causes RudderStack to merge your incoming data into your warehouse to ensure 100% non-duplicate data.


> ![info](/docs/images/info.svg)
> 
> The append operation helps to achieve faster data syncs while reducing warehouse costs. However, note that it may increase the number of duplicates in the warehouse, especially if the existing data is older than 7 days. A common scenario where duplication might occur is when the SDKs retry sending events in case of failures.
> 
> A merge strategy ensures deduplication but can lead to longer sync times and increased warehouse costs.

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.


## Granting RudderStack access to your storage bucket

This section contains the steps to edit your bucket policy to grant RudderStack the necessary permissions, depending on your preferred cloud platform.

### Amazon S3

Follow these steps to grant RudderStack access to your S3 bucket based on the following two cases:

#### Case 1: Use STS Token to copy staging files is disabled in the dashboard

> ![warning](/docs/images/warning.svg)
> 
> Follow the steps listed in this section if the **Use STS Token to copy staging files** option is disabled, that is, you **don’t want to specify** the AWS credentials while configuring your Delta Lake destination.

#### For RudderStack Cloud

If you are using RudderStack Cloud, edit your bucket policy using the following JSON:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::422074288268:user/s3-copy"
        },
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        "Resource": [
          "arn:aws:s3:::YOUR_BUCKET_NAME/*",
          "arn:aws:s3:::YOUR_BUCKET_NAME"
        ]
      }]
    }
    

> ![info](/docs/images/info.svg)
> 
> Make sure you replace `YOUR_BUCKET_NAME` with the name of your S3 bucket.

#### For self-hosted RudderStack

If you are [self-hosting RudderStack](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/>), follow these steps:

  1. Create an IAM policy with the following JSON:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": "*",
        "Resource": "arn:aws:s3:::*"
      }]
    }
    

  2. Then, create an [IAM user with programmatic access](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>). Attach the above IAM policy to this user.


> ![info](/docs/images/info.svg)
> 
> Copy the ARN of this newly-created user. This is required in the next step.

  3. Next, edit your bucket policy with the following JSON to allow RudderStack to write to your S3 bucket.


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": {
          "AWS": "arn:aws:iam::ACCOUNT_ID:user/USER_ARN"
        },
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        "Resource": [
          "arn:aws:s3:::YOUR_BUCKET_NAME/*",
          "arn:aws:s3:::YOUR_BUCKET_NAME"
        ]
      }]
    }
    

> ![info](/docs/images/info.svg)
> 
> Make sure you replace `USER_ARN` with the ARN copied in the previous step. Also, replace `ACCOUNT_ID` with your AWS account ID and `YOUR_BUCKET_NAME` with the name of your S3 bucket.

  4. Finally, add the programmatic access credentials to the `env` file present in your RudderStack installation:


    
    
    RUDDER_AWS_S3_COPY_USER_ACCESS_KEY_ID=<user_access_key>
    RUDDER_AWS_S3_COPY_USER_ACCESS_KEY=<user_access_key_secret>
    

#### Case 2: Use STS Token to copy staging files is enabled in the dashboard

In this case, provide the configuration directly while setting up the Delta Lake destination in RudderStack:

[![S3 settings in RudderStack dashboard](/docs/images/dw-integrations/delta-lake-connection-settings-3.webp)](</docs/images/dw-integrations/delta-lake-connection-settings-3.webp>)

  * **Role-based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack to write to your S3 bucket.

> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your intermediary S3 bucket. Refer to the [S3 permissions for warehouse destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#s3-permissions-for-warehouse-destinations>) section for more information.

### Google Cloud Storage

You can provide the necessary GCS bucket configuration while setting up the Delta Lake destination in RudderStack. For more information, refer to the [Google Cloud Storage bucket settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/#setting-up-google-cloud-storage>).

### Azure Blob Storage

You can provide the necessary Blob Storage container configuration while setting up the Delta Lake destination in RudderStack. For more information, refer to the [Azure Blob Storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/#setting-up-azure-blob-storage>).

## Granting Databricks access to your staging bucket

This section contains the steps to grant Databricks the necessary permissions to access your staging bucket, depending on your preferred cloud platform.

### Amazon S3

Follow these steps to grant Databricks access to your S3 bucket depending on your case:

#### Case 1: Use STS Token to copy staging files is disabled in the dashboard

> ![warning](/docs/images/warning.svg)
> 
> Follow the steps listed in this section if the **Use STS Token to copy staging files** option is disabled, i.e. you **don’t want to specify** the AWS access key and secret access key while configuring your Delta Lake destination.

In this case, you will be required to configure your AWS account to [create an instance profile](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html>) which will then be attached with your Databricks cluster.

Follow these steps in the exact order:

  1. [Create an instance profile to access the S3 bucket](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html#step-1-create-an-instance-profile-to-access-an-s3-bucket>).
  2. [Create a bucket policy for the target S3 bucket](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html#step-2-create-a-bucket-policy-for-the-target-s3-bucket>).
  3. [Note the IAM role used to create the Databricks deployment](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html#step-3-note-the-iam-role-used-to-create-the-databricks-deployment>).
  4. [Add the S3 IAM role to the EC2 policy](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html#step-4-add-the-s3-iam-role-to-the-ec2-policy>).
  5. [Add the instance profile to Databricks](<https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html#step-5-add-the-instance-profile-to-databricks>).


#### Case 2: Use STS Token to copy staging files is enabled in the dashboard

> ![info](/docs/images/info.svg)
> 
> Follow the steps listed in this section if the **Use STS Token to copy staging files** option is enabled, i.e. you are specifying the AWS access key and secret access key in the dashboard while configuring your Delta Lake destination.

Add the following Spark configuration to your Databricks cluster:
    
    
    spark.hadoop.fs.s3.impl shaded.databricks.org.apache.hadoop.fs.s3a.S3AFileSystem
    spark.hadoop.fs.s3a.impl shaded.databricks.org.apache.hadoop.fs.s3a.S3AFileSystem
    spark.hadoop.fs.s3n.impl shaded.databricks.org.apache.hadoop.fs.s3a.S3AFileSystem
    spark.hadoop.fs.s3.impl.disable.cache true
    spark.hadoop.fs.s3a.impl.disable.cache true
    spark.hadoop.fs.s3n.impl.disable.cache true
    

> ![info](/docs/images/info.svg)
> 
> For more information on adding custom Spark configuration properties in a Databricks cluster, refer to [Spark configuration guide](<https://docs.databricks.com/clusters/configure.html#spark-configuration>).

### Google Cloud Storage

To grant Databricks access to your GCS bucket, follow these steps:

  1. Follow the steps listed in this [user permissions](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/gcs-datalake/#setting-user-permissions-in-gcs-data-lake>) section to set up the required role and user permissions.
  2. Then, add the following Spark configuration to your Databricks cluster:


    
    
    spark.hadoop.fs.gs.auth.service.account.email <client_email>
    spark.hadoop.fs.gs.project.id <project_id>
    spark.hadoop.fs.gs.auth.service.account.private.key <private_key>
    spark.hadoop.fs.gs.auth.service.account.private.key.id <private_key_id>
    

> ![info](/docs/images/info.svg)
> 
> For more information on adding custom Spark configuration properties in a Databricks cluster, refer to [Spark configuration guide](<https://docs.databricks.com/clusters/configure.html#spark-configuration>).

  3. Finally, replace the following fields with the values obtained from the downloaded JSON in the previous step: `<project_id>`,`<private_key>`, `<private_key_id>`,`<client_email>`.


### Azure Blob Storage

To grant Databricks access to your Azure Blob Storage container, follow these steps:

  1. Add the following Spark configuration to your Databricks cluster.


    
    
    spark.hadoop.fs.azure.account.key.<storage-account-name>.blob.core.windows.net <storage-account-access-key>
    

> ![info](/docs/images/info.svg)
> 
> For more information on adding custom Spark configuration properties in a Databricks cluster, refer to [Spark configuration guide](<https://docs.databricks.com/clusters/configure.html#spark-configuration>).

  2. Replace the following fields with the relevant values from your Blob Storage account settings: `<storage-account-name>`,`<storage-account-access-key>`.


## Creating a new Databricks cluster

To create a new Databricks cluster, follow these steps:

  1. Sign into your Databricks account. Then, click the **Compute** option on the dashboard:

[![Delta Lake Compute option](/docs/images/dw-integrations/delta-lake-1.webp)](</docs/images/dw-integrations/delta-lake-1.webp>)

  2. Click the **Create Cluster** option.
  3. Next, enter the cluster details. Fill in the **Cluster Name** :

[![Delta Lake Cluster name](/docs/images/dw-integrations/delta-lake-2.webp)](</docs/images/dw-integrations/delta-lake-2.webp>)

  4. Select the **Cluster Mode** depending on your use-case. The following image highlights the three cluster modes:

[![Delta Lake cluster modes](/docs/images/dw-integrations/delta-lake-3.webp)](</docs/images/dw-integrations/delta-lake-3.webp>)

  5. Then, select the **Databricks Runtime Version** as **7.1** or higher:

[![Delta Lake runtime version](/docs/images/dw-integrations/delta-lake-4.webp)](</docs/images/dw-integrations/delta-lake-4.webp>)

  6. Configure the rest of the settings as per your requirement.
  7. In the **Advanced Options** section, configure the **Instances** field as shown in the following image:

[![Delta Lake instances](/docs/images/dw-integrations/delta-lake-5.webp)](</docs/images/dw-integrations/delta-lake-5.webp>)

  8. In the **Instance Profile** dropdown menu, select the Databricks instance profile that you added to your account in the previous step.

[![Delta Lake instances field](/docs/images/dw-integrations/delta-lake-6.webp)](</docs/images/dw-integrations/delta-lake-6.webp>)

  9. Finally, click the **Create Cluster** button to complete the configuration and create the Databricks cluster.

[![Delta Lake create cluster option](/docs/images/dw-integrations/delta-lake-7.webp)](</docs/images/dw-integrations/delta-lake-7.webp>)

## Obtaining the JDBC/ODBC configuration

Follow these steps to get the JDBC/ODBC configuration:

  1. In your Databricks dashboard, click the **Compute** option:

[![Delta Lake Compute option](/docs/images/dw-integrations/delta-lake-1.webp)](</docs/images/dw-integrations/delta-lake-1.webp>)

  2. Then, select the cluster you created in the previous section.

[![Delta Lake cluster](/docs/images/dw-integrations/delta-lake-8.webp)](</docs/images/dw-integrations/delta-lake-8.webp>)

  3. In the **Advanced Options** section, select the **JDBC/ODBC** field and copy the **Server Hostname** , **Port** , and **HTTP Path** values:

[![Delta Lake JDBC/ODBC settings](/docs/images/dw-integrations/delta-lake-9.webp)](</docs/images/dw-integrations/delta-lake-9.webp>)

> ![info](/docs/images/info.svg)
> 
> The **Server Hostname** , **Port** , and **HTTP Path** values are required to configure Delta Lake as a destination in RudderStack.

## Generating the Databricks access token

To generate the Databricks access token, follow these steps:

  1. In your Databricks dashboard, go to **Settings** and click **User Settings** :

[![Databricks user settings](/docs/images/dw-integrations/delta-lake-10.webp)](</docs/images/dw-integrations/delta-lake-10.webp>)

  2. Then, go to the **Access Tokens** section and click **Generate New Token** :

[![Access tokens](/docs/images/dw-integrations/delta-lake-11.webp)](</docs/images/dw-integrations/delta-lake-11.webp>)

  3. Enter your comment in the **Comment** field and click **Generate** :

[![Databricks generating new token](/docs/images/dw-integrations/delta-lake-12.webp)](</docs/images/dw-integrations/delta-lake-12.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Keep the **Lifetime (days)** field blank. If you enter a number, your access token will expire after that number of days.

  4. Finally, copy the access token as it will be used during the Delta Lake destination setup in RudderStack.


## IPs to be allowlisted

To enable network access to RudderStack, allowlist the following RudderStack IPs depending on your region and [RudderStack plan](<https://www.rudderstack.com/pricing>):

Plan| Region  
---|---  
| **US**| **EU**  
Free, Starter, and Growth| 

  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 52.38.160.231
  * 54.147.40.62

| 

  * 3.123.104.182
  * 3.125.132.33
  * 18.198.90.215
  * 18.196.167.201

  
Enterprise| 

  * 3.216.35.97
  * 34.198.90.241
  * 44.236.60.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.66.99.198
  * 3.64.201.167
  * 3.123.104.182
  * 3.125.132.33

  
  
> ![info](/docs/images/info.svg)
> 
> All the outbound traffic is routed through these RudderStack IPs.

## Supported file formats

RudderStack writes data in the [Parquet](<https://www.databricks.com/glossary/what-is-parquet>) format.

## Troubleshooting

This section contains the troubleshooting tips for various issues that you might encounter while setting up or using the Delta Lake destination.

#### Credential validation

  1. You get the below error in the **Verifying Load Table** stage:


    
    
    load test table: loading test table: databricks: execution error: failed to execute query:
    unexpected operation state 
    ERROR_STATE: shaded.databricks.org.apache.hadoop.fs.azure.AzureException: 
    Unable to access container rsprofiles in account dcianalytics.blob.core.windows.net 
    using anonymous credentials, and no credentials found for them in the configuration.
    

**Solution** : Make sure that Databricks has access to your Azure storage container.

  2. You get the below error in the **Verifying Load Table** stage:


    
    
    load test table: loading test table: databricks: execution error: failed to execute query: 
    unexpected operation state 
    ERROR_STATE: [CAST_INVALID_INPUT] 
    The value '_c0' of the type "STRING" cannot be cast to "BIGINT" because it is malformed. 
    Correct the value as per the syntax, or change its target type. 
    Use 'try_cast' to tolerated the malformed input and return NULL instead.
    

**Solution** :

  * If using a cluster, remove the `spark.sql.ansi.enabled` Spark configuration.

[![Databricks Spark configuration](/docs/images/dw-integrations/delta-lake/delta-lake-spark-config.webp)](</docs/images/dw-integrations/delta-lake/delta-lake-spark-config.webp>)

  * If using a SQL warehouse, remove the `ANSI_MODE` Spark configuration from **SQL Configuration Parameters** or set it to `false`.

[![Databricks SQL configuration settings](/docs/images/dw-integrations/delta-lake/delta-lake-sql-config.webp)](</docs/images/dw-integrations/delta-lake/delta-lake-sql-config.webp>)

See the [Databricks documentation](<https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-conf-mgmt-set#databricks-sql-examples>) for more information.

## FAQ

#### How does RudderStack handle deduplication in Databricks?

RudderStack takes the staging table and runs `MERGE` queries against the target Databricks tables to ensure no duplicate data is sent.

#### What are the reserved keys for Delta Lake?

Refer to this [documentation](<https://docs.microsoft.com/bs-cyrl-ba/azure/databricks/sql/language-manual/sql-ref-reserved-words>) for a complete list of the reserved keywords.

#### Does the Databricks cluster attached to the destination need to be up all time?

No, your Databricks cluster attached to the destination need not be up all time.

#### What happens if the cluster or the destination service is down? Is there a possibility of data loss?

If a warehouse destination is down or unavailable, RudderStack will continue to retry sending events (on an exponential backoff basis, for up to 3 hours).

RudderStack stores the syncs as staging files and retries sending them at a later time when the cluster is up again. This allows for a successful delivery without any missing data.

After retrying for up to 3 hours, RudderStack marks the syncs as aborted. Once the service is up and running again, you can go to the [Syncs](<https://www.rudderstack.com/docs/dashboard-guides/overview/#syncs>) tab in the RudderStack dashboard and retry sending the data.

#### Does RudderStack automatically spin the Databricks cluster/SQL endpoint every time it needs to write?

No, RudderStack does not spin the Databricks cluster or the SQL endpoint on its own every time it needs to write to the cluster.

Databricks itself starts up the cluster/endpoint when the connection is established. You just need to configure the [automatic termination](<https://docs.databricks.com/clusters/clusters-manage.html#automatic-termination-1>) settings in the **Autopilot Options** on the cluster creation page:

[![Databricks autopilot options](/docs/images/dw-integrations/databricks-autopilot-options.webp)](</docs/images/dw-integrations/databricks-autopilot-options.webp>)

#### How does RudderStack handle the reserved words in a column, table, or schema?

There are some limitations when it comes to using reserved words as a schema, table, or column name. If such words are used in event names, traits or properties, they will be prefixed with a `_` when RudderStack creates tables or columns for them in your schema.

Also, integers are **not** allowed at the start of a schema or table name. Hence, such schema, column, or table names will be prefixed with a `_`. For example, `'25dollarpurchase'` will be changed to `'_25dollarpurchase'`.

#### How can I modify an existing table to a partitioned table?

To modify an existing table to a partitioned table, follow these steps:

  1. Set an exclusion window (using the **Exclude window** connection setting) so that RudderStack does not process any data while performing the below changes.
  2. Make the required changes in connection settings of the configured Delta Lake destination.
  3. Run the following queries in the Databricks Cluster/SQL endpoints to:
     * Rename the existing table with `_temp` suffix.
     * Add `event_date` column to the `_temp` table.
     * Backfill the data into original table.


    
    
    ALTER TABLE x RENAME TO x_temp;
    ALTER TABLE x_temp ADD COLUMN TO event_date DATE;
    INSERT INTO x SELECT * FROM x_temp;
    

> ![info](/docs/images/info.svg)
> 
> RudderStack will create the new tables with partition support. Refer to the [Databricks documentation on partitions](<https://docs.databricks.com/sql/language-manual/sql-ref-partition.html>) for more information.

#### How can I convert an existing managed or unmanaged table at a location to an unmanaged table at a new location?

  1. Set an exclusion window (using the **Exclude window** connection setting) so that RudderStack does not process any data while performing the below changes.
  2. Run the following queries in the Databricks Cluster/SQL endpoints to:
     * Create a temporary table using the new location.
     * Drop the temporary table.
     * Drop the original table.


    
    
    CREATE OR REPLACE TABLE namespace.x_temp DEEP CLONE namespace.x LOCATION '/path/to/new/location/namespace/x';
    // where namespace represents the namespace attached to the destination in RudderStack.
    // where x represents the original table created by RudderStack.
    
    DROP TABLE namespace.x_temp;
    DROP TABLE namespace.x;
    

  3. Enable the **Enable delta tables creation in an external location** setting in RudderStack dashboard and update the location.
  4. Remove the exclusion window and make the required changes in connection settings of the configured Delta Lake destination.


RudderStack will create the table again during the subsequent data syncs.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Databricks documentation on managed and unmanaged tables](<https://docs.databricks.com/data/tables.html#managed-and-unmanaged-tables>) for more information.

#### How do I convert an existing unmanaged table at a specific location to a managed table (at default location)?

  1. Set an exclusion window (using the **Exclude window** connection setting) so that RudderStack does not process anything while performing the below changes.
  2. Run the following queries in the Databricks Cluster/SQL Endpoints to:
     * Create a temporary table.
     * Drop original table.
     * Rename temporary table to original table.


    
    
    CREATE TABLE IF NOT EXISTS namespace.x_temp DEEP CLONE namespace.x;
    // where namespace represents the namespace attached to the destination in RudderStack.
    // where x represents the original table created by RudderStack.
    
    DROP TABLE namespace.x;
    ALTER TABLE namespace.x_temp RENAME TO namespace.x;
    

  3. Remove the exclusion window and make sure the **Enable delta tables creation in an external location** setting is disabled in the RudderStack dashboard.


RudderStack will create the table again during the subsequent data syncs.

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.