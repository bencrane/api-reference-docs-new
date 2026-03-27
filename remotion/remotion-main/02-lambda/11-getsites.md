---
title: "getSites()"
url: "https://www.remotion.dev/docs/lambda/getsites"
path: "/docs/lambda/getsites"
---

"---\nimage: /generated/articles-docs-lambda-getsites.png\nid: getsites\ntitle: getSites()\nslug: /lambda/getsites\ncrumb: 'Lambda API'\n---\n\nGets an array of Remotion projects in your S3 account.\n\nThe projects are located in the `sites/` subdirectory of your S3 bucket. Remember - you should only have one bucket for Remotion Lambda per region, therefore you do not need to specify the name of the bucket for this function.\n\n## Example\n\nGets all sites and logs information about them.\n\n```ts twoslash\nimport {getSites} from '@remotion/lambda/client';\n\nconst {sites, buckets} = await getSites({\n  region: 'eu-central-1',\n});\n\nfor (const site of sites) {\n  console.log(site.id); // A unique ID for referring to that project\n  console.log(site.bucketName); // In which bucket the site resides in.\n  console.log(site.lastModified); // A unix timestamp, but may also be null\n  console.log(site.sizeInBytes); // Size of all contents in the folder\n  console.log(site.serveUrl); // URL of the deployed site that you can pass to `renderMediaOnLambda()`\n  console.log(site.version); // The Remotion version of the site, or null\n}\n\nfor (const bucket of buckets) {\n  console.log(bucket.region); // 'eu-central-1'\n  console.log(bucket.name); // The name of the S3 bucket.\n  console.log(bucket.creationDate); // A unix timestamp of when the site was created.\n}\n```\n\n:::note\nPreferrably import this function from `@remotion/lambda/client` (available from v3.3.42) to avoid problems [inside serverless functions](/docs/lambda/light-client).\n:::\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) which you want to query.\n\n### `forceBucketName?`<AvailableFrom v=\"3.3.102\"/>\n\nSpecify a specific bucket name to be used. [This is not recommended](/docs/lambda/multiple-buckets), instead let Remotion discover the right bucket automatically.\n\n### `compatibleOnly?`<AvailableFrom v=\"4.0.435\"/>\n\nIf `true`, only sites whose Remotion version matches the installed version of `@remotion/lambda` are returned. If `false` or not provided, all sites are returned.\n\n## Return value\n\nA promise resolving to an object with the following properties:\n\n### `sites`\n\nAn array of deployed Remotion projects that you can use for rendering.\n\nEach item contains the following properties:\n\n#### `id`\n\nA unique identifier for that project.\n\n#### `bucketName`\n\nThe bucket in which the project resides in.\n\n#### `lastModified`\n\nWhen the files in that project were last changed.\n\n#### `sizeInBytes`\n\nThe combined size of all files in that project.\n\n#### `serveUrl`\n\nURL of the deployed site. You can pass it into [`renderMediaOnLambda()`](/docs/lambda/rendermediaonlambda) to render a video or audio.\n\n#### `version`<AvailableFrom v=\"4.0.435\"/>\n\nThe Remotion version of the site, or `null` if the version could not be determined.\n\n### `buckets`\n\nAn array of all buckets in the selected region in your account that start with `remotionlambda-`.\n\n:::info\nYou should only have [1 bucket](/docs/lambda/multiple-buckets) per region for all your Remotion projects. Nonetheless `buckets` is an array, since we cannot prevent you from manually creating additional buckets with the `remotionlambda-` prefix.\n:::\n\nEach item contains the following properties:\n\n#### `region`\n\nThe region the bucket resides in.\n\n#### `name`\n\nThe name of the bucket. S3 buckets have globally unique names.\n\n#### `creationDate`\n\nA UNIX timestamp of the point when the bucket was first created.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-sites.ts)\n- [deleteSite()](/docs/lambda/deletesite)\n"

Gets an array of Remotion projects in your S3 account.

The projects are located in the `sites/` subdirectory of your S3 bucket. Remember - you should only have one bucket for Remotion Lambda per region, therefore you do not need to specify the name of the bucket for this function.

## Example[​](#example)

Gets all sites and logs information about them.

```
import {getSites} from '@remotion/lambda/client';

const {sites, buckets} = await getSites({
  region: 'eu-central-1',
});

for (const site of sites) {
  console.log(site.id); // A unique ID for referring to that project
  console.log(site.bucketName); // In which bucket the site resides in.
  console.log(site.lastModified); // A unix timestamp, but may also be null
  console.log(site.sizeInBytes); // Size of all contents in the folder
  console.log(site.serveUrl); // URL of the deployed site that you can pass to `renderMediaOnLambda()`
  console.log(site.version); // The Remotion version of the site, or null
}

for (const bucket of buckets) {
  console.log(bucket.region); // 'eu-central-1'
  console.log(bucket.name); // The name of the S3 bucket.
  console.log(bucket.creationDate); // A unix timestamp of when the site was created.
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