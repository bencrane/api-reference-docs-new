# Create a RudderStack IAM role for AWS-based destinations

Create a RudderStack IAM role for authenticating AWS-based destinations.

* * *

  * __3 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This guide is applicable only for [RudderStack Cloud](<https://app.rudderstack.com/>) users. As the [access keys-based authentication](<https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html>) method is deprecated, RudderStack recommends setting up a RudderStack IAM role for authenticating your AWS destinations.
> 
> Note that this guide is **not applicable** for the following users:
> 
>   * [RudderStack Open Source](<https://github.com/rudderlabs/rudder-server>): You can use the [access keys-based method](<https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html>) to authenticate your AWS destinations.
>   * Customers with on-premise RudderStack deployments. [Contact](<mailto:support@rudderstack.com>) the RudderStack team to set up the IAM role.
> 


This guide contains the steps to create an IAM role for authenticating RudderStack while setting up the following AWS destinations:

#### Cloud destinations

  * [AWS EventBridge](</docs/destinations/streaming-destinations/amazon-eventbridge/>)
  * [AWS Lambda](</docs/destinations/streaming-destinations/aws-lambda/>)
  * [AWS Personalize](</docs/destinations/streaming-destinations/aws-personalize/>)
  * [Amazon Kinesis](</docs/destinations/streaming-destinations/amazon-kinesis/>)
  * [Amazon Kinesis Firehose](</docs/destinations/streaming-destinations/amazon-kinesis-firehose/>)
  * [Amazon S3](</docs/destinations/streaming-destinations/amazon-s3/>)


#### Warehouse destinations

  * [Amazon Redshift](</docs/destinations/warehouse-destinations/redshift/>)
  * [Amazon S3 Data Lake](</docs/destinations/warehouse-destinations/s3-datalake/>)
  * [Azure Synapse](</docs/destinations/warehouse-destinations/azure-synapse/>)
  * [ClickHouse](</docs/destinations/warehouse-destinations/clickhouse/>)
  * [Databricks Delta Lake](</docs/destinations/warehouse-destinations/delta-lake/>)
  * [Materialize](</docs/destinations/warehouse-destinations/materialize/>)
  * [Microsoft SQL Server](</docs/destinations/warehouse-destinations/sql-server/>)
  * [PostgreSQL](</docs/destinations/warehouse-destinations/postgresql/>)
  * [Snowflake](</docs/destinations/warehouse-destinations/snowflake/>)


  


> ![info](/docs/images/info.svg)
> 
> See the [RudderStack IAM Role for Redshift](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/redshift-iam-role/>) guide to create an IAM role for authenticating RudderStack while setting up the Redshift destination.

## Create RudderStack IAM role

To set up a new RudderStack IAM role, follow these steps:

  1. Sign in to your AWS Management Console and open the [IAM console](<https://console.aws.amazon.com/iam/>).
  2. In the left navigation pane, click **Roles** followed by **Create role**.
  3. Under **Trusted entity type** , select **AWS account** :

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-1.webp)](</docs/images/destinations/aws-role-1.webp>)

  4. Select **Another AWS account** and under **Account ID** , enter `422074288268`, the account ID associated with RudderStack.
  5. Under **Options** check **Require external ID** and enter your [workspace ID](<https://www.rudderstack.com/docs/dashboard-guides/overview/#workspace-id>) as the **External ID**.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently **does not support** MFA setting that restricts the role only to the users who sign in using [multi-factor authentication (MFA)](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html>). Hence, do not check the **Require MFA** option.

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-2.webp)](</docs/images/destinations/aws-role-2.webp>)

  6. Review all settings carefully and click **Next** to proceed.
  7. Select your destination-specific permission policies applicable for the RudderStack IAM role. To create a new policy from scratch, click **Create policy**. For more information, refer to the [Creating IAM policies](<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start>) guide.
  8. **Optional** : You can also set a [permissions boundary](<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>). Expand the **Set permissions boundary** section, choose **Use a permissions boundary to control the maximum role permissions** , and select the policy to use for the permissions boundary. An example is shown below:

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-3.webp)](</docs/images/destinations/aws-role-3.webp>)

  9. Review all settings carefully and click **Next** to proceed.
  10. Enter a unique name for your role. Note that this name cannot be distinguished by case. For example, you cannot create a role named `RUDDERSTACK` if `rudderstack` already exists.


> ![warning](/docs/images/warning.svg)
> 
> You cannot edit the name of the role after it has been created.

  11. **Optional** : Enter the description for this role.
  12. To edit the use case or permissions for the role, click the **Edit** button next to the **Step 1: Select trusted entities** or **Step 2: Add permissions** , respectively.

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-4.webp)](</docs/images/destinations/aws-role-4.webp>)

  13. **Optional** : You can also add metadata to the role by attaching tags as key-value pairs. For more information, refer to the [Tagging IAM resources](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>) guide.
  14. Click **Create role** to complete the setup.
  15. Finally, note the **ARN** of this newly created role.

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-5.webp)](</docs/images/destinations/aws-role-5.webp>)

This ARN is required while configuring your AWS destination when you enable the **Role-based Authentication** setting:

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-6.webp)](</docs/images/destinations/aws-role-6.webp>)

## Destination-specific policy permissions

Refer to the following sections for the destination-specific policy permissions:

  * [EventBridge](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-eventbridge/#policy-permissions>)
  * [Kinesis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis/#policy-permissions>)
  * [Kinesis Firehose](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis-firehose/#policy-permissions>)
  * [Lambda](<https://www.rudderstack.com/docs/destinations/streaming-destinations/aws-lambda/#policy-permissions>)
  * [Personalize](<https://www.rudderstack.com/docs/destinations/streaming-destinations/aws-personalize/#policy-permissions>)
  * [Redshift](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/redshift-iam-role/>)
  * [S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#option-1-use-rudderstack-iam-role>)