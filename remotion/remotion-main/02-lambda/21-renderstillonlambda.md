---
title: "renderStillOnLambda()"
url: "https://www.remotion.dev/docs/lambda/renderstillonlambda"
path: "/docs/lambda/renderstillonlambda"
---

"---\nimage: /generated/articles-docs-lambda-renderstillonlambda.png\nid: renderstillonlambda\ntitle: renderStillOnLambda()\nslug: /lambda/renderstillonlambda\ncrumb: 'Lambda API'\n---\n\nRenders a still image inside a lambda function and writes it to the specified output location.\n\nIf you want to render a video or audio instead, use [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) instead.\n\nIf you want to render a still locally instead, use [`renderStill()`](/docs/renderer/render-still) instead.\n\n## Example\n\n```tsx twoslash\n// @module: esnext\n// @target: es2017\nimport {renderStillOnLambda} from '@remotion/lambda/client';\n\nconst {estimatedPrice, url, sizeInBytes} = await renderStillOnLambda({\n  region: 'us-east-1',\n  functionName: 'remotion-render-bds9aab',\n  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',\n  composition: 'MyVideo',\n  inputProps: {},\n  imageFormat: 'png',\n  maxRetries: 1,\n  privacy: 'public',\n  envVariables: {},\n  frame: 10,\n});\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nIn which region your Lambda function is deployed. It's highly recommended that your Remotion site is also in the same region.\n\n### `functionName`\n\nThe name of the deployed Lambda function.\nUse [`deployFunction()`](/docs/lambda/deployfunction) to create a new function and [`getFunctions()`](/docs/lambda/getfunctions) to obtain currently deployed Lambdas.\n\n### `serveUrl`\n\nA URL pointing to a Remotion project. Use [`deploySite()`](/docs/lambda/deploysite) to deploy a Remotion project.\n\n### `composition`\n\nThe `id` of the [composition](/docs/composition) you want to render..\n\n### `inputProps`\n\n[Input Props to pass to the selected composition of your video.](/docs/passing-props#passing-input-props-in-the-cli).  \nMust be a JSON object.  \nFrom the root component the props can be read using [`getInputProps()`](/docs/get-input-props).  \nYou may transform input props using [`calculateMetadata()`](/docs/calculate-metadata).\n\n### `privacy`\n\nOne of:\n\n- `\"public\"` (_default_): The rendered still is publicly accessible under the S3 URL.\n- `\"private\"`: The rendered still is not publicly available, but signed links can be created using [presignUrl()](/docs/lambda/presignurl).\n- `\"no-acl\"` (_available from v.3.1.7_): The ACL option is not being set at all, this option is useful if you are writing to another bucket that does not support ACL using [`outName`](#outname).\n\n### `frame?`\n\nWhich frame of the composition should be rendered. Default: `0`. Frames are zero-indexed.\n\nFrom v3.2.27, negative values are allowed, with `-1` being the last frame.\n\n### `imageFormat?`\n\nSee [`renderStill() -> imageFormat`](/docs/renderer/render-still#imageformat). Default: `\"png\"`.\n\n### `onInit?`<AvailableFrom v=\"4.0.6\" />\n\nA callback function that gets called when the render starts, useful to obtain the link to the logs even if the render fails.\n\nIt receives an object with the following properties:\n\n- `renderId`: The ID of the render.\n- `cloudWatchLogs`: A link to the CloudWatch logs of the Lambda function, if you did not disable it.\n- `lambdaInsightsUrl`<AvailableFrom v=\"4.0.61\" />: A link to the [Lambda insights](/docs/lambda/insights), if you enabled it.\n\nExample usage:\n\n```tsx twoslash\n// @module: esnext\n// @target: es2022\n\nimport {renderStillOnLambda, RenderStillOnLambdaInput} from '@remotion/lambda/client';\n\nconst otherParameters: RenderStillOnLambdaInput = {\n  region: 'us-east-1',\n  functionName: 'remotion-render-bds9aab',\n  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',\n  composition: 'MyVideo',\n  inputProps: {},\n  imageFormat: 'png',\n  maxRetries: 1,\n  privacy: 'public',\n  envVariables: {},\n  frame: 10,\n};\nawait renderStillOnLambda({\n  ...otherParameters,\n  onInit: ({cloudWatchLogs, renderId, lambdaInsightsUrl}) => {\n    console.log(console.log(`Render invoked with ID = ${renderId}`));\n    console.log(`CloudWatch logs (if enabled): ${cloudWatchLogs}`);\n    console.log(`Lambda Insights (if enabled): ${lambdaInsightsUrl}`);\n  },\n});\n```\n\n### `jpegQuality?`\n\nSets the quality of the generated JPEG images. Must be an integer between 0 and 100. Default is to leave it up to the browser, [current default is 80](https://github.com/chromium/chromium/blob/99314be8152e688bafbbf9a615536bdbb289ea87/headless/lib/browser/protocol/headless_handler.cc#L32).\n\nOnly applies if `imageFormat` is `\"jpeg\"`, otherwise this option is invalid.\n\n### ~~`quality?`~~\n\nRenamed to `jpegQuality` in `v4.0.0`.\n\n### `maxRetries?`\n\nHow often a frame render may be retried until it fails. Default: `1`.\n\n:::note\nA retry only gets executed if a the error is in the [list of flaky errors](https://github.com/remotion-dev/remotion/blob/main/packages/lambda-client/src/is-flaky-error.ts).\n:::\n\n### `envVariables?`\n\nSee [`renderStill() -> envVariables`](/docs/renderer/render-still#envvariables). Default: `{}`.\n\n### `forceHeight?`<AvailableFrom v=\"3.2.40\" />\n\nOverrides the default composition height.\n\n### `forceWidth?`<AvailableFrom v=\"3.2.40\" />\n\nOverrides the default composition width.\n\n### `forceFps?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition FPS.\n\n### `forceDurationInFrames?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition duration in frames.\n\n### `scale?`\n\n<Options id=\"scale\" />\n\n### `outName?`\n\nIt can either be:\n\n- `undefined` - it will default to `out` plus the appropriate file extension, for example: `renders/${renderId}/out.mp4`.\n- A `string` - it will get saved to the same S3 bucket as your site under the key `renders/{renderId}/{outName}`. Make sure to include the file extension at the end of the string.\n- An object if you want to render to a different bucket or cloud provider - [see here for detailed instructions](/docs/lambda/custom-destination).\n\n### `timeoutInMilliseconds?`\n\nA number describing how long the render may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout). Default: `30000`\n\n### `downloadBehavior?`<AvailableFrom v=\"3.1.5\" />\n\nHow the output file should behave when accessed through the S3 output link in the browser.  \nEither:\n\n- `{\"type\": \"play-in-browser\"}` - the default. The video will play in the browser.\n- `{\"type\": \"download\", fileName: null}` or `{\"type\": \"download\", fileName: \"download.mp4\"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.\n\n### `mediaCacheSizeInBytes?`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoCacheSizeInBytes?`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads?`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `deleteAfter?`<AvailableFrom v=\"4.0.32\"/>\n\n<Options id=\"delete-after\" />\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n#### `disableWebSecurity`\n\n_boolean - default `false`_\n\nThis will most notably disable CORS among other security features.\n\n#### `ignoreCertificateErrors`\n\n_boolean - default `false`_\n\nResults in invalid SSL certificates, such as self-signed ones, being ignored.\n\n#### `gl`\n\n<Options id=\"gl\" />\n\n#### `userAgent`<AvailableFrom v=\"3.3.83\"/>\n\nLets you set a custom user agent that the headless Chrome browser assumes.\n\n#### `darkMode?`<AvailableFrom v=\"4.0.381\"/>\n\n<Options id=\"dark-mode\" />\n\n### `forceBucketName?`\n\nSpecify a specific bucket name to be used. [This is not recommended](/docs/lambda/multiple-buckets), instead let Remotion discover the right bucket automatically.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\nLogs can be read through the CloudWatch URL that this function returns.\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n### `storageClass?`<AvailableFrom v=\"4.0.305\"/>\n\nAn [identifier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare) for the S3 storage class of the rendered media. Default: `undefined` (which is `STANDARD`).\n\n### `licenseKey?`<AvailableFrom v=\"4.0.409\"/>\n\n<Options id=\"license-key\" />\n\n### `isProduction?`<AvailableFrom v=\"4.0.409\"/>\n\n_default `true`_\n\n<Options id=\"is-production\" />\n\n### ~~`dumpBrowserLogs?`~~\n\nDeprecated in v4.0 in favor of [`logLevel`](#loglevel).\n\n## Return value\n\nReturns a promise resolving to an object with the following properties:\n\n### `bucketName`\n\nThe S3 bucket in which the video was saved.\n\n### `url`\n\nAn AWS S3 URL where the output is available.\n\n### `outKey`<AvailableFrom v=\"4.0.141\" />\n\nThe S3 key where the output is saved.\n\n### `estimatedPrice`\n\nObject containing roughly estimated information about how expensive this operation was.\n\n### `sizeInBytes`\n\nThe size of the output image in bytes.\n\n### `renderId`\n\nA unique alphanumeric identifier for this render. Useful for obtaining status and finding the relevant files in the S3 bucket.\n\n### `cloudWatchLogs`<AvailableFrom v=\"3.2.10\" />\n\nA link to CloudWatch (if you haven't disabled it) that you can visit to see the logs for the render.\n\n### `artifacts`<AvailableFrom v=\"4.0.176\"/>\n\nArtifacts that were created so far during the render. [See here for an example of dealing with field.](/docs/artifacts#using-renderstillonlambda)\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/render-still-on-lambda.ts)\n- [renderMediaOnLambda()](/docs/lambda/rendermediaonlambda)\n- [renderStill()](/docs/renderer/render-still)\n"

Renders a still image inside a lambda function and writes it to the specified output location.

If you want to render a video or audio instead, use [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) instead.

If you want to render a still locally instead, use [`renderStill()`](/docs/renderer/render-still) instead.

## Example[​](#example)

```
import {renderStillOnLambda} from '@remotion/lambda/client';

const {estimatedPrice, url, sizeInBytes} = await renderStillOnLambda({
  region: 'us-east-1',
  functionName: 'remotion-render-bds9aab',
  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',
  composition: 'MyVideo',
  inputProps: {},
  imageFormat: 'png',
  maxRetries: 1,
  privacy: 'public',
  envVariables: {},
  frame: 10,
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