---
title: "getServices()"
url: "https://www.remotion.dev/docs/cloudrun/getservices"
path: "/docs/cloudrun/getservices"
---

"---\nimage: /generated/articles-docs-cloudrun-getservices.png\ntitle: getServices()\nid: getservices\nslug: /cloudrun/getservices\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nRetrieves a list of Remotion services deployed to GCP Cloud Run.\n\nThe parameter `compatibleOnly` determines whether only services that are compatible with the installed version of Remotion Cloud Run should be returned.\n\n:::note\nThe Cloud Run service is versioned and the version of the service must match the version of the `@remotion/cloudrun` package. So if you upgrade Remotion, you should deploy a new service or otherwise you might get an empty array from this function.\n:::\n\nTo get information about only a single service, use [`getServiceInfo()`](/docs/cloudrun/getserviceinfo).\n\nIf you are sure that a service exists, you can also guess the name of it using [`speculateServiceName()`](/docs/cloudrun/speculateservicename) and save an API call to Cloud Run.\n\n## Example\n\n```ts twoslash\nimport {getServices} from '@remotion/cloudrun/client';\n\nconst info = await getServices({\n  region: 'us-east1',\n  compatibleOnly: true,\n});\n\nfor (const service of info) {\n  console.log(service.serviceName); // \"remotion--3-3-82--mem512mi--cpu1-0\"\n  console.log(service.timeoutInSeconds); // 300\n  console.log(service.memoryLimit); // 512Mi\n  console.log(service.cpuLimit); // 1.0\n  console.log(service.remotionVersion); // \"4.0.1\"\n  console.log(service.uri); // \"https://remotion--3-3-82--mem512mi--cpu1-0--t-300-1a2b3c4d5e-ue.a.run.app\"\n  console.log(service.region); // \"us-east1\"\n  console.log(service.consoleUrl); // \"https://console.cloud.google.com/run/detail/us-east1/remotion--3-3-82--mem512mi--cpu1-0--t-300/logs\"\n}\n```\n\n:::note\nImport from [`@remotion/cloudrun/client`](/docs/cloudrun/light-client) to not import the whole renderer, which cannot be bundled.\n:::\n\n## Argument\n\nAn object containing the following properties:\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) that you would like to query.\n\n```ts twoslash\nimport {getServices} from '@remotion/cloudrun';\n\nconst info = await getServices({\n  region: 'us-west1',\n  compatibleOnly: true,\n});\n\nfor (const service of info) {\n  console.log(service.serviceName); // \"remotion--3-3-82--mem2gi--cpu2--t-1100\"\n  console.log(service.timeoutInSeconds); // 1100\n  console.log(service.memoryLimit); // 2Gi\n  console.log(service.cpuLimit); // 2\n  console.log(service.remotionVersion); // \"3.3.82\"\n  console.log(service.uri); // \"https://remotion--3-3-82--mem2gi--cpu2--t-1100-1a2b3c4d5e-uw.a.run.app\"\n  console.log(service.region); // \"us-west1\"\n  console.log(service.consoleUrl); // \"https://console.cloud.google.com/run/detail/us-west1/remotion--3-3-82--mem2gi--cpu2--t-1100/logs\"\n}\n```\n\n### `compatibleOnly`\n\nIf `true`, only services that match the version of the current Remotion Cloud run package are returned. If `false`, all Remotion services are returned.\n\n## Return value\n\nA promise resolving to an **array of objects** with the following properties:\n\n### `serviceName`\n\nThe name of the service.\n\n### `memoryLimit`\n\nThe upper bound on the amount of RAM that the Cloud Run service can consume.\n\n### `cpuLimit`\n\nThe maximum number of CPU cores that the Cloud Run service can use to process requests.\n\n### `remotionVersion`\n\nThe Remotion version of the service. Remotion is versioning the Cloud Run service and a render can only be triggered from a version of `@remotion/cloudrun` that is matching the one of the service.\n\n### `timeoutInSeconds`\n\nThe timeout that has been assigned to the Cloud Run service.\n\n### `uri`\n\nThe endpoint of the service.\n\n### `region`\n\nThe region of the deployed service. Useful if passing 'all regions' to the region input.\n\n### `consoleUrl`\n\nA link to the GCP console page for this service. Specifically, a link to logs display.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/get-services.ts)\n- [`getServiceInfo()`](/docs/cloudrun/getserviceinfo)\n- [`deployService()`](/docs/cloudrun/deployservice)\n- [`deleteService()`](/docs/cloudrun/deleteservice)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Retrieves a list of Remotion services deployed to GCP Cloud Run.

The parameter `compatibleOnly` determines whether only services that are compatible with the installed version of Remotion Cloud Run should be returned.
](/docs/cloudrun/status)](/docs/cloudrun/status)
](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)
- ](/docs/cloudrun/status)