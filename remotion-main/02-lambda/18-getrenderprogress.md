---
title: "getRenderProgress()"
url: "https://www.remotion.dev/docs/lambda/getrenderprogress"
path: "/docs/lambda/getrenderprogress"
---

"---\nimage: /generated/articles-docs-lambda-getrenderprogress.png\nid: getrenderprogress\ntitle: getRenderProgress()\nslug: /lambda/getrenderprogress\ncrumb: 'Lambda API'\n---\n\nGets the current status of a render initiated via [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda).  \nCalling this function results in a Lambda invocation.\n\nFor renders initiated via [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda), do not use this function. Instead, the result is returned immediately.\n\n## Example\n\n```tsx twoslash\nimport {getRenderProgress} from '@remotion/lambda/client';\n\nconst progress = await getRenderProgress({\n  renderId: 'd7nlc2y',\n  bucketName: 'remotionlambda-d9mafgx',\n  functionName: 'remotion-render-la8ffw',\n  region: 'us-east-1',\n});\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n:::note\nYou don't need to call this function while rendering a [still](/docs/still). Once you have obtained the [`renderId`](/docs/lambda/renderstillonlambda#renderid) from [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda), the render should already be done!\n:::\n\n## API\n\nCall the function by passing an object with the following properties:\n\n### `renderId`\n\nThe unique identifier for the render that you want to get the progress for. You can get the renderId from the return value of [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda).\n\n### `bucketName`\n\nThe bucket in which information about the render is saved. You can get the bucket name from the return value of [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda).\n\n### `region`\n\nThe region in which the Lambda function is located in.\n\n### `functionName`\n\nThe name of the function that triggered the render.\n\n### `customCredentials?`<AvailableFrom v=\"3.2.23\" />\n\nIf the render is going to be saved to a [different cloud](/docs/lambda/custom-destination#saving-to-another-cloud), pass an object with the same `endpoint`, `accessKeyId` and `secretAccessKey` as you passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#outname) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#outname).\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n### `skipLambdaInvocation?`<AvailableFrom v=\"4.0.218\" />\n\nInstead of calling a Lambda function which will get the progress from S3, make the S3 call directly.  \nThis is cheaper and faster, but the function name must follow [the function name convention](/docs/lambda/naming-convention#see-also).\n\n## Response\n\nReturns a promise resolving to an object with the following properties:\n\n### `overallProgress`\n\nA number between 0 and 1 indicating the approximate progress of the render.\n\n### `chunks`\n\nHow many chunks have been fully rendered so far.\n\n### `done`\n\n`true` if video has been successfully rendered and all processes are done. `false` otherwise.\n\n### `encodingStatus`\n\nEither `null` if not all chunks have been rendered yet or an object with the signature `{framesEncoded: number}` that tells how many frames have been encoded so far in the encoding process.\n\n### `renderId`\n\nMirrors the `renderId` that has been passed as an input\n\n### `renderMetadata`\n\nContains the following information about the render:\n\n- `frameRange`: The first and last frame that is being rendered (Use `frameRange[1] - frameRange[0] + 1` to get number of total frames rendered).\n- `startedDate`: Timestamp of when the rendering process started.\n- `totalChunks`: Into how many pieces the rendering is divided.\n- `estimatedTotalLambdaInvokations`: The estimated amount of total Lambda function calls in total, excluding calls to `getRenderProgress()`.\n- `estimatedRenderLambdaInvokations`: The estimated amount of Lambdas that will render chunks of the video.\n- `compositionId`: The ID of the composition that is being rendered.\n- `codec`: The selected codec into which the video gets encoded.\n- `dimensions`: The dimensions, with any `scale` applied, of the output video. (Available from v4.0.222)\n\n### `bucket`\n\nIn which bucket the render and other artifacts get saved.\n\n### `outputFile`\n\n`null` if the video is not yet rendered, a `string` containing a URL pointing to the final artifact if the video finished rendering.\n\n### `outKey`\n\n`null` if the video is not yet rendered, a `string` containing the S3 key where the final artifact is stored.\n\n### `timeToFinish`\n\n`null` is the video is not yet rendered, a `number` describing how long the render took to finish in milliseconds.\n\n### `errors`\n\nAn array which contains errors that occurred.\n\n### `fatalErrorEncountered`\n\n`true` if an error occurred and the video cannot be rendered. You should stop polling for progress and check the `errors` array.\n\n### `currentTime`\n\nThe current time at which the Lambda function responded to the progress request.\n\n### `renderSize`\n\nHow many bytes have been saved to the S3 bucket as a result of this render.  \nFrom v4.0.165, this might be slightly underreported as the `progress.json` file is not factored in.\n\n### `outputSizeInBytes`\n\n_available from v.3.3.9_\n\nThe size of the output artifact in bytes.\n\n### `lambdasInvoked`\n\nHow many lambdas that render a chunk have been invoked yet and have started rendering.\n\n### `framesRendered`\n\n_available from v3.3.8_\n\nHow many frames have been rendered so far, approximated to a number divisible by `5`.\n\n### `costs`\n\nAn object describing the costs of the render so far. The cost may increase if the render has not finished yet. Only costs for AWS Lambda are estimated, not for S3 storage. It is a best-effort estimation, but without any guarantees. The object has the following properties:\n\n- `accruedSoFar`: The cost as a floating number.\n- `currency`: The currency of the cost.\n- `displayCost`: The cost formatted as a string.\n- `disclaimer`: Textual disclaimer removing any doubt that there is no guarantee.\n\n### `estimatedBillingDurationInMilliseconds`<AvailableFrom v=\"4.0.74\"/>\n\nThe estimated total runtime of all invoked Lambda functions combined, in milliseconds. As the render goes on, this number increases.\n\n### `mostExpensiveFrameRanges`\n\nIf the render is in progress, this is `null`. If the render is done, it is an array of the 5 most expensive chunks in the following shape:\n\n- `chunk`: The index of the chunk (starting from 0)\n- `timeInMilliseconds`: The time it took the render that chunk\n- `frameRange`: A tuple containing the first and last frame that was rendered in that chunk.\n\n### `artifacts`<AvailableFrom v=\"4.0.176\"/>\n\nArtifacts that were created so far during the render. [See here for an example of dealing with field.](/docs/artifacts#using-rendermedia-renderstill-or-renderframes)\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-render-progress.ts)\n- [renderMediaOnLambda()](/docs/lambda/rendermediaonlambda)\n"

Gets the current status of a render initiated via [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda).

Calling this function results in a Lambda invocation.

For renders initiated via [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda), do not use this function. Instead, the result is returned immediately.

## Example[​](#example)

```
import {getRenderProgress} from '@remotion/lambda/client';

const progress = await getRenderProgress({
  renderId: 'd7nlc2y',
  bucketName: 'remotionlambda-d9mafgx',
  functionName: 'remotion-render-la8ffw',
  region: 'us-east-1',
});Copy
```

](#example)](#example)
](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)
- ](#example)