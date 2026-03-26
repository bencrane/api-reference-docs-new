# Amazon S3 Destination

Send your event data from RudderStack to Amazon S3.

* * *

  * __9 minute read

  * 


[Amazon S3](<https://aws.amazon.com/s3/>) (Simple Storage Service) is a cloud-based object storage service that lets customers and businesses store their data securely and at scale.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/s3>).

## Prerequisites

  * Make sure to set up your S3 bucket with the required permissions.


## Setup

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Amazon S3**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

> ![success](/docs/images/tick.svg)
> 
> If you have already configured the AWS credentials in your RudderStack setup via [environment credentials](<https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials>) or by following the steps in the Permissions setup section, then specifying only **S3 Bucket Name** and **Prefix** (optional but recommended) is sufficient to set up your S3 destination.

Setting| Description  
---|---  
S3 Bucket Name| Enter your S3 bucket name.  
Prefix| If specified, RudderStack creates a folder in the S3 bucket with this name and pushes all data within that folder. For example, `s3://<bucket_name>/<prefix>/`.  
Role-based Authentication| This setting is toggled on by default and lets you use the [RudderStack IAM role](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/>) for authentication.  
IAM Role ARN| This setting is visible if **Role-based Authentication** is toggled on. Enter the ARN of the IAM role in this field.  
Enable Server Side Encryption| When you enable this setting, RudderStack adds a header `x-amz-server-side-encryption` with the value `AES256` to the `PutObject` request when sending the data to the S3 bucket.  
  
See Encryption with S3 managed keys for more information.  
  
You will see the following settings if **Role-based Authentication** is toggled off:

Setting| Description  
---|---  
AWS Access Key ID| Enter the AWS access key ID to authorize RudderStack to write to your S3 bucket.  
AWS Secret Access Key| Enter the secret access key corresponding to the Access Key ID.  
  
See the Permissions section more information on obtaining the **AWS Access Key ID** and **AWS Secret Access Key** values.

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * RudderStack recommends using **Role-based Authentication** as the access keys-based authentication method is deprecated and will be discontinued soon.
>   * In both the role-based and access key-based authentication methods, you need to set a policy specifying the required permissions for RudderStack to write to your S3 bucket.
>   * If you are using your S3 bucket as an intermediary object storage for sending events to a [warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>), then see the S3 permissions for warehouse destinations.
> 


#### Consent management settings

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## S3 bucket setup

  1. Go to your [S3 Management console](<https://s3.console.aws.amazon.com/s3/>).
  2. [Create a new bucket](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>). Alternatively, you can choose an existing bucket.


> ![info](/docs/images/info.svg)
> 
> It is recommended to create a new bucket for storing events coming from RudderStack.

### Permissions

To send events to S3 successfully, you need to give RudderStack the necessary permissions to write to your bucket. You can choose any of the following approaches based on your company’s security policies and setup preferences:

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
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:PutObject",
          "Resource": "arn:aws:s3:::<S3_BUCKET_NAME>/*"
        }
      ]
    }
    

Make sure to replace `<S3_BUCKET_NAME>` with the actual bucket name.

  3. After creating the role, note and specify the **IAM Role ARN** to set up your S3 destination.


#### Option 2: Create IAM user and provide credentials

> ![danger](/docs/images/danger.svg)
> 
> Note that:
> 
>   * Using **Role-based Authentication (Option 1)** is highly recommended as this method is now deprecated and will be discontinued soon.
>   * AWS **does not** recommend access key credentials-based authentication.
> 


Use this approach to set up the S3 destination in RudderStack using **Access Key Based Authentication**.

[![Access key based authentication](/docs/images/event-stream-destinations/access-key-based-authentication.webp)](</docs/images/event-stream-destinations/access-key-based-authentication.webp>)

> ![info](/docs/images/info.svg)
> 
> If the AWS credentials are already configured on your instance (see Option 4) where the RudderStack server is set up, you do not need to specify these credentials.

  1. Log in to your [Amazon AWS IAM Console](<https://console.aws.amazon.com/iam/>).
  2. [Create an IAM user](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>). Choose a policy that has **write** access to your bucket. Alternatively, you can [create a new policy](<https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html#access_policies_create-start>) with the following permissions and attach it to the IAM user:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:PutObject",
          "Resource": "arn:aws:s3:::<S3_BUCKET_NAME>/*"
        }
      ]
    }
    

Make sure to replace `<S3_BUCKET_NAME>` with the actual bucket name.

  3. Return to the IAM dashboard and go to **Users** under **Access management**. Then, click on the newly-created user.
  4. Go to the **Security credentials** tab and scroll down to **Access keys**.
  5. Click **Create access key** , select the use case as per your requirement, and click **Next**.
  6. If required, set the **Description tag value** , and click **Create access key**.
  7. Note and secure the **Access key** and **Secret access key**. Use these credentials to set up your S3 destination in RudderStack.


