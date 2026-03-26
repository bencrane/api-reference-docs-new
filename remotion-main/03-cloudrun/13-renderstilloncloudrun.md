---
title: "renderStillOnCloudrun()"
url: "https://www.remotion.dev/docs/cloudrun/renderstilloncloudrun"
path: "/docs/cloudrun/renderstilloncloudrun"
---

"---\nimage: /generated/articles-docs-cloudrun-renderstilloncloudrun.png\nid: renderstilloncloudrun\ntitle: renderStillOnCloudrun()\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nKicks off a still rendering process on Remotion Cloud Run.\n\nRequires a [service](/docs/cloudrun/deployservice) to already be deployed to execute the render.  \nA [site](/docs/cloudrun/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.\n\n## Example\n\n```tsx twoslash\n// ---cut---\nimport {renderStillOnCloudrun} from '@remotion/cloudrun/client';\n\nconst result = await renderStillOnCloudrun({\n  region: 'us-east1',\n  serviceName: 'remotion-render-bds9aab',\n  composition: 'MyStill',\n  imageFormat: 'png',\n  serveUrl: 'https://storage.googleapis.com/remotioncloudrun-123asd321/sites/abcdefgh',\n});\n\nif (result.type === 'success') {\n  console.log(result.bucketName);\n  console.log(result.renderId);\n}\n```\n\n:::note\nImport from [`@remotion/cloudrun/client`](/docs/cloudrun/light-client) to not load the whole renderer, which cannot be bundled.\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `cloudRunUrl?`\n\nRequired if `serviceName` not supplied. The url of the Cloud Run service which should be used to perform the render. You must set either `cloudRunUrl` or `serviceName`, but not both.\n\n### `serviceName?`\n\nRequired if `cloudRunUrl` not supplied. The name of the Cloud Run service which should be used to perform the render. This is used in conjunction with the region to determine the service endpoint, as the same service name can exist across multiple regions.\n\n### `metadata?`<AvailableFrom v=\"4.0.216\" />\n\n<Options id=\"metadata\" />\n\n### `region`\n\nIn which [GCP region](/docs/cloudrun/region-selection) your Cloud Run service is deployed. It's highly recommended that your Remotion site is also in the same region.\n\n### `serveUrl`\n\nA URL pointing to a Remotion project. Use [`deploySite()`](/docs/cloudrun/deploysite) to deploy a Remotion project.\n\n### `composition`\n\nThe `id` of the [composition](/docs/composition) you want to render.\n\n### `inputProps?`\n\n[Input Props to pass to the selected composition of your video.](/docs/passing-props#passing-input-props-in-the-cli).  \nMust be a JSON object.  \nFrom the root component the props can be read using [`getInputProps()`](/docs/get-input-props).  \nYou may transform input props using [`calculateMetadata()`](/docs/calculate-metadata).\n\n### `privacy?`\n\nOne of:\n\n- `\"public\"` (_default_): The rendered still is publicly accessible under the Cloud Storage URL.\n- `\"private\"`: The rendered still is not publicly available, but is available within the GCP project to those with the correct permissions.\n\n### `downloadBehavior?`<AvailableFrom v=\"4.0.176\"/>\n\nHow the output file should behave when accessed through the Cloud Storage output link in the browser.\n\n- `{\"type\": \"play-in-browser\"}` - the default. The video will play in the browser.\n- `{\"type\": \"download\", fileName: null}` or `{\"type\": \"download\", fileName: \"download.mp4\"}` - a `Content-Disposition` header will be added which makes the browser download the file. You can optionally override the filename.\n\n### `forceBucketName?`\n\nSpecify a specific bucket name to be used for the output. The resulting Google Cloud Storage URL will be in the format `gs://{bucket-name}/renders/{render-id}/{file-name}`. If not set, Remotion will choose the right bucket to use based on the region.\n\n### `jpegQuality?`\n\nSee [`renderStill() -> jpegQuality`](/docs/renderer/render-still#jpegquality).\n\n### `imageFormat?`\n\nSee [`renderStill() -> imageFormat`](/docs/renderer/render-still#imageformat).\n\n### `scale?`\n\n<Options id=\"scale\" />\n\n### `envVariables?`\n\nSee [`renderStill() -> envVariables`](/docs/renderer/render-still#envvariables).\n\n### `frame?`\n\nWhich frame of the composition should be rendered. Frames are zero-indexed, and negative values are allowed, with -1 being the last frame.\n\n### `chromiumOptions?`\n\nAllows you to set certain Chromium / Google Chrome flags. See: [Chromium flags](/docs/chromium-flags).\n\n#### `disableWebSecurity`\n\n_boolean - default `false`_\n\nThis will most notably disable CORS among other security features.\n\n#### `ignoreCertificateErrors`\n\n_boolean - default `false`_\n\nResults in invalid SSL certificates, such as self-signed ones, being ignored.\n\n#### `gl`\n\n<Options id=\"gl\" />\n\n### `forceWidth?`\n\nOverrides default composition width.\n\n### `forceHeight?`\n\nOverrides default composition height.\n\n### `forceFps?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition FPS.\n\n### `forceDurationInFrames?`<AvailableFrom v=\"4.0.424\" />\n\nOverrides the default composition duration in frames.\n\n### `logLevel?`\n\n<Options id=\"log\" />\n\n### `outName?`\n\nThe file name of the still output.\n\nIt can either be:\n\n- `undefined` - it will default to `out` plus the appropriate file extension, for example: `renders/${renderId}/out.mp4`.\n- A `string` - it will get saved to the same Cloud Storage bucket as your site under the key `renders/{renderId}/{outName}`. Make sure to include the file extension at the end of the string.\n\n### `delayRenderTimeoutInMilliseconds?`\n\nA number describing how long the render may take to resolve all [`delayRender()`](/docs/delay-render) calls [before it times out](/docs/timeout). Default: `30000`\n\n### `mediaCacheSizeInBytes?`<AvailableFrom v=\"4.0.352\"/>\n\n<Options id=\"media-cache-size-in-bytes\" />\n\n### `offthreadVideoCacheSizeInBytes?`<AvailableFrom v=\"4.0.23\"/>\n\n<Options id=\"offthreadvideo-cache-size-in-bytes\" />\n\n### `offthreadVideoThreads`<AvailableFrom v=\"4.0.261\"/>\n\n<Options id=\"offthreadvideo-video-threads\" />\n\n## Return value\n\nReturns a promise resolving to an object containing the following:\n\n### `renderId`\n\nA unique alphanumeric identifier for this render. Useful for obtaining status and finding the relevant files in the Cloud Storage bucket.\n\n### `bucketName`\n\nThe Cloud Storage bucket name in which all files are being saved.\n\n### `privacy`\n\nPrivacy of the output file, either:\n\n- \"public-read\" - Publicly accessible under the Cloud Storage URL.\n- \"project-private\" - Not publicly available, but is available within the GCP project to those with the correct permissions.\n\n### `publicUrl`\n\nIf the privacy is set to public, this will be the publicly accessible URL of the rendered file. If the privacy is not public, this will be null.\n\n### `cloudStorageUri`\n\nGoogle Storage path, beginning with `gs://{bucket-name}`. Can be used with the [gsutil](https://cloud.google.com/storage/docs/gsutil) CLI tool.\n\n### `size`\n\nSize of the rendered still in KB.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/render-still-on-cloudrun.ts)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Kicks off a still rendering process on Remotion Cloud Run.

Requires a [service](/docs/cloudrun/deployservice) to already be deployed to execute the render.

A [site](/docs/cloudrun/deploysite) or a [Serve URL](/docs/terminology/serve-url) needs to be specified to determine what will be rendered.

## Example[​](#example)

```
import {renderStillOnCloudrun} from '@remotion/cloudrun/client';

const result = await renderStillOnCloudrun({
  region: 'us-east1',
  serviceName: 'remotion-render-bds9aab',
  composition: 'MyStill',
  imageFormat: 'png',
  serveUrl: 'https://storage.googleapis.com/remotioncloudrun-123asd321/sites/abcdefgh',
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