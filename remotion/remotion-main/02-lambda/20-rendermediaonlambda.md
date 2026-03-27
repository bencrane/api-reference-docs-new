---
title: "renderMediaOnLambda()"
url: "https://www.remotion.dev/docs/lambda/rendermediaonlambda"
path: "/docs/lambda/rendermediaonlambda"
---

"---\nimage: /generated/articles-docs-lambda-rendermediaonlambda.png\nid: rendermediaonlambda\ntitle: renderMediaOnLambda()\ncrumb: 'Lambda API'\n---\n\nimport {MinimumFramesPerLambda} from '../../components/lambda/default-frames-per-lambda';\n\nKicks off a render process on Remotion Lambda. The progress can be tracked using [getRenderProgress()](/docs/lambda/getrenderprogress).\n\nRequires a [function](/docs/lambda/deployfunction) to already be deployed to execute the render.  \nA [site](/docs/lambda/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {renderMediaOnLambda} from '@remotion/lambda/client';\n\nconst {bucketName, renderId} = await renderMediaOnLambda({\n  region: 'us-east-1',\n  functionName: 'remotion-render-bds9aab',\n  composition: 'MyVideo',\n  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',\n  codec: 'h264',\n});\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nIn which region your Lambda function is deployed. It's highly recommended that your Remotion site is also in the same region.\n\n### `privacy?`\n\nOptional since <AvailableFrom v=\"3.2.27\" />.\n\nOne of:\n\n- `\"public\"` (_default_): The rendered media is publicly accessible under the S3 URL.\n- `\"private\"`: The rendered media is not publicly available, but signed links can be created using [presignUrl()](/docs/lambda/presignurl).\n- `\"no-acl\"` (_available from v.3.1.7_): The ACL option is not being set at all, this option is useful if you are writing to another bucket that does not support ACL using [`outName`](#outname).\n\n### `functionName`\n\nThe name of the deployed Lambda function.\nUse [`deployFunction()`](/docs/lambda/deployfunction) to create a new function and [`getFunctions()`](/docs/lambda/getfunctions) to obtain currently deployed Lambdas.\n\n### `framesPerLambda?`\n\nThe video rendering process gets distributed across multiple Lambda functions. This setting controls how many frames are rendered per Lambda invocation. The lower the number you pass, the more Lambdas get spawned.\n\nDefault value: [Dependant on video length](/docs/lambda/concurrency)  \nMinimum value: <MinimumFramesPerLambda />\n\n:::note\nThe `framesPerLambda` parameter cannot result in more than 200 functions being spawned. See: [Concurrency](/docs/lambda/concurrency)\n:::\n\n### `concurrency?`<AvailableFrom v=\"4.0.322\" />\n\nSpecify the number of Lambda functions to use for rendering. This is an alternative to `framesPerLambda` that allows you to set the concurrency directly without needing to know the video duration.\n\nThe concurrency is defined as `frameCount / framesPerLambda`. Remotion will automatically calculate the appropriate `framesPerLambda` value based on your concurrency setting.\n\nMaximum value: 200  \nMinimum value: Depends on video length (must result in `framesPerLambda >= 4`)\n\n:::note\nCannot be used together with `framesPerLambda`. Use only one of them.\n:::\n\n### `frameRange?`\n\nSpecify a single frame (passing a `number`) or a range of frames (passing a tuple `[number, number]`) to render a subset of a video. Example: `[0, 9]` to select the first 10 frames. By passing `null` (default) all frames of a composition get rendered. Pass `[number, null]` to render from a frame to the end of the composition.<AvailableFrom v=\"4.0.421\" inline /> To render a still, use [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).\n\n### `serveUrl`\n\nA URL pointing to a Remotion project. Use [`deploySite()`](/docs/lambda/deploysite) to deploy a Remotion project.\n\n### `composition`\n\nThe `id` of the [composition](/docs/composition) you want to render.\n\n### `metadata?`<AvailableFrom v=\"4.0.216\" />\n\n<Options id=\"metadata\" />\n\n### `inputProps?`\n\nOptional since <AvailableFrom v=\"3.2.27\" />.\n\n[Input Props to pass to the selected composition of your video.](/docs/passing-props#passing-input-props-in-the-cli).  \nMust be a JSON object.  \nFrom the root component the props can be read using [`getInputProps()`](/docs/get-input-props).  \nYou may transform input props using [`calculateMetadata()`](/docs/calculate-metadata).\n\n### `codec`\n\nWhich codec should be used to encode the video.\n\nVideo codecs `h264`, `h265`, `vp8`, `vp9`, `gif` and `prores` are supported.\n\nAudio codecs `mp3`, `aac` and `wav` are also supported.\n\n`av1` is not available on Lambda due to function size constraints.\n\nThe option `h264-mkv` has been renamed to just `h264` since `v3.3.34`. Use `h264` to get the same behavior.\n\nSee also [`renderMedia() -> codec`](/docs/renderer/render-media#codec).\n\n### `audioCodec?`<AvailableFrom v=\"3.3.41\" />\n\nChoose the encoding of your audio.\n\n- Each Lambda chunk might actually choose an uncompressed codec and convert it in the final encoding stage to prevent audio artifacts.\n- The default is dependent on the chosen `codec`.\n- Choose `pcm-16` if you need uncompressed audio.\n- Not all video containers support all audio codecs.\n- This option takes precedence if the `codec` option also specifies an audio codec.\n\nRefer to the [Encoding guide](/docs/encoding/#audio-codec) to see defaults and supported combinations.\n\n### `forceHeight?`<AvailableFrom v=\"3.2.40\" />\n\nOverrides default composition height.\n\n### `forceWidth?`<AvailableFrom v=\"3.2.40\" />\n\nOverrides default composition width.\n\n### `forceFps?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition FPS.\n\n### `forceDurationInFrames?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition duration in frames.\n\n### `muted?`\n\nDisables audio output. See also [`renderMedia() -> muted`](/docs/renderer/render-media#muted).\n\n### `imageFormat?`\n\nOptional since <AvailableFrom v=\"3.2.27\" />.\n\nSee [`renderMedia() -> imageFormat`](/docs/renderer/render-media#imageformat).\n\n### `crf?`\n\nSee [`renderMedia() -> crf`](/docs/renderer/render-media#crf).\n\n### `envVariables?`\n\nSee [`renderMedia() -> envVariables`](/docs/renderer/render-media#envvariables).\n\n### `pixelFormat?`\n\nSee [`renderMedia() -> pixelFormat`](/docs/renderer/render-media#pixelformat).\n\n### `proResProfile?`\n\nSee [`renderMedia() -> proResProfile`](/docs/renderer/render-media#proresprofile).\n\n### `x264Preset?`\n\n<Options id=\"x264-preset\" />\n\n### `jpegQuality?`\n\nSee [`renderMedia() -> jpegQuality`](/docs/renderer/render-media#jpegquality).\n\n### ~~`quality`~~\n\nRenamed to `jpegQuality` in v4.0.0.\n\n### `audioBitrate?`\n\n<Options id=\"audio-bitrate\" />\n\n### `videoBitrate?`\n\n<Options id=\"video-bitrate\" />\n\n### `bufferSize?`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"buffer-size\" />\n\n### `maxRate?`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"max-rate\" />\n\n### `maxRetries?`\n\nOptional since <AvailableFrom v=\"3.2.27\" />. Default: `1`.\n\nHow often a chunk may be retried to render in case the render fails.\nIf a rendering of a chunk is failed, the error will be reported in the [`getRenderProgress()`](/docs/lambda/getrenderprogress) object and retried up to as many times as you specify using this option.\n\n:::note\nA retry only gets executed if a the error is in the [list of flaky errors](https://github.com/remotion-dev/remotion/blob/main/packages/lambda-client/src/is-flaky-error.ts).\n:::\n\n### `scale?`\n\n<Options id=\"scale\" />\n\n### `outName?`\n\nThe file name of the media output.\n\nIt can either be:\n\n- `undefined` - it will default to `out` plus the appropriate file extension, for example: `renders/${renderId}/out.mp4`.\n- A `string` - it will get saved to the same S3 bucket as your site under the key `renders/{renderId}/{outName}`. Make sure to include the file extension at the end of the string.\n- An object if you want to render to a different bucket or cloud provider - [see here for detailed instructions](/docs/lambda/custom-destination).\n\n### `timeoutInMilliseconds?`\n\nA number describing how long the render may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout). Default: `30000`\n\n### `concurrencyPerLambda?`<AvailableFrom v=\"3.0.30\" />\n\nBy default, each Lambda function renders with concurrency 1 (one open browser tab). You may use the option to customize this value.\n\n### `everyNthFrame?`<AvailableFrom v=\"3.1\" />\n\nRenders only every nth frame. For example only every second frame, every third frame and so on. Only works for rendering GIFs. [See here for more details.](/docs/render-as-gif)\n\n### `numberOfGifLoops?`<AvailableFrom v=\"3.1\" />\n\n<Options id=\"number-of-gif-loops\" />\n\n### `downloadBehavior?`<AvailableFrom v=\"3.1.5\" />\n\nHow the output file should behave when accessed through the S3 output link in the browser.  \nEither:\n\n- `{\"type\": \"play-in-browser\"}` - the default. The video will play in the browser.\n- `{\"type\": \"download\", fileName: null}` or `{\"type\": \"download\", fileName: \"download.mp4\"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n#### `disableWebSecurity`\n\n_boolean - default `false`_\n\nThis will most notably disable CORS among other security features.\n\n#### `ignoreCertificateErrors`\n\n_boolean - default `false`_\n\nResults in invalid SSL certificates, such as self-signed ones, being ignored.\n\n#### `gl`\n\n<Options id=\"gl\" />\n\n### `overwrite?`<AvailableFrom v=\"3.2.25\" />\n\nIf a custom out name is specified and a file already exists at this key in the S3 bucket, decide whether the file should be overwritten. Default `false`.  \nIf the file exists and `overwrite` is `false`, an error will be thrown.\n\n### `rendererFunctionName?`<AvailableFrom v=\"3.3.38\" />\n\nIf specified, this function will be used for rendering the individual chunks. This is useful if you want to use a function with higher or lower power for rendering the chunks than the main orchestration function.\n\nIf you want to use this option, the function must be in the same region, the same account and have the same version as the main function.\n\n### `webhook?`<AvailableFrom v=\"3.2.30\" />\n\nIf specified, Remotion will send a POST request to the provided endpoint to notify your application when the Lambda rendering process finishes, errors out or times out.\n\n```tsx twoslash\nimport {RenderMediaOnLambdaInput} from '@remotion/lambda';\n\nconst webhook: RenderMediaOnLambdaInput['webhook'] = {\n  url: 'https://mapsnap.app/api/webhook',\n  secret: process.env.WEBHOOK_SECRET as string,\n  // Optionally pass up to 1024 bytes of custom data\n  customData: {\n    id: 42,\n  },\n};\n```\n\nIf you don't want to set up validation, you can set `secret` to null:\n\n```tsx twoslash\nimport {RenderMediaOnLambdaInput} from '@remotion/lambda';\n\nconst webhook: RenderMediaOnLambdaInput['webhook'] = {\n  url: 'https://mapsnap.app/api/webhook',\n  secret: null,\n};\n```\n\n[See here for detailed instructions on how to set up your webhook](/docs/lambda/webhooks).\n\n### `forceBucketName?`<AvailableFrom v=\"3.3.42\" />\n\nSpecify a specific bucket name to be used. [This is not recommended](/docs/lambda/multiple-buckets), instead let Remotion discover the right bucket automatically.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\nIf the `logLevel` is set to `verbose`, the Lambda function will not clean up artifacts, to aid debugging. Do not use it unless you are debugging a problem.\n\n### `mediaCacheSizeInBytes?`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoCacheSizeInBytes?`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads?`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `colorSpace?`<AvailableFrom v=\"4.0.28\"/>\n\n<Options id=\"color-space\" />\n\n### `deleteAfter?`<AvailableFrom v=\"4.0.32\"/>\n\n<Options id=\"delete-after\" />\n\n### `preferLossless?`<AvailableFrom v=\"4.0.123\"/>\n\n<Options id=\"prefer-lossless\" />\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n### `storageClass?`<AvailableFrom v=\"4.0.305\"/>\n\nAn [identifier](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare) for the S3 storage class of the rendered media. Default: `undefined` (which is `STANDARD`).\n\n### `licenseKey?`<AvailableFrom v=\"4.0.409\"/>\n\n<Options id=\"license-key\" />\n\n### `isProduction?`<AvailableFrom v=\"4.0.409\"/>\n\n_default `true`_\n\n<Options id=\"is-production\" />\n\n### ~~`apiKey?`<AvailableFrom v=\"4.0.253\"/>~~\n\n_deprecated in v4.0.409_\n\n<Options id=\"api-key\" />\n\n### ~~`dumpBrowserLogs?`~~\n\nDeprecated in v4.0 in favor of [`logLevel`](#loglevel).\n\n## Return value\n\nReturns a promise resolving to an object containing four properties. Of these, `renderId`, `bucketName` are useful for passing to `getRenderProgress()`.\n\n### `renderId`\n\nA unique alphanumeric identifier for this render. Useful for obtaining status and finding the relevant files in the S3 bucket.\n\n### `bucketName`\n\nThe S3 bucket name in which all files are being saved.\n\n### `cloudWatchLogs`<AvailableFrom v=\"3.2.10\"/>\n\nA link to CloudWatch (if you haven't disabled it) that you can visit to see the logs for the render.\n\n### `lambdaInsightsUrl`<AvailableFrom v=\"4.0.61\"/>\n\nA link to the [Lambda Insights](/docs/lambda/insights), if you enabled it.\n\n### `folderInS3Console`<AvailableFrom v=\"3.2.43\"/>\n\nA link to the folder in the AWS console where each chunk and render is located.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda-client/src/render-media-on-lambda.ts)\n- [getRenderProgress()](/docs/lambda/getrenderprogress)\n"

Kicks off a render process on Remotion Lambda. The progress can be tracked using [getRenderProgress()](/docs/lambda/getrenderprogress).

Requires a [function](/docs/lambda/deployfunction) to already be deployed to execute the render.

A [site](/docs/lambda/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.

## Example[​](#example)

```
import {renderMediaOnLambda} from '@remotion/lambda/client';

const {bucketName, renderId} = await renderMediaOnLambda({
  region: 'us-east-1',
  functionName: 'remotion-render-bds9aab',
  composition: 'MyVideo',
  serveUrl: 'https://remotionlambda-qg35eyp1s1.s3.eu-central-1.amazonaws.com/sites/bf2jrbfkw',
  codec: 'h264',
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