#### Option 3: Allow RudderStack to write into bucket

> ![warning](/docs/images/warning.svg)
> 
> Use this option **only if** :
> 
>   * You are using [RudderStack Cloud](<https://app.rudderstack.com/>) to set up your connection.
>   * You want to allow RudderStack to write into your S3 bucket directly.
> 


For this option, you can leave the role based authentication (**IAM Role ARN**) or access key based authentication (**AWS Access Key ID** and **AWS Secret Access Key**) fields blank while setting up your S3 destination in RudderStack.

Add the following JSON in your bucket policy:
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::422074288268:user/s3-copy"
          },
          "Action": ["s3:PutObject", "s3:PutObjectAcl"],
          "Resource": ["arn:aws:s3:::<S3_BUCKET_NAME>/*"]
        }
      ]
    }
    

Make sure to replace `<S3_BUCKET_NAME>` with the actual bucket name.

By adding the above policy, the RudderStack user `arn:aws:iam::422074288268:user/s3-copy` will get the necessary permission to write into your bucket.

#### Option 4: Self-hosted RudderStack

> ![warning](/docs/images/warning.svg)
> 
> Use this approach **only if** you are hosting RudderStack in your own instance and don’t want to follow the above options.

  1. [Create a new IAM user](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>) and attach the below policy:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "*",
          "Resource": "arn:aws:s3:::*"
        }
      ]
    }
    

  2. Add the following policy to your bucket. Replace `ACCOUNT_ID`, `USER_ARN`, and `<S3_BUCKET_NAME>` with the AWS account ID, user ARN, and the S3 bucket name.


    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::ACCOUNT_ID:user/USER_ARN"
          },
          "Action": ["s3:PutObject", "s3:PutObjectAcl"],
          "Resource": ["arn:aws:s3:::<S3_BUCKET_NAME>/*"]
        }
      ]
    }
    

  3. Return to the IAM dashboard and go to **Users** under **Access management**. Then, click on the newly-created user.
  4. Go to the **Security credentials** tab and scroll down to **Access keys**.
  5. Click **Create access key** , select the use case as per your requirement, and click **Next**.
  6. If required, set the **Description tag value** , and click **Create access key**.
  7. Note and secure the **Access key** and **Secret access key**.
  8. Add the above credentials to your RudderStack setup environment:


    
    
    RUDDER_AWS_S3_COPY_USER_ACCESS_KEY_ID=<access_key_id>
    RUDDER_AWS_S3_COPY_USER_ACCESS_KEY=<secret_access_key>
    

### S3 permissions for warehouse destinations

If you’re using your S3 bucket as an **intermediary object storage** for a [warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>), then attach the below permissions policy depending on your use case:

> ![warning](/docs/images/warning.svg)
> 
> Note that the below policy is applicable only for the below authentication options:
> 
>   * Using the RudderStack IAM role (recommended)
>   * Using the access key credentials
> 

    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:PutObjectAcl",
          "s3:ListBucket"
        ],
        "Resource": "arn:aws:s3:::<S3_BUCKET_NAME>/*"
      }]
    }
    

To allow RudderStack to write into your bucket directly (Option 3), use the following policy:
    
    
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
        "Resource": ["arn:aws:s3:::<S3_BUCKET_NAME>/*"]
      }]
    }
    

For self-hosted RudderStack (Option 4), use the following bucket policy in Step 2:
    
    
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
        "Resource": ["arn:aws:s3:::<S3_BUCKET_NAME>/*"]
      }]
    }
    

Make sure to replace `<S3_BUCKET_NAME>` with the actual bucket name.

## Encryption

Amazon S3 provides encryption at rest. The objects get encrypted while saving them to the bucket and are decrypted before downloading from S3.

S3 lets you set the default encryption behavior for a bucket. It encrypts the objects using server-side encryption with either **Amazon S3 managed keys (SSE-S3)** or **AWS KMS-managed keys (SSE-KMS)**.

