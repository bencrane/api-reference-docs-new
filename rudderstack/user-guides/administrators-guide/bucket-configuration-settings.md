# Bucket Configuration Settings for Event Backups

Configure cloud-specific buckets for your event backups.

* * *

  * __3 minute read

  * 


Depending on your [data retention policy](<https://www.rudderstack.com/docs/dashboard-guides/data-management/>), RudderStack stores the raw events ingested by RudderStack, including [gateway dumps](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#non-transient-customer-data>) for successfully-ingested events.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack deletes the events from the bucket upon successful delivery.
>   * RudderStack **does not persist** any of the customer data.
> 


Follow the steps in this guide if you want RudderStack to back up the events in your **own** cloud-specific bucket.

## Bucket configuration settings

If you are using [RudderStack Open Source](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/>) and want to use your own bucket to store the events, you need to enable and set certain variables in your RudderStack backend.

### Docker setup

> ![warning](/docs/images/warning.svg)
> 
> The S3 setup for event backup and replay is different to [setting up Amazon S3 as a destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>).

To store the events in your S3 bucket, uncomment the following lines in your [docker.env](<https://github.com/rudderlabs/rudder-server/blob/master/build/docker.env#L45-L50>) file:
    
    
    # JOBS_BACKUP_STORAGE_PROVIDER=S3
    # JOBS_BACKUP_BUCKET=<YOUR_S3_BUCKET>
    # JOBS_BACKUP_PREFIX=<prefix>
    # AWS_ACCESS_KEY_ID=
    # AWS_SECRET_ACCESS_KEY=
    

Then, follow these steps:

  1. Specify your S3 bucket name for the variable `JOBS_BACKUP_BUCKET`.
  2. Add the specific AWS IAM keys by following the Permissions for Amazon S3 section.


> ![info](/docs/images/info.svg)
> 
> The `<prefix>` value for the `JOBS_BACKUP_PREFIX` variable is the location in the S3 bucket where RudderStack stores the data.
> 
> For example, if `JOBS_BACKUP_PREFIX` is set to `ABC` then RudderStack stores the data in the location `<YOUR_S3_BUCKET>/ABC`.

To store the events in your GCS bucket, uncomment the following lines in your [docker.env](<https://github.com/rudderlabs/rudder-server/blob/master/build/docker.env#L45-L50>) file:
    
    
    # JOBS_BACKUP_STORAGE_PROVIDER=GCS
    # JOBS_BACKUP_BUCKET=<your_gcs_bucket>
    # JOBS_BACKUP_PREFIX=<prefix>
    # GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials
    

Then, follow these steps:

  1. Specify your GCS bucket name for the variable `JOBS_BACKUP_BUCKET`.
  2. Specify the location of the downloaded JSON file containing the required permissions for the variable `GOOGLE_APPLICATION_CREDENTIALS`. You can obtain the JSON file by referring to the Permissions for GCS section below.


> ![info](/docs/images/info.svg)
> 
> If you’re a RudderStack Growth/Enterprise user, you can share the downloaded JSON containing the required permissions with the [RudderStack team](<mailto:support@rudderstack.com>).
> 
> The RudderStack team will then use this service account JSON file to authenticate RudderStack and dump the events into your GCS bucket.

### Kubernetes setup

Similar to the Docker setup, you can configure your bucket settings by changing the values in the [values.yaml](<https://github.com/rudderlabs/rudderstack-helm/blob/master/values.yaml#L87>) file.

## Permissions for Amazon S3

Follow these steps to use your own S3 bucket for RudderStack to store the events:

  1. Create a new [S3](<https://aws.amazon.com/s3/>) bucket.
  2. Create a new [customer-managed policy](<https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html>) with the following JSON:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket",
          "s3:ListObjectsV2",
          "s3:AbortMultipartUpload"
        ],
        "Resource": [
          "arn:aws:s3:::{YOUR_S3_BUCKET_NAME}/*",
          "arn:aws:s3:::{YOUR_S3_BUCKET_NAME}"
        ]
      }]
    }
    

  3. Create a new group and add the above policy to this group.
  4. Create a new [user](<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>) in [Identity and Access Management (IAM)](<https://console.aws.amazon.com/iam>) with programmatic access and add the user to the above group.
  5. Download the **Access key ID** and **Secret Access Key**.
  6. Specify the credentials during the S3 bucket configuration.


## Permissions for GCS

This section lists the steps to use your own GCS bucket for RudderStack to store the events:

Under **Roles** in your GCP dashboard, create a role with the below permissions:

  * **storage.objects.create**
  * **storage.objects.get**
  * **storage.objects.list**


> ![warning](/docs/images/warning.svg)
> 
> Make sure to add the permissions one after the other.

[![](/docs/images/admin-guides/gcp-role-permissions.webp)](</docs/images/admin-guides/gcp-role-permissions.webp>)

### Create a service account

  1. Assign a name to the service account:

[![Assign a name](/docs/images/screenshot-2020-08-05-at-11.40.12-am%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%281%29.webp)](</docs/images/screenshot-2020-08-05-at-11.40.12-am%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%282%29%20%281%29.webp>)

  2. Add the role you created above.

[![](/docs/images/screenshot-2020-08-05-at-11.41.24-am.webp)](</docs/images/screenshot-2020-08-05-at-11.41.24-am.webp>)

  3. Create a key of JSON type and save this file locally:

[![Create a key](/docs/images/screenshot-2020-08-05-at-11.49.10-am.webp)](</docs/images/screenshot-2020-08-05-at-11.49.10-am.webp>)

  4. Create a bucket with the bucket access control set to **Uniform** :

[![Create a bucket](/docs/images/screenshot-2020-08-05-at-11.52.07-am.webp)](</docs/images/screenshot-2020-08-05-at-11.52.07-am.webp>)

Add the required permissions to your GCS bucket by following the below steps:

  1. Go to the **Permissions** tab.
  2. Add the member with the service account created above.
  3. Add the role.

[![Go to Permissions](/docs/images/screenshot-2020-08-05-at-11.53.34-am.webp)](</docs/images/screenshot-2020-08-05-at-11.53.34-am.webp>)

  4. Download the JSON file containing the required permissions.
  5. Specify the JSON file location during the GCS bucket configuration.