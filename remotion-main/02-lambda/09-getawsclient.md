---
title: "getAwsClient()"
url: "https://www.remotion.dev/docs/lambda/getawsclient"
path: "/docs/lambda/getawsclient"
---

"---\nimage: /generated/articles-docs-lambda-getawsclient.png\nid: getawsclient\ntitle: getAwsClient()\ncrumb: 'Lambda API'\n---\n\nThis API exposes full access to the AWS SDK that Remotion uses under the hood. You can use it to interact with your AWS infrastructure in ways that Remotion doesn't provide a function for.\n\n## Example: Getting a buffer for a render\n\n```tsx {19-28}\n// Import from \"@remotion/lambda\" instead before Remotion v4.0.60\nimport {getAwsClient, getRenderProgress} from '@remotion/lambda/client';\nimport {Readable} from 'stream';\n\nconst bucketName = 'remotionlambda-d9mafgx';\n\nconst getFileAsBuffer = async () => {\n  const progress = await getRenderProgress({\n    renderId: 'd7nlc2y',\n    bucketName: 'remotionlambda-d9mafgx',\n    functionName: 'remotion-render-la8ffw',\n    region: 'us-east-1',\n  });\n\n  if (!progress.outKey) {\n    // Video not yet rendered\n    return;\n  }\n\n  const {client, sdk} = getAwsClient({region: 'us-east-1', service: 's3'});\n\n  const data = client.send(\n    new sdk.GetObjectCommand({\n      Bucket: bucketName,\n      Key: progress.outKey,\n    }),\n  );\n\n  return data.Body as Readable;\n};\n```\n\n## Example: Enable CORS for a bucket\n\n```tsx\n// Import from \"@remotion/lambda\" instead before Remotion v4.0.60\nimport {getAwsClient} from '@remotion/lambda/client';\n\nconst {client, sdk} = getAwsClient({region: 'us-east-1', service: 's3'});\n\nclient.send(\n  new sdk.PutBucketCorsCommand({\n    Bucket: '[bucket-name]',\n    CORSConfiguration: {\n      CORSRules: [\n        {\n          AllowedMethods: ['GET', 'HEAD'],\n          AllowedHeaders: ['*'],\n          AllowedOrigins: ['*'],\n        },\n      ],\n    },\n  }),\n);\n```\n\n## Arguments\n\nAn object with two mandatory parameters:\n\n### `region`\n\nOne of the [supported regions](/docs/lambda/region-selection) of Remotion Lambda, for which the client should be instantiated.\n\n### `service`\n\nOne of `lambda`, `cloudwatch`, `iam`, `servicequotas`, `s3` or `sts`.\n\n### `customCredentials?`<AvailableFrom v=\"3.2.23\" />\n\nAllows you to connect to another cloud provider, useful if you [render your output to a different cloud](/docs/lambda/custom-destination). The value must satisfy the following type:\n\n```ts\ntype CustomCredentials = {\n  endpoint: string;\n  accessKeyId: string | null;\n  secretAccessKey: string | null;\n  region?: string;\n  forcePathStyle?: boolean;\n};\n```\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n## Return value\n\nAn object with two properties:\n\n### client\n\nAn AWS SDK client instantiated with the region you passed and the credentials you had set at the time of calling the function.\n\n- For `s3`: An instance of [S3Client](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/s3client.html)\n- For `iam`: An instance of [IAMClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-iam/classes/iamclient.html)\n- For `cloudwatch`: An instance of [CloudWatchLogsClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-cloudwatch-logs/classes/cloudwatchlogsclient.html)\n- For `servicequotas`: An instance of [ServiceQuotasClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-service-quotas/classes/servicequotasclient.html)\n- For `lambda`: An instance of [LambdaClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/classes/lambdaclient.html)\n\n### sdk\n\nThe full SDK JavaScript module for the service you specified.\n\n- For `s3`: The [`@aws-sdk/client-s3`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/index.html#aws-sdkclient-s3) package\n- For `iam`: The [`@aws-sdk/client-iam`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-iam/index.html#aws-sdkclient-iam) package\n- For `cloudwatch`: The [`@aws-sdk/client-cloudwatch-logs`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-cloudwatch-logs/index.html#aws-sdkclient-cloudwatch-logs) package\n- For `servicequotas`: The [`@aws-sdk/client-service-quotas`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-service-quotas/index.html) package\n- For `lambda`: The [`@aws-sdk/client-lambda`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda) package\n\n:::note\nYou don't need to create a new client from the SDK and should instead reuse the `client` that is also returned and being used by Remotion, in order to save memory.\n:::\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-aws-client.ts)\n- [Light client](/docs/lambda/light-client)\n"

