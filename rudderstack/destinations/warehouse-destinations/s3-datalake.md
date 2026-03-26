# Amazon S3 Data Lake

Sync data from RudderStack to Amazon S3 Data Lake.

* * *

  * __11 minute read

  * 


Amazon S3 is a popular object storage service used to store both structured and unstructured data. With S3 data lake, you can easily use the native AWS services for data processing, analytics, machine learning, and more.

> ![info](/docs/images/info.svg)
> 
> For more information on how the events are mapped to the tables in S3 data lake tables, see the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/s3_datalake>).

## Setup

> ![warning](/docs/images/warning.svg)
> 
> Before you set up S3 data lake as a destination in RudderStack, make sure to set up your S3 bucket with the required permissions.

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **S3 Data Lake**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

  * **S3 Storage Bucket Name** : Enter the name of the S3 bucket used to store the data before loading it into the S3 data lake.
  * **Register schema on AWS Glue** : Turn on this option to register the schema of your incoming data on AWS Glue’s data catalog. For more information on registering your schema in AWS Glue, see the [AWS Glue documentation](<https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html>).  
  

    * **AWS Glue Region** : If the **Register schema on AWS Glue** setting is turned on, enter your AWS Glue region. For example, for `N.Virginia`, the AWS Glue region would be `us-east-1`. For more information on getting your AWS Glue region and the associated service endpoints, see the [AWS Glue documentation](<https://docs.aws.amazon.com/general/latest/gr/glue.html>).


> ![warning](/docs/images/warning.svg)
> 
> Make sure to grant the following permissions to your AWS Glue instance and the RudderStack IAM role (see **Role Based Authentication** setting below):
> 
>   * glue:CreateTable
>   * glue:UpdateTable
>   * glue:CreateDatabase
>   * glue:GetTables
> 

> 
> The following **additional** permissions are required to use [AWS Glue partitions](<https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html>):
> 
>   * glue:BatchCreatePartition
>   * glue:GetPartition
> 

> 
> If you are using AWS Lake Formation for fine-grained access control on the data in your data lake, see AWS Lake Formation permissions for managing the AWS Glue resources on your Lake Formation model.

  * **S3 Prefix** : If specified, RudderStack creates a folder in the S3 bucket with this name and pushes all data within that folder. For example, `s3://<bucket_name>/<prefix>/`.
  * **Namespace** : If specified, all data for the destination will be pushed to the location `s3://<bucketName>/<prefix>/rudder-datalake/<namespace>`.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If you don’t specify a namespace in the settings, it is set to the source name, by default. You **cannot** change the namespace later.
>   * If **Register schema on AWS Glue** is turned on, RudderStack creates all table definitions in a database with the name set to this namespace.
> 


  * **Role Based Authentication** : Turn on this setting to use the RudderStack IAM role for authentication. For more information on creating an AWS IAM role for RudderStack, see [Create RudderStack IAM role for AWS-based destinations](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>).  
  

    * **IAM Role ARN** : Enter the ARN of the IAM role.


> ![warning](/docs/images/warning.svg)
> 
> It is highly recommended to turn on this setting as the access keys-based authentication method is now deprecated.

If **Role-based Authentication** is disabled, you need to enter the **AWS Access Key ID** and **AWS Secret Access Key** to authorize RudderStack to write to your S3 bucket.

> ![info](/docs/images/info.svg)
> 
> In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your S3 bucket. Refer to the Permissions section for more information.

  * **Enable server-side encryption for S3** : When you turn on this setting, RudderStack adds a header `x-amz-server-side-encryption` with the value `AES256` to the `PutObject` request when sending the data to the S3 bucket. See [Encryption with S3 managed keys](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#s3-managed-keys>) for more information.
  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your S3 data lake.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data.


### Advanced settings

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.


## S3 bucket setup

  1. Go to your [S3 Management console](<https://s3.console.aws.amazon.com/s3/>).
  2. [Create a new bucket](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>). Alternatively, you can choose an existing bucket.


> ![info](/docs/images/info.svg)
> 
> It is recommended to create a new bucket for storing events coming from RudderStack.

#### S3 Permissions

To send events to your S3 data lake successfully, you need to give RudderStack the necessary permissions to write to your bucket. You can choose any of the following approaches based on your company’s security policies and setup preferences:

#### Option 1: Use RudderStack IAM role

> ![success](/docs/images/tick.svg)
> 
> It is highly recommended to use this option for setting up the required S3 bucket permissions.

Use this approach if you are going to set up the S3 destination in RudderStack using **Role Based Authentication**.

[![Role based authentication](/docs/images/event-stream-destinations/role-based-authentication.webp)](</docs/images/event-stream-destinations/role-based-authentication.webp>)

  1. [Create a RudderStack IAM role](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/>).
  2. Use the following S3 permissions policy for creating the role:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Sid": "Statement1",
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        "Resource": [
          "arn:aws:s3:::<S3_BUCKET_NAME>",
          "arn:aws:s3:::<S3_BUCKET_NAME>/*"
        ]
      }]
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Replace `<S3_BUCKET_NAME>` with the actual bucket name.

  3. After creating the role, note and specify the **IAM Role ARN** to set up your S3 data lake destination.


#### Option 2: Create IAM user and provide credentials

> ![danger](/docs/images/danger.svg)
> 
> Note that:
> 
>   * Using **Role-based Authentication (Option 1)** is highly recommended as this method is now deprecated and will be discontinued soon.
>   * AWS **does not** recommend access key credentials-based authentication.
> 


Use this approach if you are going to set up the S3 data lake destination in RudderStack using the **Access Key Based Authentication**.

[![Access key based authentication](/docs/images/event-stream-destinations/access-key-based-authentication.webp)](</docs/images/event-stream-destinations/access-key-based-authentication.webp>)

  1. Log in to your [Amazon AWS IAM Console](<https://console.aws.amazon.com/iam/>).
  2. [Create an IAM user](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>). Choose a policy that has **write** access to your bucket. Alternatively, you can [create a new policy](<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start>) with the following permissions and attach it to the IAM user:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Sid": "Statement1",
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        "Resource": [
          "arn:aws:s3:::<S3_BUCKET_NAME>",
          "arn:aws:s3:::<S3_BUCKET_NAME>/*"
        ]
      }]
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Replace `<S3_BUCKET_NAME>` with the actual bucket name.

  3. Return to the IAM dashboard and go to **Users** under **Access management**. Then, click on the newly-created user.
  4. Go to the **Security credentials** tab and scroll down to **Access keys**.
  5. Click **Create access key** , select the use case as per your requirement, and click **Next**.
  6. If required, set the **Description tag value** , and click **Create access key**.
  7. Note and secure the **Access key** and **Secret access key**. Use these credentials to set up your S3 data lake destination in RudderStack.


