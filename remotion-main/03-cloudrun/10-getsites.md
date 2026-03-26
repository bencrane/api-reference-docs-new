---
title: "getSites()"
url: "https://www.remotion.dev/docs/cloudrun/getsites"
path: "/docs/cloudrun/getsites"
---

"---\nimage: /generated/articles-docs-cloudrun-getsites.png\nid: getsites\ntitle: getSites()\nslug: /cloudrun/getsites\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nGets an array of Remotion projects in Cloud Storage, in your GCP project.\n\nThe projects are located in the `sites/` subdirectory of your Cloud Storage bucket. Remember - you should only have one bucket for Remotion Cloud Run per region, therefore you do not need to specify the name of the bucket for this function.\n\n## Example\n\nGets all sites and logs information about them.\n\n```ts twoslash\nimport {getSites} from '@remotion/cloudrun';\n\nconst {sites, buckets} = await getSites('europe-west4');\n\nfor (const site of sites) {\n  console.log(site.id); // A unique ID for referring to that project\n  console.log(site.bucketName); // In which bucket the site resides in.\n  console.log(site.bucketRegion); // In which region the bucket resides in.\n  console.log(site.serveUrl); // URL of the deployed site that you can pass to `renderMediaOnCloudRun()`\n}\n\nfor (const bucket of buckets) {\n  console.log(bucket.name); // The name of the Cloud Storage bucket.\n  console.log(bucket.creationDate); // A unix timestamp of when the site was created.\n  console.log(bucket.region); // 'europe-west4'\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) which you want to query. Alternatively, you can pass 'all regions' to return sites across all regions.\n\n```ts twoslash\nimport {getSites} from '@remotion/cloudrun';\n\nconst {sites, buckets} = await getSites('all regions');\n```\n\n## Return value\n\nA promise resolving to an object with the following properties:\n\n### `sites`\n\nAn array of deployed Remotion projects that you can use for rendering.\n\nEach item contains the following properties:\n\n#### `id`\n\nA unique identifier for that project.\n\n#### `bucketName`\n\nThe bucket in which the project resides in.\n\n#### `bucketRegion`\n\nThe region in which the bucket resides in.\n\n#### `serveUrl`\n\nURL of the deployed site. You can pass it into [`renderMediaOnCloudRun()`](/docs/cloudrun/rendermediaoncloudrun) to render a video or audio.\n\n### `buckets`\n\nAn array of all buckets in the selected region in your account that start with `remotioncloudrun-`.\n\n:::info\nYou should only have [1 bucket](/docs/cloudrun/multiple-buckets) per region for all your Remotion projects.\n:::\n\nEach item contains the following properties:\n\n#### `region`\n\nThe region the bucket resides in.\n\n#### `name`\n\nThe name of the bucket. Cloud Storage buckets have globally unique names.\n\n#### `creationDate`\n\nA UNIX timestamp of the point when the bucket was first created.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-sites.ts)\n- [deleteSite()](/docs/cloudrun/deletesite)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Gets an array of Remotion projects in Cloud Storage, in your GCP project.

The projects are located in the `sites/` subdirectory of your Cloud Storage bucket. Remember - you should only have one bucket for Remotion Cloud Run per region, therefore you do not need to specify the name of the bucket for this function.

## Example[​](#example)

Gets all sites and logs information about them.

```
import {getSites} from '@remotion/cloudrun';

const {sites, buckets} = await getSites('europe-west4');

for (const site of sites) {
  console.log(site.id); // A unique ID for referring to that project
  console.log(site.bucketName); // In which bucket the site resides in.
  console.log(site.bucketRegion); // In which region the bucket resides in.
  console.log(site.serveUrl); // URL of the deployed site that you can pass to `renderMediaOnCloudRun()`
}

for (const bucket of buckets) {
  console.log(bucket.name); // The name of the Cloud Storage bucket.
  console.log(bucket.creationDate); // A unix timestamp of when the site was created.
  console.log(bucket.region); // 'europe-west4'
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `region`[​](#region)

The [GCP region](/docs/cloudrun/region-selection) which you want to query. Alternatively, you can pass 'all regions' to return sites across all regions.

```
import {getSites} from '@remotion/cloudrun';

const {sites, buckets} = await getSites('all regions');Copy
```

## Return value[​](#return-value)

A promise resolving to an object with the following properties:

### `sites`[​](#sites)

An array of deployed Remotion projects that you can use for rendering.

Each item contains the following properties:

#### `id`[​](#id)

A unique identifier for that project.

#### `bucketName`[​](#bucketname)

The bucket in which the project resides in.

#### `bucketRegion`[​](#bucketregion)

The region in which the bucket resides in.

#### `serveUrl`[​](#serveurl)

URL of the deployed site. You can pass it into [`renderMediaOnCloudRun()`](/docs/cloudrun/rendermediaoncloudrun) to render a video or audio.

### `buckets`[​](#buckets)

An array of all buckets in the selected region in your account that start with `remotioncloudrun-`.
](#buckets)](#buckets)
](#buckets)
- ](#buckets)
- ](#buckets)
- ](#buckets)
- ](#buckets)
- ](#buckets)
- ](#buckets)