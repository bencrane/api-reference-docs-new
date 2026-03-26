# RudderStack IAM role for Redshift

Create a RudderStack IAM role for authenticating to Redshift.

* * *

  * __4 minute read

  * 


This guide contains the steps to create an IAM role for authenticating RudderStack while setting up the following resources:

  * [Redshift destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>)
  * [Redshift Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/>)


## Prerequisites

Before creating the IAM role, make sure you have:

  * Access to your AWS Management Console with permissions to:
    * Create IAM policies
    * Create IAM roles
    * Manage trust relationships
  * Your [RudderStack workspace ID](<https://www.rudderstack.com/docs/dashboard-guides/overview/#workspace>)
  * For Redshift Serverless:
    * Workgroup ID
    * AWS region
    * AWS account ID
  * For Redshift Provisioned:
    * Cluster identifier
    * AWS region
    * AWS account ID
    * Database name
    * Database user name


## Create RudderStack IAM role

This section contains the steps to set up a new RudderStack IAM role with the required permissions to access your Redshift database.

### Create policy

  1. Sign in to your AWS Management Console and open the [IAM console](<https://console.aws.amazon.com/iam/>).
  2. Go to **Policies** > **Create policy**. See [Creating IAM policies](<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start>) guide for more information.
  3. Choose the **JSON** option. Then, paste the JSON (shown below) depending on whether the [**Use Redshift Serverless**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/#connection-settings>) connection setting is toggled on or off:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
          "Action": "redshift-serverless:GetCredentials",
          "Effect": "Allow",
          "Resource": [
            "arn:aws:redshift-serverless:${Region}:${Account}:workgroup/${WorkgroupId}"
          ],
          "Sid": "VisualEditor0"
        },
        {
          "Action": [
            "redshift-data:BatchExecuteStatement",
            "redshift-data:ExecuteStatement"
          ],
          "Effect": "Allow",
          "Resource": [
            "arn:aws:redshift-serverless:${Region}:${Account}:workgroup/${WorkgroupId}"
          ],
          "Sid": "VisualEditor1"
        },
        {
          "Action": [
            "redshift-data:GetStatementResult",
            "redshift-data:CancelStatement",
            "redshift-data:DescribeStatement"
          ],
          "Effect": "Allow",
          "Resource": "*",
          "Sid": "VisualEditor2"
        }
      ]
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to replace `{Region}`, `{Account}`, and `{WorkgroupId}` in the above policy with the exact values for your AWS region, account, and the workgroup ID, respectively.
    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
          "Action": "redshift:GetClusterCredentials",
          "Effect": "Allow",
          "Resource": [
            "arn:aws:redshift:${Region}:${Account}:dbuser:${ClusterIdentifier}/${DbUser}",
            "arn:aws:redshift:${Region}:${Account}:dbname:${ClusterIdentifier}/${DbName}"
          ],
          "Sid": "VisualEditor0"
        },
        {
          "Action": [
            "redshift-data:BatchExecuteStatement",
            "redshift-data:ExecuteStatement"
          ],
          "Effect": "Allow",
          "Resource": [
            "arn:aws:redshift:${Region}:${Account}:cluster:${ClusterIdentifier}"
          ],
          "Sid": "VisualEditor1"
        },
        {
          "Action": [
            "redshift-data:GetStatementResult",
            "redshift-data:CancelStatement",
            "redshift-data:DescribeStatement"
          ],
          "Effect": "Allow",
          "Resource": "*",
          "Sid": "VisualEditor2"
        }
      ]
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Note the following:
> 
>   * Make sure to replace `{Region}`, `{Account}`, and `{ClusterIdentifier}` in the above policy with the exact values for your AWS region, account, and cluster, respectively.
>   * Replace `{DbUser}` with the user name used to log in to the database. See **Step 2** of [Setting user permissions in Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/#setting-user-permissions-in-redshift>) for more information.
>   * Replace `{DbName}` with the name of the database for which the above user has access.
> 


### Set up new IAM role

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
  7. In the policy selection screen, add the policy created in the Create policy section.
  8. Review all settings carefully and click **Next** to proceed.
  9. Enter a unique name for your role. Note that this name cannot be distinguished by case. For example, you cannot create a role named `RUDDERSTACK` if `rudderstack` already exists.


> ![warning](/docs/images/warning.svg)
> 
> You cannot edit the name of the role after it has been created.

  10. Enter the role description.
  11. To edit the use case or permissions for the role, click the **Edit** button next to the **Step 1: Select trusted entities** or **Step 2: Add permissions** , respectively.

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-4.webp)](</docs/images/destinations/aws-role-4.webp>)

  12. **Optional** : You can also add metadata to the role by attaching tags as key-value pairs. For more information, refer to the [Tagging IAM resources](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>) guide.
  13. Click **Create role** to complete the setup.
  14. Finally, note the **ARN** of this newly created role.

[![Setting up AWS IAM Role for RudderStack](/docs/images/destinations/aws-role-5.webp)](</docs/images/destinations/aws-role-5.webp>)

## Use IAM role during Redshift setup

You can use the RudderStack IAM role to authenticate to Redshift for the following use cases:

### Warehouse destination

  1. Toggle on the **Use IAM for authentication** setting.
  2. Specify the below settings depending on whether the [**Use Redshift Serverless**](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/#connection-settings>) connection setting is toggled on or off:


  * **Workgroup name** : Enter the Redshift serverless workgroup name.
  * **Cluster region** : Enter your AWS cluster region.
  * **IAM role ARN for Authentication** : Enter the ARN of the RudderStack IAM role configured above.


  * **Cluster ID** : Enter your AWS cluster identifier.
  * **Cluster region** : Enter your AWS cluster region.
  * **IAM role ARN for Authentication** : Enter the ARN of the RudderStack IAM role configured above.


See the [Redshift destination setup](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/#connection-settings>) guide for more details.

### Reverse ETL source

  1. Select **IAM** as the **Authentication Type**.
  2. Enter the ARN of the RudderStack IAM role in the **IAM Role ARN** setting.
  3. Specify the below settings:


  * **Cluster identifier** : Enter your AWS cluster ID.
  * **Cluster region** : Enter your AWS cluster region.

[![Setting up AWS IAM Role for Redshift source](/docs/images/warehouse-destinations/redshift-source-iam.webp)](</docs/images/warehouse-destinations/redshift-source-iam.webp>)

See the [Redshift Reverse ETL source setup](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#configuring-the-connection-credentials>) guide for more details.