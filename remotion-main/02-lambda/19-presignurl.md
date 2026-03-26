---
title: "presignUrl()"
url: "https://www.remotion.dev/docs/lambda/presignurl"
path: "/docs/lambda/presignurl"
---

"---\nimage: /generated/articles-docs-lambda-presignurl.png\nid: presignurl\ntitle: presignUrl()\ncrumb: 'Lambda API'\n---\n\nTakes a private S3 object and turns it into a public URL by signing with your AWS credentials.\n\n## Example\n\n```ts twoslash\nimport {presignUrl} from '@remotion/lambda/client';\n\nconst url = await presignUrl({\n  region: 'us-east-1',\n  bucketName: 'remotionlambda-c7fsl3d',\n  objectKey: 'assets/sample.png',\n  expiresInSeconds: 900,\n  checkIfObjectExists: true,\n});\n\nconsole.log(url); // `string` - or `null` if object doesn't exist\n\nconst url2 = await presignUrl({\n  region: 'us-east-1',\n  bucketName: 'remotionlambda-c7fsl3d',\n  objectKey: 'assets/sample.png',\n  expiresInSeconds: 900,\n  checkIfObjectExists: false,\n});\n\nconsole.log(url); // always a string, or exception if object doesn't exist\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` (available from v3.3.42) to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe AWS region in which the bucket resides.\n\n### `bucketName`\n\nThe bucket where the asset exists. The bucket must have been created by Remotion Lambda.\n\n### `objectKey`\n\nThey key that uniquely identifies the object stored in the bucket.\n\n### `expiresInSeconds`\n\nThe number of seconds before the presigned URL expires.\nMust be an integer and `>=1` and `<=604800` (maximum of 7 days as enforced by AWS)\n\n### `checkIfObjectExists`\n\nWhether the function should check if the object exists in the bucket before generating the presigned url. Default `false`.\n\nIf the object does not exist and `checkIfObjectExists` is:\n\n- `true`, then `null` is returned\n- `false`, then an exception is thrown\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/presign-url.ts)\n- [`downloadMedia()`](/docs/lambda/downloadmedia)\n"

Takes a private S3 object and turns it into a public URL by signing with your AWS credentials.

## Example[​](#example)

```
import {presignUrl} from '@remotion/lambda/client';

const url = await presignUrl({
  region: 'us-east-1',
  bucketName: 'remotionlambda-c7fsl3d',
  objectKey: 'assets/sample.png',
  expiresInSeconds: 900,
  checkIfObjectExists: true,
});

console.log(url); // `string` - or `null` if object doesn't exist

const url2 = await presignUrl({
  region: 'us-east-1',
  bucketName: 'remotionlambda-c7fsl3d',
  objectKey: 'assets/sample.png',
  expiresInSeconds: 900,
  checkIfObjectExists: false,
});

console.log(url); // always a string, or exception if object doesn't existCopy
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