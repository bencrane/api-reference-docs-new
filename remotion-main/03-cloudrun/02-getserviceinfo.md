---
title: "getServiceInfo()"
url: "https://www.remotion.dev/docs/cloudrun/getserviceinfo"
path: "/docs/cloudrun/getserviceinfo"
---

"---\nimage: /generated/articles-docs-cloudrun-getServiceinfo.png\nid: getserviceinfo\ntitle: getServiceInfo()\nslug: /cloudrun/getserviceinfo\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nGets information about a service given its name and region.\n\nTo get a list of deployed services, use [`getServices()`](/docs/cloudrun/getservices).\n\nTo deploy a service, use [`deployService()`](/docs/cloudrun/deployservice).\n\n## Example\n\n```ts twoslash\nimport {getServiceInfo} from '@remotion/cloudrun/client';\n\nconst info = await getServiceInfo({\n  region: 'us-east1',\n  serviceName: 'remotion--3-3-82--mem512mi--cpu1-0--t-500',\n});\nconsole.log(info.serviceName); // remotion--3-3-82--mem512mi--cpu1-0--t-500\nconsole.log(info.timeoutInSeconds); // 500\nconsole.log(info.memoryLimit); // \"2Gi\"\nconsole.log(info.cpuLimit); // \"1.0\"\nconsole.log(info.remotionVersion); // '4.0.1'\nconsole.log(info.uri); // \"https://remotion--3-3-82--mem512mi--cpu1-0--t-500-1a2b3c4d5e-ue.a.run.app\"\nconsole.log(info.region); // \"us-east1\"\nconsole.log(info.consoleUrl); // \"https://console.cloud.google.com/run/detail/us-east1/remotion--3-3-82--mem512mi--cpu1-0--t-500/logs\"\n```\n\n:::note\nImport from [`@remotion/cloudrun/client`](/docs/cloudrun/light-client) to not import the whole renderer, which cannot be bundled.\n:::\n\n## Arguments\n\nAn object containing the following properties:\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) the service resides in.\n\n### `serviceName`\n\nThe name of the service.\n\n## Return value\n\nIf the service does not exist, an error is thrown by the GCP SDK.\nIf the service exists, a promise resolving to an object with the following properties is returned:\n\n### `memoryLimit`\n\nThe upper bound on the amount of RAM that the Cloud Run service can consume.\n\n### `cpuLimit`\n\nThe maximum number of CPU cores that the Cloud Run service can use to process requests.\n\n### `remotionVersion`\n\nThe Remotion version of the service. Remotion is versioning the Cloud Run service and a render can only be triggered from a version of `@remotion/cloudrun` that is matching the one of the service.\n\n### `timeoutInSeconds`\n\nThe timeout that has been assigned to the Cloud Run service.\n\n### `uri`\n\nThe endpoint of the service.\n\n### `region`\n\nThe region of the deployed service.\n\n### `consoleUrl`\n\nA link to the GCP console page for this service. Specifically, a link to logs display.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-service-info.ts)\n- [`getServices()`](/docs/cloudrun/getservices)\n- [`deployService()`](/docs/cloudrun/deployservice)\n- [`deleteService()`](/docs/cloudrun/deleteservice)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Gets information about a service given its name and region.

To get a list of deployed services, use [`getServices()`](/docs/cloudrun/getservices).

To deploy a service, use [`deployService()`](/docs/cloudrun/deployservice).

## Example[​](#example)

```
import {getServiceInfo} from '@remotion/cloudrun/client';

const info = await getServiceInfo({
  region: 'us-east1',
  serviceName: 'remotion--3-3-82--mem512mi--cpu1-0--t-500',
});
console.log(info.serviceName); // remotion--3-3-82--mem512mi--cpu1-0--t-500
console.log(info.timeoutInSeconds); // 500
console.log(info.memoryLimit); // "2Gi"
console.log(info.cpuLimit); // "1.0"
console.log(info.remotionVersion); // '4.0.1'
console.log(info.uri); // "https://remotion--3-3-82--mem512mi--cpu1-0--t-500-1a2b3c4d5e-ue.a.run.app"
console.log(info.region); // "us-east1"
console.log(info.consoleUrl); // "https://console.cloud.google.com/run/detail/us-east1/remotion--3-3-82--mem512mi--cpu1-0--t-500/logs"Copy
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
- ](#example)
- ](#example)
- ](#example)
- ](#example)