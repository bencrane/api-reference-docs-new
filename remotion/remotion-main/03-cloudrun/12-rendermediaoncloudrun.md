---
title: "renderMediaOnCloudrun()"
url: "https://www.remotion.dev/docs/cloudrun/rendermediaoncloudrun"
path: "/docs/cloudrun/rendermediaoncloudrun"
---

"---\nimage: /generated/articles-docs-cloudrun-rendermediaoncloudrun.png\nid: rendermediaoncloudrun\ntitle: renderMediaOnCloudrun()\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nKicks off a media rendering process on Remotion Cloud Run.\n\nRequires a [service](/docs/cloudrun/deployservice) to already be deployed to execute the render.  \nA [site](/docs/cloudrun/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {renderMediaOnCloudrun} from '@remotion/cloudrun/client';\n\nconst result = await renderMediaOnCloudrun({\n  region: 'us-east1',\n  serviceName: 'remotion-render-bds9aab',\n  composition: 'MyVideo',\n  serveUrl: 'https://storage.googleapis.com/remotioncloudrun-123asd321/sites/abcdefgh',\n  codec: 'h264',\n});\n\nif (result.type === 'success') {\n  console.log(result.bucketName);\n  console.log(result.renderId);\n}\n```\n\n:::note\nImport from [`@remotion/cloudrun/client`](/docs/cloudrun/light-client) to not load the whole renderer, which cannot be bundled.\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `cloudRunUrl?`\n\nRequired if `serviceName` not supplied. The url of the Cloud Run service which should be used to perform the render. You must set either `cloudRunUrl` or `serviceName`, but not both.\n\n### `serviceName?`\n\nRequired if `cloudRunUrl` not supplied. The name of the Cloud Run service which should be used to perform the render. This is used in conjunction with the region to determine the service endpoint, as the same service name can exist across multiple regions.\n\n### `region`\n\nIn which [GCP region](/docs/cloudrun/region-selection) your Cloud Run service is deployed. It's highly recommended that your Remotion site is also in the same region.\n\n### `serveUrl`\n\nA URL pointing to a Remotion project. Use [`deploySite()`](/docs/cloudrun/deploysite) to deploy a Remotion project.\n\n### `composition`\n\nThe `id` of the [composition](/docs/composition) you want to render.\n\n### `codec`\n\nWhich codec should be used to encode the video.\n\nVideo codecs `h264`, `vp8` and `prores` are supported.\n\nAudio codecs `mp3`, `aac` and `wav` are also supported.\n\nSee also [`renderMedia() -> codec`](/docs/renderer/render-media#codec).\n\n### `metadata?`<AvailableFrom v=\"4.0.216\" />\n\n<Options id=\"metadata\" />\n\n### `inputProps?`\n\n[Input Props to pass to the selected composition of your video.](/docs/passing-props#passing-input-props-in-the-cli).  \nMust be a JSON object.  \nFrom the root component the props can be read using [`getInputProps()`](/docs/get-input-props).  \nYou may transform input props using [`calculateMetadata()`](/docs/calculate-metadata).\n\n### `privacy?`\n\nOne of:\n\n- `\"public\"` (_default_): The rendered media is publicly accessible under the Cloud Storage URL.\n- `\"private\"`: The rendered media is not publicly available, but is available within the GCP project to those with the correct permissions.\n\n### `forceBucketName?`\n\nSpecify a specific bucket name to be used for the output. The resulting Google Cloud Storage URL will be in the format `gs://{bucket-name}/renders/{render-id}/{file-name}`. If not set, Remotion will choose the right bucket to use based on the region.\n\n### `updateRenderProgress?`\n\n```tsx twoslash\nimport type {UpdateRenderProgress} from '@remotion/cloudrun/client';\n\nconst updateRenderProgress: UpdateRenderProgress = (progress: number, error: boolean) => {\n  if (error) {\n    console.error('Render failed');\n  } else {\n    console.log(`Render progress: ${progress * 100}%`);\n  }\n};\n```\n\n### `renderStatusWebhook?`\n\nYour webhook URL that will be called with the progress of the render. This will be sent using a POST request.\n\n#### Arguments\n\n- `url`: The webhook URL endpoint.\n- `headers`: The headers to send. `Content-Type: application/json` is added automatically.\n- `data`: The data that you want to be sent alongside the progress data.\n- `webhookProgressInterval (optional)`: The interval at which the webhook is called. Defaults to 0.1 (10%). (min: 0.01, max: 1)\n\n```json title=\"Example Webhook URL Declaration\"\n{\n  \"url\": \"https://example.com/webhook\",\n  \"headers\": {\n    \"Authorization\": \"Bearer 1234567890\"\n  },\n  \"data\": {\n    \"projectId\": \"1234567890\"\n  },\n  \"webhookProgressInterval\": 0.1\n}\n```\n\n#### Example Webhook Response\n\n```json title=\"Example Webhook Response\"\n{\n  \"progress\": 0.1,\n  \"renderedFrames\": 100,\n  \"encodedFrames\": 100,\n  \"renderId\": \"1234567890\",\n  \"projectId\": \"1234567890\"\n}\n```\n\n### `renderIdOverride?`\n\nProvide a specific render ID for the render. Otherwise a random one will be generated.\n\n:::note\nYou will be responsible for ensuring that the render ID is unique, otherwise it will overwrite existing renders with the same configured Render ID.\n:::\n\n### `audioCodec?`\n\nChoose the encoding of your audio.\n\n- Choose `pcm-16` if you need uncompressed audio.\n- Not all video containers support all audio codecs.\n- This option takes precedence if the `codec` option also specifies an audio codec.\n\nRefer to the [Encoding guide](/docs/encoding/#audio-codec) to see defaults and supported combinations.\n\n### `jpegQuality?`\n\nSee [`renderMedia() -> jpegQuality`](/docs/renderer/render-media#jpegquality).\n\n### `audioBitrate?`\n\n<Options id=\"audio-bitrate\" />\n\n### `videoBitrate?`\n\n<Options id=\"video-bitrate\" />\n\n### `bufferSize?`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"buffer-size\" />\n\n### `maxRate?`<AvailableFrom v=\"4.0.78\" />\n\n<Options id=\"max-rate\" />\n\n### `proResProfile?`\n\nSee [`renderMedia() -> proResProfile`](/docs/renderer/render-media#proresprofile).\n\n### `x264Preset?`\n\n<Options id=\"x264-preset\" />\n\n### `crf?`\n\nSee [`renderMedia() -> crf`](/docs/renderer/render-media#crf).\n\n### `pixelFormat?`\n\nSee [`renderMedia() -> pixelFormat`](/docs/renderer/render-media#pixelformat).\n\n### `imageFormat?`\n\nSee [`renderMedia() -> imageFormat`](/docs/renderer/render-media#imageformat).\n\n### `scale?`\n\n<Options id=\"scale\" />\n\n### `everyNthFrame?`\n\nRenders only every nth frame. For example only every second frame, every third frame and so on. Only works for rendering GIFs. [See here for more details.](/docs/render-as-gif)\n\n### `numberOfGifLoops?`\n\n<Options id=\"number-of-gif-loops\" />\n\n### `downloadBehavior?`<AvailableFrom v=\"4.0.176\"/>\n\nHow the output file should behave when accessed through the Cloud Storage output link in the browser.\n\n- `{\"type\": \"play-in-browser\"}` - the default. The video will play in the browser.\n- `{\"type\": \"download\", fileName: null}` or `{\"type\": \"download\", fileName: \"download.mp4\"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.\n\n### `frameRange?`\n\nSpecify a single frame (a number) or a range of frames (a tuple [number, number]) to be rendered. Pass `[number, null]` to render from a frame to the end of the composition.<AvailableFrom v=\"4.0.421\" inline />\n\n### `envVariables?`\n\nSee [`renderMedia() -> envVariables`](/docs/renderer/render-media#envvariables).\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n#### `disableWebSecurity`\n\n_boolean - default `false`_\n\nThis will most notably disable CORS among other security features.\n\n#### `ignoreCertificateErrors`\n\n_boolean - default `false`_\n\nResults in invalid SSL certificates, such as self-signed ones, being ignored.\n\n#### `gl`\n\n<Options id=\"gl\" />\n\n### `muted?`\n\nDisables audio output. See also [`renderMedia() -> muted`](/docs/renderer/render-media#muted).\n\n### `forceWidth?`\n\nOverrides default composition width.\n\n### `forceHeight?`\n\nOverrides default composition height.\n\n### `forceFps?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition FPS.\n\n### `forceDurationInFrames?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition duration in frames.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\n### `outName?`\n\nThe file name of the media output.\n\nIt can either be:\n\n- `undefined` - it will default to `out` plus the appropriate file extension, for example: `renders/${renderId}/out.mp4`.\n- A `string` - it will get saved to the same Cloud Storage bucket as your site under the key `renders/{renderId}/{outName}`. Make sure to include the file extension at the end of the string.\n\n### `delayRenderTimeoutInMilliseconds?`\n\nA number describing how long the render may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout). Default: `30000`\n\n### `concurrency?`\n\nA number or a string describing how many browser tabs should be opened. Default \"50%\".\n\n:::note\nBefore v4.0.76, this was \"100%\" by default. It is now aligned to the other server-side rendering APIs.\n:::\n\n### `enforceAudioTrack?`\n\nRender a silent audio track if there wouldn't be any otherwise.\n\n### `preferLossless?`<AvailableFrom v=\"4.0.123\"/>\n\n<Options id=\"prefer-lossless\" />\n\n### `mediaCacheSizeInBytes?`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoCacheSizeInBytes?`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n### `colorSpace?`<AvailableFrom v=\"4.0.28\"/>\n\n<Options id=\"color-space\" />\n\n## Return value\n\nReturns a promise resolving to an object.\n\n### `type`\n\nUse this to determine the structure of the response. It can either be:\n\n- 'success' - render has been performed successfully.\n- 'crash - Cloud Run service has crashed.\n\n## Return when type === 'success'\n\nThe resulting object contains the following:\n\n### `type`\n\n'success' - render has been performed successfully.\n\n### `publicUrl?`\n\nThe publicly accessible URL of the rendered file. Only available when the request had the [`privacy`](/docs/cloudrun/rendermediaoncloudrun#privacy) property set to 'public'.\n\n### `renderId`\n\nA unique alphanumeric identifier for this render. Useful for obtaining status and finding the relevant files in the Cloud Storage bucket.\n\n### `bucketName`\n\nThe Cloud Storage bucket name in which all files are being saved.\n\n### `privacy`\n\nPrivacy of the output file, either:\n\n- \"public-read\" - Publicly accessible under the Cloud Storage URL.\n- \"project-private\" - Not publicly available, but is available within the GCP project to those with the correct permissions.\n\n### `publicUrl`\n\nIf the privacy is set to public, this will be the publicly accessible URL of the rendered file. If the privacy is not public, this will be null.\n\n### `cloudStorageUri`\n\nGoogle Storage path, beginning with `gs://{bucket-name}`. Can be used with the [gsutil](https://cloud.google.com/storage/docs/gsutil) CLI tool.\n\n### `size`\n\nSize of the rendered media in KB.\n\n## Return when type === 'crash'\n\nThe resulting object contains the following:\n\n### `type`\n\n'crash' - Cloud Run service has crashed without a response.\n\n### `cloudRunEndpoint`\n\nEndpoint that was called when executing the render. Used by the CLI to parse the service name to determine timeout and memory limit of the service. This can then be used when analysing the logs, to provide a hint as to the reason of the crash.\n\n### `message`\n\n'Service crashed without sending a response. Check the logs in GCP console.' This is used by the CLI for displaying an error message.\n\n### `requestStartTime`\n\ndatetime of when the request was made, in UTC format - \"2020-01-01T00:00:00+02:00\". Can be useful for filtering the logs of the service.\n\n### `requestCrashTime`\n\ndatetime of when the crash was detected, in UTC format - \"2020-01-01T00:00:00+02:00\". Can be useful for filtering the logs of the service.\n\n### `requestElapsedTimeInSeconds`\n\nSeconds elapsed between the request start and crash time. Can be checked against the timeout limit to understand if this was the likely cause of the crash.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/render-media-on-cloudrun.ts)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Kicks off a media rendering process on Remotion Cloud Run.

Requires a [service](/docs/cloudrun/deployservice) to already be deployed to execute the render.

A [site](/docs/cloudrun/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.

## Example[​](#example)

```
import {renderMediaOnCloudrun} from '@remotion/cloudrun/client';

const result = await renderMediaOnCloudrun({
  region: 'us-east1',
  serviceName: 'remotion-render-bds9aab',
  composition: 'MyVideo',
  serveUrl: 'https://storage.googleapis.com/remotioncloudrun-123asd321/sites/abcdefgh',
  codec: 'h264',
});

if (result.type === 'success') {
  console.log(result.bucketName);
  console.log(result.renderId);
}Copy
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
- ](#example)
- ](#example)
- ](#example)