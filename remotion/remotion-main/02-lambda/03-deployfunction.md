---
title: "deployFunction()"
url: "https://www.remotion.dev/docs/lambda/deployfunction"
path: "/docs/lambda/deployfunction"
---

"---\nimage: /generated/articles-docs-lambda-deployfunction.png\nid: deployfunction\ntitle: deployFunction()\nslug: /lambda/deployfunction\ncrumb: 'Lambda API'\n---\n\nCreates an [AWS Lambda](https://aws.amazon.com/lambda/) function in your AWS account that will be able to render a video in the cloud.\n\nIf a function with the same version, memory size and timeout already existed, it will be returned instead without a new one being created. This means this function can be treated as idempotent.\n\n## Example\n\n```ts twoslash\nimport {deployFunction} from '@remotion/lambda';\n\nconst {functionName} = await deployFunction({\n  region: 'us-east-1',\n  timeoutInSeconds: 120,\n  memorySizeInMb: 2048,\n  createCloudWatchLogGroup: true,\n  diskSizeInMb: 2048,\n});\nconsole.log(functionName);\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) which you want to deploy the Lambda function too. It must be the same region that your Lambda Layer resides in.\n\n### `timeoutInSeconds`\n\nHow long the Lambda function may run before it gets killed. Must be below 900 seconds.\nWe recommend a timeout of 120 seconds or lower - remember, Remotion Lambda is the fastest if you render with a high concurrency. If your video takes longer to render, the concurrency should be increased rather than the timeout.\n\n### `memorySizeInMb`\n\nHow many megabytes of RAM the Lambda function should have. By default we recommend a value of 2048MB. You may increase or decrease it depending on how memory-consuming your video is. The minimum allowed number is `512`, the maximum allowed number is `10240`. Since the costs of Remotion Lambda is directly proportional to the amount of RAM, we recommend to keep this amount as low as possible.\n\n### `createCloudWatchLogGroup?`\n\nWhether logs should be saved into CloudWatch. We recommend enabling this option.\n\n### `cloudWatchLogRetentionPeriodInDays?`\n\nRetention period for the CloudWatch Logs. Default: 14 days.\n\n### `diskSizeInMb?`\n\nSets the amount of disk storage that is available in the Lambda function. Must be between 512MB and 10240MB (10GB). Set this higher if you want to render longer videos. See also: [Disk size](/docs/lambda/disk-size)\n\n| Remotion Version | Default |\n| ---------------- | ------- |\n| &lt;5.0.0        | 2048MB  |\n| &gt;=5.0.0       | 10240MB |\n\n### `customRoleArn?`\n\nUse a custom role for the function instead of the default (`arn:aws:iam::[aws-account-id]:role/remotion-lambda-role`)\n\n### `enableLambdaInsights?`<AvailableFrom v=\"4.0.61\" />\n\n<Options id=\"enable-lambda-insights\" />\n\n### `runtimePreference?`<AvailableFrom v=\"4.0.205\" />\n\nOne of:\n\n- `default`: Currently resolving to `cjk`\n- `apple-emojis`: Use Apple Emojis instead of Google Emojis. CJK characters will be removed.\n- `cjk`: Include CJK (Chinese, Japanese, Korean) characters and Google Emojis. Apple Emojis will be removed.\n\n:::note\nApple Emojis are intellectual property of Apple Inc.  \nYou are responsible for the use of Apple Emojis in your project.\n:::\n\n## Return value\n\nAn object with the following values:\n\n- `functionName` (_string_): The name of the function just created.\n- `alreadyExisted`: (_boolean_): Whether the creation was skipped because the function already existed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/deploy-function.ts)\n- [CLI equivalent: `npx remotion lambda functions deploy`](/docs/lambda/cli/functions/deploy)\n- [`deleteFunction()`](/docs/lambda/deletefunction)\n- [`getFunctions()`](/docs/lambda/getfunctions)\n"

Creates an [AWS Lambda](https://aws.amazon.com/lambda/) function in your AWS account that will be able to render a video in the cloud.

If a function with the same version, memory size and timeout already existed, it will be returned instead without a new one being created. This means this function can be treated as idempotent.

## Example[​](#example)

```
import {deployFunction} from '@remotion/lambda';

const {functionName} = await deployFunction({
  region: 'us-east-1',
  timeoutInSeconds: 120,
  memorySizeInMb: 2048,
  createCloudWatchLogGroup: true,
  diskSizeInMb: 2048,
});
console.log(functionName);Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) which you want to deploy the Lambda function too. It must be the same region that your Lambda Layer resides in.

### `timeoutInSeconds`[​](#timeoutinseconds)

How long the Lambda function may run before it gets killed. Must be below 900 seconds.
We recommend a timeout of 120 seconds or lower - remember, Remotion Lambda is the fastest if you render with a high concurrency. If your video takes longer to render, the concurrency should be increased rather than the timeout.

### `memorySizeInMb`[​](#memorysizeinmb)

How many megabytes of RAM the Lambda function should have. By default we recommend a value of 2048MB. You may increase or decrease it depending on how memory-consuming your video is. The minimum allowed number is `512`, the maximum allowed number is `10240`. Since the costs of Remotion Lambda is directly proportional to the amount of RAM, we recommend to keep this amount as low as possible.

### `createCloudWatchLogGroup?`[​](#createcloudwatchloggroup)

Whether logs should be saved into CloudWatch. We recommend enabling this option.

### `cloudWatchLogRetentionPeriodInDays?`[​](#cloudwatchlogretentionperiodindays)

Retention period for the CloudWatch Logs. Default: 14 days.

### `diskSizeInMb?`[​](#disksizeinmb)

Sets the amount of disk storage that is available in the Lambda function. Must be between 512MB and 10240MB (10GB). Set this higher if you want to render longer videos. See also: [Disk size](/docs/lambda/disk-size)

|  Remotion Version Default
|  <5.0.0 2048MB
|  >=5.0.0 10240MB

### `customRoleArn?`[​](#customrolearn)

Use a custom role for the function instead of the default (`arn:aws:iam::[aws-account-id]:role/remotion-lambda-role`)

### `enableLambdaInsights?`[v4.0.61](https://github.com/remotion-dev/remotion/releases/v4.0.61)[​](#enablelambdainsights)

Enable [Lambda Insights in AWS CloudWatch](https://remotion.dev/docs/lambda/insights). For this to work, you may have to update your role permission.

### `runtimePreference?`[v4.0.205](https://github.com/remotion-dev/remotion/releases/v4.0.205)[​](#runtimepreference)

One of:

- `default`: Currently resolving to `cjk`

- `apple-emojis`: Use Apple Emojis instead of Google Emojis. CJK characters will be removed.

- `cjk`: Include CJK (Chinese, Japanese, Korean) characters and Google Emojis. Apple Emojis will be removed.

](#runtimepreference)](#runtimepreference)
](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)
- ](#runtimepreference)