#### Set default encryption

  1. Log in to your [S3 Management console](<https://s3.console.aws.amazon.com/s3/>) and select your bucket.
  2. Go to the **Properties** tab and scroll down to **Default encryption**. Then, click **Edit**.
  3. Under **Encryption key type** , choose from **Amazon S3 managed keys (SSE-S3)** or **AWS KMS-managed keys (SSE-KMS)** :

[![S3 default encryption](/docs/images/event-stream-destinations/s3-default-encryption-new.webp)](</docs/images/event-stream-destinations/s3-default-encryption-new.webp>)

The following settings are applicable if you choose **AWS KMS-managed keys (SSE-KMS)** as the encryption key type:

[![KMS encryption configuration](/docs/images/event-stream-destinations/s3-default-encryption-kms.webp)](</docs/images/event-stream-destinations/s3-default-encryption-kms.webp>)

> ![info](/docs/images/info.svg)
> 
> You can choose an existing AWS KMS key, enter the ARN of an AWS KMS key, or create a new KMS key.

  4. Under **Bucket Key** , choose **Enable** and click **Save changes**.


For more information on setting the default encryption behavior for a bucket, see the [S3 documentation](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html>).

### AWS KMS keys

When the default encryption is set to **AWS KMS-managed keys (SSE-KMS)** , S3 encrypts the objects using the customer managed keys (CMK) when they are uploaded to the bucket.

#### Create a new customer managed key

  1. Log in to the [AWS Key Management Service (KMS) console](<https://aws.amazon.com/kms/>).

[![KMS console login](/docs/images/event-stream-destinations/aws-kms-1.webp)](</docs/images/event-stream-destinations/aws-kms-1.webp>)

  2. From the left sidebar, go to **Customer managed keys** and click **Create key**.

[![Create new CMK](/docs/images/event-stream-destinations/aws-kms-2.webp)](</docs/images/event-stream-destinations/aws-kms-2.webp>)

  3. Under **Key type** , choose **Symmetric**. Under **Key usage** , select **Encrypt and decrypt**.


> ![warning](/docs/images/warning.svg)
> 
> S3 supports only [symmetric CMKs](<https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks>).

[![Key type and usage](/docs/images/event-stream-destinations/aws-kms-3.webp)](</docs/images/event-stream-destinations/aws-kms-3.webp>)

  4. Set an **Alias** for the key. You can also add a description or tags for the key as required.

[![Key alias and description](/docs/images/event-stream-destinations/aws-kms-4.webp)](</docs/images/event-stream-destinations/aws-kms-4.webp>)

  5. Choose the IAM user or role who can administer and use this key.

[![Key adminstration and usage](/docs/images/event-stream-destinations/aws-kms-5.webp)](</docs/images/event-stream-destinations/aws-kms-5.webp>)

  6. Review the configuration and click **Finish** to create the customer managed key.
  7. Finally, set the default encryption for your S3 bucket as **AWS KMS-managed keys (SSE-KMS)** and select this customer managed key.


### S3 managed keys

When you enable the **Enable Server Side Encryption** dashboard setting while configuring your S3 destination, RudderStack adds a `x-amz-server-side-encryption` header with the value `AES256` to all the `PutObject` requests. S3 then encrypts the object with the AES256 encryption algorithm. For more information, see [S3 encryption with S3 managed keys](<https://docs.aws.amazon.com/AmazonS3/latest/dev/SSEUsingRESTAPI.html>).

> ![warning](/docs/images/warning.svg)
> 
> If you set the default encryption key type to **Amazon S3 managed keys (SSE-S3)** , then S3 encrypts the objects that are uploaded in the bucket with AES256 encryption - irrespective of whether the **Enable Server Side Encryption** is enabled in the RudderStack dashboard or the presence of the `x-amz-server-side-encryption` header in the `PutObject` requests.

## Where RudderStack stores the data

RudderStack stores the data in the S3 bucket in the following format:

`rudder-logs/sourceId/date/timestamp.sourceID.uuid.json.gz`

In this case:

  * `sourceId` corresponds to the source ID in the RudderStack dashboard. You can find it by going to the **Settings** tab within your source:

[![Source ID in RudderStack dashboard](/docs/images/event-stream-sources/sourceid.webp)](</docs/images/event-stream-sources/sourceid.webp>)

  * `date` corresponds to the upload date.
  * `timestamp` corresponds to upload timestamp.


> ![info](/docs/images/info.svg)
> 
> Note that the events within the file might not correspond to the same upload date.
> 
> For example, events from January 1, 2025 at 23:59 hrs might go into the next day’s file if the upload happens on that day, for example, on January 2, 2025 at 00:02 hrs.

### Delete a user

You can delete a user in S3 using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![warning](/docs/images/warning.svg)
> 
> While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with Amazon S3 if the request is fulfilled.

To delete a user, specify the `userId` in the event.A sample regulation request body for deleting a user in S3 is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": ["2FIKkByqn37FhzczP23eZmURciA"],
      "users": [
        {
          "userId": "1hKOmRA4GRlm",
          "<customKey>": "<customValue>"
        }
      ]
    }