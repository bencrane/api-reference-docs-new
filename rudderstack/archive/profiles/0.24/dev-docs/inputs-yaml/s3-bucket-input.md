# Use Amazon S3 Bucket Data as Profiles Input Source

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Use Amazon S3 Bucket Data as Profiles Input Source

Use Amazon S3 bucket data stored in a CSV file format as an input source.

* * *

  * __3 minute read

  * 


> ![warning](/docs/images/warning.svg)
> 
> This is an experimental feature.

You can use data in your Amazon S3 bucket (**in a CSV file format**) as an input source in your Profiles project:
    
    
    name: s3_table
    app_defaults:
        s3: "s3://bucket-name/prefix/example.csv"
        occurred_at_col: insert_ts
        ids:
            - select: "id1"
              type: test_id
              entity: user
    

Make sure that the CSV file follows the standard format with the first row as the header containing column names, for example:
    
    
    ID1,ID2,ID3,INSERT_TS,NUM_A
    a,b,ex,2000-01-01T00:00:01Z,1
    D,e,ex,2000-01-01T00:00:01Z,3
    b,c,ex,2000-01-01T00:00:01Z,2
    NULL,d,ex,2000-01-01T00:00:01Z,4
    

Note that:

  * To escape comma (`,`) from any cell of the CSV file, enclose that cell with double quotes `" "` .
  * Double quotes (`" "`) enclosing a cell are ignored.


Follow the below steps to grant Profiles the required permissions to access the file in S3 Bucket:

## Private S3 bucket

Add `region`, `access key id`, `secret access key`, and `session token` in your `siteconfig` file so that Profiles can access the private bucket. By default, the region is set to `us-east-1` unless specified otherwise.
    
    
    aws_credential:
        region: us-east-1
        access_key: **********
        secret_access_key: **********
        session_token: **********
    

### Generate `access key id` and `secret access key`

  1. Open the AWS IAM console in your AWS account.
  2. Click **Policies**.
  3. Click **Create policy**.
  4. In the Policy editor section, click the JSON option.
  5. Replace the existing JSON policy with the following policy and replace the <bucket_name> with your actual bucket name:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion"
          ],
          "Resource": "arn:aws:s3:::<bucket_name>/*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "s3:ListBucket",
            "s3:GetBucketLocation"
          ],
          "Resource": "arn:aws:s3:::<bucket_name>",
          "Condition": {
            "StringLike": {
              "s3:prefix": [
                "*"
              ]
            }
          }
        }
      ]
    }
    

  6. Click **Review policy**.
  7. Enter the policy name. Then, click **Create policy**.


Further, create an IAM user by following the below steps:

> ![info](/docs/images/info.svg)
> 
> An IAM user requires the following permissions on an S3 bucket and folder to access files in the folder (and sub-folders):
> 
>   * s3:GetBucketLocation
>   * s3:GetObject
>   * s3:GetObjectVersion
>   * s3:ListBucket
> 


  1. In AWS IAM console, click **Users**.
  2. Click **Create user**.
  3. Enter a name for the user.
  4. Select Programmatic access as the access type, then click **Next: Permissions**.
  5. Click **Attach existing policies directly** , and select the policy you created earlier. Then, click **Next**.
  6. Review the user details, then click **Create user**.
  7. Copy the access key ID and secret access key values.


### Generate session token

  1. Use the AWS CLI to create a named profile with the AWS credentials that you copied in the previous step.
  2. To get the session token, run the following command:


    
    
     $ aws sts get-session-token --profile <named-profile>
    

See [Snowflake](<https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>), [Redshift](<https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-access-permissions.html>), and [Databricks](<https://docs.databricks.com/en/ingestion/copy-into/generate-temporary-credentials.html>) for more information.

## Public S3 Bucket

You **must** have the following permissions on the S3 bucket and folder to access files in the folder (and sub-folders):

  * s3:GetBucketLocation
  * s3:GetObject
  * s3:GetObjectVersion
  * s3:ListBucket


You can use the following policy in your bucket to grant the above permissions:

  1. Go to the **Permissions** tab of your S3 bucket.
  2. Edit bucket policy in **Permissions** tab and add the following policy. Replace the <bucket_name> with your actual bucket name:


    
    
    {
      "Version": "2012-10-17",
      "Statement": [{
          "Effect": "Allow",
          "Principal": "*",
          "Action": [
            "s3:GetObject",
            "s3:GetObjectVersion"
          ],
          "Resource": "arn:aws:s3:::<bucket_name>/*"
        },
        {
          "Effect": "Allow",
          "Principal": "*",
          "Action": [
            "s3:ListBucket",
            "s3:GetBucketLocation"
          ],
          "Resource": "arn:aws:s3:::<bucket_name>"
        }
      ]
    }
    

In Redshift, you additionally need to set an IAM role as **default** for your cluster, unless access keys are provided. It is necessary because more than one IAM role can be associated with the cluster and Redshift needs explicit permissions granted through an IAM role to access the S3 bucket (public or private).

Follow [Redshift Documentation](<https://docs.aws.amazon.com/redshift/latest/mgmt/default-iam-role.html#set-default-iam>) for setting an IAM role as default.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/dev-docs/inputs-yaml/identifiers/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/dev-docs/sql-model-yaml/>)