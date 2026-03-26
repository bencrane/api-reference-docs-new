---
title: "getOrCreateBucket()"
url: "https://www.remotion.dev/docs/cloudrun/getorcreatebucket"
path: "/docs/cloudrun/getorcreatebucket"
---

"---\nimage: /generated/articles-docs-cloudrun-getorcreatebucket.png\nid: getorcreatebucket\ntitle: getOrCreateBucket()\nslug: /cloudrun/getorcreatebucket\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nCreates a Cloud Storage bucket for Remotion Cloud Run in your GCP project. If one already exists, it will get returned instead.\n\n**Only 1 bucket per region** is necessary for Remotion Cloud Run to function.\n\n```ts twoslash\nimport {getOrCreateBucket} from '@remotion/cloudrun';\n\nconst {bucketName, alreadyExisted} = await getOrCreateBucket({\n  region: 'us-east1',\n});\n\nconsole.log(bucketName); // \"remotioncloudrun-32df3p\"\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) which you want to create a bucket in.\n\n### `updateBucketState?`\n\nCallback function that returns a state (_string_) of operation. Used by the CLI to provide a progress update. State will be one of the following;\n\n- Checking for existing bucket\n- Creating new bucket\n- Created bucket\n- Using existing bucket\n\n## Return value\n\nA promise resolving to an object with the following properties:\n\n### `bucketName`\n\nThe name of your bucket that was found or created.\n\n### `alreadyExisted`\n\nA boolean indicating whether the bucket already existed or was newly created.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-or-create-bucket.ts)\n- [getServices()](/docs/cloudrun/getservices)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Creates a Cloud Storage bucket for Remotion Cloud Run in your GCP project. If one already exists, it will get returned instead.

**Only 1 bucket per region** is necessary for Remotion Cloud Run to function.

```
import {getOrCreateBucket} from '@remotion/cloudrun';

const {bucketName, alreadyExisted} = await getOrCreateBucket({
  region: 'us-east1',
});

console.log(bucketName); // "remotioncloudrun-32df3p"Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [GCP region](/docs/cloudrun/region-selection) which you want to create a bucket in.

### `updateBucketState?`[​](#updatebucketstate)

Callback function that returns a state (*string*) of operation. Used by the CLI to provide a progress update. State will be one of the following;

- Checking for existing bucket

- Creating new bucket

- Created bucket

- Using existing bucket

## Return value[​](#return-value)

A promise resolving to an object with the following properties:

### `bucketName`[​](#bucketname)

The name of your bucket that was found or created.

### `alreadyExisted`[​](#alreadyexisted)

A boolean indicating whether the bucket already existed or was newly created.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-or-create-bucket.ts)

- [getServices()](/docs/cloudrun/getservices)
](/docs/cloudrun/getservices)](/docs/cloudrun/getservices)
](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)
- ](/docs/cloudrun/getservices)