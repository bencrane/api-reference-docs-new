# Snowflake Destination

Sync data from RudderStack to Snowflake.

* * *

  * __15 minute read

  * 


[Snowflake](<https://www.snowflake.com/>) is a popular cloud-based data warehouse known for its speed, scalability, and reliability.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for how events are mapped to Snowflake tables.

Find the open source code for this destination in the [GitHub](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/snowflake>) repository.

## Setting user permissions in Snowflake

To enable RudderStack access, make sure you have `ACCOUNTADMIN` or an account that has the `MANAGE GRANTS` privilege.

The following sections illustrate how to set up a virtual warehouse, a database, a role, and an user in Snowflake:

### Creating a virtual warehouse

In your Snowflake console, create a `X-Small` warehouse:

[![Create a virtual warehouse](/docs/images/dw-integrations/snowflake-create-warehouse.webp)](</docs/images/dw-integrations/snowflake-create-warehouse.webp>)

> ![info](/docs/images/info.svg)
> 
> Set your data warehouse size as per your data volume requirements.

Alternatively, create a new warehouse by running the following SQL commands:
    
    
    CREATE WAREHOUSE RUDDER_WAREHOUSE
      WITH WAREHOUSE_SIZE = 'XSMALL'
        WAREHOUSE_TYPE = 'STANDARD'
        AUTO_SUSPEND = 600
        AUTO_RESUME = TRUE;
    

> ![info](/docs/images/info.svg)
> 
> Set `AUTO_SUSPEND` to ~10 mins and enable `AUTO_RESUME` to avoid any extra costs.

### Creating a database

> ![warning](/docs/images/warning.svg)
> 
> Create a new database to avoid conflicts with your existing data. RudderStack creates its own tables while storing your events.

The following image demonstrates the **Create Database** option in Snowflake.

[![Create a database](/docs/images/dw-integrations/snowflake-create-database.webp)](</docs/images/dw-integrations/snowflake-create-database.webp>)

Alternatively, you can create a new database by running the following SQL command:
    
    
    CREATE DATABASE RUDDER_EVENTS;
    

### Creating a role for RudderStack

Run the following SQL commands to create a new role with the required permissions to load your data into the newly created warehouse:

  1. Create a new role called `RUDDER`:


    
    
    CREATE ROLE RUDDER;
    

  2. Grant access to the warehouse `RUDDER_WAREHOUSE`:


    
    
    GRANT USAGE ON WAREHOUSE RUDDER_WAREHOUSE TO ROLE RUDDER;
    

  3. Grant access to the database `RUDDER_EVENTS`:


    
    
    GRANT USAGE ON DATABASE RUDDER_EVENTS TO ROLE RUDDER;
    GRANT CREATE SCHEMA ON DATABASE RUDDER_EVENTS TO ROLE RUDDER;
    GRANT ALL ON ALL SCHEMAS IN DATABASE RUDDER_EVENTS TO ROLE RUDDER;
    

> ![info](/docs/images/info.svg)
> 
> Alternatively, you can also create up a custom role and specify it in the dashboard settings while setting up the Snowflake destination in RudderStack. Note that this role must have the necessary permissions for RudderStack to load the data into your warehouse.

### Creating a user

Finally, create a user to connect RudderStack to the newly created warehouse using the following SQL query:
    
    
    CREATE USER RUDDER_USER
      MUST_CHANGE_PASSWORD = FALSE
      DEFAULT_ROLE = RUDDER
      PASSWORD = "<your_password>";
    GRANT ROLE RUDDER TO USER RUDDER_USER;
    

## Configuring Snowflake destination in RudderStack

To start sending data to Snowflake, you first need to add it as a destination in RudderStack and connect it to a data source. Follow these steps to configure Snowflake as a destination in RudderStack:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), configure the data source. Then, select **Snowflake** from the list of destinations.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

  * **Account** : Enter the account ID of your Snowflake warehouse. This account ID is part of the Snowflake URL.