## Find data in S3 data lake

RudderStack converts your events into Apache Parquet files and stores them into the configured S3 bucket. Before storing the events, RudderStack groups them by the event name based on the UTC time they were received.

The folder structure is shown below:
    
    
    s3://<bucketName>/<prefix>/rudder-datalake/<namespace>/<tableName>/YYYY/MM/DD/HH
    

As mentioned in the Connection settings section:

  * `prefix`: This is the S3 prefix in the destination settings. If not specified, RudderStack will omit this value.
  * `namespace`: The namespace specified in the destination settings. If not specified, RudderStack sets this field to the source name by default.
  * `tableName`: RudderStack sets this to the event name.
  * `YYYY`, `MM`, `DD`, and `HH` are replaced by actual time values. A combination of these values represents the UTC time.


#### Use case

Suppose RudderStack tracks the following two events:

Event name| Timestamp  
---|---  
`Product Purchased`| `"2019-10-12T08:40:50.52Z" UTC`  
`Cart Viewed`| `"2019-11-12T09:34:50.52Z" UTC`  
  
RudderStack converts these events into Parquet files and dumps them into the following folders:

Event name| Folder location  
---|---  
`Product Purchased`| `s3://<bucketName>/<prefix>/rudder-datalake/<namespace>/product_purchased/2019/10/12/08`  
`Cart Viewed`| `s3://<bucketName>/<prefix>/rudder-datalake/<namespace>/cart_viewed/2019/11/12/09`  
  
> ![info](/docs/images/info.svg)
> 
> If you have the **Register schema on AWS Glue** setting toggled on, RudderStack creates all table definitions in a database with the name set to the **Namespace** specified in the dashboard settings.

## Create table definitions using a crawler

> ![warning](/docs/images/warning.svg)
> 
> Refer to this section **only** if you haven’t toggled on the **Register Schema on AWS Glue** setting while configuring the S3 data lake destination in RudderStack.

