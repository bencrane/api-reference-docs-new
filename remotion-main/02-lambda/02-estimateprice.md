---
title: "estimatePrice()"
url: "https://www.remotion.dev/docs/lambda/estimateprice"
path: "/docs/lambda/estimateprice"
---

"---\nimage: /generated/articles-docs-lambda-estimateprice.png\nid: estimateprice\ntitle: estimatePrice()\nslug: /lambda/estimateprice\ncrumb: \"Lambda API\"\n---\n\nCalculates the AWS costs incurred for AWS Lambda given the region, execution duration and memory size based on the AWS Lambda pricing matrix.\n\nDuring rendering, many Lambda functions are spawned:\n\n- The main function spawns many worker functions, waits for chunks to be rendered, and stitches them together for the full video. This is the longest-running Lambda function.\n- Render functions render a short portion of a video and then shut down.\n- Other short-lived, negligible functions get launched for initializing lambdas and fetching progress.\n\nThe total duration is the sum of execution duration of all of the above Lambda functions.\nThis duration can be passed to `estimatePrice()` to estimate the cost of AWS Lambda.\n\nThe calculated duration does not include costs for S3 and Remotion licensing fees.\n\n## Example\n\n```ts twoslash\nimport { estimatePrice } from \"@remotion/lambda\";\n\nconsole.log(\n  estimatePrice({\n    region: \"us-east-1\",\n    durationInMilliseconds: 20000,\n    memorySizeInMb: 2048,\n    diskSizeInMb: 2048,\n    lambdasInvoked: 1,\n  })\n); // 0.00067\n```\n\n## Arguments\n\nAn object containing the following parameters:\n\n### `region`\n\nThe region in which the Lambda function is executed in. [Pricing varies across regions](/docs/lambda/region-selection#other-considerations).\n\n### `memorySizeInMb`\n\nThe amount of memory that has been given to the Lambda function. May be received with [`getFunctionInfo()`](/docs/lambda/getfunctioninfo).\n\n### `durationInMilliseconds`\n\nThe estimated total execution duration in Milliseconds of all Lambdas combined. See the top of this page for a guide on how to approximate the duration.\n\n### `lambdasInvoked`\n\nThe number of lambdas that were invoked in the rendering process.\n\n### `diskSizeInMb`\n\nThe amount of disk space allocated in megabytes.\n\n## Return value\n\nThe estimated cost in USD as a `number`.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)\n"

Calculates the AWS costs incurred for AWS Lambda given the region, execution duration and memory size based on the AWS Lambda pricing matrix.

During rendering, many Lambda functions are spawned:

- The main function spawns many worker functions, waits for chunks to be rendered, and stitches them together for the full video. This is the longest-running Lambda function.

- Render functions render a short portion of a video and then shut down.

- Other short-lived, negligible functions get launched for initializing lambdas and fetching progress.

The total duration is the sum of execution duration of all of the above Lambda functions.
This duration can be passed to `estimatePrice()` to estimate the cost of AWS Lambda.

The calculated duration does not include costs for S3 and Remotion licensing fees.

## Example[​](#example)

```
import { estimatePrice } from "@remotion/lambda";

console.log(
  estimatePrice({
    region: "us-east-1",
    durationInMilliseconds: 20000,
    memorySizeInMb: 2048,
    diskSizeInMb: 2048,
    lambdasInvoked: 1,
  })
); // 0.00067Copy
```

## Arguments[​](#arguments)

An object containing the following parameters:

### `region`[​](#region)

The region in which the Lambda function is executed in. [Pricing varies across regions](/docs/lambda/region-selection#other-considerations).

### `memorySizeInMb`[​](#memorysizeinmb)

The amount of memory that has been given to the Lambda function. May be received with [`getFunctionInfo()`](/docs/lambda/getfunctioninfo).

### `durationInMilliseconds`[​](#durationinmilliseconds)

The estimated total execution duration in Milliseconds of all Lambdas combined. See the top of this page for a guide on how to approximate the duration.

### `lambdasInvoked`[​](#lambdasinvoked)

The number of lambdas that were invoked in the rendering process.

### `diskSizeInMb`[​](#disksizeinmb)

The amount of disk space allocated in megabytes.

## Return value[​](#return-value)

The estimated cost in USD as a `number`.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/estimate-price.ts)