The following examples illustrate the slight differences in the account ID for various cloud providers:

Account ID example| Corresponding Snowflake URL| Snowflake cloud provider  
---|---|---  
`qya56091.us-east-1`  
  
`qya56091.us-east-2.aws`| `https://`**`qya56091.us-east-1`**`.snowflakecomputing.com`  
  
`https://`**`qya56091.us-east-2.aws`**`.snowflakecomputing.com`| AWS  
`rx18795.east-us-2.azure`| `https://`**`rx18795.east-us-2.azure`**`.snowflakecomputing.com`| Microsoft Azure  
`ah76025.us-central1.gcp`| `https://`**`ah76025.us-central1.gcp`**`.snowflakecomputing.com`| Google Cloud Platform  
  
> ![warning](/docs/images/warning.svg)
> 
> In case of AWS, `.aws` is present in the account locator of some region’s accounts and must be included in the **Account** field above.
> 
> For more information on account locator formats depending on your region or cloud provider, refer to the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#non-vps-account-locator-formats-by-cloud-platform-and-region>).

  * **Database** : Enter the name of the database created in the Creating a database section above.
  * **Warehouse** : Enter the name of the warehouse created in the Creating a virtual warehouse section above.
  * **User** : Enter the name of the user created in the Creating a user section above.
  * **Role** : Specify the role to be assigned to the above user. If not specified, RudderStack will use the default role.


