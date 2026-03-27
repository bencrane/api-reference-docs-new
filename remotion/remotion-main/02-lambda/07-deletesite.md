---
title: "deleteSite()"
url: "https://www.remotion.dev/docs/lambda/deletesite"
path: "/docs/lambda/deletesite"
---

"---\nimage: /generated/articles-docs-lambda-deletesite.png\nid: deletesite\ntitle: deleteSite()\nslug: /lambda/deletesite\ncrumb: 'Lambda API'\n---\n\nRemoves a Remotion project from your S3 bucket.\n\nEach project is located in the `sites/` subdirectory of your S3 bucket. Calling this function is equivalent of deleting all files inside a subfolder of your `sites/` subdirectory.\n\n## Example\n\nGets all sites and deletes them.\n\n```ts twoslash\nimport {AwsRegion, deleteSite, getSites} from '@remotion/lambda';\n\nconst region: AwsRegion = 'eu-central-1';\n\nconst {sites} = await getSites({\n  region,\n});\n\nfor (const site of sites) {\n  await deleteSite({\n    bucketName: site.bucketName,\n    siteName: site.id,\n    region,\n  });\n  console.log(`Site ${site.id} deleted.`);\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\n_string_\n\nThe [AWS region](/docs/lambda/region-selection) where the project resides in.\n\n### `bucketName`\n\n_string_\n\nThe name of the S3 bucket in which your site resides in.\n\n### `siteName`\n\n_string_\n\nThe unique ID of the project you want to delete.\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n## Return value\n\nA promise resolving to an object with the following property:\n\n### `totalSizeInBytes`\n\n_number_\n\nThe amount of space that was freed by deleting the project.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-site.ts)\n- [getSites()](/docs/lambda/getsites)\n- [deploySite()](/docs/lambda/deploysite)\n"

Removes a Remotion project from your S3 bucket.

Each project is located in the `sites/` subdirectory of your S3 bucket. Calling this function is equivalent of deleting all files inside a subfolder of your `sites/` subdirectory.

## Example[​](#example)

Gets all sites and deletes them.

```
import {AwsRegion, deleteSite, getSites} from '@remotion/lambda';

const region: AwsRegion = 'eu-central-1';

const {sites} = await getSites({
  region,
});

for (const site of sites) {
  await deleteSite({
    bucketName: site.bucketName,
    siteName: site.id,
    region,
  });
  console.log(`Site ${site.id} deleted.`);
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

*string*

The [AWS region](/docs/lambda/region-selection) where the project resides in.

### `bucketName`[​](#bucketname)

*string*

The name of the S3 bucket in which your site resides in.

### `siteName`[​](#sitename)

*string*

The unique ID of the project you want to delete.

### `forcePathStyle?`[v4.0.202](https://github.com/remotion-dev/remotion/releases/v4.0.202)[​](#forcepathstyle)

Passes `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.

## Return value[​](#return-value)

A promise resolving to an object with the following property:

### `totalSizeInBytes`[​](#totalsizeinbytes)

*number*

The amount of space that was freed by deleting the project.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/delete-site.ts)

- [getSites()](/docs/lambda/getsites)

- [deploySite()](/docs/lambda/deploysite)
](/docs/lambda/deploysite)](/docs/lambda/deploysite)
](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)
- ](/docs/lambda/deploysite)