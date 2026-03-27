---
title: "@remotion/cloudrun"
url: "https://www.remotion.dev/docs/cloudrun/api"
path: "/docs/cloudrun/api"
---

"---\nimage: /generated/articles-docs-cloudrun-api.png\ntitle: '@remotion/cloudrun'\ncrumb: 'Render videos without servers on GCP'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nimport {TableOfContents} from './table-of-contents';\n\n<Installation pkg=\"@remotion/cloudrun\" />\n<br />\n\n**See the [setup guide](/docs/cloudrun/setup) for complete instructions on how to get started.**\n\n## APIs\n\nThe following Node.JS are available:\n\n<TableOfContents />\n\n## CLI\n\nSee [here](/docs/cloudrun/cli) for a list of CLI commands.\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

- Remotion CLI
- npm
- bun
- pnpm
- yarn

```

npx remotion add @remotion/cloudrunCopy
```

```

npm i --save-exact @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

pnpm i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

bun i @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

```

yarn --exact add @remotion/[[email protected]](/cdn-cgi/l/email-protection)Copy
```
This assumes you are currently using v4.0.441 of Remotion.
Also update `remotion` and all ``@remotion/*`` packages to the same version.
Remove all `^` character in front of the version numbers of it as it can lead to a version conflict.

**See the [setup guide](/docs/cloudrun/setup) for complete instructions on how to get started.**

## APIs[​](#apis)

The following Node.JS are available:

[
**getServiceInfo()**
Gets information about a service](/docs/cloudrun/getserviceinfo)[
**deployService()**
Create a new service in GCP Cloud Run](/docs/cloudrun/deployservice)[
**deleteService()**
Delete a service in GCP Cloud Run](/docs/cloudrun/deleteservice)[
**getServices()**
Lists available Remotion Cloud Run services](/docs/cloudrun/getservices)[
**speculateServiceName()**
Speculate a service name based on its configuration](/docs/cloudrun/speculateservicename)[
**getRegions()**
Get all available regions](/docs/cloudrun/getregions)[
**deploySite()**
Bundle and upload a site to Cloud Storage](/docs/cloudrun/deploysite)[
**deleteSite()**
Delete a bundle from Cloud Storage](/docs/cloudrun/deletesite)[
**getSites()**
Get all available sites from Cloud Storage](/docs/cloudrun/getsites)[
**getOrCreateBucket()**
Ensure a Remotion Cloud Storage bucket exists](/docs/cloudrun/getorcreatebucket)[
**renderMediaOnCloudrun()**
Trigger a video or audio render](/docs/cloudrun/rendermediaoncloudrun)[
**renderStillOnCloudrun()**
Trigger a still render](/docs/cloudrun/renderstilloncloudrun)[
**testPermissions()**
Ensure permissions are correctly set up in GCP](/docs/cloudrun/testpermissions)

## CLI[​](#cli)

See [here](/docs/cloudrun/cli) for a list of CLI commands.](/docs/cloudrun/cli)](/docs/cloudrun/cli)
](/docs/cloudrun/cli)
- ](/docs/cloudrun/cli)