> ![warning](/docs/images/warning.svg)
> 
> Make sure your role has the necessary permissions for RudderStack to load the data into the warehouse.

  * **Use Key Pair Authentication** : Turn on the toggle to authenticate the user via a [key pair](<https://docs.snowflake.com/en/user-guide/key-pair-auth>).


> ![info](/docs/images/info.svg)
> 
> For enhanced security, RudderStack recommends using the key pair authentication over the basic authentication mechanism (username and password).
> 
>   * See the [Migration Guide](<https://www.rudderstack.com/docs/user-guides/migration-guides/snowflake-key-pair-migration/>) to migrate from the username/password authentication to the key pair authentication.
> 
>   * Refer to the following sections in the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication>) to generate and use the key pair:
> 
>     * [Generate private key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key>)
>     * [Generate public key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-a-public-key>)
>     * [Assign public key to Snowflake user](<https://docs.snowflake.com/en/user-guide/key-pair-auth#assign-the-public-key-to-a-snowflake-user>)
> 


Then, enter the following settings:

  * **Private Key** : Specify the entire contents of the private key, including the delimiters (`BEGIN RSA PRIVATE KEY` and `END RSA PRIVATE KEY`).

  * **Private Key Passphrase** : If your private key is encrypted, specify the password used for encrypting the key. Note that:

    * RudderStack requires a non-empty passphrase for encrypted private keys.
    * Leave this field blank if your private key is not encrypted.


> ![danger](/docs/images/danger.svg)
> 
> The user authentication will fail if your private key is encrypted and you do not specify the passphrase.

  * **Password** : You will see this field only if the **Use Key Pair Authentication** setting is toggled off. Use it to enter the password for the user specified in the **User** setting above.
  * **Namespace** : Enter the schema name for the warehouse where RudderStack will create all tables. If not specified, RudderStack sets the namespace to the source name by default. Note that you **cannot** change the namespace later.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your Snowflake warehouse.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the warehouse.
  * **Exclude Window** : This optional setting lets you set a time window when RudderStack **will not** sync the data to the warehouse.


### Configuring the object storage

RudderStack lets you configure the following object storage settings during set up:

  * **Use RudderStack-managed Object Storage** : Enable this setting to use RudderStack-managed buckets for object storage.


> ![warning](/docs/images/warning.svg)
> 
> This option is applicable only for RudderStack-hosted data planes. For self-hosted data planes, you will have to specify your own object storage configuration settings.

  * **Choose your Cloud** : Select the cloud provider for your Snowflake instance. Refer to the following settings depending on your cloud provider:


  * **Staging S3 Storage Bucket Name** : Specify the name of your S3 bucket where RudderStack will store the data before loading it into Snowflake.
  * **Prefix** : If specified, RudderStack will create a folder in the bucket with this prefix and push all data within that folder.
  * **Storage Integration** : Use this setting to run the COPY command. Refer to the Configuring cloud storage integration with Snowflake section for details.
  * **Role Based Authentication** : Enable this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, refer to [this guide](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).
    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to enable this setting as the access keys-based authentication method is now deprecated.

If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack to write to your S3 bucket. Refer to these [S3 permissions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#permissions>).

  * **Enable Server-side Encryption for S3** : Toggle on this setting to enable server-side encryption for your S3 bucket.


  * **Staging Azure Blob Storage Container Name** : Specify the name of your Azure container where RudderStack will store the data before loading it into Snowflake.
  * **Prefix** : If specified, RudderStack will create a folder in the bucket with this prefix and push all data within that folder.
  * **Storage Integration** : Use this setting to run the COPY command. Refer to the Configuring cloud storage integration with Snowflake section for details.
  * **Azure Blob Storage Account Name** : Enter the account name for the Azure container.
  * **Azure Blob Storage Account Key** : Enter the account key for your Azure container. Refer to these [Blob Storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/#setting-up-azure-blob-storage>) section for more information.


  * **Staging GCS Object Storage Bucket Name** : Specify the name of your GCS bucket where RudderStack will store the data before loading it into Snowflake.
  * **Prefix** : If specified, RudderStack will create a folder in the bucket with this prefix and push all data within that folder.
  * **Storage Integration** : Use this setting to run the COPY command. Refer to the Configuring cloud storage integration with Snowflake section for details.
  * **Credentials** : Paste the contents of your GCP service account credentials JSON. The service account should have a role with `storage.objectCreator` access.


See [How RudderStack stores data in an object storage platform](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/#how-does-rudderstack-store-data-in-an-object-storage-platform>) for more information.

  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.


### Advanced settings

RudderStack provides the following advanced settings:

  * **Warehouse Append** : This setting is turned on by default - RudderStack appends your incoming Event Stream data to the existing data in your warehouse. Turning it off causes RudderStack to merge your incoming data into your warehouse to ensure 100% non-duplicate data.


> ![info](/docs/images/info.svg)
> 
> The append operation helps to achieve faster data syncs while reducing warehouse costs. However, note that it may increase the number of duplicates in the warehouse, especially if the existing data is older than 7 days. A common scenario where duplication might occur is when the SDKs retry sending events in case of failures.
> 
> A merge strategy ensures deduplication but can lead to longer sync times and increased warehouse costs.

  * **Skip Users Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.
  * **JSON Columns** : Lets you ingest semi-structured event data not defined by a fixed schema. You can specify the required JSON column paths in this setting in dot notation, separated by commas. **This option applies to all incoming`track` events for this destination**. See [JSON Column Support](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/json-column-support/>) for more information.


## Configuring cloud storage integration with Snowflake

Storage integration setting can be used to run the COPY command. This section lists the steps to configure the **Storage Integration** setting specified in the Configuring the object storage section above.

If you have Amazon Web Services (AWS) as your cloud provider and want to use S3 as your object storage, follow the steps below. You can find the detailed instructions in this [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/data-load-s3-config.html#option-1-configuring-a-snowflake-storage-integration>).

  1. **Create a policy in AWS** : In the following JSON, replace `<BUCKET_NAME>` and `<PREFIX>` with the name of your S3 bucket and the prefix set in the Configuring the object storage section above, and create the policy with a name of your choice.


    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "s3:PutObject",
            "s3:GetObject",
            "s3:GetObjectVersion",
            "s3:DeleteObject",
            "s3:DeleteObjectVersion"
          ],
          "Resource": "arn:aws:s3:::<BUCKET_NAME>/<PREFIX>/*"
        },
        {
          "Effect": "Allow",
          "Action": "s3:ListBucket",
          "Resource": "arn:aws:s3:::<BUCKET_NAME>",
          "Condition": {
            "StringLike": {
              "s3:prefix": ["<PREFIX>/*"]
            }
          }
        }
      ]
    }
    

  2. **Create a role and attach the above policy in AWS** : Follow the steps listed below:

     1. Create a role of type **Another AWS account**.
     2. Enter your AWS account ID and enable the **Require External ID** option.
     3. For external ID, you can add a placeholder value like `0000`. This can be modified later.
     4. Attach the policy created in **Step 1**. Assign a name to this role and keep the role ARN handy for the next step.
  3. **Create the cloud storage integration in Snowflake** : Replace `<INTEGRATION_NAME>` with the name of your choice (note this name for the later steps) and `<IAM_ROLE>` with the role ARN obtained in **Step 2** and run the following command:


    
    
    CREATE STORAGE INTEGRATION <INTEGRATION_NAME>
      TYPE = EXTERNAL_STAGE
      STORAGE_PROVIDER = S3
      ENABLED = TRUE
      STORAGE_AWS_ROLE_ARN = '<IAM_ROLE>'
      STORAGE_ALLOWED_LOCATIONS = ('s3://<BUCKET_NAME>/<PATH>/', 's3://<BUCKET_NAME>/<PATH>/')
      [ STORAGE_BLOCKED_LOCATIONS = ('s3://<BUCKET_NAME>/<PATH>/', 's3://<BUCKET_NAME>/<PATH>/') ]
    

  4. Retrieve the AWS IAM user for your Snowflake account as shown:


    
    
    DESC INTEGRATION <INTEGRATION_NAME>;
    

  5. Grant the IAM user permissions to access the bucket objects in S3. Choose the role you created in **Step 2** and edit the trust relationship as shown in the following JSON:


> ![warning](/docs/images/warning.svg)
> 
> Both statements included in the below JSON are **mandatory** — one is required for RudderStack ingestion and the other for Snowflake access.
    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::422074288268:root"
            ]
          },
          "Action": "sts:AssumeRole",
          "Condition": {
            "StringEquals": {
              "sts:ExternalId": "<WORKSPACE_ID>"
            }
          }
        },
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "<SNOWFLAKE_USER_ARN>"
            ]
          },
          "Action": "sts:AssumeRole",
          "Condition": {
            "StringEquals": {
              "sts:ExternalId": "<SNOWFLAKE_EXTERNAL_ID>"
            }
          }
        }
      ]
    }
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `<SNOWFLAKE_USER_ARN>` is the `STORAGE_AWS_IAM_USER_ARN` option seen in **Step 4**
>   * `<SNOWFLAKE_EXTERNAL_ID>` is the `STORAGE_AWS_EXTERNAL_ID`
>   * `<WORKSPACE_ID>` is your [RudderStack workspace ID](<https://www.rudderstack.com/docs/dashboard-guides/overview/#workspace>)
> 


  6. Grant integration access to the Snowflake role you created in the Creating a role for RudderStack section by running the following command:


    
    
    GRANT usage ON integration <INTEGRATION_NAME> TO ROLE RUDDER;
    

Here, `<INTEGRATION_NAME>` is the name of the integration created in **Step 3**.

  7. Set the **Storage Integration** dashboard setting to `<INTEGRATION_NAME`>.


While sending the data to Snowflake, RudderStack uses an external location instead of a stage in its queries. Hence, the following command listed in the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration.html#step-6-create-an-external-stage>) is **not required** :
    
    
    GRANT CREATE STAGE ON SCHEMA PUBLIC public to role myrole;
    

To leverage Azure Blob Storage as your object storage, follow the instructions below. You can find the detailed instructions in this [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/data-load-azure-config.html#option-1-configuring-a-snowflake-storage-integration>).

  1. **Create a storage account and container in Azure** : First, create a storage account in Azure. Then, navigate to **Storage Explorer** > **Blob Containers** > **Create a Blob Container**.
  2. Run the following commands to create a cloud storage integration in Snowflake:


    
    
    CREATE STORAGE INTEGRATION <INTEGRATION_NAME>
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = AZURE
    ENABLED = TRUE
    AZURE_TENANT_ID = '<TENANT_ID>'
    STORAGE_ALLOWED_LOCATIONS = ('azure://<account>.blob.core.windows.net/<container>/<PATH>/', 'azure://<account>.blob.core.windows.net/<container>/<PATH>/')
    [ STORAGE_BLOCKED_LOCATIONS = ('azure://<account>.blob.core.windows.net/<container>/<PATH>/', 'azure://<account>.blob.core.windows.net/<container>/<PATH>/') ]
    

You can get your `<TENANT_ID>` by navigating to **Azure Active Directory** > **Properties** > **Directory ID**.

  3. **Grant Snowflake access to the storage locations** : Run the following command and replace `<INTEGRATION_NAME>` with the integration name created in **Step 2**.


    
    
    DESC INTEGRATION <INTEGRATION_NAME>;
    

> ![info](/docs/images/info.svg)
> 
> Record the values for `AZURE_CONSENT_URL` and `AZURE_MULTI_TENANT_APP_NAME`.

  4. Go to the URL obtained in `AZURE_CONSENT_URL` and accept the consent requirements.
  5. **Grant Snowflake access to the container** : Navigate to **Azure Services** > **Storage Accounts** and select the storage account created in **Step 1**.
  6. **Add the role** : Navigate to **Access Control (IAM)** > **Add Role Assignment**. Select either **Storage Blob Data Reader** with **Read** access, or **Storage Blob Data Contributor** with **Read and Write** access.
  7. **Add Assign Access** : Add **Service Principal** as the security principal type for the role. Search for `AZURE_MULTI_TENANT_APP_NAME` that you obtained in **Step 3**.
  8. Grant integration access to the Snowflake role you created in the Creating a role for RudderStack section by running the following command:


    
    
    GRANT USAGE ON integration <INTEGRATION_NAME> to role RUDDER;
    

Here, `<INTEGRATION_NAME>` is the integration you created in **Step 2**.

  9. Set the **Storage Integration** dashboard setting to `<INTEGRATION_NAME`>.


If you want to leverage Google Cloud Storage as your object storage, follow the instructions below. You can find the detailed instructions in this [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/data-load-gcs-config.html#configuring-an-integration-for-google-cloud-storage>).

  1. **Create a Cloud Storage integration in Snowflake** : Run the following command:


    
    
    CREATE STORAGE INTEGRATION <INTEGRATION_NAME>
      TYPE = EXTERNAL_STAGE
      STORAGE_PROVIDER = GCS
      ENABLED = TRUE
      STORAGE_ALLOWED_LOCATIONS = ('gcs://<bucket>/<PATH>/', 'gcs://<bucket>/<PATH>/')
    

Replace `<INTEGRATION_NAME>` with the name of your Cloud Storage integration, `<bucket>` with **Staging GCS Object Storage Bucket Name** , and `<PATH>` with the prefix set in the Configuring the object storage section above.

  2. The following command retrieves the Cloud Storage service account ID created for your Snowflake account, where `<INTEGRATION_NAME>` is the integration name you specified in **Step 1**.


    
    
    DESC STORAGE INTEGRATION <INTEGRATION_NAME>;
    

> ![info](/docs/images/info.svg)
> 
> The output of this command will have a property named as `STORAGE_GCP_SERVICE_ACCOUNT`. Retrieve this property value. It should be of the format `service-account-id@UNIQUE_STRING.iam.gserviceaccount.com`.

  3. **Grant service account permissions to access the bucket objects** : Create a custom IAM role with the required permissions to access the bucket and fetch the objects by following these steps:

     1. Log into the GCP console as a Project Editor.

     2. From the dashboard, go to **IAM & Admin** > **Roles**.

     3. Click **CREATE ROLE**.

     4. Enter the title and description for the custom role.

     5. Click **ADD PERMISSIONS**.

     6. Filter the following permissions in the **Enter property name or value** and add them to the list. Then, click **ADD**.

        * `storage.buckets.get`
        * `storage.objects.get`
        * `storage.objects.list`
        * `storage.objects.create`
  4. **Assign the custom role to the Cloud Storage service account** :

     1. In your GCP console dashboard, go to **Cloud Storage** > **Browser**.
     2. Select the bucket to configure the access.
     3. Select **SHOW INFO PANEL** in the upper right corner. The information panel for the bucket will pop out.
     4. In the **Add Members** section, get the service account name from the `DESC` command run in **Step 2**.
     5. From the **Select a role** dropdown, select **Storage** > **Custom** > `<role>`, where `<role>` is the custom Cloud Storage role.
     6. Click the **ADD** button. The service account name will be added to the **Storage Object Viewer** role dropdown in the information panel.  
  

  5. Grant integration access to the Snowflake role you created in the Creating a role for RudderStack section by running the following command:


    
    
    GRANT USAGE ON INTEGRATION <INTEGRATION_NAME> TO ROLE RUDDER;
    

Here, `<INTEGRATION_NAME>` is the integration name you set up in **Step 1**.

  6. Set the **Storage Integration** dashboard setting to `<INTEGRATION_NAME`>.


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

## Troubleshooting

Issue| Solution  
---|---  
Connection verification step fails| Verify the following:  
  


  * The entire contents of the private key are specified in the **Private Key** field, including the `BEGIN RSA PRIVATE KEY` and `END RSA PRIVATE KEY` delimiters.
  * In case of an encrypted private key, you have specified the passphrase in the **Passphrase** field.

  
HTTP 404 error during connection verification| Verify your Snowflake account URL is correct. You can use the following command to check if the account URL is correct:  
  
`CURL -I https://<account_id>.snowflakecomputing.com`  
  
## FAQ

#### What should I enter in the Account field while configuring Snowflake as a destination?

While configuring Snowflake as a destination in RudderStack, you need to enter your Snowflake connection credentials which include the **Account** field, as shown below:

[![Snowflake account ID example](/docs/images/dw-integrations/snowflake-account-id-example.webp)](</docs/images/dw-integrations/snowflake-account-id-example.webp>)

The **Account** field corresponds to the account ID of your Snowflake warehouse and is a part of the Snowflake URL.

The following examples illustrate the slight differences in the Snowflake account ID for various cloud providers:

Account ID example| Corresponding Snowflake URL| Snowflake cloud provider  
---|---|---  
`qya56091.us-east-1`  
  
`qya56091.us-east-2.aws`| `https://`**`qya56091.us-east-1`**`.snowflakecomputing.com`  
  
`https://`**`qya56091.us-east-2.aws`**`.snowflakecomputing.com`| AWS  
`rx18795.east-us-2.azure`| `https://`**`rx18795.east-us-2.azure`**`.snowflakecomputing.com`| Microsoft Azure  
`ah76025.us-central1.gcp`| `https://`**`ah76025.us-central1.gcp`**`.snowflakecomputing.com`| Google Cloud Platform  
  
> ![warning](/docs/images/warning.svg)
> 
> In case of AWS, `.aws` is present in the account locator of some region’s accounts and must be included in the **Account** field above.
> 
> For more information on account locator formats depending on your region or cloud provider, refer to the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#non-vps-account-locator-formats-by-cloud-platform-and-region>).

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.