---
title: "deleteRender()"
url: "https://www.remotion.dev/docs/lambda/deleterender"
path: "/docs/lambda/deleterender"
---

"---\nimage: /generated/articles-docs-lambda-deleterender.png\nid: deleterender\ntitle: deleteRender()\nslug: /lambda/deleterender\ncrumb: 'Lambda API'\n---\n\nDeletes a rendered video, audio or still and its associated metada.\n\n```ts twoslash\nimport {deleteRender} from '@remotion/lambda';\n\nconst {freedBytes} = await deleteRender({\n  bucketName: 'remotionlambda-r42fs9fk',\n  region: 'us-east-1',\n  renderId: '8hfxlw',\n});\n\nconsole.log(freedBytes); // 21249541\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) in which the render has performed.\n\n### `bucketName`\n\nThe bucket name in which the render was stored. This should be the same variable you used for [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).\n\n### `renderId`\n\nThe ID of the render. You can retrieve this ID by calling [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).\n\n### `customCredentials?`<AvailableFrom v=\"3.2.23\" />\n\nIf the render was saved to a [different cloud](/docs/lambda/custom-destination#saving-to-another-cloud), pass an object with the same `endpoint`, `accessKeyId` and `secretAccessKey` as you passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#outname) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#outname).\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n## Return value\n\nReturns a promise resolving to an object with the following properties:\n\n### `freedBytes`\n\nThe amount of bytes that were removed from the S3 bucket.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)\n"

Deletes a rendered video, audio or still and its associated metada.

```
import {deleteRender} from '@remotion/lambda';

const {freedBytes} = await deleteRender({
  bucketName: 'remotionlambda-r42fs9fk',
  region: 'us-east-1',
  renderId: '8hfxlw',
});

console.log(freedBytes); // 21249541Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) in which the render has performed.

### `bucketName`[​](#bucketname)

The bucket name in which the render was stored. This should be the same variable you used for [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).

### `renderId`[​](#renderid)

The ID of the render. You can retrieve this ID by calling [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda).

### `customCredentials?`[v3.2.23](https://github.com/remotion-dev/remotion/releases/v3.2.23)[​](#customcredentials)

If the render was saved to a [different cloud](/docs/lambda/custom-destination#saving-to-another-cloud), pass an object with the same `endpoint`, `accessKeyId` and `secretAccessKey` as you passed to [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda#outname) or [`renderStillOnLambda()`](/docs/lambda/renderstillonlambda#outname).

### `forcePathStyle?`[v4.0.202](https://github.com/remotion-dev/remotion/releases/v4.0.202)[​](#forcepathstyle)

Passes `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.

## Return value[​](#return-value)

Returns a promise resolving to an object with the following properties:

### `freedBytes`[​](#freedbytes)

The amount of bytes that were removed from the S3 bucket.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)
- ](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-render.ts)