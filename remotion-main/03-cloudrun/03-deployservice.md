---
title: "deployService()"
url: "https://www.remotion.dev/docs/cloudrun/deployservice"
path: "/docs/cloudrun/deployservice"
---

"---\nimage: /generated/articles-docs-cloudrun-deployservice.png\nid: deployservice\ntitle: deployService()\nslug: /cloudrun/deployservice\ncrumb: 'Cloud Run API'\n---\n\n<ExperimentalBadge>\n  <p>\n    Cloud Run is in <a href=\"/docs/cloudrun/status\">Alpha status and not actively being developed.</a>\n  </p>\n</ExperimentalBadge>\n\nCreates a [GCP Cloud Run](https://cloud.google.com/run) service in your GCP project that will be able to render a video in the cloud.\n\nIf a service with the same Remotion version, memory limit, cpu limit and timeout already existed in the specified region, it will be returned instead without a new one being created. This means this service can be treated as idempotent.\n\n## Example\n\n```ts twoslash\nimport {deployService} from '@remotion/cloudrun';\n\nconst {shortName} = await deployService({\n  memoryLimit: '2Gi',\n  cpuLimit: '2.0',\n  timeoutSeconds: 500,\n  projectID: 'my-remotion-project',\n  region: 'us-east1',\n});\nconsole.log(shortName);\n```\n\n## Arguments\n\nAn object with the following properties:\n\n### `memoryLimit`\n\nThe upper bound on the amount of RAM that the Cloud Run service can consume. By default we recommend a value of 2GiB. You may increase or decrease it depending on how memory-consuming your video is. The minimum allowed number is `512MiB`, the maximum allowed number is `32GiB`. Since the costs of Remotion Cloud Run is directly proportional to the amount of RAM, we recommend to keep this amount as low as possible. As the Memory limit is raised, there is a [corresponding minimum CPU Limit](https://cloud.google.com/run/docs/configuring/memory-limits#cpu-minimum) that must be observed.\n\n### `cpuLimit`\n\nThe maximum number of CPU cores that the Cloud Run service can use to process requests. The default is 1. As the CPU limit is raised, there is a [corresponding minimum Memory Limit](https://cloud.google.com/run/docs/configuring/cpu#setting) that must be observed.\n\n### `minInstances`\n\nThe minimum number of service instances to have available, regardless of requests. The default is 0. Some users may wish to increase the minimum instances so that renders are started faster, though this would only reduce cold start time for simultaneous renders up to that minimum limit. [Read more about the minimum instance limit here](/docs/cloudrun/instancecount#minimum-instance-count)\n\n:::warning\nAny running instances, even if they are not performing a render, will be billable in GCP. The default minimum number of instances is zero, which means that when no requests are made to your service, you are not billed.\n:::\n\n### `maxInstances`\n\nThe maximum number of service instances that can be create by GCP in response to incoming requests. The default is 100. [Read more about the maximum instance limit here](/docs/cloudrun/instancecount#maximum-instance-count)\n\n### `timeoutSeconds`\n\nHow long the Cloud Run Service may run before it gets killed. Must be below 3600 seconds.\n\n### `projectID`\n\nThe [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#:~:text=to%20be%20unique.-,Project%20ID,-%3A%20A%20globally%20unique) of the GCP Project that has been configured for Remotion Cloud Run.\n\n### `region`\n\nThe [GCP region](/docs/cloudrun/region-selection) which you want to deploy the Cloud Run Service too.\n\n### `performImageVersionValidation`\n\nDefault as true. This will validate that an image exists in the public Artifact Registry that matches the Remotion Version you are trying to deploy. Can be set false for a potential time saving.\n\n### `onlyAllocateCpuDuringRequestProcessing`<AvailableFrom v=\"4.0.221\" />\n\nIf this is set to true, `cpu_idle` will be set to `true` in the service manifest.  \nCPU alloction will be disabled while no request is being processed, which can lead to significant cost savings.\n\n## Return value\n\nAn object with the following values:\n\n- `fullName` (_string_): The full name of the service just created, in the form `projects/{projectId}/locations/{region}/services/{serviceName}`.\n- `shortName` (_string_): The name of the service just created, as it appears in the console.\n- `uri` (_string_): The endpoint of the service just created.\n- `alreadyExists`: (_boolean_): Whether the creation was skipped because the service already existed.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/cloudrun/src/api/deploy-service.ts)\n- [CLI equivalent: npx remotion cloudrun services deploy](/docs/cloudrun/cli/services/deploy)\n- [deleteService()](/docs/cloudrun/deleteservice)\n- [getServices()](/docs/cloudrun/getservices)\n"

EXPERIMENTAL

Cloud Run is in [Alpha status and not actively being developed.](/docs/cloudrun/status)

Creates a [GCP Cloud Run](https://cloud.google.com/run) service in your GCP project that will be able to render a video in the cloud.

If a service with the same Remotion version, memory limit, cpu limit and timeout already existed in the specified region, it will be returned instead without a new one being created. This means this service can be treated as idempotent.

## Example[​](#example)

```
import {deployService} from '@remotion/cloudrun';

const {shortName} = await deployService({
  memoryLimit: '2Gi',
  cpuLimit: '2.0',
  timeoutSeconds: 500,
  projectID: 'my-remotion-project',
  region: 'us-east1',
});
console.log(shortName);Copy
```

## Arguments[​](#arguments)

An object with the following properties:

### `memoryLimit`[​](#memorylimit)

The upper bound on the amount of RAM that the Cloud Run service can consume. By default we recommend a value of 2GiB. You may increase or decrease it depending on how memory-consuming your video is. The minimum allowed number is `512MiB`, the maximum allowed number is `32GiB`. Since the costs of Remotion Cloud Run is directly proportional to the amount of RAM, we recommend to keep this amount as low as possible. As the Memory limit is raised, there is a [corresponding minimum CPU Limit](https://cloud.google.com/run/docs/configuring/memory-limits#cpu-minimum) that must be observed.

### `cpuLimit`[​](#cpulimit)

The maximum number of CPU cores that the Cloud Run service can use to process requests. The default is 1. As the CPU limit is raised, there is a [corresponding minimum Memory Limit](https://cloud.google.com/run/docs/configuring/cpu#setting) that must be observed.

### `minInstances`[​](#mininstances)

The minimum number of service instances to have available, regardless of requests. The default is 0. Some users may wish to increase the minimum instances so that renders are started faster, though this would only reduce cold start time for simultaneous renders up to that minimum limit. [Read more about the minimum instance limit here](/docs/cloudrun/instancecount#minimum-instance-count)
](/docs/cloudrun/instancecount#minimum-instance-count)](/docs/cloudrun/instancecount#minimum-instance-count)
](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)
- ](/docs/cloudrun/instancecount#minimum-instance-count)