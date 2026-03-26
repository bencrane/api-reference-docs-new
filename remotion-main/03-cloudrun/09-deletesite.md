---
title: "deleteSite()"
url: "https://www.remotion.dev/docs/cloudrun/deletesite"
path: "/docs/cloudrun/deletesite"
---

"---\nimage: /generated/articles-docs-cloudrun-deletesite.png\nid: deletesite\ntitle: deleteSite()\nslug: /cloudrun/deletesite\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nRemoves a Remotion project from your Cloud Storage bucket.\n\nEach project is located in the `sites/` subdirectory of your Cloud Storage bucket. Calling this function is equivalent of deleting all files inside a subfolder of your `sites/` subdirectory.\n\n## Example\n\nGets all sites and deletes them.\n\n```ts twoslash\nimport {GcpRegion, deleteSite, getSites} from '@remotion/cloudrun';\n\nconst region: GcpRegion = 'australia-southeast1';\n\nconst {sites} = await getSites(region);\n\nfor (const site of sites) {\n  await deleteSite({\n    bucketName: site.bucketName,\n    siteName: site.id,\n  });\n  console.log(`Site ${site.id} deleted.`);\n}\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `bucketName`\n\n_string_\n\nThe name of the Cloud Storage bucket in which your site resides in.\n\n### `siteName`\n\n_string_\n\nThe unique ID of the project you want to delete.\n\n## Return value\n\nA promise resolving nothing.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/delete-site.ts)\n- [getSites()](/docs/cloudrun/getsites)\n- [deploySite()](/docs/cloudrun/deploysite)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Removes a Remotion project from your Cloud Storage bucket.

Each project is located in the `sites/` subdirectory of your Cloud Storage bucket. Calling this function is equivalent of deleting all files inside a subfolder of your `sites/` subdirectory.

## Example[​](#example)

Gets all sites and deletes them.

```
import {GcpRegion, deleteSite, getSites} from '@remotion/cloudrun';

const region: GcpRegion = 'australia-southeast1';

const {sites} = await getSites(region);

for (const site of sites) {
  await deleteSite({
    bucketName: site.bucketName,
    siteName: site.id,
  });
  console.log(`Site ${site.id} deleted.`);
}Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `bucketName`[​](#bucketname)

*string*

The name of the Cloud Storage bucket in which your site resides in.

### `siteName`[​](#sitename)

*string*

The unique ID of the project you want to delete.

## Return value[​](#return-value)

A promise resolving nothing.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/delete-site.ts)

- [getSites()](/docs/cloudrun/getsites)

- [deploySite()](/docs/cloudrun/deploysite)
](/docs/cloudrun/deploysite)](/docs/cloudrun/deploysite)
](/docs/cloudrun/deploysite)
- ](/docs/cloudrun/deploysite)
- ](/docs/cloudrun/deploysite)
- ](/docs/cloudrun/deploysite)
- ](/docs/cloudrun/deploysite)
- ](/docs/cloudrun/deploysite)