This API exposes full access to the AWS SDK that Remotion uses under the hood. You can use it to interact with your AWS infrastructure in ways that Remotion doesn't provide a function for.

## Example: Getting a buffer for a render[​](#example-getting-a-buffer-for-a-render)

```
// Import from "@remotion/lambda" instead before Remotion v4.0.60
import {getAwsClient, getRenderProgress} from '@remotion/lambda/client';
import {Readable} from 'stream';

const bucketName = 'remotionlambda-d9mafgx';

const getFileAsBuffer = async () => {
  const progress = await getRenderProgress({
    renderId: 'd7nlc2y',
    bucketName: 'remotionlambda-d9mafgx',
    functionName: 'remotion-render-la8ffw',
    region: 'us-east-1',
  });

  if (!progress.outKey) {
    // Video not yet rendered
    return;
  }

  const {client, sdk} = getAwsClient({region: 'us-east-1', service: 's3'});

  const data = client.send(
    new sdk.GetObjectCommand({
      Bucket: bucketName,
      Key: progress.outKey,
    }),
  );

  return data.Body as Readable;
};Copy
```

## Example: Enable CORS for a bucket[​](#example-enable-cors-for-a-bucket)

```
// Import from "@remotion/lambda" instead before Remotion v4.0.60
import {getAwsClient} from '@remotion/lambda/client';

const {client, sdk} = getAwsClient({region: 'us-east-1', service: 's3'});

client.send(
  new sdk.PutBucketCorsCommand({
    Bucket: '[bucket-name]',
    CORSConfiguration: {
      CORSRules: [
        {
          AllowedMethods: ['GET', 'HEAD'],
          AllowedHeaders: ['*'],
          AllowedOrigins: ['*'],
        },
      ],
    },
  }),
);Copy
```

## Arguments[​](#arguments)

An object with two mandatory parameters:

### `region`[​](#region)

One of the [supported regions](/docs/lambda/region-selection) of Remotion Lambda, for which the client should be instantiated.

### `service`[​](#service)

One of `lambda`, `cloudwatch`, `iam`, `servicequotas`, `s3` or `sts`.

### `customCredentials?`[v3.2.23](https://github.com/remotion-dev/remotion/releases/v3.2.23)[​](#customcredentials)

Allows you to connect to another cloud provider, useful if you [render your output to a different cloud](/docs/lambda/custom-destination). The value must satisfy the following type:

```
type CustomCredentials = {
  endpoint: string;
  accessKeyId: string | null;
  secretAccessKey: string | null;
  region?: string;
  forcePathStyle?: boolean;
};Copy
```

### `forcePathStyle?`[v4.0.202](https://github.com/remotion-dev/remotion/releases/v4.0.202)[​](#forcepathstyle)

Passes `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.

## Return value[​](#return-value)

An object with two properties:

### client[​](#client)

An AWS SDK client instantiated with the region you passed and the credentials you had set at the time of calling the function.

- For `s3`: An instance of [S3Client](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/s3client.html)

- For `iam`: An instance of [IAMClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-iam/classes/iamclient.html)

- For `cloudwatch`: An instance of [CloudWatchLogsClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-cloudwatch-logs/classes/cloudwatchlogsclient.html)

- For `servicequotas`: An instance of [ServiceQuotasClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-service-quotas/classes/servicequotasclient.html)

- For `lambda`: An instance of [LambdaClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/classes/lambdaclient.html)

### sdk[​](#sdk)

The full SDK JavaScript module for the service you specified.

- For `s3`: The [`@aws-sdk/client-s3`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/index.html#aws-sdkclient-s3) package

- For `iam`: The [`@aws-sdk/client-iam`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-iam/index.html#aws-sdkclient-iam) package

- For `cloudwatch`: The [`@aws-sdk/client-cloudwatch-logs`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-cloudwatch-logs/index.html#aws-sdkclient-cloudwatch-logs) package

- For `servicequotas`: The [`@aws-sdk/client-service-quotas`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-service-quotas/index.html) package

- For `lambda`: The [`@aws-sdk/client-lambda`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda) package

](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)
- ](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-lambda/index.html#aws-sdkclient-lambda)