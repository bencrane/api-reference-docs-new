---
title: "getOrCreateBucket()"
url: "https://www.remotion.dev/docs/lambda/getorcreatebucket"
path: "/docs/lambda/getorcreatebucket"
---

"---\nimage: /generated/articles-docs-lambda-getorcreatebucket.png\nid: getorcreatebucket\ntitle: getOrCreateBucket()\nslug: /lambda/getorcreatebucket\ncrumb: 'Lambda API'\n---\n\nCreates a bucket for Remotion Lambda in your S3 account. If one already exists, it will get returned instead.\n\n**Only 1 bucket per region** is necessary for Remotion Lambda to function.\n\n```ts twoslash\nimport {getOrCreateBucket} from '@remotion/lambda';\n\nconst {bucketName} = await getOrCreateBucket({region: 'us-east-1'});\n\nconsole.log(bucketName); // \"remotionlambda-32df3p\"\n```\n\n## Arguments\n\nAn object with the following property:\n\n### `region`\n\nThe [AWS region](/docs/lambda/region-selection) which you want to create a bucket in.\n\n### `enableFolderExpiry`<AvailableFrom v=\"4.0.32\" />\n\n<Options id=\"enable-folder-expiry\" />\n\n### ~~`onBucketEnsured`~~\n\n_removed in v4.0_\n\nAllows to pass a callback after the bucket was created and before the S3 website option was enabled. This option exists so the CLI can better visualize the progress.  \nRemoved in v4.0 since we don't use the website option anymore.\n\n### `forcePathStyle?`<AvailableFrom v=\"4.0.202\" />\n\nPasses `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.\n\n## Return value\n\nA promise resolving to an object with the following properties:\n\n### `bucketName`\n\nThe name of your bucket that was found or created.\n\n### `alreadyExisted`<AvailableFrom v=\"3.3.78\" />\n\nA boolean indicating whether the bucket already existed or was newly created.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-or-create-bucket.ts)\n- [getFunctions()](/docs/lambda/getfunctions)\n"

Creates a bucket for Remotion Lambda in your S3 account. If one already exists, it will get returned instead.

**Only 1 bucket per region** is necessary for Remotion Lambda to function.

```
import {getOrCreateBucket} from '@remotion/lambda';

const {bucketName} = await getOrCreateBucket({region: 'us-east-1'});

console.log(bucketName); // "remotionlambda-32df3p"Copy
```

## Arguments[​](#arguments)

An object with the following property:

### `region`[​](#region)

The [AWS region](/docs/lambda/region-selection) which you want to create a bucket in.

### `enableFolderExpiry`[v4.0.32](https://github.com/remotion-dev/remotion/releases/v4.0.32)[​](#enablefolderexpiry)

When deploying sites, enable or disable S3 Lifecycle policies which allow for renders to auto-delete after a certain time. Default is `null`, which does not change any lifecycle policies of the S3 bucket. See: [Lambda autodelete](/docs/lambda/autodelete).

### `onBucketEnsured`[​](#onbucketensured)

*removed in v4.0*

Allows to pass a callback after the bucket was created and before the S3 website option was enabled. This option exists so the CLI can better visualize the progress.

Removed in v4.0 since we don't use the website option anymore.

### `forcePathStyle?`[v4.0.202](https://github.com/remotion-dev/remotion/releases/v4.0.202)[​](#forcepathstyle)

Passes `forcePathStyle` to the AWS S3 client. If you don't know what this is, you probably don't need it.

## Return value[​](#return-value)

A promise resolving to an object with the following properties:

### `bucketName`[​](#bucketname)

The name of your bucket that was found or created.

### `alreadyExisted`[v3.3.78](https://github.com/remotion-dev/remotion/releases/v3.3.78)[​](#alreadyexisted)

A boolean indicating whether the bucket already existed or was newly created.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/lambda/src/api/get-or-create-bucket.ts)

- [getFunctions()](/docs/lambda/getfunctions)
](/docs/lambda/getfunctions)](/docs/lambda/getfunctions)
](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)
- ](/docs/lambda/getfunctions)