In the absence of AWS Glue, you can create a crawler to go through your data and create table definitions out of it. To do so, follow these steps:

  1. Go to your AWS Glue console and select **Crawler** from the left pane.
  2. Select **Add Crawler**.
  3. Specify a name for your crawler and click **Next** :

[![Add Crawler](/docs/images/dw-integrations/s3-datalake-crawler-1.webp)](</docs/images/dw-integrations/s3-datalake-crawler-1.webp>)

  4. Next, under the **Crawler source type** section, choose **Data stores**.

[![Crawler source type](/docs/images/dw-integrations/s3-datalake-crawler-2.webp)](</docs/images/dw-integrations/s3-datalake-crawler-2.webp>)

  5. Configure the **Repeat crawls of S3 data stores** based on your requirement.
  6. Then, under the **Data store** section, select **S3** from the dropdown for the **Choose a data store** setting:

[![Choose a data store](/docs/images/dw-integrations/s3-datalake-crawler-3.webp)](</docs/images/dw-integrations/s3-datalake-crawler-3.webp>)

  7. For the **Crawl data in** setting, choose **Specified path in my account**.
  8. In the **Include path** setting, enter the S3 URI of your configured bucket followed by the suffix `/<prefix>/rudder-datalake/<namespace>/`.


> ![info](/docs/images/info.svg)
> 
> If your S3 bucket name is `testBucket` and the configured prefix and namespace are `testPrefix` and `testNameSpace` respectively, then your path should be: `s3://testBucket/testPrefix/rudder-datalake/testNameSpace/`

> ![warning](/docs/images/warning.svg)
> 
> If you have not configured any prefix while setting up the S3 data lake destination in RudderStack, omit the prefix. The path would then be: `s3://testBucket/rudder-datalake/testNameSpace/`.

  9. Then, under the **Add another data store** setting, select **No** :

[![Add another data store](/docs/images/dw-integrations/s3-datalake-crawler-4.webp)](</docs/images/dw-integrations/s3-datalake-crawler-4.webp>)

  10. In the **IAM Role** section, configure a suitable IAM role.

[![IAM Role](/docs/images/dw-integrations/s3-datalake-crawler-5.webp)](</docs/images/dw-integrations/s3-datalake-crawler-5.webp>)

  11. In the **Schedule** section, select the frequency of your crawler from the dropdown options:

[![Scheduler](/docs/images/dw-integrations/s3-datalake-crawler-6.webp)](</docs/images/dw-integrations/s3-datalake-crawler-6.webp>)

  12. In the **Output** section, configure the database that stores all tables. Under the Grouping behavior for S3 data section, turn on the **Create a single schema for each S3 path** option:

[![Output](/docs/images/dw-integrations/s3-datalake-crawler-7.webp)](</docs/images/dw-integrations/s3-datalake-crawler-7.webp>)

  13. Specify the **Table level** as **5** or **4** (refer to the tips below). This value indicates the absolute level of the table location in the bucket.


> ![warning](/docs/images/warning.svg)
> 
> Since all tables are created in the path `s3://testBucket/<prefix>/rudder-datalake/<namespace>/`, make sure the table level is set to:
> 
>   * **5** : If a prefix is configured.
>   * **4** : If a prefix is **not** configured.
> 


> ![info](/docs/images/info.svg)
> 
> The level for the top-level folder is 1. For example, for the path `mydataset/a/b`, if the level is set to 3, the table will be created at the location `mydataset/a/b`. Similarly, if the level is set to 2, the table will be created at the location `mydataset/a`.

  14. Review your crawler configuration and click **Finish** to confirm.

[![Review crawler configuration](/docs/images/dw-integrations/s3-datalake-crawler-8.webp)](</docs/images/dw-integrations/s3-datalake-crawler-8.webp>)

  15. Finally, click your crawler and run it. Wait for the process to finish - you should see some tables created in your configured database.


## Query data using AWS Athena

