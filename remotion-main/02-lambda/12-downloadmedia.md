---
title: "downloadMedia()"
url: "https://www.remotion.dev/docs/lambda/downloadmedia"
path: "/docs/lambda/downloadmedia"
---

"---\nimage: /generated/articles-docs-lambda-downloadmedia.png\nid: downloadmedia\ntitle: downloadMedia()\nslug: /lambda/downloadmedia\ncrumb: 'Lambda API'\n---\n\nDownloads a rendered video, audio or still to the disk of the machine this API is called from.\n\nIf you want to let the user download a result to their machine, use [`renderMediaOnLambda()` -> `downloadBehavior`](/docs/lambda/rendermediaonlambda#downloadbehavior) instead.\n\n```ts twoslash\nimport {downloadMedia} from '@remotion/lambda';\n\nconst {outputPath, sizeInBytes} = await downloadMedia({\n  bucketName: 'remotionlambda-r42fs9fk',\n  region: 'us-east-1',\n  renderId: '8hfxlw',\n  outPath: 'out.mp4',\n  onProgress: ({totalSize, downloaded, percent}) => {\n    console.log(`Download progress: ${totalSize}/${downloaded} bytes (${(percent * 100).toFixed(0)}%)`);\n  },\n});\n\nconsole.log(outputPath); // \"/Users/yourname/remotion-project/out.mp4\"\nconsole.log(sizeInBytes); // 21249541\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) in which the render has performed.\n\n### `bucketName`\n\nThe bucket name in which the render was stored. This should be the same variable you used for [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).\n\n### `renderId`\n\nThe ID of the render. You can retrieve this ID by calling [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).\n\n### `outPath`\n\nWhere the video should be saved. Pass an absolute path, or it will be resolved relative to your current working directory.\n\n### `onProgress?`\n\nCallback function that gets called with the following properties:\n\n- `totalSize` in bytes\n- `downloaded` number of bytes downloaded\n- `percent` relative progress between 0 and 1\n\n### `customCredentials?`<AvailableFrom v=\"3.2.23\" />\n\nIf the render was saved to a [different cloud](/docs/lambda/custom-destination#saving-to-another-cloud), pass an object with the same `endpoint`, `accessKeyId` and `secretAccessKey` as you passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#outname) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#outname).\n\n### `signal?`<AvailableFrom v=\"4.0.406\" />\n\nAn [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) that allows the download to be cancelled.\n\n## Return value\n\nReturns a promise resolving to an object with the following properties:\n\n### `outputPath`\n\nThe absolute path of where the file got saved.\n\n### `sizeInBytes`\n\nThe size of the file in bytes.\n\n## Compatibility\n\n<CompatibilityTable chrome={false} firefox={false} safari={false} nodejs={true} bun={true} serverlessFunctions={false} clientSideRendering={false} serverSideRendering={false} player={false} studio={false} />\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/download-media.ts)\n- [renderMediaOnLambda()](/docs/lambda/rendermediaonlambda)\n- [renderStillOnLambda()](/docs/lambda/renderstillonlambda)\n"

Downloads a rendered video, audio or still to the disk of the machine this API is called from.

If you want to let the user download a result to their machine, use [`renderMediaOnLambda()` -> `downloadBehavior`](/docs/lambda/rendermediaonlambda#downloadbehavior) instead.

```
import {downloadMedia} from '@remotion/lambda';

const {outputPath, sizeInBytes} = await downloadMedia({
  bucketName: 'remotionlambda-r42fs9fk',
  region: 'us-east-1',
  renderId: '8hfxlw',
  outPath: 'out.mp4',
  onProgress: ({totalSize, downloaded, percent}) => {
    console.log(`Download progress: ${totalSize}/${downloaded} bytes (${(percent * 100).toFixed(0)}%)`);
  },
});

console.log(outputPath); // "/Users/yourname/remotion-project/out.mp4"
console.log(sizeInBytes); // 21249541Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) in which the render has performed.

### `bucketName`[​](#bucketname)

The bucket name in which the render was stored. This should be the same variable you used for [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).

### `renderId`[​](#renderid)

The ID of the render. You can retrieve this ID by calling [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).

### `outPath`[​](#outpath)

Where the video should be saved. Pass an absolute path, or it will be resolved relative to your current working directory.

### `onProgress?`[​](#onprogress)

Callback function that gets called with the following properties:

- `totalSize` in bytes

- `downloaded` number of bytes downloaded

- `percent` relative progress between 0 and 1

### `customCredentials?`[v3.2.23](https://github.com/remotion-dev/remotion/releases/v3.2.23)[​](#customcredentials)

If the render was saved to a [different cloud](/docs/lambda/custom-destination#saving-to-another-cloud), pass an object with the same `endpoint`, `accessKeyId` and `secretAccessKey` as you passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#outname) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#outname).

### `signal?`[v4.0.406](https://github.com/remotion-dev/remotion/releases/v4.0.406)[​](#signal)

An [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal) that allows the download to be cancelled.

## Return value[​](#return-value)

Returns a promise resolving to an object with the following properties:

### `outputPath`[​](#outputpath)

The absolute path of where the file got saved.

### `sizeInBytes`[​](#sizeinbytes)

The size of the file in bytes.

## Compatibility[​](#compatibility)

|  Browsers Servers Environments
|  
Chrome 
Firefox 
Safari 
Node.js 
Bun 
Serverless Functions 
[Client-side rendering](/docs/client-side-rendering) 
[Server-side rendering](/docs/ssr) 
[Player](/docs/player) 
[Studio](/docs/studio)
|  
 
 
 
 
 
 
 
 
 

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/download-media.ts)

- [renderMediaOnLambda()](/docs/lambda/rendermediaonlambda)

- [renderStillOnLambda()](/docs/lambda/renderstillonlambda)
](/docs/lambda/renderstillonlambda)](/docs/lambda/renderstillonlambda)
](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)
- ](/docs/lambda/renderstillonlambda)