You can query your S3 data using a tool like [AWS Athena](<https://aws.amazon.com/athena/>) which lets you run SQL queries on S3.

> ![warning](/docs/images/warning.svg)
> 
> Before querying your data on S3, make sure that you have sent some data to S3 and the sync is complete.

Follow these steps to start querying your data on s3:

  1. Open your AWS Athena console. Then, go to the same AWS region which was used while configuring AWS Glue.
  2. In the left pane, select `AwsDataCatalog` as your data source:

[![AwsDataCatalog](/docs/images/dw-integrations/s3-datalake-querying-data-1.webp)](</docs/images/dw-integrations/s3-datalake-querying-data-1.webp>)

  3. Select your configured namespace (or the database you specified while configuring the crawler) from the database dropdown menu.

[![Database](/docs/images/dw-integrations/s3-datalake-querying-data-2.webp)](</docs/images/dw-integrations/s3-datalake-querying-data-2.webp>)

> ![info](/docs/images/info.svg)
> 
> By default, RudderStack sets the namespace to your source name if it is not explicitly specified in the destination settings.

  4. You should see some tables already created under the **Tables** section in the left pane.
  5. You can preview the data by clicking on the three dots next to the table and selecting the **Preview Data** option. Alternatively, you can run your own SQL queries in the workspace on the right:

[![Preview Data](/docs/images/dw-integrations/s3-datalake-querying-data-3.webp)](</docs/images/dw-integrations/s3-datalake-querying-data-3.webp>)

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

## AWS Lake Formation permissions

AWS Lake Formation lets you have fine-grained access control for the data in your lake. You can use the Lake Formation permissions model to manage your existing AWS Glue data catalog objects and data locations in Amazon S3.

To maintain backward compatibility with AWS Glue, Lake Formation has the [`Super` permission](<https://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation-background.html>) for the `IAMAllowedPrincipals` group on all the existing AWS Glue data catalog resources.

The following sections contain the necessary permissions that you need to assign for the [configured IAM role](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/#creating-a-rudderstack-iam-role>) **if** you have edited the default Lake Formation security settings so that:

  * The IAM role does not have the data lake administrator permissions, or
  * The `IAMAllowedPrincipals` group does not have the default permissions to create or access the Glue resources.


> ![info](/docs/images/info.svg)
> 
> Make sure **Register schema on AWS Glue** is enabled in the RudderStack dashboard for these settings to take effect.

#### Database creator permissions

  1. Log in to your [AWS management console](<https://console.aws.amazon.com/>) and go to Lake Formation settings.
  2. Under **Administration** , go to **Administrative roles and tasks**.
  3. Under **Database creators** , add the configured IAM role.

[![Database creators in AWS Lake Formation](/docs/images/dw-integrations/lakeformation-database-creators.webp)](</docs/images/dw-integrations/lakeformation-database-creators.webp>)

#### Data location permissions

Data location permissions in Lake Formation enable you to create and alter the data catalog resources that point to a specific S3 location. These permissions work in addition to the Lake Formation permissions to secure the data in your data lake.

This section assumes a data location is registered for your AWS Lake Formation.

[![Database creators in AWS Lake Formation](/docs/images/dw-integrations/lakeformation-register-location.webp)](</docs/images/dw-integrations/lakeformation-register-location.webp>)

To provide the [data location permissions](<https://docs.aws.amazon.com/lake-formation/latest/dg/granting-location-permissions.html>) for the configured IAM role, follow these steps:

  1. Under **Permissions** , click **Data locations**.
  2. Add the configured IAM role to grant permissions to the storage location.

[![Database creators in AWS Lake Formation](/docs/images/dw-integrations/lakeformation-location-permissions.webp)](</docs/images/dw-integrations/lakeformation-location-permissions.webp>)

#### Resource access permissions

  1. Go to **Permissions** > **Data lake permissions**.
  2. Grant the following access permissions for either `IAMAllowedPrincipals` or the configured IAM role.


  * `CREATE_TABLE` granted on `DATABASE` resource.
  * `ALTER` granted on `TABLE` resource.
  * `DESCRIBE` granted on `TABLE` resource.


See [Granting and revoking permissions on Data Catalog resources](<https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html>) for more information.

### Troubleshooting

The following table lists the possible permissions-related errors you might encounter while setting up the S3 data lake destination and their solutions:

Verification step| Error| Solution  
---|---|---  
Verifying Create Schema| AccessDeniedException: Insufficient Lake Formation permission(s): Required Create Database on Catalog| Provide database creator permissions for the configured IAM role.  
Verifying Create and Alter Table| create table: AccessDeniedException: Insufficient Lake Formation permission(s) on s3://path/you/have/configured| Provide data location permissions for the configured IAM role.  
Verifying Create and Alter Table| create table: AccessDeniedException: Insufficient Lake Formation permission(s): Required Create Table on xxx| Provide resource access for the configured IAM role.  
  
## FAQ

For a comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.